/**
 * Composition root — the only place that references the IoC container. It binds
 * concrete implementations; every component receives its dependencies through
 * its constructor (`@inject`), never by reaching into the container. That is the
 * line that keeps this Dependency Injection and not Service Location.
 *
 * All bindings are singletons (an MCP stdio server is a single long-lived
 * process). Per-request scopes (`inRequestScope`) become relevant once the HTTP
 * transport with concurrent sessions lands.
 */
import { Container } from "inversify";

import type { Config } from "../config.js";
import { Embedder } from "../rag/embedder.js";
import { Retriever } from "../rag/retriever.js";
import { ServerFactory } from "../server.js";
import type { ServerTool } from "../tools/serverTool.js";
import { SwebokSearchTool } from "../tools/swebokSearchTool.js";
import { TYPES } from "./types.js";

export function buildContainer(config: Config): Container {
  const container = new Container({ defaultScope: "Singleton" });

  container.bind<Config>(TYPES.Config).toConstantValue(config);
  container.bind(Embedder).toSelf();
  container.bind(Retriever).toSelf();
  container.bind(ServerFactory).toSelf();

  // Tools are registered under a shared token so ServerFactory can collect them
  // all via @multiInject. Adding a tool = one more bind() line here.
  container.bind<ServerTool>(TYPES.ServerTool).to(SwebokSearchTool);

  return container;
}
