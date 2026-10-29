# Surrender to Payout

Admitted Value Stream record (`value-streams:value-stream-surrender-to-payout-vf67kv`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-surrender-to-payout-vf67kv` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | insurance · industry-specific |
| Record | [`value-streams-value-stream-surrender-to-payout-vf67kv.yaml`](./value-streams-value-stream-surrender-to-payout-vf67kv.yaml) — authoritative |

## 2. Definition

> The life-insurance surrender stream from surrender request through surrender-value computation to payout and closure.

## 3. Value proposition and served party

**Outcome:** A correctly computed surrender paid and the contract closed.

## 4. Stream boundary

**Entry criterion:** A policyholder requests surrender.

**Exit criterion:** The surrender value is paid and the contract closed.

**In scope** (from the record's `scope.includes`):

- Surrender request and validation
- Surrender-value computation
- Payout and closure

**Out of scope** (each concern owned by the named neighbour):

- Maturity settlement
- Policy loans

## 5. Value stages

Surrender to Payout decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Validate Request

Validate the surrender request and contract status.

| Aspect | Value |
|---|---|
| Entry criterion | A request is received. |
| Exit criterion | The request is validated. |
| Outcome | A validated request. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Compute Value

Compute the surrender value.

| Aspect | Value |
|---|---|
| Entry criterion | The request is validated. |
| Exit criterion | The value is computed and communicated. |
| Outcome | A communicated surrender value. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### Stage 3: Pay and Close

Pay the surrender and close the contract.

| Aspect | Value |
|---|---|
| Entry criterion | The value is accepted. |
| Exit criterion | The payout is made and the contract closed. |
| Outcome | A closed contract with paid surrender. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Surrender processing cycle time** (stream-level) — Elapsed days from request to payout.

## 9. Evidence and admission

**Evidence sources:** SRC-009 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-035) from the CR-VS-11 industry evidence register extension. Industry-specific chain (insurance); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
