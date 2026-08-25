#!/usr/bin/env node
// Reports two things, both purely mechanical — no semantic judgment:
//
//   1. LANGUAGE PROJECTS FOUND — every project in the repo, its language, the
//      source root that language's own build config or convention puts code
//      under (with the AUTHORITY that decided it), the folders sitting at
//      LEVEL 1 under that root, and any source files loose at the root.
//
//   2. DOCUMENTED MODULES — if an architecture doc in the system-class-diagram
//      format exists, the module names parsed out of each subsystem's
//      `### Module Contract` classDiagram box list.
//
// LEVEL 1 is the only level this skill constrains: it must equal the documented
// module set. Everything deeper is the module's own business and is deliberately
// summarised, not enumerated — this skill never flattens.
//
// Correlating a project to a documented subsystem, deciding which module a file
// belongs to, and building a move plan are all the agent's job.
//
// Usage: node structure-status.mjs [diagramPathRelativeToRepoRoot]

import { execSync } from "node:child_process";
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { join, relative, resolve, sep } from "node:path";

const IGNORED = new Set([
  "node_modules", ".git", ".venv", "venv", "env", "__pycache__", "dist",
  "build", "out", "target", "bin", "obj", ".next", ".nuxt", ".turbo",
  "coverage", ".pytest_cache", ".mypy_cache", ".tox", ".gradle", ".idea",
  ".vscode", "vendor", "Pods", ".dart_tool",
]);

const EXT_BY_LANG = {
  typescript: [".ts", ".tsx"],
  javascript: [".js", ".jsx", ".mjs", ".cjs"],
  python: [".py"],
  go: [".go"],
  rust: [".rs"],
  jvm: [".java", ".kt"],
  dotnet: [".cs"],
  php: [".php"],
  ruby: [".rb"],
};

const posix = (p) => p.split(sep).join("/");

function readJsonc(file) {
  try {
    const raw = readFileSync(file, "utf8")
      .replace(/\/\*[\s\S]*?\*\//g, "")
      .replace(/(^|[^:])\/\/.*$/gm, "$1")
      .replace(/,(\s*[}\]])/g, "$1");
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

function listDirs(dir) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir, { withFileTypes: true })
    .filter((e) => e.isDirectory() && !IGNORED.has(e.name) && !e.name.startsWith("."))
    .map((e) => e.name)
    .sort();
}

function listFiles(dir, exts) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir, { withFileTypes: true })
    .filter((e) => e.isFile() && exts.some((x) => e.name.endsWith(x)))
    .map((e) => e.name)
    .sort();
}

function countDeep(dir, exts) {
  let files = 0;
  let dirs = 0;
  const walk = (d) => {
    let entries;
    try {
      entries = readdirSync(d, { withFileTypes: true });
    } catch {
      return;
    }
    for (const e of entries) {
      if (e.name.startsWith(".") || IGNORED.has(e.name)) continue;
      const p = join(d, e.name);
      if (e.isDirectory()) {
        dirs++;
        walk(p);
      } else if (exts.some((x) => e.name.endsWith(x))) {
        files++;
      }
    }
  };
  walk(dir);
  return { files, dirs };
}

// --- find projects ---------------------------------------------------------

const MANIFESTS = [
  "package.json", "tsconfig.json", "pyproject.toml", "setup.py", "setup.cfg",
  "requirements.txt", "go.mod", "Cargo.toml", "pom.xml", "build.gradle",
  "build.gradle.kts", "composer.json", "Gemfile",
];

function findProjects(root) {
  const found = new Map();
  const walk = (dir, depth) => {
    if (depth > 4) return;
    let entries;
    try {
      entries = readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }
    for (const e of entries) {
      if (e.name.startsWith(".") || IGNORED.has(e.name)) continue;
      const p = join(dir, e.name);
      if (e.isFile()) {
        if (MANIFESTS.includes(e.name) || e.name.endsWith(".csproj")) {
          if (!found.has(dir)) found.set(dir, new Set());
          found.get(dir).add(e.name);
        }
      } else if (e.isDirectory()) {
        walk(p, depth + 1);
      }
    }
  };
  walk(root, 0);
  return found;
}

// --- language + source root ------------------------------------------------

function detectLanguage(dir, manifests) {
  const has = (m) => manifests.has(m);
  if (has("tsconfig.json")) return "typescript";
  if (has("package.json")) {
    const pkg = readJsonc(join(dir, "package.json"));
    const deps = { ...(pkg?.dependencies ?? {}), ...(pkg?.devDependencies ?? {}) };
    return "typescript" in deps ? "typescript" : "javascript";
  }
  if (has("go.mod")) return "go";
  if (has("Cargo.toml")) return "rust";
  if (has("pom.xml") || has("build.gradle") || has("build.gradle.kts")) return "jvm";
  if (has("composer.json")) return "php";
  if (has("Gemfile")) return "ruby";
  if ([...manifests].some((m) => m.endsWith(".csproj"))) return "dotnet";
  if (has("pyproject.toml") || has("setup.py") || has("setup.cfg") || has("requirements.txt")) {
    return "python";
  }
  return "unknown";
}

// root = the directory whose LEVEL 1 must equal the module set.
// authority = which file or language convention decided that.
function detectSourceRoot(dir, lang) {
  const at = (...p) => join(dir, ...p);
  const ok = (p) => existsSync(p) && statSync(p).isDirectory();

  if (lang === "typescript") {
    const ts = readJsonc(at("tsconfig.json"));
    const rootDir = ts?.compilerOptions?.rootDir;
    if (rootDir && ok(at(rootDir))) {
      return { root: at(rootDir), authority: `tsconfig.json compilerOptions.rootDir = "${rootDir}"` };
    }
    const inc = ts?.include?.[0];
    if (inc) {
      const prefix = inc.split("/")[0].replace(/\*+/g, "");
      if (prefix && ok(at(prefix))) {
        return { root: at(prefix), authority: `tsconfig.json include[0] = "${inc}"` };
      }
    }
    if (ok(at("src"))) return { root: at("src"), authority: "Node/TS convention: src/ (no rootDir declared)" };
    return { root: dir, authority: "fallback: package directory" };
  }

  if (lang === "javascript") {
    if (ok(at("src"))) return { root: at("src"), authority: "Node convention: src/" };
    if (ok(at("lib"))) return { root: at("lib"), authority: "Node convention: lib/" };
    return { root: dir, authority: "fallback: package directory" };
  }

  if (lang === "python") {
    const pkgsIn = (base) => listDirs(base).filter((d) => existsSync(join(base, d, "__init__.py")));
    if (ok(at("src"))) {
      const pkgs = pkgsIn(at("src"));
      if (pkgs.length === 1) {
        return { root: at("src", pkgs[0]), authority: `src-layout: src/${pkgs[0]}/ (importable package)` };
      }
      if (pkgs.length > 1) {
        return { root: at("src"), authority: `src-layout, ${pkgs.length} packages: ${pkgs.join(", ")}`, multi: pkgs };
      }
    }
    const pkgs = pkgsIn(dir);
    if (pkgs.length === 1) {
      return { root: at(pkgs[0]), authority: `flat layout: ${pkgs[0]}/ (importable package)` };
    }
    if (pkgs.length > 1) {
      return { root: dir, authority: `flat layout, ${pkgs.length} packages: ${pkgs.join(", ")}`, multi: pkgs };
    }
    return { root: dir, authority: "no __init__.py package found" };
  }

  if (lang === "rust") return { root: at("src"), authority: "Cargo convention: src/" };
  if (lang === "go") return { root: dir, authority: "Go module root (cmd/, internal/, pkg/)" };
  if (lang === "jvm") {
    for (const p of ["src/main/java", "src/main/kotlin"]) {
      if (ok(at(p))) return { root: at(p), authority: `Maven/Gradle standard layout: ${p}/` };
    }
    return { root: dir, authority: "fallback: project directory" };
  }
  if (lang === "php") {
    const c = readJsonc(at("composer.json"));
    const psr4 = c?.autoload?.["psr-4"];
    const first = psr4 && Object.values(psr4)[0];
    const p = Array.isArray(first) ? first[0] : first;
    if (p && ok(at(p))) return { root: at(p), authority: `composer.json autoload psr-4 -> "${p}"` };
    if (ok(at("src"))) return { root: at("src"), authority: "PHP convention: src/" };
    return { root: dir, authority: "fallback: package directory" };
  }
  if (lang === "ruby") {
    if (ok(at("lib"))) return { root: at("lib"), authority: "Ruby gem convention: lib/" };
    return { root: dir, authority: "fallback: project directory" };
  }
  if (lang === "dotnet") return { root: dir, authority: ".NET: project directory (namespaces mirror folders)" };
  return { root: dir, authority: "unknown language" };
}

// --- documented modules ----------------------------------------------------

function parseDocumentedModules(diagramPath) {
  if (!existsSync(diagramPath)) return null;
  const text = readFileSync(diagramPath, "utf8");
  const out = [];
  const headings = [...text.matchAll(/^## (.+)$/gm)].filter(
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
    const entry = /ENTRY POINT/.test(block)
      ? (block.match(/^\s*class (\w+)\s*\{[^}]*ENTRY POINT/m) ?? [])[1] ?? null
      : null;
    out.push({ title, modules, entry });
  }
  return out;
}

// --- report ----------------------------------------------------------------

let repoRoot;
try {
  repoRoot = execSync("git rev-parse --show-toplevel", { encoding: "utf8" }).trim();
} catch {
  repoRoot = process.cwd();
}

const diagramArg = process.argv[2] || "docs/architecture/system-class-diagram.md";
const diagramPath = resolve(repoRoot, diagramArg);

console.log("--- LANGUAGE PROJECTS FOUND (source root per that language's own convention) ---");
const projects = findProjects(repoRoot);
const dirs = [...projects.keys()].sort((a, b) => a.length - b.length);

if (dirs.length === 0) {
  console.log("  none found");
}

for (const dir of dirs) {
  const manifests = projects.get(dir);
  const lang = detectLanguage(dir, manifests);
  const { root, authority, multi } = detectSourceRoot(dir, lang);
  const exts = EXT_BY_LANG[lang] ?? [];

  console.log("");
  console.log("[" + lang + "] " + (posix(relative(repoRoot, dir)) || "."));
  console.log("  manifests:   " + [...manifests].sort().join(", "));
  console.log("  source root: " + (posix(relative(repoRoot, root)) || "."));
  console.log("  authority:   " + authority);

  if (multi) {
    console.log("  NOTE: multiple packages here — each is its own module namespace;");
    console.log("        decide with the user which one the module set applies to.");
  }

  const level1 = listDirs(root);
  console.log("  LEVEL-1 FOLDERS (this set must equal the documented module set):");
  if (level1.length === 0) console.log("    (none)");
  for (const d of level1) {
    const { files, dirs: sub } = countDeep(join(root, d), exts);
    const nest = sub > 0 ? `${sub} sub-folder${sub === 1 ? "" : "s"}` : "flat";
    console.log(`    ${d.padEnd(22)} ${String(files).padStart(3)} file${files === 1 ? " " : "s"}, ${nest}`);
  }

  const loose = listFiles(root, exts);
  console.log("  ROOT-LEVEL SOURCE FILES (only the entry point / language-mandated files belong here):");
  if (loose.length === 0) console.log("    (none)");
  for (const f of loose) console.log("    " + f);
}

console.log("");
console.log("--- DOCUMENTED MODULES (from " + (posix(relative(repoRoot, diagramPath)) || ".") + ") ---");
const documented = parseDocumentedModules(diagramPath);
if (documented === null) {
  console.log("  diagram not found — run the system-class-diagram skill first, or");
  console.log("  derive module boundaries fresh and have the user approve them.");
} else if (documented.length === 0) {
  console.log("  diagram found but no Module Contract sections parsed — check its format.");
} else {
  for (const s of documented) {
    console.log("");
    console.log("  " + s.title);
    console.log("    modules: " + s.modules.join(", "));
    if (s.entry) console.log("    entry point module: " + s.entry);
  }
}
