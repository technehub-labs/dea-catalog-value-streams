# Tender to Award

Admitted Value Stream record (`value-streams:value-stream-tender-to-award-gjmy4d`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-tender-to-award-gjmy4d` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | construction-real-estate · industry-specific |
| Record | [`value-streams-value-stream-tender-to-award-gjmy4d.yaml`](./value-streams-value-stream-tender-to-award-gjmy4d.yaml) — authoritative |

## 2. Definition

> The construction stream from tender invitation through bid preparation and evaluation to contract award.

## 3. Value proposition and served party

**Outcome:** An awarded construction contract.

## 4. Stream boundary

**Entry criterion:** A tender is invited.

**Exit criterion:** The contract is awarded.

**In scope** (from the record's `scope.includes`):

- Bid preparation
- Submission
- Evaluation and clarification
- Award

**Out of scope** (each concern owned by the named neighbour):

- Project execution (Build to Handover)
- Framework agreements

## 5. Value stages

Tender to Award decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Prepare Bid

Prepare the bid against the tender.

| Aspect | Value |
|---|---|
| Entry criterion | A tender is invited. |
| Exit criterion | The bid is ready. |
| Outcome | A prepared bid. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-conceive-4uqqvg` |

### Stage 2: Submit

Submit the bid.

| Aspect | Value |
|---|---|
| Entry criterion | The bid is ready. |
| Exit criterion | The bid is submitted. |
| Outcome | A submitted bid. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-partner-management-cp3vdb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 3: Evaluate and Clarify

Respond to evaluation clarification.

| Aspect | Value |
|---|---|
| Entry criterion | The bid is submitted. |
| Exit criterion | Clarifications are closed. |
| Outcome | Closed clarifications. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-partner-management-cp3vdb` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 4: Award

Award and execute the contract.

| Aspect | Value |
|---|---|
| Entry criterion | Evaluation completes. |
| Exit criterion | The contract is awarded and executed. |
| Outcome | An awarded contract. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-conceive-4uqqvg`
- `processes:process-pr-operate-bbe384`
- `processes:process-ge-build-mctdgc`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Bid win rate** (stream-level) — Awarded bids as a share of submitted.

## 9. Evidence and admission

**Evidence sources:** SRC-017 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-092) from the CR-VS-11 industry evidence register extension. Industry-specific chain (construction-real-estate); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
