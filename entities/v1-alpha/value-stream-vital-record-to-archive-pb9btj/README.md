# Vital Record to Archive

Admitted Value Stream record (`value-streams:value-stream-vital-record-to-archive-pb9btj`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-vital-record-to-archive-pb9btj` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | public-sector · industry-specific |
| Record | [`value-streams-value-stream-vital-record-to-archive-pb9btj.yaml`](./value-streams-value-stream-vital-record-to-archive-pb9btj.yaml) — authoritative |

## 2. Definition

> The records stream from vital-event registration through certification to archived, retrievable record.

## 3. Value proposition and served party

**Outcome:** An archived, retrievable vital record with certified copies available.

## 4. Stream boundary

**Entry criterion:** A vital event is registered.

**Exit criterion:** The record is archived and retrievable.

**In scope** (from the record's `scope.includes`):

- Event registration
- Certification
- Archiving

**Out of scope** (each concern owned by the named neighbour):

- Disclosure requests (Request to Disclose)
- Digital archives governance

## 5. Value stages

Vital Record to Archive decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Register Event

Register the vital event.

| Aspect | Value |
|---|---|
| Entry criterion | An event is reported. |
| Exit criterion | The event is registered. |
| Outcome | A registered event. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Certify

Issue certified copies.

| Aspect | Value |
|---|---|
| Entry criterion | The event is registered. |
| Exit criterion | Copies are certified. |
| Outcome | Certified copies. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-8vqvkk` |

### Stage 3: Archive

Archive the record for retrieval.

| Aspect | Value |
|---|---|
| Entry criterion | The event is registered. |
| Exit criterion | The record is archived. |
| Outcome | An archived record. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-operations-management-pm3w8k`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-8vqvkk`
- `processes:process-eo-operate-zwzmbd`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Record retrieval time** (stream-level) — Elapsed time to retrieve an archived record on request.

## 9. Evidence and admission

**Evidence sources:** SRC-014 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-080) from the CR-VS-11 industry evidence register extension. Industry-specific chain (public-sector); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
