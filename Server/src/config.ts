/**
 * Runtime configuration for the swebok-mcp server.
 *
 * All knobs are read from environment variables so the same build can run in
 * different contexts without code changes. Transport selection lives here — the
 * rest of the app only sees a resolved {@link Config}.
 */

export type TransportKind = "stdio" | "http";

export interface HttpConfig {
  host: string;
  port: number;
}

export interface Config {
  serverName: string;
  serverVersion: string;
  transport: TransportKind;
  http: HttpConfig;
}

const DEFAULTS = {
  serverName: "swebok-mcp",
  serverVersion: "0.1.0",
  transport: "stdio" as TransportKind,
  httpHost: "127.0.0.1",
  httpPort: 3000,
};

function parseTransport(value: string | undefined): TransportKind {
  const normalized = (value ?? DEFAULTS.transport).toLowerCase();
  if (normalized === "stdio" || normalized === "http") {
    return normalized;
  }
  throw new Error(
    `Invalid MCP_TRANSPORT="${value}". Supported values: "stdio", "http".`,
  );
}

/**
 * Builds a validated {@link Config} from the given environment (defaults to
 * `process.env`).
 */
export function loadConfig(env: NodeJS.ProcessEnv = process.env): Config {
  return {
    serverName: env.MCP_SERVER_NAME ?? DEFAULTS.serverName,
    serverVersion: env.MCP_SERVER_VERSION ?? DEFAULTS.serverVersion,
    transport: parseTransport(env.MCP_TRANSPORT),
    http: {
      host: env.MCP_HTTP_HOST ?? DEFAULTS.httpHost,
      port: Number(env.MCP_HTTP_PORT ?? DEFAULTS.httpPort),
    },
  };
}
