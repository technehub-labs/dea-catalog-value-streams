# Customer Remediation to Current

Admitted Value Stream record (`value-streams:value-stream-customer-remediation-to-current-krrxzb`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-customer-remediation-to-current-krrxzb` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | financial-services · industry-specific |
| Record | [`value-streams-value-stream-customer-remediation-to-current-krrxzb.yaml`](./value-streams-value-stream-customer-remediation-to-current-krrxzb.yaml) — authoritative |

## 2. Definition

> The due-diligence remediation stream from an identified KYC/due-diligence backlog item through customer engagement to a current compliance status.

## 3. Value proposition and served party

**Outcome:** All due-diligence records current or the relationship exited.

## 4. Stream boundary

**Entry criterion:** A due-diligence review falls due or is flagged.

**Exit criterion:** The customer file is current or the relationship is exited.

**In scope** (from the record's `scope.includes`):

- Backlog identification
- Customer engagement and document collection
- Assessment and status update
- Escalation or exit where unresolved

**Out of scope** (each concern owned by the named neighbour):

- New-customer onboarding (Onboard to Activate)
- Financial-crime alert handling (Alert to Report)

## 5. Value stages

Customer Remediation to Current decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Identify Backlog

Identify and prioritize due-diligence backlog.

| Aspect | Value |
|---|---|
| Entry criterion | A review falls due. |
| Exit criterion | The backlog item is prioritized. |
| Outcome | A prioritized backlog item. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 2: Engage Customer

Engage the customer for updated information and documents.

| Aspect | Value |
|---|---|
| Entry criterion | The item is prioritized. |
| Exit criterion | Required information is collected. |
| Outcome | A complete remediation file. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 3: Assess and Update

Assess the file and update the compliance status.

| Aspect | Value |
|---|---|
| Entry criterion | Information is collected. |
| Exit criterion | The status is updated. |
| Outcome | A current compliance status. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 4: Escalate or Exit

Escalate or exit the unresolved relationship.

| Aspect | Value |
|---|---|
| Entry criterion | Assessment fails. |
| Exit criterion | The relationship is escalated or exited. |
| Outcome | A dispositioned relationship. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-zwaes5`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **KYC remediation backlog ratio** (stream-level) — Backlogged files as a share of the portfolio.

## 9. Evidence and admission

**Evidence sources:** SRC-012 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-028) from the CR-VS-11 industry evidence register extension. Industry-specific chain (financial-services); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
