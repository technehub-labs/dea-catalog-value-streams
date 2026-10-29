---
documentation_generated_from: value-streams-value-stream-usage-to-renewal-4hrrmg.yaml
id: value-streams:value-stream-usage-to-renewal-4hrrmg
name: Usage to Renewal
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- technology
specificity: industry-specific
entry_criterion: A subscription period begins.
exit_criterion: The renewal is settled (renewed, expanded, or churned).
outcome: A data-driven renewal decision settled with the customer.
stages:
- Monitor Usage
- Intervene
- Settle Renewal
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-marketing-xmc539
processes:
- processes:process-fa-operate-sdppmp
- processes:process-pr-improve-t6uvan
- processes:process-sd-operate-ucxpz4
metrics:
- Net revenue retention
upstream:
- value-stream-contract-to-renewal
downstream: []
evidence_sources:
- SRC-019
---

# Usage to Renewal

`value-streams:value-stream-usage-to-renewal-4hrrmg` · **operational** · technology · industry-specific

> The SaaS retention stream from usage monitoring through health scoring to the renewal decision.

**Outcome:** A data-driven renewal decision settled with the customer.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-usage-to-renewal-4hrrmg.yaml`](./value-streams-value-stream-usage-to-renewal-4hrrmg.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Monitor Usage"]
  S2["2. Intervene"]
  S3["3. Settle Renewal"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Monitor Usage** | The period begins. | Health is tracked. | 2 | 1 | no |
| 2 | **Intervene** | Health risks emerge. | Interventions are delivered. | 2 | 1 | yes |
| 3 | **Settle Renewal** | The period ends. | The renewal is settled. | 2 | 2 | yes |

### 1. Monitor Usage

Monitor usage and product health.

| Aspect | Value |
|---|---|
| Entry criterion | The period begins. |
| Exit criterion | Health is tracked. |
| Outcome | Tracked health. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

### 2. Intervene

Intervene on health risks.

| Aspect | Value |
|---|---|
| Entry criterion | Health risks emerge. |
| Exit criterion | Interventions are delivered. |
| Outcome | Delivered interventions. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pr-improve-t6uvan` |

### 3. Settle Renewal

Settle the renewal decision.

| Aspect | Value |
|---|---|
| Entry criterion | The period ends. |
| Exit criterion | The renewal is settled. |
| Outcome | A settled renewal. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-pr-improve-t6uvan` · `processes:process-fa-operate-sdppmp` |

## Scope boundary

**Entry:** A subscription period begins.

**Exit:** The renewal is settled (renewed, expanded, or churned).

**In scope**

- Usage and health monitoring
- Intervention
- Renewal decision and settlement

**Out of scope** (owned by the named neighbour)

- Sales upsell
- Billing operations

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-operate-ucxpz4`
- `processes:process-pr-improve-t6uvan`
- `processes:process-fa-operate-sdppmp`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [contract to renewal](../value-stream-contract-to-renewal-5x3r4x/README.md) — The SaaS specialization of relationship renewal.

**Downstream:** none recorded.

## Measurement

- **Net revenue retention** (stage: Settle Renewal) — Retained and expanded subscription value. → [`dea:metric-net-revenue-retention`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-019 | industry-reference-model | Technology / SaaS product chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-108) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
