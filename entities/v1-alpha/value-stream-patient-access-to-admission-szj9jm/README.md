# Patient Access to Admission

Admitted Value Stream record (`value-streams:value-stream-patient-access-to-admission-szj9jm`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-patient-access-to-admission-szj9jm` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | healthcare · industry-specific |
| Record | [`value-streams-value-stream-patient-access-to-admission-szj9jm.yaml`](./value-streams-value-stream-patient-access-to-admission-szj9jm.yaml) — authoritative |

## 2. Definition

> The end-to-end patient access stream from referral or self-scheduling through registration to an admitted or scheduled care episode.

## 3. Value proposition and served party

**Outcome:** A patient is registered, verified, and admitted or scheduled for a care episode.

## 4. Stream boundary

**Entry criterion:** A referral is received or a patient requests care.

**Exit criterion:** The patient is admitted or scheduled with registration and coverage verified.

**In scope** (from the record's `scope.includes`):

- Referral or self-scheduling intake
- Registration and identity verification
- Coverage verification and pre-authorization
- Admission or appointment scheduling

**Out of scope** (each concern owned by the named neighbour):

- Emergency stabilization protocols
- Inpatient care delivery (Admission to Discharge)

## 5. Value stages

Patient Access to Admission decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Intake and Triage

Capture the referral or request and triage urgency.

| Aspect | Value |
|---|---|
| Entry criterion | A referral is received or a patient requests care. |
| Exit criterion | The request is triaged and routed. |
| Outcome | A triaged, routed access request. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Register Patient

Register the patient and verify identity and demographics.

| Aspect | Value |
|---|---|
| Entry criterion | A triaged access request exists. |
| Exit criterion | The patient record is complete and verified. |
| Outcome | A verified patient record. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 3: Verify Coverage

Verify insurance coverage and obtain pre-authorization where required.

| Aspect | Value |
|---|---|
| Entry criterion | A verified patient record exists. |
| Exit criterion | Coverage is verified and authorization obtained. |
| Outcome | Confirmed coverage for the episode. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

### Stage 4: Schedule or Admit

Schedule the care episode or admit the patient.

| Aspect | Value |
|---|---|
| Entry criterion | Coverage is confirmed. |
| Exit criterion | The patient is admitted or scheduled. |
| Outcome | An admitted or scheduled care episode. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-operations-management-pm3w8k`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-sdppmp`
- `processes:process-eo-operate-2jnz85`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-admission-to-discharge` — Admission starts the care episode.

## 8. Measurement

- **Door-to-provider time** (stage: Intake and Triage) — Elapsed time from patient arrival to first provider contact. → [`dea:metric-door-to-provider-time`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-007 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-015) from the CR-VS-11 industry evidence register extension. Industry-specific chain (healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
