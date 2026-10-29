# Quote to Bind

Admitted Value Stream record (`value-streams:value-stream-quote-to-bind-szgnjc`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-quote-to-bind-szgnjc` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | insurance · industry-specific |
| Record | [`value-streams-value-stream-quote-to-bind-szgnjc.yaml`](./value-streams-value-stream-quote-to-bind-szgnjc.yaml) — authoritative |

## 2. Definition

> The end-to-end underwriting stream from submission through risk assessment, quote, and bound policy.

## 3. Value proposition and served party

**Outcome:** A bound policy for the accepted risk.

## 4. Stream boundary

**Entry criterion:** A quote request or submission is received.

**Exit criterion:** The policy is bound and documented.

**In scope** (from the record's `scope.includes`):

- Submission intake
- Risk assessment and underwriting
- Quotation and negotiation
- Binding and documentation

**Out of scope** (each concern owned by the named neighbour):

- Claims (Loss to Claim Settlement)
- Policy servicing (Policy to Endorsement)

## 5. Value stages

Quote to Bind decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Intake Submission

Receive and complete the submission.

| Aspect | Value |
|---|---|
| Entry criterion | A submission is received. |
| Exit criterion | The submission is complete. |
| Outcome | A complete submission. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Assess Risk

Assess the risk and determine terms.

| Aspect | Value |
|---|---|
| Entry criterion | The submission is complete. |
| Exit criterion | The risk assessment is complete. |
| Outcome | A completed risk assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 3: Quote

Quote terms to the customer and negotiate.

| Aspect | Value |
|---|---|
| Entry criterion | The assessment is complete. |
| Exit criterion | Terms are agreed. |
| Outcome | Agreed terms. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 4: Bind

Bind the policy and complete documentation.

| Aspect | Value |
|---|---|
| Entry criterion | Terms are agreed. |
| Exit criterion | The policy is bound. |
| Outcome | A bound policy. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-build-mctdgc`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-policy-to-endorsement` — The bound policy is serviced through endorsements.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-contract-to-renewal` — Bound policies renew through the renewal stream.

## 8. Measurement

- **Policy issuance turnaround** (stage: Bind) — Elapsed time from submission to bound policy. → [`dea:metric-policy-issuance-turnaround`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-009 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-029) from the CR-VS-11 industry evidence register extension. Industry-specific chain (insurance); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
