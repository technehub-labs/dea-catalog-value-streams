# CR-VS-08 — Metric backfill: link stream metrics to the catalogued PerformanceMetric records

| Field | Value |
|---|---|
| Status | Executed (this document) |
| Target repository | `technehub-labs/dea-catalog-value-streams` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-28 |
| Depends on | CR-VS-07 (merged, PR #9) — `metrics[]` block exists with optional `metric_ref` |
| Method | Catalog repository standard (CR-CATALOG-STRUCT-01); reference-resolution contract (CR-VS-03 §4; CR-VS-07 §2) |

## 1. Background and problem statement

CR-VS-07 added a `metrics[]` block to every record: `name`, `definition`,
optional `applies_to_stage`, and an optional `metric_ref` reserved for a
catalogued PerformanceMetric id (`dea:measured-by` record-side companion).
All 11 records carry 2–3 metrics **by name and definition only** — the
`metric_ref` slot is unpopulated everywhere, so the catalog's measures are
not yet referentially linked to the metrics catalog.

The sibling catalog `dea-catalog-metrics` is substantial (3,866 admitted
PerformanceMetric records), so most stream-level measures already have a
canonical home; linking them is a backfill, not new authorship.

## 2. What this CR does

Populate `metrics[].metric_ref` in the 11 records where the catalogued
metric exists, and rename the free-text `name` of any local metric to align
with the catalogued metric's canonical name when they are the same measure.

### 2.1 Schema adjustment (one pattern relaxation)

`metric_ref`'s current pattern in `schemas/entity.schema.json` is
`^metrics:[a-z0-9-]+(-[hash6])?$` — the org-wide post-migration namespace
form. However, the metrics catalog's admitted records still carry the
**legacy id form** `dea:metric-<slug>` (verified: e.g.
`dea:metric-perfect-order-rate`, `dea:metric-days-sales-outstanding`). The
pattern must admit both forms:

- `metrics:<slug>` / `metrics:metric-<slug>-<hash6>` (org-wide form), and
- `dea:metric-<slug>` (legacy form, matching the sibling catalog as it
  stands today).

When the metrics catalog migrates to the org-wide id system, the
referential-integrity gate will surface the break and the refs get
rewritten in a follow-up CR — the gate exists precisely to catch that.

### 2.2 Referential-integrity gate extension

`scripts/check_referential_integrity.py` currently checks the `metrics:`
namespace. This CR:

- adds `dea:metric-*` (legacy) refs to the checked set, resolving against
  the same id universe sources (sibling clone → sibling `CATALOG.yaml` →
  vendored snapshot);
- adds a vendored `tools/id-sets/metrics-ids.txt` snapshot. Given the
  sibling catalog's size (~3.9k records), the snapshot will carry only the
  ids referenced by this catalog (~15) plus a header documenting the scope
  decision, so the file stays reviewable.

### 2.3 Backfill map (per record, per metric)

Verified against `dea-catalog-metrics` at drafting time (record exists /
does not exist):

| Record | Metric (stage) | Catalogued metric | Exists |
|---|---|---|---|
| Order to Cash | Perfect order rate (Fulfill Order) | `dea:metric-perfect-order-rate` | yes |
| Order to Cash | Days sales outstanding (Invoice and Settle) | `dea:metric-days-sales-outstanding` | yes |
| Procure to Pay | Invoice match rate (Settle Supplier) | `dea:metric-first-time-match-rate` (AP first-time match; rename local metric to align) | yes |
| Procure to Pay | Procure-to-pay cycle time (Settle Supplier) | `dea:metric-invoice-processing-cycle-time` (partial match: invoice leg only; keep local definition, link as nearest canonical) | yes |
| Issue to Resolve | First-contact resolution rate (Diagnose) | `dea:metric-first-contact-resolution` | yes |
| Issue to Resolve | Mean time to resolve (Confirm Resolution) | — | **no** (only domain-specific MTTRs: `noc-`, `ethics-incident-`) |
| Concept to Launch | Concept-to-launch lead time (Launch) | — | **no** |
| Plan to Deliver | On-time delivery / plan adherence (Deliver) | `dea:metric-on-time-delivery-rate` (delivery leg) | yes |
| Hire to Retire | Time to hire (Hire) | `dea:metric-time-to-hire` | yes |
| Hire to Retire | Voluntary attrition rate (Separate) | `dea:metric-voluntary-turnover-rate` (rename local metric to align) | yes |
| Plan to Forecast | Forecast accuracy (Ratify Forecast) | `dea:metric-cash-forecast-accuracy` (cash scope; note scope narrower than stream) | yes |
| Record to Report | Close cycle time (Close Period) | `dea:metric-financial-close-cycle-time` | yes |
| Record to Report | Restatement rate (Report) | `dea:metric-financial-restatement-count` (count form; keep local rate definition, link as nearest canonical) | yes |
| Contract to Renewal | Net revenue retention (Settle Renewal) | `dea:metric-net-revenue-retention` | yes |
| Return to Credit | Return rate (Initiate Return) | `dea:metric-return-rate` | yes |
| Acquire to Retire | Asset utilization (Operate and Maintain) | `dea:metric-asset-utilization-rate` | yes |

Metrics with **no catalogued counterpart** (Issue-to-Resolve MTTR,
Concept-to-Launch lead time, plus any others found unresolvable at
execution) stay unlinked, with the gap recorded in §4 — proposing new
PerformanceMetric records to the metrics catalog is that catalog's
admission process, out of scope here.

## 3. Non-goals

- No new metrics authored in this catalog; no changes to `name`/`definition`
  beyond the alignment renames in §2.3.
- No metrics-catalog migration to the org-wide id system (their backlog;
  this CR only tolerates both forms).
- No `customer_ref`/`actor_refs` backfill (that is CR-VS-09, blocked on the
  actors catalog).

## 4. Follow-on register (out of this CR's scope, tracked here)

Filed as candidate-seed input to the metrics catalog: [dea-catalog-metrics#13](https://github.com/technehub-labs/dea-catalog-metrics/issues/13).

Catalogued-metric gaps discovered by the backfill map, for the metrics
catalog's own candidate pipeline: generic mean-time-to-resolve (issue
resolution), concept-to-launch lead time, procure-to-pay end-to-end cycle
time, production schedule attainment, planning-cycle length,
return-cycle-time, and time-to-retire (asset disposition).

## 5. Verification (execution record)

- Schema validation: all 11 records + fixture pass with populated
  `metric_ref` values (pattern relaxed per §2.1). Executed: 12/12 pass.
- `scripts/check_referential_integrity.py`: pass with the metrics namespace
  active — both snapshot (offline) and live-clone resolution. Executed:
  14 populated refs, 0 unresolved against the vendored snapshot and the
  live `dea-catalog-metrics` clone.
- Every `metric_ref` in §2.3 resolving to an existing
  `dea-catalog-metrics` record. Executed: scripted check against the
  sibling clone — none missing.
- CATALOG.yaml regenerated (record versions bumped 1.1.0 → 1.2.0);
  `catalog-conformance` green. Executed: `--check` OK, index OK (11 entities).

Execution notes:
- 14 links populated (the §2.3 map's 15th row — Order to Cash
  end-to-end cycle time — stays unlinked; the catalogued
  `dea:metric-invoice-processing-cycle-time` covers only the invoice leg).
- Both alignment renames applied (Invoice match rate → First-time
  match rate; Voluntary attrition rate → Voluntary turnover rate);
  Asset utilization → Asset utilization rate aligned to the
  catalogued metric name.
- Gate fix included: the snapshot loader used `lstrip("id: ")`, which
  mangled `dea:metric-*` entries (stripping the leading `d`); replaced
  with an exact-prefix strip. Also fixes a latent bug for any future id
  starting with `i`, `d`, `:`, or space in the org-wide snapshots.

## 6. Original verification plan

- Schema validation: all 11 records + fixture pass with populated
  `metric_ref` values (pattern relaxed per §2.1).
- `scripts/check_referential_integrity.py`: pass with the metrics namespace
  active (clone-resolved locally; snapshot offline).
- Every `metric_ref` in §2.3 resolving to an existing
  `dea-catalog-metrics` record (scripted check against the sibling clone).
- CATALOG.yaml regenerated (record versions bump 1.1.0 → 1.2.0);
  `catalog-conformance` green.
