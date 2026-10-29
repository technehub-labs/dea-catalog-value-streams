---
documentation_generated_from: value-streams-value-stream-initiate-to-settle-ken6np.yaml
id: value-streams:value-stream-initiate-to-settle-ken6np
name: Initiate to Settle
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- financial-services
specificity: industry-specific
entry_criterion: A payment is initiated.
exit_criterion: The payment is settled and reconciled.
outcome: A settled, reconciled payment between parties.
stages:
- Initiate Payment
- Clear
- Settle
- Reconcile
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-technology-management-maus5n
processes:
- processes:process-eo-operate-2jnz85
- processes:process-fa-operate-4xn4d6
- processes:process-fa-operate-g9zpnq
- processes:process-pr-operate-bbe384
metrics:
- Payment settlement cycle time
upstream: []
downstream: []
evidence_sources:
- SRC-008
---

# Initiate to Settle

`value-streams:value-stream-initiate-to-settle-ken6np` · **operational** · financial-services · industry-specific

> The end-to-end payments stream from payment initiation through clearing and settlement to reconciled completion.

**Outcome:** A settled, reconciled payment between parties.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-initiate-to-settle-ken6np.yaml`](./value-streams-value-stream-initiate-to-settle-ken6np.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  TRIGGER(["⏺ Entry"])
  EXIT1(["✔ Exit"])
  S1["1. Initiate Payment<br/>The instruction is validated"]
  S2["2. Clear<br/>The payment is cleared"]
  S3["3. Settle<br/>Settlement completes"]
  S4["4. Reconcile<br/>The payment is reconciled"]
  TRIGGER --> S1
  S1 --> S2
  S2 --> S3
  S3 --> S4
  S4 --> EXIT1
  S4 -. re-engage .-> S1
  classDef terminal fill:#2C3E50,color:#fff,stroke:#1a252f,stroke-width:1px;
  classDef stage fill:#EAF2F8,color:#1a252f,stroke:#2C3E50,stroke-width:1px;
  class TRIGGER,EXIT1 terminal;
  class S1,S2,S3,S4 stage;
  style TRIGGER fill:#27AE60,color:#fff,stroke:#1e8449,stroke-width:1px;
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Initiate Payment** | A payment is initiated. | The instruction is validated. | 2 | 1 | yes |
| 2 | **Clear** | The instruction is validated. | The payment is cleared. | 2 | 1 | no |
| 3 | **Settle** | The payment is cleared. | Settlement completes. | 2 | 1 | no |
| 4 | **Reconcile** | Settlement completes. | The payment is reconciled. | 2 | 1 | no |

### 1. Initiate Payment

Receive and validate the payment instruction.

| Aspect | Value |
|---|---|
| Entry criterion | A payment is initiated. |
| Exit criterion | The instruction is validated. |
| Outcome | A validated payment instruction. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Clear

Route the payment through clearing.

| Aspect | Value |
|---|---|
| Entry criterion | The instruction is validated. |
| Exit criterion | The payment is cleared. |
| Outcome | A cleared payment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### 3. Settle

Settle the payment between accounts.

| Aspect | Value |
|---|---|
| Entry criterion | The payment is cleared. |
| Exit criterion | Settlement completes. |
| Outcome | A settled payment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### 4. Reconcile

Reconcile settlement against instructions.

| Aspect | Value |
|---|---|
| Entry criterion | Settlement completes. |
| Exit criterion | The payment is reconciled. |
| Outcome | A reconciled payment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-4xn4d6` |

## Scope boundary

**Entry:** A payment is initiated.

**Exit:** The payment is settled and reconciled.

**In scope**

- Payment initiation and validation
- Clearing
- Settlement
- Reconciliation

**Out of scope** (owned by the named neighbour)

- Trade capture
- Card network disputes

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-2jnz85`
- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-4xn4d6`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Payment settlement cycle time** (stream-level) — Elapsed time from initiation to reconciled settlement.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-008 | industry-reference-model | Banking industry reference models (lending and payments chains, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-023) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
