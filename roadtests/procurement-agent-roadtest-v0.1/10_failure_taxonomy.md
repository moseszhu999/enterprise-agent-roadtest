# 10 — Failure Taxonomy v0.1

This taxonomy labels common failures in procurement AI Agent outputs.

| Code | Failure Type | Description | Severity |
|---|---|---|---|
| P01 | Lowest-price bias | Chooses the cheapest supplier without evaluating risk. | Critical |
| P02 | Inventory coverage ignored | Fails to calculate or use inventory coverage days. | Critical |
| P03 | Lead-time risk ignored | Does not compare supplier lead time against inventory coverage. | Critical |
| P04 | Supplier history ignored | Ignores on-time rate or recent delay records. | High |
| P05 | Quality risk ignored | Ignores supplier quality issue rates. | Medium |
| P06 | Payment terms ignored | Ignores prepayment or cash-flow impact. | Medium |
| P07 | Approval rules ignored | Misses required manager/finance/production approvals. | Critical |
| P08 | No split-purchase reasoning | Uses or rejects split purchasing without explaining why. | High |
| P09 | No backup plan | Does not provide contingency plan. | Medium |
| P10 | Fabricated information | Invents supplier facts not present in the input. | Critical |
| P11 | Unreviewable output | Output is too vague for business review. | High |
| P12 | Cost-risk tradeoff missing | Does not explain why higher cost may be justified. | High |

The taxonomy is intended to grow over time as more Agent outputs are evaluated.
