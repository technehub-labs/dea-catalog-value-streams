# Exam Set to Grade

Admitted Value Stream record (`value-streams:value-stream-exam-set-to-grade-cyfqd5`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-exam-set-to-grade-cyfqd5` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | education · industry-specific |
| Record | [`value-streams-value-stream-exam-set-to-grade-cyfqd5.yaml`](./value-streams-value-stream-exam-set-to-grade-cyfqd5.yaml) — authoritative |

## 2. Definition

> The assessment stream from exam setting through administration to released grades.

## 3. Value proposition and served party

**Outcome:** Released, moderated grades for the assessment.

## 4. Stream boundary

**Entry criterion:** An assessment cycle is scheduled.

**Exit criterion:** Grades are released.

**In scope** (from the record's `scope.includes`):

- Assessment setting and moderation
- Administration
- Marking and grade release

**Out of scope** (each concern owned by the named neighbour):

- Course delivery (Course Design to Delivery)
- Certification (Inspect to Certificate pattern)

## 5. Value stages

Exam Set to Grade decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Set Assessment

Set and moderate the assessment.

| Aspect | Value |
|---|---|
| Entry criterion | A cycle is scheduled. |
| Exit criterion | The assessment is set. |
| Outcome | A set assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 2: Administer

Administer the assessment.

| Aspect | Value |
|---|---|
| Entry criterion | The assessment is set. |
| Exit criterion | The assessment is administered. |
| Outcome | An administered assessment. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Mark and Release

Mark and release the grades.

| Aspect | Value |
|---|---|
| Entry criterion | The assessment is administered. |
| Exit criterion | Grades are released. |
| Outcome | Released grades. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-operations-management-pm3w8k`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-2jnz85`
- `processes:process-fa-operate-ycba3k`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Grade release turnaround** (stream-level) — Elapsed time from administration to released grades.

## 9. Evidence and admission

**Evidence sources:** SRC-015 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-086) from the CR-VS-11 industry evidence register extension. Industry-specific chain (education); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
