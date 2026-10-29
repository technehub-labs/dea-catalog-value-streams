# Research Grant to Publication

Admitted Value Stream record (`value-streams:value-stream-research-grant-to-publication-qwc4f8`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-research-grant-to-publication-qwc4f8` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | education · industry-specific |
| Record | [`value-streams-value-stream-research-grant-to-publication-qwc4f8.yaml`](./value-streams-value-stream-research-grant-to-publication-qwc4f8.yaml) — authoritative |

## 2. Definition

> The research stream from grant award through conduct to publication and dissemination.

## 3. Value proposition and served party

**Outcome:** Published, disseminated research findings.

## 4. Stream boundary

**Entry criterion:** A research grant is awarded.

**Exit criterion:** The findings are published and disseminated.

**In scope** (from the record's `scope.includes`):

- Project setup
- Research conduct
- Publication and dissemination

**Out of scope** (each concern owned by the named neighbour):

- Teaching delivery
- Grant administration (Grant Award to Closeout pattern)

## 5. Value stages

Research Grant to Publication decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Set Up Project

Set up the research project.

| Aspect | Value |
|---|---|
| Entry criterion | A grant is awarded. |
| Exit criterion | The project is set up. |
| Outcome | A set-up project. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-ao-operate-87q5mk` |

### Stage 2: Conduct Research

Conduct the research.

| Aspect | Value |
|---|---|
| Entry criterion | The project is set up. |
| Exit criterion | The research is complete. |
| Outcome | Completed research. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Publish and Disseminate

Publish and disseminate the findings.

| Aspect | Value |
|---|---|
| Entry criterion | The research is complete. |
| Exit criterion | The findings are published. |
| Outcome | Published findings. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-offering-management-6egkc8`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ao-operate-87q5mk`
- `processes:process-eo-operate-2jnz85`
- `processes:process-fa-operate-ycba3k`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Grant-to-publication rate** (stream-level) — Share of grants resulting in publication within window.

## 9. Evidence and admission

**Evidence sources:** SRC-015 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-083) from the CR-VS-11 industry evidence register extension. Industry-specific chain (education); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
