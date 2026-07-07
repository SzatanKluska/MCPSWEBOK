"""Automatic quality gates and reporting (no human in the loop).

Each gate returns a pass/fail plus metrics. A human reviews the final report
and a sample of chunks, per the agreed supervision model.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from statistics import mean, median

from .models import Document, Chunk


@dataclass
class QualityReport:
    checks: list[dict] = field(default_factory=list)
    metrics: dict = field(default_factory=dict)

    @property
    def passed(self) -> bool:
        return all(c["passed"] for c in self.checks)

    def add(self, name: str, passed: bool, detail: str) -> None:
        self.checks.append({"name": name, "passed": passed, "detail": detail})


def extraction_gate(document: Document, min_ratio: float, report: QualityReport) -> None:
    total = len(document.pages)
    non_empty = sum(1 for p in document.pages if any(l.text.strip() for l in p.lines))
    ratio = non_empty / total if total else 0.0
    report.metrics["pages_total"] = total
    report.metrics["pages_with_text"] = non_empty
    report.metrics["extraction_ratio"] = round(ratio, 3)
    report.add(
        "extraction_ratio",
        ratio >= min_ratio,
        f"{non_empty}/{total} pages yielded text (ratio {ratio:.2f} >= {min_ratio})",
    )


def chunk_gate(
    chunks: list[Chunk], min_tokens: int, max_tokens: int, report: QualityReport
) -> None:
    counts = [c.token_count for c in chunks]
    report.metrics["chunk_count"] = len(chunks)
    if counts:
        report.metrics["chunk_tokens_min"] = min(counts)
        report.metrics["chunk_tokens_max"] = max(counts)
        report.metrics["chunk_tokens_mean"] = round(mean(counts), 1)
        report.metrics["chunk_tokens_median"] = median(counts)

    report.add("chunks_non_empty", len(chunks) > 0, f"{len(chunks)} chunks produced")

    orphans = [c.id for c in chunks if c.token_count < min_tokens]
    report.add(
        "no_orphan_chunks",
        not orphans,
        f"{len(orphans)} chunks below {min_tokens} tokens",
    )
    oversized = [c.id for c in chunks if c.token_count > max_tokens]
    report.add(
        "no_oversized_chunks",
        not oversized,
        f"{len(oversized)} chunks above {max_tokens} tokens",
    )

    # KA/topic coverage
    mapped = sum(1 for c in chunks if c.topic_id)
    topics = sorted({c.topic_id for c in chunks if c.topic_id})
    report.metrics["chunks_mapped_to_topic"] = mapped
    report.metrics["topics_covered"] = topics
    report.add(
        "topic_coverage",
        len(topics) > 0,
        f"chunks mapped to topics: {mapped}/{len(chunks)}; topics: {topics}",
    )

    # metadata schema validation
    required = ("id", "text", "ka_id", "ka_name", "page_start", "checksum")
    bad = [c.id for c in chunks if any(not getattr(c, f) and getattr(c, f) != 0 for f in required)]
    report.add(
        "metadata_schema",
        not bad,
        f"{len(bad)} chunks with missing required metadata",
    )
