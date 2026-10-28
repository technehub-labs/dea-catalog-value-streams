# Change Requests — dea-catalog-value-streams

Every catalog modification of substance is governed by a numbered Change
Request, following the org-wide CR pattern (`dea-metamodel` CR-1.8,
`dea-catalog-business-capabilities` CR-DEA-BC-*).

| CR | Focus | Primary outcome | Status |
|---|---|---|---|
| CR-VS-01 | Candidate universe seed + evidence register | `catalog-research/` opened: evidence register (6 sources), candidate universe (9 value-stream candidates + 1 disambiguation record); none canonical | Proposed |
| CR-VS-02 | Distinctness sweep v0.1 | 36 pairs swept; VSC-007 merged into VSC-001 (RES-001); VSC-008/009 boundary (RES-002); 4 admission-ready candidates | Merged (PR #4) |
| CR-VS-03 | First admission gate | VSC-001/002/003/006 admitted as the first 4 canonical records under entities/v1-alpha/ | Merged (PR #5) |
| CR-VS-04 | Second-tranche evidence + admissions | Register v0.2 extension (SRC-002/SRC-003 observations); VSC-004/005/008/009 raised E2 -> E3 and admitted; 8 canonical records | Merged (PR #6) |
| CR-VS-05 | Third tranche: expansion + sweep + admissions | Universe v0.5 (VSC-011..014 seeded); sweep v0.2 (38 new pairs; RES-003 merge of Fault to Restore into Issue to Resolve); VSC-011/012/013 admitted; 11 canonical records | Merged (PR #7) |
| CR-VS-06 | Catalog index conformance | CATALOG.yaml generated (11 entities); vendored regenerator/gate/schema (metaframework v2.6.0 + documented local extension for the value-stream level token); catalog-conformance workflow | Proposed |
| CR-VS-07 | Value Stream schema enrichment | `value_stages` with per-stage capability/process refs; `value_stream_category`, `scope`, `process_refs`, upstream/downstream links, `metrics`; referential-integrity gate (`scripts/check_referential_integrity.py` + vendored id snapshots) wired into validate-entries; all 11 records enriched (v1.1.0); comprehensive per-entity READMEs + root README enrichment | Merged (PR #9) |
| CR-VS-08 | Metric backfill | `metrics[].metric_ref` populated where `dea-catalog-metrics` carries the measure (verified map, 15 links); schema pattern admits the sibling's legacy `dea:metric-*` id form; metrics namespace activated in the referential-integrity gate + scoped id snapshot | Proposed |
| CR-VS-09 | Served-party and stage-actor backfill | `customer_ref` + per-stage `actor_refs` population in all 11 records — dependency-gated on `dea-catalog-actors` admitting the generic party records (customer, supplier, employee, custodian, market-segment, governance-stakeholder) | Proposed (blocked on actors catalog) |
| CR-VS-10 | Id-set snapshot convention | Local snapshot convention documented (format, scope policy, refresh rule, safe staleness semantics); upstream ask filed to `dea-metaframework` for a standard cross-catalog id-snapshot convention + refresh helper, alongside issue #51 | Proposed |
