# Emergency Alert to Response

Admitted Value Stream record (`value-streams:value-stream-emergency-alert-to-response-jtz6qn`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-emergency-alert-to-response-jtz6qn` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | public-sector · industry-specific |
| Record | [`value-streams-value-stream-emergency-alert-to-response-jtz6qn.yaml`](./value-streams-value-stream-emergency-alert-to-response-jtz6qn.yaml) — authoritative |

## 2. Definition

> The emergency stream from alert through dispatch to response completion and after-action review.

## 3. Value proposition and served party

**Outcome:** A responded emergency with completed after-action review.

## 4. Stream boundary

**Entry criterion:** An emergency alert is received.

**Exit criterion:** The response is complete and reviewed.

**In scope** (from the record's `scope.includes`):

- Alert and triage
- Dispatch
- Response execution
- After-action review

**Out of scope** (each concern owned by the named neighbour):

- Routine case handling (Intake to Resolution)
- Continuity management

## 5. Value stages

Emergency Alert to Response decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Alert and Triage

Receive and triage the alert.

| Aspect | Value |
|---|---|
| Entry criterion | An alert is received. |
| Exit criterion | The alert is triaged. |
| Outcome | A triaged alert. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 2: Dispatch

Dispatch the response.

| Aspect | Value |
|---|---|
| Entry criterion | The alert is triaged. |
| Exit criterion | The response is dispatched. |
| Outcome | A dispatched response. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-workforce-planning-b43rhm` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Respond

Execute the response.

| Aspect | Value |
|---|---|
| Entry criterion | The response is dispatched. |
| Exit criterion | The response is complete. |
| Outcome | A completed response. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 4: After-Action Review

Complete the after-action review.

| Aspect | Value |
|---|---|
| Entry criterion | The response is complete. |
| Exit criterion | The review is complete. |
| Outcome | A completed review. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-performance-management-5fxren`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-planning-b43rhm`
- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-eo-operate-2jnz85`
- `processes:process-ge-operate-zwaes5`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-outage-to-restore` — Utility restoration is its industry counterpart.

**Downstream streams:** none recorded.

## 8. Measurement

- **Alert-to-dispatch time** (stream-level) — Elapsed time from alert to dispatched response.

## 9. Evidence and admission

**Evidence sources:** SRC-014 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-079) from the CR-VS-11 industry evidence register extension. Industry-specific chain (public-sector); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
