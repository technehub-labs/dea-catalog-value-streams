# Apply to Connect

Admitted Value Stream record (`value-streams:value-stream-apply-to-connect-y64n29`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-apply-to-connect-y64n29` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | utilities-energy · industry-specific |
| Record | [`value-streams-value-stream-apply-to-connect-y64n29.yaml`](./value-streams-value-stream-apply-to-connect-y64n29.yaml) — authoritative |

## 2. Definition

> The connection stream from connection application through design, works, and energization.

## 3. Value proposition and served party

**Outcome:** An energized connection for the applicant.

## 4. Stream boundary

**Entry criterion:** A connection application is received.

**Exit criterion:** The connection is energized.

**In scope** (from the record's `scope.includes`):

- Application and feasibility
- Design and quotation
- Works execution
- Energization

**Out of scope** (each concern owned by the named neighbour):

- Metering (Meter to Bill)
- Network capacity planning

## 5. Value stages

Apply to Connect decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Assess Application

Assess the application and connection feasibility.

| Aspect | Value |
|---|---|
| Entry criterion | An application is received. |
| Exit criterion | Feasibility is confirmed. |
| Outcome | A feasible application. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Design and Quote

Design the connection and quote.

| Aspect | Value |
|---|---|
| Entry criterion | Feasibility is confirmed. |
| Exit criterion | The quote is accepted. |
| Outcome | An accepted quote. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-eo-design-6j5mxp` |

### Stage 3: Execute Works

Execute the connection works.

| Aspect | Value |
|---|---|
| Entry criterion | The quote is accepted. |
| Exit criterion | The works are complete. |
| Outcome | Completed works. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-build-j9z3q4`, `processes:process-eo-operate-xud3hs` |

### Stage 4: Energize

Energize the connection and activate the account.

| Aspect | Value |
|---|---|
| Entry criterion | The works are complete. |
| Exit criterion | The connection is energized. |
| Outcome | An energized connection. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-design-6j5mxp`
- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-2jnz85`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-meter-to-bill` — Energized connections begin metered consumption.

## 8. Measurement

- **Connection cycle time** (stream-level) — Elapsed days from application to energization.

## 9. Evidence and admission

**Evidence sources:** SRC-011 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-044) from the CR-VS-11 industry evidence register extension. Industry-specific chain (utilities-energy); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
