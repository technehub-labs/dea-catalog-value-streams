# Referral to Treatment

Admitted Value Stream record (`value-streams:value-stream-referral-to-treatment-fjkv2g`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-referral-to-treatment-fjkv2g` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | healthcare · industry-specific |
| Record | [`value-streams-value-stream-referral-to-treatment-fjkv2g.yaml`](./value-streams-value-stream-referral-to-treatment-fjkv2g.yaml) — authoritative |

## 2. Definition

> The end-to-end stream from specialist referral through triage, booking, and clinical treatment completion.

## 3. Value proposition and served party

**Outcome:** A referred patient receives and completes specialist treatment.

## 4. Stream boundary

**Entry criterion:** A specialist referral is made.

**Exit criterion:** The referred treatment is completed.

**In scope** (from the record's `scope.includes`):

- Referral triage and prioritization
- Booking and preparation
- Treatment delivery
- Outcome and follow-up

**Out of scope** (each concern owned by the named neighbour):

- Emergency care pathways
- Inpatient admission (Admission to Discharge)

## 5. Value stages

Referral to Treatment decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Triage Referral

Receive and prioritize the referral.

| Aspect | Value |
|---|---|
| Entry criterion | A specialist referral is made. |
| Exit criterion | The referral is triaged and prioritized. |
| Outcome | A prioritized referral. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Book and Prepare

Book the treatment and prepare the patient.

| Aspect | Value |
|---|---|
| Entry criterion | A referral is prioritized. |
| Exit criterion | The treatment is booked and the patient is prepared. |
| Outcome | A booked, prepared treatment slot. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Deliver Treatment

Deliver the clinical treatment.

| Aspect | Value |
|---|---|
| Entry criterion | The patient is prepared. |
| Exit criterion | The treatment is delivered. |
| Outcome | Completed specialist treatment. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85`, `processes:process-eo-operate-44jsrp` |

### Stage 4: Complete and Follow Up

Confirm treatment outcome and arrange follow-up.

| Aspect | Value |
|---|---|
| Entry criterion | Treatment is delivered. |
| Exit criterion | The outcome is recorded and follow-up arranged. |
| Outcome | A closed referral with follow-up. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-44jsrp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-discharge-to-bill` — Delivered treatment flows to billing.

## 8. Measurement

- **Referral-to-treatment wait time** (stream-level) — Elapsed days from referral to treatment.

## 9. Evidence and admission

**Evidence sources:** SRC-007 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-018) from the CR-VS-11 industry evidence register extension. Industry-specific chain (healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
