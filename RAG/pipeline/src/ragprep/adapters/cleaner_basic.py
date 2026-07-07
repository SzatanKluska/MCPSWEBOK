"""Basic text cleaner: drops header/footer lines and repairs common artifacts."""
from __future__ import annotations

import re
import unicodedata

from ..models import Document

# de-hyphenation across line breaks: "require-\nments" -> "requirements"
_HYPHEN_BREAK = re.compile(r"(\w+)-\s+(\w+)")


class BasicCleaner:
    def __init__(self, drop_patterns: list[str] | None = None) -> None:
        self.drop_res = [re.compile(p) for p in (drop_patterns or [])]

    def clean(self, document: Document) -> Document:
        for page in document.pages:
            kept = []
            for line in page.lines:
                text = self._normalize(line.text)
                if not text or self._should_drop(text):
                    continue
                line.text = text
                kept.append(line)
            page.lines = kept
        return document

    def _should_drop(self, text: str) -> bool:
        return any(r.search(text) for r in self.drop_res)

    @staticmethod
    def _normalize(text: str) -> str:
        text = unicodedata.normalize("NFKC", text)
        text = text.replace("\u00ad", "")            # soft hyphen
        text = text.replace("’", "'").replace("“", '"').replace("”", '"')
        text = re.sub(r"[ \t]+", " ", text).strip()
        return text
