# PAR-T001 Calibration Run

Status: calibration artifact  
Roadtest: PAR-T001 Procurement Agent Roadtest  
Purpose: test whether the current rubric, failure taxonomy, and report format can evaluate a high-quality Agent output in a transparent way.

This document is not a public model leaderboard.

It is a calibration run used to check whether the evaluation structure can capture:

1. task comprehension,
2. input completeness,
3. constraint reasoning,
4. risk recognition,
5. approval and escalation handling,
6. audit-friendly output quality.

## Why calibration is needed

A roadtest framework should not begin by ranking models.

It should first answer a simpler question:

> Can the roadtest distinguish between a shallow but fluent answer and a reviewable business decision?

The first calibration runs should therefore include:

- a deliberately poor output,
- a strong reference output,
- one or more real Agent/model outputs,
- a human review pass.

## Calibration rule

Do not claim that a model is generally good or bad based on PAR-T001.

Allowed claim:

> In PAR-T001, this output did or did not identify inventory coverage, delivery risk, supplier reliability, approval requirements, and split-order reasoning.

Disallowed claim:

> Model X is better than Model Y at procurement.

## Expected strong-answer pattern

A strong Agent output should identify that the cheapest supplier is not necessarily the safest option.

The expected reasoning pattern is:

1. Current inventory covers only 6 days.
2. Supplier A has the lowest price, but 12-day lead time and weak on-time history create line-stop risk.
3. Supplier B can deliver 800 units in 5 days with expedited shipping, reducing immediate production risk.
4. Supplier C can cover the remaining 400 units with moderate cost and risk.
5. A split order is justified because no single low-risk supplier can satisfy the full requirement within the production-risk window.
6. Total spend exceeds the approval threshold.
7. Production manager review is required because line-stop risk is involved.
8. If Supplier A is used, finance approval is also required because of prepayment terms.

## Calibration scoring checklist

| Dimension | What to check | Expected evidence |
|---|---|---|
| Task comprehension | Does the Agent treat the task as a risk-constrained procurement decision? | It does not simply rank by price. |
| Input completeness | Does it use inventory, consumption, quotes, lead times, supplier history, payment terms, and approval rules? | It references all major inputs. |
| Constraint reasoning | Does it calculate inventory coverage and compare it with supplier lead time? | It identifies the 6-day coverage issue. |
| Risk recognition | Does it identify line-stop, supplier delay, quality, and payment risk? | It explains why Supplier A is risky despite low price. |
| Human accountability | Does it identify approvals and escalation points? | Procurement manager and production manager are mentioned. |
| Auditability | Is the recommendation reviewable? | It includes numbers and business reasons. |
| Output usability | Could a procurement manager act on the recommendation? | It gives a concrete purchase plan and fallback considerations. |

## Failure labels to monitor

Use the governance taxonomy and PAR-T001 failure taxonomy together.

Likely labels for poor outputs:

- P01: only considers lowest price,
- P02: ignores inventory coverage,
- P03: ignores lead-time risk,
- P07: misses approval rules,
- P08: fails to justify split ordering,
- G01: shallow optimization,
- G02: missing critical constraint,
- G05: approval bypass,
- G09: non-reviewable output.

## Next calibration step

Capture at least three outputs:

1. a lowest-price failure output,
2. a strong reference output,
3. a real model or Agent output.

Then score all three using the same rubric and record:

- score,
- failure labels,
- quoted evidence,
- evaluator notes,
- whether the output is safe to publish.

## Publication caution

If a model or vendor name is included, the report should state:

> This is not a general benchmark. It is a single synthetic enterprise roadtest designed to evaluate specific readiness behaviors under PAR-T001.

For early public writing, it is safer to discuss failure patterns rather than ranking named models.
