---
documentation_generated_from: value-streams-value-stream-tender-to-award-gjmy4d.yaml
id: value-streams:value-stream-tender-to-award-gjmy4d
name: Tender to Award
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- construction-real-estate
specificity: industry-specific
entry_criterion: A tender is invited.
exit_criterion: The contract is awarded.
outcome: An awarded construction contract.
stages:
- Prepare Bid
- Submit
- Evaluate and Clarify
- Award
capabilities:
- capabilities:capability-financial-resource-management-cd3c7c
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-offering-management-6egkc8
- capabilities:capability-partner-management-cp3vdb
processes:
- processes:process-fa-conceive-4uqqvg
- processes:process-ge-build-mctdgc
- processes:process-pr-operate-bbe384
metrics:
- Bid win rate
upstream: []
downstream: []
evidence_sources:
- SRC-017
---

# Tender to Award

`value-streams:value-stream-tender-to-award-gjmy4d` · **operational** · construction-real-estate · industry-specific

> The construction stream from tender invitation through bid preparation and evaluation to contract award.

**Outcome:** An awarded construction contract.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-tender-to-award-gjmy4d.yaml`](./value-streams-value-stream-tender-to-award-gjmy4d.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Prepare Bid"]
  S2["2. Submit"]
  S3["3. Evaluate and Clarify"]
  S4["4. Award"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Prepare Bid** | A tender is invited. | The bid is ready. | 2 | 1 | no |
| 2 | **Submit** | The bid is ready. | The bid is submitted. | 1 | 1 | no |
| 3 | **Evaluate and Clarify** | The bid is submitted. | Clarifications are closed. | 2 | 1 | no |
| 4 | **Award** | Evaluation completes. | The contract is awarded and executed. | 2 | 1 | yes |

### 1. Prepare Bid

Prepare the bid against the tender.

| Aspect | Value |
|---|---|
| Entry criterion | A tender is invited. |
| Exit criterion | The bid is ready. |
| Outcome | A prepared bid. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-conceive-4uqqvg` |

### 2. Submit

Submit the bid.

| Aspect | Value |
|---|---|
| Entry criterion | The bid is ready. |
| Exit criterion | The bid is submitted. |
| Outcome | A submitted bid. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-partner-management-cp3vdb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 3. Evaluate and Clarify

Respond to evaluation clarification.

| Aspect | Value |
|---|---|
| Entry criterion | The bid is submitted. |
| Exit criterion | Clarifications are closed. |
| Outcome | Closed clarifications. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u` · `capabilities:capability-partner-management-cp3vdb` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### 4. Award

Award and execute the contract.

| Aspect | Value |
|---|---|
| Entry criterion | Evaluation completes. |
| Exit criterion | The contract is awarded and executed. |
| Outcome | An awarded contract. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u` · `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

## Scope boundary

**Entry:** A tender is invited.

**Exit:** The contract is awarded.

**In scope**

- Bid preparation
- Submission
- Evaluation and clarification
- Award

**Out of scope** (owned by the named neighbour)

- Project execution (Build to Handover)
- Framework agreements

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-conceive-4uqqvg`
- `processes:process-pr-operate-bbe384`
- `processes:process-ge-build-mctdgc`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Bid win rate** (stream-level) — Awarded bids as a share of submitted.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-017 | industry-reference-model | Construction and real-estate chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-092) from the CR-VS-11 industry evidence register extension. Industry-specific chain (construction-real-estate); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
