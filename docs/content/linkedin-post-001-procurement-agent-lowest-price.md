# LinkedIn Post 001: A procurement AI Agent cannot just choose the lowest price

Most AI Agent demos are too clean.

A procurement Agent that only chooses the lowest price cannot be deployed in a real enterprise workflow.

Real procurement decisions include price, delivery time, inventory pressure, supplier history, quality risk, payment terms, approval rules, and fallback options.

In a simple demo, the Agent may be asked:

> Which supplier should we choose?

But in a real PoC, the task should look more like this:

- Current inventory can support only 6 days of production.
- The customer delivery deadline is 14 days away.
- Supplier A is the cheapest, but delivery takes 12 days and its historical on-time rate is low.
- Supplier B is more expensive, but can deliver urgently in 5 days and has a strong delivery record.
- Supplier C is in the middle, but cannot fully solve the supply gap alone.
- The total purchase amount triggers manager approval.
- Split purchasing requires a business justification.

If the Agent simply says:

> Choose Supplier A because it is cheapest.

Then the Agent did not pass the business roadtest.

This is why I am building **Enterprise Agent Roadtest**.

The idea is simple:

Do not only ask whether an AI Agent can answer.

Ask whether it can survive a realistic enterprise task with messy constraints, risk trade-offs, approval rules, and reviewable evidence.

The first public sample is a procurement Agent roadtest:

**PAR-T001: Urgent Supplier Selection**

It includes synthetic business data, supplier quotes, inventory constraints, approval rules, a reference answer, a scoring rubric, failure taxonomy, and an evaluation report template.

No customer business data is required.

The goal is not to build another Agent.

The goal is to test whether an Agent is ready for enterprise PoC, customer demo, or deployment.

Repository:
https://github.com/moseszhu999/enterprise-agent-roadtest
