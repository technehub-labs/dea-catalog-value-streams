---
documentation_generated_from: value-streams-value-stream-outage-to-restore-ff6xme.yaml
id: value-streams:value-stream-outage-to-restore-ff6xme
name: Outage to Restore
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- utilities-energy
specificity: industry-specific
entry_criterion: An outage is detected or reported.
exit_criterion: Supply is restored and customers are informed.
outcome: Restored supply with informed customers.
stages:
- Detect and Localize
- Dispatch Crew
- Repair and Switch
- Confirm and Communicate
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-technology-enablement-y6nkws
- capabilities:capability-technology-management-maus5n
- capabilities:capability-workforce-planning-b43rhm
processes:
- processes:process-eo-operate-2jnz85
- processes:process-eo-operate-4njp7b
- processes:process-eo-operate-j9cjzz
- processes:process-pr-operate-bbe384
metrics:
- Outage restoration time
upstream: []
downstream: []
evidence_sources:
- SRC-011
---

# Outage to Restore

`value-streams:value-stream-outage-to-restore-ff6xme` · **operational** · utilities-energy · industry-specific

> The grid-operations stream from outage detection through crew dispatch and repair to restored supply and customer communication.

**Outcome:** Restored supply with informed customers.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-outage-to-restore-ff6xme.yaml`](./value-streams-value-stream-outage-to-restore-ff6xme.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Detect and Localize"]
  S2["2. Dispatch Crew"]
  S3["3. Repair and Switch"]
  S4["4. Confirm and Communicate"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Detect and Localize** | An outage occurs. | The outage is localized. | 2 | 1 | yes |
| 2 | **Dispatch Crew** | The outage is localized. | The crew is dispatched. | 2 | 1 | no |
| 3 | **Repair and Switch** | The crew is dispatched. | Supply is restored. | 2 | 1 | no |
| 4 | **Confirm and Communicate** | Supply is restored. | Customers are informed. | 2 | 1 | yes |

### 1. Detect and Localize

Detect and localize the outage.

| Aspect | Value |
|---|---|
| Entry criterion | An outage occurs. |
| Exit criterion | The outage is localized. |
| Outcome | A localized outage. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-4njp7b` |

### 2. Dispatch Crew

Dispatch the repair crew.

| Aspect | Value |
|---|---|
| Entry criterion | The outage is localized. |
| Exit criterion | The crew is dispatched. |
| Outcome | A dispatched crew. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-workforce-planning-b43rhm` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### 3. Repair and Switch

Execute repair and switching restoration.

| Aspect | Value |
|---|---|
| Entry criterion | The crew is dispatched. |
| Exit criterion | Supply is restored. |
| Outcome | Restored supply. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-operate-j9cjzz` |

### 4. Confirm and Communicate

Confirm restoration and communicate to customers.

| Aspect | Value |
|---|---|
| Entry criterion | Supply is restored. |
| Exit criterion | Customers are informed. |
| Outcome | Informed customers. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## Scope boundary

**Entry:** An outage is detected or reported.

**Exit:** Supply is restored and customers are informed.

**In scope**

- Outage detection and localization
- Crew dispatch
- Repair and switching
- Restoration confirmation

**Out of scope** (owned by the named neighbour)

- Planned maintenance
- Field installations

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-planning-b43rhm`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-customer-management-f3n8wb`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-4njp7b`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-j9cjzz`
- `processes:process-pr-operate-bbe384`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Outage restoration time** (stage: Confirm and Communicate) — Elapsed time from detection to restoration. → [`dea:metric-mean-time-to-restore-service`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-011 | industry-reference-model | Utilities industry reference models (metering and retail-energy chains, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-045) from the CR-VS-11 industry evidence register extension. Industry-specific chain (utilities-energy); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
