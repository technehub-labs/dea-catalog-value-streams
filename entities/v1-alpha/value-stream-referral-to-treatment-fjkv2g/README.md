---
documentation_generated_from: value-streams-value-stream-referral-to-treatment-fjkv2g.yaml
id: value-streams:value-stream-referral-to-treatment-fjkv2g
name: Referral to Treatment
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- healthcare
specificity: industry-specific
entry_criterion: A specialist referral is made.
exit_criterion: The referred treatment is completed.
outcome: A referred patient receives and completes specialist treatment.
stages:
- Triage Referral
- Book and Prepare
- Deliver Treatment
- Complete and Follow Up
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
processes:
- processes:process-eo-operate-2jnz85
- processes:process-eo-operate-44jsrp
- processes:process-pr-operate-bbe384
metrics:
- Referral-to-treatment wait time
upstream: []
downstream:
- value-stream-discharge-to-bill
evidence_sources:
- SRC-007
---

# Referral to Treatment

`value-streams:value-stream-referral-to-treatment-fjkv2g` · **operational** · healthcare · industry-specific

> The end-to-end stream from specialist referral through triage, booking, and clinical treatment completion.

**Outcome:** A referred patient receives and completes specialist treatment.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-referral-to-treatment-fjkv2g.yaml`](./value-streams-value-stream-referral-to-treatment-fjkv2g.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Triage Referral"]
  S2["2. Book and Prepare"]
  S3["3. Deliver Treatment"]
  S4["4. Complete and Follow Up"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Triage Referral** | A specialist referral is made. | The referral is triaged and prioritized. | 2 | 1 | yes |
| 2 | **Book and Prepare** | A referral is prioritized. | The treatment is booked and the patient is prepared. | 2 | 1 | yes |
| 3 | **Deliver Treatment** | The patient is prepared. | The treatment is delivered. | 1 | 2 | yes |
| 4 | **Complete and Follow Up** | Treatment is delivered. | The outcome is recorded and follow-up arranged. | 2 | 1 | yes |

### 1. Triage Referral

Receive and prioritize the referral.

| Aspect | Value |
|---|---|
| Entry criterion | A specialist referral is made. |
| Exit criterion | The referral is triaged and prioritized. |
| Outcome | A prioritized referral. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 2. Book and Prepare

Book the treatment and prepare the patient.

| Aspect | Value |
|---|---|
| Entry criterion | A referral is prioritized. |
| Exit criterion | The treatment is booked and the patient is prepared. |
| Outcome | A booked, prepared treatment slot. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### 3. Deliver Treatment

Deliver the clinical treatment.

| Aspect | Value |
|---|---|
| Entry criterion | The patient is prepared. |
| Exit criterion | The treatment is delivered. |
| Outcome | Completed specialist treatment. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` · `processes:process-eo-operate-44jsrp` |

### 4. Complete and Follow Up

Confirm treatment outcome and arrange follow-up.

| Aspect | Value |
|---|---|
| Entry criterion | Treatment is delivered. |
| Exit criterion | The outcome is recorded and follow-up arranged. |
| Outcome | A closed referral with follow-up. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## Scope boundary

**Entry:** A specialist referral is made.

**Exit:** The referred treatment is completed.

**In scope**

- Referral triage and prioritization
- Booking and preparation
- Treatment delivery
- Outcome and follow-up

**Out of scope** (owned by the named neighbour)

- Emergency care pathways
- Inpatient admission (Admission to Discharge)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-44jsrp`

## Cross-stream links

**Upstream:** none recorded.

**Downstream** (this stream's exit feeds their entry):

- [discharge to bill](../value-stream-discharge-to-bill-3k7wbb/README.md) — Delivered treatment flows to billing.

## Measurement

- **Referral-to-treatment wait time** (stream-level) — Elapsed days from referral to treatment.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-007 | industry-reference-model | Healthcare industry reference models (patient-access and revenue-cycle chains, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-018) from the CR-VS-11 industry evidence register extension. Industry-specific chain (healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
