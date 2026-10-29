# Ship to Consignee

Admitted Value Stream record (`value-streams:value-stream-ship-to-consignee-nrx42x`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-ship-to-consignee-nrx42x` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | logistics-transportation · industry-specific |
| Record | [`value-streams-value-stream-ship-to-consignee-nrx42x.yaml`](./value-streams-value-stream-ship-to-consignee-nrx42x.yaml) — authoritative |

## 2. Definition

> The freight stream from shipper booking through pickup, linehaul, and delivery to consignee receipt.

## 3. Value proposition and served party

**Outcome:** Freight delivered with confirmed consignee receipt.

## 4. Stream boundary

**Entry criterion:** A shipper books the freight.

**Exit criterion:** The consignee confirms receipt.

**In scope** (from the record's `scope.includes`):

- Booking
- Pickup and linehaul
- Delivery
- Proof of delivery

**Out of scope** (each concern owned by the named neighbour):

- Customs clearance (Customs Clearance to Release)
- Warehousing (Warehouse Inbound to Bin)

## 5. Value stages

Ship to Consignee decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Book Freight

Book the freight movement.

| Aspect | Value |
|---|---|
| Entry criterion | A shipper books. |
| Exit criterion | The booking is confirmed. |
| Outcome | A confirmed booking. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Pick Up and Linehaul

Pick up and linehaul the freight.

| Aspect | Value |
|---|---|
| Entry criterion | The booking is confirmed. |
| Exit criterion | The freight arrives at destination. |
| Outcome | Arrived freight. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

### Stage 3: Deliver

Deliver to the consignee.

| Aspect | Value |
|---|---|
| Entry criterion | The freight arrives. |
| Exit criterion | The consignee receives. |
| Outcome | Received freight. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

### Stage 4: Confirm Proof

Confirm proof of delivery.

| Aspect | Value |
|---|---|
| Entry criterion | The consignee receives. |
| Exit criterion | Proof is recorded. |
| Outcome | Recorded proof. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-zh9m57`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-customs-clearance-to-release` — Cross-border freight clears customs en route.

**Downstream streams:** none recorded.

## 8. Measurement

- **On-time delivery rate (freight)** (stage: Deliver) — Share of freight delivered within the promised window. → [`dea:metric-on-time-delivery-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-066) from the CR-VS-11 industry evidence register extension. Industry-specific chain (logistics-transportation); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
