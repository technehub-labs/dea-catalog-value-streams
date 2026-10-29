---
documentation_generated_from: value-streams-value-stream-developer-onboard-to-first-commit-zeszzp.yaml
id: value-streams:value-stream-developer-onboard-to-first-commit-zeszzp
name: Developer Onboard to First Commit
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: support
industries:
- technology
specificity: industry-specific
entry_criterion: A developer joins.
exit_criterion: The first contribution is merged.
outcome: A productive new developer with a merged first contribution.
stages:
- Onboard and Grant Access
- Set Up Environment
- Merge First Contribution
capabilities:
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-security-management-wmzc7c
- capabilities:capability-technology-enablement-y6nkws
- capabilities:capability-workforce-management-9e8d8s
processes:
- processes:process-ao-operate-87q5mk
- processes:process-eo-build-j9z3q4
- processes:process-eo-operate-44jsrp
metrics:
- Onboarding time to value
upstream:
- value-stream-hire-to-retire
downstream: []
evidence_sources:
- SRC-019
---

# Developer Onboard to First Commit

`value-streams:value-stream-developer-onboard-to-first-commit-zeszzp` · **support** · technology · industry-specific

> The developer-experience stream from onboarding start through environment setup to a merged first commit.

**Outcome:** A productive new developer with a merged first contribution.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-developer-onboard-to-first-commit-zeszzp.yaml`](./value-streams-value-stream-developer-onboard-to-first-commit-zeszzp.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Onboard and Grant Access"]
  S2["2. Set Up Environment"]
  S3["3. Merge First Contribution"]
  S1 --> S2
  S2 --> S3
  TRIGGER(("⏺ Entry")) --> S1
  S3 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Onboard and Grant Access** | A developer joins. | Access is granted. | 2 | 1 | no |
| 2 | **Set Up Environment** | Access is granted. | The environment is ready. | 1 | 1 | no |
| 3 | **Merge First Contribution** | The environment is ready. | The first commit is merged. | 1 | 1 | no |

### 1. Onboard and Grant Access

Onboard the developer and grant access.

| Aspect | Value |
|---|---|
| Entry criterion | A developer joins. |
| Exit criterion | Access is granted. |
| Outcome | An equipped developer. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c` · `capabilities:capability-workforce-management-9e8d8s` |
| Realizing processes | `processes:process-ao-operate-87q5mk` |

### 2. Set Up Environment

Set up the development environment.

| Aspect | Value |
|---|---|
| Entry criterion | Access is granted. |
| Exit criterion | The environment is ready. |
| Outcome | A ready environment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-enablement-y6nkws` |
| Realizing processes | `processes:process-eo-build-j9z3q4` |

### 3. Merge First Contribution

Support the first merged contribution.

| Aspect | Value |
|---|---|
| Entry criterion | The environment is ready. |
| Exit criterion | The first commit is merged. |
| Outcome | A productive developer. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

## Scope boundary

**Entry:** A developer joins.

**Exit:** The first contribution is merged.

**In scope**

- Onboarding and access
- Environment setup
- First contribution

**Out of scope** (owned by the named neighbour)

- Hire to Retire (employment lifecycle)
- Platform provisioning

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-workforce-management-9e8d8s`
- `capabilities:capability-technology-enablement-y6nkws`
- `capabilities:capability-operations-management-pm3w8k`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ao-operate-87q5mk`
- `processes:process-eo-build-j9z3q4`
- `processes:process-eo-operate-44jsrp`

## Cross-stream links

**Upstream** (their exit feeds this stream's entry):

- [hire to retire](../value-stream-hire-to-retire-n6szcc/README.md) — The employment lifecycle governs the joining itself.

**Downstream:** none recorded.

## Measurement

- **Onboarding time to value** (stage: Merge First Contribution) — Elapsed time from joining to first merged contribution. → [`dea:metric-onboarding-time-to-value`](https://github.com/technehub-labs/dea-catalog-metrics)

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-019 | industry-reference-model | Technology / SaaS product chains (public structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-113) from the CR-VS-11 industry evidence register extension. Industry-specific chain (technology); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
