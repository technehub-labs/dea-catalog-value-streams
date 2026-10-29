# Supplier Reconciliation

Admitted Value Stream record (`value-streams:value-stream-supplier-reconciliation-y49qc3`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-supplier-reconciliation-y49qc3` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | retail-commerce · industry-specific |
| Record | [`value-streams-value-stream-supplier-reconciliation-y49qc3.yaml`](./value-streams-value-stream-supplier-reconciliation-y49qc3.yaml) — authoritative |

## 2. Definition

> The trade-payables reconciliation stream from supplier invoice matching through dispute resolution to reconciled settlement.

## 3. Value proposition and served party

**Outcome:** Reconciled supplier settlements for the trading period.

## 4. Stream boundary

**Entry criterion:** Supplier invoices and delivery records exist for the period.

**Exit criterion:** All supplier accounts are reconciled and settled.

**In scope** (from the record's `scope.includes`):

- Invoice matching
- Dispute resolution
- Settlement and reconciliation

**Out of scope** (each concern owned by the named neighbour):

- General procurement (Procure to Pay)
- Retail buying (Assortment to Shelf)

## 5. Value stages

Supplier Reconciliation decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Match Invoices

Match supplier invoices to receipts and contracts.

| Aspect | Value |
|---|---|
| Entry criterion | Period invoices exist. |
| Exit criterion | Invoices are matched. |
| Outcome | Matched invoices. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-wkqaqp` |

### Stage 2: Resolve Disputes

Resolve matching disputes with suppliers.

| Aspect | Value |
|---|---|
| Entry criterion | Invoices are matched. |
| Exit criterion | Disputes are resolved. |
| Outcome | Resolved disputes. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-supplier-management-d6fuj4`, `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 3: Settle and Reconcile

Settle and reconcile supplier accounts.

| Aspect | Value |
|---|---|
| Entry criterion | Disputes are resolved. |
| Exit criterion | Accounts are reconciled. |
| Outcome | Reconciled accounts. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-fa-operate-wkqaqp`, `processes:process-fa-operate-4xn4d6` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-supplier-management-d6fuj4`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-wkqaqp`
- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-4xn4d6`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **First-time match rate** (stage: Match Invoices) — Share of supplier invoices matched without dispute. → [`dea:metric-first-time-match-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-013 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-060) from the CR-VS-11 industry evidence register extension. Industry-specific chain (retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
