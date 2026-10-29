# CR-VS-11 — Applicability dimension: industry / organization-type vocabulary and per-record applicability

| Field | Value |
|---|---|
| Status | Executed (with CR-VS-12 population tranche) |
| Target repository | `technehub-labs/dea-catalog-value-streams` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-28 |
| Depends on | CR-VS-07 (merged, PR #9) — enriched record shape |
| Method | Catalog repository standard (CR-CATALOG-STRUCT-01); evidence-register method (register v0.4) |

## 1. Background and problem statement

Value streams can be — and in practice are — specific to organization types,
industries, and sectors. The cross-industry corpus (BIZBOK, APQC PCF;
SRC-001/SRC-002) yields enterprise-generic chains, but every industry carries
canonical chains of its own: admission-to-discharge (healthcare),
quote-to-bind (insurance), meter-to-bill (utilities), trouble-to-restore
(telecom), tender-to-award (construction). The current model could not
express this, with two consequences:

1. **Modeling gap** — two chains that differ only by industry context could
   not be distinct records under the entry/exit/served-party test.
2. **Method gap** — the distinctness sweep is pairwise; at 100+ candidates
   it would explode combinatorially and mostly re-prove that unrelated
   industries are unrelated.

## 2. What this CR does

### 2.1 Controlled vocabulary

`classifications/industry-vocabulary.yaml` (v1.0.0): 15 industry classes
(cross-industry + 14 industries), 5 organization types, each with id, name,
and description; plus the method note that distinctness is scoped by
applicability class. Lives in `classifications/` per the catalog repository
standard's cross-cutting layout.

### 2.2 Schema extension (additive)

`applicability` block on every record (required):

- `industries[]` (minItems 1, enum from the vocabulary) — industries the
  stream is canonical for.
- `organization_types[]` (enum) — for-profit enterprise, public agency,
  nonprofit, regulated entity, internal enterprise function.
- `specificity` — `generic` (cross-industry chain) or `industry-specific`.

### 2.3 Method extension (distinctness scoping)

The two-axis distinctness test (entry / exit / served party) applies
**within an applicability class**. Two candidates whose industry sets do
not overlap are distinct by construction and require no pairwise sweep;
candidates sharing an industry are swept as before. This is what makes a
100-stream population methodologically tractable (CR-VS-12), and it is
recorded in the vocabulary file as `distinctness_scope: applicability_class`.

### 2.4 Evidence register extension (v0.4.0)

New source class `industry-reference-model` and 13 new sources
(SRC-007..SRC-019): healthcare, banking (BIAN/SWIFT-style), insurance
(ACORD-style), telecom (eTOM-style), utilities, financial-crime/regulatory,
retail (GS1-style), public sector, education/hospitality, manufacturing and
logistics (SCOR-style), construction/real-estate, life sciences (ICH/GxP),
technology (SAFe/DORA). All category-level structure only, indirect
retrieval, no gated text — matching the register's existing discipline
(names never copied verbatim into canonical entries).

### 2.5 Backfill

All 11 existing records backfilled as
`industries: [cross-industry]`, `organization_types:
[for-profit-enterprise, internal-enterprise]`, `specificity: generic`
(versions 1.2.0 → 1.3.0, provenance entry appended; ids/dirs/filenames
unchanged per the rename-stability contract).

## 3. Non-goals

- No changes to the metamodel relationship set; applicability is a
  catalog-side classification, expressible today without upstream moves.
- No geo/regional dimension (can be added later under the same pattern).
- CR-VS-09 (actors) and the metrics-catalog pipeline are unaffected.

## 4. Verification

- Schema validation: all 11 records + fixture pass with the new required
  `applicability` block.
- Vocabulary file parses; every enum value in the schema matches a
  vocabulary id (scripted check).
- Referential-integrity gate unaffected (no new namespaces).
- CATALOG.yaml regenerated; conformance green.
