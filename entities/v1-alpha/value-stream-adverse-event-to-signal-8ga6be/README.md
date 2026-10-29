# Adverse Event to Signal

Admitted Value Stream record (`value-streams:value-stream-adverse-event-to-signal-8ga6be`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-adverse-event-to-signal-8ga6be` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | life-sciences · industry-specific |
| Record | [`value-streams-value-stream-adverse-event-to-signal-8ga6be.yaml`](./value-streams-value-stream-adverse-event-to-signal-8ga6be.yaml) — authoritative |

## 2. Definition

> The pharmacovigilance stream from adverse-event intake through case processing to signal detection and reporting decision.

## 3. Value proposition and served party

**Outcome:** A documented signal assessment and reporting decision for every validated case.

## 4. Stream boundary

**Entry criterion:** An adverse event is reported.

**Exit criterion:** The case is processed and the signal decision recorded.

**In scope** (from the record's `scope.includes`):

- Case intake and validation
- Case processing and assessment
- Signal detection and reporting

**Out of scope** (each concern owned by the named neighbour):

- Clinical trials safety
- Regulatory filings

## 5. Value stages

Adverse Event to Signal decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Intake Case

Intake and validate the adverse-event case.

| Aspect | Value |
|---|---|
| Entry criterion | An event is reported. |
| Exit criterion | The case is validated. |
| Outcome | A validated case. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 2: Process Case

Process and assess the case.

| Aspect | Value |
|---|---|
| Entry criterion | The case is validated. |
| Exit criterion | The case assessment is complete. |
| Outcome | A completed assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Detect and Report Signal

Run signal detection and decide reporting.

| Aspect | Value |
|---|---|
| Entry criterion | Assessment data accumulates. |
| Exit criterion | The signal decision is recorded. |
| Outcome | A recorded decision. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-sd-operate-ucxpz4`, `processes:process-fa-operate-8vqvkk` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-regulation-management-gya4d8`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-operate-zwaes5`
- `processes:process-sd-operate-ucxpz4`
- `processes:process-fa-operate-8vqvkk`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Case processing compliance rate** (stream-level) — Share of cases processed within regulatory timelines.

## 9. Evidence and admission

**Evidence sources:** SRC-018 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-100) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
