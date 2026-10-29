# Loyalty Enroll to Reward

Admitted Value Stream record (`value-streams:value-stream-loyalty-enroll-to-reward-txebyw`, v1.0.0, active).

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `value-streams:value-stream-loyalty-enroll-to-reward-txebyw` |
| Entity type | ValueStream (dea:ValueStream, layer L3, building block L3-value-delivery) |
| Category | operational |
| Version / status | 1.0.0 · active |
| Metamodel pin | 1.0.0 |
| Applicability | retail-commerce · industry-specific |
| Record | [`value-streams-value-stream-loyalty-enroll-to-reward-txebyw.yaml`](./value-streams-value-stream-loyalty-enroll-to-reward-txebyw.yaml) — authoritative |

## 2. Definition

> The loyalty stream from enrollment through earn accrual to redeemed reward.

## 3. Value proposition and served party

**Outcome:** An engaged loyalty member redeeming rewards.

## 4. Stream boundary

**Entry criterion:** A customer enrolls in the loyalty program.

**Exit criterion:** The member redeems a reward.

**In scope** (from the record's `scope.includes`):

- Enrollment
- Earn accrual
- Reward redemption

**Out of scope** (each concern owned by the named neighbour):

- Marketing campaigns (Promotion Plan to Execution)
- Payments

## 5. Value stages

Loyalty Enroll to Reward decomposes into 3 ordered value stages (array order is flow order; the first stage implements the entry criterion, the last the exit criterion):

### Stage 1: Enroll Member

Enroll the customer in the program.

| Aspect | Value |
|---|---|
| Entry criterion | A customer enrolls. |
| Exit criterion | The member is active. |
| Outcome | An active member. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-marketing-xmc539` |
| Realizing processes | `processes:process-pr-build-nygvw7` |

### Stage 2: Accrue Earn

Accrue earn on qualifying activity.

| Aspect | Value |
|---|---|
| Entry criterion | The member is active. |
| Exit criterion | Earn accrues to the account. |
| Outcome | Accrued earn. |
| Customer visible | False |
| Enabling capabilities | `capabilities:capability-information-management-6vjgdh`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-g9zpnq` |

### Stage 3: Redeem Reward

Redeem the accrued earn for rewards.

| Aspect | Value |
|---|---|
| Entry criterion | Earn accrues. |
| Exit criterion | The reward is redeemed. |
| Outcome | A redeemed reward. |
| Customer visible | True |
| Enabling capabilities | `capabilities:capability-customer-management-f3n8wb`, `capabilities:capability-financial-resource-management-cd3c7c` |
| Realizing processes | `processes:process-fa-operate-sdppmp` |

## 6. Capability and process traceability

**Capabilities aggregated by the stream** (`aggregated_capability_refs`, resolving against [dea-catalog-business-capabilities](https://github.com/technehub-labs/dea-catalog-business-capabilities)):

- `capabilities:capability-customer-management-f3n8wb`
- `capabilities:capability-marketing-xmc539`
- `capabilities:capability-information-management-6vjgdh`
- `capabilities:capability-financial-resource-management-cd3c7c`

**Processes realizing the stream** (`process_refs`, resolving against [dea-catalog-business-processes](https://github.com/technehub-labs/dea-catalog-business-processes)):

- `processes:process-pr-build-nygvw7`
- `processes:process-fa-operate-g9zpnq`
- `processes:process-fa-operate-sdppmp`

## 7. Cross-stream links

**Upstream streams:** none recorded.

**Downstream streams:** none recorded.

## 8. Measurement

- **Member active rate** (stream-level) — Share of members with qualifying activity per period.

## 9. Evidence and admission

**Evidence sources:** SRC-013 (see [`catalog-research/evidence-register.yaml`](../../catalog-research/evidence-register.yaml)).

**Rationale:** Admitted under CR-VS-12 (population tranche; candidate VSC-062) from the CR-VS-11 industry evidence register extension. Industry-specific chain (retail-commerce); distinct from cross-industry streams by applicability (CR-VS-11 method note); cross-catalog references resolve against the sibling catalogs per the referential-integrity gate.

## 10. Provenance ladder

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-28 | Emmanuel A. Otchere, candidate universe v0.6 (CR-VS-12) |
| admitted | 2026-10-28 | Emmanuel A. Otchere, admission CR-VS-12 |

---

The record file is the canonical artifact; this README satisfies the per-entity-directory README requirement (org-wide id system IDM-007) and renders record content per the CR-VS-07 comprehensive-documentation standard. Do not edit this README by hand when the record changes — regenerate it.
