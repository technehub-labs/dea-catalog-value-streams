# Clinical Trial Recruitment

Admitted Value Stream record (`value-streams:value-stream-clinical-trial-recruitment-zqvzg9`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-clinical-trial-recruitment-zqvzg9` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | life-sciences, healthcare · industry-specific |
| Record | [`value-streams-value-stream-clinical-trial-recruitment-zqvzg9.yaml`](./value-streams-value-stream-clinical-trial-recruitment-zqvzg9.yaml) — authoritative |

## 2. Definition

> The end-to-end stream from trial-site preparation through patient identification, consent, and enrollment into a clinical trial.

## 3. Value proposition and served party

**Outcome:** A fully enrolled clinical trial cohort at the site.

## 4. Stream boundary

**Entry criterion:** A trial protocol is approved and the site is activated.

**Exit criterion:** The site reaches its enrollment target.

**In scope** (from the record's `scope.includes`):

- Site activation
- Patient identification and screening
- Informed consent
- Enrollment and baseline

**Out of scope** (each concern owned by the named neighbour):

- Trial conduct and data collection (Trial to Readout)
- Care delivery (Admission to Discharge)

## 5. Value stages

Clinical Trial Recruitment decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Activate Site

Prepare and activate the trial site.

| Aspect | Value |
|---|---|
| Entry criterion | The protocol is approved. |
| Exit criterion | The site is activated and ready. |
| Outcome | An activated trial site. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-partner-management-cp3vdb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### Stage 2: Identify and Screen

Identify and screen candidate patients.

| Aspect | Value |
|---|---|
| Entry criterion | The site is activated. |
| Exit criterion | Eligible candidates are identified. |
| Outcome | A screened eligible cohort. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 3: Consent

Obtain informed consent.

| Aspect | Value |
|---|---|
| Entry criterion | Eligible candidates are identified. |
| Exit criterion | Consent is documented. |
| Outcome | Informed, documented consent. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 4: Enroll

Enroll consented patients and complete baseline.

| Aspect | Value |
|---|---|
| Entry criterion | Consent is documented. |
| Exit criterion | The enrollment target is met. |
| Outcome | A fully enrolled cohort. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-build-j9z3q4`
- `processes:process-pr-operate-bbe384`
- `processes:process-ge-build-mctdgc`
- `processes:process-eo-operate-2jnz85`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-trial-to-readout` — Enrollment completes the trial intake.

**Downstream streams:** none recorded.

## 8. Measurement

- **Clinical trial enrollment cycle time** (stage: Enroll) — Elapsed days from site activation to enrollment target. → [`dea:metric-clinical-trial-enrollment-cycle-time`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-018 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-019) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences, healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
