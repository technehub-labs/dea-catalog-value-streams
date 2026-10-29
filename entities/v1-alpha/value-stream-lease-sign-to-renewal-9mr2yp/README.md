# Lease Sign to Renewal

Admitted Value Stream record (`value-streams:value-stream-lease-sign-to-renewal-9mr2yp`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-lease-sign-to-renewal-9mr2yp` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | construction-real-estate · industry-specific |
| Record | [`value-streams-value-stream-lease-sign-to-renewal-9mr2yp.yaml`](./value-streams-value-stream-lease-sign-to-renewal-9mr2yp.yaml) — authoritative |

## 2. Definition

> The property stream from lease execution through occupancy service to lease renewal or exit.

## 3. Value proposition and served party

**Outcome:** A settled renewal or exit at lease end.

## 4. Stream boundary

**Entry criterion:** A lease is executed.

**Exit criterion:** The renewal or exit is settled.

**In scope** (from the record's `scope.includes`):

- Lease execution and onboarding
- Occupancy service and rent collection
- Renewal decision and settlement

**Out of scope** (each concern owned by the named neighbour):

- Sales transactions (List to Close)
- Facilities management

## 5. Value stages

Lease Sign to Renewal decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Execute Lease

Execute the lease and onboard the tenant.

| Aspect | Value |
|---|---|
| Entry criterion | A lease is executed. |
| Exit criterion | The tenant is onboarded. |
| Outcome | An onboarded tenant. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 2: Serve Occupancy

Serve the tenancy and collect rent.

| Aspect | Value |
|---|---|
| Entry criterion | The tenancy starts. |
| Exit criterion | The tenancy is served and rent collected. |
| Outcome | A served tenancy. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-eo-operate-2jnz85`, `processes:process-fa-operate-sdppmp` |

### Stage 3: Renew or Exit

Settle the renewal or exit.

| Aspect | Value |
|---|---|
| Entry criterion | The lease approaches end. |
| Exit criterion | The renewal or exit is settled. |
| Outcome | A settled lease end. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-legal-matter-management-zzbd2u`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-improve-t6uvan` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-build-mctdgc`
- `processes:process-eo-operate-2jnz85`
- `processes:process-fa-operate-sdppmp`
- `processes:process-pr-improve-t6uvan`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Lease renewal rate** (stream-level) — Share of expiring leases renewed.

## 9. Evidence and admission

**Evidence sources:** SRC-017 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-095) from the CR-VS-11 industry evidence register extension. Industry-specific chain (construction-real-estate); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
