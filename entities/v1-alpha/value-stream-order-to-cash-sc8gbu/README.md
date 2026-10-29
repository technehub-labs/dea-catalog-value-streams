# Order to Cash

Admitted Value Stream record (`value-streams:value-stream-order-to-cash-sc8gbu`, v1.3.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-order-to-cash-sc8gbu` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.3.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | cross-industry · generic |
| Record | [`value-streams-value-stream-order-to-cash-sc8gbu.yaml`](./value-streams-value-stream-order-to-cash-sc8gbu.yaml) — authoritative |

## 2. Definition

> The end-to-end stream from demand generation through order capture, fulfillment, invoicing, and payment settlement.

## 3. Value proposition and served party

**Outcome:** Customer receives the fulfilled order and the enterprise recognizes payment against it.

## 4. Stream boundary

**Entry criterion:** A customer need converts to an order (request for goods or services); demand generation is the pre-order stage (CR-VS-02 RES-001).

**Exit criterion:** Payment is received and recorded against the order.

**In scope** (from the record's `scope.includes`):

- Demand generation as the pre-order stage (CR-VS-02 RES-001)
- Order capture and acceptance
- Fulfillment of goods and services
- Invoicing and payment settlement

**Out of scope** (each concern owned by the named neighbour):

- Post-sale relationship service (Contract to Renewal)
- Production planning (Plan to Deliver)
- Return flows (Return to Credit)

## 5. Value stages

Order to Cash decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Generate Demand

Qualify and nurture the customer need until it converts to an order request.

| Aspect | Value |
|---|---|
| Entry criterion | A customer need is identified as addressable. |
| Exit criterion | A customer need converts to an order request. |
| Outcome | A qualified order request in the hands of the enterprise. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-build-nygvw7` |

### Stage 2: Capture Order

Record, validate, and accept the customer order.

| Aspect | Value |
|---|---|
| Entry criterion | An order request exists. |
| Exit criterion | The order is accepted and confirmed to the customer. |
| Outcome | An accepted, bookable order. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 3: Fulfill Order

Source, assemble, and deliver the goods or services ordered.

| Aspect | Value |
|---|---|
| Entry criterion | An accepted order is booked. |
| Exit criterion | The customer receives the goods or services. |
| Outcome | A fulfilled order in the customer's hands. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-eo-operate-2jnz85`, `processes:process-eo-operate-zwzmbd`, `processes:process-eo-operate-zh9m57` |

### Stage 4: Invoice and Settle

Invoice the fulfilled order and recognize payment against it.

| Aspect | Value |
|---|---|
| Entry criterion | The order is fulfilled. |
| Exit criterion | Payment is received and recorded against the order. |
| Outcome | Recognized payment closing the value exchange. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp`, `processes:process-fa-operate-g9zpnq` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-build-nygvw7`
- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-zh9m57`
- `processes:process-fa-operate-sdppmp`
- `processes:process-fa-operate-g9zpnq`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-contract-to-renewal` — An executed order seeds the post-sale relationship.
- `value-streams:value-value-stream-return-to-credit` — A post-delivery defect or dissatisfaction triggers a return.

## 8. Measurement

- **Order-to-cash cycle time** (stage: Invoice and Settle) — Elapsed time from order acceptance to payment recognition; shorter is better.
- **Perfect order rate** (stage: Fulfill Order) — Share of orders delivered complete, on time, with accurate documentation. → [`dea:metric-perfect-order-rate`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Days sales outstanding** (stage: Invoice and Settle) — Average days from invoice to collected payment. → [`dea:metric-days-sales-outstanding`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-002, SRC-006 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted from candidate VSC-001 under CR-VS-03 (evidence at E3/high, distinctness closed per CR-VS-02). Absorbs VSC-007 (Lead to Cash) per CR-VS-02 RES-001. Boundary vs. VSC-005 (Plan to Deliver): fulfillment is shared vocabulary; this stream exits at payment recognition (CR-VS-02 boundary statement).

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.1 (CR-VS-01, PR #3) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-03 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-08 metric backfill (metric_ref links to dea-catalog-metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-11 applicability backfill (cross-industry, generic) |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
