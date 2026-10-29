# Build to Handover

Admitted Value Stream record (`value-streams:value-stream-build-to-handover-9fyyzn`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-build-to-handover-9fyyzn` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | construction-real-estate · industry-specific |
| Record | [`value-streams-value-stream-build-to-handover-9fyyzn.yaml`](./value-streams-value-stream-build-to-handover-9fyyzn.yaml) — authoritative |

## 2. Definition

> The project-delivery stream from construction start through works and commissioning to client handover.

## 3. Value proposition and served party

**Outcome:** A handed-over, commissioned project.

## 4. Stream boundary

**Entry criterion:** The project commences on site.

**Exit criterion:** The project is handed over to the client.

**In scope** (from the record's `scope.includes`):

- Works execution
- Progress control
- Commissioning and testing
- Handover

**Out of scope** (each concern owned by the named neighbour):

- Pre-contract design
- Defects liability management

## 5. Value stages

Build to Handover decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Execute Works

Execute the construction works.

| Aspect | Value |
|---|---|
| Entry criterion | The project commences. |
| Exit criterion | The works are complete. |
| Outcome | Completed works. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-eo-operate-xud3hs`, `processes:process-eo-operate-2jnz85` |

### Stage 2: Control Progress

Control progress, quality, and safety.

| Aspect | Value |
|---|---|
| Entry criterion | Works are underway. |
| Exit criterion | Progress is controlled. |
| Outcome | Controlled progress. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-performance-management-5fxren`, `capabilities:capability-security-management-wmzc7c` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Commission and Test

Commission and test the asset.

| Aspect | Value |
|---|---|
| Entry criterion | The works are complete. |
| Exit criterion | Commissioning passes. |
| Outcome | A commissioned asset. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 4: Hand Over

Hand over to the client.

| Aspect | Value |
|---|---|
| Entry criterion | Commissioning passes. |
| Exit criterion | The client accepts handover. |
| Outcome | A handed-over project. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-2jnz85`
- `processes:process-ge-operate-zwaes5`
- `processes:process-eo-operate-44jsrp`
- `processes:process-ge-build-mctdgc`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Handover on-time rate** (stream-level) — Share of projects handed over on schedule.

## 9. Evidence and admission

**Evidence sources:** SRC-017 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-093) from the CR-VS-11 industry evidence register extension. Industry-specific chain (construction-real-estate); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
