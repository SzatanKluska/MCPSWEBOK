"""One-off script: split swebok-v4.pdf into per-KA chapter PDFs.

Page ranges (1-indexed, inclusive) determined by scanning for "CHAPTER NN"
headings in the full guide. Run once from KnowledgeBasePipeline/ with the venv
python. Safe to re-run (overwrites outputs).
"""
from __future__ import annotations

import os

from pypdf import PdfReader, PdfWriter

SOURCE = "SourceBooks/swebok/swebok-v4.pdf"
OUT_ROOT = "RawMaterials/swebok"

CHAPTERS = [
    (1, "Software Requirements", 43, 66),
    (2, "Software Architecture", 67, 82),
    (3, "Software Design", 83, 98),
    (4, "Software Construction", 99, 116),
    (5, "Software Testing", 117, 150),
    (6, "Software Engineering Operations", 151, 166),
    (7, "Software Maintenance", 167, 184),
    (8, "Software Configuration Management", 185, 201),
    (9, "Software Engineering Management", 202, 220),
    (10, "Software Engineering Process", 221, 232),
    (11, "Software Engineering Models and Methods", 233, 245),
    (12, "Software Quality", 246, 263),
    (13, "Software Security", 264, 273),
    (14, "Software Engineering Professional Practice", 274, 287),
    (15, "Software Engineering Economics", 288, 311),
    (16, "Computing Foundations", 312, 344),
    (17, "Mathematical Foundations", 345, 366),
    (18, "Engineering Foundations", 367, 411),
]


def main() -> None:
    reader = PdfReader(SOURCE)
    assert len(reader.pages) == 411, f"expected 411 pages, got {len(reader.pages)}"

    for num, name, start, end in CHAPTERS:
        if num == 1:
            continue  # already exists (chapter1/swebok-v4-ch1.pdf), left untouched
        writer = PdfWriter()
        for p in range(start - 1, end):  # 0-indexed, inclusive of end
            writer.add_page(reader.pages[p])
        out_dir = os.path.join(OUT_ROOT, f"chapter{num}")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"swebok-v4-ch{num}.pdf")
        with open(out_path, "wb") as fh:
            writer.write(fh)
        print(f"chapter {num:2d} ({name}): pages {start}-{end} ({end - start + 1}p) -> {out_path}")


if __name__ == "__main__":
    main()
