# Deposit to Maturity

Admitted Value Stream record (`value-streams:value-stream-deposit-to-maturity-gsbm8e`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-deposit-to-maturity-gsbm8e` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | financial-services · industry-specific |
| Record | [`value-streams-value-stream-deposit-to-maturity-gsbm8e.yaml`](./value-streams-value-stream-deposit-to-maturity-gsbm8e.yaml) — authoritative |

## 2. Definition

> The end-to-end term-deposit stream from deposit opening through interest accrual to maturity and redemption or renewal.

## 3. Value proposition and served party

**Outcome:** A term deposit held to maturity and redeemed or renewed.

## 4. Stream boundary

**Entry criterion:** A customer opens a term deposit.

**Exit criterion:** The deposit matures and is redeemed or renewed.

**In scope** (from the record's `scope.includes`):

- Deposit opening
- Interest accrual and statements
- Maturity handling
- Redemption or renewal

**Out of scope** (each concern owned by the named neighbour):

- Onboarding (Onboard to Activate)
- Trading-book operations

## 5. Value stages

Deposit to Maturity decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Open Deposit

Open and fund the term deposit.

| Aspect | Value |
|---|---|
| Entry criterion | A customer opens a term deposit. |
| Exit criterion | The deposit is opened and funded. |
| Outcome | A funded term deposit. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Accrue and Report

Accrue interest and issue statements.

| Aspect | Value |
|---|---|
| Entry criterion | The deposit is funded. |
| Exit criterion | Interest accrues and statements issue on schedule. |
| Outcome | An informed deposit holder. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

### Stage 3: Handle Maturity

Prepare maturity instructions with the customer.

| Aspect | Value |
|---|---|
| Entry criterion | The deposit approaches maturity. |
| Exit criterion | Maturity instructions are agreed. |
| Outcome | Agreed maturity instructions. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-improve-t6uvan` |

### Stage 4: Redeem or Renew

Redeem or renew the deposit.

| Aspect | Value |
|---|---|
| Entry criterion | Instructions are agreed. |
| Exit criterion | The deposit is redeemed or renewed. |
| Outcome | A settled maturity. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-ycba3k`
- `processes:process-pr-improve-t6uvan`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Deposit renewal rate** (stream-level) — Share of maturing deposits renewed.

## 9. Evidence and admission

**Evidence sources:** SRC-008 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-024) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
