/**
 * Retriever: the application's retrieval use case. Orchestrates the outbound
 * ports (embedder, chunk source, vector index, figure store) — it knows the
 * *what* (load -> embed -> index -> search, join figures by reference) but none
 * of the *how* (transformers.js, filesystem, cosine math live in adapters).
 *
 * The index needs an async warm-up (load chunks + embed them). Constructors
 * can't be async, so the work lives in an async `@postConstruct` hook that
 * Inversify awaits when the instance is resolved with `container.getAsync`.
 */
import { inject, injectable, postConstruct } from "inversify";

import type { Config } from "../config/config.js";
import { TYPES } from "../di/types.js";
import {
  figuresForRefs,
  type ChunkSource,
  type Embedder,
  type FigureStore,
  type VectorIndex,
} from "../domain/retrieval.js";
import type { Chunk, Figure, Hit, ImageBytes } from "../domain/types.js";

@injectable()
export class Retriever {
  private chunks: Chunk[] = [];
  private figuresById = new Map<string, Figure>();
  readonly defaultTopK: number;

  constructor(
    @inject(TYPES.Embedder) private readonly embedder: Embedder,
    @inject(TYPES.ChunkSource) private readonly chunkSource: ChunkSource,
    @inject(TYPES.FigureStore) private readonly figureStore: FigureStore,
    @inject(TYPES.VectorIndex) private readonly index: VectorIndex,
    @inject(TYPES.Config) config: Config,
  ) {
    this.defaultTopK = config.defaultTopK;
  }

  /** Number of indexed chunks (0 until {@link initialize} completes). */
  get chunkCount(): number {
    return this.chunks.length;
  }

  /** Async warm-up: load chunks -> embed all -> build index -> load figures. */
  @postConstruct()
  async initialize(): Promise<void> {
    this.chunks = this.chunkSource.load();
    if (this.chunks.length === 0) {
      throw new Error(
        "No chunks found in the knowledge base. Build it first " +
          "(run the pipeline: 'kbprep.cli index').",
      );
    }
    const vectors = await this.embedder.embedDocuments(
      this.chunks.map((c) => c.text),
    );
    this.index.build(this.chunks, vectors);
    this.figuresById = this.figureStore.load();
  }

  /** Figures referenced by the given ids (e.g. from a chunk's `figure_refs`). */
  figuresFor(figureRefs: string[] | undefined): Figure[] {
    return figuresForRefs(figureRefs, this.figuresById);
  }

  /** Reads a figure's image bytes (base64 + mime) from the knowledge base. */
  figureImage(figure: Figure): ImageBytes | null {
    return this.figureStore.readImage(figure);
  }

  /** All loaded figures (for exposing them as MCP resources). */
  allFigures(): Figure[] {
    return Array.from(this.figuresById.values());
  }

  /** Embeds the query and returns the top-k most similar chunks. */
  async search(query: string, k: number): Promise<Hit[]> {
    const vector = await this.embedder.embedQuery(query);
    return this.index.search(vector, k);
  }
}
