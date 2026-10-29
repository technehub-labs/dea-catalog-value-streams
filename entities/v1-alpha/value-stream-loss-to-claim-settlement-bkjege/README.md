# Loss to Claim Settlement

Admitted Value Stream record (`value-streams:value-stream-loss-to-claim-settlement-bkjege`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-loss-to-claim-settlement-bkjege` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | insurance · industry-specific |
| Record | [`value-streams-value-stream-loss-to-claim-settlement-bkjege.yaml`](./value-streams-value-stream-loss-to-claim-settlement-bkjege.yaml) — authoritative |

## 2. Definition

> The end-to-end claims stream from first notice of loss through adjustment to claim settlement and payment.

## 3. Value proposition and served party

**Outcome:** A fairly adjusted, settled, and paid claim.

## 4. Stream boundary

**Entry criterion:** A loss is notified.

**Exit criterion:** The claim is settled and paid.

**In scope** (from the record's `scope.includes`):

- First notice of loss and coverage verification
- Adjustment and valuation
- Settlement agreement
- Payment and closure

**Out of scope** (each concern owned by the named neighbour):

- Underwriting (Quote to Bind)
- Subrogation and recovery

## 5. Value stages

Loss to Claim Settlement decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Register Loss

Register the loss notice and verify coverage.

| Aspect | Value |
|---|---|
| Entry criterion | A loss is notified. |
| Exit criterion | The claim is registered and covered. |
| Outcome | A registered, covered claim. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Adjust

Investigate and adjust the claim valuation.

| Aspect | Value |
|---|---|
| Entry criterion | The claim is covered. |
| Exit criterion | The adjustment is complete. |
| Outcome | A completed adjustment. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Agree Settlement

Agree the settlement with the claimant.

| Aspect | Value |
|---|---|
| Entry criterion | The adjustment is complete. |
| Exit criterion | The settlement is agreed. |
| Outcome | An agreed settlement. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 4: Pay and Close

Pay the settlement and close the claim.

| Aspect | Value |
|---|---|
| Entry criterion | The settlement is agreed. |
| Exit criterion | The claim is paid and closed. |
| Outcome | A settled, closed claim. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-zwaes5`
- `processes:process-ge-build-mctdgc`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-quote-to-bind` — Coverage terms originate at underwriting.

**Downstream streams:** none recorded.

## 8. Measurement

- **Claims leakage rate** (stage: Pay and Close) — Payment error and leakage as a share of claims cost. → [`dea:metric-claims-leakage-rate`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Claims frequency rate** (stage: Register Loss) — Claims per exposure unit. → [`dea:metric-claims-frequency-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-009 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-030) from the CR-VS-11 industry evidence register extension. Industry-specific chain (insurance); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
