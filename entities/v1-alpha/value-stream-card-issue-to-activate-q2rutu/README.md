---
documentation_generated_from: value-streams-value-stream-card-issue-to-activate-q2rutu.yaml
id: value-streams:value-stream-card-issue-to-activate-q2rutu
name: Card Issue to Activate
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- financial-services
specificity: industry-specific
entry_criterion: A card application is approved.
exit_criterion: The card is received and activated by the cardholder.
outcome: An activated card in the cardholder's hands.
stages:
- Produce Card
- Deliver Securely
- Activate
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-security-management-wmzc7c
- capabilities:capability-technology-management-maus5n
processes:
- processes:process-eo-build-j9z3q4
- processes:process-eo-operate-zh9m57
- processes:process-pr-operate-bbe384
metrics:
- Card issuance cycle time
upstream: []
downstream: []
evidence_sources:
- SRC-008
---

# Card Issue to Activate

`value-streams:value-stream-card-issue-to-activate-q2rutu` · **operational** · financial-services · industry-specific

> The end-to-end card stream from card application through production, secure delivery, and cardholder activation.

**Outcome:** An activated card in the cardholder's hands.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-card-issue-to-activate-q2rutu.yaml`](./value-streams-value-stream-card-issue-to-activate-q2rutu.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Produce Card"]
  S2["2. Deliver Securely"]
  S3["3. Activate"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Produce Card** | A card application is approved. | The card is produced. | 2 | 1 | no |
| 2 | **Deliver Securely** | The card is produced. | The card is delivered to the cardholder. | 2 | 1 | yes |
| 3 | **Activate** | The card is delivered. | The card is activated. | 2 | 1 | yes |

### 1. Produce Card

Produce and personalize the card.

| Aspect | Value |
|---|---|
| Entry criterion | A card application is approved. |
| Exit criterion | The card is produced. |
| Outcome | A personalized card. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### 2. Deliver Securely

Deliver the card through secure channels.

| Aspect | Value |
|---|---|
| Entry criterion | The card is produced. |
| Exit criterion | The card is delivered to the cardholder. |
| Outcome | A delivered card. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

### 3. Activate

Authenticate and activate the card with the cardholder.

| Aspect | Value |
|---|---|
| Entry criterion | The card is delivered. |
| Exit criterion | The card is activated. |
| Outcome | An activated card. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-security-management-wmzc7c` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## Scope boundary

**Entry:** A card application is approved.

**Exit:** The card is received and activated by the cardholder.

**In scope**

- Card production
- Secure delivery
- Activation

**Out of scope** (owned by the named neighbour)

- Account onboarding (Onboard to Activate)
- Card payment processing (Initiate to Settle)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-security-management-wmzc7c`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-zh9m57`
- `processes:process-pr-operate-bbe384`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Card issuance cycle time** (stream-level) — Elapsed days from approval to activation.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-008 | industry-reference-model | Banking industry reference models (lending and payments chains, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-026) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
