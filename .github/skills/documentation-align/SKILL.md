---
name: documentation-align
description: "Aligns a project's physical folder structure with its documented module/layer boundaries, so that the top-level entries directly under each language's conventional source root (src/ for Node, the package dir for Python, etc.) correspond one-to-one to the modules named in the architecture doc (e.g. the system-class-diagram output) — without flattening what's inside each module's own folder. USE WHEN the user asks to align/reorganize the project structure to match its modules or architecture, asks whether the folder layout matches the diagram, or asks to put layers like ports/core/adapters or domain/application/infrastructure into their own top-level folders. Also: ułóż moduły w foldery, wyrównaj strukturę projektu do modułów/warstw, czy struktura folderów odpowiada diagramowi."
argument-hint: "[optional path to the diagram .md, default docs/architecture/system-class-diagram.md]"
---

# Documentation Align

Keeps a project's **physical folder structure** in sync with its **documented
module/layer boundaries** — the same boxes named in a subsystem's Module
Contract diagram (typically produced by the `system-class-diagram` skill).
The goal is narrow and specific: the entries **directly under** each
language's conventional source root should be exactly the documented
modules, one-to-one. What happens *inside* a module's own folder is that
module's business — this is explicitly **not** about flattening anything.

## How this skill runs
1. VS Code selects this skill from the `description` above and loads this file.
2. **The first action, every time, is to run the status helper** (step 1
   below). It is read-only — running it costs nothing and never edits the
   filesystem.

## When to use
- "Align the project structure to the modules/architecture."
- "Does the folder layout match the class diagram?"
- "Put `ports`/`core`/`adapters` (or `domain`/`application`/`infrastructure`,
  etc.) into their own top-level folders."
- *ułóż moduły w foldery*, *wyrównaj strukturę projektu do modułów/warstw*,
  *czy struktura folderów odpowiada diagramowi*.

## What it does
This is an **action** skill, not a document generator. It:
1. Reports where the physical layout has drifted from the documented modules.
2. Proposes a concrete move plan (`git mv` per misplaced file/folder).
3. **Stops for explicit confirmation before touching anything** — moving
   files across a real codebase is a hard-to-reverse, broad-blast-radius
   change (breaks imports, affects git history, touches many files), so it
   gets the same stop-and-check treatment as any other risky action.
4. After confirmation: applies the moves, fixes every import statement the
   move broke, and verifies with the project's own build/typecheck command.

## Procedure

### 1. Determine the source of truth for module boundaries
Run the status helper from the repo root:
```
node .github/skills/documentation-align/scripts/structure-status.mjs [diagramPath]
```
It is purely mechanical — it does no semantic judgment — and prints two
things:
- **LANGUAGE PROJECTS FOUND**: every Node (`package.json`) and Python
  (`__init__.py`) project in the repo, each with its **source root** detected
  per that language's own convention (Node: `tsconfig.json`'s
  `compilerOptions.rootDir` if set, else `src/` if it exists, else the
  project dir; Python: the shallowest directory containing `__init__.py`) and
  the **actual top-level entries** directly under that root.
- **DOCUMENTED MODULES**: for each subsystem in the diagram, the module names
  parsed straight out of its `### Module Contract` `classDiagram` box list.

Then:
- If a subsystem has a parsed module list → that list is authoritative; go to
  step 2.
- If the diagram doesn't exist, or a subsystem's Module Contract section
  didn't parse → **recommend running the `system-class-diagram` skill
  first**. It is cheap, and it gives both skills a single written source of
  truth for what a project's modules are, instead of this skill re-deriving
  boundaries ad hoc (which would go stale and can't be checked twice
  consistently). Only derive module boundaries fresh, by the same kind of
  survey `system-class-diagram` step 2 does, if the user explicitly declines.

### 2. Match projects to subsystems
The helper lists projects and documented subsystems separately without
correlating them — that correlation is a judgment call: read each
subsystem's heading/prose in the diagram (or the project's own README) and
match it to a project directory the helper found.

### 3. Diff documented modules against actual top-level entries
For each documented module, in each subsystem:
- **Exists?** Is there a top-level entry (a folder, or — for the entry-point
  module — a single file) directly under the source root with that name?
  See the entry-point exception below before flagging a missing folder.
- **Complete?** Using the diagram's per-module class diagram (its "one node
  per file" list — see `system-class-diagram`'s Completeness rule), confirm
  every file the diagram assigns to this module actually lives somewhere
  inside this module's folder (any depth — nested subfolders are fine and
  expected, never flag those).
- **Misplaced files** — a file the diagram assigns to module X but which
  currently sits outside X's folder (e.g. under a different module's folder,
  or loose at the source root) — is the main class of drift this skill
  exists to fix.
- **Undocumented extra top-level entries** — a folder/file at the top level
  that doesn't correspond to any documented module. Ask whether it should
  fold into an existing module, become a newly documented module (in which
  case run `system-class-diagram` afterwards to add it), or is legitimate
  non-module scaffolding that shouldn't be under the source root at all
  (stray tests, generated output).
- **Naming mismatches** — the closest matching folder has a different name,
  or nests the module one level deeper than expected (e.g. a module
  documented as `interface_mcp` but the actual folder is `interface/` with
  `mcp/` nested inside it). **Surface this as a question, not an autofix** —
  ask whether the folder should be renamed to match the doc, or the doc
  renamed to match the folder. Don't silently pick a side.

### 4. Build the move plan — then stop
List every proposed `git mv <from> <to>`, and for each, which files import it
(grep the current relative/module import path project-wide) so the user can
see the blast radius before approving. Present the full plan and get
explicit confirmation. Do not proceed to step 5 without it.

### 5. Apply (only after confirmation)
For each approved move:
1. `git mv <from> <to>` — never a plain filesystem move; this preserves
   `git log --follow` history that a delete+add would lose.
2. Fix every import that referenced the old path, **file by file** — never a
   blind global search-replace, since partial name overlaps between modules
   are common:
   - TypeScript/Node: recompute the relative import path from each importing
     file to the new location.
   - Python: recompute the dotted module path (`from .rag.ports import X` →
     `from .ports import X`, etc.).

### 6. Verify
Run the project's **actual** build/typecheck command — read it from
`package.json` scripts (`tsc`, `npm run build`) or the Python project's own
test/lint setup; never invent one. If it fails, a broken import slipped past
the grep in step 5 — fix it and re-verify. Never leave the tree in a broken
state between moves.

### 7. Re-run the helper
Confirm the new top-level structure now matches the documented modules
one-to-one (modulo the entry-point exception) and report what changed.

## Conventions

- **Language source-root conventions** — trust the project's own build
  config over guessing, and extend this list rather than inventing a
  convention that isn't idiomatic for the language:
  - **Node/TypeScript**: `src/`, or whatever `tsconfig.json`'s
    `compilerOptions.rootDir` says.
  - **Python**: the actual importable package directory (the one containing
    `__init__.py` that ships as the distribution's package). Prefer an
    explicit `src/<pkg>/` layout if the project already uses one. A project
    with no `pyproject.toml` packaging config still has a de facto
    convention: whatever directory is run as `python -m <pkg>.<entry>`.
  - **Java/Kotlin**: `src/main/java/<package/path>/` (or `.../kotlin/...`).
  - **Go**: the module root for `package main`; Go's compiler already forces
    one directory per package, so this skill matters far less there.
  - **Rust**: `src/`, with `mod.rs`/`<name>.rs` per module.
- **Never flatten.** Only the **top level** directly under the source root is
  being aligned to the documented modules. Nested structure inside a
  module's own folder (`infrastructure/embedding/`, `infrastructure/transport/`,
  `rag/adapters/`) is expected and correct — do not propose collapsing it.
- **The entry point doesn't get a folder.** A module marked `ENTRY POINT` in
  the Module Contract diagram conventionally lives as a single file at the
  source root (`index.ts`, `cli.py`, `main.go`) — mirroring how every
  mainstream language starts a program. Manufacturing a one-file `app/`
  folder for it is structure for its own sake; don't propose it.
- **Naming mismatches are a question, not an autofix** (see step 3).
- **`git mv`, always** — plain moves lose history.
- **Fix imports per file; verify with the project's real build command** —
  never assume a move is safe just because the file landed in the right
  place.
- **Every move needs a plan and explicit confirmation first** — this skill
  changes code, not just documentation. Never batch-apply a plan silently.
- **This skill doesn't edit the architecture doc.** A pure relocation doesn't
  change what a module is or what it exposes, so `docs/architecture/system-
  class-diagram.md` needs no update after a clean move. If a move plan turns
  out to imply an actual module split or rename, that's a `system-class-
  diagram` update, not something to hand-edit here — run that skill
  afterwards to reconcile the doc.

## Notes
- This skill and `system-class-diagram` deliberately share one concept of
  "module." The diagram is the cheapest, most durable place to record module
  boundaries once; this skill just holds the filesystem to that record.
  Keeping the diagram current makes this skill's job unambiguous instead of a
  fresh judgment call every run.
- A project with only one or two documented modules, or too small to have
  layers yet, doesn't need this skill — it exists for exactly the case where
  multiple documented layers have drifted from (or never matched) the
  physical layout.
- The helper is read-only and cheap to re-run at any point; only step 5
  (apply) touches the filesystem.
