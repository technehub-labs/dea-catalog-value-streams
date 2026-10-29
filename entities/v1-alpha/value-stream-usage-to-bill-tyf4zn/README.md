# Usage to Bill

Admitted Value Stream record (`value-streams:value-stream-usage-to-bill-tyf4zn`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-usage-to-bill-tyf4zn` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | telecommunications · industry-specific |
| Record | [`value-streams-value-stream-usage-to-bill-tyf4zn.yaml`](./value-streams-value-stream-usage-to-bill-tyf4zn.yaml) — authoritative |

## 2. Definition

> The telecom revenue stream from usage mediation through rating to an accurate customer bill.

## 3. Value proposition and served party

**Outcome:** An accurate, explained bill for consumed services.

## 4. Stream boundary

**Entry criterion:** Usage events are recorded on an activated service.

**Exit criterion:** The customer bill for the period is produced and accepted.

**In scope** (from the record's `scope.includes`):

- Usage mediation and collection
- Rating and discounting
- Bill production
- Bill inquiry resolution

**Out of scope** (each concern owned by the named neighbour):

- Service activation (Order to Activation)
- Collections

## 5. Value stages

Usage to Bill decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Mediate Usage

Collect and mediate usage events.

| Aspect | Value |
|---|---|
| Entry criterion | Usage events occur. |
| Exit criterion | Usage records are mediated. |
| Outcome | Mediated usage. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### Stage 2: Rate Usage

Rate the mediated usage per the price plan.

| Aspect | Value |
|---|---|
| Entry criterion | Usage is mediated. |
| Exit criterion | Usage is rated. |
| Outcome | Rated usage. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### Stage 3: Produce Bill

Produce and issue the customer bill.

| Aspect | Value |
|---|---|
| Entry criterion | Usage is rated. |
| Exit criterion | The bill is issued. |
| Outcome | An issued bill. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

### Stage 4: Resolve Inquiries

Resolve bill inquiries and disputes.

| Aspect | Value |
|---|---|
| Entry criterion | The bill is issued. |
| Exit criterion | Inquiries are resolved. |
| Outcome | An accepted bill. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-customer-management-f3n8wb`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-sdppmp`
- `processes:process-pr-operate-bbe384`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-order-to-activation` — Activated services generate usage.

**Downstream streams:** none recorded.

## 8. Measurement

- **Billing accuracy rate** (stream-level) — Billed amount variance from rated usage.

## 9. Evidence and admission

**Evidence sources:** SRC-010 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-038) from the CR-VS-11 industry evidence register extension. Industry-specific chain (telecommunications); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
