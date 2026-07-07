"""Neutral data structures that flow between pipeline stages.

These are plain dataclasses (serializable to JSON) so every stage can be run,
inspected and validated independently of the tool that produced it.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class Line:
    """A single line of text with layout attributes."""
    text: str
    page: int
    column: int
    top: float
    size: float
    font: str
    is_heading: bool = False


@dataclass
class Page:
    number: int
    lines: list[Line] = field(default_factory=list)


@dataclass
class Document:
    source_id: str
    source_path: str
    source_type: str
    pages: list[Page] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Section:
    """A logical section reconstructed from headings."""
    topic_id: str | None
    topic_name: str | None
    heading: str
    text: str
    page_start: int
    page_end: int


@dataclass
class Chunk:
    """The final RAG unit: text + metadata for retrieval and citation."""
    id: str
    text: str
    source_id: str
    source_type: str
    ka_id: str
    ka_name: str
    topic_id: str | None
    topic_name: str | None
    section_heading: str
    page_start: int
    page_end: int
    language: str
    token_count: int
    checksum: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
