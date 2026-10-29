# Prototype to Production Release

Admitted Value Stream record (`value-streams:value-stream-prototype-to-production-release-ts9b3b`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-prototype-to-production-release-ts9b3b` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | development |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | manufacturing · industry-specific |
| Record | [`value-streams-value-stream-prototype-to-production-release-ts9b3b.yaml`](./value-streams-value-stream-prototype-to-production-release-ts9b3b.yaml) — authoritative |

## 2. Definition

> The industrialization stream from approved prototype through process design to production release.

## 3. Value proposition and served party

**Outcome:** A production-released product with validated process.

## 4. Stream boundary

**Entry criterion:** A prototype is approved.

**Exit criterion:** Production is released with a validated process.

**In scope** (from the record's `scope.includes`):

- Process design
- Pilot run and validation
- Production release

**Out of scope** (each concern owned by the named neighbour):

- Product development (Concept to Launch)
- Volume production (Make to Stock Release)

## 5. Value stages

Prototype to Production Release decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Design Process

Design the manufacturing process.

| Aspect | Value |
|---|---|
| Entry criterion | A prototype is approved. |
| Exit criterion | The process is designed. |
| Outcome | A designed process. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n`, `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-eo-design-6j5mxp` |

### Stage 2: Pilot and Validate

Run the pilot and validate the process.

| Aspect | Value |
|---|---|
| Entry criterion | The process is designed. |
| Exit criterion | The process is validated. |
| Outcome | A validated process. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-operate-xud3hs`, `processes:process-eo-operate-44jsrp` |

### Stage 3: Release Production

Release to production.

| Aspect | Value |
|---|---|
| Entry criterion | The process is validated. |
| Exit criterion | Production is released. |
| Outcome | A released production. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-design-6j5mxp`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-build-j9z3q4`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-concept-to-launch` — Product development approves the prototype.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-make-to-stock-release` — Released production runs through standard production.

## 8. Measurement

- **Time to production release** (stream-level) — Elapsed time from prototype approval to release.

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-054) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
