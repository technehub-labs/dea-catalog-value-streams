# Value Stream

> An end-to-end collection of value-creating activities that deliver value to a consumer.

**Layer:** L3 · **Entity:** `VS` (`dea:ValueStream`) · **Building block:** `L3-value-delivery`

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=VS)

## Status

This is a **scaffold** repository — created during the Phase 1 metamodel rollout.
Content population is planned for a subsequent phase.

## Entity Definition

| Field | Value |
|-------|-------|
| Entity ID | `dea:ValueStream` |
| Class Alias | `VS` |
| Layer | L3 |
| Building Block | `L3-value-delivery` |
| Lifecycle | planned (normative in the metamodel; artifacts not yet generated) |
| Catalog repo | `dea-catalog-value-streams` (this repository) |

The canonical entity definition and its relationships live in the
[DEA Metamodel](https://github.com/technehub-labs/dea-metamodel)
(`metamodel/dea-metamodel.yaml`). This repository carries only the
catalog pointer and, in a later phase, the catalog entries.

## Relationships (per the metamodel)

| Relationship | Role of VS | Partner entities | Cardinality (source:target) |
|---|---|---|---|
| `dea:aggregates` | source | BusinessCapability, BusinessObject, DataEntity, EcosystemActor | `0..* : 0..*` |
| `dea:flows-to` | source | Actor, BusinessCapability, BusinessObject, JourneyTouchpoint, SystemFunction | `0..* : 0..*` |
| `dea:serves` | target | ApplicationComponent, BusinessProcess, BusinessService, EcosystemPlatform, JourneyTouchpoint | `0..* : 0..*` |
| `dea:measured-by` | source | PerformanceMetric | `0..* : 0..*` |
| `dea:measures-subject` | target | Measurement | `1 : 1` |

## Repository Structure

```
dea-catalog-value-streams/
├── metamodel-pointer.yaml   ← entity mapping (do not edit manually)
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── schemas/
│   ├── entity.schema.json   ← entry schema (mirrors metamodel dea:ValueStream, CR-MET-014)
│   └── fixtures/
│       └── example-valid.yaml
├── entities/
│   └── v1-alpha/            ← catalog entries go here (admitted via admission PRs)
│       └── README.md
└── .github/
    └── workflows/
        ├── validate-allocation.yml   ← validates pointer against OpenDEAM allocation
        └── validate-entries.yml      ← validates entries + fixture against the entry schema
```

Entries follow the org-wide catalog repository standard (CR-CATALOG-STRUCT-01)
and the entity-storage-layout spec
(`dea-metaframework/docs/entity-storage-layout.md`).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) and the
[DEA Metamodel](https://github.com/technehub-labs/dea-metamodel) for guidance.
