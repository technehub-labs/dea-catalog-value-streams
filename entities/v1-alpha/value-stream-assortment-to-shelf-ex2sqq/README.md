---
documentation_generated_from: value-streams-value-stream-assortment-to-shelf-ex2sqq.yaml
id: value-streams:value-stream-assortment-to-shelf-ex2sqq
name: Assortment to Shelf
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- retail-commerce
specificity: industry-specific
entry_criterion: An assortment planning cycle opens.
exit_criterion: The assortment is in stock at planned levels.
outcome: Planned assortment in stock and on shelf.
stages:
- Plan Assortment
- Buy
- Allocate and Replenish
- Maintain In-Stock
capabilities:
- capabilities:capability-enterprise-performance-management-5fxren
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-marketing-xmc539
- capabilities:capability-offering-management-6egkc8
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-sourcing-and-procurement-esucp4
- capabilities:capability-supplier-management-d6fuj4
processes:
- processes:process-eo-operate-2jnz85
- processes:process-eo-operate-vzcxx7
- processes:process-eo-operate-zh9m57
- processes:process-eo-operate-zwzmbd
- processes:process-fa-conceive-4uqqvg
- processes:process-pv-operate-cau4gv
metrics:
- On-shelf availability
upstream:
- value-stream-plan-to-forecast
downstream: []
evidence_sources:
- SRC-013
---

# Assortment to Shelf

`value-streams:value-stream-assortment-to-shelf-ex2sqq` · **operational** · retail-commerce · industry-specific

> The merchandising stream from assortment planning through supplier engagement to in-stock shelf availability.

**Outcome:** Planned assortment in stock and on shelf.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-assortment-to-shelf-ex2sqq.yaml`](./value-streams-value-stream-assortment-to-shelf-ex2sqq.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Plan Assortment"]
  S2["2. Buy"]
  S3["3. Allocate and Replenish"]
  S4["4. Maintain In-Stock"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Plan Assortment** | A planning cycle opens. | The assortment plan is approved. | 2 | 2 | no |
| 2 | **Buy** | The plan is approved. | Buys are placed. | 2 | 1 | no |
| 3 | **Allocate and Replenish** | Buys are placed. | Stores are allocated and replenished. | 2 | 2 | no |
| 4 | **Maintain In-Stock** | Stores are replenished. | The assortment is in stock at plan. | 2 | 1 | no |

### 1. Plan Assortment

Plan the assortment and range.

| Aspect | Value |
|---|---|
| Entry criterion | A planning cycle opens. |
| Exit criterion | The assortment plan is approved. |
| Outcome | An approved plan. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8` · `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pv-operate-cau4gv` · `processes:process-fa-conceive-4uqqvg` |

### 2. Buy

Negotiate with suppliers and place buys.

| Aspect | Value |
|---|---|
| Entry criterion | The plan is approved. |
| Exit criterion | Buys are placed. |
| Outcome | Placed buys. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-sourcing-and-procurement-esucp4` · `capabilities:capability-supplier-management-d6fuj4` |
| Realizing processes | `processes:process-eo-operate-vzcxx7` |

### 3. Allocate and Replenish

Allocate stock and drive replenishment.

| Aspect | Value |
|---|---|
| Entry criterion | Buys are placed. |
| Exit criterion | Stores are allocated and replenished. |
| Outcome | Replenished stores. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` · `processes:process-eo-operate-zh9m57` |

### 4. Maintain In-Stock

Maintain in-stock availability on shelf.

| Aspect | Value |
|---|---|
| Entry criterion | Stores are replenished. |
| Exit criterion | The assortment is in stock at plan. |
| Outcome | In-stock assortment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## Scope boundary

**Entry:** An assortment planning cycle opens.

**Exit:** The assortment is in stock at planned levels.

**In scope**

- Assortment and range planning
- Supplier negotiation and buying
- Allocation and replenishment
- In-stock maintenance

**Out of scope** (owned by the named neighbour)

- Store operations
- Promotions (Marketing)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-sourcing-and-procurement-esucp4`
- `capabilities:capability-supplier-management-d6fuj4`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pv-operate-cau4gv`
- `processes:process-fa-conceive-4uqqvg`
- `processes:process-eo-operate-vzcxx7`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-zh9m57`
- `processes:process-eo-operate-2jnz85`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [plan to forecast](../value-stream-plan-to-forecast-89vb4q/README.md) — The ratified demand plan drives assortment planning.

**Downstream:** none recorded.

## Measurement

- **On-shelf availability** (stream-level) — Share of planned assortment in stock on shelf.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-013 | industry-reference-model | Retail / consumer-commerce chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-058) from the CR-VS-11 industry evidence register extension. Industry-specific chain (retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
