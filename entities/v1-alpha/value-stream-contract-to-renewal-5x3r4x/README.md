# Contract to Renewal

Admitted Value Stream record (`value-streams:value-stream-contract-to-renewal-5x3r4x`, v1.3.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-contract-to-renewal-5x3r4x` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.3.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | cross-industry · generic |
| Record | [`value-streams-value-stream-contract-to-renewal-5x3r4x.yaml`](./value-streams-value-stream-contract-to-renewal-5x3r4x.yaml) — authoritative |

## 2. Definition

> The end-to-end post-sale relationship stream from contract execution through service of the relationship to the renewal decision.

## 3. Value proposition and served party

**Outcome:** A continuous, explicitly settled customer relationship.

## 4. Stream boundary

**Entry criterion:** A contract is executed with a customer.

**Exit criterion:** The renewal decision is settled (renewed, renegotiated, or closed out).

**In scope** (from the record's `scope.includes`):

- Contract execution
- Relationship service during term
- Renewal decision preparation
- Renewal settlement (renew, renegotiate, close out)

**Out of scope** (each concern owned by the named neighbour):

- Pre-contract sales motions (Order to Cash)
- Return/credit settlement (Return to Credit)
- Employment relationships (Hire to Retire)

## 5. Value stages

Contract to Renewal decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Execute Contract

Execute the contract with the customer.

| Aspect | Value |
|---|---|
| Entry criterion | A deal is agreed with the customer. |
| Exit criterion | The contract is executed. |
| Outcome | An in-force customer contract. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 2: Serve Relationship

Serve the contracted relationship through its term.

| Aspect | Value |
|---|---|
| Entry criterion | A contract is in force. |
| Exit criterion | The relationship is served through the term. |
| Outcome | A continuously served relationship. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384`, `processes:process-pr-improve-t6uvan` |

### Stage 3: Prepare Renewal

Prepare the renewal decision with the customer.

| Aspect | Value |
|---|---|
| Entry criterion | The term approaches its end. |
| Exit criterion | A renewal recommendation exists. |
| Outcome | An evidence-based renewal position. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pr-improve-t6uvan` |

### Stage 4: Settle Renewal

Settle the renewal decision.

| Aspect | Value |
|---|---|
| Entry criterion | A renewal position exists. |
| Exit criterion | The renewal decision is settled (renewed, renegotiated, or closed out). |
| Outcome | An explicitly settled relationship. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-marketing-xmc539`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-build-mctdgc`
- `processes:process-pr-operate-bbe384`
- `processes:process-pr-improve-t6uvan`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-order-to-cash` — An executed order seeds the contracted relationship.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-issue-to-resolve` — Service issues during the term flow to issue resolution.

## 8. Measurement

- **Net revenue retention** (stage: Settle Renewal) — Retained and expanded contract value relative to expiring value. → [`dea:metric-net-revenue-retention`](https://github.com/technehub-labs/dea-catalog-metrics)
- **On-time renewal rate** (stage: Settle Renewal) — Share of renewals settled before term expiry.

## 9. Evidence and admission

**Evidence sources:** SRC-006 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted from candidate VSC-012 under CR-VS-05 (third tranche; evidence at E3/high from the SRC-006 chain-inventory observation, distinctness closed per the CR-VS-05 sweep). Subscription-economy relationship chain. Boundary vs. Hire to Retire: employment relationship vs. customer relationship (CR-VS-05 boundary statement). Boundary vs. Return to Credit: relationship forwards vs. transaction backwards.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.4 (CR-VS-05, register v0.3) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-05 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-08 metric backfill (metric_ref links to dea-catalog-metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-11 applicability backfill (cross-industry, generic) |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
