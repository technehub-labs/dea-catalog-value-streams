# Renewal Risk to Decision

Admitted Value Stream record (`value-streams:value-stream-renewal-risk-to-decision-rcjb6b`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-renewal-risk-to-decision-rcjb6b` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | insurance · industry-specific |
| Record | [`value-streams-value-stream-renewal-risk-to-decision-rcjb6b.yaml`](./value-streams-value-stream-renewal-risk-to-decision-rcjb6b.yaml) — authoritative |

## 2. Definition

> The renewal stream from renewal-risk review through re-underwriting to the renewal decision.

## 3. Value proposition and served party

**Outcome:** A data-driven renewal decision communicated before expiry.

## 4. Stream boundary

**Entry criterion:** A policy approaches renewal.

**Exit criterion:** The renewal decision is made and communicated.

**In scope** (from the record's `scope.includes`):

- Renewal risk review
- Re-underwriting
- Decision and communication

**Out of scope** (each concern owned by the named neighbour):

- Binding (Quote to Bind)
- Broker channel management

## 5. Value stages

Renewal Risk to Decision decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Review Renewal Risk

Review the risk and loss experience.

| Aspect | Value |
|---|---|
| Entry criterion | A policy approaches renewal. |
| Exit criterion | The renewal review is complete. |
| Outcome | A completed review. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

### Stage 2: Re-underwrite

Re-underwrite the risk for the new term.

| Aspect | Value |
|---|---|
| Entry criterion | The review is complete. |
| Exit criterion | Terms for the new term are set. |
| Outcome | Set renewal terms. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 3: Decide and Communicate

Decide and communicate the renewal offer.

| Aspect | Value |
|---|---|
| Entry criterion | Terms are set. |
| Exit criterion | The decision is communicated. |
| Outcome | A communicated decision. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-improve-t6uvan` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-customer-management-f3n8wb`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-operate-ucxpz4`
- `processes:process-ge-operate-tpenm6`
- `processes:process-pr-improve-t6uvan`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-quote-to-bind` — Non-renewed risks re-enter underwriting.

**Downstream streams:** none recorded.

## 8. Measurement

- **Renewal retention rate** (stream-level) — Share of expiring policies renewed.

## 9. Evidence and admission

**Evidence sources:** SRC-009 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-032) from the CR-VS-11 industry evidence register extension. Industry-specific chain (insurance); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
