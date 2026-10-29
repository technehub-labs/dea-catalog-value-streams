# Dangerous Goods Accept to Deliver

Admitted Value Stream record (`value-streams:value-stream-dangerous-goods-accept-to-deliver-txbc4c`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-dangerous-goods-accept-to-deliver-txbc4c` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | governance |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | logistics-transportation · industry-specific |
| Record | [`value-streams-value-stream-dangerous-goods-accept-to-deliver-txbc4c.yaml`](./value-streams-value-stream-dangerous-goods-accept-to-deliver-txbc4c.yaml) — authoritative |

## 2. Definition

> The DG stream from acceptance check through compliant handling and documentation to delivered consignment.

## 3. Value proposition and served party

**Outcome:** A compliantly delivered dangerous-goods consignment.

## 4. Stream boundary

**Entry criterion:** A dangerous-goods booking is made.

**Exit criterion:** The consignment is delivered compliantly.

**In scope** (from the record's `scope.includes`):

- Acceptance and classification check
- Compliant handling and segregation
- Documentation and delivery

**Out of scope** (each concern owned by the named neighbour):

- Standard freight (Ship to Consignee)
- Incident response (Safety Incident to Closure)

## 5. Value stages

Dangerous Goods Accept to Deliver decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Accept and Classify

Accept the booking and verify classification and packing.

| Aspect | Value |
|---|---|
| Entry criterion | A DG booking is made. |
| Exit criterion | The consignment is accepted. |
| Outcome | An accepted consignment. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8`, `capabilities:capability-risk-management-h9uxdw` |
| Realizing processes | `processes:process-ge-operate-tpenm6` |

### Stage 2: Handle Compliantly

Handle and segregate per class.

| Aspect | Value |
|---|---|
| Entry criterion | The consignment is accepted. |
| Exit criterion | Handling is compliant. |
| Outcome | Compliant handling. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-security-management-wmzc7c`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-zwzmbd`, `processes:process-eo-operate-zh9m57` |

### Stage 3: Document and Deliver

Complete DG documentation and deliver.

| Aspect | Value |
|---|---|
| Entry criterion | Handling is compliant. |
| Exit criterion | The consignment is delivered with papers. |
| Outcome | A delivered consignment. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-regulation-management-gya4d8`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-fa-operate-8vqvkk`, `processes:process-eo-operate-zh9m57` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-regulation-management-gya4d8`
- `capabilities:capability-risk-management-h9uxdw`
- `capabilities:capability-security-management-wmzc7c`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-ge-operate-tpenm6`
- `processes:process-eo-operate-zwzmbd`
- `processes:process-eo-operate-zh9m57`
- `processes:process-fa-operate-8vqvkk`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **DG documentation accuracy** (stream-level) — Share of consignments with complete compliant papers at delivery.

## 9. Evidence and admission

**Evidence sources:** SRC-016 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-071) from the CR-VS-11 industry evidence register extension. Industry-specific chain (logistics-transportation); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
