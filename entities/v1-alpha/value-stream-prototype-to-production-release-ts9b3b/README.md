---
documentation_generated_from: value-streams-value-stream-prototype-to-production-release-ts9b3b.yaml
id: value-streams:value-stream-prototype-to-production-release-ts9b3b
name: Prototype to Production Release
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: development
industries:
- manufacturing
specificity: industry-specific
entry_criterion: A prototype is approved.
exit_criterion: Production is released with a validated process.
outcome: A production-released product with validated process.
stages:
- Design Process
- Pilot and Validate
- Release Production
capabilities:
- capabilities:capability-offering-management-6egkc8
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-risk-management-h9uxdw
- capabilities:capability-technology-management-maus5n
processes:
- processes:process-eo-build-j9z3q4
- processes:process-eo-design-6j5mxp
- processes:process-eo-operate-44jsrp
- processes:process-eo-operate-xud3hs
metrics:
- Time to production release
upstream:
- value-stream-concept-to-launch
downstream:
- value-stream-make-to-stock-release
evidence_sources:
- SRC-016
---

# Prototype to Production Release

`value-streams:value-stream-prototype-to-production-release-ts9b3b` · **development** · manufacturing · industry-specific

> The industrialization stream from approved prototype through process design to production release.

**Outcome:** A production-released product with validated process.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-prototype-to-production-release-ts9b3b.yaml`](./value-streams-value-stream-prototype-to-production-release-ts9b3b.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Design Process"]
  S2["2. Pilot and Validate"]
  S3["3. Release Production"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Design Process** | A prototype is approved. | The process is designed. | 2 | 1 | no |
| 2 | **Pilot and Validate** | The process is designed. | The process is validated. | 2 | 2 | no |
| 3 | **Release Production** | The process is validated. | Production is released. | 2 | 1 | no |

### 1. Design Process

Design the manufacturing process.

| Aspect | Value |
|---|---|
| Entry criterion | A prototype is approved. |
| Exit criterion | The process is designed. |
| Outcome | A designed process. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n` · `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-eo-design-6j5mxp` |

### 2. Pilot and Validate

Run the pilot and validate the process.

| Aspect | Value |
|---|---|
| Entry criterion | The process is designed. |
| Exit criterion | The process is validated. |
| Outcome | A validated process. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-operate-xud3hs` · `processes:process-eo-operate-44jsrp` |

### 3. Release Production

Release to production.

| Aspect | Value |
|---|---|
| Entry criterion | The process is validated. |
| Exit criterion | Production is released. |
| Outcome | A released production. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

## Scope boundary

**Entry:** A prototype is approved.

**Exit:** Production is released with a validated process.

**In scope**

- Process design
- Pilot run and validation
- Production release

**Out of scope** (owned by the named neighbour)

- Product development (Concept to Launch)
- Volume production (Make to Stock Release)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-design-6j5mxp`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-build-j9z3q4`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [concept to launch](../value-stream-concept-to-launch-nhvatv/README.md) — Product development approves the prototype.

**Downstream** (this stream's exit feeds their entry):

- [make to stock release](../value-stream-make-to-stock-release-xuv4fq/README.md) — Released production runs through standard production.

## Measurement

- **Time to production release** (stream-level) — Elapsed time from prototype approval to release.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-016 | industry-reference-model | Manufacturing and logistics reference models (SCOR-style category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-054) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
