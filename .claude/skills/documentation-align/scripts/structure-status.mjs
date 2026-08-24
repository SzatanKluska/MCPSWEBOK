#!/usr/bin/env node
// Reports, for every subsystem in the repo: its language, the source root that
// language's conventions put the code under, the folders that currently sit at
// LEVEL 1 under that root, and any source files loose at the root.
//
// Level 1 is the only level this skill constrains — it must equal the set of
// documented modules. Everything deeper is the module's own business and is
// deliberately NOT reported in detail.
//
// The script is purely descriptive: it reads manifests and the filesystem and
// never decides what a module is. Comparing level-1 folders against the
// documented module set is the agent's job.
//
// Usage: node structure-status.mjs [repoRoot]

import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { join, relative, resolve, sep } from "node:path";

const IGNORED = new Set([
  "node_modules", ".git", ".venv", "venv", "env", "__pycache__", "dist",
  "build", "out", "target", "bin", "obj", ".next", ".nuxt", "coverage",
  ".pytest_cache", ".mypy_cache", ".tox", ".gradle", ".idea", ".vscode",
  "vendor", "Pods", ".dart_tool",
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
  const walk = (d, depth) => {
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
        walk(p, depth + 1);
      } else if (exts.some((x) => e.name.endsWith(x))) {
        files++;
      }
    }
  };
  walk(dir, 0);
  return { files, dirs };
}

// --- find subsystems -------------------------------------------------------

const MANIFESTS = [
  "package.json", "tsconfig.json", "pyproject.toml", "setup.py", "setup.cfg",
  "requirements.txt", "go.mod", "Cargo.toml", "pom.xml", "build.gradle",
  "build.gradle.kts", "composer.json", "Gemfile",
];

function findSubsystems(root) {
  const found = new Map(); // dir -> Set(manifest)
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
    // a package.json with .ts sources but no tsconfig is still TypeScript
    const pkg = readJsonc(join(dir, "package.json"));
    const dev = { ...(pkg?.dependencies ?? {}), ...(pkg?.devDependencies ?? {}) };
    return "typescript" in dev ? "typescript" : "javascript";
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

// Returns { root, authority } — root is the directory whose LEVEL 1 must equal
// the module set; authority says which file or convention decided that.
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
    const pkgsIn = (base) =>
      listDirs(base).filter((d) => existsSync(join(base, d, "__init__.py")));
    if (ok(at("src"))) {
      const pkgs = pkgsIn(at("src"));
      if (pkgs.length === 1) {
        return { root: at("src", pkgs[0]), authority: `src-layout: src/${pkgs[0]}/ (importable package)` };
      }
      if (pkgs.length > 1) {
        return { root: at("src"), authority: `src-layout with ${pkgs.length} packages: ${pkgs.join(", ")}`, multi: pkgs };
      }
    }
    const pkgs = pkgsIn(dir);
    if (pkgs.length === 1) {
      return { root: at(pkgs[0]), authority: `flat layout: ${pkgs[0]}/ (importable package)` };
    }
    if (pkgs.length > 1) {
      return { root: dir, authority: `flat layout with ${pkgs.length} packages: ${pkgs.join(", ")}`, multi: pkgs };
    }
    return { root: dir, authority: "no __init__.py package found" };
  }

  if (lang === "rust") return { root: at("src"), authority: "Cargo convention: src/" };
  if (lang === "go") return { root: dir, authority: "Go module root (see cmd/, internal/, pkg/)" };
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

// --- report ----------------------------------------------------------------

const repoRoot = resolve(process.argv[2] ?? process.cwd());
const subsystems = findSubsystems(repoRoot);

if (subsystems.size === 0) {
  console.log("No subsystem manifest found under " + posix(repoRoot));
  process.exit(0);
}

// A nested manifest inside another subsystem's source tree is usually a
// sub-package, not a separate subsystem; report the outermost ones first.
const dirs = [...subsystems.keys()].sort((a, b) => a.length - b.length);

console.log("REPO: " + posix(repoRoot));
console.log("SUBSYSTEMS: " + dirs.length);

for (const dir of dirs) {
  const manifests = subsystems.get(dir);
  const lang = detectLanguage(dir, manifests);
  const { root, authority, multi } = detectSourceRoot(dir, lang);
  const exts = EXT_BY_LANG[lang] ?? [];

  console.log("");
  console.log("--- SUBSYSTEM: " + (posix(relative(repoRoot, dir)) || "."));
  console.log("    language:    " + lang);
  console.log("    manifests:   " + [...manifests].sort().join(", "));
  console.log("    source root: " + (posix(relative(repoRoot, root)) || ".") + "   [" + authority + "]");

  if (multi) {
    console.log("    NOTE: multiple packages here — each is its own module namespace;");
    console.log("          decide with the user which one the module set applies to.");
  }

  const level1 = listDirs(root);
  console.log("    LEVEL-1 FOLDERS (this set must equal the documented module set):");
  if (level1.length === 0) {
    console.log("      (none)");
  }
  for (const d of level1) {
    const { files, dirs: sub } = countDeep(join(root, d), exts);
    const depth = sub > 0 ? `, ${sub} sub-folder${sub === 1 ? "" : "s"}` : ", flat";
    console.log(`      ${d.padEnd(22)} ${files} file${files === 1 ? "" : "s"}${depth}`);
  }

  const loose = listFiles(root, exts);
  console.log("    ROOT-LEVEL SOURCE FILES (only the language's entry/manifest files belong here):");
  if (loose.length === 0) console.log("      (none)");
  for (const f of loose) console.log("      " + f);
}
