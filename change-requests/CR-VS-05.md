# CR-VS-05 — Third Tranche: Universe Expansion, Distinctness Sweep v0.2, and Admissions

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-value-streams` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-27 |
| Depends on | CR-VS-01 (PR #3), CR-VS-02 (PR #4), CR-VS-03 (PR #5), CR-VS-04 (PR #6) |
| Method | Universe expansion → distinctness sweep → admission gate, per the org pattern |

## 1. Background and problem statement

After CR-VS-04 the first-order operational and finance chains are admitted, but the chain inventory in SRC-006 (extended under this CR, register v0.3) shows further cross-industry chains that are first-order too: reverse logistics, subscription renewal, and asset lifecycle. This CR expands the universe, sweeps the new candidates, and admits those that pass.

## 2. Universe expansion (v0.4 → v0.5)

Register v0.3 extends SRC-006 with the chain-inventory observation; four candidates seeded at E3/high:

| Candidate | Name | Classification outcome |
|---|---|---|
| VSC-011 | Return to Credit | admitted |
| VSC-012 | Contract to Renewal | admitted |
| VSC-013 | Acquire to Retire | admitted |
| VSC-014 | Fault to Restore | **merged** into VSC-003 (RES-003) |

## 3. Distinctness sweep v0.2

All 38 new pairs swept (new × new + new × the 8 admitted). Verdicts: 38 DISTINCT-class (9 with boundary statements), 1 MERGED (RES-003), vacuous pairs involving the merged candidate. Cumulative: 74 verdicts, 0 UNRESOLVED.

- **RES-003 (MERGE)**: VSC-014 (Fault to Restore) is a naming variant of VSC-003 (Issue to Resolve) — same entry (fault/issue reported), same exit (restored/resolved and informed), same served party. Zero-axis difference. Fault to Restore is recorded as an alternate name on the Issue to Resolve record.
- Boundary statements recorded: 011/012 (transaction vs. relationship settlement), 012/006 (relationship type), 013/002 (supplier settlement vs. asset disposal), 013/005, 013/006 (lifecycle object).

## 4. Admissions (third tranche)

| Candidate | Admitted record | id |
|---|---|---|
| VSC-011 | Return to Credit | `value-streams:value-stream-return-to-credit-qan2dn` |
| VSC-012 | Contract to Renewal | `value-streams:value-stream-contract-to-renewal-5x3r4x` |
| VSC-013 | Acquire to Retire | `value-streams:value-stream-acquire-to-retire-g5x89g` |

Each record: CR-MET-014 field set, `metamodel_pin: 1.0.0`, `lifecycle_status: active`, evidence sources, rationale citing the CR-VS-05 boundary statements, two-step provenance ladder, content-addressed id (§2.5), per-entity README (IDM-007).

## 5. Non-goals

- No `customer_ref` population (actors-catalog dependency unchanged).
- No schema, workflow, or pointer changes.
- The Issue to Resolve record edit (alternate-name note) is content-only; per id-system §2.5 the suffix is assigned once at canonicalization and never recomputed against live content (rename-stability contract), so the record keeps its id.

## 6. Verification

- All 11 records (8 prior + 3 new) validate against `schemas/entity.schema.json`; ids globally unique; path-id consistency; per-entity READMEs present.
- Sweep coverage: the 38 new pairs exactly cover new × new + new × admitted; no duplicates; 0 UNRESOLVED.
- Register/universe/sweep/admission-register cross-consistency: 11 admitted, 2 merged (VSC-007, VSC-014), 1 disambiguation (VSC-010), universe total 14.
- `validate-entries` workflow simulation passes with count=11.

## 7. Follow-on

1. Actors catalog dependency → `customer_ref` backfill CR.
2. Metaframework: `value-streams` namespace token ratification (id-system §2.1).
3. Metamodel: land CR-MET-014 (technehub-labs/dea-metamodel#201).
4. First release cut per the dea-release-package program (CR-DEA-RP-01).
