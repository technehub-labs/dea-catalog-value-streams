# Alert to Report

Admitted Value Stream record (`value-streams:value-stream-alert-to-report-a2qttg`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-alert-to-report-a2qttg` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | financial-services · industry-specific |
| Record | [`value-streams-value-stream-alert-to-report-a2qttg.yaml`](./value-streams-value-stream-alert-to-report-a2qttg.yaml) — authoritative |

## 2. Definition

> The financial-crime stream from alert detection through investigation to the reporting decision.

## 3. Value proposition and served party

**Outcome:** A completed, defensible reporting decision on every financial-crime alert.

## 4. Stream boundary

**Entry criterion:** A monitoring alert is generated.

**Exit criterion:** The reporting decision is made and filed where required.

**In scope** (from the record's `scope.includes`):

- Alert triage
- Investigation
- Decision and quality review
- Regulatory filing or closure

**Out of scope** (each concern owned by the named neighbour):

- Customer onboarding due diligence (Onboard to Activate)
- General risk reporting

## 5. Value stages

Alert to Report decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Triage Alert

Triage the monitoring alert.

| Aspect | Value |
|---|---|
| Entry criterion | An alert is generated. |
| Exit criterion | The alert is triaged. |
| Outcome | A triaged alert. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 2: Investigate

Investigate the alerted activity.

| Aspect | Value |
|---|---|
| Entry criterion | The alert is triaged. |
| Exit criterion | The investigation is complete. |
| Outcome | A completed investigation. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Decide and Review

Make the reporting decision with quality review.

| Aspect | Value |
|---|---|
| Entry criterion | The investigation is complete. |
| Exit criterion | The decision is made and reviewed. |
| Outcome | A reviewed decision. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 4: File or Close

File the report or close with rationale.

| Aspect | Value |
|---|---|
| Entry criterion | The decision is made. |
| Exit criterion | The report is filed or the alert closed with rationale. |
| Outcome | A dispositioned alert. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-fa-operate-8vqvkk` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-regulation-management-gya4d8`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-operate-zwaes5`
- `processes:process-fa-operate-8vqvkk`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Alert-to-decision cycle time** (stream-level) — Elapsed days from alert to disposition.

## 9. Evidence and admission

**Evidence sources:** SRC-012 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-025) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
