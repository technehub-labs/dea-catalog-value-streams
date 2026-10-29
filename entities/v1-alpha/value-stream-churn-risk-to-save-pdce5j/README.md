# Churn Risk to Save

Admitted Value Stream record (`value-streams:value-stream-churn-risk-to-save-pdce5j`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-churn-risk-to-save-pdce5j` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | telecommunications · industry-specific |
| Record | [`value-streams-value-stream-churn-risk-to-save-pdce5j.yaml`](./value-streams-value-stream-churn-risk-to-save-pdce5j.yaml) — authoritative |

## 2. Definition

> The retention stream from churn-risk identification through targeted intervention to a saved or churned decision.

## 3. Value proposition and served party

**Outcome:** At-risk customers retained or consciously churned.

## 4. Stream boundary

**Entry criterion:** A churn-risk score crosses threshold.

**Exit criterion:** The customer is retained or churns with the decision recorded.

**In scope** (from the record's `scope.includes`):

- Risk identification
- Intervention design and offer
- Outcome tracking

**Out of scope** (each concern owned by the named neighbour):

- Acquisition campaigns
- Contractual renewal (Contract to Renewal)

## 5. Value stages

Churn Risk to Save decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Identify Risk

Identify at-risk customers from behavior and sentiment.

| Aspect | Value |
|---|---|
| Entry criterion | A risk threshold is crossed. |
| Exit criterion | At-risk customers are identified. |
| Outcome | An at-risk list. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

### Stage 2: Intervene

Design and deliver the save intervention.

| Aspect | Value |
|---|---|
| Entry criterion | The list is identified. |
| Exit criterion | Interventions are delivered. |
| Outcome | Delivered interventions. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-improve-t6uvan` |

### Stage 3: Track Outcome

Track retention outcome per intervention.

| Aspect | Value |
|---|---|
| Entry criterion | Interventions are delivered. |
| Exit criterion | Outcomes are recorded. |
| Outcome | Recorded outcomes. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-performance-management-5fxren`, `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-operate-ucxpz4`
- `processes:process-pr-improve-t6uvan`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-contract-to-renewal` — Saved customers flow to term renewal.

**Downstream streams:** none recorded.

## 8. Measurement

- **Churn rate (telecom)** (stage: Track Outcome) — Subscriber churn per period. → [`dea:metric-churn-rate-telecom`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-010 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-040) from the CR-VS-11 industry evidence register extension. Industry-specific chain (telecommunications); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
