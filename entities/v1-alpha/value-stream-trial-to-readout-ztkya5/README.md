---
documentation_generated_from: value-streams-value-stream-trial-to-readout-ztkya5.yaml
id: value-streams:value-stream-trial-to-readout-ztkya5
name: Trial to Readout
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- life-sciences
specificity: industry-specific
entry_criterion: An approved trial starts enrollment.
exit_criterion: The database locks and the readout completes.
outcome: A locked trial database and analyzed readout.
stages:
- Conduct Trial
- Monitor and Manage Data
- Lock and Read Out
capabilities:
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-eo-operate-2jnz85
- processes:process-eo-operate-44jsrp
- processes:process-fa-operate-ycba3k
- processes:process-ge-operate-zwaes5
metrics:
- Trial database lock cycle time
upstream:
- value-stream-clinical-trial-recruitment
downstream: []
evidence_sources:
- SRC-018
---

# Trial to Readout

`value-streams:value-stream-trial-to-readout-ztkya5` · **operational** · life-sciences · industry-specific

> The clinical-development stream from trial start through conduct and monitoring to database lock and readout.

**Outcome:** A locked trial database and analyzed readout.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-trial-to-readout-ztkya5.yaml`](./value-streams-value-stream-trial-to-readout-ztkya5.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  TRIGGER(["⏺ Entry"])
  EXIT1(["✔ Exit"])
  S1["1. Conduct Trial<br/>The trial completes visits"]
  S2["2. Monitor and Manage Data<br/>The data is clean and query-free"]
  S3["3. Lock and Read Out<br/>The readout is complete"]
  TRIGGER --> S1
  S1 --> S2
  S2 --> S3
  S3 --> EXIT1
  S3 -. re-engage .-> S1
  classDef terminal fill:#2C3E50,color:#fff,stroke:#1a252f,stroke-width:1px;
  classDef stage fill:#EAF2F8,color:#1a252f,stroke:#2C3E50,stroke-width:1px;
  class TRIGGER,EXIT1 terminal;
  class S1,S2,S3 stage;
  style TRIGGER fill:#27AE60,color:#fff,stroke:#1e8449,stroke-width:1px;
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Conduct Trial** | The trial starts. | The trial completes visits. | 2 | 1 | no |
| 2 | **Monitor and Manage Data** | Visits are underway. | The data is clean and query-free. | 2 | 2 | no |
| 3 | **Lock and Read Out** | Data is clean. | The readout is complete. | 2 | 1 | no |

### 1. Conduct Trial

Conduct the trial per protocol.

| Aspect | Value |
|---|---|
| Entry criterion | The trial starts. |
| Exit criterion | The trial completes visits. |
| Outcome | Completed conduct. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### 2. Monitor and Manage Data

Monitor sites and manage trial data.

| Aspect | Value |
|---|---|
| Entry criterion | Visits are underway. |
| Exit criterion | The data is clean and query-free. |
| Outcome | Clean trial data. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-zwaes5` · `processes:process-eo-operate-44jsrp` |

### 3. Lock and Read Out

Lock the database and complete the readout.

| Aspect | Value |
|---|---|
| Entry criterion | Data is clean. |
| Exit criterion | The readout is complete. |
| Outcome | A completed readout. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

## Scope boundary

**Entry:** An approved trial starts enrollment.

**Exit:** The database locks and the readout completes.

**In scope**

- Trial conduct
- Monitoring and data management
- Database lock and analysis

**Out of scope** (owned by the named neighbour)

- Recruitment (Clinical Trial Recruitment)
- Regulatory submission

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-insight-management-ms4n9d`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-2jnz85`
- `processes:process-ge-operate-zwaes5`
- `processes:process-eo-operate-44jsrp`
- `processes:process-fa-operate-ycba3k`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [clinical trial recruitment](../value-stream-clinical-trial-recruitment-zqvzg9/README.md) — Recruitment feeds trial conduct.

**Downstream:** none recorded.

## Measurement

- **Trial database lock cycle time** (stream-level) — Elapsed time from last visit to lock.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-018 | industry-reference-model | Life-sciences reference chains (public GxP/ICH category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-098) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
