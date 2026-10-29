# Recall to Remediation

Admitted Value Stream record (`value-streams:value-stream-recall-to-remediation-kq3mwc`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-recall-to-remediation-kq3mwc` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | manufacturing, retail-commerce · industry-specific |
| Record | [`value-streams-value-stream-recall-to-remediation-kq3mwc.yaml`](./value-streams-value-stream-recall-to-remediation-kq3mwc.yaml) — authoritative |

## 2. Definition

> The product-recall stream from recall decision through affected-unit traceability to remediation closure.

## 3. Value proposition and served party

**Outcome:** All affected units remediated with the recall closed.

## 4. Stream boundary

**Entry criterion:** A recall decision is made.

**Exit criterion:** The recall is closed with remediation complete.

**In scope** (from the record's `scope.includes`):

- Affected-unit identification
- Notification and retrieval
- Remediation
- Closure

**Out of scope** (each concern owned by the named neighbour):

- Quality (Inspect to Disposition)
- Field service

## 5. Value stages

Recall to Remediation decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Identify Affected Units

Trace affected units through the distribution chain.

| Aspect | Value |
|---|---|
| Entry criterion | A recall is decided. |
| Exit criterion | Affected units are identified. |
| Outcome | An affected-unit list. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

### Stage 2: Notify and Retrieve

Notify and retrieve affected units.

| Aspect | Value |
|---|---|
| Entry criterion | Units are identified. |
| Exit criterion | Units are retrieved. |
| Outcome | Retrieved units. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57`, `processes:process-eo-operate-zwzmbd` |

### Stage 3: Remediate

Remediate or replace the units.

| Aspect | Value |
|---|---|
| Entry criterion | Units are retrieved. |
| Exit criterion | Remediation is complete. |
| Outcome | Remediated units. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 4: Close Recall

Close the recall with verification.

| Aspect | Value |
|---|---|
| Entry criterion | Remediation is complete. |
| Exit criterion | The recall is closed. |
| Outcome | A closed recall. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-operate-ucxpz4`
- `processes:process-eo-operate-zh9m57`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-2jnz85`
- `processes:process-ge-operate-zwaes5`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Recall retrieval rate** (stream-level) — Share of affected units retrieved and remediated.

## 9. Evidence and admission

**Evidence sources:** SRC-016, SRC-013 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-056) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing, retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
