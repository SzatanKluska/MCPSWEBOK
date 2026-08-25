"""Port protocols: the technology-agnostic contracts `core` is written against.

Re-exported here so callers write `from ..ports import Chunker` rather than
reaching into the module file directly.
"""

from .ports import (
    Chunker,
    DocumentExtractor,
    Embedder,
    TaxonomyMapper,
    TextCleaner,
    VectorStore,
)

__all__ = [
    "Chunker",
    "DocumentExtractor",
    "Embedder",
    "TaxonomyMapper",
    "TextCleaner",
    "VectorStore",
]
