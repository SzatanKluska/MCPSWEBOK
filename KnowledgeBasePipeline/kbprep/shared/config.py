"""Loads config.yaml and resolves paths relative to the pipeline directory."""
from __future__ import annotations

import os
from typing import Any

import yaml


class Config:
    def __init__(self, data: dict[str, Any], base_dir: str) -> None:
        self._data = data
        self.base_dir = base_dir

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def path(self, *keys: str) -> str:
        node: Any = self._data
        for k in keys:
            node = node[k]
        return os.path.normpath(os.path.join(self.base_dir, node))


def load_config(path: str) -> Config:
    base_dir = os.path.dirname(os.path.abspath(path))
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return Config(data, base_dir)
