# Security Alert to Remediation

Admitted Value Stream record (`value-streams:value-stream-security-alert-to-remediation-j6wn3b`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-security-alert-to-remediation-j6wn3b` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | technology · industry-specific |
| Record | [`value-streams-value-stream-security-alert-to-remediation-j6wn3b.yaml`](./value-streams-value-stream-security-alert-to-remediation-j6wn3b.yaml) — authoritative |

## 2. Definition

> The security-operations stream from alert triage through investigation to remediated threat.

## 3. Value proposition and served party

**Outcome:** A remediated threat with closed finding.

## 4. Stream boundary

**Entry criterion:** A security alert fires.

**Exit criterion:** The threat is remediated and the finding closed.

**In scope** (from the record's `scope.includes`):

- Alert triage
- Investigation
- Containment
- Remediation and closure

**Out of scope** (each concern owned by the named neighbour):

- Incident response (Incident to Restore)
- Vulnerability management

## 5. Value stages

Security Alert to Remediation decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Triage Alert

Triage the security alert.

| Aspect | Value |
|---|---|
| Entry criterion | An alert fires. |
| Exit criterion | The alert is triaged. |
| Outcome | A triaged alert. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 2: Investigate

Investigate the threat.

| Aspect | Value |
|---|---|
| Entry criterion | The alert is triaged. |
| Exit criterion | The investigation is complete. |
| Outcome | A completed investigation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Contain

Contain the threat.

| Aspect | Value |
|---|---|
| Entry criterion | The investigation is complete. |
| Exit criterion | The threat is contained. |
| Outcome | A contained threat. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 4: Remediate and Close

Remediate and close the finding.

| Aspect | Value |
|---|---|
| Entry criterion | The threat is contained. |
| Exit criterion | The finding is closed. |
| Outcome | A closed finding. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-eo-improve-g3ngp3` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-operate-zwaes5`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-improve-g3ngp3`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Mean time to remediate** (stream-level) — Mean elapsed time from alert to closed finding.

## 9. Evidence and admission

**Evidence sources:** SRC-019 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-111) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
