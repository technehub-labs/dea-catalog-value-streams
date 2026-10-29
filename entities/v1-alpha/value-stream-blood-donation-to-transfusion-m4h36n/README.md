# Blood Donation to Transfusion

Admitted Value Stream record (`value-streams:value-stream-blood-donation-to-transfusion-m4h36n`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-blood-donation-to-transfusion-m4h36n` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | healthcare · industry-specific |
| Record | [`value-streams-value-stream-blood-donation-to-transfusion-m4h36n.yaml`](./value-streams-value-stream-blood-donation-to-transfusion-m4h36n.yaml) — authoritative |

## 2. Definition

> The end-to-end blood stream from donor recruitment through collection, testing, processing, and transfusion to the recipient.

## 3. Value proposition and served party

**Outcome:** Safe blood components transfused to the patient who needs them.

## 4. Stream boundary

**Entry criterion:** A donor presents or is recruited.

**Exit criterion:** The transfusion is completed and documented.

**In scope** (from the record's `scope.includes`):

- Donor recruitment and screening
- Collection
- Testing and processing
- Storage and issue
- Transfusion

**Out of scope** (each concern owned by the named neighbour):

- General laboratory operations
- Research biobanking

## 5. Value stages

Blood Donation to Transfusion decomposes into 5 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Recruit and Screen Donor

Recruit the donor and complete donation screening.

| Aspect | Value |
|---|---|
| Entry criterion | A donor presents or is recruited. |
| Exit criterion | The donor is screened and eligible. |
| Outcome | An eligible, screened donor. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-marketing-xmc539`, `capabilities:capability-customer-management-f3n8wb` |
| Realizing processes | `processes:process-pr-build-nygvw7` |

### Stage 2: Collect

Collect the donation.

| Aspect | Value |
|---|---|
| Entry criterion | A donor is eligible. |
| Exit criterion | The donation is collected. |
| Outcome | A collected donation. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

### Stage 3: Test and Process

Test and process the donation into components.

| Aspect | Value |
|---|---|
| Entry criterion | A donation is collected. |
| Exit criterion | Components are tested, processed, and released. |
| Outcome | Released safe components. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-risk-management-h9uxdw`, `capabilities:capability-operations-management-pm3w8k` |
| Realizing processes | `processes:process-eo-operate-44jsrp` |

### Stage 4: Store and Issue

Store components and issue to order.

| Aspect | Value |
|---|---|
| Entry criterion | Components are released. |
| Exit criterion | Components are issued to the clinical order. |
| Outcome | Issued components. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-zwzmbd` |

### Stage 5: Transfuse

Transfuse to the recipient and document.

| Aspect | Value |
|---|---|
| Entry criterion | Components are issued. |
| Exit criterion | The transfusion is completed and documented. |
| Outcome | A transfused, monitored patient. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-operations-management-pm3w8k`, `capabilities:capability-information-management-6vjgdh` |
| Realizing processes | `processes:process-eo-operate-2jnz85` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-operations-management-pm3w8k`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-risk-management-h9uxdw`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-build-nygvw7`
- `processes:process-eo-operate-2jnz85`
- `processes:process-eo-operate-44jsrp`
- `processes:process-eo-operate-zwzmbd`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Blood component wastage rate** (stream-level) — Expired or discarded units as a share of collected volume.

## 9. Evidence and admission

**Evidence sources:** SRC-007 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-020) from the CR-VS-11 industry evidence register extension. Industry-specific chain (healthcare); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
