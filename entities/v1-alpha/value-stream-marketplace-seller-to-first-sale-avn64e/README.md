---
documentation_generated_from: value-streams-value-stream-marketplace-seller-to-first-sale-avn64e.yaml
id: value-streams:value-stream-marketplace-seller-to-first-sale-avn64e
name: Marketplace Seller to First Sale
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- retail-commerce
specificity: industry-specific
entry_criterion: A seller applies to the marketplace.
exit_criterion: The seller's first sale completes.
outcome: A transacting marketplace seller.
stages:
- Verify Seller
- Set Up Listings
- Complete First Sale
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-offering-management-6egkc8
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-partner-management-cp3vdb
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-ge-operate-tpenm6
- processes:process-pr-operate-bbe384
- processes:process-pv-operate-cau4gv
metrics:
- Seller activation rate
upstream: []
downstream: []
evidence_sources:
- SRC-013
---

# Marketplace Seller to First Sale

`value-streams:value-stream-marketplace-seller-to-first-sale-avn64e` · **operational** · retail-commerce · industry-specific

> The marketplace stream from seller application through verification and listing to first completed sale.

**Outcome:** A transacting marketplace seller.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-marketplace-seller-to-first-sale-avn64e.yaml`](./value-streams-value-stream-marketplace-seller-to-first-sale-avn64e.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Verify Seller"]
  S2["2. Set Up Listings"]
  S3["3. Complete First Sale"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Verify Seller** | A seller applies. | The seller is verified. | 2 | 1 | yes |
| 2 | **Set Up Listings** | The seller is verified. | Listings are live. | 2 | 1 | yes |
| 3 | **Complete First Sale** | Listings are live. | The first sale completes. | 2 | 1 | yes |

### 1. Verify Seller

Verify the seller's identity and qualifications.

| Aspect | Value |
|---|---|
| Entry criterion | A seller applies. |
| Exit criterion | The seller is verified. |
| Outcome | A verified seller. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-partner-management-cp3vdb` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### 2. Set Up Listings

Set up catalog listings.

| Aspect | Value |
|---|---|
| Entry criterion | The seller is verified. |
| Exit criterion | Listings are live. |
| Outcome | Live listings. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-pv-operate-cau4gv` |

### 3. Complete First Sale

Support the seller to a completed first sale.

| Aspect | Value |
|---|---|
| Entry criterion | Listings are live. |
| Exit criterion | The first sale completes. |
| Outcome | A transacting seller. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## Scope boundary

**Entry:** A seller applies to the marketplace.

**Exit:** The seller's first sale completes.

**In scope**

- Seller verification
- Listing setup
- First transaction

**Out of scope** (owned by the named neighbour)

- Own-inventory retail (Checkout to Fulfillment)
- Payment processing

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-customer-management-f3n8wb`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-pv-operate-cau4gv`
- `processes:process-pr-operate-bbe384`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Seller activation rate** (stream-level) — Share of approved sellers reaching first sale.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-013 | industry-reference-model | Retail / consumer-commerce chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-064) from the CR-VS-11 industry evidence register extension. Industry-specific chain (retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
