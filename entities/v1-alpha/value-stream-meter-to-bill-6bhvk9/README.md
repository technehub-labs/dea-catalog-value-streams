# Meter to Bill

Admitted Value Stream record (`value-streams:value-stream-meter-to-bill-6bhvk9`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-meter-to-bill-6bhvk9` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | utilities-energy · industry-specific |
| Record | [`value-streams-value-stream-meter-to-bill-6bhvk9.yaml`](./value-streams-value-stream-meter-to-bill-6bhvk9.yaml) — authoritative |

## 2. Definition

> The end-to-end utility revenue stream from consumption measurement through meter data collection and validation to an accurate bill.

## 3. Value proposition and served party

**Outcome:** An accurate, explained bill for consumed energy.

## 4. Stream boundary

**Entry criterion:** Consumption occurs at a metered point.

**Exit criterion:** The period bill is produced and accepted.

**In scope** (from the record's `scope.includes`):

- Meter data collection
- Validation and estimation
- Rating and bill production
- Bill inquiry resolution

**Out of scope** (each concern owned by the named neighbour):

- Connection services (Apply to Connect)
- Credit and collections

## 5. Value stages

Meter to Bill decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Collect Meter Data

Collect consumption data from the meter.

| Aspect | Value |
|---|---|
| Entry criterion | Consumption occurs. |
| Exit criterion | Meter data is collected. |
| Outcome | Collected meter data. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### Stage 2: Validate and Estimate

Validate the data and estimate gaps.

| Aspect | Value |
|---|---|
| Entry criterion | Data is collected. |
| Exit criterion | Validated consumption exists. |
| Outcome | Validated consumption. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-fa-operate-4xn4d6` |

### Stage 3: Rate and Bill

Rate consumption and produce the bill.

| Aspect | Value |
|---|---|
| Entry criterion | Consumption is validated. |
| Exit criterion | The bill is issued. |
| Outcome | An issued bill. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

### Stage 4: Resolve Inquiries

Resolve bill inquiries.

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
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-customer-management-f3n8wb`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-4xn4d6`
- `processes:process-fa-operate-sdppmp`
- `processes:process-pr-operate-bbe384`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Estimated-bill rate** (stream-level) — Share of bills based on estimated rather than actual reads.

## 9. Evidence and admission

**Evidence sources:** SRC-011 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-043) from the CR-VS-11 industry evidence register extension. Industry-specific chain (utilities-energy); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
