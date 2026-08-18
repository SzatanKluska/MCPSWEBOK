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

// True for a source file that must map to a diagram node (excludes package markers).
function isSourceFile(f) {
  return (f.startsWith("KnowledgeBasePipeline/kbprep/") || f.startsWith("Server/src/")) &&
    (f.endsWith(".py") || f.endsWith(".ts")) && !f.endsWith("__init__.py");
}

// Code files the diagram must cover (one node per file).
function inventory() {
  return git("ls-files -- KnowledgeBasePipeline/kbprep Server/src").split(/\r?\n/).filter(isSourceFile);
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

const changed = git(`diff --name-status ${stored} ${head}`);
const changedPaths = changed.split(/\r?\n/).flatMap((l) => l.split(/\t/).slice(1)).filter(Boolean);
const sourceChanged = changedPaths.filter(isSourceFile);

// Only docs/tooling changed since STORED -> the diagram body still reflects the code.
if (sourceChanged.length === 0) {
  out({ MODE: "up-to-date", DIAGRAM: rel, HEAD: head, HEAD_SHORT: headShort, STORED: stored,
        NOTE: "only docs/tooling changed since STORED; no source files affected" });
  process.exit(0);
}

out({ MODE: "update", DIAGRAM: rel, HEAD: head, HEAD_SHORT: headShort, STORED: stored });
console.log("--- CHANGED SOURCE FILES ---");
console.log(sourceChanged.join("\n"));
console.log("--- ALL CHANGED FILES ---");
console.log(changed || "(none)");
console.log("--- COMMITS ---");
console.log(git(`log --oneline ${stored}..${head}`) || "(none)");
printInventory();
