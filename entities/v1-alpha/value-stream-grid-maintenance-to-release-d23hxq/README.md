# Grid Maintenance to Release

Admitted Value Stream record (`value-streams:value-stream-grid-maintenance-to-release-d23hxq`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-grid-maintenance-to-release-d23hxq` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | utilities-energy · industry-specific |
| Record | [`value-streams-value-stream-grid-maintenance-to-release-d23hxq.yaml`](./value-streams-value-stream-grid-maintenance-to-release-d23hxq.yaml) — authoritative |

## 2. Definition

> The asset stream from maintenance planning through execution to released-back-to-service equipment.

## 3. Value proposition and served party

**Outcome:** Maintained equipment released safely back to service.

## 4. Stream boundary

**Entry criterion:** A maintenance window is planned.

**Exit criterion:** The equipment is released back to service.

**In scope** (from the record's `scope.includes`):

- Maintenance planning
- Safe isolation
- Work execution
- Testing and release

**Out of scope** (each concern owned by the named neighbour):

- Outage repair (Outage to Restore)
- Asset lifecycle (Acquire to Retire)

## 5. Value stages

Grid Maintenance to Release decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Plan Window

Plan the maintenance window.

| Aspect | Value |
|---|---|
| Entry criterion | A window is planned. |
| Exit criterion | The window is scheduled. |
| Outcome | A scheduled window. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-workforce-planning-b43rhm` |
| Realizing processes | `processes:process-sd-build-2pkz5n` |

### Stage 2: Isolate Safely

Safely isolate the equipment.

| Aspect | Value |
|---|---|
| Entry criterion | The window is scheduled. |
| Exit criterion | The equipment is isolated. |
| Outcome | Isolated equipment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Execute Work

Execute the maintenance work.

| Aspect | Value |
|---|---|
| Entry criterion | The equipment is isolated. |
| Exit criterion | The work is complete. |
| Outcome | Completed work. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-operate-j9cjzz` |

### Stage 4: Test and Release

Test and release to service.

| Aspect | Value |
|---|---|
| Entry criterion | The work is complete. |
| Exit criterion | The equipment is back in service. |
| Outcome | Released equipment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-planning-b43rhm`
- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-technology-management-maus5n`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-build-2pkz5n`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-j9cjzz`
- `processes:process-eo-operate-44jsrp`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-acquire-to-retire` — Grid assets live in the asset lifecycle.

**Downstream streams:** none recorded.

## 8. Measurement

- **Maintenance window adherence** (stream-level) — Share of windows completed on schedule.

## 9. Evidence and admission

**Evidence sources:** SRC-011 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-047) from the CR-VS-11 industry evidence register extension. Industry-specific chain (utilities-energy); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
