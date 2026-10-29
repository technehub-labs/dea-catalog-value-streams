# Checkout to Fulfillment

Admitted Value Stream record (`value-streams:value-stream-checkout-to-fulfillment-ngbewj`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-checkout-to-fulfillment-ngbewj` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | retail-commerce · industry-specific |
| Record | [`value-streams-value-stream-checkout-to-fulfillment-ngbewj.yaml`](./value-streams-value-stream-checkout-to-fulfillment-ngbewj.yaml) — authoritative |

## 2. Definition

> The omnichannel fulfilment stream from completed checkout through pick, pack, and dispatch to customer delivery.

## 3. Value proposition and served party

**Outcome:** A delivered order with proof of delivery.

## 4. Stream boundary

**Entry criterion:** A customer completes checkout.

**Exit criterion:** The order is delivered with proof.

**In scope** (from the record's `scope.includes`):

- Order validation and payment authorization
- Pick and pack
- Dispatch and last-mile delivery
- Proof of delivery

**Out of scope** (each concern owned by the named neighbour):

- Customer service (Issue to Resolve)
- Returns (Return to Credit)

## 5. Value stages

Checkout to Fulfillment decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Validate and Authorize

Validate the order and authorize payment.

| Aspect | Value |
|---|---|
| Entry criterion | Checkout completes. |
| Exit criterion | The order is valid and authorized. |
| Outcome | An authorized order. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Pick and Pack

Pick and pack the order.

| Aspect | Value |
|---|---|
| Entry criterion | The order is authorized. |
| Exit criterion | The order is packed. |
| Outcome | A packed order. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

### Stage 3: Deliver

Dispatch and deliver the order.

| Aspect | Value |
|---|---|
| Entry criterion | The order is packed. |
| Exit criterion | The order is delivered. |
| Outcome | A delivered order. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

### Stage 4: Confirm Proof

Confirm delivery with proof.

| Aspect | Value |
|---|---|
| Entry criterion | The order is delivered. |
| Exit criterion | Proof of delivery is recorded. |
| Outcome | Recorded proof. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-zh9m57`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-order-to-cash` — The retail specialization of the fulfilment-to-payment chain.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-return-to-credit` — Delivered orders can flow to returns.

## 8. Measurement

- **On-time delivery rate** (stage: Deliver) — Share of orders delivered within the promised window. → [`dea:metric-on-time-delivery-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-013 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-059) from the CR-VS-11 industry evidence register extension. Industry-specific chain (retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
