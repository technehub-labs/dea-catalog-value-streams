---
documentation_generated_from: value-streams-value-stream-model-to-deployment-44fap5.yaml
id: value-streams:value-stream-model-to-deployment-44fap5
name: Model to Deployment
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- technology
specificity: industry-specific
entry_criterion: A model development need is approved.
exit_criterion: The model is deployed and monitored.
outcome: A deployed, monitored model serving predictions.
stages:
- Develop Model
- Validate and Approve
- Deploy
- Monitor
capabilities:
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-enterprise-performance-management-5fxren
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-risk-management-h9uxdw
- capabilities:capability-technology-enablement-y6nkws
processes:
- processes:process-eo-build-j9z3q4
- processes:process-eo-operate-xud3hs
- processes:process-ge-operate-zwaes5
- processes:process-sd-operate-ucxpz4
metrics:
- Model deployment cycle time
upstream: []
downstream: []
evidence_sources:
- SRC-019
---

# Model to Deployment

`value-streams:value-stream-model-to-deployment-44fap5` · **operational** · technology · industry-specific

> The AI/ML stream from model development through validation and approval to deployed, monitored model.

**Outcome:** A deployed, monitored model serving predictions.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-model-to-deployment-44fap5.yaml`](./value-streams-value-stream-model-to-deployment-44fap5.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Develop Model"]
  S2["2. Validate and Approve"]
  S3["3. Deploy"]
  S4["4. Monitor"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Develop Model** | A need is approved. | The model is trained. | 2 | 1 | no |
| 2 | **Validate and Approve** | The model is trained. | The model is approved. | 2 | 1 | no |
| 3 | **Deploy** | The model is approved. | The model is serving. | 1 | 1 | no |
| 4 | **Monitor** | The model serves. | The model is monitored with drift response. | 2 | 1 | no |

### 1. Develop Model

Develop and train the model.

| Aspect | Value |
|---|---|
| Entry criterion | A need is approved. |
| Exit criterion | The model is trained. |
| Outcome | A trained model. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws` · `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### 2. Validate and Approve

Validate the model and approve for use.

| Aspect | Value |
|---|---|
| Entry criterion | The model is trained. |
| Exit criterion | The model is approved. |
| Outcome | An approved model. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 3. Deploy

Deploy the model to serving.

| Aspect | Value |
|---|---|
| Entry criterion | The model is approved. |
| Exit criterion | The model is serving. |
| Outcome | A serving model. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-operate-xud3hs` |

### 4. Monitor

Monitor model performance and drift.

| Aspect | Value |
|---|---|
| Entry criterion | The model serves. |
| Exit criterion | The model is monitored with drift response. |
| Outcome | A monitored model. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d` · `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

## Scope boundary

**Entry:** A model development need is approved.

**Exit:** The model is deployed and monitored.

**In scope**

- Development and training
- Validation and approval
- Deployment
- Monitoring

**Out of scope** (owned by the named neighbour)

- Software delivery (Commit to Deploy)
- Data governance

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-build-j9z3q4`
- `processes:process-ge-operate-zwaes5`
- `processes:process-eo-operate-xud3hs`
- `processes:process-sd-operate-ucxpz4`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Model deployment cycle time** (stream-level) — Elapsed time from approval to serving.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-019 | industry-reference-model | Technology / SaaS product chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-109) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
