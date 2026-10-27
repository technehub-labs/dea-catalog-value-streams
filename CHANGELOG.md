# Value Stream Catalog Changelog

All notable changes to this catalog are recorded here. The format is based
on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Phase 0 — scaffold alignment

- README corrected to the current metamodel state: entity `dea:ValueStream`
  (alias `VS`), layer L3, building block `L3-value-delivery`, lifecycle
  planned; legacy `dea:entity-vs` / L2 / v2.0.0-alpha references removed;
  the not-yet-existing `entities/` and `schemas/` tree replaced with the
  actual repository structure and the metamodel relationship table.
- CONTRIBUTING.md added (authorship rule, pointer discipline, PR flow).
- No entity, pointer, schema, or gate-logic changes.

### Phase 2 — catalog scaffolding

- `schemas/entity.schema.json` added: entry schema for ValueStream records,
  mirroring the metamodel `dea:ValueStream` schema (CR-MET-014 field set:
  outcome, customer_ref, entry_criterion, exit_criterion,
  aggregated_capability_refs) plus catalog extensions (evidence,
  provenance ladder) per the org-wide catalog repository standard
  (CR-CATALOG-STRUCT-01).
- `schemas/fixtures/example-valid.yaml` added: schema self-exercise fixture
  (not a catalog entry) so the schema is never untested while entities/ is
  empty.
- `entities/v1-alpha/` layout established (flat, content-addressed subtrees
  per `dea-metaframework/docs/entity-storage-layout.md`), with README.
- `validate-entries.yml` workflow added: validates entries (with the
  empty-entities skip guard) and the fixture against the entry schema.
- No catalog entries admitted yet; admission follows the catalog-research
  method (candidate universe, distinctness sweep, evidence register,
  admission gate).
