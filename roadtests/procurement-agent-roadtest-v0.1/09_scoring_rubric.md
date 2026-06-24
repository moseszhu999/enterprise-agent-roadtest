# 09 — Scoring Rubric

Total score: **100 points**

## 1. Task understanding — 10 points

Full score if the Agent understands this is an urgent procurement decision, not a simple price comparison.

Major deduction if the Agent treats the task as choosing the lowest price.

## 2. Input reading completeness — 15 points

The Agent should use inventory, daily consumption, customer deadline, required quantity, supplier prices, lead time, supplier capacity, historical on-time rate, quality issue rate, payment terms, and approval rules.

Major deduction if inventory or daily consumption is ignored.

## 3. Inventory and lead-time risk — 20 points

The Agent must calculate or clearly identify:

```text
360 units / 60 units per day = 6 days of inventory coverage
```

It must recognize Supplier A's 12-day lead time creates stop-line risk and Supplier B's 5-day expedited delivery can reduce stop-line risk.

## 4. Price analysis — 10 points

The Agent should correctly explain Supplier A is cheapest but risky, Supplier B expedited is more expensive but safer, and Supplier C is a reasonable supplementary supplier.

Full score requires cost calculation.

## 5. Supplier history and quality risk — 15 points

The Agent should consider Supplier A's low on-time rate and delays, Supplier B's best delivery and quality history, and Supplier C's medium risk.

## 6. Payment terms and cash-flow impact — 10 points

The Agent should identify Supplier A requires 30% prepayment, Supplier B has the most favorable payment term, and Supplier C has medium payment terms.

## 7. Approval requirements — 10 points

The Agent must identify total amount exceeds 100,000 CNY, procurement manager approval is required, production manager confirmation is required due to stop-line risk, split purchasing needs explanation, and prepayment would require finance approval if Supplier A were used.

## 8. Recommendation quality — 5 points

The best recommendation is close to:

```text
Supplier B expedited 800 units + Supplier C 400 units
```

Choosing Supplier A as the main supplier should receive a major deduction.

## 9. Report reviewability — 5 points

The output should be readable by a procurement manager and include data references, risk explanation, approval items, backup plan, and no invented facts.

## Passing threshold

| Score | Meaning |
|---:|---|
| 85–100 | Strong. Ready for customer PoC discussion. |
| 70–84 | Usable with improvements. Needs review. |
| 50–69 | Weak. Not ready for enterprise PoC. |
| 0–49 | Fails the roadtest. |
