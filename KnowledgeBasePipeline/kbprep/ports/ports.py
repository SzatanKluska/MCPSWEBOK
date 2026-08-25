"""Ports: the interfaces the pipeline core depends on.

The core orchestration knows only these Protocols — never a concrete library.
Concrete adapters are wired in at startup via the factory (dependency injection),
so swapping a technology means providing a different adapter, not editing the core.
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable, Sequence

from ..models import Document, Section, Chunk


@runtime_checkable
class DocumentExtractor(Protocol):
    """Turns a raw file (PDF/HTML/...) into a structured Document."""

    def extract(self, path: str, source_id: str) -> Document: ...


@runtime_checkable
class TextCleaner(Protocol):
    """Removes headers/footers/artifacts and normalizes text in a Document."""

    def clean(self, document: Document) -> Document: ...


@runtime_checkable
class TaxonomyMapper(Protocol):
    """Reconstructs sections and maps them to KA/topic metadata."""

    def map_sections(self, document: Document) -> list[Section]: ...


@runtime_checkable
class Chunker(Protocol):
    """Splits sections into retrieval-sized chunks with metadata."""

    def chunk(self, sections: list[Section], document: Document) -> list[Chunk]: ...


@runtime_checkable
class Embedder(Protocol):
    """Turns text into vectors. Query and document embedding may differ."""

    def embed_documents(self, texts: Sequence[str]) -> list[list[float]]: ...

    def embed_query(self, text: str) -> list[float]: ...


@runtime_checkable
class VectorStore(Protocol):
    """Persists chunk vectors and answers similarity queries."""

    def upsert(self, chunks: list[Chunk], vectors: list[list[float]]) -> None: ...

    def query(self, vector: list[float], k: int) -> list[tuple[Chunk, float]]: ...
