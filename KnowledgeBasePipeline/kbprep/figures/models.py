"""Figure data structure for the figures feature.

Kept out of the embedded search index; the server attaches it to hits whose
text references the figure (join by reference).
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class Figure:
    """A figure record: authored description/diagram for a source figure."""
    figure_id: str
    caption: str
    source_id: str
    ka_id: str
    ka_name: str
    page: int
    image: str
    description: str
    mermaid: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
