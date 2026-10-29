# Request to Disclose

Admitted Value Stream record (`value-streams:value-stream-request-to-disclose-78w8jb`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-request-to-disclose-78w8jb` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | public-sector · industry-specific |
| Record | [`value-streams-value-stream-request-to-disclose-78w8jb.yaml`](./value-streams-value-stream-request-to-disclose-78w8jb.yaml) — authoritative |

## 2. Definition

> The information-request stream from records request through review and redaction to disclosure.

## 3. Value proposition and served party

**Outcome:** A lawful disclosure to the requester within the statutory deadline.

## 4. Stream boundary

**Entry criterion:** A records/information request is received.

**Exit criterion:** The disclosure is made within deadline.

**In scope** (from the record's `scope.includes`):

- Request registration
- Records search and review
- Redaction and disclosure

**Out of scope** (each concern owned by the named neighbour):

- Case handling (Intake to Resolution)
- Archives governance

## 5. Value stages

Request to Disclose decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Register Request

Register the request and clarify scope.

| Aspect | Value |
|---|---|
| Entry criterion | A request is received. |
| Exit criterion | The request is registered. |
| Outcome | A registered request. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Search and Review

Search records and review for exemptions.

| Aspect | Value |
|---|---|
| Entry criterion | The request is registered. |
| Exit criterion | The review is complete. |
| Outcome | A completed review. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Disclose

Redact as required and disclose.

| Aspect | Value |
|---|---|
| Entry criterion | The review is complete. |
| Exit criterion | The disclosure is made. |
| Outcome | A made disclosure. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-ge-operate-zwaes5`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Statutory deadline compliance** (stream-level) — Share of disclosures made within deadline.

## 9. Evidence and admission

**Evidence sources:** SRC-014 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-075) from the CR-VS-11 industry evidence register extension. Industry-specific chain (public-sector); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
