# SWEBOK Knowledge Base Pipeline (POC)

Tech-agnostic pipeline that turns SWEBOK source material into a retrieval-ready
knowledge base for a future MCP server. Built with a **ports & adapters** design:
the core orchestration depends only on interfaces, so every technology
(PDF parser, embedder, vector store) is swappable via `config.yaml` without
touching the core.

## Ports & Adapters Design

This project uses the **Ports & Adapters** (or Hexagonal) architecture to keep the
core logic clean and independent of external technologies.

- **Ports**: These are interfaces defined in `kbprep/rag/ports.py`. They declare
  a contract for a piece of functionality, like `DocumentExtractor` or
  `VectorStore`. The core application (`pipeline.py`) only interacts with these
  ports, without knowing any implementation details.

- **Adapters**: These are the concrete implementations of the ports, located in
  `kbprep/rag/adapters/`. An adapter "plugs into" a port. For example,
  `PdfPlumberExtractor` is an adapter that implements the `DocumentExtractor`
  port using the `pdfplumber` library.

- **Benefit**: This separation allows us to easily swap technologies. If we want
  to use a different vector database, we just write a new adapter for the
  `VectorStore` port and change one line in `config.yaml`. The core application
  logic remains untouched.

## Pipeline stages

```
extract → clean → map-taxonomy → chunk → embed → index → retrieve/eval
```

Each stage is an adapter behind a port (see `kbprep/rag/ports.py`). The current
POC scope is Chapter 1 (Software Requirements) of SWEBOK Guide V4.0.

## Stage Details

This section describes the key concepts and the sequential stages of the pipeline.

### Key Concepts

-   **Taxonomy**: A formal classification that maps raw text to a structured
    knowledge hierarchy.
    -   **What it is**: In this project, it's the `kbprep/rag/taxonomy/swebok_v4.yaml`
        file. It defines a list of `topics` for a given **KA (Knowledge Area)**, which
        is a top-level chapter of the SWEBOK guide.
    -   **How it works**: Each topic in the YAML (e.g., `topic_name: "Requirements
        Elicitation"`) contains a list of `headings` (e.g., "1.1 Elicitation",
        "1.1. Elicitation"). The `SwebokTaxonomyMapper` adapter reads the source
        document and when it finds one of these headings, it tags the subsequent
        text with the corresponding `topic_name` and `ka_name`.
    -   **Why it's used**: This tagging enriches the data with crucial metadata,
        which enables:
        -   **Precise Citations**: The final RAG system can state exactly which
            SWEBOK topic its answer is based on.
        -   **Scoped Queries**: Future ability to ask questions within the
            context of a specific Knowledge Area (e.g., "summarize validation
            in the context of Software Testing").
        -   **Analysis & Grouping**: Allows for analyzing content coverage and
            grouping related chunks of information.

-   **Chunk**: The atomic unit of knowledge for the RAG system. It's a piece of
    text small enough to contain a single, focused idea but large enough for its
    meaning to be unambiguous. Good chunking is critical for retrieval quality.

-   **Embedding**: A mathematical representation of text (a "chunk") as a
    numerical vector (a list of numbers) in a high-dimensional space. Texts with
    similar meanings will have vectors that are close to each other. This is
    performed by a language model (here, `BAAI/bge-small-en-v1.5`).

### Pipeline Stages

1.  **`extract` (Extraction)**
    -   **Goal**: To pull raw text content from source files (e.g., PDFs).
    -   **Output**: A stream of text, often including "noise" like headers,
        footers, and formatting artifacts.

2.  **`clean` (Cleaning)**
    -   **Goal**: To remove the noise from the extracted text. This involves
        stripping extra whitespace, repeated headers/footers, and other
        non-content elements.

3.  **`map-taxonomy` (Taxonomy Mapping)**
    -   **Goal**: To assign each piece of content its proper place in the
        knowledge structure using the defined **Taxonomy**.

4.  **`chunk` (Chunking)**
    -   **Goal**: To break down long documents into smaller, semantically coherent
        **Chunks**.

5.  **`embed` (Embedding)**
    -   **Goal**: To convert each text **Chunk** into a numerical **Embedding**.

6.  **`index` (Indexing)**
    -   **Goal**: To store the generated **Embeddings** in a specialized vector
        database that allows for ultra-fast semantic search.
    -   **Process**: When a user asks a question, it is also converted into an
        **Embedding**, and the database finds the chunk vectors that are "closest"
        to the question vector.

7.  **`retrieve` / `eval` (Retrieval / Evaluation)**
    -   **`retrieve`**: The process of searching for and returning relevant
        **Chunks** based on a user's query.
    -   **`eval`**: An automated process to measure retrieval quality using a
        pre-defined set of questions and expected outcomes (`golden_set.json`).
        It checks if the system returns the correct **Chunks** for a given
        question.

## Layout

```
MCP Swebok/
  KnowledgeBase/           # Handoff artifact (shared): the knowledge base the
    chunks.jsonl           #   MCP server consumes. Output of "Chunking":
                           #   each line is a JSON `Chunk` (see `rag/models.py`)
                           #   with text + full metadata (KA, topic, page, etc.).
    figures.jsonl          #   Side lookup: authored figure records (join by ref).
    figures/               #   Extracted figure images (JPG).
    vectors/               #   Persisted vector index, output of "Index":
      vectors.npz          #     (Numpy adapter) the numerical embedding vectors.
      vectors.jsonl        #     (Numpy adapter) the metadata for each vector.
  KnowledgeBasePipeline/
    RawMaterials/          # source PDFs (input)
    config.yaml            # technology choices live here, not in the core
    golden_set.json        # evaluation questions (KA/topic ground truth)
    requirements.txt
    kbprep/                # the package (feature-based)
      cli.py               # prepare / index / query / eval commands
      shared/config.py     # config loader
      rag/                 # RAG feature: text -> chunks -> vectors
        ports.py           # interfaces the core depends on
        models.py          # neutral data structures (JSON-serializable)
        pipeline.py        # core orchestration (knows only ports)
        factory.py         # wires concrete adapters from config (DI point)
        quality.py         # automatic quality gates + report
        adapters/          # concrete implementations (pdfplumber, ST, numpy...)
        taxonomy/swebok_v4.yaml # SWEBOK KA1 -> 8 topics
      figures/             # Figures feature: images + sidecar join-by-reference
        models.py          # Figure record
        sidecar.py         # load authored sidecars + detect "Figure X.Y" refs
        extract.py         # render figure images (JPG) from the source PDF
        sidecars/swebok-v4-ch1.yaml # authored figure content (input)
    tests/test_contracts.py # every adapter must satisfy its port
    output/quality_report.json # Internal QA artifact (NOT part of the handoff)
```

> The generated **knowledge base** (`chunks.jsonl` + `vectors/`) is written to
> the top-level `KnowledgeBase/` folder — the explicit handoff contract between
> this pipeline (producer) and the MCP server (consumer). Paths are configured in
> `config.yaml` (`paths.knowledge_base`, `vector_store.persist_dir`).

## Usage

```powershell
# from KnowledgeBasePipeline, using the project venv
$env:PYTHONPATH="."
.venv\Scripts\python.exe -m kbprep.cli prepare   # extract→clean→map→chunk + QA
.venv\Scripts\python.exe -m kbprep.cli index     # + embed → vector index
.venv\Scripts\python.exe -m kbprep.cli query "your question"
.venv\Scripts\python.exe -m kbprep.cli eval      # golden-set recall@k
```

## Reference implementations (all permissive licenses)

| Port           | Default adapter          | Library (license)                     |
|----------------|--------------------------|---------------------------------------|
| DocumentExtractor | PdfPlumberExtractor   | pdfplumber (MIT)                      |
| TextCleaner    | BasicCleaner             | stdlib                                |
| TaxonomyMapper | SwebokTaxonomyMapper     | PyYAML (MIT)                          |
| Chunker        | StructureChunker         | stdlib                                |
| Embedder       | SentenceTransformers     | sentence-transformers (Apache-2.0), BAAI/bge-small-en-v1.5 (MIT) |
| VectorStore    | NumpyVectorStore         | numpy (BSD) — no build tools needed  |

`chromadb` is supported as an alternative vector store but is optional (it needs
Microsoft C++ Build Tools to compile on Windows); the default numpy store avoids
that dependency.

## Human supervision

The pipeline runs automatically with quality gates (extraction ratio, chunk size
distribution, orphan/oversized detection, KA/topic coverage, metadata schema).
A human reviews the final `quality_report.json` plus a sample of `chunks.jsonl`.
