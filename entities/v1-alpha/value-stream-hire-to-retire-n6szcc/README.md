# Hire to Retire

Admitted Value Stream record (`value-streams:value-stream-hire-to-retire-n6szcc`, v1.2.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-hire-to-retire-n6szcc` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.2.0 · active |
| Metamodel pin | 1.0.0 |
| Record | [`value-streams-value-stream-hire-to-retire-n6szcc.yaml`](./value-streams-value-stream-hire-to-retire-n6szcc.yaml) — authoritative |

## 2. Definition

> The end-to-end stream across the employment lifecycle from workforce requisition through hiring, development, and separation.

## 3. Value proposition and served party

**Outcome:** A staffed, productive workforce with settled employment obligations.

## 4. Stream boundary

**Entry criterion:** A workforce need is identified and a requisition is raised.

**Exit criterion:** The employment relationship ends and obligations are settled.

**In scope** (from the record's `scope.includes`):

- Workforce requisition and hiring
- Onboarding and development
- Workforce administration and payroll
- Separation and obligation settlement

**Out of scope** (each concern owned by the named neighbour):

- Supplier settlement (Procure to Pay)
- Asset lifecycle (Acquire to Retire)
- Organizational design as a standing concern (Organization Design capability)

## 5. Value stages

Hire to Retire decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Requisition Workforce

Identify the workforce need and raise the requisition.

| Aspect | Value |
|---|---|
| Entry criterion | A workforce need is identified. |
| Exit criterion | An approved requisition exists. |
| Outcome | An approved hiring mandate. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-workforce-planning-b43rhm`, `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-ao-conceive-z6m6p5` |

### Stage 2: Hire

Source, select, and hire against the requisition.

| Aspect | Value |
|---|---|
| Entry criterion | An approved requisition exists. |
| Exit criterion | A hire is made and employment starts. |
| Outcome | A staffed position. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-ao-conceive-e3u8s2` |

### Stage 3: Develop and Administer

Develop the workforce and administer employment.

| Aspect | Value |
|---|---|
| Entry criterion | Employment has started. |
| Exit criterion | The workforce is productive and administered. |
| Outcome | A productive, administered workforce. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-workforce-management-9e8d8s`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-ao-operate-87q5mk`, `processes:process-ao-operate-dg9q4h`, `processes:process-ao-operate-38qyc6` |

### Stage 4: Separate

End the employment relationship and settle obligations.

| Aspect | Value |
|---|---|
| Entry criterion | A separation is initiated. |
| Exit criterion | The employment relationship ends and obligations are settled. |
| Outcome | A settled separation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-workforce-management-9e8d8s`, `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-ao-retire-g3eyr8`, `processes:process-ao-operate-38qyc6` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-workforce-planning-b43rhm`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ao-conceive-z6m6p5`
- `processes:process-ao-conceive-e3u8s2`
- `processes:process-ao-operate-87q5mk`
- `processes:process-ao-operate-dg9q4h`
- `processes:process-ao-operate-38qyc6`
- `processes:process-ao-retire-g3eyr8`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Time to hire** (stage: Hire) — Elapsed days from requisition approval to hire acceptance. → [`dea:metric-time-to-hire`](https://github.com/technehub-labs/dea-catalog-metrics)
- **Voluntary turnover rate** (stage: Separate) — Share of workforce separating voluntarily in period. → [`dea:metric-voluntary-turnover-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-006 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted from candidate VSC-006 under CR-VS-03 (evidence at E3/high, distinctness closed per CR-VS-02). Served party is internal (manager/employee), distinct from external-customer chains. Boundary vs. Procure to Pay: settlement counterparty is the discriminator (CR-VS-02 boundary statement).

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.1 (CR-VS-01, PR #3) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-03 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-08 metric backfill (metric_ref links to dea-catalog-metrics) |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
