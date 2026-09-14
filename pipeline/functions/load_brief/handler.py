"""Stage 0. Read the brief, reject it if it breaks a field or governance rule,
seed the execution state."""

from kneeschool_common import aws, brief as brief_rules


def handler(event, context):
    page_id = event["page_id"]
    key = aws.prefix(page_id) + "brief.json"
    doc = aws.get_json(key)

    try:
        brief_rules.validate(doc)
    except brief_rules.BriefError as exc:
        aws.update_tracker(page_id, {"draft_status": "rejected_brief",
                                     "last_error": str(exc)})
        raise RuntimeError("BriefRejected: %s" % exc)

    aws.update_tracker(page_id, {
        "title": doc.get("title"),
        "tiers_required": doc.get("tiers_required"),
        "curriculum_tags": doc.get("curriculum_tags") or [],
        "priority": (doc.get("pipeline") or {}).get("priority", "medium"),
        "draft_status": "in_pipeline",
        "execution_arn": event.get("execution_arn", ""),
        "artifact_prefix": aws.prefix(page_id),
        "regen_count": 0,
        "red_flag_count": 0,
    })

    return {
        "page_id": page_id,
        "brief": doc,
        "version": 1,
        "regen_count": 0,
        "style_loops": 0,
        "artifact_prefix": aws.prefix(page_id),
    }
