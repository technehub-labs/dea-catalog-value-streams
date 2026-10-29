---
documentation_generated_from: value-streams-value-stream-vital-record-to-archive-pb9btj.yaml
id: value-streams:value-stream-vital-record-to-archive-pb9btj
name: Vital Record to Archive
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: support
industries:
- public-sector
specificity: industry-specific
entry_criterion: A vital event is registered.
exit_criterion: The record is archived and retrievable.
outcome: An archived, retrievable vital record with certified copies available.
stages:
- Register Event
- Certify
- Archive
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
processes:
- processes:process-eo-operate-zwzmbd
- processes:process-fa-operate-8vqvkk
- processes:process-pr-operate-bbe384
metrics:
- Record retrieval time
upstream: []
downstream: []
evidence_sources:
- SRC-014
---

# Vital Record to Archive

`value-streams:value-stream-vital-record-to-archive-pb9btj` · **support** · public-sector · industry-specific

> The records stream from vital-event registration through certification to archived, retrievable record.

**Outcome:** An archived, retrievable vital record with certified copies available.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-vital-record-to-archive-pb9btj.yaml`](./value-streams-value-stream-vital-record-to-archive-pb9btj.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Register Event"]
  S2["2. Certify"]
  S3["3. Archive"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Register Event** | An event is reported. | The event is registered. | 2 | 1 | yes |
| 2 | **Certify** | The event is registered. | Copies are certified. | 2 | 1 | yes |
| 3 | **Archive** | The event is registered. | The record is archived. | 2 | 1 | no |

### 1. Register Event

Register the vital event.

| Aspect | Value |
|---|---|
| Entry criterion | An event is reported. |
| Exit criterion | The event is registered. |
| Outcome | A registered event. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Certify

Issue certified copies.

| Aspect | Value |
|---|---|
| Entry criterion | The event is registered. |
| Exit criterion | Copies are certified. |
| Outcome | Certified copies. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-8vqvkk` |

### 3. Archive

Archive the record for retrieval.

| Aspect | Value |
|---|---|
| Entry criterion | The event is registered. |
| Exit criterion | The record is archived. |
| Outcome | An archived record. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

## Scope boundary

**Entry:** A vital event is registered.

**Exit:** The record is archived and retrievable.

**In scope**

- Event registration
- Certification
- Archiving

**Out of scope** (owned by the named neighbour)

- Disclosure requests (Request to Disclose)
- Digital archives governance

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-operations-management-pm3w8k`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-8vqvkk`
- `processes:process-eo-operate-zwzmbd`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Record retrieval time** (stream-level) — Elapsed time to retrieve an archived record on request.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-014 | industry-reference-model | Public-sector service chains (permits, grants, benefits; public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-080) from the CR-VS-11 industry evidence register extension. Industry-specific chain (public-sector); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
