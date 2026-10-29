# Book to Stay

Admitted Value Stream record (`value-streams:value-stream-book-to-stay-hcrx2e`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-book-to-stay-hcrx2e` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | hospitality-travel · industry-specific |
| Record | [`value-streams-value-stream-book-to-stay-hcrx2e.yaml`](./value-streams-value-stream-book-to-stay-hcrx2e.yaml) — authoritative |

## 2. Definition

> The lodging stream from reservation through pre-arrival to completed stay and checkout.

## 3. Value proposition and served party

**Outcome:** A completed stay with settled folio.

## 4. Stream boundary

**Entry criterion:** A reservation is made.

**Exit criterion:** The guest checks out with a settled folio.

**In scope** (from the record's `scope.includes`):

- Reservation
- Pre-arrival preparation
- Stay service
- Checkout and settlement

**Out of scope** (each concern owned by the named neighbour):

- Events (Event Book to Execute)
- Loyalty programs

## 5. Value stages

Book to Stay decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Reserve

Take and confirm the reservation.

| Aspect | Value |
|---|---|
| Entry criterion | A reservation is made. |
| Exit criterion | The booking is confirmed. |
| Outcome | A confirmed booking. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Prepare Arrival

Prepare for the arrival.

| Aspect | Value |
|---|---|
| Entry criterion | A booking is confirmed. |
| Exit criterion | The room is ready. |
| Outcome | A ready room. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Serve Stay

Serve the guest through the stay.

| Aspect | Value |
|---|---|
| Entry criterion | The guest arrives. |
| Exit criterion | The stay is served. |
| Outcome | A served stay. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 4: Check Out and Settle

Check out and settle the folio.

| Aspect | Value |
|---|---|
| Entry criterion | The stay ends. |
| Exit criterion | The folio is settled. |
| Outcome | A settled folio. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-2jnz85`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Occupancy rate** (stream-level) — Occupied room-nights as a share of available.

## 9. Evidence and admission

**Evidence sources:** SRC-015 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-087) from the CR-VS-11 industry evidence register extension. Industry-specific chain (hospitality-travel); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
