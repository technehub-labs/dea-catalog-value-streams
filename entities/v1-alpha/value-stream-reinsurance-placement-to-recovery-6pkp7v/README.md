---
documentation_generated_from: value-streams-value-stream-reinsurance-placement-to-recovery-6pkp7v.yaml
id: value-streams:value-stream-reinsurance-placement-to-recovery-6pkp7v
name: Reinsurance Placement to Recovery
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- insurance
specificity: industry-specific
entry_criterion: A reinsurance need is identified.
exit_criterion: Recoveries are collected for ceded losses.
outcome: Ceded risk with recoveries collected.
stages:
- Place Cover
- Settle Premium
- Report Losses
- Collect Recovery
capabilities:
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-partner-management-cp3vdb
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-fa-operate-sdppmp
- processes:process-fa-operate-wkqaqp
- processes:process-ge-build-mctdgc
- processes:process-pr-operate-bbe384
metrics:
- Recovery collection cycle time
upstream: []
downstream: []
evidence_sources:
- SRC-009
---

# Reinsurance Placement to Recovery

`value-streams:value-stream-reinsurance-placement-to-recovery-6pkp7v` · **operational** · insurance · industry-specific

> The reinsurance stream from placement negotiation through premium settlement to loss recovery.

**Outcome:** Ceded risk with recoveries collected.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-reinsurance-placement-to-recovery-6pkp7v.yaml`](./value-streams-value-stream-reinsurance-placement-to-recovery-6pkp7v.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Place Cover"]
  S2["2. Settle Premium"]
  S3["3. Report Losses"]
  S4["4. Collect Recovery"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Place Cover** | A need is identified. | The cover is placed. | 2 | 1 | no |
| 2 | **Settle Premium** | The cover is placed. | The contract is executed and premium settled. | 2 | 2 | no |
| 3 | **Report Losses** | A covered loss occurs. | The loss is reported. | 1 | 1 | no |
| 4 | **Collect Recovery** | The loss is reported. | The recovery is collected. | 1 | 1 | no |

### 1. Place Cover

Negotiate and place the reinsurance cover.

| Aspect | Value |
|---|---|
| Entry criterion | A need is identified. |
| Exit criterion | The cover is placed. |
| Outcome | Placed cover. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-partner-management-cp3vdb` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### 2. Settle Premium

Execute the contract and settle premium.

| Aspect | Value |
|---|---|
| Entry criterion | The cover is placed. |
| Exit criterion | The contract is executed and premium settled. |
| Outcome | An executed treaty. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u` · `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-ge-build-mctdgc` · `processes:process-fa-operate-wkqaqp` |

### 3. Report Losses

Report ceded losses to the reinsurer.

| Aspect | Value |
|---|---|
| Entry criterion | A covered loss occurs. |
| Exit criterion | The loss is reported. |
| Outcome | A reported ceded loss. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 4. Collect Recovery

Collect the reinsurance recovery.

| Aspect | Value |
|---|---|
| Entry criterion | The loss is reported. |
| Exit criterion | The recovery is collected. |
| Outcome | A collected recovery. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## Scope boundary

**Entry:** A reinsurance need is identified.

**Exit:** Recoveries are collected for ceded losses.

**In scope**

- Placement negotiation
- Contract execution and premium settlement
- Loss reporting
- Recovery collection

**Out of scope** (owned by the named neighbour)

- Direct underwriting (Quote to Bind)
- Direct claims (Loss to Claim Settlement)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-information-management-6vjgdh`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-build-mctdgc`
- `processes:process-fa-operate-wkqaqp`
- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-sdppmp`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Recovery collection cycle time** (stream-level) — Elapsed time from loss report to collected recovery.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-009 | industry-reference-model | Insurance industry reference models (policy and claims lifecycles, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-034) from the CR-VS-11 industry evidence register extension. Industry-specific chain (insurance); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
