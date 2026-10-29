# Admit to Graduate

Admitted Value Stream record (`value-streams:value-stream-admit-to-graduate-v9jcg3`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-admit-to-graduate-v9jcg3` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | education · industry-specific |
| Record | [`value-streams-value-stream-admit-to-graduate-v9jcg3.yaml`](./value-streams-value-stream-admit-to-graduate-v9jcg3.yaml) — authoritative |

## 2. Definition

> The student-lifecycle stream from admission through enrollment, progression, to graduation.

## 3. Value proposition and served party

**Outcome:** A graduated student with conferred award.

## 4. Stream boundary

**Entry criterion:** An admission offer is accepted.

**Exit criterion:** The student graduates with a conferred award.

**In scope** (from the record's `scope.includes`):

- Admission and enrollment
- Academic progression and support
- Award conferral

**Out of scope** (each concern owned by the named neighbour):

- Research candidature
- Continuing education

## 5. Value stages

Admit to Graduate decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Enroll

Enroll the admitted student.

| Aspect | Value |
|---|---|
| Entry criterion | An offer is accepted. |
| Exit criterion | The student is enrolled. |
| Outcome | An enrolled student. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Progress and Support

Support academic progression to completion.

| Aspect | Value |
|---|---|
| Entry criterion | The student is enrolled. |
| Exit criterion | The student completes requirements. |
| Outcome | A completed candidature. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-eo-operate-2jnz85`, `processes:process-ao-operate-87q5mk` |

### Stage 3: Confer Award

Confer the award.

| Aspect | Value |
|---|---|
| Entry criterion | Requirements are complete. |
| Exit criterion | The award is conferred. |
| Outcome | A conferred award. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-2jnz85`
- `processes:process-ao-operate-87q5mk`
- `processes:process-fa-operate-ycba3k`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-apply-to-decide` — Admission decisions are made through the application stream.

**Downstream streams:** none recorded.

## 8. Measurement

- **Completion rate** (stream-level) — Share of enrolled students graduating within the expected window.

## 9. Evidence and admission

**Evidence sources:** SRC-015 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-081) from the CR-VS-11 industry evidence register extension. Industry-specific chain (education); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
