---
documentation_generated_from: value-streams-value-stream-applicant-outreach-to-enrollment-vyn4n7.yaml
id: value-streams:value-stream-applicant-outreach-to-enrollment-vyn4n7
name: Applicant Outreach to Enrollment
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- education
specificity: industry-specific
entry_criterion: An outreach campaign is launched.
exit_criterion: The intake enrollment target is met.
outcome: An enrolled student cohort for the intake.
stages:
- Recruit
- Support Application
- Enroll
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-marketing-xmc539
processes:
- processes:process-pr-build-nygvw7
- processes:process-pr-operate-bbe384
metrics:
- Outreach-to-enrollment conversion
upstream:
- value-stream-admit-to-graduate
downstream: []
evidence_sources:
- SRC-015
---

# Applicant Outreach to Enrollment

`value-streams:value-stream-applicant-outreach-to-enrollment-vyn4n7` · **operational** · education · industry-specific

> The recruitment stream from prospective-student outreach through application to enrolled student.

**Outcome:** An enrolled student cohort for the intake.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-applicant-outreach-to-enrollment-vyn4n7.yaml`](./value-streams-value-stream-applicant-outreach-to-enrollment-vyn4n7.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Recruit"]
  S2["2. Support Application"]
  S3["3. Enroll"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Recruit** | A campaign is launched. | Applications are received. | 1 | 1 | yes |
| 2 | **Support Application** | Applications are received. | Applications are completed. | 1 | 1 | yes |
| 3 | **Enroll** | Admissions are made. | The cohort is enrolled. | 2 | 1 | yes |

### 1. Recruit

Run outreach to prospective students.

| Aspect | Value |
|---|---|
| Entry criterion | A campaign is launched. |
| Exit criterion | Applications are received. |
| Outcome | Received applications. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pr-build-nygvw7` |

### 2. Support Application

Support applicants through application.

| Aspect | Value |
|---|---|
| Entry criterion | Applications are received. |
| Exit criterion | Applications are completed. |
| Outcome | Completed applications. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 3. Enroll

Enroll admitted students.

| Aspect | Value |
|---|---|
| Entry criterion | Admissions are made. |
| Exit criterion | The cohort is enrolled. |
| Outcome | An enrolled cohort. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## Scope boundary

**Entry:** An outreach campaign is launched.

**Exit:** The intake enrollment target is met.

**In scope**

- Outreach and recruitment
- Application support
- Enrollment

**Out of scope** (owned by the named neighbour)

- Admission decisions (Admit to Graduate)
- Alumni engagement

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-build-nygvw7`
- `processes:process-pr-operate-bbe384`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [admit to graduate](../value-stream-admit-to-graduate-v9jcg3/README.md) — Enrolled students enter the student lifecycle.

**Downstream:** none recorded.

## Measurement

- **Outreach-to-enrollment conversion** (stream-level) — Enrolled students per outreach contact.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-015 | industry-reference-model | Education and hospitality service chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-084) from the CR-VS-11 industry evidence register extension. Industry-specific chain (education); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
