# Discharge to Bill

Admitted Value Stream record (`value-streams:value-stream-discharge-to-bill-3k7wbb`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-discharge-to-bill-3k7wbb` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | healthcare · industry-specific |
| Record | [`value-streams-value-stream-discharge-to-bill-3k7wbb.yaml`](./value-streams-value-stream-discharge-to-bill-3k7wbb.yaml) — authoritative |

## 2. Definition

> The end-to-end healthcare revenue-cycle back end from discharge through charge capture, coding, and final billing to collected payment.

## 3. Value proposition and served party

**Outcome:** A clean, collected final bill for the care episode.

## 4. Stream boundary

**Entry criterion:** A patient is discharged.

**Exit criterion:** The final bill is produced, adjudicated, and collected.

**In scope** (from the record's `scope.includes`):

- Charge capture
- Coding and clinical documentation improvement
- Claim production and adjudication
- Final billing and collections

**Out of scope** (each concern owned by the named neighbour):

- Pre-episode coverage verification (Patient Access to Admission)
- General financial reporting (Record to Report)

## 5. Value stages

Discharge to Bill decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Capture Charges

Capture all billable charges for the episode.

| Aspect | Value |
|---|---|
| Entry criterion | The patient is discharged. |
| Exit criterion | Charges are captured and reconciled. |
| Outcome | A complete charge record. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### Stage 2: Code and Document

Code the episode with complete clinical documentation.

| Aspect | Value |
|---|---|
| Entry criterion | Charges are captured. |
| Exit criterion | Codes are finalized. |
| Outcome | Finalized, defensible codes. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 3: Produce Claim

Produce and submit the claim.

| Aspect | Value |
|---|---|
| Entry criterion | Codes are finalized. |
| Exit criterion | The claim is submitted and adjudicated. |
| Outcome | An adjudicated claim. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

### Stage 4: Bill and Collect

Produce the final patient bill and collect.

| Aspect | Value |
|---|---|
| Entry criterion | The claim is adjudicated. |
| Exit criterion | The final bill is collected. |
| Outcome | A clean, collected final bill. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c`, `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-g9zpnq`
- `processes:process-eo-operate-44jsrp`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-admission-to-discharge` — Discharge starts this stream.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-record-to-report` — Collected revenue is recorded and reported.

## 8. Measurement

- **Clinical documentation completion time** (stage: Code and Document) — Elapsed time from discharge to complete documentation. → [`dea:metric-clinical-documentation-completion-time`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-007 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-017) from the CR-VS-11 industry evidence register extension. Industry-specific chain (healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
