# Last-Mile Route to Proof

Admitted Value Stream record (`value-streams:value-stream-last-mile-route-to-proof-967k87`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-last-mile-route-to-proof-967k87` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | logistics-transportation, retail-commerce · industry-specific |
| Record | [`value-streams-value-stream-last-mile-route-to-proof-967k87.yaml`](./value-streams-value-stream-last-mile-route-to-proof-967k87.yaml) — authoritative |

## 2. Definition

> The last-mile stream from route planning through stop execution to complete proof-of-delivery coverage.

## 3. Value proposition and served party

**Outcome:** All stops served with captured proof.

## 4. Stream boundary

**Entry criterion:** A day's route is planned.

**Exit criterion:** All stops are served with proof captured.

**In scope** (from the record's `scope.includes`):

- Route planning
- Stop execution
- Proof capture and exception handling

**Out of scope** (each concern owned by the named neighbour):

- Linehaul (Ship to Consignee)
- Customer notification programs

## 5. Value stages

Last-Mile Route to Proof decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Plan Route

Plan the day's route.

| Aspect | Value |
|---|---|
| Entry criterion | A route is to be planned. |
| Exit criterion | The route is planned. |
| Outcome | A planned route. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-insight-management-ms4n9d`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-sd-build-2pkz5n` |

### Stage 2: Execute Stops

Execute the delivery stops.

| Aspect | Value |
|---|---|
| Entry criterion | The route is planned. |
| Exit criterion | The stops are served. |
| Outcome | Served stops. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zh9m57` |

### Stage 3: Capture Proof

Capture proof and handle exceptions.

| Aspect | Value |
|---|---|
| Entry criterion | The stops are served. |
| Exit criterion | Proof is complete and exceptions handled. |
| Outcome | Complete proof. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-insight-management-ms4n9d`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-customer-management-f3n8wb`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-sd-build-2pkz5n`
- `processes:process-eo-operate-zh9m57`
- `processes:process-pr-operate-bbe384`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Stop completion rate** (stream-level) — Share of planned stops served on the day.

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-072) from the CR-VS-11 industry evidence register extension. Industry-specific chain (logistics-transportation, retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
