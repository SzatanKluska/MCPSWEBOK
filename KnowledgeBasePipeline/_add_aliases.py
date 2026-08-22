"""One-off script: backfill `aliases` into the chapter 2-18 taxonomy YAMLs,
for consistency with chapter 1's hand-authored file (drop the generic KA-name
prefix, keep the distinguishing part — same convention ch1 already uses,
e.g. "Requirements Elicitation" -> "Elicitation"). Skipped where the topic
name has no redundant prefix to drop (an alias identical to the name adds
nothing). Confirmed separately that no currently-unmapped section would
actually match via these aliases — this is a consistency backfill, not a
coverage fix.
"""
from __future__ import annotations

import yaml

# chapter -> {topic_id: [aliases]}; topics not listed get no alias.
ALIASES: dict[int, dict[str, list[str]]] = {
    2: {
        "1": ["Architecture Fundamentals"],
        "2": ["Architecture Description"],
        "3": ["Architecture Process"],
        "4": ["Architecture Evaluation"],
    },
    3: {
        "1": ["Design Fundamentals"],
        "2": ["Design Processes"],
        "3": ["Design Qualities"],
        "4": ["Recording Designs"],
        "5": ["Design Strategies and Methods"],
        "6": ["Design Quality Analysis and Evaluation"],
    },
    4: {
        "1": ["Construction Fundamentals"],
        "2": ["Construction Management"],
        "3": ["Practical Activities"],
        "4": ["Construction Tech"],
        "5": ["Construction Tools"],
    },
    5: {
        "1": ["Testing Fundamentals"],
        "6": ["Testing in Development and Application Domains"],
        "7": ["Testing Emerging Technologies"],
        "8": ["Testing Tools"],
    },
    6: {
        "1": ["Operations Fundamentals"],
        "2": ["Operations Planning"],
        "3": ["Operations Delivery"],
        "4": ["Operations Control"],
        "5": ["Practical Activities"],
        "6": ["Operations Tools"],
    },
    7: {
        "1": ["Maintenance Fundamentals"],
        "2": ["Maintenance Issues"],
        "3": ["Maintenance Processes"],
        "4": ["Maintenance Techniques"],
        "5": ["Maintenance Tools"],
    },
    8: {
        "1": ["SCM Process Management"],
        "2": ["Configuration Identification"],
        "3": ["Configuration Change Control"],
        "4": ["Configuration Status Accounting"],
        "5": ["Configuration Auditing"],
        "6": ["Release Management and Delivery"],
        "7": ["Configuration Tools"],
    },
    9: {
        "2": ["Project Planning"],
        "3": ["Project Execution"],
        "4": ["Review and Evaluation"],
        "6": ["Engineering Measurement"],
        "7": ["Management Tools"],
    },
    10: {
        "1": ["Process Fundamentals"],
        "3": ["Process Assessment and Improvement"],
    },
    11: {
        "4": ["Engineering Methods"],
    },
    12: {
        "1": ["Quality Fundamentals"],
        "2": ["Quality Management Process"],
        "3": ["Quality Assurance Process", "QA Process"],
        "4": ["Quality Tools"],
    },
    13: {
        "1": ["Security Fundamentals"],
        "3": ["Security Engineering and Processes"],
        "5": ["Security Tools"],
        "6": ["Domain-Specific Security"],
    },
    15: {
        "1": ["Economics Fundamentals"],
        "2": ["Engineering Decision-Making Process"],
        "9": ["Practical Activities"],
    },
    16: {
        "2": ["Architecture and Organization"],
        "7": ["Networks and Communications"],
        "8": ["Human Factors"],
        "9": ["AI and Machine Learning"],
    },
    18: {
        "4": ["Empirical Methods"],
    },
}


def main() -> None:
    for num, topic_aliases in ALIASES.items():
        path = f"kbprep/rag/taxonomy/swebok-v4-ch{num}.yaml"
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
            fh.seek(0)
            data = yaml.safe_load(fh)
        header = [l for l in lines if l.startswith("#")]

        for topic in data["topics"]:
            aliases = topic_aliases.get(topic["id"])
            if aliases:
                topic["aliases"] = aliases

        with open(path, "w", encoding="utf-8") as fh:
            fh.writelines(header)
            yaml.safe_dump(data, fh, sort_keys=False, allow_unicode=True)
        print(f"updated {path}: {len(topic_aliases)}/{len(data['topics'])} topics got aliases")


if __name__ == "__main__":
    main()
