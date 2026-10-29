# Commit to Deploy

Admitted Value Stream record (`value-streams:value-stream-commit-to-deploy-65cr4z`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-commit-to-deploy-65cr4z` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | technology · industry-specific |
| Record | [`value-streams-value-stream-commit-to-deploy-65cr4z.yaml`](./value-streams-value-stream-commit-to-deploy-65cr4z.yaml) — authoritative |

## 2. Definition

> The software delivery stream from code commit through build, test, and release to production deployment.

## 3. Value proposition and served party

**Outcome:** A deployed change in production serving users.

## 4. Stream boundary

**Entry criterion:** A change is committed.

**Exit criterion:** The change is deployed to production.

**In scope** (from the record's `scope.includes`):

- Build and test
- Release staging
- Production deployment
- Verification

**Out of scope** (each concern owned by the named neighbour):

- Incident response (Incident to Restore)
- Feature development (Concept to Launch)

## 5. Value stages

Commit to Deploy decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Build and Test

Build the change and run the test suites.

| Aspect | Value |
|---|---|
| Entry criterion | A change is committed. |
| Exit criterion | The change passes tests. |
| Outcome | A tested change. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-build-j9z3q4`, `processes:process-eo-operate-44jsrp` |

### Stage 2: Stage Release

Stage the release.

| Aspect | Value |
|---|---|
| Entry criterion | The change passes tests. |
| Exit criterion | The release is staged. |
| Outcome | A staged release. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-eo-design-6j5mxp` |

### Stage 3: Deploy

Deploy to production.

| Aspect | Value |
|---|---|
| Entry criterion | The release is staged. |
| Exit criterion | The change is live in production. |
| Outcome | A deployed change. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-xud3hs` |

### Stage 4: Verify

Verify the deployment in production.

| Aspect | Value |
|---|---|
| Entry criterion | The change is deployed. |
| Exit criterion | Deployment is verified. |
| Outcome | A verified deployment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-design-6j5mxp`
- `processes:process-eo-operate-xud3hs`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-concept-to-launch` — Approved features flow into the delivery pipeline.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-incident-to-restore` — Defective deployments can trigger incidents.

## 8. Measurement

- **Lead time for changes** (stage: Deploy) — Elapsed time from commit to production. → [`dea:metric-lead-time-for-changes`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Release frequency** (stage: Deploy) — Production releases per period. → [`dea:metric-release-frequency`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-019 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-105) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
