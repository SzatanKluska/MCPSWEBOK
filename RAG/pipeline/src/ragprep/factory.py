"""Factory: builds concrete adapters from config (dependency injection point).

This is the ONLY place that knows about concrete implementations. The core
pipeline receives ports and never imports an adapter directly.
"""
from __future__ import annotations

import yaml

from .config import Config
from .ports import DocumentExtractor, TextCleaner, TaxonomyMapper, Chunker, Embedder, VectorStore


def build_extractor(cfg: Config) -> DocumentExtractor:
    ex = cfg["extractor"]
    if ex["provider"] == "pdfplumber":
        from .adapters.pdf_pdfplumber import PdfPlumberExtractor
        return PdfPlumberExtractor(
            min_font_size=ex.get("min_font_size", 8.5),
            two_column=ex.get("two_column", True),
        )
    raise ValueError(f"Unknown extractor provider: {ex['provider']}")


def build_cleaner(cfg: Config) -> TextCleaner:
    cl = cfg["cleaner"]
    if cl["provider"] == "basic":
        from .adapters.cleaner_basic import BasicCleaner
        return BasicCleaner(drop_patterns=cl.get("drop_patterns"))
    raise ValueError(f"Unknown cleaner provider: {cl['provider']}")


def build_taxonomy_mapper(cfg: Config) -> TaxonomyMapper:
    from .adapters.taxonomy_swebok import SwebokTaxonomyMapper
    return SwebokTaxonomyMapper(cfg.path("paths", "taxonomy"))


def build_chunker(cfg: Config) -> Chunker:
    ch = cfg["chunker"]
    if ch["provider"] == "structure":
        from .adapters.chunker_structure import StructureChunker
        with open(cfg.path("paths", "taxonomy"), encoding="utf-8") as fh:
            tax = yaml.safe_load(fh)
        return StructureChunker(
            ka_id=tax["ka_id"],
            ka_name=tax["ka_name"],
            max_tokens=ch.get("max_tokens", 350),
            overlap_tokens=ch.get("overlap_tokens", 50),
            min_chunk_tokens=ch.get("min_chunk_tokens", 20),
        )
    raise ValueError(f"Unknown chunker provider: {ch['provider']}")


def build_embedder(cfg: Config) -> Embedder:
    em = cfg["embedder"]
    if em["provider"] == "sentence_transformers":
        from .adapters.embedder_sentence_transformers import SentenceTransformersEmbedder
        return SentenceTransformersEmbedder(
            model=em.get("model", "BAAI/bge-small-en-v1.5"),
            query_prefix=em.get("query_prefix", ""),
        )
    raise ValueError(f"Unknown embedder provider: {em['provider']}")


def build_vector_store(cfg: Config) -> VectorStore:
    vs = cfg["vector_store"]
    if vs["provider"] == "numpy":
        from .adapters.vectorstore_numpy import NumpyVectorStore
        return NumpyVectorStore(persist_dir=cfg.path("vector_store", "persist_dir"))
    if vs["provider"] == "chroma":
        from .adapters.vectorstore_chroma import ChromaVectorStore
        return ChromaVectorStore(
            collection=vs.get("collection", "swebok"),
            persist_dir=cfg.path("vector_store", "persist_dir"),
        )
    raise ValueError(f"Unknown vector_store provider: {vs['provider']}")
