---
documentation_generated_from: value-streams-value-stream-hire-to-retire-n6szcc.yaml
id: value-streams:value-stream-hire-to-retire-n6szcc
name: Hire to Retire
type: ValueStream
version: 1.3.0
lifecycle_status: active
value_stream_category: support
industries:
- cross-industry
specificity: generic
entry_criterion: A workforce need is identified and a requisition is raised.
exit_criterion: The employment relationship ends and obligations are settled.
outcome: A staffed, productive workforce with settled employment obligations.
stages:
- Requisition Workforce
- Hire
- Develop and Administer
- Separate
capabilities:
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-workforce-management-9e8d8s
- capabilities:capability-workforce-planning-b43rhm
processes:
- processes:process-ao-conceive-e3u8s2
- processes:process-ao-conceive-z6m6p5
- processes:process-ao-operate-38qyc6
- processes:process-ao-operate-87q5mk
- processes:process-ao-operate-dg9q4h
- processes:process-ao-retire-g3eyr8
metrics:
- Time to hire
- Voluntary turnover rate
upstream: []
downstream: []
evidence_sources:
- SRC-006
---

# Hire to Retire

`value-streams:value-stream-hire-to-retire-n6szcc` · **support** · cross-industry · generic

> The end-to-end stream across the employment lifecycle from workforce requisition through hiring, development, and separation.

**Outcome:** A staffed, productive workforce with settled employment obligations.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-hire-to-retire-n6szcc.yaml`](./value-streams-value-stream-hire-to-retire-n6szcc.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Requisition Workforce"]
  S2["2. Hire"]
  S3["3. Develop and Administer"]
  S4["4. Separate"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Requisition Workforce** | A workforce need is identified. | An approved requisition exists. | 2 | 1 | no |
| 2 | **Hire** | An approved requisition exists. | A hire is made and employment starts. | 1 | 1 | no |
| 3 | **Develop and Administer** | Employment has started. | The workforce is productive and administered. | 2 | 3 | no |
| 4 | **Separate** | A separation is initiated. | The employment relationship ends and obligations are settled. | 2 | 2 | no |

### 1. Requisition Workforce

Identify the workforce need and raise the requisition.

| Aspect | Value |
|---|---|
| Entry criterion | A workforce need is identified. |
| Exit criterion | An approved requisition exists. |
| Outcome | An approved hiring mandate. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-workforce-planning-b43rhm` · `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-ao-conceive-z6m6p5` |

### 2. Hire

Source, select, and hire against the requisition.

| Aspect | Value |
|---|---|
| Entry criterion | An approved requisition exists. |
| Exit criterion | A hire is made and employment starts. |
| Outcome | A staffed position. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-ao-conceive-e3u8s2` |

### 3. Develop and Administer

Develop the workforce and administer employment.

| Aspect | Value |
|---|---|
| Entry criterion | Employment has started. |
| Exit criterion | The workforce is productive and administered. |
| Outcome | A productive, administered workforce. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-workforce-management-9e8d8s` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-ao-operate-87q5mk` · `processes:process-ao-operate-dg9q4h` · `processes:process-ao-operate-38qyc6` |

### 4. Separate

End the employment relationship and settle obligations.

| Aspect | Value |
|---|---|
| Entry criterion | A separation is initiated. |
| Exit criterion | The employment relationship ends and obligations are settled. |
| Outcome | A settled separation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-workforce-management-9e8d8s` · `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-ao-retire-g3eyr8` · `processes:process-ao-operate-38qyc6` |

## Scope boundary

**Entry:** A workforce need is identified and a requisition is raised.

**Exit:** The employment relationship ends and obligations are settled.

**In scope**

- Workforce requisition and hiring
- Onboarding and development
- Workforce administration and payroll
- Separation and obligation settlement

**Out of scope** (owned by the named neighbour)

- Supplier settlement (Procure to Pay)
- Asset lifecycle (Acquire to Retire)
- Organizational design as a standing concern (Organization Design capability)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-workforce-planning-b43rhm`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ao-conceive-z6m6p5`
- `processes:process-ao-conceive-e3u8s2`
- `processes:process-ao-operate-87q5mk`
- `processes:process-ao-operate-dg9q4h`
- `processes:process-ao-operate-38qyc6`
- `processes:process-ao-retire-g3eyr8`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Time to hire** (stage: Hire) — Elapsed days from requisition approval to hire acceptance. → [`dea:metric-time-to-hire`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Voluntary turnover rate** (stage: Separate) — Share of workforce separating voluntarily in period. → [`dea:metric-voluntary-turnover-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-006 | commercial-process-models | Hammer & Hurdle-style enterprise process-chain literature (public summaries) |

**Rationale:** Admitted from candidate VSC-006 under CR-VS-03 (evidence at E3/high, distinctness closed per CR-VS-02). Served party is internal (manager/employee), distinct from external-customer chains. Boundary vs. Procure to Pay: settlement counterparty is the discriminator (CR-VS-02 boundary statement).

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.1 (CR-VS-01, PR #3) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-03 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-08 metric backfill (metric_ref links to dea-catalog-metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-11 applicability backfill (cross-industry, generic) |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
