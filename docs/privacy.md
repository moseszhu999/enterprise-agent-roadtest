# Privacy-first roadtest design

This repository is designed around a simple privacy principle:

> Test the agent with synthetic business cases first. Do not require customer business data.

## Default public-roadtest flow

Users should not upload real procurement records, contracts, ERP exports, supplier data, customer lists, or confidential business documents.

Instead, users should:

1. use the synthetic roadtest case provided in this repository;
2. run their agent in their own environment;
3. submit or save only the agent's output for scoring;
4. generate a readiness report from that output.

## What the public sample contains

The public sample uses synthetic data:

- fictional company context;
- fictional procurement request;
- fictional supplier quotes;
- fictional inventory constraints;
- fictional supplier history;
- fictional approval rules.

## Future private evaluations

For customer-specific evaluations, the preferred privacy tiers are:

1. synthetic roadtest only;
2. customer-provided anonymized materials;
3. local/private deployment where raw data stays in the customer environment.

## No-training principle

Submitted outputs should be used only for report generation unless explicit permission is granted.

Customer-specific outputs should not be used for model training, public examples, or marketing claims without written approval.
