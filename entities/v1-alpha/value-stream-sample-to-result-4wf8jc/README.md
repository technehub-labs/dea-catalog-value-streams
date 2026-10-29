# Sample to Result

Admitted Value Stream record (`value-streams:value-stream-sample-to-result-4wf8jc`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-sample-to-result-4wf8jc` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | life-sciences, healthcare · industry-specific |
| Record | [`value-streams-value-stream-sample-to-result-4wf8jc.yaml`](./value-streams-value-stream-sample-to-result-4wf8jc.yaml) — authoritative |

## 2. Definition

> The diagnostics stream from sample accessioning through testing to a released, communicated result.

## 3. Value proposition and served party

**Outcome:** A released result communicated to the ordering clinician.

## 4. Stream boundary

**Entry criterion:** A sample is received.

**Exit criterion:** The result is released and communicated.

**In scope** (from the record's `scope.includes`):

- Accessioning
- Testing
- Result review and release

**Out of scope** (each concern owned by the named neighbour):

- Patient treatment (Referral to Treatment)
- Clinical trials lab work

## 5. Value stages

Sample to Result decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Accession Sample

Accession and register the sample.

| Aspect | Value |
|---|---|
| Entry criterion | A sample is received. |
| Exit criterion | The sample is accessioned. |
| Outcome | An accessioned sample. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

### Stage 2: Test

Perform the diagnostic testing.

| Aspect | Value |
|---|---|
| Entry criterion | The sample is accessioned. |
| Exit criterion | Testing is complete. |
| Outcome | Test results. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-operate-44jsrp`, `processes:process-eo-operate-xud3hs` |

### Stage 3: Review and Release

Review and release the result.

| Aspect | Value |
|---|---|
| Entry criterion | Testing is complete. |
| Exit criterion | The result is released and communicated. |
| Outcome | A communicated result. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-ge-operate-zwaes5`, `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-customer-management-f3n8wb`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-xud3hs`
- `processes:process-ge-operate-zwaes5`
- `processes:process-pr-operate-bbe384`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-referral-to-treatment` — Released results inform treatment.

**Downstream streams:** none recorded.

## 8. Measurement

- **Sample-to-result turnaround** (stream-level) — Elapsed time from accessioning to released result.

## 9. Evidence and admission

**Evidence sources:** SRC-018, SRC-007 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-104) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences, healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
