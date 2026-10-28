# Acquire to Retire

Admitted Value Stream record (`value-streams:value-stream-acquire-to-retire-g5x89g`, v1.1.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-acquire-to-retire-g5x89g` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.1.0 · active |
| Metamodel pin | 1.0.0 |
| Record | [`value-streams-value-stream-acquire-to-retire-g5x89g.yaml`](./value-streams-value-stream-acquire-to-retire-g5x89g.yaml) — authoritative |

## 2. Definition

> The end-to-end asset-lifecycle stream from identification of an internal asset need through acquisition, use, and disposal.

## 3. Value proposition and served party

**Outcome:** Assets productively used across their lifecycle and cleanly retired.

## 4. Stream boundary

**Entry criterion:** An asset need is identified for the enterprise's own use.

**Exit criterion:** The asset is disposed and its lifecycle obligations are closed.

**In scope** (from the record's `scope.includes`):

- Internal asset need identification
- Asset acquisition
- Asset operation and maintenance
- Disposal and obligation closure

**Out of scope** (each concern owned by the named neighbour):

- Supplier settlement (Procure to Pay)
- People lifecycle (Hire to Retire)
- Production execution as such (Plan to Deliver)

## 5. Value stages

Acquire to Retire decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Identify Asset Need

Identify the internal asset need.

| Aspect | Value |
|---|---|
| Entry criterion | An asset need is identified for the enterprise's own use. |
| Exit criterion | The need is approved for acquisition. |
| Outcome | An approved asset acquisition case. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-asset-management-judtwr`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-fa-conceive-4uqqvg` |

### Stage 2: Acquire Asset

Acquire the asset.

| Aspect | Value |
|---|---|
| Entry criterion | An acquisition case is approved. |
| Exit criterion | The asset is received and capitalized. |
| Outcome | A capitalized asset in service. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-asset-management-judtwr`, `capabilities:capability-sourcing-and-procurement-esucp4` |
| Realizing processes | `processes:process-eo-operate-vzcxx7`, `processes:process-eo-operate-j9cjzz` |

### Stage 3: Operate and Maintain

Operate and maintain the asset productively.

| Aspect | Value |
|---|---|
| Entry criterion | The asset is in service. |
| Exit criterion | The asset is productively used across its lifecycle. |
| Outcome | Productive asset use. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-asset-management-judtwr`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-j9cjzz`, `processes:process-eo-operate-xud3hs` |

### Stage 4: Retire Asset

Dispose the asset and close lifecycle obligations.

| Aspect | Value |
|---|---|
| Entry criterion | The asset reaches end of useful life. |
| Exit criterion | The asset is disposed and its lifecycle obligations are closed. |
| Outcome | Cleanly retired assets. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-asset-management-judtwr`, `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-eo-retire-rpg6d4` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-asset-management-judtwr`
- `capabilities:capability-sourcing-and-procurement-esucp4`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-conceive-4uqqvg`
- `processes:process-eo-operate-vzcxx7`
- `processes:process-eo-operate-j9cjzz`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-retire-rpg6d4`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-procure-to-pay` — Procured assets enter the asset lifecycle at receipt.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-record-to-report` — Asset depreciation and disposal are recorded as transactions.

## 8. Measurement

- **Asset utilization** (stage: Operate and Maintain) — Productive use as a share of available asset capacity.
- **Time to retire** (stage: Retire Asset) — Elapsed time from retirement decision to obligation closure.

## 9. Evidence and admission

**Evidence sources:** SRC-006 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted from candidate VSC-013 under CR-VS-05 (third tranche; evidence at E3/high from the SRC-006 chain-inventory observation, distinctness closed per the CR-VS-05 sweep). Asset-lifecycle chain; served party is the internal asset custodian. Boundary vs. Procure to Pay: supplier settlement vs. asset disposal (CR-VS-05 boundary statement). Boundary vs. Hire to Retire: assets vs. people as the lifecycle object.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.4 (CR-VS-05, register v0.3) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-05 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
