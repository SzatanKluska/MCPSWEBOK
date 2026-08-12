import { McpServer } from "@modelcontextprotocol/server";
import { inject, injectable, multiInject } from "inversify";

import type { Config } from "./config.js";
import { TYPES } from "./di/types.js";
import { Retriever } from "./rag/retriever.js";
import type { ServerTool } from "./tools/serverTool.js";
import { registerResources } from "./resources/index.js";
import { registerPrompts } from "./prompts/index.js";
import { registerCompletions } from "./completions/index.js";

/**
 * Builds a configured {@link McpServer}. An injectable factory: its config and
 * the full set of {@link ServerTool}s arrive via the constructor (`@inject` /
 * `@multiInject`), so it never touches the container — proper DI, not service
 * location. Adding a tool is a one-line binding in the composition root; this
 * class does not change.
 *
 * Extension points:
 *  - tools (ServerTool[])  — client calls server; each tool.register(server)
 *  - resources/index.ts    — registerResources()   (client reads server data)
 *  - prompts/index.ts      — registerPrompts()      (client uses server templates)
 *  - completions/index.ts  — registerCompletions()  (argument autocompletion)
 *  - sampling/index.ts     — requestSampling()      (server asks client for LLM
 *                            inference; NOT registered here — call from handlers)
 */
@injectable()
export class ServerFactory {
  constructor(
    @inject(TYPES.Config) private readonly config: Config,
    @inject(Retriever) private readonly retriever: Retriever,
    @multiInject(TYPES.ServerTool) private readonly tools: ServerTool[],
  ) {}

  create(): McpServer {
    const server = new McpServer({
      name: this.config.serverName,
      version: this.config.serverVersion,
    });

    for (const tool of this.tools) {
      tool.register(server);
    }
    registerResources(server, this.retriever);
    registerPrompts(server);
    registerCompletions(server);

    return server;
  }
}
