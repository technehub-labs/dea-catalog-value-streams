# Incident to Restore

Admitted Value Stream record (`value-streams:value-stream-incident-to-restore-7u3yyz`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-incident-to-restore-7u3yyz` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | technology · industry-specific |
| Record | [`value-streams-value-stream-incident-to-restore-7u3yyz.yaml`](./value-streams-value-stream-incident-to-restore-7u3yyz.yaml) — authoritative |

## 2. Definition

> The reliability stream from incident detection through response to restored service with post-incident review.

## 3. Value proposition and served party

**Outcome:** Restored service with a completed post-incident review.

## 4. Stream boundary

**Entry criterion:** An incident is detected or reported.

**Exit criterion:** Service is restored and the review is complete.

**In scope** (from the record's `scope.includes`):

- Detection and triage
- Response and mitigation
- Restoration
- Post-incident review

**Out of scope** (each concern owned by the named neighbour):

- Change deployment (Commit to Deploy)
- Problem management

## 5. Value stages

Incident to Restore decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Detect and Triage

Detect and triage the incident.

| Aspect | Value |
|---|---|
| Entry criterion | An incident occurs. |
| Exit criterion | The incident is triaged. |
| Outcome | A triaged incident. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-security-management-wmzc7c` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 2: Respond and Mitigate

Respond and mitigate impact.

| Aspect | Value |
|---|---|
| Entry criterion | The incident is triaged. |
| Exit criterion | Impact is mitigated. |
| Outcome | Mitigated impact. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Restore

Restore the service.

| Aspect | Value |
|---|---|
| Entry criterion | Impact is mitigated. |
| Exit criterion | The service is restored. |
| Outcome | Restored service. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-operate-j9cjzz` |

### Stage 4: Post-Incident Review

Complete the post-incident review.

| Aspect | Value |
|---|---|
| Entry criterion | The service is restored. |
| Exit criterion | The review is complete with actions. |
| Outcome | A completed review. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-performance-management-5fxren`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-j9cjzz`
- `processes:process-ge-operate-zwaes5`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Mean time to restore service** (stage: Restore) — Mean elapsed time from detection to restoration. → [`dea:metric-mean-time-to-restore-service`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-019 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-106) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
