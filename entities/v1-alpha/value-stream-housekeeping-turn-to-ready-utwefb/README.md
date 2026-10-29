# Housekeeping Turn to Ready

Admitted Value Stream record (`value-streams:value-stream-housekeeping-turn-to-ready-utwefb`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-housekeeping-turn-to-ready-utwefb` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | hospitality-travel · industry-specific |
| Record | [`value-streams-value-stream-housekeeping-turn-to-ready-utwefb.yaml`](./value-streams-value-stream-housekeeping-turn-to-ready-utwefb.yaml) — authoritative |

## 2. Definition

> The housekeeping stream from checkout through cleaning and inspection to ready-to-sell status.

## 3. Value proposition and served party

**Outcome:** A ready-to-sell room at standard.

## 4. Stream boundary

**Entry criterion:** A guest checks out.

**Exit criterion:** The room is ready to sell.

**In scope** (from the record's `scope.includes`):

- Cleaning
- Inspection
- Ready status

**Out of scope** (each concern owned by the named neighbour):

- Maintenance (Grid Maintenance pattern)
- Lodging service (Book to Stay)

## 5. Value stages

Housekeeping Turn to Ready decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Clean

Clean the departed room.

| Aspect | Value |
|---|---|
| Entry criterion | A checkout occurs. |
| Exit criterion | The room is cleaned. |
| Outcome | A cleaned room. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 2: Inspect

Inspect against the room standard.

| Aspect | Value |
|---|---|
| Entry criterion | The room is cleaned. |
| Exit criterion | The room passes inspection. |
| Outcome | A passed inspection. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 3: Mark Ready

Mark the room ready to sell.

| Aspect | Value |
|---|---|
| Entry criterion | The inspection passes. |
| Exit criterion | The room is ready. |
| Outcome | A ready room. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-zwzmbd`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-book-to-stay` — Ready rooms enable the next arrivals.

**Downstream streams:** none recorded.

## 8. Measurement

- **Room turnaround time** (stream-level) — Elapsed time from checkout to ready status.

## 9. Evidence and admission

**Evidence sources:** SRC-015 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-090) from the CR-VS-11 industry evidence register extension. Industry-specific chain (hospitality-travel); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
