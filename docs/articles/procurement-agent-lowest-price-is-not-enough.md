# A procurement AI Agent cannot just choose the lowest price

## Thesis

A procurement AI Agent that only chooses the lowest-price supplier is not ready for enterprise use.

Enterprise procurement is not a price-sorting problem. It is a constrained decision task involving delivery risk, inventory pressure, supplier reliability, quality history, payment terms, approval rules, and operational fallback planning.

This is why an enterprise AI Agent should be tested with a business roadtest before PoC, customer demo, or deployment.

## The clean demo problem

Most AI Agent demos are too clean.

A demo task may ask:

> We have three suppliers. Which one should we choose?

A model can easily produce a fluent answer. But fluency is not the same as enterprise readiness.

In real work, the question is rarely that simple.

## A more realistic procurement task

In `PAR-T001: Urgent Supplier Selection`, the Agent receives a synthetic but realistic procurement scenario:

- A manufacturing company needs 1,200 units of a critical component.
- Current inventory is 360 units.
- Daily consumption is 60 units.
- The inventory can support only 6 days of production.
- The customer delivery deadline is 14 days away.
- Supplier A has the lowest price but requires 12 days and has weak delivery history.
- Supplier B is more expensive but can deliver urgently in 5 days and has the strongest reliability.
- Supplier C has a middle price and moderate delivery risk.
- The total purchase amount may trigger manager approval.
- Prepayment may trigger finance approval.
- Split purchasing requires justification.

A real procurement Agent should not simply choose the cheapest supplier.

It should identify the operational risk:

> If the company waits 12 days for the cheapest supplier, production may stop after day 6.

## What the roadtest checks

The roadtest checks whether the Agent can handle:

1. Inventory coverage calculation
2. Delivery-time risk
3. Supplier reliability history
4. Quality risk
5. Payment-term implications
6. Approval-rule detection
7. Split-purchase justification
8. Fallback planning
9. Evidence-based reporting
10. Avoiding hallucinated business facts

The target output is not a chatbot answer. It is a reviewable business recommendation.

## Example failure

A failing Agent may say:

> Choose Supplier A because it is the cheapest and can supply all 1,200 units.

This answer is fluent, but it misses the core risk.

Supplier A's delivery time is 12 days. The company has only 6 days of inventory coverage. The recommendation may create a production-stop risk.

That is not enterprise-ready behavior.

## Why this matters

AI Agent companies, AI consultants, and enterprise AI teams often need to show a PoC to customers.

But a customer demo should not only prove that the Agent can talk.

It should prove that the Agent can survive messy business constraints and produce a decision that a human manager can review.

That is the purpose of Enterprise Agent Roadtest.

## Privacy-first design

The public roadtest uses synthetic enterprise data.

Users do not need to upload real procurement data, contracts, ERP exports, supplier lists, or customer records.

The basic workflow is:

1. Copy the synthetic roadtest task.
2. Run it in your own Agent environment.
3. Paste or save the Agent output.
4. Evaluate the output against the scoring rubric.
5. Generate a readiness report.

## Product direction

The goal is not to build another Agent.

The goal is to build roadtests that answer a different question:

> Is this Agent ready for an enterprise PoC, customer demo, or deployment?

The first sample focuses on procurement.

Future roadtests may cover inventory exception handling, logistics delay response, customer-service escalation, contract review, and enterprise document workflows.
