"""Consultant chose 'amend'. Store the edit and send it back through the style
gate, so a human edit is held to the same house style as a generated one."""

import time

from kneeschool_common import aws


def handler(event, context):
    page_id = event["page_id"]
    review = event["review"]
    version = int(event.get("version", 1)) + 1
    base = aws.prefix(page_id)

    text = review.get("edited_text")
    if not text:
        raise RuntimeError("AmendWithoutText: decision was 'amend' but no edited_text was sent")

    aws.put_json(base + "consultant_review.json", {
        "page_id": page_id,
        "decision": review.get("decision"),
        "comments": review.get("comments"),
        "consultant": review.get("consultant"),
        "reviewed_at": int(time.time()),
        "applied_to_version": version,
    })
    aws.put_text(base + "styled_v%d.md" % version, text)
    aws.update_tracker(page_id, {"draft_status": "edited",
                                 "consultant": review.get("consultant", ""),
                                 "reviewed_at": int(time.time())})

    return {"version": version, "styled": {"markdown": text}, "style_loops": 0}
