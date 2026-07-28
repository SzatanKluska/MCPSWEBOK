#!/usr/bin/env node
import "reflect-metadata";

import { loadConfig, type Config } from "./config.js";
import { buildContainer } from "./di/container.js";
import { Retriever } from "./rag/retriever.js";
import { ServerFactory } from "./server.js";
import { createTransport } from "./transport/index.js";

async function main(): Promise<void> {
  const config = loadConfig();
  const container = buildContainer(config);

  // Resolve the retriever asynchronously: this triggers its @postConstruct
  // warm-up (load + embed chunks) so the first tool call is instant.
  // Progress goes to stderr (stdout is the JSON-RPC stream on stdio).
  process.stderr.write(
    `[${config.serverName}] loading knowledge base from ${config.knowledgeBasePath} ...\n`,
  );
  const retriever = await container.getAsync(Retriever);
  process.stderr.write(
    `[${config.serverName}] indexed ${retriever.chunkCount} chunks\n`,
  );

  const factory = await container.getAsync(ServerFactory);
  const server = factory.create();
  const transport = createTransport(config);

  await server.connect(transport);
  logStartup(config);
  // On stdio the process stays alive, reading JSON-RPC from stdin.
}

function logStartup(config: Config): void {
  // stdout is reserved for the JSON-RPC stream on stdio — log to stderr.
  process.stderr.write(
    `[${config.serverName}] v${config.serverVersion} started on ${config.transport} transport\n`,
  );
}

main().catch((error: unknown) => {
  const message =
    error instanceof Error ? (error.stack ?? error.message) : String(error);
  process.stderr.write(`Fatal: ${message}\n`);
  process.exitCode = 1;
});
