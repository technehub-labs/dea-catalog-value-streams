# Regulatory Dossier to Approval

Admitted Value Stream record (`value-streams:value-stream-regulatory-dossier-to-approval-mgbk2u`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-regulatory-dossier-to-approval-mgbk2u` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | life-sciences · industry-specific |
| Record | [`value-streams-value-stream-regulatory-dossier-to-approval-mgbk2u.yaml`](./value-streams-value-stream-regulatory-dossier-to-approval-mgbk2u.yaml) — authoritative |

## 2. Definition

> The regulatory stream from dossier compilation through submission to marketing approval.

## 3. Value proposition and served party

**Outcome:** A received marketing approval for the dossier.

## 4. Stream boundary

**Entry criterion:** A dossier compilation cycle opens.

**Exit criterion:** The approval is received.

**In scope** (from the record's `scope.includes`):

- Dossier compilation
- Submission
- Review response and approval

**Out of scope** (each concern owned by the named neighbour):

- Clinical readout (Trial to Readout)
- Lifecycle license maintenance

## 5. Value stages

Regulatory Dossier to Approval decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Compile Dossier

Compile the regulatory dossier.

| Aspect | Value |
|---|---|
| Entry criterion | A cycle opens. |
| Exit criterion | The dossier is complete. |
| Outcome | A complete dossier. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

### Stage 2: Submit

Submit the dossier.

| Aspect | Value |
|---|---|
| Entry criterion | The dossier is complete. |
| Exit criterion | The submission is accepted. |
| Outcome | An accepted submission. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8`, `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-fa-operate-8vqvkk` |

### Stage 3: Respond and Gain Approval

Respond to review questions and gain approval.

| Aspect | Value |
|---|---|
| Entry criterion | Review questions arrive. |
| Exit criterion | The approval is received. |
| Outcome | A received approval. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-ycba3k`
- `processes:process-fa-operate-8vqvkk`
- `processes:process-ge-operate-zwaes5`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Submission-to-approval time** (stream-level) — Elapsed months from submission to approval.

## 9. Evidence and admission

**Evidence sources:** SRC-018 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-102) from the CR-VS-11 industry evidence register extension. Industry-specific chain (life-sciences); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
