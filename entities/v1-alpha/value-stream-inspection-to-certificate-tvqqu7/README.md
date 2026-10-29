---
documentation_generated_from: value-streams-value-stream-inspection-to-certificate-tvqqu7.yaml
id: value-streams:value-stream-inspection-to-certificate-tvqqu7
name: Inspection to Certificate
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: governance
industries:
- public-sector
- construction-real-estate
specificity: industry-specific
entry_criterion: An inspection falls due or is requested.
exit_criterion: The certificate or notice is issued.
outcome: An issued inspection certificate or notice.
stages:
- Schedule Inspection
- Inspect On Site
- Assess
- Issue Certificate
capabilities:
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-regulation-management-gya4d8
- capabilities:capability-risk-management-h9uxdw
- capabilities:capability-workforce-planning-b43rhm
processes:
- processes:process-eo-operate-44jsrp
- processes:process-fa-operate-8vqvkk
- processes:process-ge-operate-zwaes5
- processes:process-pr-operate-bbe384
metrics:
- Certificate issuance turnaround
upstream: []
downstream: []
evidence_sources:
- SRC-014
- SRC-017
---

# Inspection to Certificate

`value-streams:value-stream-inspection-to-certificate-tvqqu7` · **governance** · public-sector, construction-real-estate · industry-specific

> The regulatory-inspection stream from inspection scheduling through on-site inspection to issued certificate.

**Outcome:** An issued inspection certificate or notice.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-inspection-to-certificate-tvqqu7.yaml`](./value-streams-value-stream-inspection-to-certificate-tvqqu7.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Schedule Inspection"]
  S2["2. Inspect On Site"]
  S3["3. Assess"]
  S4["4. Issue Certificate"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Schedule Inspection** | An inspection falls due. | The inspection is scheduled. | 2 | 1 | yes |
| 2 | **Inspect On Site** | The inspection is scheduled. | The inspection is complete. | 2 | 1 | yes |
| 3 | **Assess** | The inspection is complete. | The assessment is complete. | 2 | 1 | no |
| 4 | **Issue Certificate** | The assessment is complete. | The certificate is issued. | 2 | 1 | yes |

### 1. Schedule Inspection

Schedule the inspection.

| Aspect | Value |
|---|---|
| Entry criterion | An inspection falls due. |
| Exit criterion | The inspection is scheduled. |
| Outcome | A scheduled inspection. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-workforce-planning-b43rhm` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Inspect On Site

Perform the on-site inspection.

| Aspect | Value |
|---|---|
| Entry criterion | The inspection is scheduled. |
| Exit criterion | The inspection is complete. |
| Outcome | Inspection findings. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 3. Assess

Assess findings against the standard.

| Aspect | Value |
|---|---|
| Entry criterion | The inspection is complete. |
| Exit criterion | The assessment is complete. |
| Outcome | A completed assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### 4. Issue Certificate

Issue the certificate or notice.

| Aspect | Value |
|---|---|
| Entry criterion | The assessment is complete. |
| Exit criterion | The certificate is issued. |
| Outcome | An issued certificate. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8` · `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-fa-operate-8vqvkk` |

## Scope boundary

**Entry:** An inspection falls due or is requested.

**Exit:** The certificate or notice is issued.

**In scope**

- Inspection scheduling
- On-site inspection
- Assessment
- Certificate issuance

**Out of scope** (owned by the named neighbour)

- Permitting (Apply to Decide)
- Enforcement

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-planning-b43rhm`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-zwaes5`
- `processes:process-eo-operate-44jsrp`
- `processes:process-fa-operate-8vqvkk`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Certificate issuance turnaround** (stream-level) — Elapsed time from inspection to issued certificate.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-014 | industry-reference-model | Public-sector service chains (permits, grants, benefits; public structure) |
| SRC-017 | industry-reference-model | Construction and real-estate chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-077) from the CR-VS-11 industry evidence register extension. Industry-specific chain (public-sector, construction-real-estate); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
