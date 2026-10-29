# Sustainability Data to Disclosure

Admitted Value Stream record (`value-streams:value-stream-sustainability-data-to-disclosure-4mmwks`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-sustainability-data-to-disclosure-4mmwks` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | manufacturing, utilities-energy · industry-specific |
| Record | [`value-streams-value-stream-sustainability-data-to-disclosure-4mmwks.yaml`](./value-streams-value-stream-sustainability-data-to-disclosure-4mmwks.yaml) — authoritative |

## 2. Definition

> The ESG stream from sustainability data capture through assurance to disclosure.

## 3. Value proposition and served party

**Outcome:** An assured sustainability disclosure.

## 4. Stream boundary

**Entry criterion:** A reporting cycle opens.

**Exit criterion:** The disclosure is published with assurance.

**In scope** (from the record's `scope.includes`):

- Data capture and aggregation
- Assurance
- Disclosure

**Out of scope** (each concern owned by the named neighbour):

- Financial reporting (Record to Report)
- Regulatory filings

## 5. Value stages

Sustainability Data to Disclosure decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Capture Data

Capture and aggregate sustainability data.

| Aspect | Value |
|---|---|
| Entry criterion | A cycle opens. |
| Exit criterion | The dataset is complete. |
| Outcome | A complete dataset. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### Stage 2: Assure

Assure the data and disclosures.

| Aspect | Value |
|---|---|
| Entry criterion | The dataset is complete. |
| Exit criterion | Assurance is complete. |
| Outcome | Assured data. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-governance-uas48u`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-zwaes5` |

### Stage 3: Disclose

Publish the disclosure.

| Aspect | Value |
|---|---|
| Entry criterion | Assurance is complete. |
| Exit criterion | The disclosure is published. |
| Outcome | A published disclosure. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-fa-operate-ycba3k` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-enterprise-governance-uas48u`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-fa-operate-g9zpnq`
- `processes:process-ge-operate-zwaes5`
- `processes:process-fa-operate-ycba3k`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Disclosure data completeness** (stream-level) — Share of required data points with assured values.

## 9. Evidence and admission

**Evidence sources:** SRC-016, SRC-011 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-057) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing, utilities-energy); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
