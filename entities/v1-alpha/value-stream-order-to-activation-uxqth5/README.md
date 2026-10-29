# Order to Activation

Admitted Value Stream record (`value-streams:value-stream-order-to-activation-uxqth5`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-order-to-activation-uxqth5` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | telecommunications · industry-specific |
| Record | [`value-streams-value-stream-order-to-activation-uxqth5.yaml`](./value-streams-value-stream-order-to-activation-uxqth5.yaml) — authoritative |

## 2. Definition

> The end-to-end telecom fulfilment stream from customer order through service design, provisioning, and activation.

## 3. Value proposition and served party

**Outcome:** An activated service for the customer.

## 4. Stream boundary

**Entry criterion:** A customer order for service is accepted.

**Exit criterion:** The service is activated and confirmed to the customer.

**In scope** (from the record's `scope.includes`):

- Order capture and validation
- Service design and feasibility
- Provisioning and configuration
- Activation and confirmation

**Out of scope** (each concern owned by the named neighbour):

- Billing (Usage to Bill)
- Fault handling (Trouble to Restore)

## 5. Value stages

Order to Activation decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Capture Order

Capture and validate the service order.

| Aspect | Value |
|---|---|
| Entry criterion | An order is accepted. |
| Exit criterion | The order is validated. |
| Outcome | A validated order. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Design Service

Design the service and check feasibility.

| Aspect | Value |
|---|---|
| Entry criterion | The order is validated. |
| Exit criterion | The service design is approved. |
| Outcome | An approved design. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-design-6j5mxp` |

### Stage 3: Provision

Provision network resources and configure the service.

| Aspect | Value |
|---|---|
| Entry criterion | The design is approved. |
| Exit criterion | The service is provisioned. |
| Outcome | A provisioned service. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### Stage 4: Activate

Activate and confirm the service.

| Aspect | Value |
|---|---|
| Entry criterion | The service is provisioned. |
| Exit criterion | The service is activated and confirmed. |
| Outcome | An activated service. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-technology-enablement-y6nkws`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-design-6j5mxp`
- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-2jnz85`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-order-to-cash` — Activation is the telecom specialization of order fulfilment; charging follows.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-usage-to-bill` — Activated services start metered usage.

## 8. Measurement

- **Provisioning cycle time** (stage: Activate) — Elapsed time from order to activation. → [`dea:metric-provisioning-cycle-time-telecom`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-010 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-036) from the CR-VS-11 industry evidence register extension. Industry-specific chain (telecommunications); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
