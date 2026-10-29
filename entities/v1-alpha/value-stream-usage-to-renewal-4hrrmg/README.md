# Usage to Renewal

Admitted Value Stream record (`value-streams:value-stream-usage-to-renewal-4hrrmg`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-usage-to-renewal-4hrrmg` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | technology · industry-specific |
| Record | [`value-streams-value-stream-usage-to-renewal-4hrrmg.yaml`](./value-streams-value-stream-usage-to-renewal-4hrrmg.yaml) — authoritative |

## 2. Definition

> The SaaS retention stream from usage monitoring through health scoring to the renewal decision.

## 3. Value proposition and served party

**Outcome:** A data-driven renewal decision settled with the customer.

## 4. Stream boundary

**Entry criterion:** A subscription period begins.

**Exit criterion:** The renewal is settled (renewed, expanded, or churned).

**In scope** (from the record's `scope.includes`):

- Usage and health monitoring
- Intervention
- Renewal decision and settlement

**Out of scope** (each concern owned by the named neighbour):

- Sales upsell
- Billing operations

## 5. Value stages

Usage to Renewal decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Monitor Usage

Monitor usage and product health.

| Aspect | Value |
|---|---|
| Entry criterion | The period begins. |
| Exit criterion | Health is tracked. |
| Outcome | Tracked health. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

### Stage 2: Intervene

Intervene on health risks.

| Aspect | Value |
|---|---|
| Entry criterion | Health risks emerge. |
| Exit criterion | Interventions are delivered. |
| Outcome | Delivered interventions. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pr-improve-t6uvan` |

### Stage 3: Settle Renewal

Settle the renewal decision.

| Aspect | Value |
|---|---|
| Entry criterion | The period ends. |
| Exit criterion | The renewal is settled. |
| Outcome | A settled renewal. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-pr-improve-t6uvan`, `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-operate-ucxpz4`
- `processes:process-pr-improve-t6uvan`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-contract-to-renewal` — The SaaS specialization of relationship renewal.

**Downstream streams:** none recorded.

## 8. Measurement

- **Net revenue retention** (stage: Settle Renewal) — Retained and expanded subscription value. → [`dea:metric-net-revenue-retention`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-019 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-108) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
