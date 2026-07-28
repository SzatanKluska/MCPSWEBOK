/**
 * In-memory vector store with brute-force cosine similarity search — the Node
 * counterpart of the pipeline's NumpyVectorStore. Vectors are expected to be
 * L2-normalized already (the embedder normalizes), so cosine similarity reduces
 * to a dot product. Fast enough for a POC-sized corpus (tens of chunks).
 */
import type { Chunk, Hit } from "./types.js";

export class VectorStore {
  private readonly vectors: Float32Array[];
  private readonly chunks: Chunk[];

  constructor(chunks: Chunk[], vectors: number[][]) {
    this.chunks = chunks;
    this.vectors = vectors.map((v) => Float32Array.from(v));
  }

  /** Returns the top-k chunks most similar to `query`, highest score first. */
  search(query: number[], k: number): Hit[] {
    const q = Float32Array.from(query);
    const scored: Hit[] = this.vectors.map((vec, i) => ({
      chunk: this.chunks[i]!,
      score: dot(vec, q),
    }));
    scored.sort((a, b) => b.score - a.score);
    return scored.slice(0, k);
  }
}

function dot(a: Float32Array, b: Float32Array): number {
  let sum = 0;
  const n = Math.min(a.length, b.length);
  for (let i = 0; i < n; i++) {
    sum += a[i]! * b[i]!;
  }
  return sum;
}
