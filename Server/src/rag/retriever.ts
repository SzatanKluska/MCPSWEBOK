/**
 * Retriever: the RAG entry point the search tool depends on. An injectable
 * singleton whose dependencies (embedder, config) arrive via the constructor.
 *
 * The index needs an async warm-up (load `chunks.jsonl` + embed every chunk).
 * Constructors can't be async, so the work lives in an async `@postConstruct`
 * hook — Inversify awaits it when the instance is resolved with
 * `container.getAsync`. Both documents and queries are embedded by the same
 * in-process model, so their vectors share one space (the persisted
 * `vectors.npz` from Python is not consumed).
 */
import { join } from "node:path";

import { inject, injectable, postConstruct } from "inversify";

import type { Config } from "../config.js";
import { TYPES } from "../di/types.js";
import { Embedder } from "./embedder.js";
import { loadChunks } from "./knowledgeBase.js";
import { loadFigures, readFigureImage } from "./figures.js";
import type { Figure, Hit } from "./types.js";
import { VectorStore } from "./vectorStore.js";

@injectable()
export class Retriever {
  private store: VectorStore | null = null;
  private figures = new Map<string, Figure>();
  private count = 0;
  readonly defaultTopK: number;

  constructor(
    @inject(Embedder) private readonly embedder: Embedder,
    @inject(TYPES.Config) private readonly config: Config,
  ) {
    this.defaultTopK = config.defaultTopK;
  }

  /** Number of indexed chunks (0 until {@link initialize} completes). */
  get chunkCount(): number {
    return this.count;
  }

  /** Async warm-up: load chunks -> embed all -> build in-memory store. */
  @postConstruct()
  async initialize(): Promise<void> {
    const chunksPath = join(this.config.knowledgeBasePath, "chunks.jsonl");
    const chunks = loadChunks(chunksPath);
    if (chunks.length === 0) {
      throw new Error(
        `No chunks found in ${chunksPath}. Build the knowledge base first ` +
          `(run the RAG pipeline: 'ragprep.cli index').`,
      );
    }
    const vectors = await this.embedder.embedDocuments(
      chunks.map((c) => c.text),
    );
    this.store = new VectorStore(chunks, vectors);
    this.figures = loadFigures(join(this.config.knowledgeBasePath, "figures.jsonl"));
    this.count = chunks.length;
  }

  /** Figures referenced by the given ids (e.g. from a chunk's `figure_refs`). */
  figuresFor(figureRefs: string[] | undefined): Figure[] {
    if (!figureRefs) {
      return [];
    }
    const found: Figure[] = [];
    for (const id of figureRefs) {
      const figure = this.figures.get(id);
      if (figure) {
        found.push(figure);
      }
    }
    return found;
  }

  /** Reads a figure's image bytes (base64 + mime) from the knowledge base. */
  figureImage(figure: Figure): { data: string; mimeType: string } | null {
    return readFigureImage(this.config.knowledgeBasePath, figure);
  }

  /** Embeds the query and returns the top-k most similar chunks. */
  async search(query: string, k: number): Promise<Hit[]> {
    if (this.store === null) {
      throw new Error("Retriever used before initialization completed.");
    }
    const vector = await this.embedder.embedQuery(query);
    return this.store.search(vector, k);
  }
}
