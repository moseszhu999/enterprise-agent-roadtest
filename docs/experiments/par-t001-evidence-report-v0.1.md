# PAR-T001 Evidence Report v0.1

This report records the first small calibration run for the Enterprise Agent Roadtest project.

The goal of this run is not to rank models.

The goal is to check whether PAR-T001 can distinguish a fluent but shallow procurement answer from a reviewable enterprise business recommendation.

## Roadtest under evaluation

- Roadtest: `roadtests/procurement-agent-roadtest-v0.1`
- Task: urgent procurement recommendation for 1,200 units of Optical Communication Control Board Modules
- Required output: procurement plan, supplier usage, quantity allocation, cost calculation, reasoning, risk, backup plan, approvals, stop-line risk, assumptions

## Evaluated outputs

### Output A — Lowest-price failure sample

Source:

- `roadtests/procurement-agent-roadtest-v0.1/examples/agent_output_bad_lowest_price.md`

Summary:

The output recommends Supplier A only because it has the lowest unit price and can supply the full requested quantity.

Observed behavior:

- Optimizes only for price.
- Does not calculate inventory coverage.
- Does not connect lead time to stop-line risk.
- Does not evaluate supplier reliability, quality risk, payment terms, or approval rules.
- Does not provide a backup plan.
- Does not identify required human approvals.

Score estimate:

| Dimension | Score | Notes |
|---|---:|---|
| Inventory coverage reasoning | 0/2 | No coverage calculation. |
| Delivery / stop-line risk | 0/2 | Ignores 12-day lead time vs 6-day inventory coverage. |
| Supplier reliability / quality | 0/2 | Ignores poor historical on-time rate and delay records. |
| Cost calculation | 1/2 | Calculates cheapest total cost only. |
| Supplier capacity reasoning | 1/2 | Notices Supplier A can supply all 1,200 units, but does not compare constraints. |
| Split-order reasoning | 0/2 | Rejects split ordering without risk analysis. |
| Approval / escalation | 0/2 | No approval or escalation logic. |
| Backup plan | 0/2 | None. |
| Source discipline | 2/2 | Does not invent new facts, but uses only a narrow subset. |
| Reviewability | 0/2 | Not suitable for procurement manager review. |

Estimated total: **4/20**

Failure labels:

- `PRICE_ONLY_OPTIMIZATION`
- `INVENTORY_CONTEXT_OMISSION`
- `DELIVERY_RISK_MISS`
- `SUPPLIER_HISTORY_IGNORED`
- `APPROVAL_RULE_OMISSION`
- `NO_BACKUP_PLAN`

Interpretation:

This is a useful negative control. It is fluent and numerically simple, but it fails the core enterprise-readiness requirement.

---

### Output B — Strong reference sample

Source:

- `roadtests/procurement-agent-roadtest-v0.1/examples/agent_output_good.md`

Summary:

The output recommends a split purchase: 800 units from Supplier B using expedited delivery, and 400 units from Supplier C.

Observed behavior:

- Calculates inventory coverage: 360 units / 60 units per day = 6 days.
- Identifies Supplier A's 12-day lead time as a stop-line risk.
- Uses Supplier B for urgent coverage because it can deliver in 5 days and has stronger reliability.
- Uses Supplier C for remaining quantity because Supplier B cannot supply the full 1,200 units.
- Calculates expedited cost and total cost.
- Identifies procurement manager approval and production manager confirmation.
- Provides a backup plan if Supplier B cannot confirm expedited delivery.

Score estimate:

| Dimension | Score | Notes |
|---|---:|---|
| Inventory coverage reasoning | 2/2 | Correct coverage calculation and business implication. |
| Delivery / stop-line risk | 2/2 | Correctly rejects Supplier A as main urgent supplier. |
| Supplier reliability / quality | 2/2 | Uses on-time rate and quality issue rate. |
| Cost calculation | 2/2 | Correct expedited and total cost calculation. |
| Supplier capacity reasoning | 2/2 | Handles Supplier B's 800-unit limit. |
| Split-order reasoning | 2/2 | Split order is justified by capacity and delivery risk. |
| Approval / escalation | 2/2 | Identifies procurement and production approvals. |
| Backup plan | 2/2 | Includes escalation if expedited delivery fails. |
| Source discipline | 2/2 | No unsupported supplier facts. |
| Reviewability | 2/2 | Manager-reviewable structure. |

Estimated total: **20/20**

Failure labels:

- None material in this calibration sample.

Interpretation:

This is a positive control. It demonstrates what a reviewable procurement recommendation looks like in PAR-T001.

---

### Output C — Dynamic-context stress sample

Source:

- Constructed calibration sample for `PAR-T001-DYN-A`.

Dynamic context snapshot:

```yaml
context_snapshot_id: PAR-T001-CTX-2026-06-25-A
captured_at: 2026-06-25T10:00:00Z
valid_for: PAR-T001-DYN-A only
signals:
  - supplier: Supplier C
    signal: severe weather warning in Supplier C's shipping region
    expected_delay: 2-4 days
    confidence: medium
  - supplier: Supplier B
    signal: expedited delivery route currently unaffected
    confidence: medium
  - market: emergency air freight surcharge increased
    expected_cost_impact: +8% to +15% for new expedited freight bookings
    confidence: low-to-medium
```

Constructed output behavior:

- Keeps Supplier B as the urgent base allocation.
- Reduces confidence in Supplier C normal delivery because the new weather signal may create an additional 2-4 day delay.
- Does not automatically eliminate Supplier C, because the dynamic signal is medium confidence and does not specify confirmed shipment cancellation.
- Recommends procurement manager and logistics confirmation before final PO release.
- Flags possible cost impact if emergency freight is added after the snapshot.
- Keeps the recommendation conditional rather than inventing new supplier facts.

Score estimate:

| Dimension | Score | Notes |
|---|---:|---|
| Static PAR-T001 reasoning | 17/20 | Preserves core logic, but final allocation becomes conditional. |
| Dynamic signal relevance | 2/2 | Correctly identifies Supplier C weather risk as relevant. |
| Business impact mapping | 2/2 | Maps weather delay to delivery and stop-line risk. |
| Time sensitivity | 2/2 | Treats snapshot as time-bound and asks for confirmation. |
| Source discipline | 2/2 | Does not overclaim the weather signal. |
| Human escalation | 2/2 | Requests logistics/procurement confirmation. |
| Updated recommendation quality | 1/2 | Needs a more explicit revised allocation threshold. |

Estimated dynamic total: **28/32**

Failure labels:

- `CONDITIONAL_ALLOCATION_UNDER_SPECIFIED`

Interpretation:

The dynamic layer appears useful because it creates an additional failure mode not visible in the static test: an agent may pass the original procurement task but still fail to update its recommendation when external delivery risk changes.

## Cross-output failure pattern summary

The first calibration run shows three separable output types:

1. **Fluent but shallow optimizer**
   - Picks lowest price.
   - Produces a clean-looking answer.
   - Fails hidden enterprise constraints.

2. **Static enterprise-ready recommender**
   - Reads all supplied inputs.
   - Produces a reviewable recommendation.
   - Handles cost, capacity, risk, and approvals.

3. **Dynamic risk-aware recommender**
   - Preserves the static business logic.
   - Updates risk assessment using a time-bound context snapshot.
   - Avoids overclaiming external signals.
   - Escalates uncertain dynamic changes to humans.

## Current evidence claim

Allowed claim:

> In this calibration run, PAR-T001 distinguishes a lowest-price procurement answer from a reviewable procurement recommendation that accounts for inventory coverage, delivery risk, supplier capacity, supplier history, cost calculation, approval rules, and backup planning.

Allowed dynamic-context claim:

> A dynamic context snapshot can add a second layer of evaluation by testing whether an agent updates business risk reasoning when external logistics conditions change.

Disallowed claim:

> Model X is better than Model Y at procurement.

No live third-party model comparison has been completed in this report.

## Recommended next action

Create a formal `PAR-T001-DYN-A` roadtest package with:

1. `dynamic_context_snapshot.md`
2. `agent_task_prompt_dynamic.md`
3. `reference_answer_dynamic.md`
4. `dynamic_scoring_rubric.md`
5. `examples/agent_output_dynamic_overclaim.md`
6. `examples/agent_output_dynamic_good.md`

After that, run at least two real external agent outputs and score them using the same rubric.
