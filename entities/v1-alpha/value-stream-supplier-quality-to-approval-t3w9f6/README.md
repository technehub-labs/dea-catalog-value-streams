---
documentation_generated_from: value-streams-value-stream-supplier-quality-to-approval-t3w9f6.yaml
id: value-streams:value-stream-supplier-quality-to-approval-t3w9f6
name: Supplier Quality to Approval
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: governance
industries:
- manufacturing
specificity: industry-specific
entry_criterion: A supplier quality audit is scheduled.
exit_criterion: The supplier is approved with actions closed.
outcome: Approved suppliers with closed corrective actions.
stages:
- Audit Supplier
- Agree Actions
- Verify and Approve
capabilities:
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-risk-management-h9uxdw
- capabilities:capability-supplier-management-d6fuj4
processes:
- processes:process-ge-build-mctdgc
- processes:process-ge-operate-zwaes5
metrics:
- Supplier corrective action closure time
upstream: []
downstream: []
evidence_sources:
- SRC-016
---

# Supplier Quality to Approval

`value-streams:value-stream-supplier-quality-to-approval-t3w9f6` · **governance** · manufacturing · industry-specific

> The supplier stream from quality audit through corrective action to approved-supplier status.

**Outcome:** Approved suppliers with closed corrective actions.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-supplier-quality-to-approval-t3w9f6.yaml`](./value-streams-value-stream-supplier-quality-to-approval-t3w9f6.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Audit Supplier"]
  S2["2. Agree Actions"]
  S3["3. Verify and Approve"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Audit Supplier** | An audit is scheduled. | The audit is complete. | 2 | 1 | no |
| 2 | **Agree Actions** | The audit is complete. | The plan is agreed. | 2 | 1 | no |
| 3 | **Verify and Approve** | The plan is agreed. | The supplier is approved. | 2 | 1 | no |

### 1. Audit Supplier

Audit the supplier's quality system.

| Aspect | Value |
|---|---|
| Entry criterion | An audit is scheduled. |
| Exit criterion | The audit is complete. |
| Outcome | Audit findings. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-supplier-management-d6fuj4` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 2. Agree Actions

Agree the corrective action plan.

| Aspect | Value |
|---|---|
| Entry criterion | The audit is complete. |
| Exit criterion | The plan is agreed. |
| Outcome | An agreed plan. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-supplier-management-d6fuj4` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### 3. Verify and Approve

Verify actions and approve the supplier.

| Aspect | Value |
|---|---|
| Entry criterion | The plan is agreed. |
| Exit criterion | The supplier is approved. |
| Outcome | An approved supplier. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

## Scope boundary

**Entry:** A supplier quality audit is scheduled.

**Exit:** The supplier is approved with actions closed.

**In scope**

- Audit
- Corrective action plan
- Verification and approval

**Out of scope** (owned by the named neighbour)

- Sourcing (Procure to Pay)
- Supplier onboarding

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-supplier-management-d6fuj4`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-zwaes5`
- `processes:process-ge-build-mctdgc`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Supplier corrective action closure time** (stream-level) — Elapsed days from finding to closure.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-016 | industry-reference-model | Manufacturing and logistics reference models (SCOR-style category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-053) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
