# Catalog-wide research: technehub-labs/dea-catalog-value-streams

This directory holds research artifacts that document the catalog as a whole
rather than any one entity: the candidate universe, evidence register,
distinctness sweep, and admission-gate records for the Value Stream (VS)
catalog.

## Method

Admission follows the org-wide catalog research pattern (established in
`dea-catalog-business-capabilities` under CR-DEA-BC-02):

1. **Candidate universe** (`candidate-universe.yaml`): enumerate candidate
   value streams from the evidence register sources; classify each entry;
   none are canonical by default (`canonical: false` in provenance).
2. **Evidence register** (`evidence-register.yaml`): record each public
   source, its class, its observations, and the candidates/claims it
   supports. Evidence ratings E0..E5 per the org pattern.
3. **Distinctness sweep**: pairwise distinctness of candidates against
   adjacent concepts (processes, capabilities, journeys).
4. **Admission gate**: a candidate is admitted as a canonical catalog entry
   (`entities/v1-alpha/`) only through an admission change request that
   cites the evidence register and closes the gate checklist.

## Provenance

Machine-readable state lives in the YAML files; narrative reports
(`*-v0.1.md`) summarize each staged delivery. Research artifacts that are
about a single entity move to that entity's `research/` subtree at admission
time, per CR-CATALOG-STRUCT-01 section 5.
