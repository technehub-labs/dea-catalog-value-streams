---
documentation_generated_from: value-streams-value-stream-list-to-close-2dye3r.yaml
id: value-streams:value-stream-list-to-close-2dye3r
name: List to Close
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- construction-real-estate
specificity: industry-specific
entry_criterion: A listing agreement is signed.
exit_criterion: The sale closes with settled proceeds.
outcome: A closed property sale with settled proceeds.
stages:
- Prepare Listing
- Market and Show
- Negotiate Offer
- Close and Settle
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-marketing-xmc539
processes:
- processes:process-fa-operate-sdppmp
- processes:process-ge-build-mctdgc
- processes:process-pr-build-nygvw7
- processes:process-pr-operate-bbe384
metrics:
- Days on market
upstream: []
downstream: []
evidence_sources:
- SRC-017
---

# List to Close

`value-streams:value-stream-list-to-close-2dye3r` · **operational** · construction-real-estate · industry-specific

> The real-estate transaction stream from listing agreement through marketing and negotiation to closed sale.

**Outcome:** A closed property sale with settled proceeds.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-list-to-close-2dye3r.yaml`](./value-streams-value-stream-list-to-close-2dye3r.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Prepare Listing"]
  S2["2. Market and Show"]
  S3["3. Negotiate Offer"]
  S4["4. Close and Settle"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Prepare Listing** | A listing is signed. | The listing is live. | 2 | 1 | yes |
| 2 | **Market and Show** | The listing is live. | Offers are received. | 2 | 1 | yes |
| 3 | **Negotiate Offer** | Offers are received. | An offer is accepted. | 2 | 1 | yes |
| 4 | **Close and Settle** | An offer is accepted. | The sale closes with settled proceeds. | 2 | 1 | yes |

### 1. Prepare Listing

Prepare and launch the listing.

| Aspect | Value |
|---|---|
| Entry criterion | A listing is signed. |
| Exit criterion | The listing is live. |
| Outcome | A live listing. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-build-nygvw7` |

### 2. Market and Show

Market the property and conduct viewings.

| Aspect | Value |
|---|---|
| Entry criterion | The listing is live. |
| Exit criterion | Offers are received. |
| Outcome | Received offers. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 3. Negotiate Offer

Negotiate and accept the offer.

| Aspect | Value |
|---|---|
| Entry criterion | Offers are received. |
| Exit criterion | An offer is accepted. |
| Outcome | An accepted offer. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### 4. Close and Settle

Close the sale and settle proceeds.

| Aspect | Value |
|---|---|
| Entry criterion | An offer is accepted. |
| Exit criterion | The sale closes with settled proceeds. |
| Outcome | A closed sale. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## Scope boundary

**Entry:** A listing agreement is signed.

**Exit:** The sale closes with settled proceeds.

**In scope**

- Listing preparation
- Marketing and viewings
- Offer negotiation
- Closing and settlement

**Out of scope** (owned by the named neighbour)

- Property management (Lease Sign to Renewal)
- Financing (lending streams)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-build-nygvw7`
- `processes:process-pr-operate-bbe384`
- `processes:process-ge-build-mctdgc`
- `processes:process-fa-operate-sdppmp`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Days on market** (stream-level) — Elapsed days from listing to accepted offer.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-017 | industry-reference-model | Construction and real-estate chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-094) from the CR-VS-11 industry evidence register extension. Industry-specific chain (construction-real-estate); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
