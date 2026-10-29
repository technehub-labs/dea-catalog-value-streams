# Trial to Readout

Admitted Value Stream record (`value-streams:value-stream-trial-to-readout-ztkya5`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-trial-to-readout-ztkya5` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | life-sciences · industry-specific |
| Record | [`value-streams-value-stream-trial-to-readout-ztkya5.yaml`](./value-streams-value-stream-trial-to-readout-ztkya5.yaml) — authoritative |

## 2. Definition

> The clinical-development stream from trial start through conduct and monitoring to database lock and readout.

## 3. Value proposition and served party

**Outcome:** A locked trial database and analyzed readout.

## 4. Stream boundary

**Entry criterion:** An approved trial starts enrollment.

**Exit criterion:** The database locks and the readout completes.

**In scope** (from the record's `scope.includes`):

- Trial conduct
- Monitoring and data management
- Database lock and analysis

**Out of scope** (each concern owned by the named neighbour):

- Recruitment (Clinical Trial Recruitment)
- Regulatory submission

## 5. Value stages

Trial to Readout decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Conduct Trial

Conduct the trial per protocol.

| Aspect | Value |
|---|---|
| Entry criterion | The trial starts. |
| Exit criterion | The trial completes visits. |
| Outcome | Completed conduct. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 2: Monitor and Manage Data

Monitor sites and manage trial data.

| Aspect | Value |
|---|---|
| Entry criterion | Visits are underway. |
| Exit criterion | The data is clean and query-free. |
| Outcome | Clean trial data. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-zwaes5`, `processes:process-eo-operate-44jsrp` |

### Stage 3: Lock and Read Out

Lock the database and complete the readout.

| Aspect | Value |
|---|---|
| Entry criterion | Data is clean. |
| Exit criterion | The readout is complete. |
| Outcome | A completed readout. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-insight-management-ms4n9d`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-2jnz85`
- `processes:process-ge-operate-zwaes5`
- `processes:process-eo-operate-44jsrp`
- `processes:process-fa-operate-ycba3k`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-clinical-trial-recruitment` — Recruitment feeds trial conduct.

**Downstream streams:** none recorded.

## 8. Measurement

- **Trial database lock cycle time** (stream-level) — Elapsed time from last visit to lock.

## 9. Evidence and admission

**Evidence sources:** SRC-018 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-098) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
