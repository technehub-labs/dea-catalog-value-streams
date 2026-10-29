---
documentation_generated_from: value-streams-value-stream-research-grant-to-publication-qwc4f8.yaml
id: value-streams:value-stream-research-grant-to-publication-qwc4f8
name: Research Grant to Publication
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- education
specificity: industry-specific
entry_criterion: A research grant is awarded.
exit_criterion: The findings are published and disseminated.
outcome: Published, disseminated research findings.
stages:
- Set Up Project
- Conduct Research
- Publish and Disseminate
capabilities:
- capabilities:capability-information-management-6vjgdh
- capabilities:capability-insight-management-ms4n9d
- capabilities:capability-offering-management-6egkc8
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-workforce-management-9e8d8s
processes:
- processes:process-ao-operate-87q5mk
- processes:process-eo-operate-2jnz85
- processes:process-fa-operate-ycba3k
metrics:
- Grant-to-publication rate
upstream: []
downstream: []
evidence_sources:
- SRC-015
---

# Research Grant to Publication

`value-streams:value-stream-research-grant-to-publication-qwc4f8` · **operational** · education · industry-specific

> The research stream from grant award through conduct to publication and dissemination.

**Outcome:** Published, disseminated research findings.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-research-grant-to-publication-qwc4f8.yaml`](./value-streams-value-stream-research-grant-to-publication-qwc4f8.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Set Up Project"]
  S2["2. Conduct Research"]
  S3["3. Publish and Disseminate"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Set Up Project** | A grant is awarded. | The project is set up. | 2 | 1 | no |
| 2 | **Conduct Research** | The project is set up. | The research is complete. | 2 | 1 | no |
| 3 | **Publish and Disseminate** | The research is complete. | The findings are published. | 2 | 1 | yes |

### 1. Set Up Project

Set up the research project.

| Aspect | Value |
|---|---|
| Entry criterion | A grant is awarded. |
| Exit criterion | The project is set up. |
| Outcome | A set-up project. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-ao-operate-87q5mk` |

### 2. Conduct Research

Conduct the research.

| Aspect | Value |
|---|---|
| Entry criterion | The project is set up. |
| Exit criterion | The research is complete. |
| Outcome | Completed research. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### 3. Publish and Disseminate

Publish and disseminate the findings.

| Aspect | Value |
|---|---|
| Entry criterion | The research is complete. |
| Exit criterion | The findings are published. |
| Outcome | Published findings. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` · `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

## Scope boundary

**Entry:** A research grant is awarded.

**Exit:** The findings are published and disseminated.

**In scope**

- Project setup
- Research conduct
- Publication and dissemination

**Out of scope** (owned by the named neighbour)

- Teaching delivery
- Grant administration (Grant Award to Closeout pattern)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-offering-management-6egkc8`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ao-operate-87q5mk`
- `processes:process-eo-operate-2jnz85`
- `processes:process-fa-operate-ycba3k`

## Cross-stream links

**Upstream:** none recorded.

**Downstream:** none recorded.

## Measurement

- **Grant-to-publication rate** (stream-level) — Share of grants resulting in publication within window.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-015 | industry-reference-model | Education and hospitality service chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-083) from the CR-VS-11 industry evidence register extension. Industry-specific chain (education); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
