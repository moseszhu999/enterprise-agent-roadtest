# Roadtest Methodology

Enterprise Agent Roadtest is not intended to be a general AI benchmark.

It is a method for creating small, realistic, synthetic business tasks that test whether an AI Agent is ready for customer PoC, enterprise demo, or limited workflow deployment.

The goal is not to ask whether an Agent can produce a fluent answer.

The goal is to test whether the Agent can survive a messy business situation with constraints, risks, approvals, and human review requirements.

## Core idea

A demo shows what an Agent can say.

A roadtest shows what it can survive.

A roadtest should create enough business friction that shallow answers fail.

Examples of friction:

- cheapest option is not the safest option
- fastest option has capacity or quality risk
- automation is blocked by approval rules
- input files contain conflicting constraints
- missing a human escalation point creates operational risk
- a confident answer without evidence is not reviewable

## What a roadtest must contain

Each roadtest should include the following components:

1. Synthetic business context
2. Structured input data
3. Explicit business task
4. Hidden or non-obvious risk trade-off
5. Human approval or escalation rule
6. Reference answer
7. Scoring rubric
8. Failure taxonomy
9. Example Agent outputs
10. Evaluation report template

## Synthetic first

The default roadtest design uses synthetic enterprise data.

This is intentional.

The purpose is to test Agent behavior without requiring customer data, supplier records, ERP exports, contracts, personal information, or confidential business documents.

Synthetic first does not mean unrealistic.

A good synthetic roadtest should be realistic enough to expose failure modes while safe enough to share publicly or use in early PoC discussions.

## Roadtest design principles

### 1. Make the failure mode concrete

A roadtest should not test vague intelligence.

It should test a specific enterprise failure mode.

For example:

- procurement Agent chooses the lowest price and misses delivery risk
- logistics Agent selects the fastest route and ignores customs delay
- finance Agent approves a payment without checking invoice mismatch
- customer support Agent escalates too late because it misses severity signals

### 2. Require multi-constraint reasoning

Enterprise tasks rarely have one objective.

A good roadtest should force the Agent to reason across multiple constraints:

- cost
- time
- inventory
- capacity
- quality
- payment terms
- approval limits
- risk history
- human accountability

### 3. Make the answer reviewable

The Agent output should be judged not only by the final recommendation, but by whether a human can review it.

A reviewable answer should:

- cite relevant input facts
- explain trade-offs
- identify risks
- mark approval points
- avoid unsupported claims
- avoid hallucinated evidence
- provide fallback options

### 4. Separate automation from accountability

A strong Agent should know when not to fully automate.

Roadtests should check whether the Agent can identify when human approval, escalation, or review is required.

This is especially important for enterprise workflows where accountability remains with humans or organizations.

### 5. Score failure patterns, not only final answers

A roadtest should not only produce a score.

It should identify failure types.

For example:

- shallow optimization
- missing critical constraint
- unsupported conclusion
- approval bypass
- non-reviewable output
- hallucinated evidence
- missing fallback plan

Failure labels are more valuable over time than a single numeric score.

## Roadtest lifecycle

### Stage 1: Public sample

A small synthetic roadtest is published publicly to make the method inspectable.

Purpose:

- demonstrate the idea
- invite critique
- create a shared vocabulary
- avoid overclaiming

### Stage 2: Model run

The same task is run against several AI Agents or models.

The comparison should avoid broad claims such as "Model A is better than Model B".

It should only state task-specific findings.

Example:

> In PAR-T001, Agent X identified the inventory coverage risk but failed to identify the procurement approval rule.

### Stage 3: Failure labeling

Outputs are labeled using a failure taxonomy.

The goal is to build a dataset of realistic enterprise Agent failure patterns.

### Stage 4: Human calibration

Human reviewers compare the scoring result with business judgment.

The rubric is adjusted when needed.

### Stage 5: Private or customer-specific roadtests

For serious PoC work, the roadtest can be customized.

Customer data is not required by default. If customer-specific data is used, it should be anonymized, minimized, or evaluated in a private environment.

## What this methodology does not claim

This methodology does not claim to certify AI systems.

It does not replace security audits, compliance reviews, legal review, formal AI governance frameworks, or domain expert approval.

It is a lightweight readiness evidence layer for pre-PoC and early enterprise evaluation.

## Why this matters

Enterprise AI Agent adoption will not depend only on model capability.

It will depend on whether teams can create evidence that an Agent is ready for messy, reviewable, accountable business work.

That is the gap this methodology is trying to explore.