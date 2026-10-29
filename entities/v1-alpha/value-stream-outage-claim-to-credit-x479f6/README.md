# Outage Claim to Credit

Admitted Value Stream record (`value-streams:value-stream-outage-claim-to-credit-x479f6`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-outage-claim-to-credit-x479f6` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | utilities-energy · industry-specific |
| Record | [`value-streams-value-stream-outage-claim-to-credit-x479f6.yaml`](./value-streams-value-stream-outage-claim-to-credit-x479f6.yaml) — authoritative |

## 2. Definition

> The regulatory compensation stream from a customer's outage-compensation claim through validation to issued credit.

## 3. Value proposition and served party

**Outcome:** Regulation-compliant compensation credits issued for qualifying outages.

## 4. Stream boundary

**Entry criterion:** A customer claims outage compensation.

**Exit criterion:** The qualifying credit is issued to the bill.

**In scope** (from the record's `scope.includes`):

- Claim validation against outage records
- Credit calculation
- Issuance to the bill

**Out of scope** (each concern owned by the named neighbour):

- Supply restoration (Outage to Restore)
- General billing inquiries (Meter to Bill)

## 5. Value stages

Outage Claim to Credit decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Validate Claim

Validate the claim against outage records.

| Aspect | Value |
|---|---|
| Entry criterion | A claim is received. |
| Exit criterion | The claim is validated. |
| Outcome | A validated claim. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Calculate Credit

Calculate the compensation credit.

| Aspect | Value |
|---|---|
| Entry criterion | The claim is validated. |
| Exit criterion | The credit is calculated. |
| Outcome | A calculated credit. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c`, `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### Stage 3: Issue Credit

Issue the credit to the customer's bill.

| Aspect | Value |
|---|---|
| Entry criterion | The credit is calculated. |
| Exit criterion | The credit is issued. |
| Outcome | An issued credit. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-regulation-management-gya4d8`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Compensation claim cycle time** (stream-level) — Elapsed days from claim to issued credit.

## 9. Evidence and admission

**Evidence sources:** SRC-011 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-046) from the CR-VS-11 industry evidence register extension. Industry-specific chain (utilities-energy); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
