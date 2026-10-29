# Apply to Decide

Admitted Value Stream record (`value-streams:value-stream-apply-to-decide-qr36mf`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-apply-to-decide-qr36mf` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | public-sector · industry-specific |
| Record | [`value-streams-value-stream-apply-to-decide-qr36mf.yaml`](./value-streams-value-stream-apply-to-decide-qr36mf.yaml) — authoritative |

## 2. Definition

> The public-administration stream from application receipt through completeness and eligibility assessment to a communicated, reasoned decision.

## 3. Value proposition and served party

**Outcome:** A lawful, reasoned, communicated decision within the service standard.

## 4. Stream boundary

**Entry criterion:** An application (permit, grant, benefit, license) is received.

**Exit criterion:** The decision is communicated with reasons.

**In scope** (from the record's `scope.includes`):

- Application registration and completeness
- Eligibility and merits assessment
- Decision and communication
- Appeal handling

**Out of scope** (each concern owned by the named neighbour):

- Records disclosure (Request to Disclose)
- Enforcement actions

## 5. Value stages

Apply to Decide decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Register Application

Register the application and check completeness.

| Aspect | Value |
|---|---|
| Entry criterion | An application is received. |
| Exit criterion | The application is complete. |
| Outcome | A complete application. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Assess

Assess eligibility and merits.

| Aspect | Value |
|---|---|
| Entry criterion | The application is complete. |
| Exit criterion | The assessment is complete. |
| Outcome | A completed assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Decide and Communicate

Decide and communicate with reasons.

| Aspect | Value |
|---|---|
| Entry criterion | The assessment is complete. |
| Exit criterion | The decision is communicated. |
| Outcome | A communicated decision. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 4: Handle Appeal

Handle any appeal.

| Aspect | Value |
|---|---|
| Entry criterion | An appeal is lodged. |
| Exit criterion | The appeal is resolved. |
| Outcome | A resolved appeal. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-zwaes5`
- `processes:process-ge-build-mctdgc`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Decision cycle time vs service standard** (stream-level) — Elapsed time from receipt to communicated decision against the standard.

## 9. Evidence and admission

**Evidence sources:** SRC-014 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-073) from the CR-VS-11 industry evidence register extension. Industry-specific chain (public-sector); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
