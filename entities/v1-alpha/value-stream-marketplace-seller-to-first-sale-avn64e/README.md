# Marketplace Seller to First Sale

Admitted Value Stream record (`value-streams:value-stream-marketplace-seller-to-first-sale-avn64e`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-marketplace-seller-to-first-sale-avn64e` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | retail-commerce · industry-specific |
| Record | [`value-streams-value-stream-marketplace-seller-to-first-sale-avn64e.yaml`](./value-streams-value-stream-marketplace-seller-to-first-sale-avn64e.yaml) — authoritative |

## 2. Definition

> The marketplace stream from seller application through verification and listing to first completed sale.

## 3. Value proposition and served party

**Outcome:** A transacting marketplace seller.

## 4. Stream boundary

**Entry criterion:** A seller applies to the marketplace.

**Exit criterion:** The seller's first sale completes.

**In scope** (from the record's `scope.includes`):

- Seller verification
- Listing setup
- First transaction

**Out of scope** (each concern owned by the named neighbour):

- Own-inventory retail (Checkout to Fulfillment)
- Payment processing

## 5. Value stages

Marketplace Seller to First Sale decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Verify Seller

Verify the seller's identity and qualifications.

| Aspect | Value |
|---|---|
| Entry criterion | A seller applies. |
| Exit criterion | The seller is verified. |
| Outcome | A verified seller. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-partner-management-cp3vdb` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 2: Set Up Listings

Set up catalog listings.

| Aspect | Value |
|---|---|
| Entry criterion | The seller is verified. |
| Exit criterion | Listings are live. |
| Outcome | Live listings. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-pv-operate-cau4gv` |

### Stage 3: Complete First Sale

Support the seller to a completed first sale.

| Aspect | Value |
|---|---|
| Entry criterion | Listings are live. |
| Exit criterion | The first sale completes. |
| Outcome | A transacting seller. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-customer-management-f3n8wb`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-pv-operate-cau4gv`
- `processes:process-pr-operate-bbe384`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Seller activation rate** (stream-level) — Share of approved sellers reaching first sale.

## 9. Evidence and admission

**Evidence sources:** SRC-013 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-064) from the CR-VS-11 industry evidence register extension. Industry-specific chain (retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
