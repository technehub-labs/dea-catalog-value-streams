# Trouble to Restore

Admitted Value Stream record (`value-streams:value-stream-trouble-to-restore-gtrgd8`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-trouble-to-restore-gtrgd8` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | telecommunications · industry-specific |
| Record | [`value-streams-value-stream-trouble-to-restore-gtrgd8.yaml`](./value-streams-value-stream-trouble-to-restore-gtrgd8.yaml) — authoritative |

## 2. Definition

> The telecom assurance stream from fault report through diagnosis and repair to restored service.

## 3. Value proposition and served party

**Outcome:** Restored service confirmed to the customer.

## 4. Stream boundary

**Entry criterion:** A fault is reported or detected.

**Exit criterion:** Service is restored and confirmed.

**In scope** (from the record's `scope.includes`):

- Fault localization
- Diagnosis and dispatch
- Repair
- Restoration confirmation

**Out of scope** (each concern owned by the named neighbour):

- Planned maintenance
- Customer complaint handling (Issue to Resolve)

## 5. Value stages

Trouble to Restore decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Localize Fault

Localize the reported or detected fault.

| Aspect | Value |
|---|---|
| Entry criterion | A fault is reported. |
| Exit criterion | The fault is localized. |
| Outcome | A localized fault. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-4njp7b` |

### Stage 2: Diagnose and Dispatch

Diagnose root cause and dispatch repair.

| Aspect | Value |
|---|---|
| Entry criterion | The fault is localized. |
| Exit criterion | Repair is dispatched. |
| Outcome | A dispatched repair. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Repair

Execute the repair.

| Aspect | Value |
|---|---|
| Entry criterion | Repair is dispatched. |
| Exit criterion | The repair is complete. |
| Outcome | A completed repair. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-j9cjzz` |

### Stage 4: Confirm Restoration

Confirm service restoration with the customer.

| Aspect | Value |
|---|---|
| Entry criterion | The repair is complete. |
| Exit criterion | Service is restored and confirmed. |
| Outcome | Restored service. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-management-9e8d8s`
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

- **Mean time to restore service** (stage: Confirm Restoration) — Mean elapsed time from fault to restoration. → [`dea:metric-mean-time-to-restore-service`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-010 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-037) from the CR-VS-11 industry evidence register extension. Industry-specific chain (telecommunications); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
