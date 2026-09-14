"""Stage 5. The consultant gate.

Called with waitForTaskToken. The execution stops here until the review app
calls SendTaskSuccess. There is deliberately no path from the style gate to
publication that skips this state.

The notification carries the escalations, not just links to them. Agent 2
raises red flags and lists what it could not settle from the literature;
Agent 3 lists sentences it would not rewrite without risking meaning. Those are
the reasons a human is in the loop at all, so they travel with the request
rather than waiting to be found in an artefact.
"""

import os
import time

from kneeschool_common import aws


REVIEW_APP_URL = os.environ.get("REVIEW_APP_URL", "")


def _handoff(base, stem, version):
    try:
        return aws.get_json("%s%s_v%d.handoff.json" % (base, stem, version))
    except Exception:
        # A missing handoff must not strand the execution at the gate. The
        # consultant still gets the draft and the artefact keys.
        return {}


def handler(event, context):
    payload = event["payload"]
    token = event["task_token"]
    page_id = payload["page_id"]
    version = int(payload.get("version", 1))
    base = aws.prefix(page_id)

    verified = _handoff(base, "verified", version)
    styled = _handoff(base, "styled", version)
    lint = payload.get("lint") or {}

    red_flags = verified.get("red_flags") or []
    escalations = verified.get("escalate_to_consultant") or []
    style_flags = styled.get("sentences_flagged_for_human_review") or []
    corrections = verified.get("corrected") or []

    aws.tracker().update_item(
        Key={"page_id": page_id},
        UpdateExpression=("SET task_token = :t, qa_status = :q, review_requested_at = :n, "
                          "review_escalation_count = :e"),
        ExpressionAttributeValues={
            ":t": token,
            ":q": "awaiting_consultant",
            ":n": int(time.time()),
            ":e": len(red_flags) + len(escalations) + len(style_flags),
        },
    )

    aws.publish(aws.REVIEW_TOPIC,
                "KneeSchool review ready: %s" % page_id,
                {
                    "page_id": page_id,
                    "title": (payload.get("brief") or {}).get("title"),
                    "tiers": (payload.get("brief") or {}).get("tiers_required", []),
                    "version": version,
                    "artefacts": {
                        "styled_key": base + "styled_v%d.md" % version,
                        "verification_key": base + "verified_v%d.handoff.json" % version,
                        "style_key": base + "styled_v%d.handoff.json" % version,
                        "lint_report_key": base + "lint_report.json",
                    },
                    "needs_your_judgement": {
                        "red_flags": red_flags,
                        "escalate_to_consultant": escalations,
                        "sentences_flagged_for_human_review": style_flags,
                    },
                    "for_audit": {
                        "corrections_made": len(corrections),
                        "guidelines_checked": verified.get("guidelines_checked") or [],
                        "lint_warnings": lint.get("warn_count", 0),
                    },
                    "review_url": (REVIEW_APP_URL.rstrip("/") + "/review/" + page_id)
                                  if REVIEW_APP_URL else "",
                })

    # No return value. The execution resumes when the review app sends the token.
