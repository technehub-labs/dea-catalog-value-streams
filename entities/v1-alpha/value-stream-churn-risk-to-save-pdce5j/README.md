---
documentation_generated_from: value-streams-value-stream-churn-risk-to-save-pdce5j.yaml
id: value-streams:value-stream-churn-risk-to-save-pdce5j
name: Churn Risk to Save
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- telecommunications
specificity: industry-specific
entry_criterion: A churn-risk score crosses threshold.
exit_criterion: The customer is retained or churns with the decision recorded.
outcome: At-risk customers retained or consciously churned.
stages:
- Identify Risk
- Intervene
- Track Outcome
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-enterprise-performance-management-5fxren
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-marketing-xmc539
processes:
- processes:process-pr-improve-t6uvan
- processes:process-sd-operate-ucxpz4
metrics:
- Churn rate (telecom)
upstream:
- value-stream-contract-to-renewal
downstream: []
evidence_sources:
- SRC-010
---

# Churn Risk to Save

`value-streams:value-stream-churn-risk-to-save-pdce5j` · **operational** · telecommunications · industry-specific

> The retention stream from churn-risk identification through targeted intervention to a saved or churned decision.

**Outcome:** At-risk customers retained or consciously churned.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-churn-risk-to-save-pdce5j.yaml`](./value-streams-value-stream-churn-risk-to-save-pdce5j.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Identify Risk"]
  S2["2. Intervene"]
  S3["3. Track Outcome"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Identify Risk** | A risk threshold is crossed. | At-risk customers are identified. | 2 | 1 | no |
| 2 | **Intervene** | The list is identified. | Interventions are delivered. | 2 | 1 | yes |
| 3 | **Track Outcome** | Interventions are delivered. | Outcomes are recorded. | 2 | 1 | no |

### 1. Identify Risk

Identify at-risk customers from behavior and sentiment.

| Aspect | Value |
|---|---|
| Entry criterion | A risk threshold is crossed. |
| Exit criterion | At-risk customers are identified. |
| Outcome | An at-risk list. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

### 2. Intervene

Design and deliver the save intervention.

| Aspect | Value |
|---|---|
| Entry criterion | The list is identified. |
| Exit criterion | Interventions are delivered. |
| Outcome | Delivered interventions. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-improve-t6uvan` |

### 3. Track Outcome

Track retention outcome per intervention.

| Aspect | Value |
|---|---|
| Entry criterion | Interventions are delivered. |
| Exit criterion | Outcomes are recorded. |
| Outcome | Recorded outcomes. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-performance-management-5fxren` · `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

## Scope boundary

**Entry:** A churn-risk score crosses threshold.

**Exit:** The customer is retained or churns with the decision recorded.

**In scope**

- Risk identification
- Intervention design and offer
- Outcome tracking

**Out of scope** (owned by the named neighbour)

- Acquisition campaigns
- Contractual renewal (Contract to Renewal)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-operate-ucxpz4`
- `processes:process-pr-improve-t6uvan`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [contract to renewal](../value-stream-contract-to-renewal-5x3r4x/README.md) — Saved customers flow to term renewal.

**Downstream:** none recorded.

## Measurement

- **Churn rate (telecom)** (stage: Track Outcome) — Subscriber churn per period. → [`dea:metric-churn-rate-telecom`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-010 | industry-reference-model | Telecommunications industry reference models (eTOM category-level structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-040) from the CR-VS-11 industry evidence register extension. Industry-specific chain (telecommunications); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
