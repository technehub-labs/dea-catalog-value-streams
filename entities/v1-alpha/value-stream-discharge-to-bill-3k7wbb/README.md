---
documentation_generated_from: value-streams-value-stream-discharge-to-bill-3k7wbb.yaml
id: value-streams:value-stream-discharge-to-bill-3k7wbb
name: Discharge to Bill
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- healthcare
specificity: industry-specific
entry_criterion: A patient is discharged.
exit_criterion: The final bill is produced, adjudicated, and collected.
outcome: A clean, collected final bill for the care episode.
stages:
- Capture Charges
- Code and Document
- Produce Claim
- Bill and Collect
capabilities:
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-eo-operate-44jsrp
- processes:process-fa-operate-g9zpnq
- processes:process-fa-operate-sdppmp
metrics:
- Clinical documentation completion time
upstream:
- value-stream-admission-to-discharge
downstream:
- value-stream-record-to-report
evidence_sources:
- SRC-007
---

# Discharge to Bill

`value-streams:value-stream-discharge-to-bill-3k7wbb` · **operational** · healthcare · industry-specific

> The end-to-end healthcare revenue-cycle back end from discharge through charge capture, coding, and final billing to collected payment.

**Outcome:** A clean, collected final bill for the care episode.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-discharge-to-bill-3k7wbb.yaml`](./value-streams-value-stream-discharge-to-bill-3k7wbb.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Capture Charges"]
  S2["2. Code and Document"]
  S3["3. Produce Claim"]
  S4["4. Bill and Collect"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Capture Charges** | The patient is discharged. | Charges are captured and reconciled. | 2 | 1 | no |
| 2 | **Code and Document** | Charges are captured. | Codes are finalized. | 2 | 1 | no |
| 3 | **Produce Claim** | Codes are finalized. | The claim is submitted and adjudicated. | 1 | 1 | no |
| 4 | **Bill and Collect** | The claim is adjudicated. | The final bill is collected. | 2 | 1 | yes |

### 1. Capture Charges

Capture all billable charges for the episode.

| Aspect | Value |
|---|---|
| Entry criterion | The patient is discharged. |
| Exit criterion | Charges are captured and reconciled. |
| Outcome | A complete charge record. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### 2. Code and Document

Code the episode with complete clinical documentation.

| Aspect | Value |
|---|---|
| Entry criterion | Charges are captured. |
| Exit criterion | Codes are finalized. |
| Outcome | Finalized, defensible codes. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### 3. Produce Claim

Produce and submit the claim.

| Aspect | Value |
|---|---|
| Entry criterion | Codes are finalized. |
| Exit criterion | The claim is submitted and adjudicated. |
| Outcome | An adjudicated claim. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

### 4. Bill and Collect

Produce the final patient bill and collect.

| Aspect | Value |
|---|---|
| Entry criterion | The claim is adjudicated. |
| Exit criterion | The final bill is collected. |
| Outcome | A clean, collected final bill. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` · `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## Scope boundary

**Entry:** A patient is discharged.

**Exit:** The final bill is produced, adjudicated, and collected.

**In scope**

- Charge capture
- Coding and clinical documentation improvement
- Claim production and adjudication
- Final billing and collections

**Out of scope** (owned by the named neighbour)

- Pre-episode coverage verification (Patient Access to Admission)
- General financial reporting (Record to Report)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-g9zpnq`
- `processes:process-eo-operate-44jsrp`
- `processes:process-fa-operate-sdppmp`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [admission to discharge](../value-stream-admission-to-discharge-xeuu5u/README.md) — Discharge starts this stream.

**Downstream** (this stream's exit feeds their entry):

- [record to report](../value-stream-record-to-report-zw9z2r/README.md) — Collected revenue is recorded and reported.

## Measurement

- **Clinical documentation completion time** (stage: Code and Document) — Elapsed time from discharge to complete documentation. → [`dea:metric-clinical-documentation-completion-time`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-007 | industry-reference-model | Healthcare industry reference models (patient-access and revenue-cycle chains, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-017) from the CR-VS-11 industry evidence register extension. Industry-specific chain (healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
