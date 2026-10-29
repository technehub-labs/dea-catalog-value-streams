---
documentation_generated_from: value-streams-value-stream-adverse-event-to-signal-8ga6be.yaml
id: value-streams:value-stream-adverse-event-to-signal-8ga6be
name: Adverse Event to Signal
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: governance
industries:
- life-sciences
specificity: industry-specific
entry_criterion: An adverse event is reported.
exit_criterion: The case is processed and the signal decision recorded.
outcome: A documented signal assessment and reporting decision for every validated case.
stages:
- Intake Case
- Process Case
- Detect and Report Signal
capabilities:
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-regulation-management-gya4d8
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-fa-operate-8vqvkk
- processes:process-ge-operate-tpenm6
- processes:process-ge-operate-zwaes5
- processes:process-sd-operate-ucxpz4
metrics:
- Case processing compliance rate
upstream: []
downstream: []
evidence_sources:
- SRC-018
---

# Adverse Event to Signal

`value-streams:value-stream-adverse-event-to-signal-8ga6be` · **governance** · life-sciences · industry-specific

> The pharmacovigilance stream from adverse-event intake through case processing to signal detection and reporting decision.

**Outcome:** A documented signal assessment and reporting decision for every validated case.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-adverse-event-to-signal-8ga6be.yaml`](./value-streams-value-stream-adverse-event-to-signal-8ga6be.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Intake Case"]
  S2["2. Process Case"]
  S3["3. Detect and Report Signal"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Intake Case** | An event is reported. | The case is validated. | 2 | 1 | yes |
| 2 | **Process Case** | The case is validated. | The case assessment is complete. | 2 | 1 | no |
| 3 | **Detect and Report Signal** | Assessment data accumulates. | The signal decision is recorded. | 2 | 2 | no |

### 1. Intake Case

Intake and validate the adverse-event case.

| Aspect | Value |
|---|---|
| Entry criterion | An event is reported. |
| Exit criterion | The case is validated. |
| Outcome | A validated case. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### 2. Process Case

Process and assess the case.

| Aspect | Value |
|---|---|
| Entry criterion | The case is validated. |
| Exit criterion | The case assessment is complete. |
| Outcome | A completed assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 3. Detect and Report Signal

Run signal detection and decide reporting.

| Aspect | Value |
|---|---|
| Entry criterion | Assessment data accumulates. |
| Exit criterion | The signal decision is recorded. |
| Outcome | A recorded decision. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d` · `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` · `processes:process-fa-operate-8vqvkk` |

## Scope boundary

**Entry:** An adverse event is reported.

**Exit:** The case is processed and the signal decision recorded.

**In scope**

- Case intake and validation
- Case processing and assessment
- Signal detection and reporting

**Out of scope** (owned by the named neighbour)

- Clinical trials safety
- Regulatory filings

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-regulation-management-gya4d8`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-operate-zwaes5`
- `processes:process-sd-operate-ucxpz4`
- `processes:process-fa-operate-8vqvkk`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Case processing compliance rate** (stream-level) — Share of cases processed within regulatory timelines.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-018 | industry-reference-model | Life-sciences reference chains (public GxP/ICH category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-100) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
