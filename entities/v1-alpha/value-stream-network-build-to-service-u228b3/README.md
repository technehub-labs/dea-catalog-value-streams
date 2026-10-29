# Network Build to Service

Admitted Value Stream record (`value-streams:value-stream-network-build-to-service-u228b3`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-network-build-to-service-u228b3` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | telecommunications · industry-specific |
| Record | [`value-streams-value-stream-network-build-to-service-u228b3.yaml`](./value-streams-value-stream-network-build-to-service-u228b3.yaml) — authoritative |

## 2. Definition

> The network-investment stream from capacity planning through build and integration to service-ready status.

## 3. Value proposition and served party

**Outcome:** Service-ready network capacity in production.

## 4. Stream boundary

**Entry criterion:** A capacity need is identified.

**Exit criterion:** The new capacity is in production and service-ready.

**In scope** (from the record's `scope.includes`):

- Capacity planning
- Build and integration
- Acceptance and cutover

**Out of scope** (each concern owned by the named neighbour):

- Customer provisioning (Order to Activation)
- Decommissioning

## 5. Value stages

Network Build to Service decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Plan Capacity

Plan network capacity against demand.

| Aspect | Value |
|---|---|
| Entry criterion | A capacity need is identified. |
| Exit criterion | The build is planned. |
| Outcome | A planned build. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-strategic-planning-k3rz7a`, `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-sd-build-2pkz5n`, `processes:process-fa-conceive-4uqqvg` |

### Stage 2: Build and Integrate

Build and integrate the network capacity.

| Aspect | Value |
|---|---|
| Entry criterion | The build is planned. |
| Exit criterion | The build is complete and integrated. |
| Outcome | Integrated capacity. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-build-j9z3q4`, `processes:process-eo-operate-xud3hs` |

### Stage 3: Accept and Cut Over

Accept and cut over to production.

| Aspect | Value |
|---|---|
| Entry criterion | The build is integrated. |
| Exit criterion | The capacity is service-ready. |
| Outcome | Service-ready capacity. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-strategic-planning-k3rz7a`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-operations-management-pm3w8k`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-build-2pkz5n`
- `processes:process-fa-conceive-4uqqvg`
- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-44jsrp`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-plan-to-forecast` — Capacity investment follows the ratified plan.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-order-to-activation` — Service-ready capacity enables provisioning.

## 8. Measurement

- **Build-to-service lead time** (stream-level) — Elapsed time from plan to service-ready.

## 9. Evidence and admission

**Evidence sources:** SRC-010 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-039) from the CR-VS-11 industry evidence register extension. Industry-specific chain (telecommunications); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
