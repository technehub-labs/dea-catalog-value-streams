# Solar Enrollment to Generation

Admitted Value Stream record (`value-streams:value-stream-solar-enrollment-to-generation-8hhbuq`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-solar-enrollment-to-generation-8hhbuq` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | utilities-energy · industry-specific |
| Record | [`value-streams-value-stream-solar-enrollment-to-generation-8hhbuq.yaml`](./value-streams-value-stream-solar-enrollment-to-generation-8hhbuq.yaml) — authoritative |

## 2. Definition

> The distributed-energy stream from enrollment application through site assessment and installation to exporting generation.

## 3. Value proposition and served party

**Outcome:** An enrolled customer site generating and exporting energy.

## 4. Stream boundary

**Entry criterion:** A customer applies for generation enrollment.

**Exit criterion:** The site generates and exports to the grid.

**In scope** (from the record's `scope.includes`):

- Application and eligibility
- Site assessment and approval
- Installation and inspection
- Export activation

**Out of scope** (each concern owned by the named neighbour):

- Standard connections (Apply to Connect)
- Generation settlement

## 5. Value stages

Solar Enrollment to Generation decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Enroll

Enroll the applicant and check eligibility.

| Aspect | Value |
|---|---|
| Entry criterion | An application is received. |
| Exit criterion | Eligibility is confirmed. |
| Outcome | An eligible applicant. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Assess Site

Assess the site for generation suitability.

| Aspect | Value |
|---|---|
| Entry criterion | Eligibility is confirmed. |
| Exit criterion | The site is approved. |
| Outcome | An approved site. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-eo-design-6j5mxp` |

### Stage 3: Install and Inspect

Install and inspect the generation equipment.

| Aspect | Value |
|---|---|
| Entry criterion | The site is approved. |
| Exit criterion | The installation passes inspection. |
| Outcome | An inspected installation. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-build-j9z3q4`, `processes:process-eo-operate-44jsrp` |

### Stage 4: Activate Export

Activate export and generation settlement.

| Aspect | Value |
|---|---|
| Entry criterion | The installation passes. |
| Exit criterion | The site exports energy. |
| Outcome | An exporting site. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-design-6j5mxp`
- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-2jnz85`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Enrollment-to-generation cycle time** (stream-level) — Elapsed days from application to first export.

## 9. Evidence and admission

**Evidence sources:** SRC-011 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-048) from the CR-VS-11 industry evidence register extension. Industry-specific chain (utilities-energy); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
