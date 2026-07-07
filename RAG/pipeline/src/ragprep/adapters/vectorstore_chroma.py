"""Local vector store adapter using Chroma (Apache-2.0), persisted to disk."""
from __future__ import annotations

from ..models import Chunk

_META_KEYS = (
    "source_id", "source_type", "ka_id", "ka_name", "topic_id", "topic_name",
    "section_heading", "page_start", "page_end", "language", "token_count", "checksum",
)


class ChromaVectorStore:
    def __init__(self, collection: str, persist_dir: str) -> None:
        import chromadb

        self._client = chromadb.PersistentClient(path=persist_dir)
        # reset collection for reproducible POC runs
        try:
            self._client.delete_collection(collection)
        except Exception:
            pass
        self._collection = self._client.create_collection(
            name=collection, metadata={"hnsw:space": "cosine"}
        )

    def upsert(self, chunks: list[Chunk], vectors: list[list[float]]) -> None:
        self._collection.add(
            ids=[c.id for c in chunks],
            embeddings=vectors,
            documents=[c.text for c in chunks],
            metadatas=[self._meta(c) for c in chunks],
        )

    def query(self, vector: list[float], k: int) -> list[tuple[Chunk, float]]:
        res = self._collection.query(
            query_embeddings=[vector], n_results=k,
            include=["documents", "metadatas", "distances"],
        )
        out: list[tuple[Chunk, float]] = []
        for cid, doc, meta, dist in zip(
            res["ids"][0], res["documents"][0], res["metadatas"][0], res["distances"][0]
        ):
            chunk = Chunk(
                id=cid, text=doc,
                source_id=meta["source_id"], source_type=meta["source_type"],
                ka_id=meta["ka_id"], ka_name=meta["ka_name"],
                topic_id=meta.get("topic_id") or None,
                topic_name=meta.get("topic_name") or None,
                section_heading=meta["section_heading"],
                page_start=meta["page_start"], page_end=meta["page_end"],
                language=meta["language"], token_count=meta["token_count"],
                checksum=meta["checksum"],
            )
            out.append((chunk, 1.0 - dist))  # cosine distance -> similarity
        return out

    @staticmethod
    def _meta(c: Chunk) -> dict:
        d = c.to_dict()
        # Chroma rejects None metadata values -> coerce to ""
        return {k: ("" if d[k] is None else d[k]) for k in _META_KEYS}
