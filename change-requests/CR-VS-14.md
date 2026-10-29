# CR-VS-14 — Documentation-sync CI gates: entity docs and README statistics can never drift

| Field | Value |
|---|---|
| Status | Executed (this document) |
| Target repository | `technehub-labs/dea-catalog-value-streams` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-29 |
| Depends on | CR-VS-13 (per-entity docs + generator); PR #17 (root README visual refresh) |
| Method | Freshness-gate pattern (mirrors CATALOG.yaml's `--check` gate, CR-CATALOG-STRUCT-06a) |

## 1. Problem

After CR-VS-13, the documentation base is generated — but generation only
happened when run by hand. Nothing kept the docs in sync: a record change
could land with stale per-entity READMEs, stale `research/` notes, or a
root README whose badges, industry table, and ECF matrix no longer matched
the catalog. Generated-but-ungated docs rot.

## 2. What this CR does

### 2.1 Per-entity docs freshness gate

`scripts/generate_entity_docs.py --check`: regenerates every README and
research file in memory and exits 1 if any committed file differs from
what the records + evidence register produce. Wired into
`validate-entries.yml` (runs after the referential-integrity step, on
every push/PR to main). A record change now **must** ship its regenerated
docs in the same PR, exactly like CATALOG.yaml under the conformance gate.

### 2.2 Root-README statistics gate

`scripts/check_readme_stats.py` (new): recomputes every derived number in
the landing README from the records and fails on any mismatch —

- badges (stream count, industry count) and intro counts;
- catalog-at-a-glance table (streams split, stage count, category split);
- the per-industry table (all 15 rows);
- the full 7×7 ECF overlay matrix, via a vendored coordinate map.

### 2.3 Vendored ECF coordinate map

`tools/id-sets/capability-ecf-coordinates.txt`: capability id → primary
ECF coordinate, rebuilt strictly from the sibling capabilities catalog's
authoritative `ecf.primary` fields (29 entries, refresh-dated header).
This corrects four coordinates the PR #17 matrix had guessed from
non-primary data — the authoritative matrix is materially different
(`enablement-operations/operate`: 186 streams, not 104;
`governance-existence/conceive`: 92, not 67), demonstrating exactly the
drift class this gate exists to catch. The README matrix was regenerated
from the authoritative map.

### 2.4 What stays hand-maintained

The mermaid diagrams' *topology* (which streams to include in the
backbone/bridge rendering for legibility) remains a curation choice; the
gates enforce the *numbers* and the per-entity renderings. If the catalog
grows past where the hand-curated diagram reads well, the diagram becomes
fully generated in a follow-up.

## 3. Non-goals

- No record, schema, or vocabulary changes.
- The cross-stream mermaid map is not yet gated (see §2.4).

## 4. Verification

- Drift test: perturbing one committed README makes `--check` exit 1
  naming the stale file; restoring it passes (111 docs current).
- `check_readme_stats.py`: OK (111 streams, 396 stages, 15 industries,
  ECF matrix current) — and it caught the four guessed coordinates before
  they could ship as "authoritative".
- Vendored coordinate map cross-verified against the live sibling
  records' `ecf.primary` (29/29 match).
- Both gates wired into `validate-entries.yml` with the same skip guard
  as the existing steps; workflow header documents the CR-VS-14 contract.

### 2.5 Extension: entities README + register status sync

The entities/v1-alpha README's Status section still reported "11 admitted
value streams (v1.1.0)" — hand-maintained and stale through three
population tranches. Now:

- the Status section carries a `<!-- stats:begin/end -->` anchor block
  with the derived numbers (admitted total, generic/industry split,
  industries, stages, canonical-state and no-pending claims);
- `check_readme_stats.py` validates every number in the block against
  the records (drift-tested: a fake split fails the gate);
- the evidence register's status line (also stale: "no admissions yet")
  is corrected and its admission count is gated the same way.
