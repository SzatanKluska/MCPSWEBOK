<!-- system-class-diagram
commit: e4d121e7e8d5b81fd10919ddc852075e3092984f
updated: 2026-08-18
-->
# System Class Diagram

> Auto-maintained by the `system-class-diagram` skill. Anchored to the commit in
> the marker above. Run the skill to refresh after new commits.

The system has two subsystems that meet at a file-based handoff contract: the
**KnowledgeBasePipeline** (Python) produces the knowledge base; the **Server**
(TypeScript, MCP) consumes it.

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

Ports & adapters: the `Pipeline` core depends only on the port protocols; the
`Factory` wires concrete adapters from `config.yaml`.

```mermaid
classDiagram
  direction LR

  namespace ports {
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
  }

  namespace core {
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
  }

  namespace adapters {
    class PdfPlumberExtractor
    class BasicCleaner
    class SwebokTaxonomyMapper
    class StructureChunker
    class SentenceTransformersEmbedder
    class NumpyVectorStore
    class ChromaVectorStore
  }

  namespace models {
    class Document
    class Section
    class Chunk
    class Page
    class Line
  }

  namespace figures {
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
  }

  namespace shared {
    class Config {
      +path(keys) str
    }
    class Factory {
      <<module>>
      +build_extractor(cfg) DocumentExtractor
      +build_chunker(cfg) Chunker
      +build_embedder(cfg) Embedder
      +build_vector_store(cfg) VectorStore
    }
  }

  namespace app {
    class Cli {
      <<module>>
      +prepare()
      +index()
      +query(text)
      +eval()
    }
  }

  PdfPlumberExtractor ..|> DocumentExtractor
  BasicCleaner ..|> TextCleaner
  SwebokTaxonomyMapper ..|> TaxonomyMapper
  StructureChunker ..|> Chunker
  SentenceTransformersEmbedder ..|> Embedder
  NumpyVectorStore ..|> VectorStore
  ChromaVectorStore ..|> VectorStore

  Pipeline --> DocumentExtractor
  Pipeline --> TextCleaner
  Pipeline --> TaxonomyMapper
  Pipeline --> Chunker
  Pipeline --> Embedder
  Pipeline --> VectorStore
  Pipeline --> PipelineResult
  Pipeline --> QualityReport

  Factory --> Config
  StructureChunker --> Chunk
  StructureChunker ..> FiguresSidecar
  FiguresSidecar --> Figure
  Document *-- Page
  Page *-- Line
  PipelineResult --> Document
  PipelineResult --> Chunk

  Cli --> Pipeline
  Cli --> Factory
  Cli ..> FiguresSidecar
  Cli --> Config

  note for Factory "Builds each adapter from config (the DI point)."
  note for FigureExtract "One-off tool: renders figure JPGs into KnowledgeBase/figures."
```

## Server (TypeScript · MCP)

Layered / hexagonal: dependencies point inward (`interface -> application ->
domain`); `infrastructure` implements the domain ports; `di` and `config` are
cross-cutting bootstrap.

```mermaid
classDiagram
  direction LR

  namespace domain {
    class Chunk {
      <<type>>
    }
    class Figure {
      <<type>>
    }
    class Hit {
      <<type>>
    }
    class ImageBytes {
      <<type>>
    }
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
  }

  namespace application {
    class Retriever {
      +initialize()
      +search(query, k) List~Hit~
      +figuresFor(refs) List~Figure~
      +figureImage(figure) ImageBytes
      +allFigures() List~Figure~
      +chunkCount
    }
  }

  namespace infrastructure {
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
  }

  namespace interface_mcp {
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
  }

  namespace di {
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
  }

  namespace config {
    class Config {
      <<type>>
    }
    class ConfigModule {
      <<module>>
      +loadConfig(env) Config
    }
  }

  namespace app {
    class Main {
      <<module>>
      +main()
    }
  }

  TransformersEmbedder ..|> Embedder
  InMemoryVectorIndex ..|> VectorIndex
  ChunkFileSource ..|> ChunkSource
  FigureFileSource ..|> FigureStore
  SwebokSearchTool ..|> ServerTool

  Retriever --> Embedder
  Retriever --> ChunkSource
  Retriever --> FigureStore
  Retriever --> VectorIndex
  Retriever ..> RetrievalPolicies

  SwebokSearchTool --> Retriever
  SwebokSearchTool ..> RetrievalPolicies
  SwebokSearchTool ..> FigureResources

  ServerFactory --> Retriever
  ServerFactory --> ServerTool
  ServerFactory ..> FigureResources
  ServerFactory ..> SwebokExplainPrompt
  ServerFactory ..> SwebokSkillMakerPrompt
  ServerFactory ..> Completions
  FigureResources --> Retriever

  TransportFactory ..> StdioTransport
  TransportFactory ..> HttpTransport

  ConfigModule --> Config
  Container --> Tokens
  Container ..> Retriever
  Container ..> ServerFactory
  Container ..> TransformersEmbedder
  Container ..> InMemoryVectorIndex
  Container ..> ChunkFileSource
  Container ..> FigureFileSource
  Container ..> SwebokSearchTool

  Main ..> Container
  Main ..> ServerFactory
  Main ..> Retriever
  Main ..> TransportFactory

  note for Container "Composition root: binds ports to adapters (DI, not service location)."
```

## Changelog
| Date | Commit range | Summary |
|------|--------------|---------|
| 2026-08-18 | b17f905..e4d121e | Add `SwebokSkillMakerPrompt` module node (`prompts/swebokSkillMaker.ts`, `registerSwebokSkillMakerPrompt(server)`) and its `ServerFactory ..> SwebokSkillMakerPrompt` edge, alongside the existing `SwebokExplainPrompt`. |
| 2026-08-13 | fd9f1a6..b17f905 | Re-anchor. `ChunkFileSource`/`FigureFileSource` (previously git-ignored, now tracked) were already represented; other changes were skill/tooling/docs only — no diagram body change. |
| 2026-08-13 | fd9f1a6 (correction) | One node per file: split MCP registrars (figure resources / swebokExplain prompt / completions / sampling) and transport (factory / stdio / http); add CLI, entrypoint (Main), figure-extract tool, DI tokens. |
| 2026-08-13 | initial @ fd9f1a6 | Initial diagram: KnowledgeBasePipeline ports/adapters (Python) + Server layered/hexagonal architecture (TypeScript MCP). |
