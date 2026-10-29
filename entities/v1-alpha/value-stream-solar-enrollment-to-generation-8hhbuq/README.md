---
documentation_generated_from: value-streams-value-stream-solar-enrollment-to-generation-8hhbuq.yaml
id: value-streams:value-stream-solar-enrollment-to-generation-8hhbuq
name: Solar Enrollment to Generation
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- utilities-energy
specificity: industry-specific
entry_criterion: A customer applies for generation enrollment.
exit_criterion: The site generates and exports to the grid.
outcome: An enrolled customer site generating and exporting energy.
stages:
- Enroll
- Assess Site
- Install and Inspect
- Activate Export
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-risk-management-h9uxdw
- capabilities:capability-technology-management-maus5n
processes:
- processes:process-eo-build-j9z3q4
- processes:process-eo-design-6j5mxp
- processes:process-eo-operate-2jnz85
- processes:process-eo-operate-44jsrp
- processes:process-pr-operate-bbe384
metrics:
- Enrollment-to-generation cycle time
upstream: []
downstream: []
evidence_sources:
- SRC-011
---

# Solar Enrollment to Generation

`value-streams:value-stream-solar-enrollment-to-generation-8hhbuq` · **operational** · utilities-energy · industry-specific

> The distributed-energy stream from enrollment application through site assessment and installation to exporting generation.

**Outcome:** An enrolled customer site generating and exporting energy.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-solar-enrollment-to-generation-8hhbuq.yaml`](./value-streams-value-stream-solar-enrollment-to-generation-8hhbuq.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Enroll"]
  S2["2. Assess Site"]
  S3["3. Install and Inspect"]
  S4["4. Activate Export"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Enroll** | An application is received. | Eligibility is confirmed. | 1 | 1 | yes |
| 2 | **Assess Site** | Eligibility is confirmed. | The site is approved. | 1 | 1 | yes |
| 3 | **Install and Inspect** | The site is approved. | The installation passes inspection. | 2 | 2 | yes |
| 4 | **Activate Export** | The installation passes. | The site exports energy. | 2 | 1 | yes |

### 1. Enroll

Enroll the applicant and check eligibility.

| Aspect | Value |
|---|---|
| Entry criterion | An application is received. |
| Exit criterion | Eligibility is confirmed. |
| Outcome | An eligible applicant. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Assess Site

Assess the site for generation suitability.

| Aspect | Value |
|---|---|
| Entry criterion | Eligibility is confirmed. |
| Exit criterion | The site is approved. |
| Outcome | An approved site. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-eo-design-6j5mxp` |

### 3. Install and Inspect

Install and inspect the generation equipment.

| Aspect | Value |
|---|---|
| Entry criterion | The site is approved. |
| Exit criterion | The installation passes inspection. |
| Outcome | An inspected installation. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-build-j9z3q4` · `processes:process-eo-operate-44jsrp` |

### 4. Activate Export

Activate export and generation settlement.

| Aspect | Value |
|---|---|
| Entry criterion | The installation passes. |
| Exit criterion | The site exports energy. |
| Outcome | An exporting site. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## Scope boundary

**Entry:** A customer applies for generation enrollment.

**Exit:** The site generates and exports to the grid.

**In scope**

- Application and eligibility
- Site assessment and approval
- Installation and inspection
- Export activation

**Out of scope** (owned by the named neighbour)

- Standard connections (Apply to Connect)
- Generation settlement

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-design-6j5mxp`
- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-2jnz85`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Enrollment-to-generation cycle time** (stream-level) — Elapsed days from application to first export.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-011 | industry-reference-model | Utilities industry reference models (metering and retail-energy chains, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-048) from the CR-VS-11 industry evidence register extension. Industry-specific chain (utilities-energy); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
