# Private Label Design to Launch

Admitted Value Stream record (`value-streams:value-stream-private-label-design-to-launch-mh6xqr`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-private-label-design-to-launch-mh6xqr` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | development |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | retail-commerce · industry-specific |
| Record | [`value-streams-value-stream-private-label-design-to-launch-mh6xqr.yaml`](./value-streams-value-stream-private-label-design-to-launch-mh6xqr.yaml) — authoritative |

## 2. Definition

> The private-label stream from product brief through development to launched own-brand product.

## 3. Value proposition and served party

**Outcome:** A launched private-label product on shelf.

## 4. Stream boundary

**Entry criterion:** A private-label product brief is approved.

**Exit criterion:** The product is launched and on shelf.

**In scope** (from the record's `scope.includes`):

- Product brief and supplier selection
- Development and compliance
- Launch

**Out of scope** (each concern owned by the named neighbour):

- National-brand buying (Assortment to Shelf)
- Concept to Launch (generic product development)

## 5. Value stages

Private Label Design to Launch decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Brief and Select

Approve the brief and select the supplier.

| Aspect | Value |
|---|---|
| Entry criterion | A brief is approved. |
| Exit criterion | The supplier is selected. |
| Outcome | A selected supplier. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8`, `capabilities:capability-supplier-management-d6fuj4` |
| Realizing processes | `processes:process-eo-operate-vzcxx7` |

### Stage 2: Develop and Comply

Develop the product to compliance.

| Aspect | Value |
|---|---|
| Entry criterion | The supplier is selected. |
| Exit criterion | The product is developed and compliant. |
| Outcome | A compliant product. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 3: Launch

Launch to shelf.

| Aspect | Value |
|---|---|
| Entry criterion | The product is compliant. |
| Exit criterion | The product is on shelf. |
| Outcome | A launched product. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-offering-management-6egkc8`, `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pv-operate-cau4gv` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-supplier-management-d6fuj4`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-marketing-xmc539`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-eo-operate-vzcxx7`
- `processes:process-eo-operate-44jsrp`
- `processes:process-pv-operate-cau4gv`

## 7. Cross-stream links

**Upstream streams** (their exit feeds this stream's entry):

- `value-streams:value-value-stream-concept-to-launch` — The private-label specialization of product development.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-assortment-to-shelf` — The launched product enters the assortment.

## 8. Measurement

- **Brief-to-shelf time** (stream-level) — Elapsed weeks from brief to on-shelf availability.

## 9. Evidence and admission

**Evidence sources:** SRC-013 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-063) from the CR-VS-11 industry evidence register extension. Industry-specific chain (retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
