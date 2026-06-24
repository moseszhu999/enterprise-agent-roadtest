# Evaluation Report — Bad Example

| Field | Value |
|---|---|
| Roadtest ID | PAR-T001 |
| Tested output | examples/agent_output_bad_lowest_price.md |
| Total score | 32 / 100 |
| Conclusion | Fails the roadtest |

## Major failures

- P01 Lowest-price bias
- P02 Inventory coverage ignored
- P03 Lead-time risk ignored
- P04 Supplier history ignored
- P07 Approval rules ignored
- P08 No split-purchase reasoning
- P09 No backup plan
- P12 Cost-risk tradeoff missing

## Summary

The Agent selected Supplier A only because it had the lowest price and could supply all units.

The output ignored the most important business constraint: current inventory only covers 6 days, while Supplier A requires 12 days to deliver.

This output is not suitable for enterprise procurement PoC use.
