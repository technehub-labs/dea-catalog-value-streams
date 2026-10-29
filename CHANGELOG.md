# Value Stream Catalog Changelog

All notable changes to this catalog are recorded here. The format is based
on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Phase 8 — per-stream folder enrichment (CR-VS-13)

- All 111 value stream folders now carry three artifacts: the
  authoritative record, a front-mattered visual README (YAML metadata,
  mermaid stage-flow diagram, compact stage table + per-stage detail,
  clickable cross-stream links, evidence table, provenance ladder), and
  a `research/` subtree (folder contract + per-entity evidence notes
  expanded from the register).
- `scripts/generate_entity_docs.py`: permanent, deterministic generator
  (--only / --dry-run); replaces throwaway scripts; READMEs are
  reproducible artifacts.
- Vendored regenerator state bug fixed: infer_state probed
  `{entity_id}.yaml` but ids contain ':' (never a filename), so canonical
  records were indexed as `state: candidate` since CR-VS-06 — and would
  have degraded to `research` once research/ subtrees landed. CATALOG.yaml
  now reports 111 `state: canonical` (research_count: 2 each).
- All relative links across the 333 markdown files scripted-verified.


### Phase 7 — README visual refresh (post-CR-VS-12)

- Restructured the landing README: visual-first layout, project-management
  detail compressed to a short Governance section pointing at the CR
  ledger and CHANGELOG.
- New mermaid cross-stream flow map: the 11-stream enterprise-generic
  backbone with 18 industry bridges and per-industry chain fragments,
  rendered from the records' upstream/downstream links.
- New ECF overlay matrix: the 111 streams projected onto the 7x7
  Enterprise Concept Framework via their stage capabilities' primary
  coordinates (computed from the sibling capabilities catalog; 14 of 49
  cells populated, concentration annotated).
- New mermaid mindmap of the record anatomy; new badges (stream count,
  industries); method section now carries an admission-pipeline flow
  diagram.


### Upstream dependency filings (CR-VS-08 §4, CR-VS-09, CR-VS-10)

- dea-metaframework#53 filed: standardize cross-catalog id-set snapshots
  (vendored offline fallback for referential-integrity gates) alongside
  issue #51 — CR-VS-10 executed.
- dea-catalog-actors#9 filed: requests the six generic party records
  (customer, supplier, employee, custodian, market-segment,
  governance-stakeholder) CR-VS-09 is gated on; backfill executes when
  that admission lands.
- dea-catalog-metrics#13 filed: CR-VS-08 §4's seven catalogued-metric
  gaps as candidate-seed input for that catalog's research pipeline.
- CR documents and index updated with the issue links; no schema,
  record, workflow, or index changes in this tranche.


### Phase 5 — metric backfill executed (CR-VS-08)

- `metrics[].metric_ref` populated in all 11 records per the verified
  backfill map: 14 links to `dea-catalog-metrics` (legacy `dea:metric-*`
  id form), e.g. `dea:metric-perfect-order-rate`,
  `dea:metric-days-sales-outstanding`, `dea:metric-time-to-hire`,
  `dea:metric-financial-close-cycle-time`, `dea:metric-net-revenue-retention`.
- Alignment renames: Invoice match rate -> First-time match rate;
  Voluntary attrition rate -> Voluntary turnover rate; Asset utilization
  -> Asset utilization rate (matching the catalogued metric names).
- Schema: `metric_ref` pattern admits both the org-wide `metrics:` form
  and the sibling's legacy `dea:metric-*` form.
- Referential-integrity gate: metrics namespace activated
  (`namespace_of` normalization maps `dea:metric-*` onto the metrics id
  universe); vendored scoped snapshot `tools/id-sets/metrics-ids.txt`
  (14 ids, fail-closed per CR-VS-10's scope policy); snapshot-loader bug
  fixed (`lstrip("id: ")` mangled `dea:...` entries).
- Records bumped 1.1.0 -> 1.2.0 with a CR-VS-08 provenance entry
  (ids/dirs/filenames unchanged); per-entity READMEs re-rendered with
  metric links; fixture extended with a legacy-form `metric_ref`.
  CATALOG.yaml regenerated.


### Follow-up CRs drafted (CR-VS-08..10)

- **CR-VS-08** (metric backfill): populate `metrics[].metric_ref` where
  `dea-catalog-metrics` carries the measure — verified backfill map (15
  links, e.g. `dea:metric-perfect-order-rate`, `dea:metric-time-to-hire`);
  relax the `metric_ref` pattern to admit the sibling's legacy
  `dea:metric-*` id form; activate the metrics namespace in the
  referential-integrity gate with a scoped id snapshot. Catalogued-metric
  gaps (generic MTTR, concept-to-launch lead time, P2P cycle time, ...)
  recorded as a follow-on register for the metrics catalog's pipeline.
- **CR-VS-09** (served-party backfill): `customer_ref` + per-stage
  `actor_refs` population in all 11 records — dependency-gated on
  `dea-catalog-actors` (currently empty) admitting the generic party
  records; required-actor mapping table recorded in the CR.
- **CR-VS-10** (id-set snapshot convention): the vendored
  `tools/id-sets/` convention documented as normative local practice
  (format, scope policy, refresh rule, fail-closed staleness semantics);
  upstream ask to `dea-metaframework` for a standard cross-catalog
  snapshot convention + refresh helper, alongside issue #51.
- CR index updated (CR-VS-07 → Merged; CR-VS-08..10 added). No schema,
  record, workflow, or index changes in this tranche.

### Phase 4a — conformance hardening (follow-ons to PR #10)

- `scripts/regenerate_catalog.py`: `detect_repository_url` now normalizes
  the origin URL to the canonical form (no trailing `.git`), so the
  emitted `repository:` line is identical whether the checkout's origin
  was configured with or without the suffix (CI sets the `.git` form;
  local clones vary). `--check` no longer depends on how the checkout
  was made. `CATALOG.yaml` regenerated to the canonical form.
- `classifications/` and `contributions/` created with `.gitkeep`
  placeholders (matching the `dea-catalog-business-capabilities` layout),
  clearing the standing `cross_cutting.*` structural-sanity warnings from
  `check_catalog_index.py`.

### Phase 4 — value stream enrichment (CR-VS-07)

- `schemas/entity.schema.json` extended (additive; CR-MET-014 core
  unchanged): `value_stages[]` (ordered stage decomposition with per-stage
  entry/exit criteria, outcome, customer visibility, and referential
  `capability_refs`/`process_refs`/`actor_refs`), `value_stream_category`,
  `scope` (includes/excludes boundary), stream-level `process_refs`,
  slug-based `upstream_refs`/`downstream_refs`, and `metrics[]` (stream-level
  or stage-scoped).
- Referential-integrity gate added (`scripts/check_referential_integrity.py`):
  every `capabilities:` ref resolves in dea-catalog-business-capabilities,
  every `processes:` ref in dea-catalog-business-processes, cross-stream
  slugs against this catalog; vendored id snapshots under `tools/id-sets/`
  keep the gate deterministic offline. Wired into `validate-entries.yml`.
- All 11 admitted records enriched in place (ids, directories, filenames
  unchanged per the rename-stability contract; version 1.0.0 -> 1.1.0):
  each carries its value stages with curated, verified capability and
  process links; `aggregated_capability_refs` extended to the per-stage
  union; provenance ladder gains the CR-VS-07 entry. CATALOG.yaml
  regenerated (versions).
- Fixture extended to exercise every new schema block.
- Documentation: comprehensive per-entity READMEs (10 sections each,
  rendered from the records) and root README enrichment (schema shape,
  catalogued-streams table, updated structure and status).

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

### Phase 3d — second-tranche evidence and admissions (CR-VS-04)

- Evidence register v0.2: SRC-002 (APQC PCF) extended with
  product-development, planning, and reporting category observations;
  SRC-003 (OMG BACM) extended with the stakeholder-value observation
  (internal governance stakeholders).
- Candidate universe v0.3: VSC-004/005/008/009 raised E2 -> E3.
- Second tranche admitted (8 canonical records total): Concept to Launch
  (`value-streams:value-stream-concept-to-launch-nhvatv`), Plan to Deliver
  (`value-streams:value-stream-plan-to-deliver-smmwpx`), Plan to Forecast
  (`value-streams:value-stream-plan-to-forecast-89vb4q`), Record to Report
  (`value-streams:value-stream-record-to-report-zw9z2r`).
- The first-order candidate universe is now fully resolved: 8 admitted,
  1 merged (VSC-007), 1 disambiguation record (VSC-010).

### Phase 3e — third tranche (CR-VS-05)

- Register v0.3: SRC-006 extended with the chain-inventory observation
  (reverse-logistics, subscription-renewal, asset-lifecycle chains).
- Universe v0.5: VSC-011/012/013/014 seeded; VSC-014 (Fault to Restore)
  merged into VSC-003 (Issue to Resolve) per RES-003 — recorded as an
  alternate name on the Issue to Resolve record.
- Sweep v0.2: 38 new pairs; boundary statements for 011/012, 012/006,
  013/002, 013/005, 013/006.
- Third tranche admitted (11 canonical records total): Return to Credit
  (`value-streams:value-stream-return-to-credit-qan2dn`), Contract to
  Renewal (`value-streams:value-stream-contract-to-renewal-5x3r4x`),
  Acquire to Retire (`value-streams:value-stream-acquire-to-retire-g5x89g`).

### Catalog index conformance (CR-VS-06)

- `CATALOG.yaml` added (machine-generated; 11 entities indexed) with the
  catalog identity block in `metamodel-pointer.yaml` per
  CR-CATALOG-STRUCT-06a.
- Vendored toolchain from dea-metaframework v2.6.0
  (`scripts/regenerate_catalog.py`, `scripts/check_catalog_index.py`,
  `catalog-index-schema/catalog-index-schema.json`) with a documented
  local extension adding the `value-stream` level token (upstream gap
  filed as dea-metaframework issue #51).
- `catalog-conformance` workflow added: freshness gate + index schema
  validation (fetch-depth 0, head-SHA checkout).
