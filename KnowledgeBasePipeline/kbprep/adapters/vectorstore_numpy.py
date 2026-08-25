"""Pure-Python vector store adapter (numpy, BSD).

A dependency-free alternative to Chroma that needs no C++ build tools. Stores
vectors in memory, persists them to a .npz + .jsonl pair, and answers queries by
brute-force cosine similarity. Fast enough for a POC-sized corpus and proves the
ports/adapters design: swapping the vector store required no core changes.
"""
from __future__ import annotations

import json
import os

import numpy as np

from ..models import Chunk

_META_KEYS = (
    "source_id", "source_type", "ka_id", "ka_name", "topic_id", "topic_name",
    "section_heading", "page_start", "page_end", "language", "token_count", "checksum",
)


class NumpyVectorStore:
    def __init__(self, persist_dir: str) -> None:
        self._dir = persist_dir
        os.makedirs(persist_dir, exist_ok=True)
        self._vec_path = os.path.join(persist_dir, "vectors.npz")
        self._meta_path = os.path.join(persist_dir, "vectors.jsonl")
        self._vectors: np.ndarray | None = None
        self._chunks: list[Chunk] = []
        self._load()

    def upsert(self, chunks: list[Chunk], vectors: list[list[float]]) -> None:
        self._chunks = list(chunks)
        self._vectors = self._normalize(np.asarray(vectors, dtype=np.float32))
        self._save()

    def query(self, vector: list[float], k: int) -> list[tuple[Chunk, float]]:
        if self._vectors is None or not self._chunks:
            return []
        q = self._normalize(np.asarray([vector], dtype=np.float32))[0]
        sims = self._vectors @ q  # cosine similarity (all normalized)
        top = np.argsort(-sims)[:k]
        return [(self._chunks[i], float(sims[i])) for i in top]

    @staticmethod
    def _normalize(m: np.ndarray) -> np.ndarray:
        norms = np.linalg.norm(m, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return m / norms

    def _save(self) -> None:
        np.savez_compressed(self._vec_path, vectors=self._vectors)
        with open(self._meta_path, "w", encoding="utf-8") as fh:
            for c in self._chunks:
                fh.write(json.dumps(c.to_dict(), ensure_ascii=False) + "\n")

    def _load(self) -> None:
        if os.path.exists(self._vec_path) and os.path.exists(self._meta_path):
            self._vectors = np.load(self._vec_path)["vectors"]
            self._chunks = [Chunk(**json.loads(l)) for l in open(self._meta_path, encoding="utf-8")]
