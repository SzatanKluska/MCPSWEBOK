---
name: system-class-diagram
description: "Generate or update a layered Mermaid diagram set for the whole system (the KnowledgeBasePipeline Python package and the Server MCP TypeScript app), anchored to a timestamp (not a commit — so it also catches uncommitted work): a subsystem-level Context diagram, a per-subsystem Module Contract diagram (each module as one box exposing only its public contract), and one detailed class diagram per module. USE WHEN the user asks to create/update/refresh a class diagram, module diagram, layer diagram, architecture diagram, diagram klas, diagram modułów, diagram warstw, system overview diagram, or asks 'is the diagram up to date with recent changes'. On first run it creates docs/architecture/system-class-diagram.md and records the current time; on later runs it detects commits AND uncommitted edits since that time and updates only the affected diagrams."
argument-hint: "[optional path to the diagram .md, default docs/architecture/system-class-diagram.md]"
---

# System Class Diagram

Keep a single, timestamp-anchored, **layered** Mermaid diagram set of the whole
system in sync with the code. Three levels of zoom, each answering a
different question:

1. **Context** — the two subsystems and how they hand off data.
2. **Module Contract** (one per subsystem) — the subsystem's internal
   modules/layers as boxes, each showing only the contract it exposes to the
   rest of the system (its ports, or its key public operations) — never its
   internal classes. This is the level meant to stay small and stable as the
   system grows.
3. **Per-module class diagram** (one per module/layer) — the actual
   classes/interfaces/types inside one module, in full detail.

The diagram lives in one Markdown file and remembers the timestamp it was
last generated at, so later runs only reconcile what changed since then —
whether that change was committed or not. This is deliberate: the diagram
doesn't have to be committed together with the code it describes, so it
never forces its own separate commit just to stay anchored.

## How this skill runs
1. VS Code selects this skill from the `description` above and loads this file.
2. **The first action, every time, is to run the status helper** (step 1 below).
   Its `MODE` output decides everything else — never skip it and never guess the
   mode by eyeballing git.

## When to use
- "Create/generate a class diagram of the system" (also: *diagram klas*,
  *diagram modułów*, *diagram warstw*, architecture diagram).
- "Update the class diagram", "refresh the diagram with the latest changes".
- "Is the diagram up to date with recent changes?"

## What it produces
A Markdown file (default `docs/architecture/system-class-diagram.md`) containing:
1. A **provenance marker** (HTML comment) with the timestamp the diagram
   reflects — not a commit SHA.
2. A **Context** flowchart (subsystem-level; shape doesn't change often).
3. Per subsystem, a **Module Contract** `classDiagram` — one box per
   module/layer (the same groups used in step 4), each listing only its
   exposed contract; relationships between boxes show the Dependency Rule.
4. Per module/layer: a short **Responsibility** description and, where the
   module introduces domain terms a reader wouldn't already know, a
   **Concepts** glossary — then its own dedicated `classDiagram` with the
   real classes/interfaces/types it contains (see
   [Conventions](#module-description-rules)).
5. A **Changelog** table recording each generation/update — including which
   of the diagrams above it touched.

## Procedure

### 1. Determine the mode (ALWAYS run this first)
Always start by running the status helper from the repo root — this is how the
skill knows whether to create, update, or do nothing:
```
node .github/skills/system-class-diagram/scripts/diagram-status.mjs [diagramPath]
```
It prints `MODE: create` | `update` | `up-to-date`, plus `STORED` (the
timestamp recorded in the diagram's marker) and `NOW` (current time), and for
updates: the changed source files (both from commits made after `STORED` and
from **uncommitted** working-tree edits whose file mtime is after `STORED`),
the commit list since `STORED`, and a **SOURCE INVENTORY** — the code files
the diagram must cover (this also includes uncommitted new files). `update`
triggers only when a **source** file changed; edits to only docs/tooling
(including the diagram itself) report `up-to-date`, so updating the diagram
never loops, and it never has to be committed to "count." Then:

- **up-to-date** → tell the user the diagram already matches `HEAD`; stop.
- **create** → go to step 2.
- **update** → go to step 3.

### 2. CREATE — build the diagram set from scratch
1. Survey the codebase to identify classes/types and relationships. Cover **both**
   subsystems:
   - `KnowledgeBasePipeline/kbprep/` — Python: ports (`rag/ports.py`), pipeline
     core, adapters (`rag/adapters/`), models (`rag/models.py`,
     `figures/models.py`), figures sidecar, CLI, config.
   - `Server/src/` — TypeScript, layered: `domain/` (types + ports + policies),
     `application/` (Retriever), `infrastructure/` (adapters), `interface/mcp/`
     (tools/resources/prompts), `di/`, `config/`.
   For speed, delegate the survey to a read-only exploration subagent if one is
   available (e.g. the `Explore` agent); otherwise read each subsystem's
   `README.md` `## Layout` section, then open the actual class/interface
   declarations to get members and relationships right. Do **not** invent members.
   Then reconcile against the helper's **SOURCE INVENTORY**: every listed file
   must map to at least one node, and no node may stand for more than one file.
2. Partition each subsystem into modules/layers — reuse the boundaries this
   skill has already established for this project (KnowledgeBasePipeline:
   `ports`, `core`, `adapters`, `models`, `figures`, `di`, `shared`, `app`;
   Server: `domain`, `application`, `infrastructure`, `interface_mcp`, `di`,
   `config`, `app`). Don't invent new boundaries on a whim — this level is
   meant to stay stable; if the codebase has genuinely outgrown the current
   split, changing it is a deliberate, called-out decision (note it in the
   Changelog), not an incidental side effect of an unrelated update.
3. For each subsystem, write its **Module Contract diagram** (see
   [Conventions](#module-contract-diagram-rules)).
4. For each module, write its own **class diagram** (see
   [Conventions](#per-module-class-diagram-rules)) preceded by its
   **Responsibility/Concepts** description (see
   [Conventions](#module-description-rules)).
5. Take a current timestamp (the helper's `NOW`, or a fresh one if meaningful
   time has passed since running it — see [Notes](#notes)).
6. Create the file with the provenance marker set to that timestamp and an
   initial Changelog row (see [File skeleton](#file-skeleton)).
7. [Validate](#4-validate) and report the anchor timestamp.

### 3. UPDATE — reconcile changes since STORED
1. From the helper output take `STORED`, `NOW`, and the changed files (both
   the committed and the uncommitted lists). For more context on the
   committed side: `git log --oneline --since="<STORED>"` and
   `git log --since="<STORED>" -p -- <path>` for a specific file's diff.
2. Map each changed source file to its module (by path) and update **only
   that module's own class diagram** (add/remove a class, edit shown members,
   edit implements/uses/composition edges). Keep the diff minimal — do not
   redraw untouched parts. A new source file MUST get its own node in the
   right module's diagram (never fold it into an existing one); a deleted
   file's node is removed.
3. **Check whether the change also touches that module's exposed contract**
   (a new/removed/changed port, a new inter-module dependency, a changed
   public entry-point signature) — if yes, also update that subsystem's
   Module Contract diagram. If the change is purely internal (private
   members, internal helpers, an adapter's own implementation detail), the
   Module Contract diagram is untouched. Most changes should **not** touch
   it — that stability is the whole point of this tier.
4. **Check whether the change touches that module's Responsibility/Concepts
   description** — a genuinely new domain term, or the module taking on/
   dropping a responsibility. Most changes (a new method, a new adapter for
   an existing port) don't; don't rewrite the description just because the
   diagram below it changed.
5. Update the provenance marker's `updated:` timestamp to a fresh current
   time (re-check the time if reconciling took a while — don't reuse a
   `NOW` that's gone stale, see [Notes](#notes)) and prepend a Changelog row:
   `<date> | <STORED>..<new updated> | <summary, noting which diagrams changed>`.
6. [Validate](#4-validate) and report what changed and the new anchor timestamp.

### 4. Validate
- **Coverage**: cross-check against the helper's SOURCE INVENTORY — every
  listed file is represented by >=1 node in some module's **class diagram**
  (the Module Contract diagram is intentionally abstracted and doesn't count
  for this check), and no node merges multiple files; state any deliberate
  omission.
- Every module referenced as a box in a Module Contract diagram has a
  corresponding `###` class-diagram section below it, and vice versa.
- Every module section has a Responsibility line.
- Re-run the helper; it must now print `MODE: up-to-date`.
- Sanity-check each Mermaid block renders (balanced fences, valid
  `classDiagram`/`flowchart` syntax, every relationship references a declared
  class). Open the Markdown preview if unsure.

## Conventions
- **Output path**: `docs/architecture/system-class-diagram.md` unless the user
  passes another path (create the folder if missing).
- **Provenance marker** — the `updated:` line is the anchor the helper reads
  (must match `updated:\s*<ISO-8601>`, e.g. `2026-08-22T16:45:00.000Z`,
  precise to at least the minute — no bare date, and **no `commit:` line**;
  this skill deliberately doesn't key off a commit, so nothing here should
  imply it does:
  ```
  <!-- system-class-diagram
  updated: <ISO-8601 timestamp>
  -->
  ```
- **Completeness — one node per source module (do NOT merge files)**: every
  source file that declares a class, interface, or module-level public functions
  gets its own node in its module's class diagram; function-only files
  (registrars, factories, entry points, tool scripts) are nodes with the
  `<<module>>` stereotype. This explicitly includes entry points
  (`kbprep/cli.py`, `Server/src/index.ts`), standalone tools
  (`kbprep/figures/extract.py`), and DI token modules (`di/types.ts`). NEVER
  collapse several files into one node — keep the MCP `resources`, `prompts`
  (swebokExplain, swebokSkillMaker), `completions`, and `sampling` registrars
  as separate nodes. Exclude only package markers (`__init__.py`), data
  (`*.yaml`, `*.jsonl`, images), tests, and build output; note any other
  deliberate omission.
- **Member granularity**: within a node, show key public methods/attributes that
  define collaborations; omit private helpers, getters, and trivial DTO fields.
  This trims *members*, never whole files (see Completeness).
- **Relationships**: `A ..|> B` implements a port/interface; `A --> B` uses/depends;
  `A *-- B` composes; `A o-- B` aggregates.
- **Polyglot**: Python and TypeScript go in the same file but every diagram
  (Module Contract and each module's class diagram) is **subsystem-specific**;
  never merge languages into one `classDiagram` block.
- **Note wrapping — applies to every `note for X "..."` in the whole file**:
  hard-wrap with `<br/>` every ~6-8 words, e.g.
  `note for X "first clause —<br/>second clause<br/>third clause"`. Mermaid
  does not reliably auto-wrap note text across renderers (GitHub, VS Code
  preview); a long single-line note silently overflows the diagram's
  calculated bounds and gets visually clipped by the surrounding container —
  it then reads as an unrelated, half-cut box rather than an annotation.
  Manual wrapping is mandatory, not optional, for any note this skill writes.

### Module Contract diagram rules
- One `classDiagram` per subsystem, one class-box per module (stereotype
  `<<layer>>`).
- A box's members = **only its exposed contract**, chosen by its role:
  - Defines ports for others to implement (e.g. `domain`, `ports`) → list the
    port/interface names, one per line.
  - Orchestration/use-case facade (e.g. `application`, `core`) → list its
    main public entry-point signatures (e.g. `Retriever.search(query, k)`).
  - Pure wiring/composition (e.g. `di`) → no members needed; the box + its
    edges are enough.
  - Small side-feature (e.g. `figures`) → 1-2 key public functions.
- **NEVER list an internal/private class or a concrete adapter by name here**
  — that belongs only in the per-module class diagram. This discipline is
  what keeps this diagram small and stable as the system grows; if you're
  tempted to add a class name here, it belongs one level down instead.
- Relationships use the same arrow vocabulary as class diagrams, but between
  modules, mirroring the Dependency Rule (e.g. `infrastructure ..|> domain`,
  `application --> domain`, `di ..> infrastructure`).

### Module description rules
- Immediately under each module's `###` heading, before its `classDiagram`,
  write:
  - **Responsibility** — one or two sentences on the module's job, in plain
    language a newcomer to this specific module could follow.
  - **Concepts** — a short bullet glossary, only where the module introduces
    or is the natural home of a domain term a reader wouldn't already know
    (`**Term** — one-line definition`, using the project's own vocabulary,
    not invented terminology). Define what the term *means* in this system,
    not which class implements it — that's what the diagram below is for.
- Omit the Concepts glossary entirely for modules that introduce no new
  vocabulary (pure wiring/composition modules like `di`/`app` usually need
  only the Responsibility line).
- Keep it tight — this is orientation a reader skims in a few seconds before
  looking at the diagram, not a design document. A term already defined in
  an earlier module isn't redefined; reference it by name instead.

### Per-module class diagram rules
- One `classDiagram` per module/layer, containing only classes/interfaces/
  types/functions that module owns (same Completeness/Member granularity
  rules as above).
- A class from **another** module may appear only as a minimal **reference
  stub** when needed to anchor a single, locally-important relationship —
  typically an adapter's `..|>` to the port it implements. A stub shows
  **method names only, no parameter list and no return type**
  (`+search()`, not `+search(query, k) List~Hit~`) — enough to see at a glance
  what the port/class actually offers, without duplicating the full signature
  that belongs to the owning module's own diagram. A bare data type with no
  behavior (e.g. a plain value object) stays bare, matching how its owning
  module shows it too — don't invent members it doesn't have.
  Add a `note for <Stub>` line saying which module actually owns it
  (hard-wrapped per the note-wrapping rule above, e.g.
  `note for Embedder "owned by domain —<br/>shown only to anchor implements"`).
- **Default: don't repeat cross-module "uses" dependencies here** — those are
  already summarized once, at the right altitude, in the subsystem's Module
  Contract diagram (e.g. `core`'s dependency on all 6 `ports` interfaces is
  one edge up there, not six edges down here).
- **Exception — pure wiring/composition modules** (`di`, and thin bootstrap
  entry points like `app`/`Main`): their entire responsibility *is* wiring
  concrete instances from other modules, so enumerating exactly what gets
  wired **is** their detailed contract. For these specific modules, keep the
  cross-module "wires"/"uses" edges as reference stubs even though the
  general rule above says not to — that wiring list is the valuable content,
  not clutter to abstract away.
- TypeScript-specific: not every node is a class — interfaces (`<<interface>>`),
  plain types/value objects (`<<type>>`), and function-only modules
  (`<<module>>`) are all valid nodes; use the stereotype that matches what
  the file actually is, don't force everything into a class shape.

## File skeleton
````markdown
<!-- system-class-diagram
updated: <ISO-8601, e.g. 2026-08-22T16:45:00.000Z>
-->
# System Class Diagram

> Auto-maintained by the `system-class-diagram` skill. Anchored to the
> timestamp in the marker above (not a commit). Run the skill to refresh
> after new changes, committed or not.

## Context
```mermaid
flowchart LR
  A["Subsystem A"] -->|handoff| B["Subsystem B"]
```

## Subsystem A
### Module Contract
```mermaid
classDiagram
  class moduleX { <<layer>> PortOne, PortTwo }
  class moduleY { <<layer>> Facade.mainOp(arg) }
  class moduleZ { <<layer>> }
  moduleY --> moduleX
  moduleZ ..|> moduleX
```
### moduleX
**Responsibility**: defines the contracts moduleY and moduleZ are built against.
**Concepts**:
- **Result** — the outcome type every port operation returns.
```mermaid
classDiagram
  class PortOne { <<interface>> +op(arg) Result }
  class PortTwo { <<interface>> +op(arg) Result }
```
### moduleY
**Responsibility**: the one use case, expressed as a single facade over moduleX's ports.
```mermaid
classDiagram
  class Facade { +mainOp(arg) Result }
```
### moduleZ
**Responsibility**: the concrete implementation of moduleX's ports.
```mermaid
classDiagram
  class ConcreteImpl
  class PortOne { <<interface>> +op() }
  ConcreteImpl ..|> PortOne
  note for PortOne "owned by moduleX —<br/>shown only to anchor implements"
```

## Changelog
| Date | Since -> Updated | Summary |
|------|------------------|---------|
| <date> | initial | Initial diagram. |
````

## Notes
- The helper only reads git, the filesystem, and the marker; the semantic
  diagramming is the agent's job. If the marker's `updated:` line is missing
  or unparseable, the helper reports `MODE: create` — regenerate from scratch.
- **Why a timestamp, not a commit**: a commit anchor would force the diagram
  to be committed in lockstep with the code it describes (its own separate
  commit, since the diagram's own commit doesn't count as a source change) —
  and it can't see uncommitted work at all. A timestamp sees both: commits
  made after `STORED` (via `git log --since`) and uncommitted edits (via
  working-tree file mtimes compared to `STORED`), so the skill can be run
  freely mid-session, before anything is committed.
- **Freshness of the anchor you write**: if reconciling the diagram takes a
  while (a large update, several tool calls), the `NOW` the helper printed at
  the *start* may no longer be "now" by the time you write the marker. If in
  doubt, get a fresh timestamp right before writing
  (`node -e "console.log(new Date().toISOString())"`) rather than reusing a
  stale one — an anchor slightly in the past just means the next run
  re-checks a bit more than strictly necessary, which is harmless; an anchor
  in the future would hide real changes.
- **mtime caveat**: uncommitted-change detection relies on each file's
  filesystem modified-time. Operations that rewrite files without a real
  edit (a fresh `git checkout`/clone, some formatters that touch every file)
  can reset mtimes and cause a spurious `update`. This is rare in normal use
  and safe to over-trigger on — worst case is an unnecessary reconciliation
  pass, not a missed one.
- Module boundaries are meant to be stable — if you find yourself
  renaming/splitting them often, the boundary was probably wrong to begin
  with; prefer to keep them fixed and let the per-module class diagrams
  absorb the actual churn, exactly as this scheme intends.
- Keep the file self-contained (no external images); Mermaid renders in the VS
  Code Markdown preview and on GitHub.
