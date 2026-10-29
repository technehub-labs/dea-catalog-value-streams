# Promotion Plan to Execution

Admitted Value Stream record (`value-streams:value-stream-promotion-plan-to-execution-j73nkj`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-promotion-plan-to-execution-j73nkj` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | retail-commerce · industry-specific |
| Record | [`value-streams-value-stream-promotion-plan-to-execution-j73nkj.yaml`](./value-streams-value-stream-promotion-plan-to-execution-j73nkj.yaml) — authoritative |

## 2. Definition

> The promotions stream from promotion design through setup to executed promotion with measured lift.

## 3. Value proposition and served party

**Outcome:** An executed promotion with measured performance.

## 4. Stream boundary

**Entry criterion:** A promotion is designed and approved.

**Exit criterion:** The promotion is executed and its lift measured.

**In scope** (from the record's `scope.includes`):

- Promotion design
- Setup and pricing
- Execution
- Measurement

**Out of scope** (each concern owned by the named neighbour):

- Everyday pricing
- Loyalty program management

## 5. Value stages

Promotion Plan to Execution decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Design Promotion

Design the promotion mechanics.

| Aspect | Value |
|---|---|
| Entry criterion | A promotion is approved for design. |
| Exit criterion | The promotion is designed. |
| Outcome | A designed promotion. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pr-design-j6fakx` |

### Stage 2: Set Up

Set up pricing, media, and stock for the promotion.

| Aspect | Value |
|---|---|
| Entry criterion | The promotion is designed. |
| Exit criterion | Setup is complete. |
| Outcome | A staged promotion. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-marketing-xmc539`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-build-nygvw7` |

### Stage 3: Execute

Run the promotion in market.

| Aspect | Value |
|---|---|
| Entry criterion | Setup is complete. |
| Exit criterion | The promotion runs to completion. |
| Outcome | An executed promotion. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 4: Measure Lift

Measure the promotion's lift and effectiveness.

| Aspect | Value |
|---|---|
| Entry criterion | The promotion completes. |
| Exit criterion | Performance is measured. |
| Outcome | Measured performance. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-design-j6fakx`
- `processes:process-pr-build-nygvw7`
- `processes:process-eo-operate-2jnz85`
- `processes:process-sd-operate-ucxpz4`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Promotion lift** (stream-level) — Incremental sales attributable to the promotion.

## 9. Evidence and admission

**Evidence sources:** SRC-013 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-061) from the CR-VS-11 industry evidence register extension. Industry-specific chain (retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
