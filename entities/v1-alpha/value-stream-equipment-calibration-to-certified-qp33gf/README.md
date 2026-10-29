# Equipment Calibration to Certified

Admitted Value Stream record (`value-streams:value-stream-equipment-calibration-to-certified-qp33gf`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-equipment-calibration-to-certified-qp33gf` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | manufacturing · industry-specific |
| Record | [`value-streams-value-stream-equipment-calibration-to-certified-qp33gf.yaml`](./value-streams-value-stream-equipment-calibration-to-certified-qp33gf.yaml) — authoritative |

## 2. Definition

> The metrology stream from calibration due through calibration execution to certified status.

## 3. Value proposition and served party

**Outcome:** Calibration-certified equipment available for use.

## 4. Stream boundary

**Entry criterion:** A calibration due date is reached.

**Exit criterion:** The equipment is certified for use.

**In scope** (from the record's `scope.includes`):

- Calibration execution
- Certification
- Release to use

**Out of scope** (each concern owned by the named neighbour):

- Maintenance
- Equipment procurement

## 5. Value stages

Equipment Calibration to Certified decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Calibrate

Execute the calibration.

| Aspect | Value |
|---|---|
| Entry criterion | Calibration falls due. |
| Exit criterion | Calibration is complete. |
| Outcome | Calibration results. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-j9cjzz` |

### Stage 2: Certify

Certify against the standard.

| Aspect | Value |
|---|---|
| Entry criterion | Calibration is complete. |
| Exit criterion | The equipment is certified. |
| Outcome | A certified instrument. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 3: Release to Use

Release the equipment for use.

| Aspect | Value |
|---|---|
| Entry criterion | The equipment is certified. |
| Exit criterion | The equipment is in use. |
| Outcome | Released equipment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-regulation-management-gya4d8`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-j9cjzz`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-zwzmbd`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Calibration on-time rate** (stream-level) — Share of calibrations completed before due date.

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-055) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
