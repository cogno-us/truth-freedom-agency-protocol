#!/usr/bin/env python3
import json
import sys
from pathlib import Path

REQUIRED_CASE_KEYS = {
    "id",
    "category",
    "input",
    "expected_behaviors",
    "failure_conditions",
    "status",
}
ALLOWED_STATUS = {"unexecuted", "executed", "invalid"}

def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)

def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("evaluation/cases.json")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {path}: {exc}")

    if data.get("schema_version") != "1.0":
        fail("schema_version must be 1.0")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("cases must be a non-empty list")

    seen = set()
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            fail(f"case {index} must be an object")
        missing = REQUIRED_CASE_KEYS - case.keys()
        if missing:
            fail(f"case {index} missing keys: {sorted(missing)}")
        if case["id"] in seen:
            fail(f"duplicate case id: {case['id']}")
        seen.add(case["id"])
        if case["status"] not in ALLOWED_STATUS:
            fail(f"{case['id']} has invalid status {case['status']!r}")
        if not isinstance(case["expected_behaviors"], list) or not case["expected_behaviors"]:
            fail(f"{case['id']} expected_behaviors must be a non-empty list")
        if not isinstance(case["failure_conditions"], list) or not case["failure_conditions"]:
            fail(f"{case['id']} failure_conditions must be a non-empty list")

    required_categories = {
        "truthful_disagreement_without_pressure",
        "uncertainty_without_invented_certainty",
        "necessary_clarification",
        "excessive_questioning",
        "authority_not_inferred_from_persuasion",
        "preserve_meaningful_alternatives",
        "routine_work_without_unnecessary_process",
    }
    categories = {case["category"] for case in cases}
    missing_categories = required_categories - categories
    if missing_categories:
        fail(f"missing required categories: {sorted(missing_categories)}")

    print(f"OK: {len(cases)} cases validated; all statuses are explicit.")

if __name__ == "__main__":
    main()
