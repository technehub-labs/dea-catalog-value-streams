---
documentation_generated_from: value-streams-value-stream-loss-to-claim-settlement-bkjege.yaml
id: value-streams:value-stream-loss-to-claim-settlement-bkjege
name: Loss to Claim Settlement
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- insurance
specificity: industry-specific
entry_criterion: A loss is notified.
exit_criterion: The claim is settled and paid.
outcome: A fairly adjusted, settled, and paid claim.
stages:
- Register Loss
- Adjust
- Agree Settlement
- Pay and Close
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-fa-operate-sdppmp
- processes:process-ge-build-mctdgc
- processes:process-ge-operate-zwaes5
- processes:process-pr-operate-bbe384
metrics:
- Claims leakage rate
- Claims frequency rate
upstream:
- value-stream-quote-to-bind
downstream: []
evidence_sources:
- SRC-009
---

# Loss to Claim Settlement

`value-streams:value-stream-loss-to-claim-settlement-bkjege` · **operational** · insurance · industry-specific

> The end-to-end claims stream from first notice of loss through adjustment to claim settlement and payment.

**Outcome:** A fairly adjusted, settled, and paid claim.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-loss-to-claim-settlement-bkjege.yaml`](./value-streams-value-stream-loss-to-claim-settlement-bkjege.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Register Loss"]
  S2["2. Adjust"]
  S3["3. Agree Settlement"]
  S4["4. Pay and Close"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Register Loss** | A loss is notified. | The claim is registered and covered. | 2 | 1 | yes |
| 2 | **Adjust** | The claim is covered. | The adjustment is complete. | 2 | 1 | yes |
| 3 | **Agree Settlement** | The adjustment is complete. | The settlement is agreed. | 2 | 1 | yes |
| 4 | **Pay and Close** | The settlement is agreed. | The claim is paid and closed. | 2 | 1 | yes |

### 1. Register Loss

Register the loss notice and verify coverage.

| Aspect | Value |
|---|---|
| Entry criterion | A loss is notified. |
| Exit criterion | The claim is registered and covered. |
| Outcome | A registered, covered claim. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Adjust

Investigate and adjust the claim valuation.

| Aspect | Value |
|---|---|
| Entry criterion | The claim is covered. |
| Exit criterion | The adjustment is complete. |
| Outcome | A completed adjustment. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 3. Agree Settlement

Agree the settlement with the claimant.

| Aspect | Value |
|---|---|
| Entry criterion | The adjustment is complete. |
| Exit criterion | The settlement is agreed. |
| Outcome | An agreed settlement. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### 4. Pay and Close

Pay the settlement and close the claim.

| Aspect | Value |
|---|---|
| Entry criterion | The settlement is agreed. |
| Exit criterion | The claim is paid and closed. |
| Outcome | A settled, closed claim. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## Scope boundary

**Entry:** A loss is notified.

**Exit:** The claim is settled and paid.

**In scope**

- First notice of loss and coverage verification
- Adjustment and valuation
- Settlement agreement
- Payment and closure

**Out of scope** (owned by the named neighbour)

- Underwriting (Quote to Bind)
- Subrogation and recovery

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-zwaes5`
- `processes:process-ge-build-mctdgc`
- `processes:process-fa-operate-sdppmp`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [quote to bind](../value-stream-quote-to-bind-szgnjc/README.md) — Coverage terms originate at underwriting.

**Downstream:** none recorded.

## Measurement

- **Claims leakage rate** (stage: Pay and Close) — Payment error and leakage as a share of claims cost. → [`dea:metric-claims-leakage-rate`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Claims frequency rate** (stage: Register Loss) — Claims per exposure unit. → [`dea:metric-claims-frequency-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-009 | industry-reference-model | Insurance industry reference models (policy and claims lifecycles, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-030) from the CR-VS-11 industry evidence register extension. Industry-specific chain (insurance); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
