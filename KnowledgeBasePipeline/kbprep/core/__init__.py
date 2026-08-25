"""Pipeline orchestration: extract -> clean -> map -> chunk, plus the quality gates."""

from .pipeline import Pipeline, PipelineResult
from .quality import QualityReport, chunk_gate, extraction_gate

__all__ = [
    "Pipeline",
    "PipelineResult",
    "QualityReport",
    "chunk_gate",
    "extraction_gate",
]
