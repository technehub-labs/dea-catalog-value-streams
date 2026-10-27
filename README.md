# Value Stream

> An end-to-end collection of value-creating activities that deliver value to a consumer.

**Layer:** L3 · **Entity:** `VS` (`dea:ValueStream`) · **Building block:** `L3-value-delivery`

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=VS)

## Status

This catalog carries **11 admitted value streams** (v1-alpha). Each record
validates against [`schemas/entity.schema.json`](./schemas/entity.schema.json)
and its cross-catalog references are referential-integrity-checked (CR-VS-07).

## Entity Definition

| Field | Value |
|-------|-------|
| Entity ID | `dea:ValueStream` |
| Class Alias | `VS` |
| Layer | L3 |
| Building Block | `L3-value-delivery` |
| Catalog repo | `dea-catalog-value-streams` (this repository) |

The canonical entity definition and its relationships live in the
[DEA Metamodel](https://github.com/technehub-labs/dea-metamodel)
(`metamodel/dea-metamodel.yaml`). This repository carries the catalog
pointer and the admitted catalog entries.

## Relationships (per the metamodel)

| Relationship | Role of VS | Partner entities | Cardinality (source:target) |
|---|---|---|---|
| `dea:aggregates` | source | BusinessCapability, BusinessObject, DataEntity, EcosystemActor | `0..* : 0..*` |
| `dea:flows-to` | source | Actor, BusinessCapability, BusinessObject, JourneyTouchpoint, SystemFunction | `0..* : 0..*` |
| `dea:serves` | target | ApplicationComponent, BusinessProcess, BusinessService, EcosystemPlatform, JourneyTouchpoint | `0..* : 0..*` |
| `dea:measured-by` | source | PerformanceMetric | `0..* : 0..*` |
| `dea:measures-subject` | target | Measurement | `1 : 1` |

## Entry schema (CR-VS-07 shape)

Each record captures, beyond the CR-MET-014 core (definition, outcome,
entry/exit criteria, `aggregated_capability_refs`):

| Block | Purpose |
|---|---|
| `value_stream_category` | operational / support / governance / development classification |
| `scope.includes` / `scope.excludes` | explicit in/out-of-scope boundary, each exclusion naming the owning neighbour |
| `value_stages[]` | ordered stage decomposition; each stage carries its own entry/exit criteria, outcome, customer-visibility, and referential links to enabling **capabilities** and realizing **processes** |
| `process_refs` | business processes realizing the stream, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes) |
| `upstream_refs` / `downstream_refs` | slug-based cross-stream flow links (stable across sibling hash changes) |
| `metrics[]` | stream-level and per-stage measures (`dea:measured-by` record-side companion) |

**Referential integrity (CR-VS-07):** every `capabilities:` ref resolves in
[dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities),
every `processes:` ref in [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes),
and every cross-stream slug against this catalog. The gate is
[`scripts/check_referential_integrity.py`](./scripts/check_referential_integrity.py),
run by the `validate-entries` workflow, with a vendored offline snapshot under
`tools/id-sets/`.

## Catalogued value streams

| Value stream | Category | Outcome | Stages | Record |
|---|---|---|---|---|
| [Order to Cash](./entities/v1-alpha/value-stream-order-to-cash-sc8gbu/README.md) | operational | Customer receives the fulfilled order and the enterprise recognizes payment against it. | Generate Demand → Capture Order → Fulfill Order → Invoice and Settle | [`value-stream-order-to-cash-sc8gbu`](./entities/v1-alpha/value-stream-order-to-cash-sc8gbu/) |
| [Procure to Pay](./entities/v1-alpha/value-stream-procure-to-pay-utma5c/README.md) | operational | The internal need is met and the supplier obligation is settled. | Requisition Need → Source Supplier → Order and Receive → Settle Supplier | [`value-stream-procure-to-pay-utma5c`](./entities/v1-alpha/value-stream-procure-to-pay-utma5c/) |
| [Issue to Resolve](./entities/v1-alpha/value-stream-issue-to-resolve-crmbay/README.md) | operational | The customer's issue is resolved and trust is restored. | Intake Issue → Diagnose → Correct → Confirm Resolution | [`value-stream-issue-to-resolve-crmbay`](./entities/v1-alpha/value-stream-issue-to-resolve-crmbay/) |
| [Concept to Launch](./entities/v1-alpha/value-stream-concept-to-launch-nhvatv/README.md) | operational | A launched offering delivering value to its intended market. | Approve Concept → Develop Offering → Prepare Launch → Launch | [`value-stream-concept-to-launch-nhvatv`](./entities/v1-alpha/value-stream-concept-to-launch-nhvatv/) |
| [Plan to Deliver](./entities/v1-alpha/value-stream-plan-to-deliver-smmwpx/README.md) | operational | Delivered supply against planned demand. | Plan Demand → Schedule Production → Produce → Deliver | [`value-stream-plan-to-deliver-smmwpx`](./entities/v1-alpha/value-stream-plan-to-deliver-smmwpx/) |
| [Return to Credit](./entities/v1-alpha/value-stream-return-to-credit-qan2dn/README.md) | operational | A fairly settled return with the customer relationship preserved. | Initiate Return → Receive Reverse Logistics → Inspect and Dispose → Settle Credit | [`value-stream-return-to-credit-qan2dn`](./entities/v1-alpha/value-stream-return-to-credit-qan2dn/) |
| [Contract to Renewal](./entities/v1-alpha/value-stream-contract-to-renewal-5x3r4x/README.md) | operational | A continuous, explicitly settled customer relationship. | Execute Contract → Serve Relationship → Prepare Renewal → Settle Renewal | [`value-stream-contract-to-renewal-5x3r4x`](./entities/v1-alpha/value-stream-contract-to-renewal-5x3r4x/) |
| [Hire to Retire](./entities/v1-alpha/value-stream-hire-to-retire-n6szcc/README.md) | support | A staffed, productive workforce with settled employment obligations. | Requisition Workforce → Hire → Develop and Administer → Separate | [`value-stream-hire-to-retire-n6szcc`](./entities/v1-alpha/value-stream-hire-to-retire-n6szcc/) |
| [Acquire to Retire](./entities/v1-alpha/value-stream-acquire-to-retire-g5x89g/README.md) | support | Assets productively used across their lifecycle and cleanly retired. | Identify Asset Need → Acquire Asset → Operate and Maintain → Retire Asset | [`value-stream-acquire-to-retire-g5x89g`](./entities/v1-alpha/value-stream-acquire-to-retire-g5x89g/) |
| [Plan to Forecast](./entities/v1-alpha/value-stream-plan-to-forecast-89vb4q/README.md) | governance | A ratified plan guiding enterprise resource allocation. | Open Planning Cycle → Form Plan → Negotiate Commitment → Ratify Forecast | [`value-stream-plan-to-forecast-89vb4q`](./entities/v1-alpha/value-stream-plan-to-forecast-89vb4q/) |
| [Record to Report](./entities/v1-alpha/value-stream-record-to-report-zw9z2r/README.md) | governance | Attested financial visibility for stakeholders. | Record Transactions → Close Period → Report → Disclose | [`value-stream-record-to-report-zw9z2r`](./entities/v1-alpha/value-stream-record-to-report-zw9z2r/) |

Each value stream's directory README renders the full record: identity,
definition, outcome and served party, boundary (entry/exit criteria plus
explicit in/out-of-scope), the ordered value stages with their per-stage
criteria, capability and process traceability, cross-stream links, metrics,
evidence, and the provenance ladder.

## Repository Structure

```
dea-catalog-value-streams/
├── metamodel-pointer.yaml   ← entity mapping (do not edit manually)
├── CATALOG.yaml             ← machine-generated catalog index (do not edit manually)
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── schemas/
│   ├── entity.schema.json   ← entry schema (CR-MET-014 core + CR-VS-07 extensions)
│   └── fixtures/
│       └── example-valid.yaml
├── entities/
│   └── v1-alpha/            ← admitted records (one subtree per value stream)
│       ├── value-stream-<slug>-<hash6>/
│       │   ├── value-streams-value-stream-<slug>-<hash6>.yaml  ← authoritative record
│       │   └── README.md                                     ← comprehensive per-stream documentation
│       └── README.md
├── scripts/
│   ├── regenerate_catalog.py          ← CATALOG.yaml regenerator (CR-CATALOG-STRUCT-06a)
│   ├── check_catalog_index.py         ← index schema gate
│   ├── check_referential_integrity.py ← cross-catalog ref gate (CR-VS-07)
│   └── hash6.py                       ← org id-system §2.5 suffix algorithm
├── tools/
│   └── id-sets/              ← vendored sibling-catalog id snapshots (offline ref gate)
└── .github/
    └── workflows/
        ├── validate-allocation.yml   ← validates pointer against OpenDEAM allocation
        ├── validate-entries.yml      ← schema validation + referential-integrity gate
        └── catalog-conformance.yml   ← CATALOG.yaml freshness + index schema gate
```

Entries follow the org-wide catalog repository standard (CR-CATALOG-STRUCT-01)
and the entity-storage-layout spec
(`dea-metaframework/docs/entity-storage-layout.md`).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and the
[DEA Metamodel](https://github.com/technehub-labs/dea-metamodel) for guidance.
Record ids are content-addressed at canonicalization and stable thereafter
(rename-stability contract, PR #5); substantive enrichment happens in place
under a change request (see `change-requests/CR-VS-07.md`).
