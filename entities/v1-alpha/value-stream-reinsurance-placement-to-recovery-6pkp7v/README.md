# Reinsurance Placement to Recovery

Admitted Value Stream record (`value-streams:value-stream-reinsurance-placement-to-recovery-6pkp7v`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-reinsurance-placement-to-recovery-6pkp7v` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | insurance · industry-specific |
| Record | [`value-streams-value-stream-reinsurance-placement-to-recovery-6pkp7v.yaml`](./value-streams-value-stream-reinsurance-placement-to-recovery-6pkp7v.yaml) — authoritative |

## 2. Definition

> The reinsurance stream from placement negotiation through premium settlement to loss recovery.

## 3. Value proposition and served party

**Outcome:** Ceded risk with recoveries collected.

## 4. Stream boundary

**Entry criterion:** A reinsurance need is identified.

**Exit criterion:** Recoveries are collected for ceded losses.

**In scope** (from the record's `scope.includes`):

- Placement negotiation
- Contract execution and premium settlement
- Loss reporting
- Recovery collection

**Out of scope** (each concern owned by the named neighbour):

- Direct underwriting (Quote to Bind)
- Direct claims (Loss to Claim Settlement)

## 5. Value stages

Reinsurance Placement to Recovery decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Place Cover

Negotiate and place the reinsurance cover.

| Aspect | Value |
|---|---|
| Entry criterion | A need is identified. |
| Exit criterion | The cover is placed. |
| Outcome | Placed cover. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-partner-management-cp3vdb`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 2: Settle Premium

Execute the contract and settle premium.

| Aspect | Value |
|---|---|
| Entry criterion | The cover is placed. |
| Exit criterion | The contract is executed and premium settled. |
| Outcome | An executed treaty. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-ge-build-mctdgc`, `processes:process-fa-operate-wkqaqp` |

### Stage 3: Report Losses

Report ceded losses to the reinsurer.

| Aspect | Value |
|---|---|
| Entry criterion | A covered loss occurs. |
| Exit criterion | The loss is reported. |
| Outcome | A reported ceded loss. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 4: Collect Recovery

Collect the reinsurance recovery.

| Aspect | Value |
|---|---|
| Entry criterion | The loss is reported. |
| Exit criterion | The recovery is collected. |
| Outcome | A collected recovery. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-build-mctdgc`
- `processes:process-fa-operate-wkqaqp`
- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Recovery collection cycle time** (stream-level) — Elapsed time from loss report to collected recovery.

## 9. Evidence and admission

**Evidence sources:** SRC-009 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-034) from the CR-VS-11 industry evidence register extension. Industry-specific chain (insurance); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
