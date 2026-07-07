"""Structure-aware chunker.

Splits each reconstructed section into retrieval-sized chunks, preserving
sentence boundaries and adding overlap. Every chunk carries full KA/topic/page
metadata so retrieval can cite Knowledge Area, topic and page range.
"""
from __future__ import annotations

import hashlib
import re

from ..models import Section, Document, Chunk

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9])")


def _tokens(text: str) -> int:
    return len(text.split())


class StructureChunker:
    def __init__(
        self,
        ka_id: str,
        ka_name: str,
        max_tokens: int = 350,
        overlap_tokens: int = 50,
        min_chunk_tokens: int = 20,
    ) -> None:
        self.ka_id = ka_id
        self.ka_name = ka_name
        self.max_tokens = max_tokens
        self.overlap_tokens = overlap_tokens
        self.min_chunk_tokens = min_chunk_tokens

    def chunk(self, sections: list[Section], document: Document) -> list[Chunk]:
        chunks: list[Chunk] = []
        for s_idx, section in enumerate(sections):
            for c_idx, text in enumerate(self._split(section.text)):
                if _tokens(text) < self.min_chunk_tokens:
                    continue
                checksum = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]
                chunks.append(
                    Chunk(
                        id=f"{document.source_id}-s{s_idx:02d}-c{c_idx:02d}",
                        text=text,
                        source_id=document.source_id,
                        source_type=document.source_type,
                        ka_id=self.ka_id,
                        ka_name=self.ka_name,
                        topic_id=section.topic_id,
                        topic_name=section.topic_name,
                        section_heading=section.heading,
                        page_start=section.page_start,
                        page_end=section.page_end,
                        language="en",
                        token_count=_tokens(text),
                        checksum=checksum,
                    )
                )
        return chunks

    def _split(self, text: str) -> list[str]:
        sentences = _SENT_SPLIT.split(text) if text else []
        chunks: list[str] = []
        current: list[str] = []
        count = 0
        for sent in sentences:
            st = _tokens(sent)
            if count + st > self.max_tokens and current:
                chunks.append(" ".join(current))
                current = self._overlap(current)
                count = _tokens(" ".join(current))
            current.append(sent)
            count += st
        if current:
            chunks.append(" ".join(current))
        return chunks

    def _overlap(self, sentences: list[str]) -> list[str]:
        """Keep trailing sentences up to overlap_tokens for context continuity."""
        kept: list[str] = []
        count = 0
        for sent in reversed(sentences):
            st = _tokens(sent)
            if count + st > self.overlap_tokens:
                break
            kept.insert(0, sent)
            count += st
        return kept
