---
documentation_generated_from: value-streams-value-stream-contract-to-renewal-5x3r4x.yaml
id: value-streams:value-stream-contract-to-renewal-5x3r4x
name: Contract to Renewal
type: ValueStream
version: 1.3.0
lifecycle_status: active
value_stream_category: operational
industries:
- cross-industry
specificity: generic
entry_criterion: A contract is executed with a customer.
exit_criterion: The renewal decision is settled (renewed, renegotiated, or closed out).
outcome: A continuous, explicitly settled customer relationship.
stages:
- Execute Contract
- Serve Relationship
- Prepare Renewal
- Settle Renewal
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-marketing-xmc539
- capabilities:capability-operations-management-pm3w8k
processes:
- processes:process-ge-build-mctdgc
- processes:process-pr-improve-t6uvan
- processes:process-pr-operate-bbe384
metrics:
- Net revenue retention
- On-time renewal rate
upstream:
- value-stream-order-to-cash
downstream:
- value-stream-issue-to-resolve
evidence_sources:
- SRC-006
---

# Contract to Renewal

`value-streams:value-stream-contract-to-renewal-5x3r4x` · **operational** · cross-industry · generic

> The end-to-end post-sale relationship stream from contract execution through service of the relationship to the renewal decision.

**Outcome:** A continuous, explicitly settled customer relationship.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-contract-to-renewal-5x3r4x.yaml`](./value-streams-value-stream-contract-to-renewal-5x3r4x.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Execute Contract"]
  S2["2. Serve Relationship"]
  S3["3. Prepare Renewal"]
  S4["4. Settle Renewal"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Execute Contract** | A deal is agreed with the customer. | The contract is executed. | 2 | 1 | yes |
| 2 | **Serve Relationship** | A contract is in force. | The relationship is served through the term. | 2 | 2 | yes |
| 3 | **Prepare Renewal** | The term approaches its end. | A renewal recommendation exists. | 2 | 1 | yes |
| 4 | **Settle Renewal** | A renewal position exists. | The renewal decision is settled (renewed, renegotiated, or closed out). | 3 | 1 | yes |

### 1. Execute Contract

Execute the contract with the customer.

| Aspect | Value |
|---|---|
| Entry criterion | A deal is agreed with the customer. |
| Exit criterion | The contract is executed. |
| Outcome | An in-force customer contract. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### 2. Serve Relationship

Serve the contracted relationship through its term.

| Aspect | Value |
|---|---|
| Entry criterion | A contract is in force. |
| Exit criterion | The relationship is served through the term. |
| Outcome | A continuously served relationship. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` · `processes:process-pr-improve-t6uvan` |

### 3. Prepare Renewal

Prepare the renewal decision with the customer.

| Aspect | Value |
|---|---|
| Entry criterion | The term approaches its end. |
| Exit criterion | A renewal recommendation exists. |
| Outcome | An evidence-based renewal position. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pr-improve-t6uvan` |

### 4. Settle Renewal

Settle the renewal decision.

| Aspect | Value |
|---|---|
| Entry criterion | A renewal position exists. |
| Exit criterion | The renewal decision is settled (renewed, renegotiated, or closed out). |
| Outcome | An explicitly settled relationship. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u` · `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

## Scope boundary

**Entry:** A contract is executed with a customer.

**Exit:** The renewal decision is settled (renewed, renegotiated, or closed out).

**In scope**

- Contract execution
- Relationship service during term
- Renewal decision preparation
- Renewal settlement (renew, renegotiate, close out)

**Out of scope** (owned by the named neighbour)

- Pre-contract sales motions (Order to Cash)
- Return/credit settlement (Return to Credit)
- Employment relationships (Hire to Retire)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-marketing-xmc539`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-build-mctdgc`
- `processes:process-pr-operate-bbe384`
- `processes:process-pr-improve-t6uvan`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [order to cash](../value-stream-order-to-cash-sc8gbu/README.md) — An executed order seeds the contracted relationship.

**Downstream** (this stream's exit feeds their entry):

- [issue to resolve](../value-stream-issue-to-resolve-crmbay/README.md) — Service issues during the term flow to issue resolution.

## Measurement

- **Net revenue retention** (stage: Settle Renewal) — Retained and expanded contract value relative to expiring value. → [`dea:metric-net-revenue-retention`](https://github.com/technehub-labs/dea-catalog-metrics)
- **On-time renewal rate** (stage: Settle Renewal) — Share of renewals settled before term expiry.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-006 | commercial-process-models | Hammer & Hurdle-style enterprise process-chain literature (public summaries) |

**Rationale:** Admitted from candidate VSC-012 under CR-VS-05 (third tranche; evidence at E3/high from the SRC-006 chain-inventory observation, distinctness closed per the CR-VS-05 sweep). Subscription-economy relationship chain. Boundary vs. Hire to Retire: employment relationship vs. customer relationship (CR-VS-05 boundary statement). Boundary vs. Return to Credit: relationship forwards vs. transaction backwards.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.4 (CR-VS-05, register v0.3) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-05 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-08 metric backfill (metric_ref links to dea-catalog-metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-11 applicability backfill (cross-industry, generic) |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
