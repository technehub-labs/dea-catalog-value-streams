---
documentation_generated_from: value-streams-value-stream-meter-to-bill-6bhvk9.yaml
id: value-streams:value-stream-meter-to-bill-6bhvk9
name: Meter to Bill
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- utilities-energy
specificity: industry-specific
entry_criterion: Consumption occurs at a metered point.
exit_criterion: The period bill is produced and accepted.
outcome: An accurate, explained bill for consumed energy.
stages:
- Collect Meter Data
- Validate and Estimate
- Rate and Bill
- Resolve Inquiries
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-risk-management-h9uxdw
- capabilities:capability-technology-management-maus5n
processes:
- processes:process-fa-operate-4xn4d6
- processes:process-fa-operate-g9zpnq
- processes:process-fa-operate-sdppmp
- processes:process-pr-operate-bbe384
metrics:
- Estimated-bill rate
upstream: []
downstream: []
evidence_sources:
- SRC-011
---

# Meter to Bill

`value-streams:value-stream-meter-to-bill-6bhvk9` · **operational** · utilities-energy · industry-specific

> The end-to-end utility revenue stream from consumption measurement through meter data collection and validation to an accurate bill.

**Outcome:** An accurate, explained bill for consumed energy.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-meter-to-bill-6bhvk9.yaml`](./value-streams-value-stream-meter-to-bill-6bhvk9.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Collect Meter Data"]
  S2["2. Validate and Estimate"]
  S3["3. Rate and Bill"]
  S4["4. Resolve Inquiries"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Collect Meter Data** | Consumption occurs. | Meter data is collected. | 2 | 1 | no |
| 2 | **Validate and Estimate** | Data is collected. | Validated consumption exists. | 2 | 1 | no |
| 3 | **Rate and Bill** | Consumption is validated. | The bill is issued. | 2 | 1 | yes |
| 4 | **Resolve Inquiries** | The bill is issued. | Inquiries are resolved. | 1 | 1 | yes |

### 1. Collect Meter Data

Collect consumption data from the meter.

| Aspect | Value |
|---|---|
| Entry criterion | Consumption occurs. |
| Exit criterion | Meter data is collected. |
| Outcome | Collected meter data. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### 2. Validate and Estimate

Validate the data and estimate gaps.

| Aspect | Value |
|---|---|
| Entry criterion | Data is collected. |
| Exit criterion | Validated consumption exists. |
| Outcome | Validated consumption. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-fa-operate-4xn4d6` |

### 3. Rate and Bill

Rate consumption and produce the bill.

| Aspect | Value |
|---|---|
| Entry criterion | Consumption is validated. |
| Exit criterion | The bill is issued. |
| Outcome | An issued bill. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

### 4. Resolve Inquiries

Resolve bill inquiries.

| Aspect | Value |
|---|---|
| Entry criterion | The bill is issued. |
| Exit criterion | Inquiries are resolved. |
| Outcome | An accepted bill. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## Scope boundary

**Entry:** Consumption occurs at a metered point.

**Exit:** The period bill is produced and accepted.

**In scope**

- Meter data collection
- Validation and estimation
- Rating and bill production
- Bill inquiry resolution

**Out of scope** (owned by the named neighbour)

- Connection services (Apply to Connect)
- Credit and collections

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-customer-management-f3n8wb`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-4xn4d6`
- `processes:process-fa-operate-sdppmp`
- `processes:process-pr-operate-bbe384`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Estimated-bill rate** (stream-level) — Share of bills based on estimated rather than actual reads.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-011 | industry-reference-model | Utilities industry reference models (metering and retail-energy chains, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-043) from the CR-VS-11 industry evidence register extension. Industry-specific chain (utilities-energy); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
