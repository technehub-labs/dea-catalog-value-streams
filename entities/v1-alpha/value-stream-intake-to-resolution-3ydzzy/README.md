# Intake to Resolution

Admitted Value Stream record (`value-streams:value-stream-intake-to-resolution-3ydzzy`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-intake-to-resolution-3ydzzy` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | public-sector · industry-specific |
| Record | [`value-streams-value-stream-intake-to-resolution-3ydzzy.yaml`](./value-streams-value-stream-intake-to-resolution-3ydzzy.yaml) — authoritative |

## 2. Definition

> The case-handling stream from case intake through investigation to resolved case with recorded outcome.

## 3. Value proposition and served party

**Outcome:** A resolved case with recorded, communicated outcome.

## 4. Stream boundary

**Entry criterion:** A case is reported or referred.

**Exit criterion:** The case is resolved and the outcome recorded.

**In scope** (from the record's `scope.includes`):

- Case registration and triage
- Investigation
- Resolution and outcome recording

**Out of scope** (each concern owned by the named neighbour):

- Applications (Apply to Decide)
- Enforcement referrals

## 5. Value stages

Intake to Resolution decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Register Case

Register and triage the case.

| Aspect | Value |
|---|---|
| Entry criterion | A case is reported. |
| Exit criterion | The case is registered and triaged. |
| Outcome | A triaged case. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Investigate

Investigate the case.

| Aspect | Value |
|---|---|
| Entry criterion | The case is triaged. |
| Exit criterion | The investigation is complete. |
| Outcome | A completed investigation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Resolve

Resolve the case and record the outcome.

| Aspect | Value |
|---|---|
| Entry criterion | The investigation is complete. |
| Exit criterion | The case is resolved with recorded outcome. |
| Outcome | A resolved case. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-zwaes5`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Case resolution cycle time** (stream-level) — Elapsed time from intake to resolution.

## 9. Evidence and admission

**Evidence sources:** SRC-014 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-074) from the CR-VS-11 industry evidence register extension. Industry-specific chain (public-sector); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
