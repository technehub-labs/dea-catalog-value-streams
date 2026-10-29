# Policy to Endorsement

Admitted Value Stream record (`value-streams:value-stream-policy-to-endorsement-3jwbzy`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-policy-to-endorsement-3jwbzy` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | insurance · industry-specific |
| Record | [`value-streams-value-stream-policy-to-endorsement-3jwbzy.yaml`](./value-streams-value-stream-policy-to-endorsement-3jwbzy.yaml) — authoritative |

## 2. Definition

> The policy-administration stream from an endorsement request through assessment to an issued policy change.

## 3. Value proposition and served party

**Outcome:** An accurately issued endorsement on the in-force policy.

## 4. Stream boundary

**Entry criterion:** An endorsement request is received.

**Exit criterion:** The endorsement is issued and billed.

**In scope** (from the record's `scope.includes`):

- Endorsement intake
- Assessment and pricing
- Issuance
- Billing adjustment

**Out of scope** (each concern owned by the named neighbour):

- Renewal (Contract to Renewal)
- New business (Quote to Bind)

## 5. Value stages

Policy to Endorsement decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Intake Request

Receive and clarify the endorsement request.

| Aspect | Value |
|---|---|
| Entry criterion | A request is received. |
| Exit criterion | The request is complete. |
| Outcome | A complete request. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Assess and Price

Assess the change and price the premium impact.

| Aspect | Value |
|---|---|
| Entry criterion | The request is complete. |
| Exit criterion | The change is assessed and priced. |
| Outcome | A priced change. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 3: Issue Endorsement

Issue the endorsement to the policy.

| Aspect | Value |
|---|---|
| Entry criterion | The change is priced. |
| Exit criterion | The endorsement is issued. |
| Outcome | An issued endorsement. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 4: Adjust Billing

Adjust billing for the change.

| Aspect | Value |
|---|---|
| Entry criterion | The endorsement is issued. |
| Exit criterion | Billing reflects the change. |
| Outcome | Reconciled billing. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-tpenm6`
- `processes:process-ge-build-mctdgc`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Endorsement issuance turnaround** (stream-level) — Elapsed time from request to issued endorsement.

## 9. Evidence and admission

**Evidence sources:** SRC-009 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-031) from the CR-VS-11 industry evidence register extension. Industry-specific chain (insurance); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
