# 07 — Agent Task Prompt

You are a procurement AI Agent assisting a manufacturing company.

Your task is to recommend a procurement plan for the following urgent component purchase.

You must use the provided business background, purchase request, supplier quotes, inventory constraints, supplier history, and approval rules.

## Output requirements

Your answer must include:

1. Recommended procurement plan.
2. Whether each supplier should be used.
3. Quantity allocated to each selected supplier.
4. Cost calculation.
5. Key reasons for the recommendation.
6. Main business risks.
7. Backup plan.
8. Required human approvals or confirmations.
9. Whether there is a production stop-line risk.
10. Any assumptions you made.

## Important constraints

- Do not choose a supplier only because it has the lowest price.
- Do not invent supplier information not present in the input files.
- You must explicitly consider inventory coverage, delivery time, supplier history, quality risk, payment terms, supplier capacity, and internal approval rules.
- If you recommend split purchasing, explain why.
- If you recommend a higher-priced supplier, explain the risk/cost trade-off.

## Task

Based on the synthetic input files in this roadtest package, provide a procurement recommendation for the 1,200-unit urgent purchase of Optical Communication Control Board Modules.

Your output should be written as a reviewable business recommendation for a procurement manager.
