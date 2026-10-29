# Return to Credit

Admitted Value Stream record (`value-streams:value-stream-return-to-credit-qan2dn`, v1.3.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-return-to-credit-qan2dn` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.3.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | cross-industry · generic |
| Record | [`value-streams-value-stream-return-to-credit-qan2dn.yaml`](./value-streams-value-stream-return-to-credit-qan2dn.yaml) — authoritative |

## 2. Definition

> The end-to-end stream from initiation of a customer return through reverse logistics and settlement by refund, credit, or replacement.

## 3. Value proposition and served party

**Outcome:** A fairly settled return with the customer relationship preserved.

## 4. Stream boundary

**Entry criterion:** A customer initiates a return of goods or services.

**Exit criterion:** The return is settled (refund, credit, or replacement confirmed to the customer).

**In scope** (from the record's `scope.includes`):

- Return initiation and authorization
- Reverse logistics receipt
- Inspection and disposition
- Settlement (refund, credit, replacement)

**Out of scope** (each concern owned by the named neighbour):

- Forward order flows (Order to Cash)
- Relationship-level renewal decisions (Contract to Renewal)
- Warranty strategy design (Offering Management capability)

## 5. Value stages

Return to Credit decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Initiate Return

Authorize the customer's return initiation.

| Aspect | Value |
|---|---|
| Entry criterion | A customer initiates a return of goods or services. |
| Exit criterion | The return is authorized. |
| Outcome | An authorized return. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Receive Reverse Logistics

Receive the returned goods through reverse logistics.

| Aspect | Value |
|---|---|
| Entry criterion | A return is authorized. |
| Exit criterion | The goods are received back. |
| Outcome | Received returned goods. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57`, `processes:process-eo-operate-zwzmbd` |

### Stage 3: Inspect and Dispose

Inspect the return and determine disposition.

| Aspect | Value |
|---|---|
| Entry criterion | The goods are received back. |
| Exit criterion | A disposition decision is made. |
| Outcome | A settled disposition. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 4: Settle Credit

Settle by refund, credit, or replacement.

| Aspect | Value |
|---|---|
| Entry criterion | A disposition decision exists. |
| Exit criterion | The return is settled (refund, credit, or replacement confirmed to the customer). |
| Outcome | A fairly settled return with the relationship preserved. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp`, `processes:process-fa-operate-g9zpnq` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-zh9m57`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-44jsrp`
- `processes:process-fa-operate-sdppmp`
- `processes:process-fa-operate-g9zpnq`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-order-to-cash` — Returns mirror fulfilled orders; goods and value flow back.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-record-to-report` — Credits and refunds are recorded as transactions.

## 8. Measurement

- **Return cycle time** (stage: Settle Credit) — Elapsed time from return initiation to settlement confirmation.
- **Return rate** (stage: Initiate Return) — Returns as a share of fulfilled orders in period. → [`dea:metric-return-rate`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-006 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted from candidate VSC-011 under CR-VS-05 (third tranche; evidence at E3/high from the SRC-006 chain-inventory observation, distinctness closed per the CR-VS-05 sweep). Mirrors Order to Cash: goods/value flow back; entry and exit are mirrored, not shared (CR-VS-05 sweep). Boundary vs. Contract to Renewal: settles a single transaction backwards vs. the relationship forwards (CR-VS-05 boundary statement).

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.4 (CR-VS-05, register v0.3) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-05 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-08 metric backfill (metric_ref links to dea-catalog-metrics) |
| active | 2026-10-28 | Emmanuel A. Otchere, CR-VS-11 applicability backfill (cross-industry, generic) |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
