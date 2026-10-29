---
documentation_generated_from: value-streams-value-stream-network-build-to-service-u228b3.yaml
id: value-streams:value-stream-network-build-to-service-u228b3
name: Network Build to Service
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: support
industries:
- telecommunications
specificity: industry-specific
entry_criterion: A capacity need is identified.
exit_criterion: The new capacity is in production and service-ready.
outcome: Service-ready network capacity in production.
stages:
- Plan Capacity
- Build and Integrate
- Accept and Cut Over
capabilities:
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-strategic-planning-k3rz7a
- capabilities:capability-technology-enablement-y6nkws
- capabilities:capability-technology-management-maus5n
processes:
- processes:process-eo-build-j9z3q4
- processes:process-eo-operate-44jsrp
- processes:process-eo-operate-xud3hs
- processes:process-fa-conceive-4uqqvg
- processes:process-sd-build-2pkz5n
metrics:
- Build-to-service lead time
upstream:
- value-stream-plan-to-forecast
downstream:
- value-stream-order-to-activation
evidence_sources:
- SRC-010
---

# Network Build to Service

`value-streams:value-stream-network-build-to-service-u228b3` · **support** · telecommunications · industry-specific

> The network-investment stream from capacity planning through build and integration to service-ready status.

**Outcome:** Service-ready network capacity in production.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-network-build-to-service-u228b3.yaml`](./value-streams-value-stream-network-build-to-service-u228b3.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Plan Capacity"]
  S2["2. Build and Integrate"]
  S3["3. Accept and Cut Over"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Plan Capacity** | A capacity need is identified. | The build is planned. | 2 | 2 | no |
| 2 | **Build and Integrate** | The build is planned. | The build is complete and integrated. | 2 | 2 | no |
| 3 | **Accept and Cut Over** | The build is integrated. | The capacity is service-ready. | 2 | 1 | no |

### 1. Plan Capacity

Plan network capacity against demand.

| Aspect | Value |
|---|---|
| Entry criterion | A capacity need is identified. |
| Exit criterion | The build is planned. |
| Outcome | A planned build. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-strategic-planning-k3rz7a` · `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-sd-build-2pkz5n` · `processes:process-fa-conceive-4uqqvg` |

### 2. Build and Integrate

Build and integrate the network capacity.

| Aspect | Value |
|---|---|
| Entry criterion | The build is planned. |
| Exit criterion | The build is complete and integrated. |
| Outcome | Integrated capacity. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-build-j9z3q4` · `processes:process-eo-operate-xud3hs` |

### 3. Accept and Cut Over

Accept and cut over to production.

| Aspect | Value |
|---|---|
| Entry criterion | The build is integrated. |
| Exit criterion | The capacity is service-ready. |
| Outcome | Service-ready capacity. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

## Scope boundary

**Entry:** A capacity need is identified.

**Exit:** The new capacity is in production and service-ready.

**In scope**

- Capacity planning
- Build and integration
- Acceptance and cutover

**Out of scope** (owned by the named neighbour)

- Customer provisioning (Order to Activation)
- Decommissioning

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-strategic-planning-k3rz7a`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-operations-management-pm3w8k`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-build-2pkz5n`
- `processes:process-fa-conceive-4uqqvg`
- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-44jsrp`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [plan to forecast](../value-stream-plan-to-forecast-89vb4q/README.md) — Capacity investment follows the ratified plan.

**Downstream** (this stream's exit feeds their entry):

- [order to activation](../value-stream-order-to-activation-uxqth5/README.md) — Service-ready capacity enables provisioning.

## Measurement

- **Build-to-service lead time** (stream-level) — Elapsed time from plan to service-ready.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-010 | industry-reference-model | Telecommunications industry reference models (eTOM category-level structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-039) from the CR-VS-11 industry evidence register extension. Industry-specific chain (telecommunications); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
