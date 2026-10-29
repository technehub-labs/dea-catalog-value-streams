---
documentation_generated_from: value-streams-value-stream-ship-to-consignee-nrx42x.yaml
id: value-streams:value-stream-ship-to-consignee-nrx42x
name: Ship to Consignee
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- logistics-transportation
specificity: industry-specific
entry_criterion: A shipper books the freight.
exit_criterion: The consignee confirms receipt.
outcome: Freight delivered with confirmed consignee receipt.
stages:
- Book Freight
- Pick Up and Linehaul
- Deliver
- Confirm Proof
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
processes:
- processes:process-eo-operate-zh9m57
- processes:process-pr-operate-bbe384
metrics:
- On-time delivery rate (freight)
upstream:
- value-stream-customs-clearance-to-release
downstream: []
evidence_sources:
- SRC-016
---

# Ship to Consignee

`value-streams:value-stream-ship-to-consignee-nrx42x` · **operational** · logistics-transportation · industry-specific

> The freight stream from shipper booking through pickup, linehaul, and delivery to consignee receipt.

**Outcome:** Freight delivered with confirmed consignee receipt.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-ship-to-consignee-nrx42x.yaml`](./value-streams-value-stream-ship-to-consignee-nrx42x.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  TRIGGER(["⏺ Entry"])
  EXIT1(["✔ Exit"])
  S1["1. Book Freight<br/>The booking is confirmed"]
  S2["2. Pick Up and Linehaul<br/>The freight arrives at destination"]
  S3["3. Deliver<br/>The consignee receives"]
  S4["4. Confirm Proof<br/>Proof is recorded"]
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
| 1 | **Book Freight** | A shipper books. | The booking is confirmed. | 2 | 1 | yes |
| 2 | **Pick Up and Linehaul** | The booking is confirmed. | The freight arrives at destination. | 1 | 1 | no |
| 3 | **Deliver** | The freight arrives. | The consignee receives. | 1 | 1 | yes |
| 4 | **Confirm Proof** | The consignee receives. | Proof is recorded. | 1 | 1 | yes |

### 1. Book Freight

Book the freight movement.

| Aspect | Value |
|---|---|
| Entry criterion | A shipper books. |
| Exit criterion | The booking is confirmed. |
| Outcome | A confirmed booking. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Pick Up and Linehaul

Pick up and linehaul the freight.

| Aspect | Value |
|---|---|
| Entry criterion | The booking is confirmed. |
| Exit criterion | The freight arrives at destination. |
| Outcome | Arrived freight. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

### 3. Deliver

Deliver to the consignee.

| Aspect | Value |
|---|---|
| Entry criterion | The freight arrives. |
| Exit criterion | The consignee receives. |
| Outcome | Received freight. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

### 4. Confirm Proof

Confirm proof of delivery.

| Aspect | Value |
|---|---|
| Entry criterion | The consignee receives. |
| Exit criterion | Proof is recorded. |
| Outcome | Recorded proof. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## Scope boundary

**Entry:** A shipper books the freight.

**Exit:** The consignee confirms receipt.

**In scope**

- Booking
- Pickup and linehaul
- Delivery
- Proof of delivery

**Out of scope** (owned by the named neighbour)

- Customs clearance (Customs Clearance to Release)
- Warehousing (Warehouse Inbound to Bin)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-zh9m57`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [customs clearance to release](../value-stream-customs-clearance-to-release-cfgc3b/README.md) — Cross-border freight clears customs en route.

**Downstream:** none recorded.

## Measurement

- **On-time delivery rate (freight)** (stage: Deliver) — Share of freight delivered within the promised window. → [`dea:metric-on-time-delivery-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-016 | industry-reference-model | Manufacturing and logistics reference models (SCOR-style category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-066) from the CR-VS-11 industry evidence register extension. Industry-specific chain (logistics-transportation); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
