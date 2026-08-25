"""Composition root: builds each concrete adapter from `config.yaml`.

The only place in the pipeline that knows adapter classes exist. Every builder
returns a `ports` protocol, which is what keeps `core` free of adapter imports.
"""

from .factory import (
    build_chunker,
    build_cleaner,
    build_embedder,
    build_extractor,
    build_taxonomy_mapper,
    build_vector_store,
)

__all__ = [
    "build_chunker",
    "build_cleaner",
    "build_embedder",
    "build_extractor",
    "build_taxonomy_mapper",
    "build_vector_store",
]
