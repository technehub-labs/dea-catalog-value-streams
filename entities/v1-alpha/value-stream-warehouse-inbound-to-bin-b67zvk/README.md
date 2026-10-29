# Warehouse Inbound to Bin

Admitted Value Stream record (`value-streams:value-stream-warehouse-inbound-to-bin-b67zvk`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-warehouse-inbound-to-bin-b67zvk` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | logistics-transportation · industry-specific |
| Record | [`value-streams-value-stream-warehouse-inbound-to-bin-b67zvk.yaml`](./value-streams-value-stream-warehouse-inbound-to-bin-b67zvk.yaml) — authoritative |

## 2. Definition

> The warehousing stream from carrier arrival through receiving and putaway to bin-confirmed stock.

## 3. Value proposition and served party

**Outcome:** Bin-confirmed, system-visible received stock.

## 4. Stream boundary

**Entry criterion:** A carrier arrives with inbound freight.

**Exit criterion:** Stock is confirmed in its bin locations.

**In scope** (from the record's `scope.includes`):

- Receiving
- Quality and quantity check
- Putaway and bin confirmation

**Out of scope** (each concern owned by the named neighbour):

- Freight (Ship to Consignee)
- Order fulfilment pick (Checkout to Fulfillment)

## 5. Value stages

Warehouse Inbound to Bin decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Receive

Receive the inbound freight.

| Aspect | Value |
|---|---|
| Entry criterion | A carrier arrives. |
| Exit criterion | The freight is received. |
| Outcome | Received freight. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

### Stage 2: Check

Check quantity and condition.

| Aspect | Value |
|---|---|
| Entry criterion | The freight is received. |
| Exit criterion | The check is complete. |
| Outcome | Checked stock. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 3: Put Away

Put away and confirm bin locations.

| Aspect | Value |
|---|---|
| Entry criterion | The check is complete. |
| Exit criterion | Stock is bin-confirmed. |
| Outcome | Bin-confirmed stock. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-44jsrp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Dock-to-stock time** (stream-level) — Elapsed hours from arrival to bin-confirmed stock.

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-068) from the CR-VS-11 industry evidence register extension. Industry-specific chain (logistics-transportation); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
