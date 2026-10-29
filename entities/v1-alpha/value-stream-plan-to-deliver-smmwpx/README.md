# Plan to Deliver

Admitted Value Stream record (`value-streams:value-stream-plan-to-deliver-smmwpx`, v1.3.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-plan-to-deliver-smmwpx` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.3.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | cross-industry · generic |
| Record | [`value-streams-value-stream-plan-to-deliver-smmwpx.yaml`](./value-streams-value-stream-plan-to-deliver-smmwpx.yaml) — authoritative |

## 2. Definition

> The end-to-end stream from demand planning through production and delivery of products or services.

## 3. Value proposition and served party

**Outcome:** Delivered supply against planned demand.

## 4. Stream boundary

**Entry criterion:** Demand is forecast or an order backlog is planned.

**Exit criterion:** Product or service is delivered per the plan.

**In scope** (from the record's `scope.includes`):

- Demand planning and backlog planning
- Production scheduling
- Production execution
- Delivery per plan

**Out of scope** (each concern owned by the named neighbour):

- Payment recognition (Order to Cash exits at payment)
- Forecast ratification (Plan to Forecast exits at a ratified forecast)
- Supplier settlement (Procure to Pay)

## 5. Value stages

Plan to Deliver decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Plan Demand

Forecast demand or plan the order backlog.

| Aspect | Value |
|---|---|
| Entry criterion | Demand is forecast or an order backlog exists. |
| Exit criterion | A committed delivery plan exists. |
| Outcome | A committed delivery plan. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-strategic-planning-k3rz7a`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-sd-build-2pkz5n`, `processes:process-fa-build-92v24c` |

### Stage 2: Schedule Production

Translate the plan into a production schedule.

| Aspect | Value |
|---|---|
| Entry criterion | A committed delivery plan exists. |
| Exit criterion | A production schedule is released. |
| Outcome | A released production schedule. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-xud3hs` |

### Stage 3: Produce

Execute production against the schedule.

| Aspect | Value |
|---|---|
| Entry criterion | A released schedule exists. |
| Exit criterion | Products or services are produced per plan. |
| Outcome | Produced supply. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-xud3hs`, `processes:process-eo-operate-44jsrp` |

### Stage 4: Deliver

Deliver the product or service per the plan.

| Aspect | Value |
|---|---|
| Entry criterion | Produced supply exists. |
| Exit criterion | Product or service is delivered per the plan. |
| Outcome | Delivered supply against planned demand. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57`, `processes:process-eo-operate-zwzmbd` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-strategic-planning-k3rz7a`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-build-2pkz5n`
- `processes:process-fa-build-92v24c`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-zh9m57`
- `processes:process-eo-operate-zwzmbd`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-plan-to-forecast` — A ratified forecast or plan is the input to demand planning.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-order-to-cash` — Delivered supply fulfills orders downstream.

## 8. Measurement

- **Plan adherence** (stage: Deliver) — Share of deliveries made per plan (volume and date). → [`dea:metric-on-time-delivery-rate`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Production schedule attainment** (stage: Produce) — Share of scheduled production completed in period.

## 9. Evidence and admission

**Evidence sources:** SRC-002 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted from candidate VSC-005 under CR-VS-04 (evidence raised E2 -> E3 via register v0.2 extension; distinctness closed per CR-VS-02). Production chain (APQC plan-produce-deliver structure, SRC-002). Boundary vs. Order to Cash: fulfillment is shared vocabulary; this stream exits at delivery per plan, Order to Cash at payment recognition (CR-VS-02 boundary statement). Boundary vs. Plan to Forecast: the exit condition is the discriminator (delivery vs. ratified forecast).

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.1 (CR-VS-01, PR #3) |
| candidate | 2026-10-27 | Emmanuel A. Otchere, evidence raised E2 -> E3 (CR-VS-04, register v0.2) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-04 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-08 metric backfill (metric_ref links to dea-catalog-metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-11 applicability backfill (cross-industry, generic) |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
