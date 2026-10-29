# v1-alpha Catalog Entries

This directory will contain the authoritative `v1-alpha` Value Stream catalog
entries for the TechNeHub Labs Digital Enterprise Architecture (DEA) ecosystem.

Value streams are stored in a **flat layout** under this directory (one subtree
per record), per the org-wide entity-storage-layout spec
(`dea-metaframework/docs/entity-storage-layout.md`). Each record is a
`value-stream-<slug>-<hash6>` subtree containing the record YAML:

```
v1-alpha/
├── value-stream-<slug>-<hash6>/                      # admitted record subtree
│   └── value-streams-value-stream-<slug>-<hash6>.yaml
├── candidates-value-stream-<slug>-<hash6>/          # candidate subtree (not yet admitted)
│   └── value-streams-candidate-<slug>-<hash6>.yaml
└── README.md
```

Subdirectory names follow `<level>-<slug>-<hash6>`. The 6-character hash is
content-derived (first 4 bytes of the record file's SHA-256, base-31 over the
alphabet `a-z` minus `i`, `l`, `o` plus digits `2-9`). See
`dea-metaframework/docs/id-system.md` section 2.5.

## Entry anatomy

Per the DEA Metamodel, each record is a `dea:ValueStream` (type `ValueStream`,
layer L3, building block `L3-value-delivery`). Records validate against
[`schemas/entity.schema.json`](../../schemas/entity.schema.json), which mirrors
the metamodel's `dea:ValueStream` schema (CR-MET-014) plus catalog extensions
(evidence, provenance ladder).

### Canonical id forms

| Level | id form |
| :--- | :--- |
| Admitted value stream | `value-streams:value-stream-<slug>-<hash6>` |
| Candidate | `value-streams:candidate-<slug>-<hash6>` |

Each record file's id is content-addressed: changing the file's contents
(without renaming the file) changes its hash. This is what makes the catalog
content-addressed rather than directory-addressed.

## Folder shape (CR-VS-13)

Each subtree is both human- and machine-readable:

```
value-stream-<slug>-<hash6>/
├── value-streams-value-stream-<slug>-<hash6>.yaml   ← authoritative record
├── README.md                                        ← generated: YAML front matter,
│                                                      mermaid stage flow, full rendering
└── research/
    ├── README.md        ← folder contract (CR-CATALOG-STRUCT-01 §5)
    └── evidence.md      ← per-entity evidence notes from the register
```

The README's front matter is machine-extractable metadata (id, stages,
capability/process/metric ids, links). Regenerate everything with
`scripts/generate_entity_docs.py`; never hand-edit — the generator
overwrites.

## Status

11 admitted value streams (v1.1.0, CR-VS-07 enriched shape): each record
carries its ordered value stages with per-stage capability and process
references, an explicit scope boundary, cross-stream links, and metrics.
Cross-catalog references are referential-integrity-checked
(`scripts/check_referential_integrity.py`, CR-VS-07); admission of new
entries continues to follow the catalog-research method (candidate
universe, distinctness sweep, evidence register, admission gate) per the
org-wide catalog repository standard (CR-CATALOG-STRUCT-01) and the pattern
established in `dea-catalog-business-capabilities`.

Each subtree's README.md renders the full record (comprehensive
documentation per CR-VS-07/13): front-mattered metadata, mermaid stage
flow, identity, definition, value proposition, boundary, value stages,
capability/process traceability, cross-stream links, measurement,
evidence (with per-entity research notes), and the provenance ladder.
