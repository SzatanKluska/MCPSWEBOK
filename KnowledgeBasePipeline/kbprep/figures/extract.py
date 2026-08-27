"""Extract SWEBOK figure images (Figure N.M) to JPG, per chapter.

Renders each page with pypdfium2 (BSD) and crops the figure region, whose
bounds are derived from the caption position plus the surrounding vector
graphics (lines/rects/curves) and label chars. No AGPL dependencies.

The crop geometry per figure (page, column, top-bound source) is authored by
hand in `<figures_extract_dir>/<source_id>.yaml` — see
`data/figures_extract/swebok-v4-ch1.yaml` for the format. This module is the
extraction *engine*; it has no chapter-specific data of its own.

Usage (from KnowledgeBasePipeline, with the venv Python):
  python -m kbprep.figures.extract --source swebok-v4-ch2
  python -m kbprep.figures.extract --all
  python -m kbprep.figures.extract --pdf path/to.pdf --out dir --figures-config path/to.yaml
"""
from __future__ import annotations

import argparse
import glob
import os

import pdfplumber
import pypdfium2 as pdfium
import yaml

_CONFIG = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")

DEFAULT_DPI = 200
DEFAULT_PAD = 8.0      # points of padding around the detected box
DEFAULT_HEADER = 40.0  # skip running header at the top of the page


def caption_box(page, fig_id, xlo, xhi):
    """Bounding box (x0, top, x1, bottom) of the (possibly 2-line) caption."""
    words = page.extract_words()
    num = fig_id  # e.g. "2.1"
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


def figure_box(page, fig_id, column, top_src, prev_caption, *, pad: float, header: float):
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
        top_bound = header
    elif top_src.startswith("after:"):
        top_bound = prev_caption[3] + 2
    else:  # "top"
        top_bound = 0.0

    def in_col(o):
        cx = (o["x0"] + o["x1"]) / 2
        return xlo - 1 <= cx <= xhi + 1

    graphics = [
        o for o in (page.lines + page.rects + page.curves + page.images)
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
    else:
        # No vector/raster graphics found (e.g. a figure that's a text/code
        # listing): fall back to the text content between top_bound and the
        # caption.
        words = [
            w for w in page.extract_words()
            if in_col(w) and w["top"] >= top_bound - 1 and w["bottom"] <= cap[1] + 1
        ]
        if words:
            boxes.append(union([(w["x0"], w["top"], w["x1"], w["bottom"]) for w in words]))

    x0, top, x1, bottom = union(boxes)
    x0 = max(0.0, x0 - pad)
    top = max(0.0, top - pad)
    x1 = min(page.width, x1 + pad)
    bottom = min(page.height, bottom + pad)
    return (x0, top, x1, bottom), cap


def load_figures_config(path: str) -> dict:
    """Load a `<figures_extract_dir>/<source_id>.yaml` crop config.

    Format:
      dpi: 200        # optional, defaults to DEFAULT_DPI
      pad: 8.0        # optional
      header: 40.0    # optional
      figures:
        - id: "2.1"
          page: 0          # 0-based page index
          column: full     # left | right | full
          top: header      # header | top | after:<fig_id>
    """
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    figures = [
        (str(item["id"]), int(item["page"]), item["column"], item["top"])
        for item in data.get("figures", [])
    ]
    return {
        "dpi": data.get("dpi", DEFAULT_DPI),
        "pad": data.get("pad", DEFAULT_PAD),
        "header": data.get("header", DEFAULT_HEADER),
        "figures": figures,
    }


def extract_figures(
    pdf_path: str,
    out_dir: str,
    figures: list[tuple[str, int, str, str]],
    *,
    dpi: float = DEFAULT_DPI,
    pad: float = DEFAULT_PAD,
    header: float = DEFAULT_HEADER,
) -> list[dict]:
    """Crop each (fig_id, page_idx, column, top_src) in `figures` out of
    `pdf_path` into `out_dir` as `figure-<id>.jpg`. Returns per-figure results."""
    os.makedirs(out_dir, exist_ok=True)
    scale = dpi / 72.0
    results = []
    pdf = pdfium.PdfDocument(pdf_path)
    prev_caption: dict[str, tuple[float, float, float, float]] = {}
    with pdfplumber.open(pdf_path) as plumb:
        for fig_id, page_idx, column, top_src in figures:
            page = plumb.pages[page_idx]
            prev = prev_caption.get(top_src.split(":")[-1]) if top_src.startswith("after:") else None
            box, cap = figure_box(page, fig_id, column, top_src, prev, pad=pad, header=header)
            prev_caption[fig_id] = cap

            bitmap = pdf[page_idx].render(scale=scale)
            img = bitmap.to_pil().convert("RGB")
            crop = img.crop(tuple(round(v * scale) for v in box))
            out_name = f"figure-{fig_id.replace('.', '-')}.jpg"
            out_path = os.path.join(out_dir, out_name)
            crop.save(out_path, "JPEG", quality=90)
            result = {
                "id": fig_id, "page": page_idx, "box": tuple(round(v, 1) for v in box),
                "out_path": out_path, "width": crop.width, "height": crop.height,
            }
            results.append(result)
            print(f"Figure {fig_id}: page {page_idx + 1}  box={result['box']}  "
                  f"-> {out_path}  ({crop.width}x{crop.height})")
    return results


def _pdf_for_source(raw_materials_dir: str, source_id: str) -> str:
    matches = glob.glob(os.path.join(raw_materials_dir, "**", f"{source_id}.pdf"), recursive=True)
    if not matches:
        raise FileNotFoundError(f"No PDF for source '{source_id}' under {raw_materials_dir}")
    return matches[0]


def _load_pipeline_config():
    from ..shared.config import load_config
    return load_config(os.path.normpath(_CONFIG))


def _run_source(cfg, source_id: str) -> None:
    raw_materials = cfg.path("paths", "raw_materials")
    figures_extract_dir = cfg.path("paths", "figures_extract")
    out_dir = os.path.join(cfg.path("paths", "knowledge_base"), "figures")

    pdf_path = _pdf_for_source(raw_materials, source_id)
    config_path = os.path.join(figures_extract_dir, f"{source_id}.yaml")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"No figure-extraction config for '{source_id}': expected {config_path}")

    fc = load_figures_config(config_path)
    print(f"=== {source_id}: {len(fc['figures'])} figure(s) ===")
    extract_figures(
        pdf_path, out_dir, fc["figures"],
        dpi=fc["dpi"], pad=fc["pad"], header=fc["header"],
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pdf", help="Path to the source PDF (direct mode)")
    parser.add_argument("--out", help="Output directory for cropped JPGs (direct mode)")
    parser.add_argument("--figures-config", help="Path to a figure-extraction YAML config (direct mode)")
    parser.add_argument("--source", help="Source id (e.g. swebok-v4-ch2); resolves paths via config.yaml")
    parser.add_argument("--all", action="store_true", help="Run every source with a config in paths.figures_extract")
    args = parser.parse_args()

    if args.all:
        cfg = _load_pipeline_config()
        figures_extract_dir = cfg.path("paths", "figures_extract")
        for config_path in sorted(glob.glob(os.path.join(figures_extract_dir, "*.yaml"))):
            source_id = os.path.splitext(os.path.basename(config_path))[0]
            _run_source(cfg, source_id)
    elif args.source:
        cfg = _load_pipeline_config()
        _run_source(cfg, args.source)
    elif args.pdf and args.out and args.figures_config:
        fc = load_figures_config(args.figures_config)
        extract_figures(args.pdf, args.out, fc["figures"], dpi=fc["dpi"], pad=fc["pad"], header=fc["header"])
    else:
        parser.error("either --source, --all, or all of --pdf/--out/--figures-config are required")


if __name__ == "__main__":
    main()
