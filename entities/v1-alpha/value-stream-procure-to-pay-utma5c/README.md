# Procure to Pay

Admitted Value Stream record (`value-streams:value-stream-procure-to-pay-utma5c`, v1.3.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-procure-to-pay-utma5c` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.3.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | cross-industry · generic |
| Record | [`value-streams-value-stream-procure-to-pay-utma5c.yaml`](./value-streams-value-stream-procure-to-pay-utma5c.yaml) — authoritative |

## 2. Definition

> The end-to-end stream from identification of an external supply need through sourcing, ordering, receipt, and supplier payment.

## 3. Value proposition and served party

**Outcome:** The internal need is met and the supplier obligation is settled.

## 4. Stream boundary

**Entry criterion:** An internal need for external supply is identified and a requisition is raised.

**Exit criterion:** The supplier is paid and the need is met.

**In scope** (from the record's `scope.includes`):

- Requisition of external supply
- Sourcing and supplier selection
- Purchase ordering and receipt
- Supplier invoice settlement

**Out of scope** (each concern owned by the named neighbour):

- Employee lifecycle settlement (Hire to Retire)
- Asset-lifecycle custody after receipt (Acquire to Retire)
- Demand-side flows (Order to Cash)

## 5. Value stages

Procure to Pay decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Requisition Need

Identify and approve the internal need for external supply.

| Aspect | Value |
|---|---|
| Entry criterion | An internal need for external supply is identified. |
| Exit criterion | An approved requisition exists. |
| Outcome | An approved, fundable requisition. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-sourcing-and-procurement-esucp4`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-eo-operate-vzcxx7` |

### Stage 2: Source Supplier

Select the supplier and agree commercial terms.

| Aspect | Value |
|---|---|
| Entry criterion | An approved requisition exists. |
| Exit criterion | A supplier and terms are selected. |
| Outcome | A sourced supply commitment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-sourcing-and-procurement-esucp4`, `capabilities:capability-supplier-management-d6fuj4` |
| Realizing processes | `processes:process-eo-operate-vzcxx7` |

### Stage 3: Order and Receive

Place the purchase order and receive the goods or services.

| Aspect | Value |
|---|---|
| Entry criterion | A sourcing decision exists. |
| Exit criterion | The goods or services are received and verified. |
| Outcome | Verified receipt against the order. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-sourcing-and-procurement-esucp4`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-vzcxx7`, `processes:process-eo-operate-zwzmbd` |

### Stage 4: Settle Supplier

Match, approve, and pay the supplier invoice.

| Aspect | Value |
|---|---|
| Entry criterion | A verified receipt exists. |
| Exit criterion | The supplier is paid and the need is met. |
| Outcome | A settled supplier obligation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-supplier-management-d6fuj4` |
| Realizing processes | `processes:process-fa-operate-wkqaqp`, `processes:process-fa-operate-g9zpnq` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-sourcing-and-procurement-esucp4`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-supplier-management-d6fuj4`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-vzcxx7`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-fa-operate-wkqaqp`
- `processes:process-fa-operate-g9zpnq`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-acquire-to-retire` — Received assets enter the asset lifecycle.

## 8. Measurement

- **Procure-to-pay cycle time** (stage: Settle Supplier) — Elapsed time from requisition approval to supplier payment. → [`dea:metric-invoice-processing-cycle-time`](https://github.com/technehub-labs/dea-catalog-metrics)
- **First-time match rate** (stage: Settle Supplier) — Share of supplier invoices matched to PO and receipt without exception. → [`dea:metric-first-time-match-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-002, SRC-006 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted from candidate VSC-002 under CR-VS-03 (evidence at E3/high, distinctness closed per CR-VS-02). Counterpart of Order to Cash on the supply side. Boundary vs. Hire to Retire: settlement is shared vocabulary; the counterparty (supplier vs. employee) is the discriminator (CR-VS-02 boundary statement).

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
