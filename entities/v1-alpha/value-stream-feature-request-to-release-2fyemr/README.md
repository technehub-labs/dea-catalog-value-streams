# Feature Request to Release

Admitted Value Stream record (`value-streams:value-stream-feature-request-to-release-2fyemr`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-feature-request-to-release-2fyemr` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | technology · industry-specific |
| Record | [`value-streams-value-stream-feature-request-to-release-2fyemr.yaml`](./value-streams-value-stream-feature-request-to-release-2fyemr.yaml) — authoritative |

## 2. Definition

> The product stream from feature request through prioritization and build to released feature.

## 3. Value proposition and served party

**Outcome:** A released feature adopted by users.

## 4. Stream boundary

**Entry criterion:** A feature request is received.

**Exit criterion:** The feature is released.

**In scope** (from the record's `scope.includes`):

- Intake and prioritization
- Specification and build
- Release and adoption

**Out of scope** (each concern owned by the named neighbour):

- Roadmap planning (Plan to Forecast pattern)
- Delivery pipeline (Commit to Deploy)

## 5. Value stages

Feature Request to Release decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Intake and Prioritize

Intake and prioritize the request.

| Aspect | Value |
|---|---|
| Entry criterion | A request is received. |
| Exit criterion | The request is prioritized. |
| Outcome | A prioritized request. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-idea-management-86dckf` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

### Stage 2: Specify and Build

Specify the feature and build it.

| Aspect | Value |
|---|---|
| Entry criterion | The request is prioritized. |
| Exit criterion | The feature is built. |
| Outcome | A built feature. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8`, `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-pv-design-8v4k89`, `processes:process-eo-build-j9z3q4` |

### Stage 3: Release and Drive Adoption

Release the feature and drive adoption.

| Aspect | Value |
|---|---|
| Entry criterion | The feature is built. |
| Exit criterion | The feature is released and adopted. |
| Outcome | An adopted feature. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-build-nygvw7`, `processes:process-eo-operate-xud3hs` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-idea-management-86dckf`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-operations-management-pm3w8k`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-operate-ucxpz4`
- `processes:process-pv-design-8v4k89`
- `processes:process-eo-build-j9z3q4`
- `processes:process-pr-build-nygvw7`
- `processes:process-eo-operate-xud3hs`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-commit-to-deploy` — Built features deploy through the pipeline.

**Downstream streams:** none recorded.

## 8. Measurement

- **Feature adoption time** (stream-level) — Elapsed time from release to target adoption.

## 9. Evidence and admission

**Evidence sources:** SRC-019 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-107) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
