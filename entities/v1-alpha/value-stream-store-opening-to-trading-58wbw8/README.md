# Store Opening to Trading

Admitted Value Stream record (`value-streams:value-stream-store-opening-to-trading-58wbw8`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-store-opening-to-trading-58wbw8` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | retail-commerce · industry-specific |
| Record | [`value-streams-value-stream-store-opening-to-trading-58wbw8.yaml`](./value-streams-value-stream-store-opening-to-trading-58wbw8.yaml) — authoritative |

## 2. Definition

> The store-lifecycle stream from site decision through fit-out and staffing to first-day trading.

## 3. Value proposition and served party

**Outcome:** A trading store at full operating standard.

## 4. Stream boundary

**Entry criterion:** A site is selected and approved.

**Exit criterion:** The store trades on day one at standard.

**In scope** (from the record's `scope.includes`):

- Fit-out and merchandising
- Staffing and training
- Opening and stabilization

**Out of scope** (each concern owned by the named neighbour):

- Assortment planning
- Real-estate transactions

## 5. Value stages

Store Opening to Trading decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Fit Out

Fit out the site and merchandise it.

| Aspect | Value |
|---|---|
| Entry criterion | A site is approved. |
| Exit criterion | The store is fitted out. |
| Outcome | A fitted store. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-asset-management-judtwr` |
| Realizing processes | `processes:process-eo-build-j9z3q4`, `processes:process-eo-operate-zwzmbd` |

### Stage 2: Staff and Train

Staff and train the store team.

| Aspect | Value |
|---|---|
| Entry criterion | The store is fitted out. |
| Exit criterion | The team is ready. |
| Outcome | A ready team. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-workforce-management-9e8d8s`, `capabilities:capability-workforce-planning-b43rhm` |
| Realizing processes | `processes:process-ao-operate-87q5mk` |

### Stage 3: Open and Stabilize

Open for trading and stabilize to standard.

| Aspect | Value |
|---|---|
| Entry criterion | The team is ready. |
| Exit criterion | The store trades at standard. |
| Outcome | A trading store. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-enterprise-performance-management-5fxren` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-asset-management-judtwr`
- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-workforce-planning-b43rhm`
- `capabilities:capability-enterprise-performance-management-5fxren`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-ao-operate-87q5mk`
- `processes:process-eo-operate-2jnz85`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Opening-to-standard time** (stream-level) — Elapsed weeks from opening to full operating standard.

## 9. Evidence and admission

**Evidence sources:** SRC-013 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-065) from the CR-VS-11 industry evidence register extension. Industry-specific chain (retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
