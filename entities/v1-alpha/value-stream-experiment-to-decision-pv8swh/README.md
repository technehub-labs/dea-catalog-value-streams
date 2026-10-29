# Experiment to Decision

Admitted Value Stream record (`value-streams:value-stream-experiment-to-decision-pv8swh`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-experiment-to-decision-pv8swh` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | technology · industry-specific |
| Record | [`value-streams-value-stream-experiment-to-decision-pv8swh.yaml`](./value-streams-value-stream-experiment-to-decision-pv8swh.yaml) — authoritative |

## 2. Definition

> The experimentation stream from hypothesis setup through experiment run to a recorded ship/iterate/kill decision.

## 3. Value proposition and served party

**Outcome:** A recorded, evidence-based decision for every experiment.

## 4. Stream boundary

**Entry criterion:** A hypothesis is approved.

**Exit criterion:** The decision is recorded and actioned.

**In scope** (from the record's `scope.includes`):

- Hypothesis and instrumentation
- Experiment run
- Analysis and decision

**Out of scope** (each concern owned by the named neighbour):

- Roadmap planning
- Marketing testing

## 5. Value stages

Experiment to Decision decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Set Up Experiment

Set up the hypothesis and instrumentation.

| Aspect | Value |
|---|---|
| Entry criterion | A hypothesis is approved. |
| Exit criterion | The experiment is live. |
| Outcome | A live experiment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-idea-management-86dckf` |
| Realizing processes | `processes:process-pv-conceive-kps544` |

### Stage 2: Run

Run the experiment to significance.

| Aspect | Value |
|---|---|
| Entry criterion | The experiment is live. |
| Exit criterion | The run is complete. |
| Outcome | A completed run. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Analyze and Decide

Analyze and record the decision.

| Aspect | Value |
|---|---|
| Entry criterion | The run is complete. |
| Exit criterion | The decision is recorded and actioned. |
| Outcome | An actioned decision. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-idea-management-86dckf`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pv-conceive-kps544`
- `processes:process-eo-operate-2jnz85`
- `processes:process-sd-operate-ucxpz4`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-feature-request-to-release` — Ship decisions feed the feature pipeline.

**Downstream streams:** none recorded.

## 8. Measurement

- **Experiment decision cycle time** (stream-level) — Elapsed time from setup to recorded decision.

## 9. Evidence and admission

**Evidence sources:** SRC-019 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-114) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
