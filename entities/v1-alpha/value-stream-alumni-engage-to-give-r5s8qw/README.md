# Alumni Engage to Give

Admitted Value Stream record (`value-streams:value-stream-alumni-engage-to-give-r5s8qw`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-alumni-engage-to-give-r5s8qw` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | support |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | education · industry-specific |
| Record | [`value-streams-value-stream-alumni-engage-to-give-r5s8qw.yaml`](./value-streams-value-stream-alumni-engage-to-give-r5s8qw.yaml) — authoritative |

## 2. Definition

> The advancement stream from alumni engagement through cultivation to received contribution.

## 3. Value proposition and served party

**Outcome:** A received, acknowledged alumni contribution.

## 4. Stream boundary

**Entry criterion:** An alumnus is engaged.

**Exit criterion:** The contribution is received and acknowledged.

**In scope** (from the record's `scope.includes`):

- Engagement
- Cultivation and solicitation
- Receipt and acknowledgement

**Out of scope** (each concern owned by the named neighbour):

- Degree delivery
- Corporate partnerships

## 5. Value stages

Alumni Engage to Give decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Engage

Engage the alumnus.

| Aspect | Value |
|---|---|
| Entry criterion | An alumnus is identified. |
| Exit criterion | The alumnus is engaged. |
| Outcome | An engaged alumnus. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-improve-t6uvan` |

### Stage 2: Cultivate and Solicit

Cultivate and solicit the gift.

| Aspect | Value |
|---|---|
| Entry criterion | The alumnus is engaged. |
| Exit criterion | A pledge is made. |
| Outcome | A pledged gift. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-partner-management-cp3vdb` |
| Realizing processes | `processes:process-pr-operate-bbe384` |

### Stage 3: Receive and Acknowledge

Receive and acknowledge the contribution.

| Aspect | Value |
|---|---|
| Entry criterion | A pledge is made. |
| Exit criterion | The gift is received and acknowledged. |
| Outcome | A received gift. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-financial-stewardship-c7xtfk`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-partner-management-cp3vdb`
- `capabilities:capability-financial-stewardship-c7xtfk`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-improve-t6uvan`
- `processes:process-pr-operate-bbe384`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Alumni participation rate** (stream-level) — Share of alumni contributing per year.

## 9. Evidence and admission

**Evidence sources:** SRC-015 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-085) from the CR-VS-11 industry evidence register extension. Industry-specific chain (education); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
