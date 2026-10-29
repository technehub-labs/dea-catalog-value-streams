# Safety Incident to Closure

Admitted Value Stream record (`value-streams:value-stream-safety-incident-to-closure-6v5uxt`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-safety-incident-to-closure-6v5uxt` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | utilities-energy, manufacturing · industry-specific |
| Record | [`value-streams-value-stream-safety-incident-to-closure-6v5uxt.yaml`](./value-streams-value-stream-safety-incident-to-closure-6v5uxt.yaml) — authoritative |

## 2. Definition

> The safety stream from incident report through investigation to corrective-action closure.

## 3. Value proposition and served party

**Outcome:** Incidents investigated with corrective actions closed out.

## 4. Stream boundary

**Entry criterion:** A safety incident is reported.

**Exit criterion:** The investigation and corrective actions are closed.

**In scope** (from the record's `scope.includes`):

- Incident reporting
- Investigation
- Corrective action
- Closure verification

**Out of scope** (each concern owned by the named neighbour):

- Regulatory reporting (Record to Report)
- Insurance claims interface

## 5. Value stages

Safety Incident to Closure decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Report Incident

Report and register the safety incident.

| Aspect | Value |
|---|---|
| Entry criterion | An incident occurs. |
| Exit criterion | The incident is registered. |
| Outcome | A registered incident. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 2: Investigate

Investigate causes.

| Aspect | Value |
|---|---|
| Entry criterion | The incident is registered. |
| Exit criterion | Causes are determined. |
| Outcome | Determined causes. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Correct

Implement corrective actions.

| Aspect | Value |
|---|---|
| Entry criterion | Causes are determined. |
| Exit criterion | Corrective actions are implemented. |
| Outcome | Implemented actions. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-eo-improve-g3ngp3` |

### Stage 4: Verify Closure

Verify effectiveness and close.

| Aspect | Value |
|---|---|
| Entry criterion | Actions are implemented. |
| Exit criterion | Closure is verified. |
| Outcome | A closed incident. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-operate-zwaes5`
- `processes:process-eo-improve-g3ngp3`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Recordable incident rate** (stream-level) — Recordable incidents per hours worked.

## 9. Evidence and admission

**Evidence sources:** SRC-011, SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-049) from the CR-VS-11 industry evidence register extension. Industry-specific chain (utilities-energy, manufacturing); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
