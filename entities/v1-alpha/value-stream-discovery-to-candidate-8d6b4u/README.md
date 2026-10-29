# Discovery to Candidate

Admitted Value Stream record (`value-streams:value-stream-discovery-to-candidate-8d6b4u`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-discovery-to-candidate-8d6b4u` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | development |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | life-sciences · industry-specific |
| Record | [`value-streams-value-stream-discovery-to-candidate-8d6b4u.yaml`](./value-streams-value-stream-discovery-to-candidate-8d6b4u.yaml) — authoritative |

## 2. Definition

> The research stream from target identification through screening to a nominated development candidate.

## 3. Value proposition and served party

**Outcome:** A nominated development candidate.

## 4. Stream boundary

**Entry criterion:** A target is identified.

**Exit criterion:** A candidate is nominated for development.

**In scope** (from the record's `scope.includes`):

- Target identification and validation
- Screening
- Candidate nomination

**Out of scope** (each concern owned by the named neighbour):

- Clinical development (Trial to Readout)
- Research platform governance

## 5. Value stages

Discovery to Candidate decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Validate Target

Validate the identified target.

| Aspect | Value |
|---|---|
| Entry criterion | A target is identified. |
| Exit criterion | The target is validated. |
| Outcome | A validated target. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-idea-management-86dckf` |
| Realizing processes | `processes:process-pv-conceive-kps544` |

### Stage 2: Screen

Screen for active candidates.

| Aspect | Value |
|---|---|
| Entry criterion | The target is validated. |
| Exit criterion | Screening is complete. |
| Outcome | Screened candidates. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-2jnz85`, `processes:process-eo-operate-44jsrp` |

### Stage 3: Nominate Candidate

Nominate the development candidate.

| Aspect | Value |
|---|---|
| Entry criterion | Screening is complete. |
| Exit criterion | The candidate is nominated. |
| Outcome | A nominated candidate. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-pv-design-8v4k89` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-idea-management-86dckf`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pv-conceive-kps544`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-44jsrp`
- `processes:process-pv-design-8v4k89`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-concept-to-launch` — The life-sciences specialization of development intake.

**Downstream streams:** none recorded.

## 8. Measurement

- **Discovery project attrition** (stream-level) — Share of targets reaching candidate nomination.

## 9. Evidence and admission

**Evidence sources:** SRC-018 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-101) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
