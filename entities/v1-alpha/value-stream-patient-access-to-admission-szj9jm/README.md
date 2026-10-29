---
documentation_generated_from: value-streams-value-stream-patient-access-to-admission-szj9jm.yaml
id: value-streams:value-stream-patient-access-to-admission-szj9jm
name: Patient Access to Admission
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- healthcare
specificity: industry-specific
entry_criterion: A referral is received or a patient requests care.
exit_criterion: The patient is admitted or scheduled with registration and coverage verified.
outcome: A patient is registered, verified, and admitted or scheduled for a care episode.
stages:
- Intake and Triage
- Register Patient
- Verify Coverage
- Schedule or Admit
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
processes:
- processes:process-eo-operate-2jnz85
- processes:process-fa-operate-sdppmp
- processes:process-pr-operate-bbe384
metrics:
- Door-to-provider time
upstream: []
downstream:
- value-stream-admission-to-discharge
evidence_sources:
- SRC-007
---

# Patient Access to Admission

`value-streams:value-stream-patient-access-to-admission-szj9jm` · **operational** · healthcare · industry-specific

> The end-to-end patient access stream from referral or self-scheduling through registration to an admitted or scheduled care episode.

**Outcome:** A patient is registered, verified, and admitted or scheduled for a care episode.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-patient-access-to-admission-szj9jm.yaml`](./value-streams-value-stream-patient-access-to-admission-szj9jm.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Intake and Triage"]
  S2["2. Register Patient"]
  S3["3. Verify Coverage"]
  S4["4. Schedule or Admit"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Intake and Triage** | A referral is received or a patient requests care. | The request is triaged and routed. | 2 | 1 | yes |
| 2 | **Register Patient** | A triaged access request exists. | The patient record is complete and verified. | 2 | 1 | yes |
| 3 | **Verify Coverage** | A verified patient record exists. | Coverage is verified and authorization obtained. | 2 | 1 | yes |
| 4 | **Schedule or Admit** | Coverage is confirmed. | The patient is admitted or scheduled. | 1 | 1 | yes |

### 1. Intake and Triage

Capture the referral or request and triage urgency.

| Aspect | Value |
|---|---|
| Entry criterion | A referral is received or a patient requests care. |
| Exit criterion | The request is triaged and routed. |
| Outcome | A triaged, routed access request. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Register Patient

Register the patient and verify identity and demographics.

| Aspect | Value |
|---|---|
| Entry criterion | A triaged access request exists. |
| Exit criterion | The patient record is complete and verified. |
| Outcome | A verified patient record. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 3. Verify Coverage

Verify insurance coverage and obtain pre-authorization where required.

| Aspect | Value |
|---|---|
| Entry criterion | A verified patient record exists. |
| Exit criterion | Coverage is verified and authorization obtained. |
| Outcome | Confirmed coverage for the episode. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

### 4. Schedule or Admit

Schedule the care episode or admit the patient.

| Aspect | Value |
|---|---|
| Entry criterion | Coverage is confirmed. |
| Exit criterion | The patient is admitted or scheduled. |
| Outcome | An admitted or scheduled care episode. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## Scope boundary

**Entry:** A referral is received or a patient requests care.

**Exit:** The patient is admitted or scheduled with registration and coverage verified.

**In scope**

- Referral or self-scheduling intake
- Registration and identity verification
- Coverage verification and pre-authorization
- Admission or appointment scheduling

**Out of scope** (owned by the named neighbour)

- Emergency stabilization protocols
- Inpatient care delivery (Admission to Discharge)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-operations-management-pm3w8k`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-sdppmp`
- `processes:process-eo-operate-2jnz85`

## Cross-stream links

**Upstream:** none recorded.

**Downstream** (this stream's exit feeds their entry):

- [admission to discharge](../value-stream-admission-to-discharge-xeuu5u/README.md) — Admission starts the care episode.

## Measurement

- **Door-to-provider time** (stage: Intake and Triage) — Elapsed time from patient arrival to first provider contact. → [`dea:metric-door-to-provider-time`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-007 | industry-reference-model | Healthcare industry reference models (patient-access and revenue-cycle chains, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-015) from the CR-VS-11 industry evidence register extension. Industry-specific chain (healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
