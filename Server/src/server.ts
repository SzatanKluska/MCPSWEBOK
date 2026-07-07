import { McpServer } from "@modelcontextprotocol/server";

import type { Config } from "./config.js";
import { registerTools } from "./tools/index.js";
import { registerResources } from "./resources/index.js";
import { registerPrompts } from "./prompts/index.js";
import { registerCompletions } from "./completions/index.js";

/**
 * Builds and configures the MCP server instance.
 *
 * Extension points:
 *  - tools/index.ts       — registerTools()       (client calls server)
 *  - resources/index.ts   — registerResources()   (client reads server data)
 *  - prompts/index.ts     — registerPrompts()     (client uses server templates)
 *  - completions/index.ts — registerCompletions() (argument autocompletion for
 *                           prompts & resource templates — add `complete`
 *                           callbacks inside registerPrompts/registerResources)
 *  - sampling/index.ts    — requestSampling()     (server asks client for LLM
 *                           inference; NOT registered here — call from handlers)
 */
export function createServer(config: Config): McpServer {
  const server = new McpServer({
    name: config.serverName,
    version: config.serverVersion,
  });

  registerTools(server);
  registerResources(server);
  registerPrompts(server);
  registerCompletions(server);

  return server;
}
