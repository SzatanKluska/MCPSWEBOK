"""One-off: extract SWEBOK ch.1 Figures 1.1-1.6 to JPG.

Renders each page with pypdfium2 (BSD) and crops the figure region, whose
bounds are derived from the caption position plus the surrounding vector
graphics (lines/rects/curves) and label chars. No AGPL dependencies.
"""
from __future__ import annotations

import os
import re

import pdfplumber
import pypdfium2 as pdfium

PDF = r"C:\dev\MCP Swebok\RAG\RawMaterials\swebok\chapter1\swebok-v4-ch1.pdf"
OUT = r"C:\dev\MCP Swebok\KnowledgeBase\figures"
DPI = 200
PAD = 8.0          # points of padding around the detected box
HEADER = 40.0      # skip running header at the top of the page

# (figure id, 0-based page index, column, top-bound source)
FIGURES = [
    ("1.1", 2, "full", "header"),
    ("1.2", 3, "left", "top"),
    ("1.3", 5, "left", "top"),
    ("1.4", 8, "right", "header"),
    ("1.5", 8, "right", "after:1.4"),
    ("1.6", 11, "full", "header"),
]


def caption_box(page, fig_id, xlo, xhi):
    """Bounding box (x0, top, x1, bottom) of the (possibly 2-line) caption."""
    words = page.extract_words()
    num = fig_id  # e.g. "1.1"
    for i, w in enumerate(words[:-1]):
        cx = (w["x0"] + w["x1"]) / 2
        if (
            w["text"] == "Figure"
            and words[i + 1]["text"].startswith(num + ".")
            and xlo - 1 <= cx <= xhi + 1
        ):
            anchor = w
            line = [
                x for x in words
                if anchor["top"] - 1 <= x["top"] <= anchor["top"] + 22
                and x["x0"] >= anchor["x0"] - 2
                and (x["x0"] + x["x1"]) / 2 <= xhi + 1
            ]
            x0 = min(x["x0"] for x in line)
            x1 = max(x["x1"] for x in line)
            top = anchor["top"]
            bottom = max(x["bottom"] for x in line)
            return (x0, top, x1, bottom)
    raise RuntimeError(f"caption for Figure {fig_id} not found")


def union(boxes):
    xs0 = min(b[0] for b in boxes)
    ys0 = min(b[1] for b in boxes)
    xs1 = max(b[2] for b in boxes)
    ys1 = max(b[3] for b in boxes)
    return (xs0, ys0, xs1, ys1)


def figure_box(page, fig_id, column, top_src, prev_caption):
    mid = page.width / 2
    gutter = 12  # keep the crop clear of the opposite column's text
    if column == "left":
        xlo, xhi = 0, mid - gutter
    elif column == "right":
        xlo, xhi = mid + gutter, page.width
    else:
        xlo, xhi = 0, page.width
    cap = caption_box(page, fig_id, xlo, xhi)

    if top_src == "header":
        top_bound = HEADER
    elif top_src.startswith("after:"):
        top_bound = prev_caption[3] + 2
    else:  # "top"
        top_bound = 0.0

    def in_col(o):
        cx = (o["x0"] + o["x1"]) / 2
        return xlo - 1 <= cx <= xhi + 1

    graphics = [
        o for o in (page.lines + page.rects + page.curves)
        if in_col(o) and o["bottom"] <= cap[1] + 3 and o["top"] >= top_bound - 1
    ]
    boxes = [cap]
    if graphics:
        g = union([(o["x0"], o["top"], o["x1"], o["bottom"]) for o in graphics])
        boxes.append(g)
        # include label chars just above the graphics (e.g. a root node) up to the caption
        chars = [
            c for c in page.chars
            if in_col(c) and c["top"] >= g[1] - 16 and c["bottom"] <= cap[1] + 1
        ]
        if chars:
            boxes.append(union([(c["x0"], c["top"], c["x1"], c["bottom"]) for c in chars]))

    x0, top, x1, bottom = union(boxes)
    x0 = max(0.0, x0 - PAD)
    top = max(0.0, top - PAD)
    x1 = min(page.width, x1 + PAD)
    bottom = min(page.height, bottom + PAD)
    return (x0, top, x1, bottom), cap


def main():
    os.makedirs(OUT, exist_ok=True)
    scale = DPI / 72.0
    pdf = pdfium.PdfDocument(PDF)
    prev_caption = {}
    with pdfplumber.open(PDF) as plumb:
        for fig_id, page_idx, column, top_src in FIGURES:
            page = plumb.pages[page_idx]
            prev = prev_caption.get(top_src.split(":")[-1]) if top_src.startswith("after:") else None
            box, cap = figure_box(page, fig_id, column, top_src, prev)
            prev_caption[fig_id] = cap

            bitmap = pdf[page_idx].render(scale=scale)
            img = bitmap.to_pil().convert("RGB")
            crop = img.crop(tuple(round(v * scale) for v in box))
            out_path = os.path.join(OUT, f"figure-{fig_id.replace('.', '-')}.jpg")
            crop.save(out_path, "JPEG", quality=90)
            print(f"Figure {fig_id}: page {page_idx + 1}  box={tuple(round(v,1) for v in box)}  -> {out_path}  ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
