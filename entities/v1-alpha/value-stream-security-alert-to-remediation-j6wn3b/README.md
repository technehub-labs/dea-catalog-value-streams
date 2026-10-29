---
documentation_generated_from: value-streams-value-stream-security-alert-to-remediation-j6wn3b.yaml
id: value-streams:value-stream-security-alert-to-remediation-j6wn3b
name: Security Alert to Remediation
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: governance
industries:
- technology
specificity: industry-specific
entry_criterion: A security alert fires.
exit_criterion: The threat is remediated and the finding closed.
outcome: A remediated threat with closed finding.
stages:
- Triage Alert
- Investigate
- Contain
- Remediate and Close
capabilities:
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-risk-management-h9uxdw
- capabilities:capability-security-management-wmzc7c
processes:
- processes:process-eo-improve-g3ngp3
- processes:process-eo-operate-2jnz85
- processes:process-ge-operate-tpenm6
- processes:process-ge-operate-zwaes5
metrics:
- Mean time to remediate
upstream: []
downstream: []
evidence_sources:
- SRC-019
---

# Security Alert to Remediation

`value-streams:value-stream-security-alert-to-remediation-j6wn3b` · **governance** · technology · industry-specific

> The security-operations stream from alert triage through investigation to remediated threat.

**Outcome:** A remediated threat with closed finding.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-security-alert-to-remediation-j6wn3b.yaml`](./value-streams-value-stream-security-alert-to-remediation-j6wn3b.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Triage Alert"]
  S2["2. Investigate"]
  S3["3. Contain"]
  S4["4. Remediate and Close"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Triage Alert** | An alert fires. | The alert is triaged. | 2 | 1 | no |
| 2 | **Investigate** | The alert is triaged. | The investigation is complete. | 2 | 1 | no |
| 3 | **Contain** | The investigation is complete. | The threat is contained. | 2 | 1 | no |
| 4 | **Remediate and Close** | The threat is contained. | The finding is closed. | 2 | 1 | no |

### 1. Triage Alert

Triage the security alert.

| Aspect | Value |
|---|---|
| Entry criterion | An alert fires. |
| Exit criterion | The alert is triaged. |
| Outcome | A triaged alert. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### 2. Investigate

Investigate the threat.

| Aspect | Value |
|---|---|
| Entry criterion | The alert is triaged. |
| Exit criterion | The investigation is complete. |
| Outcome | A completed investigation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 3. Contain

Contain the threat.

| Aspect | Value |
|---|---|
| Entry criterion | The investigation is complete. |
| Exit criterion | The threat is contained. |
| Outcome | A contained threat. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### 4. Remediate and Close

Remediate and close the finding.

| Aspect | Value |
|---|---|
| Entry criterion | The threat is contained. |
| Exit criterion | The finding is closed. |
| Outcome | A closed finding. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c` · `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-eo-improve-g3ngp3` |

## Scope boundary

**Entry:** A security alert fires.

**Exit:** The threat is remediated and the finding closed.

**In scope**

- Alert triage
- Investigation
- Containment
- Remediation and closure

**Out of scope** (owned by the named neighbour)

- Incident response (Incident to Restore)
- Vulnerability management

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-operate-zwaes5`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-improve-g3ngp3`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Mean time to remediate** (stream-level) — Mean elapsed time from alert to closed finding.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-019 | industry-reference-model | Technology / SaaS product chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-111) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
