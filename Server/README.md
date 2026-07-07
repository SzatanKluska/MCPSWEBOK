# swebok-mcp (server skeleton)

A minimal, runnable **MCP server skeleton** (Node.js + TypeScript, MCP SDK v2)
for the SWEBOK knowledge base. It boots, selects a transport from configuration
(stdio by default), connects, and waits. Tools, resources, and prompts are **not
implemented yet** — the registration points are in place, ready to fill in.

## Layout

```
Server/
  package.json           # scripts + deps (@modelcontextprotocol/server)
  tsconfig.json          # NodeNext, ES2022, strict -> dist/
  src/
    index.ts             # entry: config -> server -> transport -> connect
    config.ts            # env-driven config (transport, name, version)
    server.ts            # builds McpServer, wires the registrars
    transport/
      index.ts           # createTransport(config): the single swap point
      stdio.ts           # stdio transport (implemented)
      http.ts            # Streamable HTTP transport (stub / extension point)
    tools/index.ts       # registerTools()      — empty (TODO)
    resources/index.ts   # registerResources()  — empty (TODO)
    prompts/index.ts     # registerPrompts()    — empty (TODO)
```

## Transport abstraction

Every concrete transport implements the same interface that
`McpServer.connect()` accepts, so `createTransport(config)` in
[`src/transport/index.ts`](src/transport/index.ts) is the only place that knows
which one is active — mirroring the ports & adapters factory used in the RAG
pipeline. `stdio` is implemented; `http` is a typed stub documenting how to add
Streamable HTTP later.

## Prerequisites

- Node.js **>= 20** (`node --version`). If missing on Windows:
  `winget install OpenJS.NodeJS.LTS`.

## Install & build

```powershell
# from Server/
npm install
npm run build      # tsc -> dist/
```

## Run

```powershell
npm start                        # stdio transport (default)
$env:MCP_TRANSPORT="http"; npm start   # -> "not implemented yet" (proves the switch)
```

Development watch mode (auto-restart on change, no manual build):

```powershell
npm run dev
```

## Configuration

All via environment variables:

| Variable             | Default       | Description                          |
|----------------------|---------------|--------------------------------------|
| `MCP_TRANSPORT`      | `stdio`       | `stdio` or `http`                    |
| `MCP_SERVER_NAME`    | `swebok-mcp`  | Server name advertised to clients    |
| `MCP_SERVER_VERSION` | `0.1.0`       | Server version advertised            |
| `MCP_HTTP_HOST`      | `127.0.0.1`   | HTTP bind host (when HTTP is added)  |
| `MCP_HTTP_PORT`      | `3000`        | HTTP bind port (when HTTP is added)  |

## Register in VS Code (example)

After `npm run build`, add an `.vscode/mcp.json` (workspace) entry:

```jsonc
{
  "servers": {
    "swebok-mcp": {
      "type": "stdio",
      "command": "node",
      "args": ["${workspaceFolder}/Server/dist/index.js"]
    }
  }
}
```

## Where to add capabilities

- **Tools** -> [`src/tools/index.ts`](src/tools/index.ts) (`server.registerTool(...)`)
- **Resources** -> [`src/resources/index.ts`](src/resources/index.ts)
- **Prompts** -> [`src/prompts/index.ts`](src/prompts/index.ts)

Each `register*` function currently does nothing; implement inside and it is
picked up automatically by `createServer()`.
