# Admission to Discharge

Admitted Value Stream record (`value-streams:value-stream-admission-to-discharge-xeuu5u`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-admission-to-discharge-xeuu5u` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | healthcare · industry-specific |
| Record | [`value-streams-value-stream-admission-to-discharge-xeuu5u.yaml`](./value-streams-value-stream-admission-to-discharge-xeuu5u.yaml) — authoritative |

## 2. Definition

> The end-to-end care delivery stream from admission through care provision to discharge with a documented transition.

## 3. Value proposition and served party

**Outcome:** A patient completes a care episode and is discharged with documented transition of care.

## 4. Stream boundary

**Entry criterion:** A patient is admitted for a care episode.

**Exit criterion:** The patient is discharged with documented transition of care.

**In scope** (from the record's `scope.includes`):

- Care planning and delivery during the episode
- Clinical documentation
- Discharge planning and execution

**Out of scope** (each concern owned by the named neighbour):

- Patient access and scheduling (Patient Access to Admission)
- Final billing (Discharge to Bill)

## 5. Value stages

Admission to Discharge decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Admit and Assess

Complete admission assessment and care plan.

| Aspect | Value |
|---|---|
| Entry criterion | The patient is admitted. |
| Exit criterion | The care plan is approved. |
| Outcome | An approved care plan. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 2: Deliver Care

Deliver care per the plan across the episode.

| Aspect | Value |
|---|---|
| Entry criterion | A care plan is approved. |
| Exit criterion | Planned care is delivered and documented. |
| Outcome | Delivered, documented care. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-2jnz85`, `processes:process-eo-operate-44jsrp` |

### Stage 3: Plan Discharge

Prepare the discharge and transition plan.

| Aspect | Value |
|---|---|
| Entry criterion | The episode nears completion. |
| Exit criterion | The discharge plan is agreed. |
| Outcome | An agreed discharge plan. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 4: Discharge

Execute discharge with documented transition.

| Aspect | Value |
|---|---|
| Entry criterion | A discharge plan is agreed. |
| Exit criterion | The patient is discharged with documented transition of care. |
| Outcome | A completed episode with safe transition. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-44jsrp`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-patient-access-to-admission` — The access stream ends at admission.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-discharge-to-bill` — Discharge starts the revenue-cycle back end.

## 8. Measurement

- **Average length of stay** (stage: Discharge) — Mean inpatient days per episode. → [`dea:metric-average-length-of-stay`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Readmission rate within 30 days** (stage: Discharge) — Share of discharges readmitted within 30 days. → [`dea:metric-readmission-rate-within-30-days`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-007 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-016) from the CR-VS-11 industry evidence register extension. Industry-specific chain (healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
