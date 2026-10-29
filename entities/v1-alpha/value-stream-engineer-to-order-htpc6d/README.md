# Engineer to Order

Admitted Value Stream record (`value-streams:value-stream-engineer-to-order-htpc6d`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-engineer-to-order-htpc6d` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | manufacturing · industry-specific |
| Record | [`value-streams-value-stream-engineer-to-order-htpc6d.yaml`](./value-streams-value-stream-engineer-to-order-htpc6d.yaml) — authoritative |

## 2. Definition

> The make-to-order stream from customer specification through engineering design, build, and delivery.

## 3. Value proposition and served party

**Outcome:** A delivered product engineered to the customer's specification.

## 4. Stream boundary

**Entry criterion:** A customer order with engineering specification is received.

**Exit criterion:** The engineered product is delivered and accepted.

**In scope** (from the record's `scope.includes`):

- Specification and contract
- Engineering design
- Procurement and build
- Testing and delivery

**Out of scope** (each concern owned by the named neighbour):

- Standard production (Plan to Deliver)
- R&D (Concept to Launch)

## 5. Value stages

Engineer to Order decomposes into 4 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Agree Specification

Agree the technical specification and contract.

| Aspect | Value |
|---|---|
| Entry criterion | A specified order is received. |
| Exit criterion | The specification is agreed. |
| Outcome | An agreed specification. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### Stage 2: Engineer Design

Engineer the product design.

| Aspect | Value |
|---|---|
| Entry criterion | The specification is agreed. |
| Exit criterion | The design is released. |
| Outcome | A released design. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n`, `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-pv-design-8v4k89` |

### Stage 3: Procure and Build

Procure materials and build the product.

| Aspect | Value |
|---|---|
| Entry criterion | The design is released. |
| Exit criterion | The product is built. |
| Outcome | A built product. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-sourcing-and-procurement-esucp4`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-vzcxx7`, `processes:process-eo-operate-xud3hs` |

### Stage 4: Test and Deliver

Test and deliver for customer acceptance.

| Aspect | Value |
|---|---|
| Entry criterion | The product is built. |
| Exit criterion | The product is delivered and accepted. |
| Outcome | An accepted delivery. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-eo-operate-44jsrp`, `processes:process-eo-operate-zh9m57` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-sourcing-and-procurement-esucp4`
- `capabilities:capability-operations-management-pm3w8k`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-build-mctdgc`
- `processes:process-pv-design-8v4k89`
- `processes:process-eo-operate-vzcxx7`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-zh9m57`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams** (this stream's exit feeds their entry):

- `value-streams:value-value-stream-plan-to-deliver` — Standardized variants flow through standard production.

## 8. Measurement

- **Engineering change orders per project** (stream-level) — Design stability indicator.

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-050) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
