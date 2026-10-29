---
documentation_generated_from: value-streams-value-stream-checkout-to-fulfillment-ngbewj.yaml
id: value-streams:value-stream-checkout-to-fulfillment-ngbewj
name: Checkout to Fulfillment
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- retail-commerce
specificity: industry-specific
entry_criterion: A customer completes checkout.
exit_criterion: The order is delivered with proof.
outcome: A delivered order with proof of delivery.
stages:
- Validate and Authorize
- Pick and Pack
- Deliver
- Confirm Proof
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
processes:
- processes:process-eo-operate-zh9m57
- processes:process-eo-operate-zwzmbd
- processes:process-pr-operate-bbe384
metrics:
- On-time delivery rate
upstream:
- value-stream-order-to-cash
downstream:
- value-stream-return-to-credit
evidence_sources:
- SRC-013
---

# Checkout to Fulfillment

`value-streams:value-stream-checkout-to-fulfillment-ngbewj` · **operational** · retail-commerce · industry-specific

> The omnichannel fulfilment stream from completed checkout through pick, pack, and dispatch to customer delivery.

**Outcome:** A delivered order with proof of delivery.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-checkout-to-fulfillment-ngbewj.yaml`](./value-streams-value-stream-checkout-to-fulfillment-ngbewj.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  TRIGGER(["⏺ Entry"])
  EXIT1(["✔ Exit"])
  S1["1. Validate and Authorize<br/>The order is valid and authorized"]
  S2["2. Pick and Pack<br/>The order is packed"]
  S3["3. Deliver<br/>The order is delivered"]
  S4["4. Confirm Proof<br/>Proof of delivery is recorded"]
  TRIGGER --> S1
  S1 --> S2
  S2 --> S3
  S3 --> S4
  S4 --> EXIT1
  S4 -. re-engage .-> S1
  classDef terminal fill:#2C3E50,color:#fff,stroke:#1a252f,stroke-width:1px;
  classDef stage fill:#EAF2F8,color:#1a252f,stroke:#2C3E50,stroke-width:1px;
  class TRIGGER,EXIT1 terminal;
  class S1,S2,S3,S4 stage;
  style TRIGGER fill:#27AE60,color:#fff,stroke:#1e8449,stroke-width:1px;
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Validate and Authorize** | Checkout completes. | The order is valid and authorized. | 2 | 1 | yes |
| 2 | **Pick and Pack** | The order is authorized. | The order is packed. | 1 | 1 | no |
| 3 | **Deliver** | The order is packed. | The order is delivered. | 1 | 1 | yes |
| 4 | **Confirm Proof** | The order is delivered. | Proof of delivery is recorded. | 2 | 1 | yes |

### 1. Validate and Authorize

Validate the order and authorize payment.

| Aspect | Value |
|---|---|
| Entry criterion | Checkout completes. |
| Exit criterion | The order is valid and authorized. |
| Outcome | An authorized order. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Pick and Pack

Pick and pack the order.

| Aspect | Value |
|---|---|
| Entry criterion | The order is authorized. |
| Exit criterion | The order is packed. |
| Outcome | A packed order. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

### 3. Deliver

Dispatch and deliver the order.

| Aspect | Value |
|---|---|
| Entry criterion | The order is packed. |
| Exit criterion | The order is delivered. |
| Outcome | A delivered order. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

### 4. Confirm Proof

Confirm delivery with proof.

| Aspect | Value |
|---|---|
| Entry criterion | The order is delivered. |
| Exit criterion | Proof of delivery is recorded. |
| Outcome | Recorded proof. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## Scope boundary

**Entry:** A customer completes checkout.

**Exit:** The order is delivered with proof.

**In scope**

- Order validation and payment authorization
- Pick and pack
- Dispatch and last-mile delivery
- Proof of delivery

**Out of scope** (owned by the named neighbour)

- Customer service (Issue to Resolve)
- Returns (Return to Credit)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-zh9m57`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [order to cash](../value-stream-order-to-cash-sc8gbu/README.md) — The retail specialization of the fulfilment-to-payment chain.

**Downstream** (this stream's exit feeds their entry):

- [return to credit](../value-stream-return-to-credit-qan2dn/README.md) — Delivered orders can flow to returns.

## Measurement

- **On-time delivery rate** (stage: Deliver) — Share of orders delivered within the promised window. → [`dea:metric-on-time-delivery-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-013 | industry-reference-model | Retail / consumer-commerce chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-059) from the CR-VS-11 industry evidence register extension. Industry-specific chain (retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
