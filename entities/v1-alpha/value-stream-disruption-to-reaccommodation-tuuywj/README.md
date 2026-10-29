# Disruption to Reaccommodation

Admitted Value Stream record (`value-streams:value-stream-disruption-to-reaccommodation-tuuywj`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-disruption-to-reaccommodation-tuuywj` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | hospitality-travel · industry-specific |
| Record | [`value-streams-value-stream-disruption-to-reaccommodation-tuuywj.yaml`](./value-streams-value-stream-disruption-to-reaccommodation-tuuywj.yaml) — authoritative |

## 2. Definition

> The travel stream from disruption detection through rebooking to the reaccommodated traveler.

## 3. Value proposition and served party

**Outcome:** A reaccommodated traveler completing the journey.

## 4. Stream boundary

**Entry criterion:** A journey disruption occurs.

**Exit criterion:** The traveler completes the journey.

**In scope** (from the record's `scope.includes`):

- Disruption detection and communication
- Rebooking
- Compensation handling
- Journey completion

**Out of scope** (each concern owned by the named neighbour):

- Standard booking
- Loyalty goodwill

## 5. Value stages

Disruption to Reaccommodation decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Detect and Communicate

Detect the disruption and communicate to travelers.

| Aspect | Value |
|---|---|
| Entry criterion | A disruption occurs. |
| Exit criterion | Travelers are informed. |
| Outcome | Informed travelers. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 2: Rebook

Rebook affected travelers.

| Aspect | Value |
|---|---|
| Entry criterion | Travelers are informed. |
| Exit criterion | New arrangements are confirmed. |
| Outcome | Rebooked travelers. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 3: Handle Compensation

Handle applicable compensation.

| Aspect | Value |
|---|---|
| Entry criterion | Travelers are rebooked. |
| Exit criterion | Compensation is settled. |
| Outcome | Settled compensation. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

### Stage 4: Complete Journey

Confirm journey completion.

| Aspect | Value |
|---|---|
| Entry criterion | Travelers are rebooked. |
| Exit criterion | The journey is completed. |
| Outcome | A completed journey. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Reaccommodation cycle time** (stream-level) — Elapsed time from disruption to confirmed rebooking.

## 9. Evidence and admission

**Evidence sources:** SRC-015 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-089) from the CR-VS-11 industry evidence register extension. Industry-specific chain (hospitality-travel); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
