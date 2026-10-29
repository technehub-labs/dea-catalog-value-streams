# Onboard to Activate

Admitted Value Stream record (`value-streams:value-stream-onboard-to-activate-ft6jk9`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-onboard-to-activate-ft6jk9` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | financial-services · industry-specific |
| Record | [`value-streams-value-stream-onboard-to-activate-ft6jk9.yaml`](./value-streams-value-stream-onboard-to-activate-ft6jk9.yaml) — authoritative |

## 2. Definition

> The end-to-end customer-onboarding stream from account application through identity verification (KYC) and due diligence to an activated account.

## 3. Value proposition and served party

**Outcome:** A KYC-cleared, activated account for the customer.

## 4. Stream boundary

**Entry criterion:** An account application is received.

**Exit criterion:** The account is activated after identity verification and due diligence.

**In scope** (from the record's `scope.includes`):

- Application capture
- Identity verification (KYC)
- Due-diligence clearing
- Activation and welcome

**Out of scope** (each concern owned by the named neighbour):

- Product application (Application to Book)
- Ongoing relationship service (Contract to Renewal)

## 5. Value stages

Onboard to Activate decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Capture Application

Capture the account application.

| Aspect | Value |
|---|---|
| Entry criterion | An application is received. |
| Exit criterion | The application is captured and complete. |
| Outcome | A complete application. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Verify Identity

Verify identity per KYC requirements.

| Aspect | Value |
|---|---|
| Entry criterion | The application is complete. |
| Exit criterion | Identity is verified. |
| Outcome | A verified identity. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 3: Clear Due Diligence

Complete due-diligence checks and risk classification.

| Aspect | Value |
|---|---|
| Entry criterion | Identity is verified. |
| Exit criterion | Due diligence is cleared. |
| Outcome | A due-diligence-cleared customer. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 4: Activate

Open and activate the account and welcome the customer.

| Aspect | Value |
|---|---|
| Entry criterion | Due diligence is cleared. |
| Exit criterion | The account is activated. |
| Outcome | An activated account. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-tpenm6`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-application-to-book` — Lending follows the same KYC-cleared onboarding.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-contract-to-renewal` — The activated relationship is served through its term.

## 8. Measurement

- **Know-your-customer onboarding time** (stage: Activate) — Elapsed time from application to activation. → [`dea:metric-know-your-customer-onboarding-time`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Onboarding completion rate** (stage: Activate) — Share of started onboardings completed. → [`dea:metric-onboarding-completion-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-008, SRC-012 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-022) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
