---
documentation_generated_from: value-streams-value-stream-return-to-credit-qan2dn.yaml
id: value-streams:value-stream-return-to-credit-qan2dn
name: Return to Credit
type: ValueStream
version: 1.3.0
lifecycle_status: active
value_stream_category: operational
industries:
- cross-industry
specificity: generic
entry_criterion: A customer initiates a return of goods or services.
exit_criterion: The return is settled (refund, credit, or replacement confirmed to the customer).
outcome: A fairly settled return with the customer relationship preserved.
stages:
- Initiate Return
- Receive Reverse Logistics
- Inspect and Dispose
- Settle Credit
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-operations-management-pm3w8k
processes:
- processes:process-eo-operate-44jsrp
- processes:process-eo-operate-zh9m57
- processes:process-eo-operate-zwzmbd
- processes:process-fa-operate-g9zpnq
- processes:process-fa-operate-sdppmp
- processes:process-pr-operate-bbe384
metrics:
- Return cycle time
- Return rate
upstream:
- value-stream-order-to-cash
downstream:
- value-stream-record-to-report
evidence_sources:
- SRC-006
---

# Return to Credit

`value-streams:value-stream-return-to-credit-qan2dn` · **operational** · cross-industry · generic

> The end-to-end stream from initiation of a customer return through reverse logistics and settlement by refund, credit, or replacement.

**Outcome:** A fairly settled return with the customer relationship preserved.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-return-to-credit-qan2dn.yaml`](./value-streams-value-stream-return-to-credit-qan2dn.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Initiate Return"]
  S2["2. Receive Reverse Logistics"]
  S3["3. Inspect and Dispose"]
  S4["4. Settle Credit"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Initiate Return** | A customer initiates a return of goods or services. | The return is authorized. | 2 | 1 | yes |
| 2 | **Receive Reverse Logistics** | A return is authorized. | The goods are received back. | 1 | 2 | yes |
| 3 | **Inspect and Dispose** | The goods are received back. | A disposition decision is made. | 1 | 1 | no |
| 4 | **Settle Credit** | A disposition decision exists. | The return is settled (refund, credit, or replacement confirmed to the customer). | 2 | 2 | yes |

### 1. Initiate Return

Authorize the customer's return initiation.

| Aspect | Value |
|---|---|
| Entry criterion | A customer initiates a return of goods or services. |
| Exit criterion | The return is authorized. |
| Outcome | An authorized return. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Receive Reverse Logistics

Receive the returned goods through reverse logistics.

| Aspect | Value |
|---|---|
| Entry criterion | A return is authorized. |
| Exit criterion | The goods are received back. |
| Outcome | Received returned goods. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` · `processes:process-eo-operate-zwzmbd` |

### 3. Inspect and Dispose

Inspect the return and determine disposition.

| Aspect | Value |
|---|---|
| Entry criterion | The goods are received back. |
| Exit criterion | A disposition decision is made. |
| Outcome | A settled disposition. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### 4. Settle Credit

Settle by refund, credit, or replacement.

| Aspect | Value |
|---|---|
| Entry criterion | A disposition decision exists. |
| Exit criterion | The return is settled (refund, credit, or replacement confirmed to the customer). |
| Outcome | A fairly settled return with the relationship preserved. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp` · `processes:process-fa-operate-g9zpnq` |

## Scope boundary

**Entry:** A customer initiates a return of goods or services.

**Exit:** The return is settled (refund, credit, or replacement confirmed to the customer).

**In scope**

- Return initiation and authorization
- Reverse logistics receipt
- Inspection and disposition
- Settlement (refund, credit, replacement)

**Out of scope** (owned by the named neighbour)

- Forward order flows (Order to Cash)
- Relationship-level renewal decisions (Contract to Renewal)
- Warranty strategy design (Offering Management capability)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-zh9m57`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-44jsrp`
- `processes:process-fa-operate-sdppmp`
- `processes:process-fa-operate-g9zpnq`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [order to cash](../value-stream-order-to-cash-sc8gbu/README.md) — Returns mirror fulfilled orders; goods and value flow back.

**Downstream** (this stream's exit feeds their entry):

- [record to report](../value-stream-record-to-report-zw9z2r/README.md) — Credits and refunds are recorded as transactions.

## Measurement

- **Return cycle time** (stage: Settle Credit) — Elapsed time from return initiation to settlement confirmation.
- **Return rate** (stage: Initiate Return) — Returns as a share of fulfilled orders in period. → [`dea:metric-return-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-006 | commercial-process-models | Hammer & Hurdle-style enterprise process-chain literature (public summaries) |

**Rationale:** Admitted from candidate VSC-011 under CR-VS-05 (third tranche; evidence at E3/high from the SRC-006 chain-inventory observation, distinctness closed per the CR-VS-05 sweep). Mirrors Order to Cash: goods/value flow back; entry and exit are mirrored, not shared (CR-VS-05 sweep). Boundary vs. Contract to Renewal: settles a single transaction backwards vs. the relationship forwards (CR-VS-05 boundary statement).

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
