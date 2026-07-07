#!/usr/bin/env node
import { loadConfig, type Config } from "./config.js";
import { createServer } from "./server.js";
import { createTransport } from "./transport/index.js";

async function main(): Promise<void> {
  const config = loadConfig();
  const server = createServer(config);
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
