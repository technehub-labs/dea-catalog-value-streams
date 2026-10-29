---
documentation_generated_from: value-streams-value-stream-engineer-to-order-htpc6d.yaml
id: value-streams:value-stream-engineer-to-order-htpc6d
name: Engineer to Order
type: ValueStream
version: 1.0.0
lifecycle_status: active
value_stream_category: operational
industries:
- manufacturing
specificity: industry-specific
entry_criterion: A customer order with engineering specification is received.
exit_criterion: The engineered product is delivered and accepted.
outcome: A delivered product engineered to the customer's specification.
stages:
- Agree Specification
- Engineer Design
- Procure and Build
- Test and Deliver
capabilities:
- capabilities:capability-customer-management-f3n8wb
- capabilities:capability-legal-matter-management-zzbd2u
- capabilities:capability-offering-management-6egkc8
- capabilities:capability-operations-management-pm3w8k
- capabilities:capability-sourcing-and-procurement-esucp4
- capabilities:capability-technology-management-maus5n
processes:
- processes:process-eo-operate-44jsrp
- processes:process-eo-operate-vzcxx7
- processes:process-eo-operate-xud3hs
- processes:process-eo-operate-zh9m57
- processes:process-ge-build-mctdgc
- processes:process-pv-design-8v4k89
metrics:
- Engineering change orders per project
upstream: []
downstream:
- value-stream-plan-to-deliver
evidence_sources:
- SRC-016
---

# Engineer to Order

`value-streams:value-stream-engineer-to-order-htpc6d` · **operational** · manufacturing · industry-specific

> The make-to-order stream from customer specification through engineering design, build, and delivery.

**Outcome:** A delivered product engineered to the customer's specification.

**Machine-readable:** this page is generated from — and must stay in sync with — the authoritative record [`value-streams-value-stream-engineer-to-order-htpc6d.yaml`](./value-streams-value-stream-engineer-to-order-htpc6d.yaml). The front matter above is YAML-extractable metadata.

## Stage flow

```mermaid
flowchart LR
  S1["1. Agree Specification"]
  S2["2. Engineer Design"]
  S3["3. Procure and Build"]
  S4["4. Test and Deliver"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  TRIGGER(("⏺ Entry")) --> S1
  S4 --> EXIT1((("✔ Exit"))
```

## Value stages

| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |
|---|---|---|---|---|---|---|
| 1 | **Agree Specification** | A specified order is received. | The specification is agreed. | 2 | 1 | yes |
| 2 | **Engineer Design** | The specification is agreed. | The design is released. | 2 | 1 | no |
| 3 | **Procure and Build** | The design is released. | The product is built. | 2 | 2 | no |
| 4 | **Test and Deliver** | The product is built. | The product is delivered and accepted. | 2 | 2 | yes |

### 1. Agree Specification

Agree the technical specification and contract.

| Aspect | Value |
|---|---|
| Entry criterion | A specified order is received. |
| Exit criterion | The specification is agreed. |
| Outcome | An agreed specification. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb` · `capabilities:capability-legal-matter-management-zzbd2u` |
| Realizing processes | `processes:process-ge-build-mctdgc` |

### 2. Engineer Design

Engineer the product design.

| Aspect | Value |
|---|---|
| Entry criterion | The specification is agreed. |
| Exit criterion | The design is released. |
| Outcome | A released design. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-technology-management-maus5n` · `capabilities:capability-offering-management-6egkc8` |
| Realizing processes | `processes:process-pv-design-8v4k89` |

### 3. Procure and Build

Procure materials and build the product.

| Aspect | Value |
|---|---|
| Entry criterion | The design is released. |
| Exit criterion | The product is built. |
| Outcome | A built product. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-sourcing-and-procurement-esucp4` · `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-vzcxx7` · `processes:process-eo-operate-xud3hs` |

### 4. Test and Deliver

Test and deliver for customer acceptance.

| Aspect | Value |
|---|---|
| Entry criterion | The product is built. |
| Exit criterion | The product is delivered and accepted. |
| Outcome | An accepted delivery. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` · `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-eo-operate-44jsrp` · `processes:process-eo-operate-zh9m57` |

## Scope boundary

**Entry:** A customer order with engineering specification is received.

**Exit:** The engineered product is delivered and accepted.

**In scope**

- Specification and contract
- Engineering design
- Procurement and build
- Testing and delivery

**Out of scope** (owned by the named neighbour)

- Standard production (Plan to Deliver)
- R&D (Concept to Launch)

## Traceability

**Capabilities** (`aggregated_capability_refs`, resolving in [business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-legal-matter-management-zzbd2u`
- `capabilities:capability-technology-management-maus5n`
- `capabilities:capability-offering-management-6egkc8`
- `capabilities:capability-sourcing-and-procurement-esucp4`
- `capabilities:capability-operations-management-pm3w8k`

**Processes** (`process_refs`, resolving in [business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-build-mctdgc`
- `processes:process-pv-design-8v4k89`
- `processes:process-eo-operate-vzcxx7`
- `processes:process-eo-operate-xud3hs`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-zh9m57`

## Cross-stream links

**Upstream:** none recorded.

**Downstream** (this stream's exit feeds their entry):

- [plan to deliver](../value-stream-plan-to-deliver-smmwpx/README.md) — Standardized variants flow through standard production.

## Measurement

- **Engineering change orders per project** (stream-level) — Design stability indicator.

## Evidence

| Source | Class | Reference |
|---|---|---|
| SRC-016 | industry-reference-model | Manufacturing and logistics reference models (SCOR-style category structure) |

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-050) from the CR-VS-11 industry evidence register extension. Industry-specific chain (manufacturing); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

See [research/evidence.md](./research/evidence.md) for the source-backed notes.

## Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) (CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*
