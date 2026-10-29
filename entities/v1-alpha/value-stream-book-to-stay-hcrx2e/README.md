---
documentation_generated_from: value-streams-value-stream-book-to-stay-hcrx2e.yaml
id: value-streams:value-stream-book-to-stay-hcrx2e
name: Book to Stay
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- hospitality-travel
specificity: industry-specific
entry_criterion: A reservation is made.
exit_criterion: The guest checks out with a settled folio.
outcome: A completed stay with settled folio.
stages:
- Reserve
- Prepare Arrival
- Serve Stay
- Check Out and Settle
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-operations-management-pm3w8k
processes:
- processes:process-eo-operate-2jnz85
- processes:process-fa-operate-sdppmp
- processes:process-pr-operate-bbe384
metrics:
- Occupancy rate
upstream: []
downstream: []
evidence_sources:
- SRC-015
---

# Book to Stay

`value-streams:value-stream-book-to-stay-hcrx2e` · **operational** · hospitality-travel · industry-specific

> The lodging stream from reservation through pre-arrival to completed stay and checkout.

**Outcome:** A completed stay with settled folio.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-book-to-stay-hcrx2e.yaml`](./value-streams-value-stream-book-to-stay-hcrx2e.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Reserve"]
  S2["2. Prepare Arrival"]
  S3["3. Serve Stay"]
  S4["4. Check Out and Settle"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Reserve** | A reservation is made. | The booking is confirmed. | 1 | 1 | yes |
| 2 | **Prepare Arrival** | A booking is confirmed. | The room is ready. | 1 | 1 | no |
| 3 | **Serve Stay** | The guest arrives. | The stay is served. | 2 | 1 | yes |
| 4 | **Check Out and Settle** | The stay ends. | The folio is settled. | 1 | 1 | yes |

### 1. Reserve

Take and confirm the reservation.

| Aspect | Value |
|---|---|
| Entry criterion | A reservation is made. |
| Exit criterion | The booking is confirmed. |
| Outcome | A confirmed booking. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Prepare Arrival

Prepare for the arrival.

| Aspect | Value |
|---|---|
| Entry criterion | A booking is confirmed. |
| Exit criterion | The room is ready. |
| Outcome | A ready room. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### 3. Serve Stay

Serve the guest through the stay.

| Aspect | Value |
|---|---|
| Entry criterion | The guest arrives. |
| Exit criterion | The stay is served. |
| Outcome | A served stay. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### 4. Check Out and Settle

Check out and settle the folio.

| Aspect | Value |
|---|---|
| Entry criterion | The stay ends. |
| Exit criterion | The folio is settled. |
| Outcome | A settled folio. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## Scope boundary

**Entry:** A reservation is made.

**Exit:** The guest checks out with a settled folio.

**In scope**

- Reservation
- Pre-arrival preparation
- Stay service
- Checkout and settlement

**Out of scope** (owned by the named neighbour)

- Events (Event Book to Execute)
- Loyalty programs

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-2jnz85`
- `processes:process-fa-operate-sdppmp`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Occupancy rate** (stream-level) — Occupied room-nights as a share of available.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-015 | industry-reference-model | Education and hospitality service chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-087) from the CR-VS-11 industry evidence register extension. Industry-specific chain (hospitality-travel); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
