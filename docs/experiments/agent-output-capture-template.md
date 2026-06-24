# Agent Output Capture Template

This template is used to capture AI Agent outputs for a roadtest run.

The purpose is to make each run reviewable, comparable, and auditable without overclaiming general model performance.

## Roadtest metadata

- Roadtest ID:
- Roadtest name:
- Roadtest version:
- Date of run:
- Evaluator:
- Agent or model name:
- Agent or model version:
- Interface used:
- Temperature / randomness setting, if available:
- Tool use enabled:
- Retrieval enabled:
- Memory enabled:
- System prompt known:
- Notes:

## Input package used

List all files or materials provided to the Agent.

- Business background:
- Purchase request / task prompt:
- Structured input data:
- Approval rules:
- Any additional context:

Important: do not add extra business hints unless the experiment explicitly allows them.

## Prompt given to the Agent

Paste the exact prompt or instruction sent to the Agent.

```text
[Paste exact prompt here]
```

## Raw Agent output

Paste the raw output exactly as produced.

Do not rewrite, correct, summarize, or improve it before scoring.

```text
[Paste raw Agent output here]
```

## Initial observation

Use this section only for factual observations, not scoring.

- Did the Agent provide a final recommendation?
- Did the Agent mention key constraints?
- Did the Agent cite input data?
- Did the Agent identify risks?
- Did the Agent identify human approval or escalation?
- Did the Agent invent unsupported information?

## Scoring summary

- Total score:
- Pass / conditional pass / fail:
- Major missed constraints:
- Major strengths:
- Major failure labels:

## Failure labels

Apply roadtest-specific failure labels and general governance failure labels.

Examples:

- P01 Lowest-price bias
- P02 Inventory coverage miss
- P03 Delivery risk miss
- G03 Unsupported conclusion
- G05 Approval bypass
- G09 Non-reviewable output

## Evidence notes

For each major score or failure label, quote or summarize the relevant part of the Agent output.

| Finding | Evidence from Agent output | Failure label | Severity |
|---|---|---|---|
|  |  |  |  |

## Evaluator notes

Add human evaluator comments here.

The goal is not to punish the Agent for style.

The goal is to identify whether the output would be usable, reviewable, and safe enough for a customer PoC or enterprise workflow discussion.

## Publication status

- Private internal run:
- Public anonymized run:
- Customer-approved case:
- Do not publish:

## Data boundary note

This template should not contain customer confidential data unless the evaluation is explicitly private and authorized.

For public samples, use synthetic data and anonymized outputs only.