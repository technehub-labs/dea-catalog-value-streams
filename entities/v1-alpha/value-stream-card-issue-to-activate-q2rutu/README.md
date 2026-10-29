# Card Issue to Activate

Admitted Value Stream record (`value-streams:value-stream-card-issue-to-activate-q2rutu`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-card-issue-to-activate-q2rutu` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | financial-services · industry-specific |
| Record | [`value-streams-value-stream-card-issue-to-activate-q2rutu.yaml`](./value-streams-value-stream-card-issue-to-activate-q2rutu.yaml) — authoritative |

## 2. Definition

> The end-to-end card stream from card application through production, secure delivery, and cardholder activation.

## 3. Value proposition and served party

**Outcome:** An activated card in the cardholder's hands.

## 4. Stream boundary

**Entry criterion:** A card application is approved.

**Exit criterion:** The card is received and activated by the cardholder.

**In scope** (from the record's `scope.includes`):

- Card production
- Secure delivery
- Activation

**Out of scope** (each concern owned by the named neighbour):

- Account onboarding (Onboard to Activate)
- Card payment processing (Initiate to Settle)

## 5. Value stages

Card Issue to Activate decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Produce Card

Produce and personalize the card.

| Aspect | Value |
|---|---|
| Entry criterion | A card application is approved. |
| Exit criterion | The card is produced. |
| Outcome | A personalized card. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### Stage 2: Deliver Securely

Deliver the card through secure channels.

| Aspect | Value |
|---|---|
| Entry criterion | The card is produced. |
| Exit criterion | The card is delivered to the cardholder. |
| Outcome | A delivered card. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

### Stage 3: Activate

Authenticate and activate the card with the cardholder.

| Aspect | Value |
|---|---|
| Entry criterion | The card is delivered. |
| Exit criterion | The card is activated. |
| Outcome | An activated card. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-security-management-wmzc7c` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-security-management-wmzc7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-zh9m57`
- `processes:process-pr-operate-bbe384`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Card issuance cycle time** (stream-level) — Elapsed days from approval to activation.

## 9. Evidence and admission

**Evidence sources:** SRC-008 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-026) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
