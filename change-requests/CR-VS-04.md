# CR-VS-04 — Second-Tranche Evidence Work and Admissions: Concept to Launch, Plan to Deliver, Plan to Forecast, Record to Report

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-value-streams` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-27 |
| Depends on | CR-VS-01 (PR #3), CR-VS-02 (PR #4), CR-VS-03 (PR #5, merged `aaamem2`) |
| Blocks | CR-VS-05+ (remaining universe work: none pending; cross-repo follow-ons) |
| Method | Evidence upgrade then admission gate, per the org pattern |

## 1. Background and problem statement

CR-VS-02's sweep left four E2/medium candidates (VSC-004, VSC-005, VSC-008, VSC-009) distinct but evidence-pending; CR-VS-03 admitted the first tranche only. This CR closes the evidence gap with genuine register extensions, then admits the second tranche.

## 2. Evidence work (register v0.1 → v0.2)

Two extensions, both grounded in already-recorded sources (no new sources invented):

- **SRC-002 (APQC PCF)** — new observation: the PCF's category structure extends beyond the operational chains to product/service development categories (concept-through-launch), financial planning and analysis categories (planning-through-forecast), and financial reporting categories (record-through-report). This corroborates enterprise-generality for VSC-004, VSC-005, VSC-008, VSC-009.
- **SRC-003 (OMG BACM)** — new observation: BACM anchors value delivery to stakeholders generally, not only external customers; a value stream may deliver value to an internal stakeholder such as enterprise governance. This resolves the internal-chain scope question for the finance-side candidates (VSC-008, VSC-009).

Universe bumped to v0.3: all four candidates raised to E3/high with extended source citations (VSC-004: +SRC-002; VSC-005: SRC-002 already cited; VSC-008/009: +SRC-002, +SRC-003).

## 3. Admissions (second tranche)

| Candidate | Admitted record | id |
|---|---|---|
| VSC-004 | Concept to Launch | `value-streams:value-stream-concept-to-launch-nhvatv` |
| VSC-005 | Plan to Deliver | `value-streams:value-stream-plan-to-deliver-smmwpx` |
| VSC-008 | Plan to Forecast | `value-streams:value-stream-plan-to-forecast-89vb4q` |
| VSC-009 | Record to Report | `value-streams:value-stream-record-to-report-zw9z2r` |

Each record carries the CR-MET-014 field set, `metamodel_pin: 1.0.0`, `lifecycle_status: active`, evidence sources, a rationale citing the applicable CR-VS-02 boundary statements, and a three-step provenance ladder (candidate → evidence-raised candidate → admitted).

## 4. Gate checklist (per candidate)

- Evidence at E3/high: all four raised via the register v0.2 extension, with per-candidate source citations (see §2).
- Distinctness: all four DISTINCT or DISTINCT-with-boundary in the CR-VS-02 sweep; boundary statements cited in record rationales (001/005 fulfillment-exit; 005/008 exit-condition; 008/009 RES-002 forward/backward-looking).
- Content-addressed id per id-system §2.5 (suffix assigned once at canonicalization; `scripts/hash6.py`).
- Path-id consistency (IDM-005); per-entity READMEs (IDM-007).
- Entry schema validation (verified locally, 0 errors each).

## 5. Non-goals

- No new candidates: the universe's remaining records are VSC-007 (merged, append-only) and VSC-010 (disambiguation, no admission path). The first-order universe is now fully resolved.
- No `customer_ref` population (actors-catalog dependency unchanged; CR-VS-03 §4 still governs).
- No schema, workflow, or pointer changes.

## 6. Verification

- All 8 records (4 prior + 4 new) validate against `schemas/entity.schema.json`; ids globally unique; suffixes well-formed; path-id consistency and per-entity READMEs verified.
- Register and universe YAML parse; candidate source citations resolve against register source ids; universe counts consistent (8 VALUE-STREAM admitted, 1 MERGED, 1 DEVELOPMENT-STREAM).
- Admission register v0.2: 8 admissions recorded; counts consistent.

## 7. Follow-on

1. Actors catalog dependency: generic customer/supplier/employee actor records, then the `customer_ref` backfill CR here.
2. Metaframework: register the `value-streams` namespace token in `dea-metaframework/docs/id-system.md` §2.1.
3. Metamodel: land CR-MET-014 (technehub-labs/dea-metamodel#201) for the upstream `metamodel_pin` target.
4. Release packaging per the dea-release-package program (CR-DEA-RP-01) once the catalog's first release is cut.
