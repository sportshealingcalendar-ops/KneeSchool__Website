"""Stage 6. Reached only after an approve decision.

Writes the published artefacts, sets the annual review date and hands the page
to the CMS as a draft. The CMS receives it as a draft on purpose: publication
to the live site stays a human action in the CMS.
"""

import json
import os
import time
import urllib.request

from kneeschool_common import aws


CMS_ENDPOINT = os.environ.get("CMS_ENDPOINT", "")
YEAR = 365 * 24 * 3600


def handler(event, context):
    page_id = event["page_id"]
    brief = event.get("brief") or {}
    version = int(event.get("version", 1))
    base = aws.prefix(page_id)
    out = "published/%s/" % page_id

    text = aws.get_text(base + "styled_v%d.md" % version)
    handoff = {}
    try:
        handoff = aws.get_json(base + "verified_v%d.handoff.json" % version)
    except Exception:
        pass

    now = int(time.time())
    aws.put_text(out + "final.md", text)
    aws.put_json(out + "references.json", {"page_id": page_id,
                                           "references": handoff.get("sources", [])})
    aws.put_json(out + "curriculum_tags.json", {"page_id": page_id,
                                                "tags": brief.get("curriculum_tags", [])})

    aws.update_tracker(page_id, {
        "publication_status": "published",
        "qa_status": "consultant_reviewed",
        "published_at": now,
        "next_review_due": now + YEAR,
        "published_version": version,
    })

    if CMS_ENDPOINT:
        body = json.dumps({"page_id": page_id, "title": brief.get("title"),
                           "status": "draft", "markdown": text,
                           "curriculum_tags": brief.get("curriculum_tags", [])}).encode("utf-8")
        req = urllib.request.Request(CMS_ENDPOINT, data=body, method="POST",
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            resp.read()

    return {"page_id": page_id, "published_prefix": out, "version": version}
