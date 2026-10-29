# Assortment to Shelf

Admitted Value Stream record (`value-streams:value-stream-assortment-to-shelf-ex2sqq`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-assortment-to-shelf-ex2sqq` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | retail-commerce · industry-specific |
| Record | [`value-streams-value-stream-assortment-to-shelf-ex2sqq.yaml`](./value-streams-value-stream-assortment-to-shelf-ex2sqq.yaml) — authoritative |

## 2. Definition

> The merchandising stream from assortment planning through supplier engagement to in-stock shelf availability.

## 3. Value proposition and served party

**Outcome:** Planned assortment in stock and on shelf.

## 4. Stream boundary

**Entry criterion:** An assortment planning cycle opens.

**Exit criterion:** The assortment is in stock at planned levels.

**In scope** (from the record's `scope.includes`):

- Assortment and range planning
- Supplier negotiation and buying
- Allocation and replenishment
- In-stock maintenance

**Out of scope** (each concern owned by the named neighbour):

- Store operations
- Promotions (Marketing)

## 5. Value stages

Assortment to Shelf decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Plan Assortment

Plan the assortment and range.

| Aspect | Value |
|---|---|
| Entry criterion | A planning cycle opens. |
| Exit criterion | The assortment plan is approved. |
| Outcome | An approved plan. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8`, `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pv-operate-cau4gv`, `processes:process-fa-conceive-4uqqvg` |

### Stage 2: Buy

Negotiate with suppliers and place buys.

| Aspect | Value |
|---|---|
| Entry criterion | The plan is approved. |
| Exit criterion | Buys are placed. |
| Outcome | Placed buys. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-sourcing-and-procurement-esucp4`, `capabilities:capability-supplier-management-d6fuj4` |
| Realizing processes | `processes:process-eo-operate-vzcxx7` |

### Stage 3: Allocate and Replenish

Allocate stock and drive replenishment.

| Aspect | Value |
|---|---|
| Entry criterion | Buys are placed. |
| Exit criterion | Stores are allocated and replenished. |
| Outcome | Replenished stores. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-zwzmbd`, `processes:process-eo-operate-zh9m57` |

### Stage 4: Maintain In-Stock

Maintain in-stock availability on shelf.

| Aspect | Value |
|---|---|
| Entry criterion | Stores are replenished. |
| Exit criterion | The assortment is in stock at plan. |
| Outcome | In-stock assortment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-sourcing-and-procurement-esucp4`
- `capabilities:capability-supplier-management-d6fuj4`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pv-operate-cau4gv`
- `processes:process-fa-conceive-4uqqvg`
- `processes:process-eo-operate-vzcxx7`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-zh9m57`
- `processes:process-eo-operate-2jnz85`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-plan-to-forecast` — The ratified demand plan drives assortment planning.

**Downstream streams:** none recorded.

## 8. Measurement

- **On-shelf availability** (stream-level) — Share of planned assortment in stock on shelf.

## 9. Evidence and admission

**Evidence sources:** SRC-013 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-058) from the CR-VS-11 industry evidence register extension. Industry-specific chain (retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
