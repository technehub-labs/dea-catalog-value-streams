---
documentation_generated_from: value-streams-value-stream-inspect-to-disposition-uu3grx.yaml
id: value-streams:value-stream-inspect-to-disposition-uu3grx
name: Inspect to Disposition
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: governance
industries:
- manufacturing
- logistics-transportation
specificity: industry-specific
entry_criterion: An inspection is triggered (incoming, in-process, or final).
exit_criterion: The lot is dispositioned.
outcome: A documented disposition for every inspected lot.
stages:
- Inspect
- Evaluate
- Disposition
- Document
capabilities:
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-eo-operate-44jsrp
- processes:process-fa-operate-4xn4d6
- processes:process-ge-operate-zwaes5
metrics:
- Lot rejection rate
upstream: []
downstream: []
evidence_sources:
- SRC-016
---

# Inspect to Disposition

`value-streams:value-stream-inspect-to-disposition-uu3grx` · **governance** · manufacturing, logistics-transportation · industry-specific

> The quality stream from inspection trigger through evaluation to disposition of the material.

**Outcome:** A documented disposition for every inspected lot.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-inspect-to-disposition-uu3grx.yaml`](./value-streams-value-stream-inspect-to-disposition-uu3grx.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Inspect"]
  S2["2. Evaluate"]
  S3["3. Disposition"]
  S4["4. Document"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Inspect** | An inspection is triggered. | The inspection is complete. | 2 | 1 | no |
| 2 | **Evaluate** | The inspection is complete. | The evaluation is complete. | 2 | 1 | no |
| 3 | **Disposition** | The evaluation is complete. | The disposition is decided. | 2 | 1 | no |
| 4 | **Document** | The disposition is decided. | Documentation is complete. | 1 | 1 | no |

### 1. Inspect

Sample and inspect the lot.

| Aspect | Value |
|---|---|
| Entry criterion | An inspection is triggered. |
| Exit criterion | The inspection is complete. |
| Outcome | Inspection results. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### 2. Evaluate

Evaluate results against specification.

| Aspect | Value |
|---|---|
| Entry criterion | The inspection is complete. |
| Exit criterion | The evaluation is complete. |
| Outcome | An evaluation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### 3. Disposition

Decide the lot disposition.

| Aspect | Value |
|---|---|
| Entry criterion | The evaluation is complete. |
| Exit criterion | The disposition is decided. |
| Outcome | A disposition. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 4. Document

Document and communicate the disposition.

| Aspect | Value |
|---|---|
| Entry criterion | The disposition is decided. |
| Exit criterion | Documentation is complete. |
| Outcome | Documented disposition. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-4xn4d6` |

## Scope boundary

**Entry:** An inspection is triggered (incoming, in-process, or final).

**Exit:** The lot is dispositioned.

**In scope**

- Sampling and inspection
- Evaluation against specification
- Disposition decision
- Documentation

**Out of scope** (owned by the named neighbour)

- Supplier quality (Procure to Pay receipt leg)
- Warranty claims

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-44jsrp`
- `processes:process-ge-operate-zwaes5`
- `processes:process-fa-operate-4xn4d6`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Lot rejection rate** (stream-level) — Share of inspected lots rejected.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-016 | industry-reference-model | Manufacturing and logistics reference models (SCOR-style category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-052) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing, logistics-transportation); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
