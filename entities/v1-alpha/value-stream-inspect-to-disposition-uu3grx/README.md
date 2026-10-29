# Inspect to Disposition

Admitted Value Stream record (`value-streams:value-stream-inspect-to-disposition-uu3grx`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-inspect-to-disposition-uu3grx` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | manufacturing, logistics-transportation · industry-specific |
| Record | [`value-streams-value-stream-inspect-to-disposition-uu3grx.yaml`](./value-streams-value-stream-inspect-to-disposition-uu3grx.yaml) — authoritative |

## 2. Definition

> The quality stream from inspection trigger through evaluation to disposition of the material.

## 3. Value proposition and served party

**Outcome:** A documented disposition for every inspected lot.

## 4. Stream boundary

**Entry criterion:** An inspection is triggered (incoming, in-process, or final).

**Exit criterion:** The lot is dispositioned.

**In scope** (from the record's `scope.includes`):

- Sampling and inspection
- Evaluation against specification
- Disposition decision
- Documentation

**Out of scope** (each concern owned by the named neighbour):

- Supplier quality (Procure to Pay receipt leg)
- Warranty claims

## 5. Value stages

Inspect to Disposition decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Inspect

Sample and inspect the lot.

| Aspect | Value |
|---|---|
| Entry criterion | An inspection is triggered. |
| Exit criterion | The inspection is complete. |
| Outcome | Inspection results. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 2: Evaluate

Evaluate results against specification.

| Aspect | Value |
|---|---|
| Entry criterion | The inspection is complete. |
| Exit criterion | The evaluation is complete. |
| Outcome | An evaluation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 3: Disposition

Decide the lot disposition.

| Aspect | Value |
|---|---|
| Entry criterion | The evaluation is complete. |
| Exit criterion | The disposition is decided. |
| Outcome | A disposition. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 4: Document

Document and communicate the disposition.

| Aspect | Value |
|---|---|
| Entry criterion | The disposition is decided. |
| Exit criterion | Documentation is complete. |
| Outcome | Documented disposition. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-4xn4d6` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-44jsrp`
- `processes:process-ge-operate-zwaes5`
- `processes:process-fa-operate-4xn4d6`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Lot rejection rate** (stream-level) — Share of inspected lots rejected.

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-052) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing, logistics-transportation); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
