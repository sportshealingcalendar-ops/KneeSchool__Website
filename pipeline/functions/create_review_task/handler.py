"""Stage 5. The consultant gate.

Called with waitForTaskToken. The execution stops here until the review app
calls SendTaskSuccess. There is deliberately no path from the style gate to
publication that skips this state.
"""

import os
import time

from kneeschool_common import aws


REVIEW_APP_URL = os.environ.get("REVIEW_APP_URL", "")


def handler(event, context):
    payload = event["payload"]
    token = event["task_token"]
    page_id = payload["page_id"]
    base = aws.prefix(page_id)

    aws.tracker().update_item(
        Key={"page_id": page_id},
        UpdateExpression="SET task_token = :t, qa_status = :q, review_requested_at = :n",
        ExpressionAttributeValues={
            ":t": token,
            ":q": "awaiting_consultant",
            ":n": int(time.time()),
        },
    )

    aws.publish(aws.REVIEW_TOPIC,
                "KneeSchool review ready: %s" % page_id,
                {"page_id": page_id,
                 "title": (payload.get("brief") or {}).get("title"),
                 "styled_key": base + "styled_v%d.md" % payload.get("version", 1),
                 "verification_key": base + "verified_v%d.handoff.json" % payload.get("version", 1),
                 "lint_report_key": base + "lint_report.json",
                 "review_url": (REVIEW_APP_URL.rstrip("/") + "/review/" + page_id)
                               if REVIEW_APP_URL else ""})

    # No return value. The execution resumes when the review app sends the token.
