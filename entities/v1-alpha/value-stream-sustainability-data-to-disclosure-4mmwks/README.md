---
documentation_generated_from: value-streams-value-stream-sustainability-data-to-disclosure-4mmwks.yaml
id: value-streams:value-stream-sustainability-data-to-disclosure-4mmwks
name: Sustainability Data to Disclosure
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: governance
industries:
- manufacturing
- utilities-energy
specificity: industry-specific
entry_criterion: A reporting cycle opens.
exit_criterion: The disclosure is published with assurance.
outcome: An assured sustainability disclosure.
stages:
- Capture Data
- Assure
- Disclose
capabilities:
- capabilities:capability-enterprise-governance-uas48u
- capabilities:capability-financial-stewardship-c7xtfk
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-risk-management-h9uxdw
processes:
- processes:process-fa-operate-g9zpnq
- processes:process-fa-operate-ycba3k
- processes:process-ge-operate-zwaes5
metrics:
- Disclosure data completeness
upstream: []
downstream: []
evidence_sources:
- SRC-016
- SRC-011
---

# Sustainability Data to Disclosure

`value-streams:value-stream-sustainability-data-to-disclosure-4mmwks` · **governance** · manufacturing, utilities-energy · industry-specific

> The ESG stream from sustainability data capture through assurance to disclosure.

**Outcome:** An assured sustainability disclosure.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-sustainability-data-to-disclosure-4mmwks.yaml`](./value-streams-value-stream-sustainability-data-to-disclosure-4mmwks.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Capture Data"]
  S2["2. Assure"]
  S3["3. Disclose"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Capture Data** | A cycle opens. | The dataset is complete. | 2 | 1 | no |
| 2 | **Assure** | The dataset is complete. | Assurance is complete. | 2 | 1 | no |
| 3 | **Disclose** | Assurance is complete. | The disclosure is published. | 2 | 1 | no |

### 1. Capture Data

Capture and aggregate sustainability data.

| Aspect | Value |
|---|---|
| Entry criterion | A cycle opens. |
| Exit criterion | The dataset is complete. |
| Outcome | A complete dataset. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### 2. Assure

Assure the data and disclosures.

| Aspect | Value |
|---|---|
| Entry criterion | The dataset is complete. |
| Exit criterion | Assurance is complete. |
| Outcome | Assured data. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u` · `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### 3. Disclose

Publish the disclosure.

| Aspect | Value |
|---|---|
| Entry criterion | Assurance is complete. |
| Exit criterion | The disclosure is published. |
| Outcome | A published disclosure. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` · `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

## Scope boundary

**Entry:** A reporting cycle opens.

**Exit:** The disclosure is published with assurance.

**In scope**

- Data capture and aggregation
- Assurance
- Disclosure

**Out of scope** (owned by the named neighbour)

- Financial reporting (Record to Report)
- Regulatory filings

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-g9zpnq`
- `processes:process-ge-operate-zwaes5`
- `processes:process-fa-operate-ycba3k`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Disclosure data completeness** (stream-level) — Share of required data points with assured values.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-016 | industry-reference-model | Manufacturing and logistics reference models (SCOR-style category structure) |
| SRC-011 | industry-reference-model | Utilities industry reference models (metering and retail-energy chains, public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-057) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing, utilities-energy); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
