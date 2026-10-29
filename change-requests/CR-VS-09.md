# CR-VS-09 — Served-party and stage-actor backfill: `customer_ref` and `actor_refs` population

| Field | Value |
|---|---|
| Status | Proposed (this document) — **dependency-gated, not executable yet** |
| Target repository | `technehub-labs/dea-catalog-value-streams` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-28 |
| Depends on | CR-VS-07 (merged, PR #9) — `customer_ref` and `actor_refs` slots exist; **and** `dea-catalog-actors` admitting the generic party records listed in §3 — requested in [dea-catalog-actors#9](https://github.com/technehub-labs/dea-catalog-actors/issues/9) |
| Method | Catalog repository standard (CR-CATALOG-STRUCT-01); reference-resolution contract (CR-VS-03 §4/§7; CR-VS-07 §2) |

## 1. Background and problem statement

CR-VS-03 deliberately omitted `customer_ref`: "the actors catalog does not
yet carry generic customer/supplier/employee records, and fabricating
references would violate the reference-resolution contract." CR-VS-07 kept
that contract — `customer_ref` remains unpopulated across all 11 records,
and the per-stage `actor_refs` slots (schema-supported since CR-VS-07) are
likewise empty. The served party is currently only expressible as free text.

Verified at drafting time: `dea-catalog-actors` has **no `entities/`
content at all** (repository exists, no admitted records). This CR is
therefore drafted as a ready-to-execute backfill, gated on that catalog's
first admissions.

## 2. What this CR does

When the gate opens (§3 records exist in `dea-catalog-actors`):

1. **`customer_ref` backfill** — populate the stream-level served-party
   reference in all 11 records.
2. **`actor_refs` backfill** — populate the per-stage participating-actor
   links in `value_stages[]` (schema slot already present).
3. **Gate hardening** — extend `scripts/check_referential_integrity.py`:
   the `actors:` namespace check activates as soon as any record populates
   an `actors:` ref (the gate already handles this namespace; this CR adds
   a vendored `tools/id-sets/actors-ids.txt` snapshot once the sibling
   catalog lands its first records).
4. **README regeneration** — per-entity READMEs re-render (they render
   record content, so served-party and stage-actor rows appear
   automatically); root README's record-anatomy section unchanged.

Record versions bump 1.x.0 → next minor; ids/directories/filenames stay
stable (rename-stability contract, PR #5).

## 3. Dependency: required actor records

The generic party records this backfill needs (naming per the evidence
register's served-party observations, SRC-001/SRC-003):

| Served party (streams) | Required actor record |
|---|---|
| Customer (Order to Cash, Issue to Resolve, Contract to Renewal, Return to Credit) | customer |
| Supplier / trading partner (Procure to Pay) | supplier |
| Employee / workforce (Hire to Retire) | employee |
| Asset custodian / internal operator (Acquire to Retire) | internal-asset-custodian |
| Market / consumer segment (Concept to Launch) | market-segment (or the closest record the actors catalog admits) |
| Enterprise governance stakeholders (Plan to Forecast, Record to Report) | governance-stakeholder (or the closest admitted record) |

Exact ids will be taken from `dea-catalog-actors` at execution time; the
gate enforces resolution, so this CR cannot land with invented ids. If the
actors catalog admits different granularity (e.g. a generic
`external-party`), the mapping table above is revised at execution, not
the streams' semantics.

## 4. Stage-actor sketch (execution-time detail)

Per-stage `actor_refs` should name the **operating** actor, not the served
party (e.g. Order to Cash "Fulfill Order" → fulfillment operations actor;
Hire to Retire "Develop and Administer" → HR-operations actor). The exact
actor inventory is deferred to execution so it uses only admitted records;
the schema imposes no minimum on `actor_refs`, so partial population is
valid and the gate still checks whatever is present.

## 5. Non-goals

- No new value streams, merges, retirements.
- No actors-catalog authorship (their admission pipeline owns generic
  actor records; this CR only consumes).
- No change to the metamodel relationship set (`dea:served-by`,
  `dea:flows-to` semantics unchanged).

## 6. Verification plan

- `scripts/check_referential_integrity.py`: pass with `actors:` refs
  resolving against the sibling clone (and snapshot offline).
- Schema validation: all records + fixture pass.
- Per-entity READMEs re-rendered; CATALOG.yaml regenerated; all three CI
  workflows green.
