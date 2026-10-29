---
documentation_generated_from: value-streams-value-stream-apply-to-decide-qr36mf.yaml
id: value-streams:value-stream-apply-to-decide-qr36mf
name: Apply to Decide
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- public-sector
specificity: industry-specific
entry_criterion: An application (permit, grant, benefit, license) is received.
exit_criterion: The decision is communicated with reasons.
outcome: A lawful, reasoned, communicated decision within the service standard.
stages:
- Register Application
- Assess
- Decide and Communicate
- Handle Appeal
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-ge-build-mctdgc
- processes:process-ge-operate-zwaes5
- processes:process-pr-operate-bbe384
metrics:
- Decision cycle time vs service standard
upstream: []
downstream: []
evidence_sources:
- SRC-014
---

# Apply to Decide

`value-streams:value-stream-apply-to-decide-qr36mf` · **operational** · public-sector · industry-specific

> The public-administration stream from application receipt through completeness and eligibility assessment to a communicated, reasoned decision.

**Outcome:** A lawful, reasoned, communicated decision within the service standard.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-apply-to-decide-qr36mf.yaml`](./value-streams-value-stream-apply-to-decide-qr36mf.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Register Application"]
  S2["2. Assess"]
  S3["3. Decide and Communicate"]
  S4["4. Handle Appeal"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Register Application** | An application is received. | The application is complete. | 2 | 1 | yes |
| 2 | **Assess** | The application is complete. | The assessment is complete. | 2 | 1 | no |
| 3 | **Decide and Communicate** | The assessment is complete. | The decision is communicated. | 2 | 1 | yes |
| 4 | **Handle Appeal** | An appeal is lodged. | The appeal is resolved. | 2 | 1 | yes |

### 1. Register Application

Register the application and check completeness.

| Aspect | Value |
|---|---|
| Entry criterion | An application is received. |
| Exit criterion | The application is complete. |
| Outcome | A complete application. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Assess

Assess eligibility and merits.

| Aspect | Value |
|---|---|
| Entry criterion | The application is complete. |
| Exit criterion | The assessment is complete. |
| Outcome | A completed assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 3. Decide and Communicate

Decide and communicate with reasons.

| Aspect | Value |
|---|---|
| Entry criterion | The assessment is complete. |
| Exit criterion | The decision is communicated. |
| Outcome | A communicated decision. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 4. Handle Appeal

Handle any appeal.

| Aspect | Value |
|---|---|
| Entry criterion | An appeal is lodged. |
| Exit criterion | The appeal is resolved. |
| Outcome | A resolved appeal. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u` · `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

## Scope boundary

**Entry:** An application (permit, grant, benefit, license) is received.

**Exit:** The decision is communicated with reasons.

**In scope**

- Application registration and completeness
- Eligibility and merits assessment
- Decision and communication
- Appeal handling

**Out of scope** (owned by the named neighbour)

- Records disclosure (Request to Disclose)
- Enforcement actions

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-zwaes5`
- `processes:process-ge-build-mctdgc`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Decision cycle time vs service standard** (stream-level) — Elapsed time from receipt to communicated decision against the standard.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-014 | industry-reference-model | Public-sector service chains (permits, grants, benefits; public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-073) from the CR-VS-11 industry evidence register extension. Industry-specific chain (public-sector); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
