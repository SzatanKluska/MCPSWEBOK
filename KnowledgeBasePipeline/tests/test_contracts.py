"""Contract tests: every adapter must satisfy its port.

These guarantee interchangeability — a new implementation of any port must pass
the same tests, so swapping technologies cannot silently break the pipeline.
Run with: python -m pytest  (or the plain runner in __main__).
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from kbprep.rag import ports, factory
from kbprep.shared.config import load_config

_CONFIG = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "config.yaml"))


def test_extractor_satisfies_port():
    cfg = load_config(_CONFIG)
    assert isinstance(factory.build_extractor(cfg), ports.DocumentExtractor)


def test_cleaner_satisfies_port():
    cfg = load_config(_CONFIG)
    assert isinstance(factory.build_cleaner(cfg), ports.TextCleaner)


def test_mapper_satisfies_port():
    cfg = load_config(_CONFIG)
    assert isinstance(factory.build_taxonomy_mapper(cfg), ports.TaxonomyMapper)


def test_chunker_satisfies_port():
    cfg = load_config(_CONFIG)
    assert isinstance(factory.build_chunker(cfg), ports.Chunker)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"[OK] {name}")
    print("All contract tests passed.")
