# Concept to Launch

Admitted Value Stream record (`value-streams:value-stream-concept-to-launch-nhvatv`, v1.1.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-concept-to-launch-nhvatv` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.1.0 · active |
| Metamodel pin | 1.0.0 |
| Record | [`value-streams-value-stream-concept-to-launch-nhvatv.yaml`](./value-streams-value-stream-concept-to-launch-nhvatv.yaml) — authoritative |

## 2. Definition

> The end-to-end stream from approval of an offering concept through development and launch to its market.

## 3. Value proposition and served party

**Outcome:** A launched offering delivering value to its intended market.

## 4. Stream boundary

**Entry criterion:** An offering concept is approved for development.

**Exit criterion:** The offering is launched to its market.

**In scope** (from the record's `scope.includes`):

- Approved-concept development
- Offering build and validation
- Market-readiness preparation
- Launch to the intended market

**Out of scope** (each concern owned by the named neighbour):

- Pre-concept innovation intake (Idea Management capability, upstream)
- Post-launch proposition evolution (Concept to Launch exits at launch)
- Order flows (Order to Cash)

## 5. Value stages

Concept to Launch decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Approve Concept

Confirm the offering concept is approved for development.

| Aspect | Value |
|---|---|
| Entry criterion | An offering concept is proposed. |
| Exit criterion | The concept is approved for development. |
| Outcome | A funded development mandate. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8`, `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pv-operate-cau4gv` |

### Stage 2: Develop Offering

Build and validate the offering against the approved concept.

| Aspect | Value |
|---|---|
| Entry criterion | A development mandate exists. |
| Exit criterion | The offering is built and validated. |
| Outcome | A validated, launchable offering. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-build-j9z3q4`, `processes:process-eo-operate-44jsrp` |

### Stage 3: Prepare Launch

Prepare the market-facing proposition and readiness.

| Aspect | Value |
|---|---|
| Entry criterion | A validated offering exists. |
| Exit criterion | Market readiness is confirmed. |
| Outcome | Launch-ready propositions and readiness. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-marketing-xmc539`, `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-pv-activate-5686v7` |

### Stage 4: Launch

Release the offering to its market.

| Aspect | Value |
|---|---|
| Entry criterion | Market readiness is confirmed. |
| Exit criterion | The offering is launched to its market. |
| Outcome | A launched offering delivering value. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539`, `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-pv-activate-5686v7` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-operations-management-pm3w8k`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pv-operate-cau4gv`
- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-44jsrp`
- `processes:process-pv-activate-5686v7`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-order-to-cash` — A launched offering becomes sellable and can be ordered.

## 8. Measurement

- **Concept-to-launch lead time** (stage: Launch) — Elapsed time from concept approval to market launch.
- **Launch readiness pass rate** (stage: Prepare Launch) — Share of launch-readiness gates passed at first review.

## 9. Evidence and admission

**Evidence sources:** SRC-002, SRC-006 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted from candidate VSC-004 under CR-VS-04 (evidence raised E2 -> E3 via register v0.2 extension; distinctness closed per CR-VS-02). Innovation/launch chain; distinct from the development value stream (VSC-010 disambiguation record, out of scope) by its market-facing exit. Distinct from Order to Cash on entry, exit, and served party (market vs. customer).

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-27 | Emmanuel A. Otchere, candidate universe v0.1 (CR-VS-01, PR #3) |
| candidate | 2026-10-27 | Emmanuel A. Otchere, evidence raised E2 -> E3 (CR-VS-04, register v0.2) |
| admitted | 2026-10-27 | Emmanuel A. Otchere, admission CR-VS-04 |
| active | 2026-10-27 | Emmanuel A. Otchere, CR-VS-07 enrichment (value stages, process links, scope, metrics) |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
