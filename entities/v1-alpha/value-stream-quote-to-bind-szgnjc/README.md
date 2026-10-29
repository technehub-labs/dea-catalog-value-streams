---
documentation_generated_from: value-streams-value-stream-quote-to-bind-szgnjc.yaml
id: value-streams:value-stream-quote-to-bind-szgnjc
name: Quote to Bind
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- insurance
specificity: industry-specific
entry_criterion: A quote request or submission is received.
exit_criterion: The policy is bound and documented.
outcome: A bound policy for the accepted risk.
stages:
- Intake Submission
- Assess Risk
- Quote
- Bind
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-ge-build-mctdgc
- processes:process-ge-operate-tpenm6
- processes:process-pr-operate-bbe384
metrics:
- Policy issuance turnaround
upstream:
- value-stream-policy-to-endorsement
downstream:
- value-stream-contract-to-renewal
evidence_sources:
- SRC-009
---

# Quote to Bind

`value-streams:value-stream-quote-to-bind-szgnjc` · **operational** · insurance · industry-specific

> The end-to-end underwriting stream from submission through risk assessment, quote, and bound policy.

**Outcome:** A bound policy for the accepted risk.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-quote-to-bind-szgnjc.yaml`](./value-streams-value-stream-quote-to-bind-szgnjc.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Intake Submission"]
  S2["2. Assess Risk"]
  S3["3. Quote"]
  S4["4. Bind"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Intake Submission** | A submission is received. | The submission is complete. | 2 | 1 | yes |
| 2 | **Assess Risk** | The submission is complete. | The risk assessment is complete. | 2 | 1 | no |
| 3 | **Quote** | The assessment is complete. | Terms are agreed. | 2 | 1 | yes |
| 4 | **Bind** | Terms are agreed. | The policy is bound. | 2 | 1 | yes |

### 1. Intake Submission

Receive and complete the submission.

| Aspect | Value |
|---|---|
| Entry criterion | A submission is received. |
| Exit criterion | The submission is complete. |
| Outcome | A complete submission. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Assess Risk

Assess the risk and determine terms.

| Aspect | Value |
|---|---|
| Entry criterion | The submission is complete. |
| Exit criterion | The risk assessment is complete. |
| Outcome | A completed risk assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### 3. Quote

Quote terms to the customer and negotiate.

| Aspect | Value |
|---|---|
| Entry criterion | The assessment is complete. |
| Exit criterion | Terms are agreed. |
| Outcome | Agreed terms. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 4. Bind

Bind the policy and complete documentation.

| Aspect | Value |
|---|---|
| Entry criterion | Terms are agreed. |
| Exit criterion | The policy is bound. |
| Outcome | A bound policy. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

## Scope boundary

**Entry:** A quote request or submission is received.

**Exit:** The policy is bound and documented.

**In scope**

- Submission intake
- Risk assessment and underwriting
- Quotation and negotiation
- Binding and documentation

**Out of scope** (owned by the named neighbour)

- Claims (Loss to Claim Settlement)
- Policy servicing (Policy to Endorsement)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-build-mctdgc`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [policy to endorsement](../value-stream-policy-to-endorsement-3jwbzy/README.md) — The bound policy is serviced through endorsements.

**Downstream** (this stream's exit feeds their entry):

- [contract to renewal](../value-stream-contract-to-renewal-5x3r4x/README.md) — Bound policies renew through the renewal stream.

## Measurement

- **Policy issuance turnaround** (stage: Bind) — Elapsed time from submission to bound policy. → [`dea:metric-policy-issuance-turnaround`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-009 | industry-reference-model | Insurance industry reference models (policy and claims lifecycles, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-029) from the CR-VS-11 industry evidence register extension. Industry-specific chain (insurance); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
