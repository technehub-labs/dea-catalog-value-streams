---
documentation_generated_from: value-streams-value-stream-safety-incident-to-closure-6v5uxt.yaml
id: value-streams:value-stream-safety-incident-to-closure-6v5uxt
name: Safety Incident to Closure
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: governance
industries:
- utilities-energy
- manufacturing
specificity: industry-specific
entry_criterion: A safety incident is reported.
exit_criterion: The investigation and corrective actions are closed.
outcome: Incidents investigated with corrective actions closed out.
stages:
- Report Incident
- Investigate
- Correct
- Verify Closure
capabilities:
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-enterprise-performance-management-5fxren
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-risk-management-h9uxdw
- capabilities:capability-security-management-wmzc7c
processes:
- processes:process-eo-improve-g3ngp3
- processes:process-ge-operate-tpenm6
- processes:process-ge-operate-zwaes5
metrics:
- Recordable incident rate
upstream: []
downstream: []
evidence_sources:
- SRC-011
- SRC-016
---

# Safety Incident to Closure

`value-streams:value-stream-safety-incident-to-closure-6v5uxt` · **governance** · utilities-energy, manufacturing · industry-specific

> The safety stream from incident report through investigation to corrective-action closure.

**Outcome:** Incidents investigated with corrective actions closed out.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-safety-incident-to-closure-6v5uxt.yaml`](./value-streams-value-stream-safety-incident-to-closure-6v5uxt.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Report Incident"]
  S2["2. Investigate"]
  S3["3. Correct"]
  S4["4. Verify Closure"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Report Incident** | An incident occurs. | The incident is registered. | 2 | 1 | yes |
| 2 | **Investigate** | The incident is registered. | Causes are determined. | 2 | 1 | no |
| 3 | **Correct** | Causes are determined. | Corrective actions are implemented. | 2 | 1 | no |
| 4 | **Verify Closure** | Actions are implemented. | Closure is verified. | 2 | 1 | no |

### 1. Report Incident

Report and register the safety incident.

| Aspect | Value |
|---|---|
| Entry criterion | An incident occurs. |
| Exit criterion | The incident is registered. |
| Outcome | A registered incident. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### 2. Investigate

Investigate causes.

| Aspect | Value |
|---|---|
| Entry criterion | The incident is registered. |
| Exit criterion | Causes are determined. |
| Outcome | Determined causes. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 3. Correct

Implement corrective actions.

| Aspect | Value |
|---|---|
| Entry criterion | Causes are determined. |
| Exit criterion | Corrective actions are implemented. |
| Outcome | Implemented actions. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-eo-improve-g3ngp3` |

### 4. Verify Closure

Verify effectiveness and close.

| Aspect | Value |
|---|---|
| Entry criterion | Actions are implemented. |
| Exit criterion | Closure is verified. |
| Outcome | A closed incident. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u` · `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

## Scope boundary

**Entry:** A safety incident is reported.

**Exit:** The investigation and corrective actions are closed.

**In scope**

- Incident reporting
- Investigation
- Corrective action
- Closure verification

**Out of scope** (owned by the named neighbour)

- Regulatory reporting (Record to Report)
- Insurance claims interface

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-operate-zwaes5`
- `processes:process-eo-improve-g3ngp3`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Recordable incident rate** (stream-level) — Recordable incidents per hours worked.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-011 | industry-reference-model | Utilities industry reference models (metering and retail-energy chains, public structure) |
| SRC-016 | industry-reference-model | Manufacturing and logistics reference models (SCOR-style category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-049) from the CR-VS-11 industry evidence register extension. Industry-specific chain (utilities-energy, manufacturing); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
