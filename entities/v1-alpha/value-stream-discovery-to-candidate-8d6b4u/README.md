---
documentation_generated_from: value-streams-value-stream-discovery-to-candidate-8d6b4u.yaml
id: value-streams:value-stream-discovery-to-candidate-8d6b4u
name: Discovery to Candidate
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: development
industries:
- life-sciences
specificity: industry-specific
entry_criterion: A target is identified.
exit_criterion: A candidate is nominated for development.
outcome: A nominated development candidate.
stages:
- Validate Target
- Screen
- Nominate Candidate
capabilities:
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-idea-management-86dckf
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-offering-management-6egkc8
- capabilities:capability-operations-management-pm3w8k
processes:
- processes:process-eo-operate-2jnz85
- processes:process-eo-operate-44jsrp
- processes:process-pv-conceive-kps544
- processes:process-pv-design-8v4k89
metrics:
- Discovery project attrition
upstream:
- value-stream-concept-to-launch
downstream: []
evidence_sources:
- SRC-018
---

# Discovery to Candidate

`value-streams:value-stream-discovery-to-candidate-8d6b4u` · **development** · life-sciences · industry-specific

> The research stream from target identification through screening to a nominated development candidate.

**Outcome:** A nominated development candidate.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-discovery-to-candidate-8d6b4u.yaml`](./value-streams-value-stream-discovery-to-candidate-8d6b4u.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Validate Target"]
  S2["2. Screen"]
  S3["3. Nominate Candidate"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Validate Target** | A target is identified. | The target is validated. | 2 | 1 | no |
| 2 | **Screen** | The target is validated. | Screening is complete. | 2 | 2 | no |
| 3 | **Nominate Candidate** | Screening is complete. | The candidate is nominated. | 2 | 1 | no |

### 1. Validate Target

Validate the identified target.

| Aspect | Value |
|---|---|
| Entry criterion | A target is identified. |
| Exit criterion | The target is validated. |
| Outcome | A validated target. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d` · `capabilities:capability-idea-management-86dckf` |
| Realizing processes | `processes:process-pv-conceive-kps544` |

### 2. Screen

Screen for active candidates.

| Aspect | Value |
|---|---|
| Entry criterion | The target is validated. |
| Exit criterion | Screening is complete. |
| Outcome | Screened candidates. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-2jnz85` · `processes:process-eo-operate-44jsrp` |

### 3. Nominate Candidate

Nominate the development candidate.

| Aspect | Value |
|---|---|
| Entry criterion | Screening is complete. |
| Exit criterion | The candidate is nominated. |
| Outcome | A nominated candidate. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8` · `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-pv-design-8v4k89` |

## Scope boundary

**Entry:** A target is identified.

**Exit:** A candidate is nominated for development.

**In scope**

- Target identification and validation
- Screening
- Candidate nomination

**Out of scope** (owned by the named neighbour)

- Clinical development (Trial to Readout)
- Research platform governance

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-idea-management-86dckf`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pv-conceive-kps544`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-44jsrp`
- `processes:process-pv-design-8v4k89`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [concept to launch](../value-stream-concept-to-launch-nhvatv/README.md) — The life-sciences specialization of development intake.

**Downstream:** none recorded.

## Measurement

- **Discovery project attrition** (stream-level) — Share of targets reaching candidate nomination.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-018 | industry-reference-model | Life-sciences reference chains (public GxP/ICH category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-101) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
