# Plan to Forecast

Admitted Value Stream record (`value-streams:value-stream-plan-to-forecast-89vb4q`, v1.2.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-plan-to-forecast-89vb4q` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.2.0 · active |
| Metamodel pin | 1.0.0 |
| Record | [`value-streams-value-stream-plan-to-forecast-89vb4q.yaml`](./value-streams-value-stream-plan-to-forecast-89vb4q.yaml) — authoritative |

## 2. Definition

> The end-to-end stream from opening of a planning cycle through ratification of a committed forecast or budget.

## 3. Value proposition and served party

**Outcome:** A ratified plan guiding enterprise resource allocation.

## 4. Stream boundary

**Entry criterion:** A planning cycle opens.

**Exit criterion:** A committed forecast or budget is ratified.

**In scope** (from the record's `scope.includes`):

- Planning-cycle opening
- Target and plan formation
- Commitment negotiation
- Forecast or budget ratification

**Out of scope** (each concern owned by the named neighbour):

- Backward-looking attestation (Record to Report)
- Delivery execution (Plan to Deliver)
- Strategic direction setting itself (Strategy Formulation capability, upstream)

## 5. Value stages

Plan to Forecast decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Open Planning Cycle

Open the planning cycle and frame its scope.

| Aspect | Value |
|---|---|
| Entry criterion | A planning cycle opens. |
| Exit criterion | The cycle is framed and resourced. |
| Outcome | An open, framed planning cycle. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-strategic-planning-k3rz7a`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-operate-53y4j4` |

### Stage 2: Form Plan

Develop objectives, targets, and the draft plan.

| Aspect | Value |
|---|---|
| Entry criterion | The cycle is framed. |
| Exit criterion | A complete draft plan exists. |
| Outcome | A complete draft plan. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-strategic-planning-k3rz7a`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-design-vdwkmh`, `processes:process-fa-conceive-4uqqvg` |

### Stage 3: Negotiate Commitment

Negotiate resource allocation and commitments.

| Aspect | Value |
|---|---|
| Entry criterion | A draft plan exists. |
| Exit criterion | Commitments are agreed across the enterprise. |
| Outcome | Agreed commitments. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-performance-management-5fxren`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-sd-operate-u6xgu5` |

### Stage 4: Ratify Forecast

Ratify the committed forecast or budget.

| Aspect | Value |
|---|---|
| Entry criterion | Commitments are agreed. |
| Exit criterion | A committed forecast or budget is ratified. |
| Outcome | A ratified plan guiding allocation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-performance-management-5fxren`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-sd-build-2pkz5n` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-strategic-planning-k3rz7a`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-operate-53y4j4`
- `processes:process-sd-design-vdwkmh`
- `processes:process-fa-conceive-4uqqvg`
- `processes:process-sd-operate-u6xgu5`
- `processes:process-sd-build-2pkz5n`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-plan-to-deliver` — The ratified plan drives demand and delivery planning.
- `value-streams:value-value-stream-record-to-report` — Plan commitments are later attested against in reporting.

## 8. Measurement

- **Forecast accuracy** (stage: Ratify Forecast) — Deviation of committed forecast from actuals in the period. → [`dea:metric-cash-forecast-accuracy`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Planning cycle length** (stage: Ratify Forecast) — Elapsed time from cycle open to ratification.

## 9. Evidence and admission

**Evidence sources:** SRC-002, SRC-003, SRC-006 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted from candidate VSC-008 under CR-VS-04 (evidence raised E2 -> E3 via register v0.2 extension; distinctness closed per CR-VS-02). Enterprise-internal planning chain; served party is the enterprise itself as governance stakeholder (SRC-003 stakeholder-value observation). Boundary vs. Record to Report: forward-looking commitment vs. backward-looking attestation (CR-VS-02 RES-002).

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.1 (CR-VS-01, PR #3) |
| candidate | 2026-10-27 | Emmanuel A. Otchere, evidence raised E2 -> E3 (CR-VS-04, register v0.2) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-04 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-08 metric backfill (metric_ref links to dea-catalog-metrics) |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
