---
documentation_generated_from: value-streams-value-stream-number-port-to-activate-428e2j.yaml
id: value-streams:value-stream-number-port-to-activate-428e2j
name: Number Port to Activate
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- telecommunications
specificity: industry-specific
entry_criterion: A customer requests to port a number.
exit_criterion: The number is ported and activated.
outcome: A ported number active on the recipient network.
stages:
- Validate Request
- Coordinate Cutover
- Cut Over and Activate
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-partner-management-cp3vdb
- capabilities:capability-regulation-management-gya4d8
- capabilities:capability-technology-enablement-y6nkws
processes:
- processes:process-eo-operate-2jnz85
- processes:process-pr-operate-bbe384
metrics:
- Porting completion time
upstream: []
downstream: []
evidence_sources:
- SRC-010
---

# Number Port to Activate

`value-streams:value-stream-number-port-to-activate-428e2j` · **operational** · telecommunications · industry-specific

> The porting stream from a porting request through validation and coordination to an activated ported number.

**Outcome:** A ported number active on the recipient network.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-number-port-to-activate-428e2j.yaml`](./value-streams-value-stream-number-port-to-activate-428e2j.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Validate Request"]
  S2["2. Coordinate Cutover"]
  S3["3. Cut Over and Activate"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Validate Request** | A port request is received. | The request is validated. | 2 | 1 | yes |
| 2 | **Coordinate Cutover** | The request is validated. | The cutover is scheduled. | 2 | 1 | no |
| 3 | **Cut Over and Activate** | The cutover is scheduled. | The number is active. | 2 | 1 | yes |

### 1. Validate Request

Validate the porting request and eligibility.

| Aspect | Value |
|---|---|
| Entry criterion | A port request is received. |
| Exit criterion | The request is validated. |
| Outcome | A validated request. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Coordinate Cutover

Coordinate the cutover window with the donor.

| Aspect | Value |
|---|---|
| Entry criterion | The request is validated. |
| Exit criterion | The cutover is scheduled. |
| Outcome | A scheduled cutover. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-partner-management-cp3vdb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 3. Cut Over and Activate

Execute the cutover and activate the ported number.

| Aspect | Value |
|---|---|
| Entry criterion | The cutover is scheduled. |
| Exit criterion | The number is active. |
| Outcome | An active ported number. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## Scope boundary

**Entry:** A customer requests to port a number.

**Exit:** The number is ported and activated.

**In scope**

- Porting request and validation
- Donor coordination
- Cutover and activation

**Out of scope** (owned by the named neighbour)

- New-service provisioning (Order to Activation)
- Number allocation governance

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-technology-enablement-y6nkws`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-2jnz85`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Porting completion time** (stream-level) — Elapsed time from request to activation.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-010 | industry-reference-model | Telecommunications industry reference models (eTOM category-level structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-041) from the CR-VS-11 industry evidence register extension. Industry-specific chain (telecommunications); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
