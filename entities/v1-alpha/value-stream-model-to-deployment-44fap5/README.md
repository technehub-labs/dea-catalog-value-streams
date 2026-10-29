# Model to Deployment

Admitted Value Stream record (`value-streams:value-stream-model-to-deployment-44fap5`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-model-to-deployment-44fap5` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | technology · industry-specific |
| Record | [`value-streams-value-stream-model-to-deployment-44fap5.yaml`](./value-streams-value-stream-model-to-deployment-44fap5.yaml) — authoritative |

## 2. Definition

> The AI/ML stream from model development through validation and approval to deployed, monitored model.

## 3. Value proposition and served party

**Outcome:** A deployed, monitored model serving predictions.

## 4. Stream boundary

**Entry criterion:** A model development need is approved.

**Exit criterion:** The model is deployed and monitored.

**In scope** (from the record's `scope.includes`):

- Development and training
- Validation and approval
- Deployment
- Monitoring

**Out of scope** (each concern owned by the named neighbour):

- Software delivery (Commit to Deploy)
- Data governance

## 5. Value stages

Model to Deployment decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Develop Model

Develop and train the model.

| Aspect | Value |
|---|---|
| Entry criterion | A need is approved. |
| Exit criterion | The model is trained. |
| Outcome | A trained model. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws`, `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### Stage 2: Validate and Approve

Validate the model and approve for use.

| Aspect | Value |
|---|---|
| Entry criterion | The model is trained. |
| Exit criterion | The model is approved. |
| Outcome | An approved model. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Deploy

Deploy the model to serving.

| Aspect | Value |
|---|---|
| Entry criterion | The model is approved. |
| Exit criterion | The model is serving. |
| Outcome | A serving model. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-operate-xud3hs` |

### Stage 4: Monitor

Monitor model performance and drift.

| Aspect | Value |
|---|---|
| Entry criterion | The model serves. |
| Exit criterion | The model is monitored with drift response. |
| Outcome | A monitored model. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-build-j9z3q4`
- `processes:process-ge-operate-zwaes5`
- `processes:process-eo-operate-xud3hs`
- `processes:process-sd-operate-ucxpz4`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Model deployment cycle time** (stream-level) — Elapsed time from approval to serving.

## 9. Evidence and admission

**Evidence sources:** SRC-019 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-109) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
