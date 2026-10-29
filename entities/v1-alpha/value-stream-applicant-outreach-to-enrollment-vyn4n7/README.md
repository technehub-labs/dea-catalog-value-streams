# Applicant Outreach to Enrollment

Admitted Value Stream record (`value-streams:value-stream-applicant-outreach-to-enrollment-vyn4n7`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-applicant-outreach-to-enrollment-vyn4n7` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | education · industry-specific |
| Record | [`value-streams-value-stream-applicant-outreach-to-enrollment-vyn4n7.yaml`](./value-streams-value-stream-applicant-outreach-to-enrollment-vyn4n7.yaml) — authoritative |

## 2. Definition

> The recruitment stream from prospective-student outreach through application to enrolled student.

## 3. Value proposition and served party

**Outcome:** An enrolled student cohort for the intake.

## 4. Stream boundary

**Entry criterion:** An outreach campaign is launched.

**Exit criterion:** The intake enrollment target is met.

**In scope** (from the record's `scope.includes`):

- Outreach and recruitment
- Application support
- Enrollment

**Out of scope** (each concern owned by the named neighbour):

- Admission decisions (Admit to Graduate)
- Alumni engagement

## 5. Value stages

Applicant Outreach to Enrollment decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Recruit

Run outreach to prospective students.

| Aspect | Value |
|---|---|
| Entry criterion | A campaign is launched. |
| Exit criterion | Applications are received. |
| Outcome | Received applications. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pr-build-nygvw7` |

### Stage 2: Support Application

Support applicants through application.

| Aspect | Value |
|---|---|
| Entry criterion | Applications are received. |
| Exit criterion | Applications are completed. |
| Outcome | Completed applications. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 3: Enroll

Enroll admitted students.

| Aspect | Value |
|---|---|
| Entry criterion | Admissions are made. |
| Exit criterion | The cohort is enrolled. |
| Outcome | An enrolled cohort. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-build-nygvw7`
- `processes:process-pr-operate-bbe384`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-admit-to-graduate` — Enrolled students enter the student lifecycle.

**Downstream streams:** none recorded.

## 8. Measurement

- **Outreach-to-enrollment conversion** (stream-level) — Enrolled students per outreach contact.

## 9. Evidence and admission

**Evidence sources:** SRC-015 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-084) from the CR-VS-11 industry evidence register extension. Industry-specific chain (education); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
