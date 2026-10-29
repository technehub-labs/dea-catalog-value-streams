---
documentation_generated_from: value-streams-value-stream-surrender-to-payout-vf67kv.yaml
id: value-streams:value-stream-surrender-to-payout-vf67kv
name: Surrender to Payout
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- insurance
specificity: industry-specific
entry_criterion: A policyholder requests surrender.
exit_criterion: The surrender value is paid and the contract closed.
outcome: A correctly computed surrender paid and the contract closed.
stages:
- Validate Request
- Compute Value
- Pay and Close
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-legal-matter-management-zzbd2u
processes:
- processes:process-fa-operate-g9zpnq
- processes:process-fa-operate-sdppmp
- processes:process-pr-operate-bbe384
metrics:
- Surrender processing cycle time
upstream: []
downstream: []
evidence_sources:
- SRC-009
---

# Surrender to Payout

`value-streams:value-stream-surrender-to-payout-vf67kv` · **operational** · insurance · industry-specific

> The life-insurance surrender stream from surrender request through surrender-value computation to payout and closure.

**Outcome:** A correctly computed surrender paid and the contract closed.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-surrender-to-payout-vf67kv.yaml`](./value-streams-value-stream-surrender-to-payout-vf67kv.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Validate Request"]
  S2["2. Compute Value"]
  S3["3. Pay and Close"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Validate Request** | A request is received. | The request is validated. | 2 | 1 | yes |
| 2 | **Compute Value** | The request is validated. | The value is computed and communicated. | 2 | 1 | yes |
| 3 | **Pay and Close** | The value is accepted. | The payout is made and the contract closed. | 2 | 1 | yes |

### 1. Validate Request

Validate the surrender request and contract status.

| Aspect | Value |
|---|---|
| Entry criterion | A request is received. |
| Exit criterion | The request is validated. |
| Outcome | A validated request. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Compute Value

Compute the surrender value.

| Aspect | Value |
|---|---|
| Entry criterion | The request is validated. |
| Exit criterion | The value is computed and communicated. |
| Outcome | A communicated surrender value. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### 3. Pay and Close

Pay the surrender and close the contract.

| Aspect | Value |
|---|---|
| Entry criterion | The value is accepted. |
| Exit criterion | The payout is made and the contract closed. |
| Outcome | A closed contract with paid surrender. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## Scope boundary

**Entry:** A policyholder requests surrender.

**Exit:** The surrender value is paid and the contract closed.

**In scope**

- Surrender request and validation
- Surrender-value computation
- Payout and closure

**Out of scope** (owned by the named neighbour)

- Maturity settlement
- Policy loans

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-sdppmp`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Surrender processing cycle time** (stream-level) — Elapsed days from request to payout.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-009 | industry-reference-model | Insurance industry reference models (policy and claims lifecycles, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-035) from the CR-VS-11 industry evidence register extension. Industry-specific chain (insurance); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
