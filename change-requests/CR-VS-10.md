# CR-VS-10 — Id-set snapshot convention: upstream the vendored cross-catalog id snapshots to the metaframework

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-value-streams` (this CR documents the local convention); the ask lands in `dea-metaframework` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-28 |
| Depends on | CR-VS-07 (merged, PR #9) — `tools/id-sets/` introduced; dea-metaframework issue #51 (namespace/level token ratification) is related but not a hard dependency |
| Method | Org-wide catalog repository standard (CR-CATALOG-STRUCT-01); cross-catalog reference-resolution contract |

## 1. Background and problem statement

CR-VS-07 introduced the first automated cross-catalog referential-integrity
gate in the catalog family (`scripts/check_referential_integrity.py`).
To keep the gate deterministic offline (no sibling clone in CI, no network
fetch), it falls back to **vendored id-set snapshots** under
`tools/id-sets/` — one file per referenced sibling catalog, with a refresh
date in the header:

```
tools/id-sets/
├── business-capabilities-ids.txt   # 32 ids (full catalog)
├── business-processes-ids.txt      # 243 ids (process/pc/group levels)
└── metrics-ids.txt                 # (planned, CR-VS-08 — scoped subset)
```

This solved the immediate problem but the convention is now local lore:
every catalog that links cross-catalog (which the CR-VS-07 shape makes
routine — capabilities, processes, metrics, actors) has to reinvent the
snapshot mechanism, the refresh discipline, and the staleness semantics.

## 2. What this CR does

### 2.1 In this repository (documentation-only)

Record the convention as normative local documentation so it survives
independent of the implementing PR:

- **Snapshot format**: one id per line, UTF-8, `#`-prefixed header with the
  sibling repo, scope, and `Last refreshed: YYYY-MM-DD`.
- **Scope policy**: full catalog by default; a scoped subset is allowed for
  very large siblings (e.g. metrics at ~3.9k records) **only** when the
  subset covers every id this catalog actually references — the gate fails
  closed, so under-scoping surfaces as a CI failure, never as a silent
  pass.
- **Refresh rule**: refresh whenever a PR adds or changes a cross-catalog
  ref, or when the gate reports an id that the live sibling carries but the
  snapshot lacks (resolution order clone → index → snapshot means the
  snapshot only matters when neither clone nor index is available).
- **Staleness semantics**: a stale snapshot can produce false *negatives*
  (unresolved ref that actually resolves) but never false *positives* —
  the gate's failure mode is safe.

### 2.2 The upstream ask (dea-metaframework)

File a metaframework issue proposing:

1. **Standard snapshot location and format** — e.g.
   `tools/id-sets/<catalog>-ids.txt` with the header convention above, as
   part of the catalog repository standard (CR-CATALOG-STRUCT-01 §7 or a
   new CR-CATALOG-REF-01).
2. **A snapshot-refresh helper** — a small standard-library script that
   regenerates a snapshot from a sibling clone or its `CATALOG.yaml` index
   (either vendored or fetched), replacing each catalog's hand-rolled
   refresh.
3. **Ratification alongside issue #51** — the id-system namespace/level
   token ratification (#51) should carry this convention, since both govern
   how catalogs reference each other's records.

This catalog's `tools/id-sets/` and gate then re-sync to the standard form
without behavioral change.

## 3. Non-goals

- No schema or record changes; no gate behavior changes.
- No cross-catalog *reverse* integrity (sibling catalogs checking that
  their records are still referenced) — that is a metaframework-level
  design question raised in the issue, not decided here.

## 4. Verification plan

- Documentation-only in this repo: README/CHANGELOG pointers updated; no
  CI surface changes.
- Upstream: metaframework issue filed, linked from this CR; tracked to
  resolution via the change-requests index status column.
