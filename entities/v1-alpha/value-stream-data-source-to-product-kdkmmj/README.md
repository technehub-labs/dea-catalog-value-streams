---
documentation_generated_from: value-streams-value-stream-data-source-to-product-kdkmmj.yaml
id: value-streams:value-stream-data-source-to-product-kdkmmj
name: Data Source to Product
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- technology
specificity: industry-specific
entry_criterion: A source or use case is approved.
exit_criterion: The data product is live and consumed.
outcome: A consumed, SLA-backed data product.
stages:
- Onboard Source
- Build Pipeline
- Publish Product
- Support Consumption
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-offering-management-6egkc8
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-technology-enablement-y6nkws
processes:
- processes:process-eo-build-j9z3q4
- processes:process-eo-operate-2jnz85
- processes:process-eo-operate-xud3hs
- processes:process-pv-operate-cau4gv
metrics:
- Data product freshness SLA
upstream: []
downstream: []
evidence_sources:
- SRC-019
---

# Data Source to Product

`value-streams:value-stream-data-source-to-product-kdkmmj` · **operational** · technology · industry-specific

> The data-product stream from source onboarding through pipeline build to a consumed, SLA-backed data product.

**Outcome:** A consumed, SLA-backed data product.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-data-source-to-product-kdkmmj.yaml`](./value-streams-value-stream-data-source-to-product-kdkmmj.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Onboard Source"]
  S2["2. Build Pipeline"]
  S3["3. Publish Product"]
  S4["4. Support Consumption"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Onboard Source** | A source is approved. | The source is onboarded. | 2 | 1 | no |
| 2 | **Build Pipeline** | The source is onboarded. | The pipeline is built. | 1 | 1 | no |
| 3 | **Publish Product** | The pipeline is built. | The product is published. | 2 | 1 | no |
| 4 | **Support Consumption** | The product is published. | The product is consumed. | 2 | 1 | no |

### 1. Onboard Source

Onboard the data source.

| Aspect | Value |
|---|---|
| Entry criterion | A source is approved. |
| Exit criterion | The source is onboarded. |
| Outcome | An onboarded source. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### 2. Build Pipeline

Build the data pipeline.

| Aspect | Value |
|---|---|
| Entry criterion | The source is onboarded. |
| Exit criterion | The pipeline is built. |
| Outcome | A built pipeline. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-operate-xud3hs` |

### 3. Publish Product

Publish the data product with SLA.

| Aspect | Value |
|---|---|
| Entry criterion | The pipeline is built. |
| Exit criterion | The product is published. |
| Outcome | A published product. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-pv-operate-cau4gv` |

### 4. Support Consumption

Support consumer onboarding and usage.

| Aspect | Value |
|---|---|
| Entry criterion | The product is published. |
| Exit criterion | The product is consumed. |
| Outcome | A consumed product. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## Scope boundary

**Entry:** A source or use case is approved.

**Exit:** The data product is live and consumed.

**In scope**

- Source onboarding
- Pipeline build
- Product publication
- Consumption support

**Out of scope** (owned by the named neighbour)

- Model development (Model to Deployment)
- Enterprise reporting (Record to Report)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-xud3hs`
- `processes:process-pv-operate-cau4gv`
- `processes:process-eo-operate-2jnz85`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Data product freshness SLA** (stream-level) — Share of refreshes meeting the freshness SLA.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-019 | industry-reference-model | Technology / SaaS product chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-110) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
