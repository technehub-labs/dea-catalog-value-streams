# Supplier Quality to Approval

Admitted Value Stream record (`value-streams:value-stream-supplier-quality-to-approval-t3w9f6`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-supplier-quality-to-approval-t3w9f6` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | manufacturing · industry-specific |
| Record | [`value-streams-value-stream-supplier-quality-to-approval-t3w9f6.yaml`](./value-streams-value-stream-supplier-quality-to-approval-t3w9f6.yaml) — authoritative |

## 2. Definition

> The supplier stream from quality audit through corrective action to approved-supplier status.

## 3. Value proposition and served party

**Outcome:** Approved suppliers with closed corrective actions.

## 4. Stream boundary

**Entry criterion:** A supplier quality audit is scheduled.

**Exit criterion:** The supplier is approved with actions closed.

**In scope** (from the record's `scope.includes`):

- Audit
- Corrective action plan
- Verification and approval

**Out of scope** (each concern owned by the named neighbour):

- Sourcing (Procure to Pay)
- Supplier onboarding

## 5. Value stages

Supplier Quality to Approval decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Audit Supplier

Audit the supplier's quality system.

| Aspect | Value |
|---|---|
| Entry criterion | An audit is scheduled. |
| Exit criterion | The audit is complete. |
| Outcome | Audit findings. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-supplier-management-d6fuj4` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 2: Agree Actions

Agree the corrective action plan.

| Aspect | Value |
|---|---|
| Entry criterion | The audit is complete. |
| Exit criterion | The plan is agreed. |
| Outcome | An agreed plan. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-supplier-management-d6fuj4`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 3: Verify and Approve

Verify actions and approve the supplier.

| Aspect | Value |
|---|---|
| Entry criterion | The plan is agreed. |
| Exit criterion | The supplier is approved. |
| Outcome | An approved supplier. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-supplier-management-d6fuj4`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-zwaes5`
- `processes:process-ge-build-mctdgc`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Supplier corrective action closure time** (stream-level) — Elapsed days from finding to closure.

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-053) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
