---
documentation_generated_from: value-streams-value-stream-make-to-stock-release-xuv4fq.yaml
id: value-streams:value-stream-make-to-stock-release-xuv4fq
name: Make to Stock Release
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- manufacturing
specificity: industry-specific
entry_criterion: A replenishment signal is raised.
exit_criterion: Finished stock is received and available.
outcome: Finished stock available to promise.
stages:
- Release Order
- Produce
- Release to Stock
capabilities:
- capabilities:capability-enterprise-performance-management-5fxren
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-eo-operate-44jsrp
- processes:process-eo-operate-xud3hs
- processes:process-eo-operate-zwzmbd
- processes:process-sd-build-2pkz5n
metrics:
- First pass yield
upstream:
- value-stream-plan-to-deliver
downstream: []
evidence_sources:
- SRC-016
---

# Make to Stock Release

`value-streams:value-stream-make-to-stock-release-xuv4fq` · **operational** · manufacturing · industry-specific

> The production stream from stock-replenishment signal through production and release to finished-stock availability.

**Outcome:** Finished stock available to promise.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-make-to-stock-release-xuv4fq.yaml`](./value-streams-value-stream-make-to-stock-release-xuv4fq.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Release Order"]
  S2["2. Produce"]
  S3["3. Release to Stock"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Release Order** | A replenishment signal is raised. | The order is released. | 2 | 2 | no |
| 2 | **Produce** | The order is released. | Production is complete. | 1 | 1 | no |
| 3 | **Release to Stock** | Production is complete. | Stock is available. | 2 | 2 | no |

### 1. Release Order

Release the production order.

| Aspect | Value |
|---|---|
| Entry criterion | A replenishment signal is raised. |
| Exit criterion | The order is released. |
| Outcome | A released order. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-build-2pkz5n` · `processes:process-eo-operate-xud3hs` |

### 2. Produce

Execute production.

| Aspect | Value |
|---|---|
| Entry criterion | The order is released. |
| Exit criterion | Production is complete. |
| Outcome | Completed production. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-xud3hs` |

### 3. Release to Stock

Quality-release and receive into finished stock.

| Aspect | Value |
|---|---|
| Entry criterion | Production is complete. |
| Exit criterion | Stock is available. |
| Outcome | Available stock. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` · `processes:process-eo-operate-zwzmbd` |

## Scope boundary

**Entry:** A replenishment signal is raised.

**Exit:** Finished stock is received and available.

**In scope**

- Production order release
- Production execution
- Quality release to stock

**Out of scope** (owned by the named neighbour)

- Demand planning (Plan to Forecast)
- Distribution (Ship to Consignee)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-risk-management-h9uxdw`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-build-2pkz5n`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-zwzmbd`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [plan to deliver](../value-stream-plan-to-deliver-smmwpx/README.md) — The stream refines the generic production chain for stock replenishment.

**Downstream:** none recorded.

## Measurement

- **First pass yield** (stage: Release to Stock) — Share of output passing quality first time. → [`dea:metric-first-pass-yield`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-016 | industry-reference-model | Manufacturing and logistics reference models (SCOR-style category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-051) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
