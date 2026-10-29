---
documentation_generated_from: value-streams-value-stream-alert-to-report-a2qttg.yaml
id: value-streams:value-stream-alert-to-report-a2qttg
name: Alert to Report
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: governance
industries:
- financial-services
specificity: industry-specific
entry_criterion: A monitoring alert is generated.
exit_criterion: The reporting decision is made and filed where required.
outcome: A completed, defensible reporting decision on every financial-crime alert.
stages:
- Triage Alert
- Investigate
- Decide and Review
- File or Close
capabilities:
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-regulation-management-gya4d8
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-fa-operate-8vqvkk
- processes:process-ge-operate-tpenm6
- processes:process-ge-operate-zwaes5
metrics:
- Alert-to-decision cycle time
upstream: []
downstream: []
evidence_sources:
- SRC-012
---

# Alert to Report

`value-streams:value-stream-alert-to-report-a2qttg` · **governance** · financial-services · industry-specific

> The financial-crime stream from alert detection through investigation to the reporting decision.

**Outcome:** A completed, defensible reporting decision on every financial-crime alert.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-alert-to-report-a2qttg.yaml`](./value-streams-value-stream-alert-to-report-a2qttg.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Triage Alert"]
  S2["2. Investigate"]
  S3["3. Decide and Review"]
  S4["4. File or Close"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Triage Alert** | An alert is generated. | The alert is triaged. | 2 | 1 | no |
| 2 | **Investigate** | The alert is triaged. | The investigation is complete. | 2 | 1 | no |
| 3 | **Decide and Review** | The investigation is complete. | The decision is made and reviewed. | 2 | 1 | no |
| 4 | **File or Close** | The decision is made. | The report is filed or the alert closed with rationale. | 2 | 1 | no |

### 1. Triage Alert

Triage the monitoring alert.

| Aspect | Value |
|---|---|
| Entry criterion | An alert is generated. |
| Exit criterion | The alert is triaged. |
| Outcome | A triaged alert. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### 2. Investigate

Investigate the alerted activity.

| Aspect | Value |
|---|---|
| Entry criterion | The alert is triaged. |
| Exit criterion | The investigation is complete. |
| Outcome | A completed investigation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 3. Decide and Review

Make the reporting decision with quality review.

| Aspect | Value |
|---|---|
| Entry criterion | The investigation is complete. |
| Exit criterion | The decision is made and reviewed. |
| Outcome | A reviewed decision. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 4. File or Close

File the report or close with rationale.

| Aspect | Value |
|---|---|
| Entry criterion | The decision is made. |
| Exit criterion | The report is filed or the alert closed with rationale. |
| Outcome | A dispositioned alert. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-fa-operate-8vqvkk` |

## Scope boundary

**Entry:** A monitoring alert is generated.

**Exit:** The reporting decision is made and filed where required.

**In scope**

- Alert triage
- Investigation
- Decision and quality review
- Regulatory filing or closure

**Out of scope** (owned by the named neighbour)

- Customer onboarding due diligence (Onboard to Activate)
- General risk reporting

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-regulation-management-gya4d8`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-operate-zwaes5`
- `processes:process-fa-operate-8vqvkk`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Alert-to-decision cycle time** (stream-level) — Elapsed days from alert to disposition.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-012 | industry-reference-model | Financial-crime and regulatory operations chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-025) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
