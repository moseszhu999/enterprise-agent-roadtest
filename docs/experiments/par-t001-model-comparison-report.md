# PAR-T001 Model Comparison Report Template

This document is a template for comparing how different AI agents or models perform on the same synthetic enterprise roadtest.

The goal is not to rank general model intelligence.

The goal is to observe whether an agent can survive a specific enterprise task with business constraints, risk trade-offs, approval rules, and human review requirements.

## Roadtest

- Roadtest ID: PAR-T001
- Roadtest name: Urgent Procurement Supplier Selection
- Domain: Procurement / supply chain
- Data type: Synthetic enterprise data
- Customer data required: No
- Evaluation mode: Agent output only

## Evaluation Principle

This report should avoid broad claims such as:

- Model A is better than Model B.
- Model X is unsafe.
- Model Y cannot do procurement.

Use narrower, evidence-based language:

- In PAR-T001, Agent A identified the inventory coverage risk.
- In PAR-T001, Agent B selected the lowest-price supplier but missed the delivery constraint.
- In PAR-T001, Agent C produced a fluent answer but did not identify approval requirements.

## Models or Agents Tested

| Run ID | Model / Agent | Version / Date | Run Environment | Notes |
|---|---|---|---|---|
| RUN-001 | TBD | TBD | TBD | TBD |
| RUN-002 | TBD | TBD | TBD | TBD |
| RUN-003 | TBD | TBD | TBD | TBD |

## Required Output Checks

Each output should be checked against the following core questions:

1. Did the agent understand that the task is not simple price ranking?
2. Did the agent calculate or infer inventory coverage pressure?
3. Did the agent recognize that Supplier A is risky despite the lowest unit price?
4. Did the agent consider expedited delivery from Supplier B?
5. Did the agent consider split ordering or capacity limits?
6. Did the agent identify approval requirements?
7. Did the agent state risks and fallback options?
8. Did the agent avoid hallucinating unsupported facts?
9. Did the agent produce a human-reviewable recommendation?

## Score Summary

| Run ID | Score | Readiness Band | Key Strength | Key Failure |
|---|---:|---|---|---|
| RUN-001 | TBD / 100 | TBD | TBD | TBD |
| RUN-002 | TBD / 100 | TBD | TBD | TBD |
| RUN-003 | TBD / 100 | TBD | TBD | TBD |

Suggested readiness bands:

- 85–100: Strong for this roadtest, subject to human review.
- 70–84: Promising but requires improvement before customer PoC.
- 50–69: Not ready for enterprise PoC on this task.
- Below 50: High risk; fails core business constraints.

## Per-Run Evaluation

### RUN-001

#### Agent Output Summary

TBD.

#### Score

TBD / 100.

#### Strengths

- TBD

#### Failure Types

- TBD

#### Evidence Notes

- TBD

#### PoC Readiness Judgment

TBD.

---

### RUN-002

#### Agent Output Summary

TBD.

#### Score

TBD / 100.

#### Strengths

- TBD

#### Failure Types

- TBD

#### Evidence Notes

- TBD

#### PoC Readiness Judgment

TBD.

---

### RUN-003

#### Agent Output Summary

TBD.

#### Score

TBD / 100.

#### Strengths

- TBD

#### Failure Types

- TBD

#### Evidence Notes

- TBD

#### PoC Readiness Judgment

TBD.

## Cross-Run Observations

Use this section to identify repeated patterns.

Examples:

- Multiple agents produced fluent recommendations without calculating inventory coverage.
- Some agents identified delivery risk but failed to identify approval rules.
- Some agents correctly rejected the lowest-price supplier but did not provide a fallback plan.
- Some agents gave a useful recommendation but did not make the output audit-friendly.

## What This Report Can Support

This report can support:

- internal PoC readiness discussions,
- agent improvement planning,
- sales engineering preparation,
- business workflow evaluation design,
- AI governance conversations around evidence and accountability.

This report should not be used as:

- a formal audit,
- a certification,
- a general-purpose model benchmark,
- proof that an agent is safe for production deployment.

## Interpretation

A business roadtest is not a final answer.

It is a structured way to expose whether an AI Agent can handle a messy enterprise task before it is shown to customers, connected to workflows, or trusted with operational recommendations.

Demo shows what an Agent can say.

Roadtest shows what it can survive.
