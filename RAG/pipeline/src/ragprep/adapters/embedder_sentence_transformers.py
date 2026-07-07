"""Local embedding adapter using sentence-transformers (Apache-2.0).

Default model BAAI/bge-small-en-v1.5 runs fully locally and free. BGE models
recommend a query instruction prefix for asymmetric search, applied here.
"""
from __future__ import annotations

from typing import Sequence


class SentenceTransformersEmbedder:
    def __init__(
        self,
        model: str = "BAAI/bge-small-en-v1.5",
        query_prefix: str = "",
    ) -> None:
        # imported lazily so the rest of the pipeline can run without the model
        from sentence_transformers import SentenceTransformer

        self._model = SentenceTransformer(model)
        self._query_prefix = query_prefix

    def embed_documents(self, texts: Sequence[str]) -> list[list[float]]:
        vectors = self._model.encode(
            list(texts), normalize_embeddings=True, show_progress_bar=False
        )
        return [v.tolist() for v in vectors]

    def embed_query(self, text: str) -> list[float]:
        vector = self._model.encode(
            self._query_prefix + text, normalize_embeddings=True, show_progress_bar=False
        )
        return vector.tolist()
