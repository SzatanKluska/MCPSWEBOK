#!/usr/bin/env node
// Reports whether the system class diagram must be created, updated, or is current.
// Anchored to a TIMESTAMP (not a commit) recorded in the diagram's own provenance
// marker, so it also catches uncommitted working-tree changes — not just
// changes reachable from HEAD. That means the diagram never has to be
// committed in lockstep with the code it describes.
// Usage: node diagram-status.mjs [diagramPathRelativeToRepoRoot]
import { execSync } from "node:child_process";
import { existsSync, readFileSync, statSync } from "node:fs";
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

// Code files the diagram must cover (one node per file). Reflects the current
// working tree (includes uncommitted new files), not just what's committed.
function inventory() {
  const tracked = git("ls-files -- KnowledgeBasePipeline/kbprep Server/src").split(/\r?\n/);
  const untracked = git(
    "ls-files --others --exclude-standard -- KnowledgeBasePipeline/kbprep Server/src"
  ).split(/\r?\n/);
  return [...new Set([...tracked, ...untracked])].filter(isSourceFile).sort();
}

function printInventory() {
  console.log("--- SOURCE INVENTORY (each file must map to >=1 diagram node) ---");
  for (const f of inventory()) console.log(f);
}

// Uncommitted changes (staged + unstaged + untracked), as {status, path} pairs,
// restricted to files whose on-disk mtime is after `stored` (so an uncommitted
// edit already reconciled by a previous run of this skill isn't flagged again).
function workingTreeChanges(repoRoot, stored) {
  const raw = git("status --porcelain");
  if (!raw) return [];
  const changes = [];
  for (const line of raw.split(/\r?\n/)) {
    if (!line) continue;
    const status = line.slice(0, 2).trim();
    let path = line.slice(3);
    if (path.includes(" -> ")) path = path.split(" -> ")[1]; // renames
    path = path.replace(/^"|"$/g, "");
    if (status === "D") {
      changes.push({ status, path }); // deleted: no mtime to check, always report
      continue;
    }
    const abs = resolve(repoRoot, path);
    if (!existsSync(abs)) continue;
    if (statSync(abs).mtime > stored) changes.push({ status, path });
  }
  return changes;
}

// Committed changes in commits whose commit date is after `stored`.
function committedChanges(stored) {
  const raw = git(`log --since="${stored.toISOString()}" --name-status --pretty=format:`);
  const changes = [];
  for (const line of raw.split(/\r?\n/)) {
    if (!line.trim()) continue;
    const [status, ...rest] = line.split(/\t/);
    const path = rest[rest.length - 1];
    changes.push({ status: status.trim(), path });
  }
  return changes;
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
const now = new Date();

if (!existsSync(diagramPath)) {
  out({ MODE: "create", DIAGRAM: rel, NOW: now.toISOString() });
  printInventory();
  process.exit(0);
}

const content = readFileSync(diagramPath, "utf8");
const marker = content.match(/updated:\s*([0-9T:.Z+-]{16,32})/i);
if (!marker) {
  out({ MODE: "create", DIAGRAM: rel, NOW: now.toISOString(),
        NOTE: "diagram exists but has no parseable 'updated:' timestamp; regenerate" });
  printInventory();
  process.exit(0);
}

const stored = new Date(marker[1]);
if (isNaN(stored.getTime())) {
  out({ MODE: "create", DIAGRAM: rel, NOW: now.toISOString(),
        NOTE: `stored timestamp '${marker[1]}' is not parseable; regenerate` });
  printInventory();
  process.exit(0);
}

const changed = [...committedChanges(stored), ...workingTreeChanges(repoRoot, stored)];
// De-dupe by path, keeping the first (committed) status if a file appears in both.
const byPath = new Map();
for (const c of changed) if (!byPath.has(c.path)) byPath.set(c.path, c.status);
const sourceChanged = [...byPath.entries()].filter(([p]) => isSourceFile(p));

if (sourceChanged.length === 0) {
  out({ MODE: "up-to-date", DIAGRAM: rel, STORED: stored.toISOString(), NOW: now.toISOString() });
  process.exit(0);
}

out({ MODE: "update", DIAGRAM: rel, STORED: stored.toISOString(), NOW: now.toISOString() });
console.log("--- CHANGED SOURCE FILES (status<TAB>path; committed + uncommitted) ---");
for (const [path, status] of sourceChanged) console.log(`${status}\t${path}`);
console.log("--- COMMITS SINCE STORED ---");
console.log(git(`log --oneline --since="${stored.toISOString()}"`) || "(none)");
console.log("--- UNCOMMITTED WORKING-TREE CHANGES (status<TAB>path) ---");
const wt = workingTreeChanges(repoRoot, stored);
console.log(wt.length ? wt.map((c) => `${c.status}\t${c.path}`).join("\n") : "(none)");
printInventory();
