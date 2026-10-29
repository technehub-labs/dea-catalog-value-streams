# Customs Clearance to Release

Admitted Value Stream record (`value-streams:value-stream-customs-clearance-to-release-cfgc3b`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-customs-clearance-to-release-cfgc3b` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | logistics-transportation · industry-specific |
| Record | [`value-streams-value-stream-customs-clearance-to-release-cfgc3b.yaml`](./value-streams-value-stream-customs-clearance-to-release-cfgc3b.yaml) — authoritative |

## 2. Definition

> The customs stream from declaration filing through assessment and inspection to released cargo.

## 3. Value proposition and served party

**Outcome:** Customs-released cargo with duties settled.

## 4. Stream boundary

**Entry criterion:** A shipment requires customs clearance.

**Exit criterion:** The cargo is released and duties settled.

**In scope** (from the record's `scope.includes`):

- Declaration filing
- Assessment and inspection
- Release and duty settlement

**Out of scope** (each concern owned by the named neighbour):

- Freight movement (Ship to Consignee)
- Trade compliance governance

## 5. Value stages

Customs Clearance to Release decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: File Declaration

File the customs declaration.

| Aspect | Value |
|---|---|
| Entry criterion | A shipment requires clearance. |
| Exit criterion | The declaration is filed. |
| Outcome | A filed declaration. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-8vqvkk` |

### Stage 2: Assess and Inspect

Assess and inspect if selected.

| Aspect | Value |
|---|---|
| Entry criterion | The declaration is filed. |
| Exit criterion | Assessment completes. |
| Outcome | A completed assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Release and Settle

Release the cargo and settle duties.

| Aspect | Value |
|---|---|
| Entry criterion | Assessment completes. |
| Exit criterion | The cargo is released. |
| Outcome | Released cargo. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-operations-management-pm3w8k`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-8vqvkk`
- `processes:process-ge-operate-zwaes5`
- `processes:process-fa-operate-g9zpnq`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Customs clearance cycle time** (stage: Release and Settle) — Elapsed time from filing to release. → [`dea:metric-customs-clearance-cycle-time`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-067) from the CR-VS-11 industry evidence register extension. Industry-specific chain (logistics-transportation); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
