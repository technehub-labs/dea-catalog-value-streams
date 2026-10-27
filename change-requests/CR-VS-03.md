# CR-VS-03 — First Admission Gate: Order to Cash, Procure to Pay, Issue to Resolve, Hire to Retire

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-value-streams` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-27 |
| Depends on | CR-VS-01 (merged, PR #3), CR-VS-02 (merged, PR #4) |
| Blocks | CR-VS-04+ (subsequent tranches, E2 candidate admissions) |
| Method | Admission gate per the org pattern: evidence ≥ E2, distinctness closed, content-addressed id, provenance ladder |

## 1. Background and problem statement

CR-VS-02 closed distinctness for the universe and named the admission-ready set: VSC-001, VSC-002, VSC-003, VSC-006 (all E3/high, pairwise distinct or distinct-with-boundary). This CR admits those four as the catalog's first canonical records under `entities/v1-alpha/`.

## 2. Admissions

| Candidate | Admitted record | id |
|---|---|---|
| VSC-001 | Order to Cash | `value-streams:value-stream-order-to-cash-sc8gbu` |
| VSC-002 | Procure to Pay | `value-streams:value-stream-procure-to-pay-utma5c` |
| VSC-003 | Issue to Resolve | `value-streams:value-stream-issue-to-resolve-crmbay` |
| VSC-006 | Hire to Retire | `value-streams:value-stream-hire-to-retire-n6szcc` |

Each record carries: the CR-MET-014 field set (definition, outcome, entry/exit criteria, aggregated capability refs), `metamodel_pin: 1.0.0`, `lifecycle_status: active`, evidence sources citing the register, an evidence rationale that cites the applicable CR-VS-02 boundary statements, and a two-step provenance ladder (candidate → admitted).

## 3. Gate checklist (per candidate)

- Evidence at E3/high from ≥1 register source: VSC-001 (SRC-002, SRC-006), VSC-002 (SRC-002, SRC-006), VSC-003 (SRC-006), VSC-006 (SRC-006).
- Distinctness: all four pairwise DISTINCT in the CR-VS-02 sweep; boundary statements (001/005 fulfillment-exit; 002/006 settlement-counterparty) cited in the record evidence rationale rather than re-derived.
- Content-addressed id: 6-char suffix over the 31-symbol alphabet per `dea-metaframework/docs/id-system.md` §2.5; suffix assigned once at canonicalization (record serialization with the id hash field neutralized), never recomputed against live content (rename-stability contract).
- Path-id consistency (IDM-005): `entities/v1-alpha/value-stream-<slug>-<hash6>/value-streams-value-stream-<slug>-<hash6>.yaml`.
- Per-entity README (IDM-007): present in each subtree.
- Entry schema validation: each record validates against `schemas/entity.schema.json` (verified locally, 0 errors; the `validate-entries` workflow now has entries to validate — the empty-skip guard no longer triggers).

## 4. Cross-repo references

- `aggregated_capability_refs` resolve against `dea-catalog-business-capabilities` ids: `capability-customer-management-f3n8wb`, `capability-operations-management-pm3w8k`, `capability-financial-stewardship-c7xtfk`, `capability-sourcing-and-procurement-esucp4`, `capability-workforce-management-9e8d8s`, `capability-workforce-planning-b43rhm` (all verified present in that catalog).
- `customer_ref` is deliberately omitted at this stage: the actors catalog does not yet carry generic customer/supplier/employee actor records, and fabricating references would violate the reference-resolution contract. A follow-up CR adds them when the actors catalog lands those records.

## 5. Non-goals

- No E2/medium candidate admissions (VSC-004, VSC-005, VSC-008, VSC-009): they passed the sweep but wait for per-candidate evidence work (CR-VS-04).
- No universe reclassification beyond admission bookkeeping: candidates admitted keep their universe records (append-only); the universe `compiled` note records the admission.
- No schema, workflow, or pointer changes.

## 6. Verification

- All four records parse and validate against `schemas/entity.schema.json` (0 errors each).
- Ids globally unique; suffix well-formed (6 chars over `abcdefghjkmnpqrstuvwxyz23456789`).
- Path-id consistency holds for all four; per-entity READMEs present.
- All capability refs resolve against the business-capabilities catalog.
- `catalog-research/candidate-universe.yaml` `compiled` note updated (v0.2 → admission noted); machine-readable admission map recorded in `catalog-research/admission-register.yaml`.

## 7. Follow-on

1. CR-VS-04: E2 candidate evidence work and second-tranche admissions.
2. Actors catalog dependency: generic actor records for customer/supplier/employee, then `customer_ref` backfill CR in this repo.
3. Metaframework: register the `value-streams` namespace token in `dea-metaframework/docs/id-system.md` §2.1 (the token is used here first; the registry update is the org-side ratification).
