/**
 * `swebok_search` — a retrieval-only RAG search tool. Returns the most relevant
 * SWEBOK passages with citations; the calling LLM synthesizes the final answer.
 *
 * An injectable class: its {@link Retriever} dependency arrives via the
 * constructor, so the tool never reaches into the container (no service
 * location). {@link register} binds it onto an {@link McpServer}.
 */
import { z } from "zod";
import { inject, injectable } from "inversify";

import type { McpServer } from "@modelcontextprotocol/server";
import { Retriever } from "../rag/retriever.js";
import type { ServerTool } from "./serverTool.js";

interface SearchResult {
  rank: number;
  score: number;
  text: string;
  ka_name: string | null;
  topic_name: string | null;
  source_id: string;
  page_start: number | null;
  page_end: number | null;
  section_heading: string | null;
}

function citation(r: SearchResult): string {
  const topic = r.topic_name ?? "(unmapped)";
  const pages =
    r.page_start === null
      ? ""
      : r.page_start === r.page_end
        ? ` p.${r.page_start}`
        : ` pp.${r.page_start}-${r.page_end}`;
  return `[${r.ka_name ?? "?"} > ${topic}, ${r.source_id}${pages}]`;
}

function formatResult(r: SearchResult): string {
  return `#${r.rank} (score ${r.score.toFixed(3)}) ${citation(r)}\n${r.text}`;
}

@injectable()
export class SwebokSearchTool implements ServerTool {
  constructor(@inject(Retriever) private readonly retriever: Retriever) {}

  register(server: McpServer): void {
    server.registerTool(
      "swebok_search",
      {
        title: "SWEBOK Search",
        description:
          "Semantic search over the SWEBOK (Software Engineering Body of " +
          "Knowledge) knowledge base. Returns the most relevant passages with " +
          "citations (knowledge area, source document, pages). Use it to ground " +
          "answers about software engineering topics in authoritative SWEBOK " +
          "text, then synthesize the answer from the returned passages.",
        inputSchema: z.object({
          query: z
            .string()
            .min(1)
            .describe("Natural-language question or search phrase."),
          topK: z
            .number()
            .int()
            .positive()
            .max(20)
            .optional()
            .describe("How many passages to return (default 5)."),
        }),
        outputSchema: z.object({
          results: z.array(
            z.object({
              rank: z.number(),
              score: z.number(),
              text: z.string(),
              ka_name: z.string().nullable(),
              topic_name: z.string().nullable(),
              source_id: z.string(),
              page_start: z.number().nullable(),
              page_end: z.number().nullable(),
              section_heading: z.string().nullable(),
            }),
          ),
        }),
      },
      async ({ query, topK }) => {
        const k = topK ?? this.retriever.defaultTopK;
        const hits = await this.retriever.search(query, k);
        const results: SearchResult[] = hits.map((hit, i) => ({
          rank: i + 1,
          score: hit.score,
          text: hit.chunk.text,
          ka_name: hit.chunk.ka_name,
          topic_name: hit.chunk.topic_name,
          source_id: hit.chunk.source_id,
          page_start: hit.chunk.page_start,
          page_end: hit.chunk.page_end,
          section_heading: hit.chunk.section_heading,
        }));

        const text =
          results.length > 0
            ? results.map(formatResult).join("\n\n")
            : `No SWEBOK passages found for "${query}".`;

        return {
          content: [{ type: "text", text }],
          structuredContent: { results },
        };
      },
    );
  }
}
