# Make to Stock Release

Admitted Value Stream record (`value-streams:value-stream-make-to-stock-release-xuv4fq`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-make-to-stock-release-xuv4fq` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | manufacturing · industry-specific |
| Record | [`value-streams-value-stream-make-to-stock-release-xuv4fq.yaml`](./value-streams-value-stream-make-to-stock-release-xuv4fq.yaml) — authoritative |

## 2. Definition

> The production stream from stock-replenishment signal through production and release to finished-stock availability.

## 3. Value proposition and served party

**Outcome:** Finished stock available to promise.

## 4. Stream boundary

**Entry criterion:** A replenishment signal is raised.

**Exit criterion:** Finished stock is received and available.

**In scope** (from the record's `scope.includes`):

- Production order release
- Production execution
- Quality release to stock

**Out of scope** (each concern owned by the named neighbour):

- Demand planning (Plan to Forecast)
- Distribution (Ship to Consignee)

## 5. Value stages

Make to Stock Release decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Release Order

Release the production order.

| Aspect | Value |
|---|---|
| Entry criterion | A replenishment signal is raised. |
| Exit criterion | The order is released. |
| Outcome | A released order. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-build-2pkz5n`, `processes:process-eo-operate-xud3hs` |

### Stage 2: Produce

Execute production.

| Aspect | Value |
|---|---|
| Entry criterion | The order is released. |
| Exit criterion | Production is complete. |
| Outcome | Completed production. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-xud3hs` |

### Stage 3: Release to Stock

Quality-release and receive into finished stock.

| Aspect | Value |
|---|---|
| Entry criterion | Production is complete. |
| Exit criterion | Stock is available. |
| Outcome | Available stock. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp`, `processes:process-eo-operate-zwzmbd` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-risk-management-h9uxdw`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-build-2pkz5n`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-zwzmbd`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-plan-to-deliver` — The stream refines the generic production chain for stock replenishment.

**Downstream streams:** none recorded.

## 8. Measurement

- **First pass yield** (stage: Release to Stock) — Share of output passing quality first time. → [`dea:metric-first-pass-yield`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-051) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
