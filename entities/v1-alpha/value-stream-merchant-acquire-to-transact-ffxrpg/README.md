# Merchant Acquire to Transact

Admitted Value Stream record (`value-streams:value-stream-merchant-acquire-to-transact-ffxrpg`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-merchant-acquire-to-transact-ffxrpg` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | financial-services · industry-specific |
| Record | [`value-streams-value-stream-merchant-acquire-to-transact-ffxrpg.yaml`](./value-streams-value-stream-merchant-acquire-to-transact-ffxrpg.yaml) — authoritative |

## 2. Definition

> The end-to-end merchant-acquiring stream from merchant application through underwriting, terminal provisioning, and first transaction.

## 3. Value proposition and served party

**Outcome:** An acquiring relationship live with the merchant's first settled transaction.

## 4. Stream boundary

**Entry criterion:** A merchant applies for acceptance.

**Exit criterion:** The merchant's first transaction is settled.

**In scope** (from the record's `scope.includes`):

- Merchant application and underwriting
- Terminal or integration provisioning
- Activation and first transaction

**Out of scope** (each concern owned by the named neighbour):

- Card issuance (Card Issue to Activate)
- Merchant chargeback handling (Return to Credit pattern)

## 5. Value stages

Merchant Acquire to Transact decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Underwrite Merchant

Underwrite the merchant application.

| Aspect | Value |
|---|---|
| Entry criterion | A merchant applies. |
| Exit criterion | The merchant is underwritten and approved. |
| Outcome | An approved merchant. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 2: Provision Acceptance

Provision terminals or API integration.

| Aspect | Value |
|---|---|
| Entry criterion | The merchant is approved. |
| Exit criterion | Acceptance is provisioned. |
| Outcome | Provisioned acceptance. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### Stage 3: Activate and Transact

Activate the merchant and process the first transaction.

| Aspect | Value |
|---|---|
| Entry criterion | Acceptance is provisioned. |
| Exit criterion | The first transaction is settled. |
| Outcome | A live merchant relationship. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-eo-operate-2jnz85`, `processes:process-fa-operate-g9zpnq` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-2jnz85`
- `processes:process-fa-operate-g9zpnq`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Merchant onboarding cycle time** (stream-level) — Elapsed days from application to first settled transaction.

## 9. Evidence and admission

**Evidence sources:** SRC-008 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-027) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
