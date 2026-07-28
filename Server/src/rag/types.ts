/**
 * Neutral data structures for the retrieval layer.
 *
 * A {@link Chunk} mirrors one line of the RAG pipeline's `chunks.jsonl` handoff
 * artifact (see `RAG/pipeline/src/ragprep/models.py`). Only fields the server
 * consumes are typed; the shape is intentionally permissive (nullable metadata)
 * because taxonomy mapping may leave topic fields empty.
 */
export interface Chunk {
  id: string;
  text: string;
  source_id: string;
  source_type: string;
  ka_id: string | null;
  ka_name: string | null;
  topic_id: string | null;
  topic_name: string | null;
  section_heading: string | null;
  page_start: number | null;
  page_end: number | null;
  language: string | null;
  token_count: number | null;
  checksum: string | null;
}

/** A single retrieval result: a chunk and its similarity score (higher = closer). */
export interface Hit {
  chunk: Chunk;
  score: number;
}
