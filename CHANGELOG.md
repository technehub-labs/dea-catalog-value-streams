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

### Phase 3 — catalog research foundations (CR-VS-01)

- `catalog-research/` opened: evidence register v0.1 (6 sources across 6
  source classes: BIZBOK, APQC PCF, OMG BACM, TOGAF, SAFe/Lean guidance,
  enterprise process-chain literature) and candidate universe v0.1.
- Candidate universe: 9 VALUE-STREAM candidates (VSC-001..VSC-009 — Order to
  Cash, Procure to Pay, Issue to Resolve, Concept to Launch, Plan to
  Deliver, Hire to Retire, Lead to Cash, Plan to Forecast, Record to
  Report) + 1 DEVELOPMENT-STREAM disambiguation record (VSC-010). None
  canonical; three candidates at E3/high.
- `change-requests/` opened with CR-VS-01 documenting the seed and the
  follow-on pipeline (distinctness sweep CR-VS-02, admission CR-VS-03).
- No canonical entries; `entities/v1-alpha/` untouched.

### Phase 3b — distinctness sweep (CR-VS-02)

- `catalog-research/distinctness-sweep.yaml` (v0.1): 36 ordered pairs swept
  under the two-axis test (entry / exit / served party; authority SRC-001).
  No UNRESOLVED verdicts remain.
- RES-001: VSC-007 (Lead to Cash) merged into VSC-001 (Order to Cash) —
  one-axis (entry-only) difference; VSC-001 entry widened to include demand
  generation as the pre-order stage.
- RES-002: VSC-008 / VSC-009 retained distinct with an explicit boundary
  statement (forward-looking commitment vs. backward-looking attestation).
- Candidate universe bumped to v0.2: 8 VALUE-STREAM candidates remain;
  admission-ready: VSC-001, VSC-002, VSC-003, VSC-006.
- No admissions in this CR; `entities/v1-alpha/` untouched.

### Phase 3c — first admission gate (CR-VS-03)

- First 4 canonical records admitted under `entities/v1-alpha/`:
  Order to Cash (`value-streams:value-stream-order-to-cash-sc8gbu`),
  Procure to Pay (`value-streams:value-stream-procure-to-pay-utma5c`),
  Issue to Resolve (`value-streams:value-stream-issue-to-resolve-crmbay`),
  Hire to Retire (`value-streams:value-stream-hire-to-retire-n6szcc`).
- Content-addressed ids per the org id system (§2.5): `scripts/hash6.py`
  added, matching the reference implementation; suffix assigned once at
  canonicalization.
- Per-entity READMEs (IDM-007); admission map in
  `catalog-research/admission-register.yaml`.
- `validate-entries` workflow now validates real entries (empty-skip guard
  no longer triggers).
