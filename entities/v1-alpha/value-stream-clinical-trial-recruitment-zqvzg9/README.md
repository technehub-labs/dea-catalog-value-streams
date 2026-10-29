---
documentation_generated_from: value-streams-value-stream-clinical-trial-recruitment-zqvzg9.yaml
id: value-streams:value-stream-clinical-trial-recruitment-zqvzg9
name: Clinical Trial Recruitment
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- life-sciences
- healthcare
specificity: industry-specific
entry_criterion: A trial protocol is approved and the site is activated.
exit_criterion: The site reaches its enrollment target.
outcome: A fully enrolled clinical trial cohort at the site.
stages:
- Activate Site
- Identify and Screen
- Consent
- Enroll
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-partner-management-cp3vdb
processes:
- processes:process-eo-build-j9z3q4
- processes:process-eo-operate-2jnz85
- processes:process-ge-build-mctdgc
- processes:process-pr-operate-bbe384
metrics:
- Clinical trial enrollment cycle time
upstream:
- value-stream-trial-to-readout
downstream: []
evidence_sources:
- SRC-018
---

# Clinical Trial Recruitment

`value-streams:value-stream-clinical-trial-recruitment-zqvzg9` · **operational** · life-sciences, healthcare · industry-specific

> The end-to-end stream from trial-site preparation through patient identification, consent, and enrollment into a clinical trial.

**Outcome:** A fully enrolled clinical trial cohort at the site.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-clinical-trial-recruitment-zqvzg9.yaml`](./value-streams-value-stream-clinical-trial-recruitment-zqvzg9.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Activate Site"]
  S2["2. Identify and Screen"]
  S3["3. Consent"]
  S4["4. Enroll"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Activate Site** | The protocol is approved. | The site is activated and ready. | 2 | 1 | no |
| 2 | **Identify and Screen** | The site is activated. | Eligible candidates are identified. | 2 | 1 | no |
| 3 | **Consent** | Eligible candidates are identified. | Consent is documented. | 2 | 1 | yes |
| 4 | **Enroll** | Consent is documented. | The enrollment target is met. | 2 | 1 | no |

### 1. Activate Site

Prepare and activate the trial site.

| Aspect | Value |
|---|---|
| Entry criterion | The protocol is approved. |
| Exit criterion | The site is activated and ready. |
| Outcome | An activated trial site. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-partner-management-cp3vdb` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### 2. Identify and Screen

Identify and screen candidate patients.

| Aspect | Value |
|---|---|
| Entry criterion | The site is activated. |
| Exit criterion | Eligible candidates are identified. |
| Outcome | A screened eligible cohort. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### 3. Consent

Obtain informed consent.

| Aspect | Value |
|---|---|
| Entry criterion | Eligible candidates are identified. |
| Exit criterion | Consent is documented. |
| Outcome | Informed, documented consent. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### 4. Enroll

Enroll consented patients and complete baseline.

| Aspect | Value |
|---|---|
| Entry criterion | Consent is documented. |
| Exit criterion | The enrollment target is met. |
| Outcome | A fully enrolled cohort. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## Scope boundary

**Entry:** A trial protocol is approved and the site is activated.

**Exit:** The site reaches its enrollment target.

**In scope**

- Site activation
- Patient identification and screening
- Informed consent
- Enrollment and baseline

**Out of scope** (owned by the named neighbour)

- Trial conduct and data collection (Trial to Readout)
- Care delivery (Admission to Discharge)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-build-j9z3q4`
- `processes:process-pr-operate-bbe384`
- `processes:process-ge-build-mctdgc`
- `processes:process-eo-operate-2jnz85`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [trial to readout](../value-stream-trial-to-readout-ztkya5/README.md) — Enrollment completes the trial intake.

**Downstream:** none recorded.

## Measurement

- **Clinical trial enrollment cycle time** (stage: Enroll) — Elapsed days from site activation to enrollment target. → [`dea:metric-clinical-trial-enrollment-cycle-time`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-018 | industry-reference-model | Life-sciences reference chains (public GxP/ICH category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-019) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences, healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
