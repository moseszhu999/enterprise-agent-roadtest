# PAR-T001 Model Runbook

This runbook defines how to test multiple AI Agents or models on the same procurement roadtest.

## Goal

The goal is to compare whether an AI Agent can handle a realistic procurement decision under inventory, delivery, supplier-risk, payment, and approval constraints.

This is not a benchmark of general intelligence.

It is a business-readiness roadtest for enterprise PoC or demo scenarios.

## Roadtest

Roadtest ID: `PAR-T001`

Roadtest name: Urgent Supplier Selection

Location:

```text
roadtests/procurement-agent-roadtest-v0.1/
```

## Test protocol

For each model or Agent:

1. Open `07_agent_task_prompt.md`.
2. Provide the Agent with the task prompt and all required input files.
3. Do not add extra hints.
4. Ask the Agent to produce a procurement recommendation.
5. Save the raw Agent output.
6. Score the output using `tools/evaluate_agent_output.py`.
7. Manually review the score against `09_scoring_rubric.md`.
8. Record failure types from `10_failure_taxonomy.md`.
9. Produce an evaluation report using `11_evaluation_report_template.md`.

## Suggested output folder

```text
experiments/par-t001/YYYY-MM-DD-model-name/
  agent_output.md
  auto_score.json
  manual_review.md
  final_report.md
```

## Models or Agents to test

Suggested initial set:

```text
ChatGPT
Claude
Gemini
DeepSeek
Any customer or internal procurement Agent
```

If testing commercial models, record model names and dates clearly because model behavior changes over time.

## What to look for

The most important question is not whether the output sounds fluent.

The key question is whether the Agent identifies the operational constraint:

> Inventory supports only 6 days of production, so the cheapest supplier with a 12-day lead time creates a production-stop risk.

A strong answer should:

- Avoid choosing Supplier A only because it is cheapest.
- Recognize Supplier B's urgent delivery option.
- Recognize Supplier B's capacity limit.
- Use Supplier C as a complementary supplier if needed.
- Identify manager approval due to total amount.
- Identify production-manager confirmation due to line-stop risk.
- Explain split purchasing.
- Avoid hallucinating unavailable facts.

## Manual review notes

The automatic scoring script is only an initial screen.

Final evaluation should include human review, because enterprise-readiness depends on reasoning quality, decision justification, and whether the recommendation is reviewable by a business manager.

## Failure labels

Use the failure taxonomy:

```text
P01 Lowest-price trap
P02 Inventory coverage omission
P03 Lead-time risk omission
P04 Supplier-history omission
P05 Quality-risk omission
P06 Payment-term omission
P07 Approval-rule omission
P08 No split-purchase rationale
P09 No fallback option
P10 Hallucinated input facts
P11 Non-actionable output
P12 Cost-optimal vs risk-optimal confusion
```

## Comparison table template

| Model / Agent | Date | Score | Main failures | PoC readiness |
|---|---:|---:|---|---|
| Model A | YYYY-MM-DD | TBD | TBD | TBD |
| Model B | YYYY-MM-DD | TBD | TBD | TBD |
| Model C | YYYY-MM-DD | TBD | TBD | TBD |

Keep notes concise. Put detailed review in each model's experiment folder.

## Public communication rule

When publishing results, avoid overstating model quality from one task.

This roadtest shows behavior on one procurement scenario only.

Do not claim broad model rankings unless multiple tasks and repeated runs are available.

A safe public wording is:

> In PAR-T001, the Agent failed to identify the inventory and lead-time risk.

Avoid:

> Model X is bad at procurement.

## Next step

Run the same roadtest on at least three Agents or models and create a short comparison note:

```text
Procurement AI Agent Roadtest: Fluent answers are not enough.
```
