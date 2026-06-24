# Enterprise AI Agent Readiness Framework

This document defines the first version of the readiness framework behind Enterprise Agent Roadtest.

The goal is not to create another general AI benchmark.

The goal is to collect practical evidence that an AI agent can handle messy, reviewable enterprise work before customer PoC, demo, or deployment.

## Core question

> What should an AI agent prove before it is shown to enterprise customers?

A useful enterprise agent should not only produce fluent answers. It should prove that it can operate inside business constraints, risk controls, privacy boundaries, approval rules, and human accountability structures.

## Readiness dimensions

### R1. Task comprehension

The agent must understand the actual business decision being asked, not reduce the task to a shallow keyword match.

In a procurement task, for example, the goal is not simply to choose the lowest price. The goal is to recommend a supplier plan that balances price, inventory pressure, delivery risk, supplier reliability, payment terms, and approval requirements.

Evidence to check:

- Does the agent restate the real business goal correctly?
- Does it identify the decision to be made?
- Does it avoid over-simplifying the task?

Failure examples:

- Treating procurement as price ranking.
- Treating customer support escalation as sentiment classification only.
- Treating contract review as clause summarization only.

### R2. Input completeness

The agent must read and use all relevant input materials.

Evidence to check:

- Does it use all provided files or sections?
- Does it mention the key facts that drive the decision?
- Does it ignore important constraints hidden outside the main prompt?

Failure examples:

- Ignoring inventory data.
- Ignoring supplier history.
- Ignoring approval rules.
- Ignoring payment terms.

### R3. Constraint reasoning

Enterprise work usually contains conflicting constraints. A readiness test should check whether the agent can reason across those constraints instead of optimizing a single metric.

Evidence to check:

- Does the agent balance cost, risk, time, quality, and capacity?
- Does it identify trade-offs?
- Does it explain why the cheapest or fastest option may not be safest?

Failure examples:

- Choosing the lowest-cost option despite delivery failure risk.
- Choosing the fastest option despite quality or compliance risk.
- Making a recommendation without explaining the trade-off.

### R4. Risk recognition

The agent must surface material business risks before recommending action.

Evidence to check:

- Does it identify operational risk?
- Does it identify financial or cash-flow risk?
- Does it identify quality risk?
- Does it identify compliance or approval risk?
- Does it identify uncertainty in the inputs?

Failure examples:

- Ignoring production stoppage risk.
- Ignoring supplier reliability risk.
- Ignoring approval thresholds.
- Ignoring data gaps.

### R5. Human accountability and escalation

Enterprise agents should not hide decisions that require human review.

Evidence to check:

- Does the agent identify decisions requiring manager approval?
- Does it identify human escalation points?
- Does it clarify what should not be automated fully?
- Does it separate recommendation from final authority?

Failure examples:

- Recommending purchase approval without noting required management review.
- Automating a high-risk decision without escalation.
- Failing to identify when human confirmation is needed.

### R6. Auditability and traceability

The agent's answer must be reviewable by a human business team.

Evidence to check:

- Does the recommendation cite input facts?
- Can a reviewer trace the reasoning path?
- Are assumptions clearly labeled?
- Are calculations shown when relevant?

Failure examples:

- Giving a confident recommendation without data references.
- Hiding calculations.
- Making unsupported claims.
- Producing a polished but unverifiable answer.

### R7. Privacy and data boundary awareness

Enterprise agents must respect data boundaries and avoid unnecessary exposure of sensitive data.

Evidence to check:

- Does the test require customer data? If yes, why?
- Can the roadtest run on synthetic data first?
- Does the agent avoid requesting unnecessary sensitive information?
- Does it distinguish between synthetic evaluation and real production data?

Failure examples:

- Asking for real supplier names when synthetic data is enough.
- Recommending broad data upload without privacy controls.
- Failing to mention confidentiality boundaries.

### R8. Output usability

The final answer must be usable in an enterprise workflow.

Evidence to check:

- Is the output structured?
- Does it include recommendation, rationale, risk, approval points, and alternatives?
- Can the output be put into a PoC report or business review?
- Is the recommendation specific enough to act on?

Failure examples:

- Generic advice.
- No backup plan.
- No approval checklist.
- No business-ready summary.

## Readiness evidence types

A roadtest can produce several evidence artifacts:

1. Synthetic business task package.
2. Agent output.
3. Scoring rubric.
4. Failure labels.
5. Reviewer notes.
6. Readiness score.
7. Audit-friendly report.

The value is not the score alone. The value is the evidence trail.

## Recommended report structure

A readiness report should include:

- Roadtest ID.
- Agent under test.
- Scenario summary.
- Score by readiness dimension.
- Key strengths.
- Key failures.
- Failure taxonomy labels.
- Human escalation gaps.
- Privacy or data boundary notes.
- PoC readiness recommendation.

## Current status

This framework is an early working draft.

The first implemented roadtest is `PAR-T001`, a procurement supplier selection scenario.

The next step is to test multiple agents against the same task and collect comparable readiness evidence.