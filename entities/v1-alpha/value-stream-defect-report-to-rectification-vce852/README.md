# Defect Report to Rectification

Admitted Value Stream record (`value-streams:value-stream-defect-report-to-rectification-vce852`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-defect-report-to-rectification-vce852` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | construction-real-estate · industry-specific |
| Record | [`value-streams-value-stream-defect-report-to-rectification-vce852.yaml`](./value-streams-value-stream-defect-report-to-rectification-vce852.yaml) — authoritative |

## 2. Definition

> The post-handover stream from defect report through inspection to rectified and accepted defect.

## 3. Value proposition and served party

**Outcome:** A rectified, accepted defect within the liability period.

## 4. Stream boundary

**Entry criterion:** A defect is reported in the liability period.

**Exit criterion:** The rectification is accepted.

**In scope** (from the record's `scope.includes`):

- Defect inspection
- Rectification
- Re-inspection and acceptance

**Out of scope** (each concern owned by the named neighbour):

- Build quality (Build to Handover)
- Warranty claims

## 5. Value stages

Defect Report to Rectification decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Inspect Defect

Inspect the reported defect.

| Aspect | Value |
|---|---|
| Entry criterion | A defect is reported. |
| Exit criterion | The inspection is complete. |
| Outcome | An inspected defect. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 2: Rectify

Rectify the defect.

| Aspect | Value |
|---|---|
| Entry criterion | The inspection is complete. |
| Exit criterion | Rectification is complete. |
| Outcome | A rectified defect. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Re-inspect and Accept

Re-inspect and obtain acceptance.

| Aspect | Value |
|---|---|
| Entry criterion | Rectification is complete. |
| Exit criterion | The rectification is accepted. |
| Outcome | An accepted rectification. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-customer-management-f3n8wb`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-2jnz85`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Defect rectification cycle time** (stream-level) — Elapsed days from report to acceptance.

## 9. Evidence and admission

**Evidence sources:** SRC-017 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-096) from the CR-VS-11 industry evidence register extension. Industry-specific chain (construction-real-estate); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
