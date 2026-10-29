---
documentation_generated_from: value-streams-value-stream-housekeeping-turn-to-ready-utwefb.yaml
id: value-streams:value-stream-housekeeping-turn-to-ready-utwefb
name: Housekeeping Turn to Ready
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: support
industries:
- hospitality-travel
specificity: industry-specific
entry_criterion: A guest checks out.
exit_criterion: The room is ready to sell.
outcome: A ready-to-sell room at standard.
stages:
- Clean
- Inspect
- Mark Ready
capabilities:
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-eo-operate-2jnz85
- processes:process-eo-operate-44jsrp
- processes:process-eo-operate-zwzmbd
metrics:
- Room turnaround time
upstream:
- value-stream-book-to-stay
downstream: []
evidence_sources:
- SRC-015
---

# Housekeeping Turn to Ready

`value-streams:value-stream-housekeeping-turn-to-ready-utwefb` · **support** · hospitality-travel · industry-specific

> The housekeeping stream from checkout through cleaning and inspection to ready-to-sell status.

**Outcome:** A ready-to-sell room at standard.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-housekeeping-turn-to-ready-utwefb.yaml`](./value-streams-value-stream-housekeeping-turn-to-ready-utwefb.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Clean"]
  S2["2. Inspect"]
  S3["3. Mark Ready"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Clean** | A checkout occurs. | The room is cleaned. | 1 | 1 | no |
| 2 | **Inspect** | The room is cleaned. | The room passes inspection. | 2 | 1 | no |
| 3 | **Mark Ready** | The inspection passes. | The room is ready. | 2 | 1 | no |

### 1. Clean

Clean the departed room.

| Aspect | Value |
|---|---|
| Entry criterion | A checkout occurs. |
| Exit criterion | The room is cleaned. |
| Outcome | A cleaned room. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### 2. Inspect

Inspect against the room standard.

| Aspect | Value |
|---|---|
| Entry criterion | The room is cleaned. |
| Exit criterion | The room passes inspection. |
| Outcome | A passed inspection. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### 3. Mark Ready

Mark the room ready to sell.

| Aspect | Value |
|---|---|
| Entry criterion | The inspection passes. |
| Exit criterion | The room is ready. |
| Outcome | A ready room. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

## Scope boundary

**Entry:** A guest checks out.

**Exit:** The room is ready to sell.

**In scope**

- Cleaning
- Inspection
- Ready status

**Out of scope** (owned by the named neighbour)

- Maintenance (Grid Maintenance pattern)
- Lodging service (Book to Stay)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-information-management-6vjgdh`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-zwzmbd`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [book to stay](../value-stream-book-to-stay-hcrx2e/README.md) — Ready rooms enable the next arrivals.

**Downstream:** none recorded.

## Measurement

- **Room turnaround time** (stream-level) — Elapsed time from checkout to ready status.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-015 | industry-reference-model | Education and hospitality service chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-090) from the CR-VS-11 industry evidence register extension. Industry-specific chain (hospitality-travel); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
