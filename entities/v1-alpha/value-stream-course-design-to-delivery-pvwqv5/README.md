# Course Design to Delivery

Admitted Value Stream record (`value-streams:value-stream-course-design-to-delivery-pvwqv5`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-course-design-to-delivery-pvwqv5` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | development |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | education · industry-specific |
| Record | [`value-streams-value-stream-course-design-to-delivery-pvwqv5.yaml`](./value-streams-value-stream-course-design-to-delivery-pvwqv5.yaml) — authoritative |

## 2. Definition

> The academic stream from course design through approval to delivered and evaluated course.

## 3. Value proposition and served party

**Outcome:** A delivered, evaluated course offering.

## 4. Stream boundary

**Entry criterion:** A course design cycle opens.

**Exit criterion:** The course is delivered and evaluated.

**In scope** (from the record's `scope.includes`):

- Design and approval
- Delivery
- Evaluation

**Out of scope** (each concern owned by the named neighbour):

- Curriculum governance
- Faculty development

## 5. Value stages

Course Design to Delivery decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Design Course

Design the course and outcomes.

| Aspect | Value |
|---|---|
| Entry criterion | A cycle opens. |
| Exit criterion | The course is designed. |
| Outcome | A designed course. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pv-design-8v4k89` |

### Stage 2: Approve

Approve the course for delivery.

| Aspect | Value |
|---|---|
| Entry criterion | The course is designed. |
| Exit criterion | The course is approved. |
| Outcome | An approved course. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u`, `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-ge-design-kpsj5b` |

### Stage 3: Deliver

Deliver the course.

| Aspect | Value |
|---|---|
| Entry criterion | The course is approved. |
| Exit criterion | The course is delivered. |
| Outcome | A delivered course. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 4: Evaluate

Evaluate and improve the course.

| Aspect | Value |
|---|---|
| Entry criterion | The course is delivered. |
| Exit criterion | The evaluation is complete. |
| Outcome | A completed evaluation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pv-design-8v4k89`
- `processes:process-ge-design-kpsj5b`
- `processes:process-eo-operate-2jnz85`
- `processes:process-sd-operate-ucxpz4`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Course evaluation score** (stream-level) — Mean student evaluation score per offering.

## 9. Evidence and admission

**Evidence sources:** SRC-015 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-082) from the CR-VS-11 industry evidence register extension. Industry-specific chain (education); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
