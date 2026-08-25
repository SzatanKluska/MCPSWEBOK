"""PDF extraction adapter built on pdfplumber (MIT).

Handles the two challenges of the SWEBOK PDF:
  * two-column layout  -> each page is split at mid-x and columns read L->R
  * figure/diagram garbage -> characters below `min_font_size` are dropped
Headings are detected via the Semibold font used by SWEBOK section titles.
"""
from __future__ import annotations

import pdfplumber

from ..models import Document, Page, Line

_HEADING_FONT_HINTS = ("Semibold", "Bold")
_TITLE_FONT_HINT = "Montserrat"


class PdfPlumberExtractor:
    def __init__(self, min_font_size: float = 8.5, two_column: bool = True) -> None:
        self.min_font_size = min_font_size
        self.two_column = two_column

    def extract(self, path: str, source_id: str) -> Document:
        doc = Document(
            source_id=source_id,
            source_path=path,
            source_type="pdf",
        )
        with pdfplumber.open(path) as pdf:
            for i, page in enumerate(pdf.pages, start=1):
                doc.pages.append(self._extract_page(page, i))
        return doc

    def _extract_page(self, page, number: int) -> Page:
        mid_x = page.width / 2
        columns = [(0, mid_x), (mid_x, page.width)] if self.two_column else [(0, page.width)]
        result = Page(number=number)
        for col_idx, (x0, x1) in enumerate(columns):
            words = page.extract_words(
                extra_attrs=["fontname", "size"],
                use_text_flow=False,
                keep_blank_chars=False,
            )
            # keep words whose center falls in this column and above size threshold
            col_words = [
                w for w in words
                if x0 <= (w["x0"] + w["x1"]) / 2 < x1 and w["size"] >= self.min_font_size
            ]
            result.lines.extend(self._group_lines(col_words, number, col_idx))
        return result

    def _group_lines(self, words, page_number: int, column: int) -> list[Line]:
        """Group words into lines by their vertical position (top)."""
        lines: list[Line] = []
        current: list[dict] = []
        last_top: float | None = None
        for w in sorted(words, key=lambda w: (round(w["top"], 0), w["x0"])):
            top = w["top"]
            if last_top is None or abs(top - last_top) <= 3:
                current.append(w)
            else:
                lines.append(self._finalize_line(current, page_number, column))
                current = [w]
            last_top = top
        if current:
            lines.append(self._finalize_line(current, page_number, column))
        return [ln for ln in lines if ln.text.strip()]

    def _finalize_line(self, words, page_number: int, column: int) -> Line:
        words_sorted = sorted(words, key=lambda w: w["x0"])
        text = " ".join(w["text"] for w in words_sorted)
        sizes = [w["size"] for w in words_sorted]
        fonts = [w["fontname"] for w in words_sorted]
        size = max(sizes)
        font = fonts[0]
        is_heading = self._is_heading(text, size, fonts)
        return Line(
            text=text,
            page=page_number,
            column=column,
            top=min(w["top"] for w in words_sorted),
            size=size,
            font=font,
            is_heading=is_heading,
        )

    @staticmethod
    def _is_heading(text: str, size: float, fonts: list[str]) -> bool:
        emphasized = any(h in f for f in fonts for h in _HEADING_FONT_HINTS)
        big_title = size >= 14 and any(_TITLE_FONT_HINT in f for f in fonts)
        return bool(emphasized or big_title)
