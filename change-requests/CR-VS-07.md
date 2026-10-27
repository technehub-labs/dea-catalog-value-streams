# CR-VS-07 — Value Stream schema enrichment: value stages, referential capability/process links, and comprehensive documentation

**Status**: Proposed

## Summary

Enrich the Value Stream entry schema, the 11 admitted records, and the
repository documentation so a catalog entry captures the full anatomy of a
value stream: its ordered **value stages**, per-stage links to business
capabilities and business processes under **referential integrity**, an
explicit scope boundary, cross-stream flow links, categorisation, and
measurement hooks.

## Motivation

The CR-MET-014 core record (definition, outcome, entry/exit criteria,
`aggregated_capability_refs`) describes a value stream only at its
endpoints. Missing aspects:

1. **Value stages** — the internal stage-by-stage decomposition that turns
   the entry criterion into the exit criterion (BIZBOK value-stream stage
   discipline, SRC-001).
2. **Per-stage capability enablement** — which capabilities enable each
   stage, not just the stream-level aggregate.
3. **Process realization** — no link at all to the business-process catalog
   (`dea:serves` partner side), leaving the value stream unmoored from how
   work actually happens.
4. **Referential integrity** — the CR-VS-03 `customer_ref` omission showed
   the contract (never fabricate a reference that does not resolve) was
   documentation-only; there was no automated gate.
5. **Scope discipline** — boundary statements existed only as free text in
   evidence rationale.
6. **Cross-stream flow** — the `dea:flows-to` relationship had no
   record-side expression.
7. **Documentation** — per-entity READMEs were four-field stubs; the root
   README still described the repository as an empty scaffold.

## Changes

### 1. Schema (`schemas/entity.schema.json`)

New/extended blocks (additive; all CR-MET-014 core fields unchanged):

- `value_stream_category` — operational / support / governance / development.
- `scope` — `includes` (required) and `excludes` (each naming the owning neighbour).
- `value_stages[]` (required, minItems 2) — ordered stage objects: `name`,
  `definition`, `entry_criterion`, `exit_criterion`, `outcome`,
  `customer_visible`, `capability_refs` (required, minItems 1, resolving in
  the capabilities catalog), `process_refs`, `actor_refs`.
- `process_refs[]` — stream-level process links (union of per-stage links).
- `upstream_refs[]` / `downstream_refs[]` — cross-stream links **by slug**
  (`value-stream-<slug>`), deliberately hash-free so sibling hash changes
  cannot break integrity.
- `metrics[]` — `name`, `definition`, optional `applies_to_stage` (must match
  a stage name), optional `metric_ref` (metrics catalog).

### 2. Referential-integrity gate

`scripts/check_referential_integrity.py` (new; wired into
`validate-entries.yml`):

- every `capabilities:` ref resolves in `dea-catalog-business-capabilities`;
- every `processes:` ref resolves in `dea-catalog-business-processes`;
- `actors:`/`metrics:` refs resolve when those namespaces are used;
- `upstream_refs`/`downstream_refs` slugs resolve against this catalog;
- `metrics[].applies_to_stage` matches a declared stage name.

Resolution order: local sibling clone → sibling `CATALOG.yaml` index →
vendored snapshot under `tools/id-sets/` (committed, with refresh date in the
header) so the gate is fully deterministic offline. The gate fails with exit
code 2 only when a namespace in use has no locatable id universe.

### 3. Record enrichment (all 11 records, in place)

Per the rename-stability contract (PR #5), record ids, directories, and
filenames are unchanged; each record's `version` bumps 1.0.0 → 1.1.0 and the
provenance ladder gains a CR-VS-07 `active` entry. Every stage's
`capability_refs`/`process_refs` were hand-curated against the actual sibling
catalog contents (verified: all 30 capability refs and all process refs
resolve; one transcription error `38ycq6` vs `38qyc6` was caught by the gate
itself and fixed).

`aggregated_capability_refs` are extended to the union of the per-stage
`capability_refs` (e.g. Order to Cash gains Marketing and Information
Management through the Generate Demand and Capture Order stages).

### 4. Documentation

- Per-entity READMEs regenerated from the records: 10 sections each —
  identity, definition, value proposition/served party, boundary
  (entry/exit + scope includes/excludes), value stages with per-stage
  criteria and traceability, capability/process traceability, cross-stream
  links, measurement, evidence/admission, provenance ladder.
- Root README: status corrected from scaffold to 11 admitted streams; new
  schema-shape section; catalogued-streams table (category, outcome,
  stages, record links); repository structure updated (scripts, tools,
  CATALOG.yaml).
- `entities/v1-alpha/README.md` status section updated.

## Non-goals

- No new admissions, merges, or retirements (candidate universe untouched).
- `customer_ref` stays unpopulated pending the actors-catalog records
  (CR-VS-03 §4/§7 contract unchanged).
- No metamodel change: `dea:ValueStream` CR-MET-014 upstream work
  (technehub-labs/dea-metamodel#201) is tracked separately; this CR keeps
  the record-side extension catalog-local and additive.

## Verification

- `jsonschema` validation: all 11 records + fixture pass (0 errors).
- `scripts/check_referential_integrity.py`: pass (11 entries checked).
- `scripts/regenerate_catalog.py --check`: CATALOG.yaml current (versions
  bumped to 1.1.0); `check_catalog_index.py`: OK (11 entities).
- Fixture extended to exercise every new block (including an intentional
  stage-scoped metric and slug links).
