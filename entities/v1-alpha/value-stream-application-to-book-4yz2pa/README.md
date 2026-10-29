# Application to Book

Admitted Value Stream record (`value-streams:value-stream-application-to-book-4yz2pa`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-application-to-book-4yz2pa` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | financial-services · industry-specific |
| Record | [`value-streams-value-stream-application-to-book-4yz2pa.yaml`](./value-streams-value-stream-application-to-book-4yz2pa.yaml) — authoritative |

## 2. Definition

> The end-to-end lending stream from loan application through underwriting, approval decision, and booking of the loan.

## 3. Value proposition and served party

**Outcome:** An approved loan booked and available to the customer.

## 4. Stream boundary

**Entry criterion:** A loan application is submitted.

**Exit criterion:** The loan is booked and available to the customer.

**In scope** (from the record's `scope.includes`):

- Application intake and completeness
- Credit assessment and underwriting
- Approval decision and disclosure
- Booking and funds availability

**Out of scope** (each concern owned by the named neighbour):

- Deposit onboarding (Onboard to Activate)
- Collateral foreclosure

## 5. Value stages

Application to Book decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Intake Application

Receive and complete the loan application.

| Aspect | Value |
|---|---|
| Entry criterion | An application is submitted. |
| Exit criterion | The application is complete and screened. |
| Outcome | A complete, screened application. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Assess Credit

Assess creditworthiness and structure the offer.

| Aspect | Value |
|---|---|
| Entry criterion | The application is complete. |
| Exit criterion | The credit assessment is complete. |
| Outcome | A completed credit assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 3: Decide and Disclose

Decide, price, and disclose terms to the customer.

| Aspect | Value |
|---|---|
| Entry criterion | The assessment is complete. |
| Exit criterion | The decision is communicated and terms accepted. |
| Outcome | An accepted loan offer. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c`, `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 4: Book Loan

Book the loan and make funds available.

| Aspect | Value |
|---|---|
| Entry criterion | Terms are accepted. |
| Exit criterion | The loan is booked and funds available. |
| Outcome | A booked, usable loan. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-build-mctdgc`
- `processes:process-fa-operate-g9zpnq`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-initiate-to-settle` — Loan drawdowns settle through payments.

## 8. Measurement

- **Loan origination cycle time** (stage: Book Loan) — Elapsed time from application to booked loan. → [`dea:metric-loan-origination-cycle-time`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Loan application approval rate** (stage: Decide and Disclose) — Share of applications approved. → [`dea:metric-loan-application-approval-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-008 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-021) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
