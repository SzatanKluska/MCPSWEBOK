"""Reconstructs logical sections from headings and maps them to SWEBOK topics.

SWEBOK top-level topics appear as Semibold headings shaped like "N. Topic Name".
Text between headings is accumulated into the section it belongs to; the section
inherits the KA/topic metadata of the most recent matched topic heading.
"""
from __future__ import annotations

import re
import difflib

import yaml

from ..models import Document, Section

_TOPIC_NUM = re.compile(r"^(\d+)\.\s+(.*)$")


class SwebokTaxonomyMapper:
    def __init__(self, taxonomy_path: str) -> None:
        with open(taxonomy_path, encoding="utf-8") as fh:
            tax = yaml.safe_load(fh)
        self.ka_id = tax["ka_id"]
        self.ka_name = tax["ka_name"]
        self.topics = tax["topics"]
        # lookup: topic_id -> (name), and name/alias -> topic
        self._by_id = {t["id"]: t for t in self.topics}
        self._name_index: dict[str, dict] = {}
        for t in self.topics:
            for label in [t["name"], *t.get("aliases", [])]:
                self._name_index[label.lower()] = t

    def map_sections(self, document: Document) -> list[Section]:
        sections: list[Section] = []
        current: Section | None = None
        pending_text: list[str] = []

        def flush():
            nonlocal current, pending_text
            if current is not None:
                current.text = self._join(pending_text)
                if current.text.strip():
                    sections.append(current)
            pending_text = []

        for page in document.pages:
            for line in page.lines:
                topic = self._match_topic(line.text) if line.is_heading else None
                if topic is not None:
                    flush()
                    current = Section(
                        topic_id=topic["id"],
                        topic_name=topic["name"],
                        heading=line.text,
                        text="",
                        page_start=page.number,
                        page_end=page.number,
                    )
                elif line.is_heading and current is None:
                    # a heading before any topic (e.g. INTRODUCTION) -> generic section
                    flush()
                    current = Section(
                        topic_id=None,
                        topic_name=None,
                        heading=line.text,
                        text="",
                        page_start=page.number,
                        page_end=page.number,
                    )
                else:
                    if current is None:
                        current = Section(None, None, "PREAMBLE", "", page.number, page.number)
                    pending_text.append(line.text)
                    current.page_end = page.number
        flush()
        return sections

    def _match_topic(self, text: str) -> dict | None:
        m = _TOPIC_NUM.match(text)
        if m:
            num, title = m.group(1), m.group(2).strip()
            if num in self._by_id:
                # confirm the title resembles the taxonomy entry
                cand = self._by_id[num]
                if self._similar(title, cand):
                    return cand
        # try direct name/alias match for unnumbered headings
        key = text.strip().lower()
        return self._name_index.get(key)

    def _similar(self, title: str, topic: dict) -> bool:
        labels = [topic["name"], *topic.get("aliases", [])]
        title_l = title.lower()
        for label in labels:
            ratio = difflib.SequenceMatcher(None, title_l, label.lower()).ratio()
            if ratio >= 0.6 or label.lower() in title_l or title_l in label.lower():
                return True
        return False

    @staticmethod
    def _join(parts: list[str]) -> str:
        text = " ".join(parts)
        # repair hyphenation introduced by line breaks
        text = re.sub(r"(\w+)-\s+(\w+)", r"\1\2", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text
