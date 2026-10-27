# CR-VS-06 — Catalog Index Conformance: CATALOG.yaml, Vendored Regenerator, and Gate Workflow

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-value-streams` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-27 |
| Depends on | CR-VS-01..05 (PRs #3–#7); dea-metaframework v2.6.0 toolchain |
| Method | Catalog repository standard (CR-CATALOG-STRUCT-01; regenerator/gate per CR-CATALOG-STRUCT-06a) |

## 1. Background and problem statement

The catalog repository standard (CR-CATALOG-STRUCT-01) requires every catalog repo to carry a machine-generated `CATALOG.yaml` index, kept fresh by a regenerator gate in CI. The sibling catalogs (e.g. `dea-catalog-business-capabilities`, CR-CATALOG-STRUCT-03a) vendor the metaframework toolchain (`tools/regenerate_catalog.py`, `tools/check_catalog_index.py`, `tools/catalog-index-schema.json`) and run a `catalog-conformance` workflow. This catalog had none of these; with 11 canonical records admitted through CR-VS-03..05, the index requirement is now operative.

## 2. What this CR does

- **`CATALOG.yaml`** (generated): 11 entities indexed; catalog identity (id `dea:catalog-value-streams`, name Value Stream, abbreviation VS, version 1.0.0, status active, metamodel_version 1.0.0, owner TechNeHub Labs) read from the pointer's new identity block per CR-CATALOG-STRUCT-06a.
- **`metamodel-pointer.yaml`**: catalog identity block added at the top level (the block the regenerator reads); the `metamodel:` block and its ADR-0002 semantics unchanged — allocation changes still go through the root model.
- **Vendored toolchain**: `scripts/regenerate_catalog.py`, `scripts/check_catalog_index.py`, `catalog-index-schema/catalog-index-schema.json` (from dea-metaframework v2.6.0).
- **`.github/workflows/catalog-conformance.yml`**: freshness gate (`--check`) + index schema validation; `fetch-depth: 0` and head-SHA checkout (the CR-DEA-BC-37 pattern that keeps git-log-based `last_modified` fields meaningful); no metaframework fetch in CI (vendored copies preferred).

## 3. Local extension (documented, pending upstream)

Upstream's entity-id pattern (regenerator, gate, and index schema) enumerates level tokens and does not include `value-stream`, and its namespace subpattern `[a-z]+:` rejects hyphenated namespaces. Both would silently skip every record in this catalog. The vendored copies carry a minimal, in-file-documented extension: the `value-stream` level token and a hyphen-tolerant namespace prefix (`[a-z][a-z0-9-]*:`). The upstream gap is filed as [dea-metaframework issue #51](https://github.com/technehub-labs/dea-metaframework/issues/51) (which also requests the registry ratification); when it lands upstream, the vendored copies can be re-synced without the extension.

## 4. Non-goals

- No entity, universe, sweep, or admission changes; `CATALOG.yaml` is machine-generated and its state fields reflect the current subtree layout (records at subtree roots with `lifecycle_status: active` are indexed as entities; the state precedence semantics are upstream's, unchanged).
- No release packaging (waits on the dea-release-package program's umbrella CR).

## 5. Verification

- `scripts/regenerate_catalog.py --check`: CATALOG.yaml is current (exit 0).
- `scripts/check_catalog_index.py`: CATALOG.yaml validates against the index schema (11 entities; exit 0).
- Regenerated output byte-stable across re-runs; the two `cross_cutting` warnings (optional `classifications/`, `contributions/` dirs absent) are non-blocking and match the sibling catalog behavior.

## 6. Follow-on

1. Upstream: dea-metaframework issue #51 (namespace token + level token + hyphen-tolerant patterns), then re-vendor without the local extension.
2. Release packaging per the dea-release-package program once its umbrella CR is accepted.
3. Actors catalog dependency → `customer_ref` backfill (blocked: actors repo content not readable from this sandbox).
