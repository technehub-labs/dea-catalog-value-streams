---
documentation_generated_from: value-streams-value-stream-plan-to-deliver-smmwpx.yaml
id: value-streams:value-stream-plan-to-deliver-smmwpx
name: Plan to Deliver
type: ValueStream
version: 1.3.0
lifecycle_status: active
value_stream_category: operational
industries:
- cross-industry
specificity: generic
entry_criterion: Demand is forecast or an order backlog is planned.
exit_criterion: Product or service is delivered per the plan.
outcome: Delivered supply against planned demand.
stages:
- Plan Demand
- Schedule Production
- Produce
- Deliver
capabilities:
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-strategic-planning-k3rz7a
processes:
- processes:process-eo-operate-44jsrp
- processes:process-eo-operate-xud3hs
- processes:process-eo-operate-zh9m57
- processes:process-eo-operate-zwzmbd
- processes:process-fa-build-92v24c
- processes:process-sd-build-2pkz5n
metrics:
- Plan adherence
- Production schedule attainment
upstream:
- value-stream-plan-to-forecast
downstream:
- value-stream-order-to-cash
evidence_sources:
- SRC-002
---

# Plan to Deliver

`value-streams:value-stream-plan-to-deliver-smmwpx` · **operational** · cross-industry · generic

> The end-to-end stream from demand planning through production and delivery of products or services.

**Outcome:** Delivered supply against planned demand.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-plan-to-deliver-smmwpx.yaml`](./value-streams-value-stream-plan-to-deliver-smmwpx.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Plan Demand"]
  S2["2. Schedule Production"]
  S3["3. Produce"]
  S4["4. Deliver"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Plan Demand** | Demand is forecast or an order backlog exists. | A committed delivery plan exists. | 2 | 2 | no |
| 2 | **Schedule Production** | A committed delivery plan exists. | A production schedule is released. | 1 | 1 | no |
| 3 | **Produce** | A released schedule exists. | Products or services are produced per plan. | 1 | 2 | no |
| 4 | **Deliver** | Produced supply exists. | Product or service is delivered per the plan. | 1 | 2 | yes |

### 1. Plan Demand

Forecast demand or plan the order backlog.

| Aspect | Value |
|---|---|
| Entry criterion | Demand is forecast or an order backlog exists. |
| Exit criterion | A committed delivery plan exists. |
| Outcome | A committed delivery plan. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-strategic-planning-k3rz7a` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-sd-build-2pkz5n` · `processes:process-fa-build-92v24c` |

### 2. Schedule Production

Translate the plan into a production schedule.

| Aspect | Value |
|---|---|
| Entry criterion | A committed delivery plan exists. |
| Exit criterion | A production schedule is released. |
| Outcome | A released production schedule. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-xud3hs` |

### 3. Produce

Execute production against the schedule.

| Aspect | Value |
|---|---|
| Entry criterion | A released schedule exists. |
| Exit criterion | Products or services are produced per plan. |
| Outcome | Produced supply. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-xud3hs` · `processes:process-eo-operate-44jsrp` |

### 4. Deliver

Deliver the product or service per the plan.

| Aspect | Value |
|---|---|
| Entry criterion | Produced supply exists. |
| Exit criterion | Product or service is delivered per the plan. |
| Outcome | Delivered supply against planned demand. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` · `processes:process-eo-operate-zwzmbd` |

## Scope boundary

**Entry:** Demand is forecast or an order backlog is planned.

**Exit:** Product or service is delivered per the plan.

**In scope**

- Demand planning and backlog planning
- Production scheduling
- Production execution
- Delivery per plan

**Out of scope** (owned by the named neighbour)

- Payment recognition (Order to Cash exits at payment)
- Forecast ratification (Plan to Forecast exits at a ratified forecast)
- Supplier settlement (Procure to Pay)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-strategic-planning-k3rz7a`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-build-2pkz5n`
- `processes:process-fa-build-92v24c`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-zh9m57`
- `processes:process-eo-operate-zwzmbd`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [plan to forecast](../value-stream-plan-to-forecast-89vb4q/README.md) — A ratified forecast or plan is the input to demand planning.

**Downstream** (this stream's exit feeds their entry):

- [order to cash](../value-stream-order-to-cash-sc8gbu/README.md) — Delivered supply fulfills orders downstream.

## Measurement

- **Plan adherence** (stage: Deliver) — Share of deliveries made per plan (volume and date). → [`dea:metric-on-time-delivery-rate`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Production schedule attainment** (stage: Produce) — Share of scheduled production completed in period.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-002 | cross-industry-process | APQC Process Classification Framework (cross-industry, process-to-value-stream groupings) |

**Rationale:** Admitted from candidate VSC-005 under CR-VS-04 (evidence raised E2 -> E3 via register v0.2 extension; distinctness closed per CR-VS-02). Production chain (APQC plan-produce-deliver structure, SRC-002). Boundary vs. Order to Cash: fulfillment is shared vocabulary; this stream exits at delivery per plan, Order to Cash at payment recognition (CR-VS-02 boundary statement). Boundary vs. Plan to Forecast: the exit condition is the discriminator (delivery vs. ratified forecast).

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
