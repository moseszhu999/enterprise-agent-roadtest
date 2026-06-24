# Procurement Agent Roadtest v0.1

**A synthetic business roadtest for evaluating whether an AI Agent can handle an enterprise procurement decision before a customer PoC.**

中文一句话：**给采购类 AI Agent 做企业业务路考：它不是看起来会回答，而是真的能不能在价格、库存、交期、供应商风险、付款条件和审批规则冲突下给出可验收建议。**

## What this package tests

This roadtest evaluates whether an AI Agent can:

1. Read a multi-file business scenario.
2. Understand that procurement is not simply choosing the lowest price.
3. Calculate inventory coverage and delivery risk.
4. Compare supplier price, lead time, quality, delivery history, payment terms, and capacity.
5. Identify approval requirements.
6. Recommend a practical procurement plan.
7. Produce a reviewable report without inventing information.

## Privacy design

This package uses only **synthetic enterprise data**.

The customer does **not** need to upload real procurement data, real ERP exports, real supplier files, real contracts, or real customer orders.

Basic workflow:

1. Copy the task prompt and synthetic input data into your own AI Agent.
2. Run the Agent inside your own environment.
3. Paste only the Agent output into the evaluator or send it for manual review.
4. Receive a readiness report.

## Quick start

### Step 1 — Read the business task

Open:

```text
07_agent_task_prompt.md
```

Copy the task prompt and provide the synthetic input files to your AI Agent.

### Step 2 — Collect Agent output

Save the Agent answer as:

```text
agent_output.md
```

### Step 3 — Run the simple evaluator

```bash
python tools/evaluate_agent_output.py agent_output.md
```

This script is only a lightweight first-pass evaluator. It does not replace expert review.

### Step 4 — Produce the final report

Use:

```text
11_evaluation_report_template.md
```

## Files

```text
01_business_background.md      Business context
02_purchase_request.md         Purchase need and constraints
03_supplier_quotes.csv         Supplier price, lead time, capacity, payment terms
04_inventory_constraints.csv   Inventory and consumption constraints
05_supplier_history.csv        Historical supplier performance
06_approval_rules.md           Internal approval rules
07_agent_task_prompt.md        Prompt/task for the Agent
08_reference_answer.md         Expected decision and reasoning
09_scoring_rubric.md           100-point scoring rubric
10_failure_taxonomy.md         Failure/error type taxonomy
11_evaluation_report_template.md
12_privacy_note.md
examples/                       Sample good/bad Agent outputs and reports
tools/evaluate_agent_output.py  Simple first-pass evaluator
metadata.json                   Machine-readable package metadata
```

## Intended users

- AI Agent teams preparing enterprise customer demos.
- AI consulting teams running procurement/supply-chain PoCs.
- Enterprise AI project teams evaluating vendors.
- AI evaluation/data teams designing realistic business tasks.

## Positioning

This is not a procurement optimization engine.

This is not a generic benchmark.

This is a **business-readiness roadtest**: a small but realistic task that checks whether an AI Agent can produce a decision that a business stakeholder could review.
