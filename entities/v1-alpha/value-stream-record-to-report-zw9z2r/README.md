# Record to Report

Admitted Value Stream record (`value-streams:value-stream-record-to-report-zw9z2r`, v1.1.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-record-to-report-zw9z2r` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.1.0 · active |
| Metamodel pin | 1.0.0 |
| Record | [`value-streams-value-stream-record-to-report-zw9z2r.yaml`](./value-streams-value-stream-record-to-report-zw9z2r.yaml) — authoritative |

## 2. Definition

> The end-to-end stream from recording of transactions through period close and attested financial reporting.

## 3. Value proposition and served party

**Outcome:** Attested financial visibility for stakeholders.

## 4. Stream boundary

**Entry criterion:** An accounting period opens or a transaction is recorded.

**Exit criterion:** Financial results are reported and attested.

**In scope** (from the record's `scope.includes`):

- Transaction recording
- Period close
- Attested financial reporting
- Disclosure and stakeholder visibility

**Out of scope** (each concern owned by the named neighbour):

- Forward-looking commitments (Plan to Forecast)
- Payment settlement flows (Order to Cash / Procure to Pay)
- Tax strategy design (Regulation Management capability)

## 5. Value stages

Record to Report decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Record Transactions

Record enterprise transactions in the ledger.

| Aspect | Value |
|---|---|
| Entry criterion | An accounting period opens or a transaction occurs. |
| Exit criterion | Transactions are recorded in the ledger. |
| Outcome | A complete transactional record. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### Stage 2: Close Period

Perform period close and reconciliation.

| Aspect | Value |
|---|---|
| Entry criterion | The period's transactions are recorded. |
| Exit criterion | The period is closed. |
| Outcome | A closed, reconciled period. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-fa-operate-4xn4d6` |

### Stage 3: Report

Compile and attest financial results.

| Aspect | Value |
|---|---|
| Entry criterion | A period is closed. |
| Exit criterion | Financial results are reported and attested. |
| Outcome | Attested financial results. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

### Stage 4: Disclose

Publish results to stakeholders.

| Aspect | Value |
|---|---|
| Entry criterion | Results are attested. |
| Exit criterion | Stakeholders have attested visibility. |
| Outcome | Attested financial visibility for stakeholders. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-fa-operate-8vqvkk`, `processes:process-fa-operate-ycba3k` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-4xn4d6`
- `processes:process-fa-operate-ycba3k`
- `processes:process-fa-operate-8vqvkk`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-plan-to-forecast` — Ratified plans are the commitments attested against.
- `value-streams:value-value-stream-order-to-cash` — Recognized payments are recorded as transactions.
- `value-streams:value-value-stream-procure-to-pay` — Supplier settlements are recorded as transactions.

**Downstream streams:** none recorded.

## 8. Measurement

- **Close cycle time** (stage: Close Period) — Elapsed days from period end to attested close.
- **Restatement rate** (stage: Report) — Count of restatements per reporting year; zero is the target.

## 9. Evidence and admission

**Evidence sources:** SRC-002, SRC-003, SRC-006 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted from candidate VSC-009 under CR-VS-04 (evidence raised E2 -> E3 via register v0.2 extension; distinctness closed per CR-VS-02). Finance reporting chain; served party is enterprise governance stakeholders (SRC-003). Boundary vs. Plan to Forecast: backward-looking attestation vs. forward-looking commitment (CR-VS-02 RES-002).

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.1 (CR-VS-01, PR #3) |
| candidate | 2026-10-27 | Emmanuel A. Otchere, evidence raised E2 -> E3 (CR-VS-04, register v0.2) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-04 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
