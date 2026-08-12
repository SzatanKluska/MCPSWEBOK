#!/usr/bin/env node
// Reports whether the system class diagram must be created, updated, or is current.
// Usage: node diagram-status.mjs [diagramPathRelativeToRepoRoot]
import { execSync } from "node:child_process";
import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";

const DEFAULT_REL = "docs/architecture/system-class-diagram.md";

function git(args) {
  return execSync(`git ${args}`, { encoding: "utf8" }).trim();
}

function out(obj) {
  for (const [k, v] of Object.entries(obj)) console.log(`${k}: ${v}`);
}

// Code files the diagram must cover (one node per file); excludes package markers.
function inventory() {
  return git("ls-files -- KnowledgeBasePipeline/kbprep Server/src")
    .split(/\r?\n/)
    .filter((f) => (f.endsWith(".py") || f.endsWith(".ts")) && !f.endsWith("__init__.py"));
}

function printInventory() {
  console.log("--- SOURCE INVENTORY (each file must map to >=1 diagram node) ---");
  for (const f of inventory()) console.log(f);
}

let repoRoot;
try {
  repoRoot = git("rev-parse --show-toplevel");
} catch {
  console.log("ERROR: not a git repository");
  process.exit(1);
}

const rel = process.argv[2] ?? DEFAULT_REL;
const diagramPath = resolve(repoRoot, rel);
const head = git("rev-parse HEAD");
const headShort = git("rev-parse --short HEAD");

if (!existsSync(diagramPath)) {
  out({ MODE: "create", DIAGRAM: rel, HEAD: head, HEAD_SHORT: headShort });
  printInventory();
  process.exit(0);
}

const content = readFileSync(diagramPath, "utf8");
const marker = content.match(/commit:\s*([0-9a-f]{7,40})/i);
if (!marker) {
  out({ MODE: "create", DIAGRAM: rel, HEAD: head, HEAD_SHORT: headShort,
        NOTE: "diagram exists but has no commit marker; regenerate" });
  printInventory();
  process.exit(0);
}

let stored;
try {
  stored = git(`rev-parse ${marker[1]}`);
} catch {
  out({ MODE: "create", DIAGRAM: rel, HEAD: head, HEAD_SHORT: headShort,
        NOTE: `stored commit ${marker[1]} not in history; regenerate` });
  printInventory();
  process.exit(0);
}

if (stored === head) {
  out({ MODE: "up-to-date", DIAGRAM: rel, HEAD: head, HEAD_SHORT: headShort, STORED: stored });
  process.exit(0);
}

out({ MODE: "update", DIAGRAM: rel, HEAD: head, HEAD_SHORT: headShort, STORED: stored });
console.log("--- CHANGED FILES ---");
console.log(git(`diff --name-status ${stored} ${head}`) || "(none)");
console.log("--- COMMITS ---");
console.log(git(`log --oneline ${stored}..${head}`) || "(none)");
printInventory();
