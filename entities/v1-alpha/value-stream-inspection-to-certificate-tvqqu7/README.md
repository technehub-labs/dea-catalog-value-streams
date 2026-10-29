# Inspection to Certificate

Admitted Value Stream record (`value-streams:value-stream-inspection-to-certificate-tvqqu7`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-inspection-to-certificate-tvqqu7` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | public-sector, construction-real-estate · industry-specific |
| Record | [`value-streams-value-stream-inspection-to-certificate-tvqqu7.yaml`](./value-streams-value-stream-inspection-to-certificate-tvqqu7.yaml) — authoritative |

## 2. Definition

> The regulatory-inspection stream from inspection scheduling through on-site inspection to issued certificate.

## 3. Value proposition and served party

**Outcome:** An issued inspection certificate or notice.

## 4. Stream boundary

**Entry criterion:** An inspection falls due or is requested.

**Exit criterion:** The certificate or notice is issued.

**In scope** (from the record's `scope.includes`):

- Inspection scheduling
- On-site inspection
- Assessment
- Certificate issuance

**Out of scope** (each concern owned by the named neighbour):

- Permitting (Apply to Decide)
- Enforcement

## 5. Value stages

Inspection to Certificate decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Schedule Inspection

Schedule the inspection.

| Aspect | Value |
|---|---|
| Entry criterion | An inspection falls due. |
| Exit criterion | The inspection is scheduled. |
| Outcome | A scheduled inspection. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-workforce-planning-b43rhm` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Inspect On Site

Perform the on-site inspection.

| Aspect | Value |
|---|---|
| Entry criterion | The inspection is scheduled. |
| Exit criterion | The inspection is complete. |
| Outcome | Inspection findings. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Assess

Assess findings against the standard.

| Aspect | Value |
|---|---|
| Entry criterion | The inspection is complete. |
| Exit criterion | The assessment is complete. |
| Outcome | A completed assessment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 4: Issue Certificate

Issue the certificate or notice.

| Aspect | Value |
|---|---|
| Entry criterion | The assessment is complete. |
| Exit criterion | The certificate is issued. |
| Outcome | An issued certificate. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-fa-operate-8vqvkk` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-workforce-planning-b43rhm`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-zwaes5`
- `processes:process-eo-operate-44jsrp`
- `processes:process-fa-operate-8vqvkk`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Certificate issuance turnaround** (stream-level) — Elapsed time from inspection to issued certificate.

## 9. Evidence and admission

**Evidence sources:** SRC-014, SRC-017 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-077) from the CR-VS-11 industry evidence register extension. Industry-specific chain (public-sector, construction-real-estate); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
