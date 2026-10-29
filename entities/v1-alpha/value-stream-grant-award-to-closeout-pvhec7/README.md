# Grant Award to Closeout

Admitted Value Stream record (`value-streams:value-stream-grant-award-to-closeout-pvhec7`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-grant-award-to-closeout-pvhec7` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | public-sector · industry-specific |
| Record | [`value-streams-value-stream-grant-award-to-closeout-pvhec7.yaml`](./value-streams-value-stream-grant-award-to-closeout-pvhec7.yaml) — authoritative |

## 2. Definition

> The grants stream from award through disbursement and monitoring to closeout.

## 3. Value proposition and served party

**Outcome:** A closed-out grant with settled funds and reported outcomes.

## 4. Stream boundary

**Entry criterion:** A grant is awarded.

**Exit criterion:** The grant is closed out with settled funds.

**In scope** (from the record's `scope.includes`):

- Award and agreement
- Disbursement
- Monitoring and reporting
- Closeout

**Out of scope** (each concern owned by the named neighbour):

- Application assessment (Apply to Decide)
- Audit programs

## 5. Value stages

Grant Award to Closeout decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Award

Award the grant and execute the agreement.

| Aspect | Value |
|---|---|
| Entry criterion | A grant is awarded. |
| Exit criterion | The agreement is executed. |
| Outcome | An executed agreement. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-partner-management-cp3vdb` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 2: Disburse

Disburse funds per schedule.

| Aspect | Value |
|---|---|
| Entry criterion | The agreement is executed. |
| Exit criterion | Funds are disbursed. |
| Outcome | Disbursed funds. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk` |
| Realizing processes | `processes:process-fa-operate-wkqaqp` |

### Stage 3: Monitor

Monitor use of funds and milestone reporting.

| Aspect | Value |
|---|---|
| Entry criterion | Funds are disbursed. |
| Exit criterion | Reporting is complete. |
| Outcome | Complete reporting. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-enterprise-performance-management-5fxren`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-sd-operate-ucxpz4` |

### Stage 4: Close Out

Close out the grant with settled funds.

| Aspect | Value |
|---|---|
| Entry criterion | Reporting is complete. |
| Exit criterion | The grant is closed out. |
| Outcome | A closed grant. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-enterprise-governance-uas48u` |
| Realizing processes | `processes:process-fa-operate-4xn4d6` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-financial-stewardship-c7xtfk`
- `capabilities:capability-enterprise-performance-management-5fxren`
- `capabilities:capability-enterprise-governance-uas48u`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-build-mctdgc`
- `processes:process-fa-operate-wkqaqp`
- `processes:process-sd-operate-ucxpz4`
- `processes:process-fa-operate-4xn4d6`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Grant closeout timeliness** (stream-level) — Share of grants closed within the closeout window.

## 9. Evidence and admission

**Evidence sources:** SRC-014 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-076) from the CR-VS-11 industry evidence register extension. Industry-specific chain (public-sector); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
