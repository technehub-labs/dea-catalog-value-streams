# Policy Draft to Enactment

Admitted Value Stream record (`value-streams:value-stream-policy-draft-to-enactment-nhqx6e`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-policy-draft-to-enactment-nhqx6e` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | public-sector · industry-specific |
| Record | [`value-streams-value-stream-policy-draft-to-enactment-nhqx6e.yaml`](./value-streams-value-stream-policy-draft-to-enactment-nhqx6e.yaml) — authoritative |

## 2. Definition

> The policy stream from drafting through consultation to enacted and published policy.

## 3. Value proposition and served party

**Outcome:** An enacted, published policy instrument.

## 4. Stream boundary

**Entry criterion:** A policy need is mandated.

**Exit criterion:** The policy is enacted and published.

**In scope** (from the record's `scope.includes`):

- Drafting
- Consultation
- Enactment
- Publication

**Out of scope** (each concern owned by the named neighbour):

- Legislative process
- Regulatory impact analysis

## 5. Value stages

Policy Draft to Enactment decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Draft

Draft the policy instrument.

| Aspect | Value |
|---|---|
| Entry criterion | A mandate exists. |
| Exit criterion | The draft is complete. |
| Outcome | A policy draft. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-build-3p38us` |

### Stage 2: Consult

Run the consultation.

| Aspect | Value |
|---|---|
| Entry criterion | The draft is complete. |
| Exit criterion | The consultation is complete. |
| Outcome | Consultation outcomes. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

### Stage 3: Enact

Enact the policy.

| Aspect | Value |
|---|---|
| Entry criterion | The consultation is complete. |
| Exit criterion | The policy is enacted. |
| Outcome | An enacted policy. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u`, `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 4: Publish

Publish the enacted policy.

| Aspect | Value |
|---|---|
| Entry criterion | The policy is enacted. |
| Exit criterion | The policy is published. |
| Outcome | A published policy. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-build-3p38us` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-build-3p38us`
- `processes:process-sd-operate-ucxpz4`
- `processes:process-ge-build-mctdgc`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Consultation participation** (stream-level) — Responses received per consultation.

## 9. Evidence and admission

**Evidence sources:** SRC-014 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-078) from the CR-VS-11 industry evidence register extension. Industry-specific chain (public-sector); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
