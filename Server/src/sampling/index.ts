import type { McpServer } from "@modelcontextprotocol/server";
import type { CreateMessageRequestParams, CreateMessageResult } from "@modelcontextprotocol/server";

/**
 * Requests LLM inference from the connected MCP client (Sampling).
 *
 * Sampling is server-initiated — the server asks the *client* (e.g. VS Code,
 * Claude Desktop) to run an LLM completion and return the result. This is the
 * reverse direction compared to tools/resources/prompts, so it is not
 * registered at startup but called from within request handlers (e.g. from a
 * tool handler that needs to reason before responding).
 *
 * Prerequisites:
 *   - The client must declare `{ sampling: {} }` in its `capabilities` during
 *     the `initialize` handshake. If not, this will throw.
 *   - The server must already be connected (`server.connect()` called).
 *
 * Usage example (inside a tool handler):
 * ```ts
 * import { requestSampling } from "../sampling/index.js";
 *
 * const result = await requestSampling(server, {
 *   messages: [{ role: "user", content: { type: "text", text: prompt } }],
 *   maxTokens: 1024,
 * });
 * return { content: [{ type: "text", text: result.content.text ?? "" }] };
 * ```
 *
 * TODO: wrap with error handling for clients that do not support sampling.
 */
export async function requestSampling(
  server: McpServer,
  params: CreateMessageRequestParams,
): Promise<CreateMessageResult> {
  return server.server.createMessage(params);
}
