# Initiate to Settle

Admitted Value Stream record (`value-streams:value-stream-initiate-to-settle-ken6np`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-initiate-to-settle-ken6np` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | financial-services · industry-specific |
| Record | [`value-streams-value-stream-initiate-to-settle-ken6np.yaml`](./value-streams-value-stream-initiate-to-settle-ken6np.yaml) — authoritative |

## 2. Definition

> The end-to-end payments stream from payment initiation through clearing and settlement to reconciled completion.

## 3. Value proposition and served party

**Outcome:** A settled, reconciled payment between parties.

## 4. Stream boundary

**Entry criterion:** A payment is initiated.

**Exit criterion:** The payment is settled and reconciled.

**In scope** (from the record's `scope.includes`):

- Payment initiation and validation
- Clearing
- Settlement
- Reconciliation

**Out of scope** (each concern owned by the named neighbour):

- Trade capture
- Card network disputes

## 5. Value stages

Initiate to Settle decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Initiate Payment

Receive and validate the payment instruction.

| Aspect | Value |
|---|---|
| Entry criterion | A payment is initiated. |
| Exit criterion | The instruction is validated. |
| Outcome | A validated payment instruction. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Clear

Route the payment through clearing.

| Aspect | Value |
|---|---|
| Entry criterion | The instruction is validated. |
| Exit criterion | The payment is cleared. |
| Outcome | A cleared payment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Settle

Settle the payment between accounts.

| Aspect | Value |
|---|---|
| Entry criterion | The payment is cleared. |
| Exit criterion | Settlement completes. |
| Outcome | A settled payment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### Stage 4: Reconcile

Reconcile settlement against instructions.

| Aspect | Value |
|---|---|
| Entry criterion | Settlement completes. |
| Exit criterion | The payment is reconciled. |
| Outcome | A reconciled payment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-4xn4d6` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-2jnz85`
- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-4xn4d6`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Payment settlement cycle time** (stream-level) — Elapsed time from initiation to reconciled settlement.

## 9. Evidence and admission

**Evidence sources:** SRC-008 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-023) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
