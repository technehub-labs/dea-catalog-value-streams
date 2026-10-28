# OpenDEA Value Stream Catalog

> An end-to-end collection of value-creating activities that deliver value to a consumer.

**Layer:** L3 · **Entity:** `VS` (`dea:ValueStream`) · **Building block:** `L3-value-delivery`

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=VS)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)

This repository is the **canonical catalog of Value Stream (`VS`) records** in
the TechNeHub Labs Digital Enterprise Architecture (DEA) ecosystem. It holds
the authoritative, machine-readable definition of each value stream the
enterprise runs — its boundary, its ordered value stages, the capabilities
that enable it, the business processes that realize it, the streams it
connects to, and the measures that tell you it is working.

## Catalog at a glance

| Aspect | Value |
|---|---|
| Entity | `dea:ValueStream` (alias `VS`, layer L3, building block `L3-value-delivery`) |
| Admitted streams | 11 (v1-alpha, record version 1.1.0) |
| Categories | 7 operational · 2 support · 2 governance |
| Value stages | 44 (4 per stream, each with entry/exit criteria and outcome) |
| Cross-catalog links | capabilities → [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities) · processes → [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes) (referential-integrity-checked) |
| Entry schema | [`schemas/entity.schema.json`](./schemas/entity.schema.json) — CR-MET-014 core + CR-VS-07 extensions |
| Catalog index | [`CATALOG.yaml`](./CATALOG.yaml) — machine-generated (CR-CATALOG-STRUCT-06a) |
| CI gates | pointer allocation · entry schema + referential integrity · catalog index conformance |

The canonical entity definition and its relationships live in the
[DEA Metamodel](https://github.com/technehub-labs/dea-metamodel)
(`metamodel/dea-metamodel.yaml`). This repository carries the catalog
pointer ([`metamodel-pointer.yaml`](./metamodel-pointer.yaml), auto-generated
from OpenDEAM — do not edit manually) and the admitted catalog entries.

## What a Value Stream record captures

Each entry is a YAML record under `entities/v1-alpha/`, validated against the
entry schema. Beyond the CR-MET-014 core (definition, outcome, entry/exit
criteria, `aggregated_capability_refs`), the CR-VS-07 shape captures:

| Block | Purpose |
|---|---|
| `value_stream_category` | operational / support / governance / development classification |
| `scope.includes` / `scope.excludes` | explicit in/out-of-scope boundary, each exclusion naming the owning neighbour concept |
| `value_stages[]` | ordered stage decomposition; each stage carries its own entry/exit criteria, outcome, `customer_visible` flag, and referential links to enabling **capabilities** and realizing **processes** |
| `process_refs` | business processes realizing the stream, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes) |
| `upstream_refs` / `downstream_refs` | slug-based cross-stream flow links (stable across sibling hash changes) |
| `metrics[]` | stream-level and per-stage measures (`dea:measured-by` record-side companion) |
| `evidence` / `provenance` | evidence-register sources and rationale; ladder passage (candidate → admitted → active) |

### Referential integrity (CR-VS-07)

Every cross-catalog reference must resolve:

- `capabilities:` refs → [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)
- `processes:` refs → [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)
- `actors:` / `metrics:` refs → their catalogs, when used
- cross-stream slugs → an admitted stream in this catalog

The gate is [`scripts/check_referential_integrity.py`](./scripts/check_referential_integrity.py),
run by the `validate-entries` workflow. Resolution order: local sibling
clone → sibling `CATALOG.yaml` index → vendored snapshot under
[`tools/id-sets/`](./tools/id-sets/) (committed with refresh date, so the
gate is deterministic offline). Unresolved references fail CI.

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

Each value stream's directory README renders the full record — identity,
definition, value proposition and served party, boundary (entry/exit
criteria plus explicit in/out-of-scope), the ordered value stages with
per-stage criteria, capability and process traceability, cross-stream
links, metrics, evidence, and the provenance ladder.

### Cross-stream flow map

The `upstream_refs`/`downstream_refs` links form the enterprise flow map
recorded in the catalog:

```
Plan to Forecast ─→ Plan to Deliver ─→ Order to Cash ─┬→ Contract to Renewal ─→ Issue to Resolve
                       │                               ├→ Return to Credit ─→ Record to Report
Concept to Launch ─→ Order to Cash                     └→ Record to Report
Procure to Pay ─→ Acquire to Retire ─→ Record to Report
Order to Cash / Procure to Pay ─→ Record to Report (transaction recording)
```

## Method: how streams enter and evolve

Admission follows the org-wide catalog research pattern
(CR-CATALOG-STRUCT-01; established in `dea-catalog-business-capabilities`
under CR-DEA-BC-02). All research artifacts live in
[`catalog-research/`](./catalog-research/):

1. **Evidence register** (`evidence-register.yaml`) — public sources
   (BIZBOK, APQC PCF, OMG BACM, TOGAF, SAFe/Lean guidance, enterprise
   process-chain literature), each with observations and the candidates
   they support. Evidence ratings E0..E5.
2. **Candidate universe** (`candidate-universe.yaml`) — candidate value
   streams enumerated from the register; none canonical by default.
3. **Distinctness sweep** (`distinctness-sweep.yaml`) — pairwise
   distinctness against adjacent concepts (processes, capabilities,
   journeys) under the entry/exit/served-party test; merges and boundary
   statements recorded as resolutions.
4. **Admission gate** — a candidate becomes a canonical entry only through
   an admission change request citing the evidence register and closing
   the per-candidate checklist (evidence ≥ E2, distinctness closed,
   content-addressed id, provenance ladder).

Every modification of substance is governed by a numbered change request
in [`change-requests/`](./change-requests/) — from the candidate seed
(CR-VS-01) through the admissions (CR-VS-03/04/05), the schema enrichment
(CR-VS-07), and the conformance hardening (PR #10/#11 follow-ons). See the
[CR index](./change-requests/README.md) for the full ledger and
[CHANGELOG.md](./CHANGELOG.md) for the delivery history.

## CI gates (what a PR must pass)

| Workflow | What it checks |
|---|---|
| `validate-allocation` | [`metamodel-pointer.yaml`](./metamodel-pointer.yaml) against the OpenDEAM allocation (dea-architecture-framework) |
| `validate-entries` | every record (and the fixture) against [`schemas/entity.schema.json`](./schemas/entity.schema.json); cross-catalog referential integrity |
| `catalog-conformance` | [`CATALOG.yaml`](./CATALOG.yaml) matches regenerator output (freshness) and validates against the index schema |

Local equivalents: `scripts/check_referential_integrity.py`,
`scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json`,
`scripts/check_catalog_index.py --schema catalog-index-schema/catalog-index-schema.json`.

## Repository structure

```
dea-catalog-value-streams/
├── metamodel-pointer.yaml   ← entity mapping (auto-generated from OpenDEAM; do not edit)
├── CATALOG.yaml             ← machine-generated catalog index (do not edit; regenerate)
├── README.md                ← this landing document
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE · NOTICE         ← Apache License 2.0
├── schemas/
│   ├── entity.schema.json   ← entry schema (CR-MET-014 core + CR-VS-07 extensions)
│   └── fixtures/
│       └── example-valid.yaml   ← schema self-exercise fixture (not a catalog entry)
├── entities/
│   └── v1-alpha/            ← admitted records (one subtree per value stream)
│       ├── value-stream-<slug>-<hash6>/
│       │   ├── value-streams-value-stream-<slug>-<hash6>.yaml  ← authoritative record
│       │   └── README.md                                     ← comprehensive per-stream documentation
│       └── README.md
├── catalog-research/        ← evidence register, candidate universe, distinctness sweep,
│                             admission register (catalog-wide research method)
├── change-requests/        ← CR-VS-* governance documents
├── schemas/fixtures/        ← (see schemas/ above)
├── classifications/ · contributions/   ← cross-cutting queues (CR-CATALOG-STRUCT-01)
├── scripts/
│   ├── regenerate_catalog.py          ← CATALOG.yaml regenerator (CR-CATALOG-STRUCT-06a)
│   ├── check_catalog_index.py         ← index schema + structural sanity gate
│   ├── check_referential_integrity.py ← cross-catalog reference gate (CR-VS-07)
│   └── hash6.py                       ← org id-system §2.5 suffix algorithm
├── tools/
│   └── id-sets/             ← vendored sibling-catalog id snapshots (offline ref gate)
└── .github/workflows/
    ├── validate-allocation.yml   ← pointer vs. OpenDEAM allocation
    ├── validate-entries.yml      ← entry schema + referential-integrity gate
    └── catalog-conformance.yml   ← CATALOG.yaml freshness + index schema gate
```

Entries follow the org-wide catalog repository standard (CR-CATALOG-STRUCT-01)
and the entity-storage-layout spec
(`dea-metaframework/docs/entity-storage-layout.md`). Record ids are
content-addressed at canonicalization
(`value-streams:value-stream-<slug>-<hash6>`; hash per
[`scripts/hash6.py`](./scripts/hash6.py)) and stable thereafter
(rename-stability contract, PR #5) — substantive enrichment happens in
place under a change request.

## Ecosystem

| Artifact | Where |
|---|---|
| DEA Metamodel (canonical entity definitions) | [dea-metamodel](https://github.com/technehub-labs/dea-metamodel) |
| Root model / OpenDEAM (allocation source) | [dea-architecture-framework](https://github.com/technehub-labs/dea-architecture-framework) |
| Business capabilities (stage enablement) | [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities) |
| Business processes (stage realization) | [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes) |
| Org-wide catalog standards | `dea-metaframework` (CR-CATALOG-STRUCT-01, id-system, entity-storage-layout) |
| Metamodel Explorer | [technehub-labs.github.io/metamodel/?entity=VS](https://technehub-labs.github.io/metamodel/?entity=VS) |

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) — authorship rule, pointer
discipline, branch/PR flow — and the research method above for how new
streams are admitted. Substantive record changes go through a numbered
change request (latest: [`change-requests/CR-VS-07.md`](./change-requests/CR-VS-07.md)).

## License

Apache License 2.0 — see [LICENSE](./LICENSE) and [NOTICE](./NOTICE).
