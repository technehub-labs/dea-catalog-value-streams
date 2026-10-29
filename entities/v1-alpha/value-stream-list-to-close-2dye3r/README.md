# List to Close

Admitted Value Stream record (`value-streams:value-stream-list-to-close-2dye3r`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-list-to-close-2dye3r` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | construction-real-estate · industry-specific |
| Record | [`value-streams-value-stream-list-to-close-2dye3r.yaml`](./value-streams-value-stream-list-to-close-2dye3r.yaml) — authoritative |

## 2. Definition

> The real-estate transaction stream from listing agreement through marketing and negotiation to closed sale.

## 3. Value proposition and served party

**Outcome:** A closed property sale with settled proceeds.

## 4. Stream boundary

**Entry criterion:** A listing agreement is signed.

**Exit criterion:** The sale closes with settled proceeds.

**In scope** (from the record's `scope.includes`):

- Listing preparation
- Marketing and viewings
- Offer negotiation
- Closing and settlement

**Out of scope** (each concern owned by the named neighbour):

- Property management (Lease Sign to Renewal)
- Financing (lending streams)

## 5. Value stages

List to Close decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Prepare Listing

Prepare and launch the listing.

| Aspect | Value |
|---|---|
| Entry criterion | A listing is signed. |
| Exit criterion | The listing is live. |
| Outcome | A live listing. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-build-nygvw7` |

### Stage 2: Market and Show

Market the property and conduct viewings.

| Aspect | Value |
|---|---|
| Entry criterion | The listing is live. |
| Exit criterion | Offers are received. |
| Outcome | Received offers. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 3: Negotiate Offer

Negotiate and accept the offer.

| Aspect | Value |
|---|---|
| Entry criterion | Offers are received. |
| Exit criterion | An offer is accepted. |
| Outcome | An accepted offer. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 4: Close and Settle

Close the sale and settle proceeds.

| Aspect | Value |
|---|---|
| Entry criterion | An offer is accepted. |
| Exit criterion | The sale closes with settled proceeds. |
| Outcome | A closed sale. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-build-nygvw7`
- `processes:process-pr-operate-bbe384`
- `processes:process-ge-build-mctdgc`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Days on market** (stream-level) — Elapsed days from listing to accepted offer.

## 9. Evidence and admission

**Evidence sources:** SRC-017 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-094) from the CR-VS-11 industry evidence register extension. Industry-specific chain (construction-real-estate); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
