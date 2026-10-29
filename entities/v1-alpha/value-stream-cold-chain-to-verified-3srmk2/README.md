# Cold Chain to Verified

Admitted Value Stream record (`value-streams:value-stream-cold-chain-to-verified-3srmk2`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-cold-chain-to-verified-3srmk2` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | logistics-transportation, retail-commerce · industry-specific |
| Record | [`value-streams-value-stream-cold-chain-to-verified-3srmk2.yaml`](./value-streams-value-stream-cold-chain-to-verified-3srmk2.yaml) — authoritative |

## 2. Definition

> The temperature-controlled stream from sealed load through monitored transit to verified cold-chain integrity.

## 3. Value proposition and served party

**Outcome:** Delivered goods with verified cold-chain integrity.

## 4. Stream boundary

**Entry criterion:** A temperature-controlled load is sealed.

**Exit criterion:** Cold-chain integrity is verified at delivery.

**In scope** (from the record's `scope.includes`):

- Sealed monitored transit
- Excursion handling
- Verification at receipt

**Out of scope** (each concern owned by the named neighbour):

- Ambient freight (Ship to Consignee)
- Quality disposition (Inspect to Disposition)

## 5. Value stages

Cold Chain to Verified decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Seal and Monitor

Seal the load and monitor temperature in transit.

| Aspect | Value |
|---|---|
| Entry criterion | A load is sealed. |
| Exit criterion | Transit completes with monitoring. |
| Outcome | Monitored transit. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

### Stage 2: Handle Excursions

Handle temperature excursions per protocol.

| Aspect | Value |
|---|---|
| Entry criterion | An excursion occurs. |
| Exit criterion | The excursion is handled and documented. |
| Outcome | A handled excursion. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 3: Verify at Receipt

Verify cold-chain integrity at receipt.

| Aspect | Value |
|---|---|
| Entry criterion | Transit completes. |
| Exit criterion | Integrity is verified. |
| Outcome | Verified integrity. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-zh9m57`
- `processes:process-eo-operate-44jsrp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Cold-chain excursion rate** (stream-level) — Share of loads with a reportable excursion.

## 9. Evidence and admission

**Evidence sources:** SRC-016, SRC-013 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-070) from the CR-VS-11 industry evidence register extension. Industry-specific chain (logistics-transportation, retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
