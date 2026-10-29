# Outage to Restore

Admitted Value Stream record (`value-streams:value-stream-outage-to-restore-ff6xme`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-outage-to-restore-ff6xme` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | utilities-energy · industry-specific |
| Record | [`value-streams-value-stream-outage-to-restore-ff6xme.yaml`](./value-streams-value-stream-outage-to-restore-ff6xme.yaml) — authoritative |

## 2. Definition

> The grid-operations stream from outage detection through crew dispatch and repair to restored supply and customer communication.

## 3. Value proposition and served party

**Outcome:** Restored supply with informed customers.

## 4. Stream boundary

**Entry criterion:** An outage is detected or reported.

**Exit criterion:** Supply is restored and customers are informed.

**In scope** (from the record's `scope.includes`):

- Outage detection and localization
- Crew dispatch
- Repair and switching
- Restoration confirmation

**Out of scope** (each concern owned by the named neighbour):

- Planned maintenance
- Field installations

## 5. Value stages

Outage to Restore decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Detect and Localize

Detect and localize the outage.

| Aspect | Value |
|---|---|
| Entry criterion | An outage occurs. |
| Exit criterion | The outage is localized. |
| Outcome | A localized outage. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-4njp7b` |

### Stage 2: Dispatch Crew

Dispatch the repair crew.

| Aspect | Value |
|---|---|
| Entry criterion | The outage is localized. |
| Exit criterion | The crew is dispatched. |
| Outcome | A dispatched crew. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-workforce-planning-b43rhm` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Repair and Switch

Execute repair and switching restoration.

| Aspect | Value |
|---|---|
| Entry criterion | The crew is dispatched. |
| Exit criterion | Supply is restored. |
| Outcome | Restored supply. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-operate-j9cjzz` |

### Stage 4: Confirm and Communicate

Confirm restoration and communicate to customers.

| Aspect | Value |
|---|---|
| Entry criterion | Supply is restored. |
| Exit criterion | Customers are informed. |
| Outcome | Informed customers. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-planning-b43rhm`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-customer-management-f3n8wb`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-4njp7b`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-j9cjzz`
- `processes:process-pr-operate-bbe384`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Outage restoration time** (stage: Confirm and Communicate) — Elapsed time from detection to restoration. → [`dea:metric-mean-time-to-restore-service`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-011 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-045) from the CR-VS-11 industry evidence register extension. Industry-specific chain (utilities-energy); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
