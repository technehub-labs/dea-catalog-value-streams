# CR-VS-13 — Per-stream folder enrichment: human- and machine-readable entity documentation

| Field | Value |
|---|---|
| Status | Executed (this document) |
| Target repository | `technehub-labs/dea-catalog-value-streams` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-29 |
| Depends on | CR-VS-07/11/12 (record shape, applicability, population) |
| Method | Catalog repository standard (CR-CATALOG-STRUCT-01 §5 per-entity research layout; IDM-007 per-entity README) |

## 1. Problem

Each value stream folder carried only the record and a plain README. The
README was human-readable but not machine-extractable, had no visualization,
and the evidence trail lived only in the catalog-wide register — nothing
per-entity. The generation logic was a throwaway script outside the repo,
so READMEs were not reproducible.

## 2. What this CR does

### 2.1 Folder shape (per stream)

```
value-stream-<slug>-<hash6>/
├── value-streams-value-stream-<slug>-<hash6>.yaml   (authoritative record)
├── README.md                                        (generated, front-mattered, visual)
└── research/
    ├── README.md        (folder contract per CR-CATALOG-STRUCT-01 §5)
    └── evidence.md      (source-backed notes expanded from the register)
```

The `research/` subtree is the standard's per-entity research location and
is what the CATALOG index's `research_count` field has tracked all along.

### 2.2 README shape (machine + human)

- **YAML front matter** — machine-extractable summary: id, name, type,
  version, lifecycle, category, industries, specificity, entry/exit
  criteria, outcome, stage names, capability/process/metric id lists,
  upstream/downstream slugs, evidence sources. GitHub renders it as a
  table; any tool can parse it with a front-matter parser.
- **Mermaid stage-flow diagram** — the stream's stages as a left-to-right
  flow with explicit entry and exit nodes.
- **Compact stage table + per-stage detail** — criteria, outcomes,
  capability/process counts at a glance; full refs per stage.
- **Clickable cross-stream links** — upstream/downstream neighbours link
  to the sibling folder (relative links, verified).
- **Evidence table + rationale** with a pointer to `research/evidence.md`.
- **Provenance ladder table.**
- Generation footer: every README names its generator and the record it
  derives from; hand-editing is discouraged by contract.

### 2.3 `research/evidence.md` (per entity)

Expands every cited evidence-register source into per-entity notes: class,
reference, retrieval mode, each observation, what it supports, and its
implication. Generated from the register — no hand-authored content, no
new evidence claims. `research/README.md` documents the folder contract
and the standard clause it implements.

### 2.4 Generator as repo infrastructure

`scripts/generate_entity_docs.py` (stdlib + PyYAML): regenerates one
(`--only <slug>`) or all subtrees deterministically from the records and
the register; `--dry-run` for review. Replaces the throwaway generation
scripts; per-stream READMEs are now reproducible artifacts.

### 2.5 Regenerator state fix (found by this work)

Adding `research/` subtrees exposed a latent bug in the vendored
`scripts/regenerate_catalog.py`: `infer_state` probed for the canonical
file as `{entity_id}.yaml`, but ids contain `:` which is never a filename
— canonical records were silently indexed as `state: candidate` since
CR-VS-06 (and would have degraded to `research` once research/ subtrees
appeared). Fixed to probe the IDM-005 normalized name
(`id.replace(':', '-')`) first, with the legacy form as fallback. Same bug
class as the actors catalog's CR-ACT-07 fix. CATALOG.yaml now correctly
reports **111 `state: canonical`** (previously 111 `state: candidate`).

## 3. Non-goals

- No record, schema, workflow, or vocabulary changes; documentation and
  tooling only (plus the regenerator fix above with its CATALOG.yaml
  regeneration).
- No new evidence; `evidence.md` strictly derives from the existing
  register.

## 4. Verification

- All 111 folders regenerated; all relative links across the 333 markdown
  files scripted-verified to resolve.
- Front matter parses on every README; stage/capability/process/metric
  counts derive from the records.
- CATALOG.yaml: 111 entities, all `state: canonical`, `research_count: 2`;
  index schema validation OK; `--check` freshness OK.
- Schema validation 112/112; referential-integrity gate 111/111.
