#!/usr/bin/env node
// Reports the actual top-level folder structure of every language project in
// the repo (under each ecosystem's conventional source root), plus — if the
// system-class-diagram output exists — the module/layer names each
// subsystem's Module Contract diagram documents. Purely mechanical: finds
// roots, lists entries, parses box names. Deciding whether a given file
// belongs under a given module, and building a move plan, is the agent's job.
// Usage: node structure-status.mjs [diagramPathRelativeToRepoRoot]
import { execSync } from "node:child_process";
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, join, relative, resolve, sep } from "node:path";

const IGNORE_DIRS = new Set([
  "node_modules", ".git", "dist", "build", "out", "__pycache__",
  ".venv", "venv", "env", ".mypy_cache", ".pytest_cache", ".tox",
  "coverage", ".next", ".turbo",
]);

function git(args) {
  return execSync(`git ${args}`, { encoding: "utf8" }).trim();
}

function walk(dir, depth, out) {
  if (depth < 0) return;
  let names;
  try { names = readdirSync(dir); } catch { return; }
  for (const name of names) {
    if (IGNORE_DIRS.has(name) || name.startsWith(".")) continue;
    const full = join(dir, name);
    let st;
    try { st = statSync(full); } catch { continue; }
    if (st.isDirectory()) {
      out.push(full);
      walk(full, depth - 1, out);
    }
  }
}

function isUnder(child, parent) {
  return child !== parent && child.startsWith(parent + sep);
}

// --- Node/TypeScript projects: every package.json outside IGNORE_DIRS ---
function findNodeProjects(repoRoot) {
  const dirs = [repoRoot];
  walk(repoRoot, 4, dirs);
  const projects = [];
  for (const d of dirs) {
    const pkgPath = join(d, "package.json");
    if (!existsSync(pkgPath)) continue;
    let pkg;
    try { pkg = JSON.parse(readFileSync(pkgPath, "utf8")); } catch { continue; }
    let srcRoot = null;
    const tsconfigPath = join(d, "tsconfig.json");
    if (existsSync(tsconfigPath)) {
      try {
        const raw = readFileSync(tsconfigPath, "utf8").replace(/\/\/.*$/gm, "");
        const tsconfig = JSON.parse(raw);
        const rootDir = tsconfig?.compilerOptions?.rootDir;
        if (rootDir) srcRoot = resolve(d, rootDir);
      } catch { /* ignore unparsable tsconfig */ }
    }
    if (!srcRoot) {
      const guess = join(d, "src");
      srcRoot = existsSync(guess) ? guess : d;
    }
    const name = pkg.name || relative(repoRoot, d) || ".";
    projects.push({ kind: "node", name, projectDir: d, srcRoot });
  }
  return projects;
}

// --- Python projects: any directory containing __init__.py, taking the
// shallowest such directory as the package root (drop ones nested under
// another package dir, so a sub-package doesn't get listed separately) ---
function findPythonProjects(repoRoot) {
  const dirs = [repoRoot];
  walk(repoRoot, 4, dirs);
  const packageDirs = dirs.filter((d) => existsSync(join(d, "__init__.py")));
  const shallow = packageDirs.filter(
    (d) => !packageDirs.some((other) => other !== d && isUnder(d, other)),
  );
  return shallow.map((d) => {
    const parent = dirname(d);
    const projectDir = parent.endsWith(sep + "src") ? dirname(parent) : parent;
    return { kind: "python", name: relative(repoRoot, d) || ".", projectDir, srcRoot: d };
  });
}

function printTopLevel(srcRoot) {
  const entries = readdirSync(srcRoot, { withFileTypes: true })
    .filter((e) => !e.name.startsWith(".") && !IGNORE_DIRS.has(e.name))
    .sort((a, b) => Number(b.isDirectory()) - Number(a.isDirectory()) || a.name.localeCompare(b.name));
  for (const e of entries) {
    console.log(`    ${e.isDirectory() ? "[dir] " : "[file]"} ${e.name}`);
  }
}

// --- Parse documented module names from the system-class-diagram output ---
function parseDocumentedModules(diagramPath) {
  if (!existsSync(diagramPath)) return null;
  const text = readFileSync(diagramPath, "utf8");
  const subsystems = [];
  const headingRe = /^## (.+)$/gm;
  const headings = [...text.matchAll(headingRe)].filter(
    (m) => !/^(Context|Changelog|Reading these diagrams)$/.test(m[1].trim()),
  );
  for (let i = 0; i < headings.length; i++) {
    const title = headings[i][1].trim();
    const start = headings[i].index;
    const end = i + 1 < headings.length ? headings[i + 1].index : text.length;
    const section = text.slice(start, end);
    const contractIdx = section.indexOf("### Module Contract");
    if (contractIdx < 0) continue;
    const fenceStart = section.indexOf("```mermaid", contractIdx);
    const fenceEnd = section.indexOf("```", fenceStart + 10);
    if (fenceStart < 0 || fenceEnd < 0) continue;
    const block = section.slice(fenceStart, fenceEnd);
    const modules = [...block.matchAll(/^\s*class (\w+)\s*\{/gm)].map((m) => m[1]);
    subsystems.push({ title, modules });
  }
  return subsystems;
}

let repoRoot;
try {
  repoRoot = git("rev-parse --show-toplevel");
} catch {
  console.log("ERROR: not a git repository");
  process.exit(1);
}

const diagramArg = process.argv[2] || "docs/architecture/system-class-diagram.md";
const diagramPath = resolve(repoRoot, diagramArg);

console.log("--- LANGUAGE PROJECTS FOUND (mechanical: package.json / __init__.py scan) ---");
const projects = [...findNodeProjects(repoRoot), ...findPythonProjects(repoRoot)];
if (!projects.length) {
  console.log("  none found");
} else {
  for (const p of projects) {
    console.log(`\n[${p.kind}] ${p.name}`);
    console.log(`  project dir: ${relative(repoRoot, p.projectDir) || "."}`);
    console.log(`  source root: ${relative(repoRoot, p.srcRoot) || "."}  (top-level = directly under this)`);
    console.log(`  top-level entries:`);
    printTopLevel(p.srcRoot);
  }
}

console.log("\n--- DOCUMENTED MODULES (from " + (relative(repoRoot, diagramPath) || ".") + ") ---");
const documented = parseDocumentedModules(diagramPath);
if (documented === null) {
  console.log("  diagram not found — run the system-class-diagram skill first,");
  console.log("  or derive module boundaries fresh (see SKILL.md fallback).");
} else if (!documented.length) {
  console.log("  diagram found but no Module Contract sections parsed — check its format.");
} else {
  for (const s of documented) {
    console.log(`\n${s.title}`);
    console.log(`  modules: ${s.modules.join(", ")}`);
  }
}
