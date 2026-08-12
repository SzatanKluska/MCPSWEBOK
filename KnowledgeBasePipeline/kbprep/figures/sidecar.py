"""Figure records: authored sidecar content joined to chunks by reference.

A source's figures are authored (by hand) in `<figures_dir>/<source_id>.yaml` —
they are pipeline input, not raw material and not a pipeline output. These
records are a side lookup (not embedded in the search index); the MCP server
attaches a figure to any retrieved chunk whose text references it
(e.g., "... shown in Figure 1.2").
"""
from __future__ import annotations

import os
import re

import yaml

from .models import Figure

_FIG_REF = re.compile(r"\bFigure\s+(\d+\.\d+)")


def figure_refs(text: str) -> list[str]:
    """Figure ids referenced in `text` (e.g. "1.2"), de-duplicated, in order."""
    seen: dict[str, None] = {}
    for m in _FIG_REF.finditer(text):
        seen.setdefault(m.group(1), None)
    return list(seen)


def load_figures(figures_dir: str, source_id: str, ka_id: str, ka_name: str) -> list[Figure]:
    """Load figure definitions from `<figures_dir>/<source_id>.yaml`."""
    sidecar = os.path.join(figures_dir, f"{source_id}.yaml")
    if not os.path.exists(sidecar):
        return []
    with open(sidecar, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    figures: list[Figure] = []
    for item in data.get("figures", []):
        mermaid = item.get("mermaid")
        figures.append(
            Figure(
                figure_id=str(item["id"]),
                caption=item["caption"],
                source_id=source_id,
                ka_id=ka_id,
                ka_name=ka_name,
                page=int(item["page"]),
                image=item["image"],
                description=item["description"].strip(),
                mermaid=mermaid.strip() if isinstance(mermaid, str) else None,
            )
        )
    return figures
