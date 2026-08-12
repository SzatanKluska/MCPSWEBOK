/**
 * Loads figure records (`figures.jsonl`) produced by the RAG pipeline into a
 * lookup keyed by figure id. Figures are a side artifact — not part of the
 * embedded search index; the retriever attaches them to hits by reference.
 *
 * The file is optional: a knowledge base without figures yields an empty map.
 */
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";

import type { Figure } from "./types.js";

/** Stable resource URI for a figure image (e.g. "swebok://figure/1.4"). */
export function figureUri(id: string): string {
  return `swebok://figure/${id}`;
}

export function loadFigures(path: string): Map<string, Figure> {
  const figures = new Map<string, Figure>();
  if (!existsSync(path)) {
    return figures;
  }
  const raw = readFileSync(path, "utf-8");
  for (const line of raw.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (trimmed.length === 0) {
      continue;
    }
    const figure = JSON.parse(trimmed) as Figure;
    figures.set(figure.figure_id, figure);
  }
  return figures;
}

/**
 * Reads a figure's image as a base64 MCP image block, or null if the file is
 * missing. `figure.image` is relative to the knowledge base folder.
 */
export function readFigureImage(
  knowledgeBasePath: string,
  figure: Figure,
): { data: string; mimeType: string } | null {
  if (!figure.image) {
    return null;
  }
  const path = join(knowledgeBasePath, figure.image);
  if (!existsSync(path)) {
    return null;
  }
  const lower = figure.image.toLowerCase();
  const mimeType = lower.endsWith(".png")
    ? "image/png"
    : lower.endsWith(".jpg") || lower.endsWith(".jpeg")
      ? "image/jpeg"
      : "application/octet-stream";
  return { data: readFileSync(path).toString("base64"), mimeType };
}
