"""One-off script: write per-chapter taxonomy YAMLs (chapters 2-18) for the
full SWEBOK v4.0a Guide. Topic titles were extracted from the Guide's own
Table of Contents (pages 6-25), cross-checked against real heading detection
in the split chapter PDFs (PdfPlumberExtractor's Semibold/Bold signal), and
manually corrected in the two spots (ch4 topic 3, ch8 all topics) where the
ToC's two-column PDF layout garbled the raw text extraction. Chapter 1's
existing hand-authored taxonomy is left untouched.
"""
from __future__ import annotations

import yaml

CHAPTERS: dict[int, tuple[str, list[str]]] = {
    2: ("Software Architecture", [
        "Software Architecture Fundamentals",
        "Software Architecture Description",
        "Software Architecture Process",
        "Software Architecture Evaluation",
    ]),
    3: ("Software Design", [
        "Software Design Fundamentals",
        "Software Design Processes",
        "Software Design Qualities",
        "Recording Software Designs",
        "Software Design Strategies and Methods",
        "Software Design Quality Analysis and Evaluation",
    ]),
    4: ("Software Construction", [
        "Software Construction Fundamentals",
        "Managing Construction",
        "Practical Considerations",
        "Construction Technologies",
        "Software Construction Tools",
    ]),
    5: ("Software Testing", [
        "Software Testing Fundamentals",
        "Test Levels",
        "Test Techniques",
        "Test-Related Measures",
        "Test Process",
        "Software Testing in the Development Processes and the Application Domains",
        "Testing of and Testing Through Emerging Technologies",
        "Software Testing Tools",
    ]),
    6: ("Software Engineering Operations", [
        "Software Engineering Operations Fundamentals",
        "Software Engineering Operations Planning",
        "Software Engineering Operations Delivery",
        "Software Engineering Operations Control",
        "Practical Considerations",
        "Software Engineering Operations Tools",
    ]),
    7: ("Software Maintenance", [
        "Software Maintenance Fundamentals",
        "Key Issues in Software Maintenance",
        "Software Maintenance Processes",
        "Software Maintenance Techniques",
        "Software Maintenance Tools",
    ]),
    8: ("Software Configuration Management", [
        "Management of the SCM Process",
        "Software Configuration Identification",
        "Software Configuration Change Control",
        "Software Configuration Status Accounting",
        "Software Configuration Auditing",
        "Software Release Management and Delivery",
        "Software Configuration Tools",
    ]),
    9: ("Software Engineering Management", [
        "Initiation and Scope Definition",
        "Software Project Planning",
        "Software Project Execution",
        "Software Review and Evaluation",
        "Closure",
        "Software Engineering Measurement",
        "Software Engineering Management Tools",
    ]),
    10: ("Software Engineering Process", [
        "Software Engineering Process Fundamentals",
        "Life Cycles",
        "Software Process Assessment and Improvement",
    ]),
    11: ("Software Engineering Models and Methods", [
        "Modeling",
        "Types of Models",
        "Analysis of Models",
        "Software Engineering Methods",
    ]),
    12: ("Software Quality", [
        "Software Quality Fundamentals",
        "Software Quality Management Process",
        "Software Quality Assurance Process",
        "Software Quality Tools",
    ]),
    13: ("Software Security", [
        "Software Security Fundamentals",
        "Security Management and Organization",
        "Software Security Engineering and Processes",
        "Security Engineering for Software Systems",
        "Software Security Tools",
        "Domain-Specific Software Security",
    ]),
    14: ("Software Engineering Professional Practice", [
        "Professionalism",
        "Group Dynamics and Psychology",
        "Communication Skills",
    ]),
    15: ("Software Engineering Economics", [
        "Software Engineering Economics Fundamentals",
        "The Engineering Decision-Making Process",
        "For-Profit Decision-Making",
        "Nonprofit Decision-Making",
        "Present Economy Decision-Making",
        "Multiple-Attribute Decision-Making",
        "Identifying and Characterizing Intangible Assets",
        "Estimation",
        "Practical Considerations",
        "Related Concepts",
    ]),
    16: ("Computing Foundations", [
        "Basic Concepts of a System or Solution",
        "Computer Architecture and Organization",
        "Data Structures and Algorithms",
        "Programming Fundamentals and Languages",
        "Operating Systems",
        "Database Management",
        "Computer Networks and Communications",
        "User and Developer Human Factors",
        "Artificial Intelligence and Machine Learning",
    ]),
    17: ("Mathematical Foundations", [
        "Basic Logic",
        "Proof Techniques",
        "Set, Relation, Function",
        "Graph and Tree",
        "Finite-State Machine",
        "Grammar",
        "Number Theory",
        "Basics of Counting",
        "Discrete Probability",
        "Numerical Precision, Accuracy, and Error",
        "Algebraic Structures",
        "Engineering Calculus",
        "New Advancements",
    ]),
    18: ("Engineering Foundations", [
        "The Engineering Process",
        "Engineering Design",
        "Abstraction and Encapsulation",
        "Empirical Methods and Experimental Techniques",
        "Statistical Analysis",
        "Modeling, Simulation, and Prototyping",
        "Measurement",
        "Standards",
        "Root Cause Analysis",
        "Industry 4.0 and Software Engineering",
    ]),
}

for num, (ka_name, topics) in CHAPTERS.items():
    out = {
        "ka_id": f"SWEBOK-KA-{num:02d}",
        "ka_name": ka_name,
        "source_version": "SWEBOK Guide V4.0",
        "topics": [{"id": str(i + 1), "name": t} for i, t in enumerate(topics)],
    }
    out_path = f"kbprep/rag/taxonomy/swebok-v4-ch{num}.yaml"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(f"# SWEBOK v4.0 taxonomy — Knowledge Area {num}: {ka_name}\n")
        fh.write("# Used to tag chunks with (ka, topic) metadata for RAG filtering & citation.\n")
        fh.write("# Top-level topics follow the KA breakdown of topics (from the Guide's Table of Contents).\n")
        yaml.safe_dump(out, fh, sort_keys=False, allow_unicode=True)
    print(f"wrote {out_path} ({len(topics)} topics)")
