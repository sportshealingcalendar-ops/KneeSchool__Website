"""Stage 4. The deterministic style gate.

No model call. Returns pass or fail plus every violation in one pass, so the
styler fixes them all in a single loop rather than one at a time.
"""

import linter
from kneeschool_common import aws


def handler(event, context):
    page_id = event["page_id"]
    brief = event.get("brief") or {}
    text = (event.get("styled") or {}).get("markdown") or event.get("text") or ""

    report = linter.lint(text, brief)
    report["page_id"] = page_id
    report["style_loops"] = int(event.get("style_loops", 0))

    aws.put_json(aws.prefix(page_id) + "lint_report.json", report)
    if not report["pass"]:
        aws.update_tracker(page_id, {"last_lint_fail_count": report["fail_count"]})

    return {
        "pass": report["pass"],
        "fail_count": report["fail_count"],
        "warn_count": report["warn_count"],
        "findings": report["findings"][:100],
        "report_key": aws.prefix(page_id) + "lint_report.json",
    }
