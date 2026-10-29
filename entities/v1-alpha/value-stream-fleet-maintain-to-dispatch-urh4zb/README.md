# Fleet Maintain to Dispatch

Admitted Value Stream record (`value-streams:value-stream-fleet-maintain-to-dispatch-urh4zb`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-fleet-maintain-to-dispatch-urh4zb` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | logistics-transportation · industry-specific |
| Record | [`value-streams-value-stream-fleet-maintain-to-dispatch-urh4zb.yaml`](./value-streams-value-stream-fleet-maintain-to-dispatch-urh4zb.yaml) — authoritative |

## 2. Definition

> The fleet stream from maintenance completion through roadworthiness to dispatchable vehicle status.

## 3. Value proposition and served party

**Outcome:** A roadworthy, dispatchable vehicle.

## 4. Stream boundary

**Entry criterion:** A vehicle completes maintenance.

**Exit criterion:** The vehicle is dispatched on a revenue movement.

**In scope** (from the record's `scope.includes`):

- Roadworthiness certification
- Dispatch planning
- Dispatch

**Out of scope** (each concern owned by the named neighbour):

- Linehaul operations (Ship to Consignee)
- Fleet acquisition (Acquire to Retire)

## 5. Value stages

Fleet Maintain to Dispatch decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Certify Roadworthy

Certify the vehicle roadworthy.

| Aspect | Value |
|---|---|
| Entry criterion | Maintenance completes. |
| Exit criterion | The vehicle is certified. |
| Outcome | A certified vehicle. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 2: Plan Dispatch

Plan the vehicle's next movement.

| Aspect | Value |
|---|---|
| Entry criterion | The vehicle is certified. |
| Exit criterion | The movement is planned. |
| Outcome | A planned movement. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-build-2pkz5n` |

### Stage 3: Dispatch

Dispatch the vehicle.

| Aspect | Value |
|---|---|
| Entry criterion | The movement is planned. |
| Exit criterion | The vehicle is dispatched. |
| Outcome | A dispatched vehicle. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-44jsrp`
- `processes:process-sd-build-2pkz5n`
- `processes:process-eo-operate-zh9m57`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-acquire-to-retire` — Vehicles live in the asset lifecycle.

**Downstream streams:** none recorded.

## 8. Measurement

- **Fleet utilization** (stream-level) — Share of available vehicle time on revenue movements.

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-069) from the CR-VS-11 industry evidence register extension. Industry-specific chain (logistics-transportation); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
