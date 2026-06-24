# Enterprise Agent Roadtest

Business roadtests for evaluating whether AI agents can handle real enterprise workflows before PoC, customer demos, or deployment.

## Core idea

Many AI agent demos are clean. Real enterprise work is not.

A procurement agent should not simply choose the cheapest supplier. It must reason about inventory pressure, delivery risk, payment terms, supplier history, quality risk, approval rules, backup plans, and human escalation points.

This repository explores a simple question:

> Can an AI agent pass a realistic business roadtest before being shown to customers?

## What this is

This is a research-style evaluation lab for enterprise AI agents.

It provides synthetic business tasks, input files, reference answers, scoring rubrics, failure taxonomies, sample agent outputs, and report templates.

The first public roadtest is:

- `roadtests/procurement-agent-roadtest-v0.1` — urgent supplier selection for a manufacturing procurement agent.

## Framework docs

The repository is now organized around a broader readiness-evidence idea, not only one procurement task.

- `docs/agent-readiness-framework.md` — readiness dimensions for enterprise AI agents.
- `docs/governance-failure-taxonomy.md` — governance-level failure labels beyond one scenario.
- `docs/evidence-layer.md` — why synthetic roadtests can provide pre-PoC readiness evidence without requiring customer data.
- `docs/privacy.md` — privacy-first design principles.
- `docs/positioning.md` — project positioning.
- `docs/roadmap.md` — planned development path.

## What this is not

This is not a generic benchmark of model intelligence.

It is not a chatbot demo.

It is not a replacement for enterprise acceptance testing.

It is a practical roadtest format for checking whether an AI agent can produce a reviewable business recommendation under messy constraints.

## Privacy-first design

The public roadtests use synthetic enterprise data.

Users do not need to upload real procurement data, contracts, ERP exports, supplier lists, or customer records.

The intended flow is:

1. Copy the synthetic roadtest task.
2. Run it in your own AI agent environment.
3. Paste or save only the agent's output.
4. Score the output using the rubric or helper script.
5. Produce a readiness report.

See `docs/privacy.md` for details.

## Quick start

Open the first roadtest:

```bash
cd roadtests/procurement-agent-roadtest-v0.1
```

Read the task prompt:

```bash
cat 07_agent_task_prompt.md
```

Run your AI agent with the task and supporting files.

Save the agent output as:

```bash
agent_output.md
```

Run the helper scorer:

```bash
python tools/evaluate_agent_output.py agent_output.md
```

You can also test the bundled examples:

```bash
python tools/evaluate_agent_output.py examples/agent_output_bad_lowest_price.md
python tools/evaluate_agent_output.py examples/agent_output_good.md
```

## Roadtest philosophy

A useful enterprise agent should be able to:

- read all relevant inputs;
- identify hidden constraints;
- avoid shallow optimization;
- reason about business risk;
- identify approval and escalation points;
- produce a reviewable recommendation;
- avoid inventing facts not present in the input.

## Current status

This repository is at v0.1.

It is intentionally small. The goal is to make one hard, clear, inspectable roadtest before expanding into more scenarios.

The project now separates three layers:

1. Concrete roadtest assets.
2. Readiness framework and failure taxonomy.
3. Evidence-layer explanation for PoC and governance use cases.

## Planned roadtests

Possible future roadtests include:

- inventory exception handling;
- logistics delay escalation;
- purchase order discrepancy review;
- invoice reconciliation;
- customer service escalation;
- contract clause risk triage.

## License

MIT License for the public sample materials and helper scripts.

Commercial task packs, private evaluations, customer-specific reports, and proprietary failure datasets are not included in this public repository.
