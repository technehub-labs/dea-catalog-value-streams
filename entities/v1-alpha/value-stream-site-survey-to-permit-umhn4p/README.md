# Site Survey to Permit

Admitted Value Stream record (`value-streams:value-stream-site-survey-to-permit-umhn4p`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-site-survey-to-permit-umhn4p` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | construction-real-estate · industry-specific |
| Record | [`value-streams-value-stream-site-survey-to-permit-umhn4p.yaml`](./value-streams-value-stream-site-survey-to-permit-umhn4p.yaml) — authoritative |

## 2. Definition

> The development stream from site survey through design submission to issued planning/building permit.

## 3. Value proposition and served party

**Outcome:** An issued development permit.

## 4. Stream boundary

**Entry criterion:** A development need is identified.

**Exit criterion:** The permit is issued.

**In scope** (from the record's `scope.includes`):

- Site survey and feasibility
- Design submission
- Permit review and issuance

**Out of scope** (each concern owned by the named neighbour):

- Construction (Build to Handover)
- Regulatory inspections (Inspection to Certificate)

## 5. Value stages

Site Survey to Permit decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Survey Site

Survey the site and assess feasibility.

| Aspect | Value |
|---|---|
| Entry criterion | A need is identified. |
| Exit criterion | Feasibility is confirmed. |
| Outcome | A feasible site. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-technology-management-maus5n` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

### Stage 2: Submit Design

Submit the design for permitting.

| Aspect | Value |
|---|---|
| Entry criterion | Feasibility is confirmed. |
| Exit criterion | The design is submitted. |
| Outcome | A submitted design. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8`, `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-pv-design-8v4k89` |

### Stage 3: Obtain Permit

Respond to review and obtain the permit.

| Aspect | Value |
|---|---|
| Entry criterion | The design is submitted. |
| Exit criterion | The permit is issued. |
| Outcome | An issued permit. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8`, `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-fa-operate-8vqvkk` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-operate-ucxpz4`
- `processes:process-pv-design-8v4k89`
- `processes:process-fa-operate-8vqvkk`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Permit approval cycle time** (stream-level) — Elapsed days from submission to issued permit.

## 9. Evidence and admission

**Evidence sources:** SRC-017 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-097) from the CR-VS-11 industry evidence register extension. Industry-specific chain (construction-real-estate); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
