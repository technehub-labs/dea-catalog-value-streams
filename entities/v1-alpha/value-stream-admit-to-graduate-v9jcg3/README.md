---
documentation_generated_from: value-streams-value-stream-admit-to-graduate-v9jcg3.yaml
id: value-streams:value-stream-admit-to-graduate-v9jcg3
name: Admit to Graduate
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- education
specificity: industry-specific
entry_criterion: An admission offer is accepted.
exit_criterion: The student graduates with a conferred award.
outcome: A graduated student with conferred award.
stages:
- Enroll
- Progress and Support
- Confer Award
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-workforce-management-9e8d8s
processes:
- processes:process-ao-operate-87q5mk
- processes:process-eo-operate-2jnz85
- processes:process-fa-operate-ycba3k
- processes:process-pr-operate-bbe384
metrics:
- Completion rate
upstream:
- value-stream-apply-to-decide
downstream: []
evidence_sources:
- SRC-015
---

# Admit to Graduate

`value-streams:value-stream-admit-to-graduate-v9jcg3` · **operational** · education · industry-specific

> The student-lifecycle stream from admission through enrollment, progression, to graduation.

**Outcome:** A graduated student with conferred award.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-admit-to-graduate-v9jcg3.yaml`](./value-streams-value-stream-admit-to-graduate-v9jcg3.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Enroll"]
  S2["2. Progress and Support"]
  S3["3. Confer Award"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Enroll** | An offer is accepted. | The student is enrolled. | 2 | 1 | yes |
| 2 | **Progress and Support** | The student is enrolled. | The student completes requirements. | 2 | 2 | yes |
| 3 | **Confer Award** | Requirements are complete. | The award is conferred. | 2 | 1 | yes |

### 1. Enroll

Enroll the admitted student.

| Aspect | Value |
|---|---|
| Entry criterion | An offer is accepted. |
| Exit criterion | The student is enrolled. |
| Outcome | An enrolled student. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Progress and Support

Support academic progression to completion.

| Aspect | Value |
|---|---|
| Entry criterion | The student is enrolled. |
| Exit criterion | The student completes requirements. |
| Outcome | A completed candidature. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-eo-operate-2jnz85` · `processes:process-ao-operate-87q5mk` |

### 3. Confer Award

Confer the award.

| Aspect | Value |
|---|---|
| Entry criterion | Requirements are complete. |
| Exit criterion | The award is conferred. |
| Outcome | A conferred award. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

## Scope boundary

**Entry:** An admission offer is accepted.

**Exit:** The student graduates with a conferred award.

**In scope**

- Admission and enrollment
- Academic progression and support
- Award conferral

**Out of scope** (owned by the named neighbour)

- Research candidature
- Continuing education

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-2jnz85`
- `processes:process-ao-operate-87q5mk`
- `processes:process-fa-operate-ycba3k`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [apply to decide](../value-stream-apply-to-decide-qr36mf/README.md) — Admission decisions are made through the application stream.

**Downstream:** none recorded.

## Measurement

- **Completion rate** (stream-level) — Share of enrolled students graduating within the expected window.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-015 | industry-reference-model | Education and hospitality service chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-081) from the CR-VS-11 industry evidence register extension. Industry-specific chain (education); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
