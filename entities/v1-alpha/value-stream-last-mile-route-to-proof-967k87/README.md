---
documentation_generated_from: value-streams-value-stream-last-mile-route-to-proof-967k87.yaml
id: value-streams:value-stream-last-mile-route-to-proof-967k87
name: Last-Mile Route to Proof
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- logistics-transportation
- retail-commerce
specificity: industry-specific
entry_criterion: A day's route is planned.
exit_criterion: All stops are served with proof captured.
outcome: All stops served with captured proof.
stages:
- Plan Route
- Execute Stops
- Capture Proof
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-operations-management-pm3w8k
processes:
- processes:process-eo-operate-zh9m57
- processes:process-pr-operate-bbe384
- processes:process-sd-build-2pkz5n
metrics:
- Stop completion rate
upstream: []
downstream: []
evidence_sources:
- SRC-016
---

# Last-Mile Route to Proof

`value-streams:value-stream-last-mile-route-to-proof-967k87` · **operational** · logistics-transportation, retail-commerce · industry-specific

> The last-mile stream from route planning through stop execution to complete proof-of-delivery coverage.

**Outcome:** All stops served with captured proof.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-last-mile-route-to-proof-967k87.yaml`](./value-streams-value-stream-last-mile-route-to-proof-967k87.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Plan Route"]
  S2["2. Execute Stops"]
  S3["3. Capture Proof"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Plan Route** | A route is to be planned. | The route is planned. | 2 | 1 | no |
| 2 | **Execute Stops** | The route is planned. | The stops are served. | 1 | 1 | yes |
| 3 | **Capture Proof** | The stops are served. | Proof is complete and exceptions handled. | 2 | 1 | yes |

### 1. Plan Route

Plan the day's route.

| Aspect | Value |
|---|---|
| Entry criterion | A route is to be planned. |
| Exit criterion | The route is planned. |
| Outcome | A planned route. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-sd-build-2pkz5n` |

### 2. Execute Stops

Execute the delivery stops.

| Aspect | Value |
|---|---|
| Entry criterion | The route is planned. |
| Exit criterion | The stops are served. |
| Outcome | Served stops. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

### 3. Capture Proof

Capture proof and handle exceptions.

| Aspect | Value |
|---|---|
| Entry criterion | The stops are served. |
| Exit criterion | Proof is complete and exceptions handled. |
| Outcome | Complete proof. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## Scope boundary

**Entry:** A day's route is planned.

**Exit:** All stops are served with proof captured.

**In scope**

- Route planning
- Stop execution
- Proof capture and exception handling

**Out of scope** (owned by the named neighbour)

- Linehaul (Ship to Consignee)
- Customer notification programs

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-build-2pkz5n`
- `processes:process-eo-operate-zh9m57`
- `processes:process-pr-operate-bbe384`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Stop completion rate** (stream-level) — Share of planned stops served on the day.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-016 | industry-reference-model | Manufacturing and logistics reference models (SCOR-style category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-072) from the CR-VS-11 industry evidence register extension. Industry-specific chain (logistics-transportation, retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
