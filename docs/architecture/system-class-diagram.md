<!-- system-class-diagram
updated: 2026-08-22T21:54:59.296Z
-->
# System Class Diagram

> Auto-maintained by the `system-class-diagram` skill. Anchored to the commit in
> the marker above. Run the skill to refresh after new commits.

The system has two subsystems that meet at a file-based handoff contract: the
**KnowledgeBasePipeline** (Python) produces the knowledge base; the **Server**
(TypeScript, MCP) consumes it. Three levels of zoom, each answering a
different question: **Context** (how do the subsystems hand off data?),
**Module Contract** (what does each internal module expose to the rest of the
system, and who depends on whom?), and **per-module class diagrams** (what
does a given module actually contain?).

## Context

```mermaid
flowchart LR
  subgraph KBP["KnowledgeBasePipeline (producer · Python)"]
    CLI["kbprep.cli<br/>prepare / index"]
  end
  KB[("KnowledgeBase/<br/>chunks.jsonl · figures.jsonl · vectors/")]
  subgraph SRV["Server (consumer · TypeScript · MCP)"]
    TOOL["swebok_search tool<br/>+ figure resources"]
  end
  CLI -->|writes handoff| KB
  KB -->|loads at startup| SRV
```

## KnowledgeBasePipeline (Python)

Ports & adapters: `core` depends only on the port protocols; `di` (the
`Factory`) wires concrete adapters from `config.yaml`.

### Module Contract

```mermaid
classDiagram
  direction LR

  class ports { <<layer>>
    DocumentExtractor
    TextCleaner
    TaxonomyMapper
    Chunker
    Embedder
    VectorStore
  }
  class core { <<layer>>
    Pipeline.prepare(path, source_id)
    Pipeline.index(chunks)
    Pipeline.search(query, k)
  }
  class adapters { <<layer>> }
  class models { <<layer>>
    Document, Section, Chunk, Page, Line
  }
  class figures { <<layer>>
    figure_refs(text)
    load_figures(dir, source_id, ka_id, ka_name)
  }
  class di { <<layer>> }
  class shared { <<layer>>
    Config.path(keys)
  }
  class app { <<layer>>
    Cli.prepare() / index() / query(text) / eval()
  }

  adapters ..|> ports : implement
  core --> ports : depends only on
  core --> models
  adapters ..> figures : StructureChunker calls figure_refs
  di ..> adapters : wires concrete adapters
  di --> shared
  app --> core
  app --> di
  app --> shared
  app ..> figures
```

### ports

**Responsibility**: defines the technology-agnostic contracts between the
pipeline's orchestration core and every concrete implementation — the core
depends only on these, never on a concrete library.
**Concepts**:
- **Document** — the structured, in-memory result of extracting one source
  file (pages of lines with layout info), before any cleaning or tagging.
- **Section** — a reconstructed block of text between two headings, tagged
  with the topic it belongs to.
- **Chunk** — a retrieval-sized piece of text with full citation metadata;
  the unit that actually gets embedded and searched.

```mermaid
classDiagram
  class DocumentExtractor {
    <<interface>>
    +extract(path, source_id) Document
  }
  class TextCleaner {
    <<interface>>
    +clean(document) Document
  }
  class TaxonomyMapper {
    <<interface>>
    +map_sections(document) List~Section~
  }
  class Chunker {
    <<interface>>
    +chunk(sections, document) List~Chunk~
  }
  class Embedder {
    <<interface>>
    +embed_documents(texts) List~Vector~
    +embed_query(text) Vector
  }
  class VectorStore {
    <<interface>>
    +upsert(chunks, vectors)
    +query(vector, k) List~ScoredChunk~
  }
```

### core

**Responsibility**: orchestrates the extract→clean→map→chunk stages in
sequence, knowing only the `ports` interfaces — never a concrete adapter.
**Concepts**:
- **PipelineResult** — everything produced by preparing one source (its
  Document, Sections, Chunks, and QualityReport) bundled together.
- **QualityReport** — the pass/fail outcome of the automatic quality gates
  run on one source (extraction ratio, chunk size, topic coverage, ...).

```mermaid
classDiagram
  class Pipeline {
    +prepare(path, source_id) PipelineResult
    +index(chunks)
    +search(query, k) List~ScoredChunk~
  }
  class PipelineResult {
    +document
    +sections
    +chunks
    +report
  }
  class QualityReport {
    +checks
    +passed
  }

  Pipeline --> PipelineResult
  Pipeline --> QualityReport
```
> Depends on `ports` and `models` (see Module Contract) — not repeated here.

### adapters

**Responsibility**: one concrete, swappable implementation per port — this is
the only place a third-party library (pdfplumber, sentence-transformers,
numpy/chroma) actually gets imported.

```mermaid
classDiagram
  class PdfPlumberExtractor
  class BasicCleaner
  class SwebokTaxonomyMapper
  class StructureChunker
  class SentenceTransformersEmbedder
  class NumpyVectorStore
  class ChromaVectorStore

  class DocumentExtractor { <<interface>> +extract() }
  class TextCleaner { <<interface>> +clean() }
  class TaxonomyMapper { <<interface>> +map_sections() }
  class Chunker { <<interface>> +chunk() }
  class Embedder { <<interface>> +embed_documents() +embed_query() }
  class VectorStore { <<interface>> +upsert() +query() }
  class Chunk { <<type>> }
  class FiguresSidecar { <<module>> +figure_refs() +load_figures() }

  PdfPlumberExtractor ..|> DocumentExtractor
  BasicCleaner ..|> TextCleaner
  SwebokTaxonomyMapper ..|> TaxonomyMapper
  StructureChunker ..|> Chunker
  SentenceTransformersEmbedder ..|> Embedder
  NumpyVectorStore ..|> VectorStore
  ChromaVectorStore ..|> VectorStore
  StructureChunker --> Chunk
  StructureChunker ..> FiguresSidecar

  note for DocumentExtractor "owned by ports —<br/>shown only to anchor implements<br/>(same for TextCleaner/TaxonomyMapper/<br/>Chunker/Embedder/VectorStore)"
  note for Chunk "owned by models —<br/>shown only to anchor StructureChunker's output"
  note for FiguresSidecar "owned by figures —<br/>shown only to anchor the call"
```

### models

**Responsibility**: the plain, JSON-serializable data structures that flow
between pipeline stages — framework-free, no behavior.
**Concepts**:
- **Page / Line** — the raw layout unit extracted from a PDF page (text plus
  font size and heading flags), before any cleaning or section reconstruction.

```mermaid
classDiagram
  class Document
  class Section
  class Chunk
  class Page
  class Line

  Document *-- Page
  Page *-- Line
```

### figures

**Responsibility**: a side-feature, parallel to the main text pipeline, that
joins hand-authored figure content to whatever chunk references it by
"Figure X.Y" — plus a one-off tool to render figure images from the source PDF.
**Concepts**:
- **Figure** — one authored figure record (id, caption, description, optional
  Mermaid re-drawing, source image path) — input data, not something
  extracted automatically.
- **sidecar** — the hand-written YAML file (`<source_id>.yaml`) holding a
  source's figures; "sidecar" because it sits next to the generated pipeline
  output rather than being derived from it.

```mermaid
classDiagram
  class Figure
  class FiguresSidecar {
    <<module>>
    +figure_refs(text) List~str~
    +load_figures(dir, source_id) List~Figure~
  }
  class FigureExtract {
    <<module>>
    +main()
  }

  FiguresSidecar --> Figure

  note for FigureExtract "One-off tool: renders figure<br/>JPGs into KnowledgeBase/figures."
```

### di

**Responsibility**: the composition root — the only place that knows about
concrete adapter classes and wires them together from `config.yaml`, per
source (each source may need a different taxonomy).

```mermaid
classDiagram
  class Factory {
    <<module>>
    +build_extractor(cfg) DocumentExtractor
    +build_cleaner(cfg, extra_drop_patterns) TextCleaner
    +build_taxonomy_mapper(cfg, source_id) TaxonomyMapper
    +build_chunker(cfg, source_id) Chunker
    +build_embedder(cfg) Embedder
    +build_vector_store(cfg) VectorStore
  }
  class Config { <<type>> +path() }

  Factory --> Config

  note for Factory "Builds each adapter from config —<br/>the composition root (DI point)."
  note for Config "owned by shared —<br/>shown only to anchor the dependency"
```

### shared

**Responsibility**: cross-cutting config loading, used by any module that
needs a value from `config.yaml`.
**Concepts**:
- **Config** — resolves dotted config keys and paths relative to the
  pipeline's own directory.

```mermaid
classDiagram
  class Config {
    +path(keys) str
  }
```

### app

**Responsibility**: the command-line entry point a human runs
(`prepare`/`index`/`query`/`eval`) — turns CLI arguments into pipeline calls
and writes the on-disk handoff artifacts.

```mermaid
classDiagram
  class Cli {
    <<module>>
    +prepare()
    +index()
    +query(text)
    +eval()
  }
```
> Depends on `core`, `di`, `shared`, `figures` (see Module Contract) — not repeated here.

## Server (TypeScript · MCP)

Layered / hexagonal: dependencies point inward (`interface -> application ->
domain`); `infrastructure` implements the domain ports; `di` and `config` are
cross-cutting bootstrap.

### Module Contract

```mermaid
classDiagram
  direction LR

  class domain { <<layer>>
    Embedder, ChunkSource, FigureStore, VectorIndex
    RetrievalPolicies
  }
  class application { <<layer>>
    Retriever.search(query, k)
    Retriever.figuresFor(refs)
  }
  class infrastructure { <<layer>> }
  class interface_mcp { <<layer>>
    ServerFactory.create() McpServer
  }
  class di { <<layer>> }
  class config { <<layer>>
    loadConfig(env) Config
  }
  class app { <<layer>>
    main()
  }

  infrastructure ..|> domain : implement ports
  application --> domain : depends only on
  interface_mcp --> application
  interface_mcp ..> domain : RetrievalPolicies (citations)
  di ..> infrastructure : wires concrete adapters
  di ..> application
  di ..> interface_mcp
  di --> domain
  app --> di
  app --> config
  app ..> application
  app ..> interface_mcp
```

### domain

**Responsibility**: the framework-free core — the ports every adapter must
implement, the value types passed across the whole system, and pure
retrieval policies.
**Concepts**:
- **Chunk / Hit** — a `Chunk` is one retrievable passage with its citation
  metadata (loaded from `chunks.jsonl`); a `Hit` is a `Chunk` plus its
  similarity score, returned by a search.
- **Figure** — one figure record (loaded from `figures.jsonl`), joined to a
  `Hit` by reference.
- **RetrievalPolicies** — pure functions that turn raw retrieval results into
  what a client actually needs (which figures are relevant, how to format a
  citation) — logic, not I/O.

```mermaid
classDiagram
  class Chunk { <<type>> }
  class Figure { <<type>> }
  class Hit { <<type>> }
  class ImageBytes { <<type>> }
  class Embedder {
    <<interface>>
    +embedDocuments(texts) List~Vector~
    +embedQuery(text) Vector
  }
  class ChunkSource {
    <<interface>>
    +load() List~Chunk~
  }
  class FigureStore {
    <<interface>>
    +load() FigureMap
    +readImage(figure) ImageBytes
  }
  class VectorIndex {
    <<interface>>
    +build(chunks, vectors)
    +search(query, k) List~Hit~
  }
  class RetrievalPolicies {
    <<module>>
    +figuresForRefs(refs, byId) List~Figure~
    +citationOf(chunk) str
  }
```
> Framework-free: no `inversify` / `node:fs` / MCP imports, and no edges to
> other modules — it depends on nothing (see Server README).

### application

**Responsibility**: the single use case — retrieval — expressed as one class
that combines an `Embedder` and a `VectorIndex` behind the `domain` ports;
nothing here talks to a library or the filesystem directly.
**Concepts**:
- **warm-up** — `initialize()` loads and embeds the whole knowledge base once,
  at startup, so every subsequent search is in-memory and instant.

```mermaid
classDiagram
  class Retriever {
    +initialize()
    +search(query, k) List~Hit~
    +figuresFor(refs) List~Figure~
    +figureImage(figure) ImageBytes
    +allFigures() List~Figure~
    +chunkCount
  }
```
> Depends on `domain` only (ports + `RetrievalPolicies`) — see Module Contract.

### infrastructure

**Responsibility**: concrete, swappable implementations of the `domain`
ports (embedding model, vector index, file loaders) plus the transport the
MCP server talks over — where Node-specific and third-party code lives.
**Concepts**:
- **transport** — the wire protocol an MCP client and this server exchange
  JSON-RPC over (`stdio` today, `HTTP` a stubbed extension point).

```mermaid
classDiagram
  class TransformersEmbedder
  class InMemoryVectorIndex {
    +build(chunks, vectors)
    +search(query, k) List~Hit~
  }
  class ChunkFileSource
  class FigureFileSource
  class TransportFactory {
    <<module>>
    +createTransport(config)
  }
  class StdioTransport {
    <<module>>
    +createStdioTransport()
  }
  class HttpTransport {
    <<module>>
    +createHttpTransport(config)
  }

  class Embedder { <<interface>> +embedDocuments() +embedQuery() }
  class VectorIndex { <<interface>> +build() +search() }
  class ChunkSource { <<interface>> +load() }
  class FigureStore { <<interface>> +load() +readImage() }

  TransformersEmbedder ..|> Embedder
  InMemoryVectorIndex ..|> VectorIndex
  ChunkFileSource ..|> ChunkSource
  FigureFileSource ..|> FigureStore
  TransportFactory ..> StdioTransport
  TransportFactory ..> HttpTransport

  note for Embedder "owned by domain —<br/>shown only to anchor implements<br/>(same for VectorIndex/ChunkSource/<br/>FigureStore)"
```

### interface_mcp

**Responsibility**: everything a connecting MCP client can see and call — the
`swebok_search` tool, the two prompts, figure resources, completions, and
sampling — plus the factory that assembles them all onto one `McpServer`.
**Concepts**:
- **tool / prompt / resource** — the three kinds of capability the Model
  Context Protocol lets a server expose: a callable function (tool), a
  reusable templated conversation starter (prompt), and a piece of
  server-held data addressed by URI (resource — here, figure images).

```mermaid
classDiagram
  class ServerTool {
    <<interface>>
    +register(server)
  }
  class SwebokSearchTool {
    +register(server)
  }
  class ServerFactory {
    +create() McpServer
  }
  class FigureResources {
    <<module>>
    +registerResources(server, retriever)
    +figureUri(id) str
  }
  class SwebokExplainPrompt {
    <<module>>
    +registerPrompts(server)
  }
  class SwebokSkillMakerPrompt {
    <<module>>
    +registerSwebokSkillMakerPrompt(server)
  }
  class Completions {
    <<module>>
    +registerCompletions(server)
  }
  class Sampling {
    <<module>>
    +requestSampling(server, params)
  }

  class Retriever { <<type>> +initialize() +search() +figuresFor() +figureImage() +allFigures() +chunkCount }

  SwebokSearchTool ..|> ServerTool
  SwebokSearchTool --> Retriever
  SwebokSearchTool ..> FigureResources
  ServerFactory --> Retriever
  ServerFactory --> ServerTool
  ServerFactory ..> FigureResources
  ServerFactory ..> SwebokExplainPrompt
  ServerFactory ..> SwebokSkillMakerPrompt
  ServerFactory ..> Completions
  FigureResources --> Retriever

  note for Retriever "owned by application —<br/>shown only to anchor these calls"
  note for Sampling "standalone helper; not<br/>registered/wired here — called<br/>ad hoc from tool/prompt handlers"
```

### di

**Responsibility**: the composition root — the only place that binds each
`domain` port to its concrete `infrastructure` adapter and assembles the
object graph the rest of the app runs on.
**Concepts**:
- **token** — the DI key (`TYPES.Embedder`, etc.) a binding is registered and
  looked up under, since TypeScript interfaces don't exist at runtime and
  can't be used as container keys directly.

```mermaid
classDiagram
  class Container {
    <<module>>
    +buildContainer(config) Container
  }
  class Tokens {
    <<module>>
    +Config
    +ServerTool
    +Embedder
    +ChunkSource
    +FigureStore
    +VectorIndex
  }

  class Retriever { <<type>> +initialize() +search() +figuresFor() +figureImage() +allFigures() +chunkCount }
  class ServerFactory { <<type>> +create() }
  class TransformersEmbedder { <<type>> }
  class InMemoryVectorIndex { <<type>> +build() +search() }
  class ChunkFileSource { <<type>> }
  class FigureFileSource { <<type>> }
  class SwebokSearchTool { <<type>> +register() }

  Container --> Tokens
  Container ..> Retriever
  Container ..> ServerFactory
  Container ..> TransformersEmbedder
  Container ..> InMemoryVectorIndex
  Container ..> ChunkFileSource
  Container ..> FigureFileSource
  Container ..> SwebokSearchTool

  note for Container "Composition root: binds ports<br/>to adapters (DI, not service location)."
  note for Retriever "owned by application —<br/>shown only to anchor what Container wires"
  note for ServerFactory "owned by interface_mcp<br/>(same for SwebokSearchTool)"
  note for TransformersEmbedder "owned by infrastructure<br/>(same for InMemoryVectorIndex/<br/>ChunkFileSource/FigureFileSource)"
```
> Exception to the usual "no cross-module edges" rule: `di`'s whole job is
> wiring concrete instances from other modules, so enumerating exactly what it
> wires **is** its detailed contract — unlike other modules, that wiring list
> belongs here, not just abstracted away in the Module Contract diagram.

### config

**Responsibility**: reads process environment variables into one typed
`Config` object used everywhere else that needs a setting (transport, model
name, top-k default, ...).

```mermaid
classDiagram
  class Config { <<type>> }
  class ConfigModule {
    <<module>>
    +loadConfig(env) Config
  }

  ConfigModule --> Config
```

### app

**Responsibility**: the process entry point — loads config, builds the
container, gets a `ServerFactory` from it, and connects the resulting
`McpServer` over the configured transport.

```mermaid
classDiagram
  class Main {
    <<module>>
    +main()
  }

  class Container { <<type>> +buildContainer() }
  class ServerFactory { <<type>> +create() }
  class Retriever { <<type>> +initialize() +search() +figuresFor() +figureImage() +allFigures() +chunkCount }
  class TransportFactory { <<type>> +createTransport() }

  Main ..> Container
  Main ..> ServerFactory
  Main ..> Retriever
  Main ..> TransportFactory

  note for Container "owned by di; ServerFactory by<br/>interface_mcp; Retriever by application;<br/>TransportFactory by infrastructure —<br/>shown only to anchor Main's bootstrap sequence"
```
> Same exception as `di`: `app`/`Main` is a thin bootstrap script whose entire
> content is "config -> container -> factory -> connect", so its wiring
> sequence is shown in full rather than abstracted.

## Changelog
| Date | Since -> Updated | Summary |
|------|------------------|---------|
| 2026-08-22 | (re-anchor) -> 2026-08-22T21:54:59.296Z | Switched the anchor from a git commit SHA to a timestamp, so the diagram no longer has to be committed together with (or right after) the code it describes, and uncommitted working-tree edits are detected too (via file mtime), not just committed ones. The helper script (`diagram-status.mjs`) was rewritten accordingly: it compares `git log --since` output plus `git status --porcelain` (mtime-filtered) against the marker's `updated:` line instead of diffing two commits. Prior rows below predate this change and still cite commit ranges as historical fact. |
| 2026-08-22 | fc284e4 (module descriptions) | Added a **Responsibility** line (and a **Concepts** glossary where the module introduces domain terms) to all 15 module sections, per the skill's new convention — orientation text before each class diagram, kept tight (a few sentences/bullets, not documentation). |
| 2026-08-22 | fc284e4 (stub methods) | Reference stubs now show method **names only** (no params/return types, e.g. `+search()`) instead of being fully empty — enough to see at a glance what the referenced port/class offers. Data-type stubs with genuinely no members in their own module's diagram (`Chunk`, `TransformersEmbedder`, `ChunkFileSource`, `FigureFileSource`, ...) stay bare. Updated the skill's convention to match. |
| 2026-08-22 | fc284e4 (note wrapping) | Kept `note for` (not the display-label variant tried briefly in between) for marking a reference stub's real owner. The actual truncation problem was that Mermaid does not auto-wrap long note text — fixed by hard-wrapping every note in this file with `<br/>` every ~6-8 words. This wrapping rule now applies to every note the skill writes, not just stub-ownership ones. |
| 2026-08-22 | fc284e4 (restructure) | Reworked into three zoom levels per the `system-class-diagram` skill's new format: Context (unchanged) -> per-subsystem **Module Contract** diagram (one box per module, contract-only members) -> one **class diagram per module** (cross-module "uses" edges dropped in favor of the Module Contract diagram; cross-module "implements" edges and the `di`/`app` wiring exceptions kept via reference stubs). Also split KnowledgeBasePipeline's `Factory` out of `shared` into its own `di` module, mirroring the Server side, so `shared`/`config` hold only real value-bearing contracts. No underlying code changed in this pass — same commit as the previous entry. |
| 2026-08-22 | e4d121e..fc284e4 | `Factory.build_chunker` now takes `source_id` (per-source taxonomy resolution, part of the KnowledgeBasePipeline multi-chapter/multi-source extension). `Cli` and `StructureChunker` also changed (new per-source pipeline assembly, per-source cleaner header pattern, oversized-run word-slicing) but only via private (`_`-prefixed) helpers, which the diagram omits by convention — no other node/edge changes. |
| 2026-08-18 | b17f905..e4d121e | Add `SwebokSkillMakerPrompt` module node (`prompts/swebokSkillMaker.ts`, `registerSwebokSkillMakerPrompt(server)`) and its `ServerFactory ..> SwebokSkillMakerPrompt` edge, alongside the existing `SwebokExplainPrompt`. |
| 2026-08-13 | fd9f1a6..b17f905 | Re-anchor. `ChunkFileSource`/`FigureFileSource` (previously git-ignored, now tracked) were already represented; other changes were skill/tooling/docs only — no diagram body change. |
| 2026-08-13 | fd9f1a6 (correction) | One node per file: split MCP registrars (figure resources / swebokExplain prompt / completions / sampling) and transport (factory / stdio / http); add CLI, entrypoint (Main), figure-extract tool, DI tokens. |
| 2026-08-13 | initial @ fd9f1a6 | Initial diagram: KnowledgeBasePipeline ports/adapters (Python) + Server layered/hexagonal architecture (TypeScript MCP). |
