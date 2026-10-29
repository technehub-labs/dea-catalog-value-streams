---
documentation_generated_from: value-streams-value-stream-customs-clearance-to-release-cfgc3b.yaml
id: value-streams:value-stream-customs-clearance-to-release-cfgc3b
name: Customs Clearance to Release
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: governance
industries:
- logistics-transportation
specificity: industry-specific
entry_criterion: A shipment requires customs clearance.
exit_criterion: The cargo is released and duties settled.
outcome: Customs-released cargo with duties settled.
stages:
- File Declaration
- Assess and Inspect
- Release and Settle
capabilities:
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-regulation-management-gya4d8
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-fa-operate-8vqvkk
- processes:process-fa-operate-g9zpnq
- processes:process-ge-operate-zwaes5
metrics:
- Customs clearance cycle time
upstream: []
downstream: []
evidence_sources:
- SRC-016
---

# Customs Clearance to Release

`value-streams:value-stream-customs-clearance-to-release-cfgc3b` · **governance** · logistics-transportation · industry-specific

> The customs stream from declaration filing through assessment and inspection to released cargo.

**Outcome:** Customs-released cargo with duties settled.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-customs-clearance-to-release-cfgc3b.yaml`](./value-streams-value-stream-customs-clearance-to-release-cfgc3b.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. File Declaration"]
  S2["2. Assess and Inspect"]
  S3["3. Release and Settle"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **File Declaration** | A shipment requires clearance. | The declaration is filed. | 2 | 1 | no |
| 2 | **Assess and Inspect** | The declaration is filed. | Assessment completes. | 2 | 1 | no |
| 3 | **Release and Settle** | Assessment completes. | The cargo is released. | 2 | 1 | no |

### 1. File Declaration

File the customs declaration.

| Aspect | Value |
|---|---|
| Entry criterion | A shipment requires clearance. |
| Exit criterion | The declaration is filed. |
| Outcome | A filed declaration. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-8vqvkk` |

### 2. Assess and Inspect

Assess and inspect if selected.

| Aspect | Value |
|---|---|
| Entry criterion | The declaration is filed. |
| Exit criterion | Assessment completes. |
| Outcome | A completed assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 3. Release and Settle

Release the cargo and settle duties.

| Aspect | Value |
|---|---|
| Entry criterion | Assessment completes. |
| Exit criterion | The cargo is released. |
| Outcome | Released cargo. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

## Scope boundary

**Entry:** A shipment requires customs clearance.

**Exit:** The cargo is released and duties settled.

**In scope**

- Declaration filing
- Assessment and inspection
- Release and duty settlement

**Out of scope** (owned by the named neighbour)

- Freight movement (Ship to Consignee)
- Trade compliance governance

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-operations-management-pm3w8k`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-8vqvkk`
- `processes:process-ge-operate-zwaes5`
- `processes:process-fa-operate-g9zpnq`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Customs clearance cycle time** (stage: Release and Settle) — Elapsed time from filing to release. → [`dea:metric-customs-clearance-cycle-time`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-016 | industry-reference-model | Manufacturing and logistics reference models (SCOR-style category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-067) from the CR-VS-11 industry evidence register extension. Industry-specific chain (logistics-transportation); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
