# Dynamic Context Layer for Enterprise Agent Roadtests

Enterprise work does not happen in a static environment.

Procurement, logistics, finance, customer operations, and risk decisions are affected by external conditions:

- weather disruptions,
- port congestion,
- supplier news,
- exchange rates,
- commodity prices,
- transportation delays,
- regulatory changes,
- sanctions or export restrictions,
- geopolitical events,
- cyber incidents,
- public security advisories.

A stronger roadtest should eventually evaluate whether an AI Agent can reason with both **internal business constraints** and **external environment signals**.

This document defines how dynamic external context can be added without losing reproducibility, privacy, or auditability.

---

## 1. Why dynamic context matters

A static roadtest asks:

> Can the Agent solve the business task using the provided files?

A dynamic-context roadtest asks:

> Can the Agent update its recommendation when relevant external conditions change?

For example, in a procurement roadtest, the cheapest supplier may become riskier if:

- its region is affected by severe weather,
- its shipping route has port delays,
- its currency exposure changes,
- there is recent negative supplier news,
- a new export restriction affects the component.

This creates a more realistic enterprise test.

---

## 2. The core design principle

Dynamic context must be added as a **snapshot**, not as an uncontrolled live dependency.

A roadtest should not simply say:

> Go search the web and decide.

That makes the result hard to reproduce.

Instead, a roadtest should provide or capture a time-stamped context packet:

```text
context_snapshot_id: PAR-T001-CTX-2026-06-24-A
captured_at: 2026-06-24T10:00:00Z
sources: weather, shipping delay notice, FX rate, public supplier news
valid_for: this roadtest run only
```

The Agent can use the context, but the evaluator can still reproduce what the Agent saw.

---

## 3. Dynamic context types

### 3.1 Market context

Examples:

- exchange rate movement,
- commodity price change,
- freight cost increase,
- semiconductor shortage signal,
- steel or copper price shock.

Roadtest question:

> Did the Agent recognize that external cost volatility affects the procurement recommendation?

### 3.2 Logistics context

Examples:

- port congestion,
- weather disruption,
- trucking delay,
- air freight restriction,
- customs delay.

Roadtest question:

> Did the Agent adjust delivery-risk reasoning based on transport disruption?

### 3.3 Supplier risk context

Examples:

- supplier cyber incident,
- public quality complaint,
- labor strike,
- financial distress signal,
- regulatory investigation.

Roadtest question:

> Did the Agent identify external supplier risk and avoid overconfident automation?

### 3.4 Regulatory context

Examples:

- export restriction,
- sanctions update,
- data transfer regulation,
- compliance notice,
- product safety recall.

Roadtest question:

> Did the Agent escalate compliance-sensitive decisions to a human reviewer?

### 3.5 Security context

Examples:

- CVE advisory,
- software supply-chain compromise,
- vendor breach disclosure,
- phishing campaign against a supplier,
- leaked credential warning.

Roadtest question:

> Did the Agent respect security boundaries and avoid unsafe recommendations?

---

## 4. Two modes of use

### Mode A: Static synthetic context

The roadtest includes a synthetic external context packet created by the evaluator.

Example:

```text
External Context Snapshot:
- A typhoon is expected to affect Supplier A's regional logistics hub within 72 hours.
- Port processing time on Route A has increased from 2 days to 5-7 days.
- Supplier B is not affected by the disruption.
```

This is best for public samples because it is reproducible and privacy-safe.

### Mode B: Live captured context

The evaluator captures real public signals at test time and stores them as a context snapshot.

Example:

```text
Captured sources:
- public weather advisory,
- public port congestion notice,
- exchange rate snapshot,
- public supplier press release.
```

This is better for advanced paid or private evaluations, but it requires source logging and timestamping.

---

## 5. Reproducibility requirement

Every dynamic-context roadtest should record:

```yaml
context_snapshot_id:
captured_at:
source_type:
source_name:
source_url_or_reference:
summary:
relevance_to_task:
expected_agent_use:
```

The report should state whether the Agent:

- ignored the context,
- used it correctly,
- over-weighted it,
- hallucinated unsupported information,
- escalated appropriately,
- failed to cite or reference the context.

---

## 6. Privacy requirement

Dynamic context should not require customer internal data.

Preferred first design:

```text
Synthetic internal business data
+
Public or synthetic external context snapshot
+
Agent output only
```

Avoid asking customers to upload:

- real ERP exports,
- supplier contracts,
- customer orders,
- confidential pricing,
- internal risk registers,
- private incident reports.

---

## 7. Scoring extension

Dynamic-context roadtests can add new readiness dimensions:

### D1 Context relevance detection

Did the Agent identify which external signals matter?

### D2 Context-to-business mapping

Did the Agent connect external data to business impact?

### D3 Time sensitivity

Did the Agent recognize urgency or validity window?

### D4 Source discipline

Did the Agent avoid inventing unsupported external facts?

### D5 Escalation judgment

Did the Agent know when external risk requires human review?

### D6 Recommendation update

Did the Agent adjust the recommendation appropriately?

---

## 8. Example upgrade to PAR-T001

Current PAR-T001 tests internal constraints:

- inventory coverage,
- supplier delivery time,
- supplier history,
- approval rules,
- split-order reasoning.

A future dynamic version can add:

```text
PAR-T001-DYN-A

External Context Snapshot:
- Severe weather is expected near Supplier C's regional distribution center.
- Route C estimated delay: 2-4 days.
- Supplier B's route remains unaffected.
- Recent freight surcharge applies to emergency air shipment.

Expected Agent behavior:
- Recalculate the risk of using Supplier C.
- Reassess whether B should receive a larger allocation.
- Identify whether additional approval is needed due to increased cost.
- State uncertainty and request human confirmation if needed.
```

This makes the roadtest closer to real enterprise operations.

---

## 9. What this adds to the category position

Static roadtests evaluate whether an Agent can handle a known business case.

Dynamic-context roadtests evaluate whether an Agent can handle a changing business environment.

This strengthens the category claim:

> Enterprise AI Agents need business roadtests before customer PoC.

A stronger version is:

> Enterprise AI Agents need roadtests that combine internal business constraints with external environment signals.

---

## 10. Development roadmap

Recommended sequence:

1. Keep PAR-T001 static and reproducible.
2. Add one synthetic external context packet.
3. Add a dynamic scoring extension.
4. Run the same Agent output with and without context.
5. Compare whether the Agent updates its recommendation.
6. Later, support captured public-data snapshots.

Do not start with uncontrolled live web browsing.

Start with controlled context snapshots.

That keeps the roadtest inspectable, repeatable, and governance-friendly.
