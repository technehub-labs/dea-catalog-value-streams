# Developer Onboard to First Commit

Admitted Value Stream record (`value-streams:value-stream-developer-onboard-to-first-commit-zeszzp`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-developer-onboard-to-first-commit-zeszzp` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | technology · industry-specific |
| Record | [`value-streams-value-stream-developer-onboard-to-first-commit-zeszzp.yaml`](./value-streams-value-stream-developer-onboard-to-first-commit-zeszzp.yaml) — authoritative |

## 2. Definition

> The developer-experience stream from onboarding start through environment setup to a merged first commit.

## 3. Value proposition and served party

**Outcome:** A productive new developer with a merged first contribution.

## 4. Stream boundary

**Entry criterion:** A developer joins.

**Exit criterion:** The first contribution is merged.

**In scope** (from the record's `scope.includes`):

- Onboarding and access
- Environment setup
- First contribution

**Out of scope** (each concern owned by the named neighbour):

- Hire to Retire (employment lifecycle)
- Platform provisioning

## 5. Value stages

Developer Onboard to First Commit decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Onboard and Grant Access

Onboard the developer and grant access.

| Aspect | Value |
|---|---|
| Entry criterion | A developer joins. |
| Exit criterion | Access is granted. |
| Outcome | An equipped developer. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c`, `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-ao-operate-87q5mk` |

### Stage 2: Set Up Environment

Set up the development environment.

| Aspect | Value |
|---|---|
| Entry criterion | Access is granted. |
| Exit criterion | The environment is ready. |
| Outcome | A ready environment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### Stage 3: Merge First Contribution

Support the first merged contribution.

| Aspect | Value |
|---|---|
| Entry criterion | The environment is ready. |
| Exit criterion | The first commit is merged. |
| Outcome | A productive developer. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-operations-management-pm3w8k`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ao-operate-87q5mk`
- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-44jsrp`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-hire-to-retire` — The employment lifecycle governs the joining itself.

**Downstream streams:** none recorded.

## 8. Measurement

- **Onboarding time to value** (stage: Merge First Contribution) — Elapsed time from joining to first merged contribution. → [`dea:metric-onboarding-time-to-value`](https://github.com/technehub-labs/dea-catalog-metrics)

## 9. Evidence and admission

**Evidence sources:** SRC-019 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-113) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
