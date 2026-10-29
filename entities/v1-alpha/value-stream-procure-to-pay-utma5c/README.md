---
documentation_generated_from: value-streams-value-stream-procure-to-pay-utma5c.yaml
id: value-streams:value-stream-procure-to-pay-utma5c
name: Procure to Pay
type: ValueStream
version: 1.3.0
lifecycle_status: active
value_stream_category: operational
industries:
- cross-industry
specificity: generic
entry_criterion: An internal need for external supply is identified and a requisition is raised.
exit_criterion: The supplier is paid and the need is met.
outcome: The internal need is met and the supplier obligation is settled.
stages:
- Requisition Need
- Source Supplier
- Order and Receive
- Settle Supplier
capabilities:
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-sourcing-and-procurement-esucp4
- capabilities:capability-supplier-management-d6fuj4
processes:
- processes:process-eo-operate-vzcxx7
- processes:process-eo-operate-zwzmbd
- processes:process-fa-operate-g9zpnq
- processes:process-fa-operate-wkqaqp
metrics:
- Procure-to-pay cycle time
- First-time match rate
upstream: []
downstream:
- value-stream-acquire-to-retire
evidence_sources:
- SRC-002
- SRC-006
---

# Procure to Pay

`value-streams:value-stream-procure-to-pay-utma5c` · **operational** · cross-industry · generic

> The end-to-end stream from identification of an external supply need through sourcing, ordering, receipt, and supplier payment.

**Outcome:** The internal need is met and the supplier obligation is settled.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-procure-to-pay-utma5c.yaml`](./value-streams-value-stream-procure-to-pay-utma5c.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Requisition Need"]
  S2["2. Source Supplier"]
  S3["3. Order and Receive"]
  S4["4. Settle Supplier"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Requisition Need** | An internal need for external supply is identified. | An approved requisition exists. | 2 | 1 | no |
| 2 | **Source Supplier** | An approved requisition exists. | A supplier and terms are selected. | 2 | 1 | no |
| 3 | **Order and Receive** | A sourcing decision exists. | The goods or services are received and verified. | 2 | 2 | no |
| 4 | **Settle Supplier** | A verified receipt exists. | The supplier is paid and the need is met. | 2 | 2 | no |

### 1. Requisition Need

Identify and approve the internal need for external supply.

| Aspect | Value |
|---|---|
| Entry criterion | An internal need for external supply is identified. |
| Exit criterion | An approved requisition exists. |
| Outcome | An approved, fundable requisition. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-sourcing-and-procurement-esucp4` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-eo-operate-vzcxx7` |

### 2. Source Supplier

Select the supplier and agree commercial terms.

| Aspect | Value |
|---|---|
| Entry criterion | An approved requisition exists. |
| Exit criterion | A supplier and terms are selected. |
| Outcome | A sourced supply commitment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-sourcing-and-procurement-esucp4` · `capabilities:capability-supplier-management-d6fuj4` |
| Realizing processes | `processes:process-eo-operate-vzcxx7` |

### 3. Order and Receive

Place the purchase order and receive the goods or services.

| Aspect | Value |
|---|---|
| Entry criterion | A sourcing decision exists. |
| Exit criterion | The goods or services are received and verified. |
| Outcome | Verified receipt against the order. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-sourcing-and-procurement-esucp4` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-vzcxx7` · `processes:process-eo-operate-zwzmbd` |

### 4. Settle Supplier

Match, approve, and pay the supplier invoice.

| Aspect | Value |
|---|---|
| Entry criterion | A verified receipt exists. |
| Exit criterion | The supplier is paid and the need is met. |
| Outcome | A settled supplier obligation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` · `capabilities:capability-supplier-management-d6fuj4` |
| Realizing processes | `processes:process-fa-operate-wkqaqp` · `processes:process-fa-operate-g9zpnq` |

## Scope boundary

**Entry:** An internal need for external supply is identified and a requisition is raised.

**Exit:** The supplier is paid and the need is met.

**In scope**

- Requisition of external supply
- Sourcing and supplier selection
- Purchase ordering and receipt
- Supplier invoice settlement

**Out of scope** (owned by the named neighbour)

- Employee lifecycle settlement (Hire to Retire)
- Asset-lifecycle custody after receipt (Acquire to Retire)
- Demand-side flows (Order to Cash)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-sourcing-and-procurement-esucp4`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-supplier-management-d6fuj4`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-vzcxx7`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-fa-operate-wkqaqp`
- `processes:process-fa-operate-g9zpnq`

## Cross-stream links

**Upstream:** none recorded.

**Downstream** (this stream's exit feeds their entry):

- [acquire to retire](../value-stream-acquire-to-retire-g5x89g/README.md) — Received assets enter the asset lifecycle.

## Measurement

- **Procure-to-pay cycle time** (stage: Settle Supplier) — Elapsed time from requisition approval to supplier payment. → [`dea:metric-invoice-processing-cycle-time`](https://github.com/technehub-labs/dea-catalog-metrics)
- **First-time match rate** (stage: Settle Supplier) — Share of supplier invoices matched to PO and receipt without exception. → [`dea:metric-first-time-match-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-002 | cross-industry-process | APQC Process Classification Framework (cross-industry, process-to-value-stream groupings) |
| SRC-006 | commercial-process-models | Hammer & Hurdle-style enterprise process-chain literature (public summaries) |

**Rationale:** Admitted from candidate VSC-002 under CR-VS-03 (evidence at E3/high, distinctness closed per CR-VS-02). Counterpart of Order to Cash on the supply side. Boundary vs. Hire to Retire: settlement is shared vocabulary; the counterparty (supplier vs. employee) is the discriminator (CR-VS-02 boundary statement).

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.1 (CR-VS-01, PR #3) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-03 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-08 metric backfill (metric_ref links to dea-catalog-metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-11 applicability backfill (cross-industry, generic) |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
