---
documentation_generated_from: value-streams-value-stream-customer-remediation-to-current-krrxzb.yaml
id: value-streams:value-stream-customer-remediation-to-current-krrxzb
name: Customer Remediation to Current
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: governance
industries:
- financial-services
specificity: industry-specific
entry_criterion: A due-diligence review falls due or is flagged.
exit_criterion: The customer file is current or the relationship is exited.
outcome: All due-diligence records current or the relationship exited.
stages:
- Identify Backlog
- Engage Customer
- Assess and Update
- Escalate or Exit
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-regulation-management-gya4d8
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-ge-operate-tpenm6
- processes:process-ge-operate-zwaes5
- processes:process-pr-operate-bbe384
metrics:
- KYC remediation backlog ratio
upstream: []
downstream: []
evidence_sources:
- SRC-012
---

# Customer Remediation to Current

`value-streams:value-stream-customer-remediation-to-current-krrxzb` · **governance** · financial-services · industry-specific

> The due-diligence remediation stream from an identified KYC/due-diligence backlog item through customer engagement to a current compliance status.

**Outcome:** All due-diligence records current or the relationship exited.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-customer-remediation-to-current-krrxzb.yaml`](./value-streams-value-stream-customer-remediation-to-current-krrxzb.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Identify Backlog"]
  S2["2. Engage Customer"]
  S3["3. Assess and Update"]
  S4["4. Escalate or Exit"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Identify Backlog** | A review falls due. | The backlog item is prioritized. | 2 | 1 | no |
| 2 | **Engage Customer** | The item is prioritized. | Required information is collected. | 1 | 1 | yes |
| 3 | **Assess and Update** | Information is collected. | The status is updated. | 2 | 1 | no |
| 4 | **Escalate or Exit** | Assessment fails. | The relationship is escalated or exited. | 2 | 1 | no |

### 1. Identify Backlog

Identify and prioritize due-diligence backlog.

| Aspect | Value |
|---|---|
| Entry criterion | A review falls due. |
| Exit criterion | The backlog item is prioritized. |
| Outcome | A prioritized backlog item. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### 2. Engage Customer

Engage the customer for updated information and documents.

| Aspect | Value |
|---|---|
| Entry criterion | The item is prioritized. |
| Exit criterion | Required information is collected. |
| Outcome | A complete remediation file. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 3. Assess and Update

Assess the file and update the compliance status.

| Aspect | Value |
|---|---|
| Entry criterion | Information is collected. |
| Exit criterion | The status is updated. |
| Outcome | A current compliance status. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 4. Escalate or Exit

Escalate or exit the unresolved relationship.

| Aspect | Value |
|---|---|
| Entry criterion | Assessment fails. |
| Exit criterion | The relationship is escalated or exited. |
| Outcome | A dispositioned relationship. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

## Scope boundary

**Entry:** A due-diligence review falls due or is flagged.

**Exit:** The customer file is current or the relationship is exited.

**In scope**

- Backlog identification
- Customer engagement and document collection
- Assessment and status update
- Escalation or exit where unresolved

**Out of scope** (owned by the named neighbour)

- New-customer onboarding (Onboard to Activate)
- Financial-crime alert handling (Alert to Report)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-zwaes5`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **KYC remediation backlog ratio** (stream-level) — Backlogged files as a share of the portfolio.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-012 | industry-reference-model | Financial-crime and regulatory operations chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-028) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
