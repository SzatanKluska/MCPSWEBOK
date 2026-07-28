/**
 * Loads the knowledge base handoff artifact (`chunks.jsonl`) produced by the
 * RAG pipeline. Each non-empty line is a JSON-serialized {@link Chunk}.
 */
import { readFileSync } from "node:fs";

import type { Chunk } from "./types.js";

export function loadChunks(path: string): Chunk[] {
  const raw = readFileSync(path, "utf-8");
  const chunks: Chunk[] = [];
  for (const line of raw.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (trimmed.length === 0) {
      continue;
    }
    chunks.push(JSON.parse(trimmed) as Chunk);
  }
  return chunks;
}
