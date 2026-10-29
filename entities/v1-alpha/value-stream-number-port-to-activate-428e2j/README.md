# Number Port to Activate

Admitted Value Stream record (`value-streams:value-stream-number-port-to-activate-428e2j`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-number-port-to-activate-428e2j` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | telecommunications · industry-specific |
| Record | [`value-streams-value-stream-number-port-to-activate-428e2j.yaml`](./value-streams-value-stream-number-port-to-activate-428e2j.yaml) — authoritative |

## 2. Definition

> The porting stream from a porting request through validation and coordination to an activated ported number.

## 3. Value proposition and served party

**Outcome:** A ported number active on the recipient network.

## 4. Stream boundary

**Entry criterion:** A customer requests to port a number.

**Exit criterion:** The number is ported and activated.

**In scope** (from the record's `scope.includes`):

- Porting request and validation
- Donor coordination
- Cutover and activation

**Out of scope** (each concern owned by the named neighbour):

- New-service provisioning (Order to Activation)
- Number allocation governance

## 5. Value stages

Number Port to Activate decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Validate Request

Validate the porting request and eligibility.

| Aspect | Value |
|---|---|
| Entry criterion | A port request is received. |
| Exit criterion | The request is validated. |
| Outcome | A validated request. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-regulation-management-gya4d8` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 2: Coordinate Cutover

Coordinate the cutover window with the donor.

| Aspect | Value |
|---|---|
| Entry criterion | The request is validated. |
| Exit criterion | The cutover is scheduled. |
| Outcome | A scheduled cutover. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-partner-management-cp3vdb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 3: Cut Over and Activate

Execute the cutover and activate the ported number.

| Aspect | Value |
|---|---|
| Entry criterion | The cutover is scheduled. |
| Exit criterion | The number is active. |
| Outcome | An active ported number. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-technology-enablement-y6nkws`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-operate-bbe384`
- `processes:process-eo-operate-2jnz85`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Porting completion time** (stream-level) — Elapsed time from request to activation.

## 9. Evidence and admission

**Evidence sources:** SRC-010 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-041) from the CR-VS-11 industry evidence register extension. Industry-specific chain (telecommunications); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
