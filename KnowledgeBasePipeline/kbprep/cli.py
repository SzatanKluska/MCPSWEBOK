"""Command-line entrypoints for the SWEBOK RAG preparation POC.

Usage (from KnowledgeBasePipeline, with the venv Python):
  python -m kbprep.cli prepare      # extract -> clean -> map -> chunk -> QA
  python -m kbprep.cli index        # + embed -> vector index
  python -m kbprep.cli query "..."  # retrieve top-k with citations
  python -m kbprep.cli eval         # run golden-set evaluation
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys

from .shared.config import load_config
from .rag import factory
from .figures.sidecar import load_figures
from .rag.pipeline import Pipeline

_CONFIG = os.path.join(os.path.dirname(__file__), "..", "config.yaml")


def _load():
    cfg = load_config(os.path.normpath(_CONFIG))
    return cfg


def _build_shared(cfg, with_vectors: bool) -> dict:
    """Adapters reused across every source: extractor is stateless, embedder is
    the expensive one (loads a model) so it must be built once, not per source."""
    return {
        "extractor": factory.build_extractor(cfg),
        "embedder": factory.build_embedder(cfg) if with_vectors else None,
        "vector_store": factory.build_vector_store(cfg) if with_vectors else None,
    }


def _build_pipeline_for_source(cfg, shared: dict, source_id: str) -> Pipeline:
    """Mapper/chunker (and thus the cleaner's extra header pattern) depend on
    the source's own taxonomy (ka_id/ka_name/topics), so these are rebuilt
    per source; the shared, expensive-to-build adapters are reused as-is."""
    mapper = factory.build_taxonomy_mapper(cfg, source_id)
    header_pattern = rf"^{re.escape(mapper.ka_name.upper())}$"
    cleaner = factory.build_cleaner(cfg, extra_drop_patterns=[header_pattern])
    chunker = factory.build_chunker(cfg, source_id)
    return Pipeline(
        extractor=shared["extractor"],
        cleaner=cleaner,
        mapper=mapper,
        chunker=chunker,
        embedder=shared["embedder"],
        vector_store=shared["vector_store"],
    )


def _source_files(cfg) -> list[str]:
    raw = cfg.path("paths", "raw_materials")
    return sorted(glob.glob(os.path.join(raw, "**", "*.pdf"), recursive=True))


def _prepare_all(cfg, shared: dict):
    q = cfg["quality"]
    results = []
    for path in _source_files(cfg):
        source_id = os.path.splitext(os.path.basename(path))[0]
        pipeline = _build_pipeline_for_source(cfg, shared, source_id)
        result = pipeline.prepare(
            path, source_id,
            min_extraction_ratio=q["min_extraction_ratio"],
            min_chunk_tokens=q["min_chunk_tokens"],
            max_chunk_tokens=q["max_chunk_tokens"],
        )
        results.append(result)
    return results


def _collect_figures(cfg, results):
    figures_dir = cfg.path("paths", "figures")
    figures = []
    for r in results:
        chunks = [c for c in r.chunks]
        if not chunks:
            continue
        figures.extend(
            load_figures(figures_dir, r.document.source_id,
                         chunks[0].ka_id, chunks[0].ka_name)
        )
    return figures


def _write_outputs(cfg, results):
    out_dir = cfg.path("paths", "output")
    kb_dir = cfg.path("paths", "knowledge_base")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(kb_dir, exist_ok=True)
    chunks_path = os.path.join(kb_dir, "chunks.jsonl")
    figures_path = os.path.join(kb_dir, "figures.jsonl")
    report_path = os.path.join(out_dir, "quality_report.json")
    all_chunks = [c for r in results for c in r.chunks]
    with open(chunks_path, "w", encoding="utf-8") as fh:
        for c in all_chunks:
            fh.write(json.dumps(c.to_dict(), ensure_ascii=False) + "\n")
    figures = _collect_figures(cfg, results)
    with open(figures_path, "w", encoding="utf-8") as fh:
        for f in figures:
            fh.write(json.dumps(f.to_dict(), ensure_ascii=False) + "\n")
    merged = {
        "sources": [r.document.source_id for r in results],
        "reports": [
            {"source": r.document.source_id,
             "passed": r.report.passed,
             "checks": r.report.checks,
             "metrics": r.report.metrics}
            for r in results
        ],
    }
    with open(report_path, "w", encoding="utf-8") as fh:
        json.dump(merged, fh, ensure_ascii=False, indent=2)
    return chunks_path, report_path, all_chunks


def _print_report(results):
    for r in results:
        print(f"\n=== {r.document.source_id} — QA {'PASS' if r.report.passed else 'FAIL'} ===")
        for c in r.report.checks:
            mark = "[OK]" if c["passed"] else "[!!]"
            print(f"  {mark} {c['name']}: {c['detail']}")
        print("  metrics:", json.dumps(r.report.metrics, ensure_ascii=False))


def cmd_prepare():
    cfg = _load()
    shared = _build_shared(cfg, with_vectors=False)
    results = _prepare_all(cfg, shared)
    chunks_path, report_path, all_chunks = _write_outputs(cfg, results)
    _print_report(results)
    print(f"\nWrote {len(all_chunks)} chunks -> {chunks_path}")
    print(f"Wrote quality report -> {report_path}")


def cmd_index():
    cfg = _load()
    shared = _build_shared(cfg, with_vectors=True)
    results = _prepare_all(cfg, shared)
    chunks_path, report_path, all_chunks = _write_outputs(cfg, results)
    _print_report(results)
    print(f"\nEmbedding + indexing {len(all_chunks)} chunks ...")
    Pipeline(
        extractor=shared["extractor"], cleaner=None, mapper=None, chunker=None,
        embedder=shared["embedder"], vector_store=shared["vector_store"],
    ).index(all_chunks)
    print("Vector index built.")


def _build_search_pipeline(cfg) -> Pipeline:
    """Search spans the whole merged index (all sources already embedded by
    `index`), so it needs only embedder + vector_store — no source_id to pick
    a taxonomy/cleaner for. extractor/cleaner/mapper/chunker are unused by
    `Pipeline.search`."""
    return Pipeline(
        extractor=None, cleaner=None, mapper=None, chunker=None,
        embedder=factory.build_embedder(cfg),
        vector_store=factory.build_vector_store(cfg),
    )


def _format_hit(chunk, score) -> str:
    topic = f"{chunk.topic_id}. {chunk.topic_name}" if chunk.topic_id else "(unmapped)"
    pages = (f"p.{chunk.page_start}" if chunk.page_start == chunk.page_end
             else f"pp.{chunk.page_start}-{chunk.page_end}")
    cite = f"[{chunk.ka_name} > {topic}, {chunk.source_id} {pages}]"
    preview = chunk.text[:280] + ("..." if len(chunk.text) > 280 else "")
    return f"  score={score:.3f} {cite}\n    {preview}"


def cmd_query(query: str):
    cfg = _load()
    pipeline = _build_search_pipeline(cfg)
    # rebuild index if empty is out of scope; assume `index` ran first
    k = cfg["evaluation"]["top_k"]
    hits = pipeline.search(query, k)
    print(f"\nQuery: {query}\n")
    for chunk, score in hits:
        print(_format_hit(chunk, score))


def cmd_eval():
    cfg = _load()
    pipeline = _build_search_pipeline(cfg)
    gs_path = os.path.normpath(os.path.join(os.path.dirname(_CONFIG), "golden_set.json"))
    with open(gs_path, encoding="utf-8") as fh:
        golden = json.load(fh)
    k = cfg["evaluation"]["top_k"]
    threshold = cfg["evaluation"]["recall_threshold"]
    hits_at_k = 0
    for item in golden:
        results = pipeline.search(item["question"], k)
        # (ka_id, topic_id) pair: topic numbering restarts at 1 per KA, so a bare
        # topic_id is ambiguous once the corpus spans more than one KA.
        pairs = {(c.ka_id, c.topic_id) for c, _ in results}
        expected = (item["expected_ka"], item["expected_topic"])
        ok = expected in pairs
        hits_at_k += int(ok)
        mark = "[OK]" if ok else "[!!]"
        print(f"{mark} '{item['question'][:60]}...' expected {expected} "
              f"-> retrieved {sorted(p for p in pairs if p[1])}")
    recall = hits_at_k / len(golden)
    print(f"\nrecall@{k} (topic match): {recall:.2f}  (threshold {threshold})")
    print("EVAL PASS" if recall >= threshold else "EVAL FAIL")


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 1
    cmd = argv[0]
    if cmd == "prepare":
        cmd_prepare()
    elif cmd == "index":
        cmd_index()
    elif cmd == "query":
        cmd_query(" ".join(argv[1:]) or "What is requirements elicitation?")
    elif cmd == "eval":
        cmd_eval()
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
