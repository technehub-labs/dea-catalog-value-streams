# Batch to Release

Admitted Value Stream record (`value-streams:value-stream-batch-to-release-mzc7cf`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-batch-to-release-mzc7cf` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | life-sciences · industry-specific |
| Record | [`value-streams-value-stream-batch-to-release-mzc7cf.yaml`](./value-streams-value-stream-batch-to-release-mzc7cf.yaml) — authoritative |

## 2. Definition

> The GMP stream from batch start through manufacturing and quality control to released batch.

## 3. Value proposition and served party

**Outcome:** A quality-released batch available for distribution.

## 4. Stream boundary

**Entry criterion:** A production batch is scheduled.

**Exit criterion:** The batch is released by quality.

**In scope** (from the record's `scope.includes`):

- Batch manufacturing
- Quality control testing
- Batch record review and release

**Out of scope** (each concern owned by the named neighbour):

- Supply planning (Plan to Deliver)
- Distribution (Ship to Consignee)

## 5. Value stages

Batch to Release decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Manufacture Batch

Manufacture the batch.

| Aspect | Value |
|---|---|
| Entry criterion | A batch is scheduled. |
| Exit criterion | The batch is manufactured. |
| Outcome | A manufactured batch. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-xud3hs` |

### Stage 2: Test Quality Control

Run quality-control testing.

| Aspect | Value |
|---|---|
| Entry criterion | The batch is manufactured. |
| Exit criterion | Testing is complete. |
| Outcome | QC results. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 3: Review and Release

Review the batch record and release.

| Aspect | Value |
|---|---|
| Entry criterion | Testing is complete. |
| Exit criterion | The batch is released. |
| Outcome | A released batch. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-44jsrp`
- `processes:process-ge-operate-zwaes5`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Batch release cycle time** (stream-level) — Elapsed time from manufacture to release.

## 9. Evidence and admission

**Evidence sources:** SRC-018 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-099) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
