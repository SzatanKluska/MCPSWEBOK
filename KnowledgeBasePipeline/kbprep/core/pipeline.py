"""Pipeline core — orchestrates stages through ports only.

Knows nothing about pdfplumber, sentence-transformers or Chroma. It receives
port implementations and drives: extract -> clean -> map -> chunk -> embed -> index.
"""
from __future__ import annotations

from dataclasses import dataclass

from ..ports import (
    DocumentExtractor, TextCleaner, TaxonomyMapper, Chunker, Embedder, VectorStore,
)
from ..models import Document, Section, Chunk
from .quality import QualityReport, extraction_gate, chunk_gate


@dataclass
class PipelineResult:
    document: Document
    sections: list[Section]
    chunks: list[Chunk]
    report: QualityReport


class Pipeline:
    def __init__(
        self,
        extractor: DocumentExtractor,
        cleaner: TextCleaner,
        mapper: TaxonomyMapper,
        chunker: Chunker,
        embedder: Embedder | None = None,
        vector_store: VectorStore | None = None,
    ) -> None:
        self.extractor = extractor
        self.cleaner = cleaner
        self.mapper = mapper
        self.chunker = chunker
        self.embedder = embedder
        self.vector_store = vector_store

    def prepare(
        self,
        path: str,
        source_id: str,
        min_extraction_ratio: float,
        min_chunk_tokens: int,
        max_chunk_tokens: int,
    ) -> PipelineResult:
        report = QualityReport()

        document = self.extractor.extract(path, source_id)
        document = self.cleaner.clean(document)
        extraction_gate(document, min_extraction_ratio, report)

        sections = self.mapper.map_sections(document)
        chunks = self.chunker.chunk(sections, document)
        chunk_gate(chunks, min_chunk_tokens, max_chunk_tokens, report)

        return PipelineResult(document, sections, chunks, report)

    def index(self, chunks: list[Chunk]) -> None:
        if self.embedder is None or self.vector_store is None:
            raise RuntimeError("Embedder and vector store are required to index.")
        vectors = self.embedder.embed_documents([c.text for c in chunks])
        self.vector_store.upsert(chunks, vectors)

    def search(self, query: str, k: int) -> list[tuple[Chunk, float]]:
        if self.embedder is None or self.vector_store is None:
            raise RuntimeError("Embedder and vector store are required to search.")
        vector = self.embedder.embed_query(query)
        return self.vector_store.query(vector, k)
