# Actuarial Data to Price

Admitted Value Stream record (`value-streams:value-stream-actuarial-data-to-price-t5vjcj`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-actuarial-data-to-price-t5vjcj` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | insurance · industry-specific |
| Record | [`value-streams-value-stream-actuarial-data-to-price-t5vjcj.yaml`](./value-streams-value-stream-actuarial-data-to-price-t5vjcj.yaml) — authoritative |

## 2. Definition

> The pricing-governance stream from experience-data compilation through actuarial analysis to filed/adopted rates.

## 3. Value proposition and served party

**Outcome:** Filed or adopted, defensible rates.

## 4. Stream boundary

**Entry criterion:** A pricing review cycle opens.

**Exit criterion:** Rates are filed or adopted.

**In scope** (from the record's `scope.includes`):

- Experience data compilation
- Actuarial analysis
- Rate proposal
- Filing and adoption

**Out of scope** (each concern owned by the named neighbour):

- Claims data operations
- Regulatory reporting

## 5. Value stages

Actuarial Data to Price decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Compile Data

Compile claims and exposure experience data.

| Aspect | Value |
|---|---|
| Entry criterion | A pricing cycle opens. |
| Exit criterion | The dataset is compiled. |
| Outcome | A compiled dataset. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-insight-management-ms4n9d` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

### Stage 2: Analyze

Perform the actuarial analysis.

| Aspect | Value |
|---|---|
| Entry criterion | The dataset is compiled. |
| Exit criterion | The analysis is complete. |
| Outcome | A completed analysis. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-fa-conceive-4uqqvg` |

### Stage 3: Propose Rates

Propose the rate changes.

| Aspect | Value |
|---|---|
| Entry criterion | The analysis is complete. |
| Exit criterion | The proposal is ready. |
| Outcome | A rate proposal. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-conceive-4uqqvg` |

### Stage 4: File and Adopt

File or adopt the rates.

| Aspect | Value |
|---|---|
| Entry criterion | The proposal is ready. |
| Exit criterion | Rates are filed or adopted. |
| Outcome | Adopted rates. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8`, `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-fa-operate-8vqvkk` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-financial-resource-management-cd3c7c`
- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-legal-matter-management-zzbd2u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-operate-ucxpz4`
- `processes:process-fa-conceive-4uqqvg`
- `processes:process-fa-operate-8vqvkk`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Rate-filing cycle time** (stream-level) — Elapsed time from cycle open to adoption.

## 9. Evidence and admission

**Evidence sources:** SRC-009 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-033) from the CR-VS-11 industry evidence register extension. Industry-specific chain (insurance); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
