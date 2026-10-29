---
documentation_generated_from: value-streams-value-stream-application-to-book-4yz2pa.yaml
id: value-streams:value-stream-application-to-book-4yz2pa
name: Application to Book
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- financial-services
specificity: industry-specific
entry_criterion: A loan application is submitted.
exit_criterion: The loan is booked and available to the customer.
outcome: An approved loan booked and available to the customer.
stages:
- Intake Application
- Assess Credit
- Decide and Disclose
- Book Loan
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-fa-operate-g9zpnq
- processes:process-ge-build-mctdgc
- processes:process-ge-operate-tpenm6
- processes:process-pr-operate-bbe384
metrics:
- Loan origination cycle time
- Loan application approval rate
upstream: []
downstream:
- value-stream-initiate-to-settle
evidence_sources:
- SRC-008
---

# Application to Book

`value-streams:value-stream-application-to-book-4yz2pa` · **operational** · financial-services · industry-specific

> The end-to-end lending stream from loan application through underwriting, approval decision, and booking of the loan.

**Outcome:** An approved loan booked and available to the customer.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-application-to-book-4yz2pa.yaml`](./value-streams-value-stream-application-to-book-4yz2pa.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Intake Application"]
  S2["2. Assess Credit"]
  S3["3. Decide and Disclose"]
  S4["4. Book Loan"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Intake Application** | An application is submitted. | The application is complete and screened. | 2 | 1 | yes |
| 2 | **Assess Credit** | The application is complete. | The credit assessment is complete. | 2 | 1 | no |
| 3 | **Decide and Disclose** | The assessment is complete. | The decision is communicated and terms accepted. | 2 | 1 | yes |
| 4 | **Book Loan** | Terms are accepted. | The loan is booked and funds available. | 2 | 1 | yes |

### 1. Intake Application

Receive and complete the loan application.

| Aspect | Value |
|---|---|
| Entry criterion | An application is submitted. |
| Exit criterion | The application is complete and screened. |
| Outcome | A complete, screened application. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Assess Credit

Assess creditworthiness and structure the offer.

| Aspect | Value |
|---|---|
| Entry criterion | The application is complete. |
| Exit criterion | The credit assessment is complete. |
| Outcome | A completed credit assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### 3. Decide and Disclose

Decide, price, and disclose terms to the customer.

| Aspect | Value |
|---|---|
| Entry criterion | The assessment is complete. |
| Exit criterion | The decision is communicated and terms accepted. |
| Outcome | An accepted loan offer. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` · `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### 4. Book Loan

Book the loan and make funds available.

| Aspect | Value |
|---|---|
| Entry criterion | Terms are accepted. |
| Exit criterion | The loan is booked and funds available. |
| Outcome | A booked, usable loan. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

## Scope boundary

**Entry:** A loan application is submitted.

**Exit:** The loan is booked and available to the customer.

**In scope**

- Application intake and completeness
- Credit assessment and underwriting
- Approval decision and disclosure
- Booking and funds availability

**Out of scope** (owned by the named neighbour)

- Deposit onboarding (Onboard to Activate)
- Collateral foreclosure

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-information-management-6vjgdh`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-build-mctdgc`
- `processes:process-fa-operate-g9zpnq`

## Cross-stream links

**Upstream:** none recorded.

**Downstream** (this stream's exit feeds their entry):

- [initiate to settle](../value-stream-initiate-to-settle-ken6np/README.md) — Loan drawdowns settle through payments.

## Measurement

- **Loan origination cycle time** (stage: Book Loan) — Elapsed time from application to booked loan. → [`dea:metric-loan-origination-cycle-time`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Loan application approval rate** (stage: Decide and Disclose) — Share of applications approved. → [`dea:metric-loan-application-approval-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-008 | industry-reference-model | Banking industry reference models (lending and payments chains, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-021) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
