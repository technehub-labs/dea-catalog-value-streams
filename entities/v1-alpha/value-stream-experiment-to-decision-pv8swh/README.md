---
documentation_generated_from: value-streams-value-stream-experiment-to-decision-pv8swh.yaml
id: value-streams:value-stream-experiment-to-decision-pv8swh
name: Experiment to Decision
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: governance
industries:
- technology
specificity: industry-specific
entry_criterion: A hypothesis is approved.
exit_criterion: The decision is recorded and actioned.
outcome: A recorded, evidence-based decision for every experiment.
stages:
- Set Up Experiment
- Run
- Analyze and Decide
capabilities:
- capabilities:capability-enterprise-performance-management-5fxren
- capabilities:capability-idea-management-86dckf
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-operations-management-pm3w8k
processes:
- processes:process-eo-operate-2jnz85
- processes:process-pv-conceive-kps544
- processes:process-sd-operate-ucxpz4
metrics:
- Experiment decision cycle time
upstream:
- value-stream-feature-request-to-release
downstream: []
evidence_sources:
- SRC-019
---

# Experiment to Decision

`value-streams:value-stream-experiment-to-decision-pv8swh` · **governance** · technology · industry-specific

> The experimentation stream from hypothesis setup through experiment run to a recorded ship/iterate/kill decision.

**Outcome:** A recorded, evidence-based decision for every experiment.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-experiment-to-decision-pv8swh.yaml`](./value-streams-value-stream-experiment-to-decision-pv8swh.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Set Up Experiment"]
  S2["2. Run"]
  S3["3. Analyze and Decide"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Set Up Experiment** | A hypothesis is approved. | The experiment is live. | 2 | 1 | no |
| 2 | **Run** | The experiment is live. | The run is complete. | 2 | 1 | no |
| 3 | **Analyze and Decide** | The run is complete. | The decision is recorded and actioned. | 2 | 1 | no |

### 1. Set Up Experiment

Set up the hypothesis and instrumentation.

| Aspect | Value |
|---|---|
| Entry criterion | A hypothesis is approved. |
| Exit criterion | The experiment is live. |
| Outcome | A live experiment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d` · `capabilities:capability-idea-management-86dckf` |
| Realizing processes | `processes:process-pv-conceive-kps544` |

### 2. Run

Run the experiment to significance.

| Aspect | Value |
|---|---|
| Entry criterion | The experiment is live. |
| Exit criterion | The run is complete. |
| Outcome | A completed run. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### 3. Analyze and Decide

Analyze and record the decision.

| Aspect | Value |
|---|---|
| Entry criterion | The run is complete. |
| Exit criterion | The decision is recorded and actioned. |
| Outcome | An actioned decision. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d` · `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

## Scope boundary

**Entry:** A hypothesis is approved.

**Exit:** The decision is recorded and actioned.

**In scope**

- Hypothesis and instrumentation
- Experiment run
- Analysis and decision

**Out of scope** (owned by the named neighbour)

- Roadmap planning
- Marketing testing

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-idea-management-86dckf`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pv-conceive-kps544`
- `processes:process-eo-operate-2jnz85`
- `processes:process-sd-operate-ucxpz4`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [feature request to release](../value-stream-feature-request-to-release-2fyemr/README.md) — Ship decisions feed the feature pipeline.

**Downstream:** none recorded.

## Measurement

- **Experiment decision cycle time** (stream-level) — Elapsed time from setup to recorded decision.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-019 | industry-reference-model | Technology / SaaS product chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-114) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
