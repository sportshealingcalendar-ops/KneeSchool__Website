"""Write an agent output to S3 and record the stage on the tracker.

Every stage output is versioned, because the audit trail is the point: a
published page must be traceable back to the draft it came from and the prompt
version that produced it.
"""

from kneeschool_common import aws


STAGE_FILES = {"draft": "draft", "verified": "verified", "styled": "styled"}
STAGE_STATUS = {
    "draft": {"draft_status": "ai_draft", "qa_status": "assistant_checked"},
    "verified": {"qa_status": "evidence_checked"},
    "styled": {"qa_status": "evidence_checked"},
}


def handler(event, context):
    page_id = event["page_id"]
    stage = event["stage"]
    version = int(event.get("version", 1))
    payload = event.get("payload") or {}

    stem = STAGE_FILES[stage]
    base = aws.prefix(page_id)
    text = payload.get("markdown") or payload.get("text") or ""
    handoff = payload.get("handoff") or {}

    md_key = aws.put_text("%s%s_v%d.md" % (base, stem, version), text)
    handoff_key = aws.put_json("%s%s_v%d.handoff.json" % (base, stem, version), handoff)

    fields = dict(STAGE_STATUS.get(stage, {}))
    red_flags = handoff.get("red_flags") or handoff.get("red_flag_findings") or []
    if stage == "verified":
        fields["red_flag_count"] = len(red_flags)
    if fields:
        aws.update_tracker(page_id, fields)

    return {"markdown_key": md_key, "handoff_key": handoff_key,
            "stage": stage, "version": version,
            "red_flag_count": len(red_flags)}
