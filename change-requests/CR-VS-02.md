# CR-VS-02 — Distinctness Sweep v0.1

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-value-streams` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-27 |
| Depends on | CR-VS-01 (merged, PR #3 / `68a7880`) |
| Blocks | CR-VS-03 (first admission gate) |
| Method | Pairwise distinctness per the org pattern (`DISTINCTNESS-SWEEP-v0.1.md` in `dea-catalog-business-capabilities`) |

## 1. Background and problem statement

CR-VS-01 seeded 9 VALUE-STREAM candidates + 1 disambiguation record and flagged two
overlaps as open: VSC-007 (Lead to Cash) vs. VSC-001 (Order to Cash), and VSC-008
(Plan to Forecast) vs. VSC-009 (Record to Report). The admission gate (CR-VS-03)
requires that every admitted candidate be pairwise distinct from every other
admitted candidate on entry, exit, and served-party; the sweep closes this
requirement before any admission.

## 2. Distinctness test

A value stream candidate is distinct from another iff they differ on at least
two of the three first-order axes (per the BIZBOK identity tests, SRC-001):

- **Entry criterion**: the customer-visible event that triggers the stream.
- **Exit criterion**: the condition that confirms value delivered.
- **Served party**: whose need is satisfied at the exit.

Two candidates differing on only one axis are **overlap-flagged** and require an
explicit boundary statement or a merge.

## 3. Sweep results (machine-readable: `catalog-research/distinctness-sweep.yaml`)

| Pair | Verdict | Rationale |
|---|---|---|
| VSC-001 / VSC-002 | DISTINCT | Different entry (customer order vs. internal need), exit (customer payment vs. supplier payment), served party (external customer vs. internal need owner) |
| VSC-001 / VSC-003 | DISTINCT | Fulfillment chain vs. service restoration; different entry (order vs. issue), exit (payment vs. resolution) |
| VSC-001 / VSC-004 | DISTINCT | Operational chain vs. innovation chain; different entry, exit, served party (market vs. customer) |
| VSC-001 / VSC-005 | DISTINCT with boundary | Overlap at fulfillment only: VSC-005 exits at delivery per plan, VSC-001 exits at payment recognition. Boundary statement recorded: fulfillment is shared vocabulary, the exit is the discriminator |
| VSC-001 / VSC-006 | DISTINCT | External customer chain vs. workforce chain; all three axes differ |
| VSC-001 / VSC-007 | **RESOLVED: MERGE** | Same exit (paying, fulfilled customer); VSC-007 differs only on entry (demand generation vs. order placement). One axis is insufficient per §2. VSC-007 is merged into VSC-001 with its entry folded in as the pre-order stage of the boundary statement |
| VSC-001 / VSC-008 | DISTINCT | Customer chain vs. enterprise-internal planning chain; served parties differ |
| VSC-001 / VSC-009 | DISTINCT | Customer chain vs. finance reporting chain; served parties differ |
| VSC-002 / VSC-003 | DISTINCT | Supply chain vs. service chain; all three axes differ |
| VSC-002 / VSC-004 | DISTINCT | Different entry, exit, served party |
| VSC-002 / VSC-005 | DISTINCT | Supply-side vs. production-side; entry differs (requisition vs. demand plan) |
| VSC-002 / VSC-006 | DISTINCT with boundary | Both end in settlement (supplier vs. employee obligations); entries and served parties differ. Boundary: settlement is shared vocabulary, the counterparty is the discriminator |
| VSC-002 / VSC-007 | VACUOUS | VSC-007 merged into VSC-001 (RES-001); recorded for completeness |
| VSC-002 / VSC-008 | DISTINCT | Supply chain vs. planning chain |
| VSC-002 / VSC-009 | DISTINCT | Supply chain vs. reporting chain |
| VSC-003 / VSC-004 | DISTINCT | All three axes differ |
| VSC-003 / VSC-005 | DISTINCT | Service restoration vs. planned delivery |
| VSC-003 / VSC-006 | DISTINCT | External customer issue vs. workforce lifecycle |
| VSC-003 / VSC-007 | Vacuous | VSC-007 merged into VSC-001 |
| VSC-003 / VSC-008 | DISTINCT | Customer chain vs. planning chain |
| VSC-003 / VSC-009 | DISTINCT | Customer chain vs. reporting chain |
| VSC-004 / VSC-005 | DISTINCT | Innovation chain vs. production chain |
| VSC-004 / VSC-006 | DISTINCT | All three axes differ |
| VSC-004 / VSC-007 | Vacuous | VSC-007 merged into VSC-001 |
| VSC-004 / VSC-008 | DISTINCT | Market-facing vs. enterprise-internal |
| VSC-004 / VSC-009 | DISTINCT | Market-facing vs. stakeholder reporting |
| VSC-005 / VSC-006 | DISTINCT | Production vs. workforce |
| VSC-005 / VSC-007 | Vacuous | VSC-007 merged into VSC-001 |
| VSC-005 / VSC-008 | DISTINCT with boundary | Planning vocabulary shared (plan/forecast); VSC-005 exits at delivery, VSC-008 at ratified forecast. Boundary: the exit condition is the discriminator |
| VSC-005 / VSC-009 | DISTINCT | Delivery vs. reporting |
| VSC-006 / VSC-007 | Vacuous | VSC-007 merged into VSC-001 |
| VSC-006 / VSC-008 | DISTINCT | Workforce vs. planning; served parties differ |
| VSC-006 / VSC-009 | DISTINCT | Workforce vs. reporting |
| VSC-007 / VSC-008 | Vacuous | VSC-007 merged into VSC-001 |
| VSC-007 / VSC-009 | Vacuous | VSC-007 merged into VSC-001 |
| VSC-008 / VSC-009 | **RESOLVED: BOUNDARY STATEMENT** | Both finance-side and both enterprise-internal. Entries differ (planning cycle opens vs. transaction recorded), exits differ (ratified forecast vs. attested report). Two axes differ → distinct, but the shared finance vocabulary requires the boundary statement: planning produces the forward-looking commitment; recording/reporting produces the backward-looking attestation. Distinct is retained |
| VSC-010 (disambiguation) | N/A | Not a candidate; blocks development-stream misclassification (SRC-005) |

## 4. Resolutions

1. **VSC-007 (Lead to Cash) is merged into VSC-001 (Order to Cash)**: one-axis
   difference fails the §2 test. The VSC-001 entry criterion is widened to
   "a customer need converts to an order" with the demand-generation stage
   noted as the pre-order boundary. VSC-007 leaves the universe as merged
   (record retained, classification becomes MERGED; no deletion — the sweep
   is append-only evidence).
2. **VSC-008 / VSC-009 remain distinct** with an explicit boundary statement
   (forward-looking commitment vs. backward-looking attestation).
3. Three DISTINCT-with-boundary pairs recorded (VSC-001/005, VSC-002/006,
   VSC-005/008): boundary statements are recorded in the machine-readable
   sweep so admissions cite them rather than re-deriving.

## 5. Effect on the universe

- 8 VALUE-STREAM candidates remain (VSC-001..VSC-006, VSC-008, VSC-009);
  VSC-007 merged; VSC-010 unchanged as disambiguation.
- Admission-ready (E3/high, distinctness closed): VSC-001, VSC-002, VSC-003, VSC-006.
- E2/medium candidates (VSC-004, VSC-005, VSC-008, VSC-009) pass the sweep but
  wait for per-candidate evidence at E2+ admission, which is CR-VS-03 scope
  for the first tranche only.

## 6. Verification

- All 36 ordered pairs swept; every verdict DISTINCT, DISTINCT-with-boundary,
  MERGE, or vacuous; no UNRESOLVED remains.
- `distinctness-sweep.yaml` parses; every pair cites both candidate ids that
  exist in `candidate-universe.yaml` v0.1; merge resolution recorded on both
  the sweep and the universe update.
- `entities/v1-alpha/` untouched; no admissions in this CR.
