# Data Source to Product

Admitted Value Stream record (`value-streams:value-stream-data-source-to-product-kdkmmj`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-data-source-to-product-kdkmmj` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | technology · industry-specific |
| Record | [`value-streams-value-stream-data-source-to-product-kdkmmj.yaml`](./value-streams-value-stream-data-source-to-product-kdkmmj.yaml) — authoritative |

## 2. Definition

> The data-product stream from source onboarding through pipeline build to a consumed, SLA-backed data product.

## 3. Value proposition and served party

**Outcome:** A consumed, SLA-backed data product.

## 4. Stream boundary

**Entry criterion:** A source or use case is approved.

**Exit criterion:** The data product is live and consumed.

**In scope** (from the record's `scope.includes`):

- Source onboarding
- Pipeline build
- Product publication
- Consumption support

**Out of scope** (each concern owned by the named neighbour):

- Model development (Model to Deployment)
- Enterprise reporting (Record to Report)

## 5. Value stages

Data Source to Product decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Onboard Source

Onboard the data source.

| Aspect | Value |
|---|---|
| Entry criterion | A source is approved. |
| Exit criterion | The source is onboarded. |
| Outcome | An onboarded source. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### Stage 2: Build Pipeline

Build the data pipeline.

| Aspect | Value |
|---|---|
| Entry criterion | The source is onboarded. |
| Exit criterion | The pipeline is built. |
| Outcome | A built pipeline. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-operate-xud3hs` |

### Stage 3: Publish Product

Publish the data product with SLA.

| Aspect | Value |
|---|---|
| Entry criterion | The pipeline is built. |
| Exit criterion | The product is published. |
| Outcome | A published product. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-pv-operate-cau4gv` |

### Stage 4: Support Consumption

Support consumer onboarding and usage.

| Aspect | Value |
|---|---|
| Entry criterion | The product is published. |
| Exit criterion | The product is consumed. |
| Outcome | A consumed product. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-xud3hs`
- `processes:process-pv-operate-cau4gv`
- `processes:process-eo-operate-2jnz85`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Data product freshness SLA** (stream-level) — Share of refreshes meeting the freshness SLA.

## 9. Evidence and admission

**Evidence sources:** SRC-019 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-110) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
