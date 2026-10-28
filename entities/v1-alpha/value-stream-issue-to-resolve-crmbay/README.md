# Issue to Resolve

Admitted Value Stream record (`value-streams:value-stream-issue-to-resolve-crmbay`, v1.1.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-issue-to-resolve-crmbay` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.1.0 · active |
| Metamodel pin | 1.0.0 |
| Record | [`value-streams-value-stream-issue-to-resolve-crmbay.yaml`](./value-streams-value-stream-issue-to-resolve-crmbay.yaml) — authoritative |

## 2. Definition

> The end-to-end stream from a raised customer issue through diagnosis, corrective action, and confirmed resolution.

## 3. Value proposition and served party

**Outcome:** The customer's issue is resolved and trust is restored.

## 4. Stream boundary

**Entry criterion:** A customer raises an issue or complaint.

**Exit criterion:** The issue is resolved and the customer is informed.

**In scope** (from the record's `scope.includes`):

- Issue intake and triage
- Diagnosis and root-cause analysis
- Corrective action execution
- Resolution confirmation and closure

**Out of scope** (each concern owned by the named neighbour):

- Order flows (Order to Cash)
- Contractual relationship management (Contract to Renewal)
- Multi-channel journey design (out of scope at first order)

## 5. Value stages

Issue to Resolve decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Intake Issue

Capture and classify the customer issue or complaint.

| Aspect | Value |
|---|---|
| Entry criterion | A customer raises an issue or complaint. |
| Exit criterion | The issue is logged and classified. |
| Outcome | A visible, owned issue record. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Diagnose

Investigate the issue and identify root cause.

| Aspect | Value |
|---|---|
| Entry criterion | An owned issue record exists. |
| Exit criterion | Root cause is identified and corrective path chosen. |
| Outcome | An understood cause and corrective plan. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 3: Correct

Execute the corrective action.

| Aspect | Value |
|---|---|
| Entry criterion | A corrective plan exists. |
| Exit criterion | The corrective action is executed. |
| Outcome | A restored customer situation. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 4: Confirm Resolution

Confirm resolution with the customer and close the record.

| Aspect | Value |
|---|---|
| Entry criterion | The corrective action is executed. |
| Exit criterion | The issue is resolved and the customer is informed. |
| Outcome | Restored trust and a closed issue. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-2jnz85`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-order-to-cash` — Issues typically arise after fulfillment of an order.
- `value-streams:value-value-stream-contract-to-renewal` — Service issues surface during the contracted relationship.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-return-to-credit` — Unresolved dissatisfaction can convert to a return.

## 8. Measurement

- **Mean time to resolve** (stage: Confirm Resolution) — Average elapsed time from issue intake to confirmed resolution.
- **First-contact resolution rate** (stage: Diagnose) — Share of issues resolved without handoff or repeat contact.

## 9. Evidence and admission

**Evidence sources:** SRC-006 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted from candidate VSC-003 under CR-VS-03 (evidence at E3/high, distinctness closed per CR-VS-02). Service-side chain: no order is involved; distinct from Order to Cash on entry and exit, and from journeys (multi-channel experience is out of scope at first order). Alternate name: Fault to Restore (VSC-014, merged per CR-VS-05 RES-003).

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.1 (CR-VS-01, PR #3) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-03 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
