# CR-VS-01 — Catalog Research Foundations: Candidate Universe Seed and Evidence Register

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-value-streams` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-27 |
| Depends on | Phase 0 + Phase 2 scaffolding (merged, PR #2 / `3a6cc21`); metamodel CR-MET-014 field set (technehub-labs/dea-metamodel#201) |
| Blocks | CR-VS-02+ (distinctness sweep, admission gates) |
| Method | Org-wide catalog research pattern (CR-DEA-BC-02 adapted): candidate universe → evidence register → distinctness sweep → admission gate |

## 1. Background and problem statement

The Value Stream catalog is scaffolded (entry schema, entities/v1-alpha layout, validate-entries gate) but has no research foundation. Content population cannot begin with entries directly: the org-wide method requires a candidate universe derived from a recorded evidence register, with every candidate carrying `canonical: false` until an admission CR closes the gate.

## 2. Objective

Open `catalog-research/` with the evidence register and candidate universe for first-order, enterprise-general value streams, seeding the admission pipeline without admitting anything.

## 3. What this CR does

- `catalog-research/evidence-register.yaml` (v0.1): 6 sources across 6 source classes — BIZBOK (value stream identity; entry-criterion anchoring), APQC PCF (cross-industry chain structure), OMG BACM (formal ValueStream semantics; stage decomposition deferred), TOGAF value streams × capabilities (corroborates `dea:aggregates` binding), SAFe/Lean guidance (operational vs. development stream disambiguation), enterprise process-chain literature (cross-source name convergence).
- `catalog-research/candidate-universe.yaml` (v0.1): 9 VALUE-STREAM candidates (VSC-001..VSC-009) + 1 DEVELOPMENT-STREAM disambiguation record (VSC-010). Each candidate carries entry/exit criterion hypotheses, an outcome hypothesis, spanned capabilities (slug-level; resolve to ids at admission), sources, and distinctness notes. Three candidates (Order to Cash, Procure to Pay, Hire to Retire) at E3/high; six at E2/medium.
- `catalog-research/README.md`: method statement (4-step admission pipeline).

## 4. Explicit non-goals

- No canonical entries: nothing lands in `entities/v1-alpha/` under this CR.
- No distinctness decisions: VSC-007 vs. VSC-001 (Lead to Cash vs. Order to Cash) and VSC-008 vs. VSC-009 (Plan to Forecast vs. Record to Report) overlaps are flagged, not resolved; resolution belongs to the distinctness sweep (CR-VS-02).
- No metamodel changes: the entry schema stays as landed in Phase 2.

## 5. Verification

- YAML parses; candidate ids unique; every candidate cites ≥1 register source; register source ids referenced by candidates all exist (VSC-010 cites SRC-005; others cite SRC-002/SRC-006 as recorded).
- Counts in the universe header match the candidate list (9 VALUE-STREAM, 1 DEVELOPMENT-STREAM).
- No files under `entities/` touched; validate-entries skip guard unaffected.

## 6. Follow-on

1. CR-VS-02: distinctness sweep (pairwise; resolve the two flagged overlaps).
2. CR-VS-03: admission gate for the first candidates (target: the three E3/high candidates), producing the first `entities/v1-alpha/value-stream-<slug>-<hash6>/` records.
3. Metamodel-side: land CR-MET-014 (technehub-labs/dea-metamodel#201) so `metamodel_pin` has an upstream target.
