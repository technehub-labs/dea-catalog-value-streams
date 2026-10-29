---
documentation_generated_from: value-streams-value-stream-plan-to-forecast-89vb4q.yaml
id: value-streams:value-stream-plan-to-forecast-89vb4q
name: Plan to Forecast
type: ValueStream
version: 1.3.0
lifecycle_status: active
value_stream_category: governance
industries:
- cross-industry
specificity: generic
entry_criterion: A planning cycle opens.
exit_criterion: A committed forecast or budget is ratified.
outcome: A ratified plan guiding enterprise resource allocation.
stages:
- Open Planning Cycle
- Form Plan
- Negotiate Commitment
- Ratify Forecast
capabilities:
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-enterprise-performance-management-5fxren
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-strategic-planning-k3rz7a
processes:
- processes:process-fa-conceive-4uqqvg
- processes:process-sd-build-2pkz5n
- processes:process-sd-design-vdwkmh
- processes:process-sd-operate-53y4j4
- processes:process-sd-operate-u6xgu5
metrics:
- Forecast accuracy
- Planning cycle length
upstream: []
downstream:
- value-stream-plan-to-deliver
- value-stream-record-to-report
evidence_sources:
- SRC-002
- SRC-003
- SRC-006
---

# Plan to Forecast

`value-streams:value-stream-plan-to-forecast-89vb4q` · **governance** · cross-industry · generic

> The end-to-end stream from opening of a planning cycle through ratification of a committed forecast or budget.

**Outcome:** A ratified plan guiding enterprise resource allocation.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-plan-to-forecast-89vb4q.yaml`](./value-streams-value-stream-plan-to-forecast-89vb4q.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Open Planning Cycle"]
  S2["2. Form Plan"]
  S3["3. Negotiate Commitment"]
  S4["4. Ratify Forecast"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Open Planning Cycle** | A planning cycle opens. | The cycle is framed and resourced. | 2 | 1 | no |
| 2 | **Form Plan** | The cycle is framed. | A complete draft plan exists. | 2 | 2 | no |
| 3 | **Negotiate Commitment** | A draft plan exists. | Commitments are agreed across the enterprise. | 2 | 1 | no |
| 4 | **Ratify Forecast** | Commitments are agreed. | A committed forecast or budget is ratified. | 2 | 1 | no |

### 1. Open Planning Cycle

Open the planning cycle and frame its scope.

| Aspect | Value |
|---|---|
| Entry criterion | A planning cycle opens. |
| Exit criterion | The cycle is framed and resourced. |
| Outcome | An open, framed planning cycle. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-strategic-planning-k3rz7a` · `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-operate-53y4j4` |

### 2. Form Plan

Develop objectives, targets, and the draft plan.

| Aspect | Value |
|---|---|
| Entry criterion | The cycle is framed. |
| Exit criterion | A complete draft plan exists. |
| Outcome | A complete draft plan. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-strategic-planning-k3rz7a` · `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-design-vdwkmh` · `processes:process-fa-conceive-4uqqvg` |

### 3. Negotiate Commitment

Negotiate resource allocation and commitments.

| Aspect | Value |
|---|---|
| Entry criterion | A draft plan exists. |
| Exit criterion | Commitments are agreed across the enterprise. |
| Outcome | Agreed commitments. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-performance-management-5fxren` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-sd-operate-u6xgu5` |

### 4. Ratify Forecast

Ratify the committed forecast or budget.

| Aspect | Value |
|---|---|
| Entry criterion | Commitments are agreed. |
| Exit criterion | A committed forecast or budget is ratified. |
| Outcome | A ratified plan guiding allocation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-performance-management-5fxren` · `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-sd-build-2pkz5n` |

## Scope boundary

**Entry:** A planning cycle opens.

**Exit:** A committed forecast or budget is ratified.

**In scope**

- Planning-cycle opening
- Target and plan formation
- Commitment negotiation
- Forecast or budget ratification

**Out of scope** (owned by the named neighbour)

- Backward-looking attestation (Record to Report)
- Delivery execution (Plan to Deliver)
- Strategic direction setting itself (Strategy Formulation capability, upstream)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-strategic-planning-k3rz7a`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-operate-53y4j4`
- `processes:process-sd-design-vdwkmh`
- `processes:process-fa-conceive-4uqqvg`
- `processes:process-sd-operate-u6xgu5`
- `processes:process-sd-build-2pkz5n`

## Cross-stream links

**Upstream:** none recorded.

**Downstream** (this stream's exit feeds their entry):

- [plan to deliver](../value-stream-plan-to-deliver-smmwpx/README.md) — The ratified plan drives demand and delivery planning.
- [record to report](../value-stream-record-to-report-zw9z2r/README.md) — Plan commitments are later attested against in reporting.

## Measurement

- **Forecast accuracy** (stage: Ratify Forecast) — Deviation of committed forecast from actuals in the period. → [`dea:metric-cash-forecast-accuracy`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Planning cycle length** (stage: Ratify Forecast) — Elapsed time from cycle open to ratification.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-002 | cross-industry-process | APQC Process Classification Framework (cross-industry, process-to-value-stream groupings) |
| SRC-003 | standards-body | OMG Business Architecture Core Metamodel (BACM) — ValueStream element |
| SRC-006 | commercial-process-models | Hammer & Hurdle-style enterprise process-chain literature (public summaries) |

**Rationale:** Admitted from candidate VSC-008 under CR-VS-04 (evidence raised E2 -> E3 via register v0.2 extension; distinctness closed per CR-VS-02). Enterprise-internal planning chain; served party is the enterprise itself as governance stakeholder (SRC-003 stakeholder-value observation). Boundary vs. Record to Report: forward-looking commitment vs. backward-looking attestation (CR-VS-02 RES-002).

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.1 (CR-VS-01, PR #3) |
| candidate | 2026-10-27 | Emmanuel A. Otchere, evidence raised E2 -> E3 (CR-VS-04, register v0.2) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-04 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-08 metric backfill (metric_ref links to dea-catalog-metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-11 applicability backfill (cross-industry, generic) |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
