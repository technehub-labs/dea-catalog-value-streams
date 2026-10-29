---
documentation_generated_from: value-streams-value-stream-usage-to-bill-tyf4zn.yaml
id: value-streams:value-stream-usage-to-bill-tyf4zn
name: Usage to Bill
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- telecommunications
specificity: industry-specific
entry_criterion: Usage events are recorded on an activated service.
exit_criterion: The customer bill for the period is produced and accepted.
outcome: An accurate, explained bill for consumed services.
stages:
- Mediate Usage
- Rate Usage
- Produce Bill
- Resolve Inquiries
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-technology-management-maus5n
processes:
- processes:process-fa-operate-g9zpnq
- processes:process-fa-operate-sdppmp
- processes:process-pr-operate-bbe384
metrics:
- Billing accuracy rate
upstream:
- value-stream-order-to-activation
downstream: []
evidence_sources:
- SRC-010
---

# Usage to Bill

`value-streams:value-stream-usage-to-bill-tyf4zn` · **operational** · telecommunications · industry-specific

> The telecom revenue stream from usage mediation through rating to an accurate customer bill.

**Outcome:** An accurate, explained bill for consumed services.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-usage-to-bill-tyf4zn.yaml`](./value-streams-value-stream-usage-to-bill-tyf4zn.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Mediate Usage"]
  S2["2. Rate Usage"]
  S3["3. Produce Bill"]
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
| 1 | **Mediate Usage** | Usage events occur. | Usage records are mediated. | 2 | 1 | no |
| 2 | **Rate Usage** | Usage is mediated. | Usage is rated. | 2 | 1 | no |
| 3 | **Produce Bill** | Usage is rated. | The bill is issued. | 2 | 1 | yes |
| 4 | **Resolve Inquiries** | The bill is issued. | Inquiries are resolved. | 1 | 1 | yes |

### 1. Mediate Usage

Collect and mediate usage events.

| Aspect | Value |
|---|---|
| Entry criterion | Usage events occur. |
| Exit criterion | Usage records are mediated. |
| Outcome | Mediated usage. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### 2. Rate Usage

Rate the mediated usage per the price plan.

| Aspect | Value |
|---|---|
| Entry criterion | Usage is mediated. |
| Exit criterion | Usage is rated. |
| Outcome | Rated usage. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### 3. Produce Bill

Produce and issue the customer bill.

| Aspect | Value |
|---|---|
| Entry criterion | Usage is rated. |
| Exit criterion | The bill is issued. |
| Outcome | An issued bill. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

### 4. Resolve Inquiries

Resolve bill inquiries and disputes.

| Aspect | Value |
|---|---|
| Entry criterion | The bill is issued. |
| Exit criterion | Inquiries are resolved. |
| Outcome | An accepted bill. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## Scope boundary

**Entry:** Usage events are recorded on an activated service.

**Exit:** The customer bill for the period is produced and accepted.

**In scope**

- Usage mediation and collection
- Rating and discounting
- Bill production
- Bill inquiry resolution

**Out of scope** (owned by the named neighbour)

- Service activation (Order to Activation)
- Collections

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-customer-management-f3n8wb`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-sdppmp`
- `processes:process-pr-operate-bbe384`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [order to activation](../value-stream-order-to-activation-uxqth5/README.md) — Activated services generate usage.

**Downstream:** none recorded.

## Measurement

- **Billing accuracy rate** (stream-level) — Billed amount variance from rated usage.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-010 | industry-reference-model | Telecommunications industry reference models (eTOM category-level structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-038) from the CR-VS-11 industry evidence register extension. Industry-specific chain (telecommunications); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
