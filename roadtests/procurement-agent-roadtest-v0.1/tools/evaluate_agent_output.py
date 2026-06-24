#!/usr/bin/env python3
"""
Lightweight first-pass evaluator for Procurement Agent Roadtest PAR-T001.

This is not a final expert judge. It is a simple screening script that checks
whether an Agent output mentions the core business constraints and likely plan.

Usage:
    python tools/evaluate_agent_output.py agent_output.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Check:
    name: str
    points: int
    passed: bool
    failure_code: str | None = None
    note: str = ""


def contains_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(p, text, flags=re.I) for p in patterns)


def evaluate(text: str) -> tuple[int, list[Check]]:
    t = text.lower()
    checks: list[Check] = []

    def add(name: str, points: int, passed: bool, failure_code: str | None = None, note: str = ""):
        checks.append(Check(name, points, passed, failure_code, note))

    add(
        "Recognizes inventory coverage / 6-day constraint",
        20,
        contains_any(t, [r"\b6\s*days?\b", r"360\s*/\s*60", r"inventory coverage", r"库存.*6", r"6\s*天"]),
        "P02",
        "Must identify current inventory covers only 6 days.",
    )

    add(
        "Recognizes Supplier A lead-time risk",
        15,
        contains_any(t, [r"supplier a.*12\s*days?", r"12\s*days?.*supplier a", r"a.*交期.*12", r"a.*lead time.*12"]),
        "P03",
        "Must recognize Supplier A's 12-day lead time is risky.",
    )

    add(
        "Avoids lowest-price-only decision",
        10,
        not (
            contains_any(t, [r"recommend.*supplier a", r"select.*supplier a", r"choose.*supplier a"])
            and not contains_any(t, [r"not recommend.*supplier a", r"do not use supplier a", r"a.*not.*recommended", r"不建议.*a"])
        ),
        "P01",
        "Selecting Supplier A as main supplier is likely lowest-price bias.",
    )

    add(
        "Mentions Supplier B expedited delivery",
        10,
        contains_any(t, [r"supplier b.*expedit", r"expedit.*supplier b", r"b.*5\s*days?", r"b.*加急.*5"]),
        None,
        "Should use Supplier B expedited delivery as the urgent supply component.",
    )

    add(
        "Mentions split purchase / B + C plan",
        10,
        contains_any(t, [r"supplier b.*800", r"b.*800"]) and contains_any(t, [r"supplier c.*400", r"c.*400"]),
        "P08",
        "Best answer should allocate B 800 units and C 400 units.",
    )

    add(
        "Considers supplier history / reliability",
        10,
        contains_any(t, [r"on[- ]?time", r"准时", r"delay", r"延期", r"95%", r"72%"]),
        "P04",
        "Should compare historical delivery performance.",
    )

    add(
        "Considers payment terms / cash flow",
        5,
        contains_any(t, [r"payment", r"prepayment", r"cash[- ]?flow", r"付款", r"预付款", r"现金流"]),
        "P06",
        "Should mention payment terms.",
    )

    add(
        "Identifies approval requirements",
        10,
        contains_any(t, [r"approval", r"manager", r"审批", r"采购经理", r"production manager", r"生产经理"]),
        "P07",
        "Should identify approval requirements.",
    )

    add(
        "Mentions backup / contingency plan",
        5,
        contains_any(t, [r"backup", r"contingency", r"alternative", r"备选", r"应急"]),
        "P09",
        "Should include backup plan.",
    )

    add(
        "Avoids obvious fabrication",
        5,
        not contains_any(t, [r"contract clause", r"exclusive supplier", r"discount agreement", r"warranty period"]),
        "P10",
        "Should not invent unavailable facts.",
    )

    total = sum(c.points for c in checks if c.passed)
    return total, checks


def conclusion(score: int) -> str:
    if score >= 85:
        return "Strong. Ready for customer PoC discussion."
    if score >= 70:
        return "Usable with improvements. Needs review."
    if score >= 50:
        return "Weak. Not ready for enterprise PoC."
    return "Fails the roadtest."


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/evaluate_agent_output.py path/to/agent_output.md")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8")
    score, checks = evaluate(text)

    print("# Procurement Agent Readiness Evaluation")
    print()
    print(f"Score: {score} / 100")
    print(f"Conclusion: {conclusion(score)}")
    print()
    print("## Check results")
    print()

    failures = []

    for c in checks:
        status = "PASS" if c.passed else "FAIL"
        print(f"- [{status}] {c.name} ({c.points} pts)")
        if not c.passed and c.failure_code:
            failures.append(c.failure_code)

    if failures:
        print()
        print("## Detected failure codes")
        print()
        print(", ".join(sorted(set(failures))))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
