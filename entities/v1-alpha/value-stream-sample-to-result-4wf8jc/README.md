---
documentation_generated_from: value-streams-value-stream-sample-to-result-4wf8jc.yaml
id: value-streams:value-stream-sample-to-result-4wf8jc
name: Sample to Result
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- life-sciences
- healthcare
specificity: industry-specific
entry_criterion: A sample is received.
exit_criterion: The result is released and communicated.
outcome: A released result communicated to the ordering clinician.
stages:
- Accession Sample
- Test
- Review and Release
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-risk-management-h9uxdw
- capabilities:capability-technology-enablement-y6nkws
processes:
- processes:process-eo-operate-44jsrp
- processes:process-eo-operate-xud3hs
- processes:process-eo-operate-zwzmbd
- processes:process-ge-operate-zwaes5
- processes:process-pr-operate-bbe384
metrics:
- Sample-to-result turnaround
upstream:
- value-stream-referral-to-treatment
downstream: []
evidence_sources:
- SRC-018
- SRC-007
---

# Sample to Result

`value-streams:value-stream-sample-to-result-4wf8jc` · **operational** · life-sciences, healthcare · industry-specific

> The diagnostics stream from sample accessioning through testing to a released, communicated result.

**Outcome:** A released result communicated to the ordering clinician.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-sample-to-result-4wf8jc.yaml`](./value-streams-value-stream-sample-to-result-4wf8jc.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Accession Sample"]
  S2["2. Test"]
  S3["3. Review and Release"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Accession Sample** | A sample is received. | The sample is accessioned. | 2 | 1 | no |
| 2 | **Test** | The sample is accessioned. | Testing is complete. | 2 | 2 | no |
| 3 | **Review and Release** | Testing is complete. | The result is released and communicated. | 2 | 2 | yes |

### 1. Accession Sample

Accession and register the sample.

| Aspect | Value |
|---|---|
| Entry criterion | A sample is received. |
| Exit criterion | The sample is accessioned. |
| Outcome | An accessioned sample. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

### 2. Test

Perform the diagnostic testing.

| Aspect | Value |
|---|---|
| Entry criterion | The sample is accessioned. |
| Exit criterion | Testing is complete. |
| Outcome | Test results. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-operate-44jsrp` · `processes:process-eo-operate-xud3hs` |

### 3. Review and Release

Review and release the result.

| Aspect | Value |
|---|---|
| Entry criterion | Testing is complete. |
| Exit criterion | The result is released and communicated. |
| Outcome | A communicated result. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-ge-operate-zwaes5` · `processes:process-pr-operate-bbe384` |

## Scope boundary

**Entry:** A sample is received.

**Exit:** The result is released and communicated.

**In scope**

- Accessioning
- Testing
- Result review and release

**Out of scope** (owned by the named neighbour)

- Patient treatment (Referral to Treatment)
- Clinical trials lab work

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-customer-management-f3n8wb`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-xud3hs`
- `processes:process-ge-operate-zwaes5`
- `processes:process-pr-operate-bbe384`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [referral to treatment](../value-stream-referral-to-treatment-fjkv2g/README.md) — Released results inform treatment.

**Downstream:** none recorded.

## Measurement

- **Sample-to-result turnaround** (stream-level) — Elapsed time from accessioning to released result.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-018 | industry-reference-model | Life-sciences reference chains (public GxP/ICH category structure) |
| SRC-007 | industry-reference-model | Healthcare industry reference models (patient-access and revenue-cycle chains, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-104) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences, healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
