"""Write an agent output to S3 and record the stage on the tracker.

Every stage output is versioned, because the audit trail is the point: a
published page must be traceable back to the draft it came from and the prompt
version that produced it.

The handoff blocks carry more than status. Agent 2 reports red flags,
guidelines checked and anything it wants a consultant to settle; Agent 3
reports sentences it would not touch without risking meaning. Those counts are
recorded here so the tracker can be queried for them, and the blocks themselves
stay in S3 because a DynamoDB item cannot hold them.
"""

from kneeschool_common import aws


STAGE_FILES = {"draft": "draft", "verified": "verified", "styled": "styled"}
STAGE_STATUS = {
    "draft": {"draft_status": "ai_draft", "qa_status": "assistant_checked"},
    "verified": {"qa_status": "evidence_checked"},
    "styled": {"qa_status": "evidence_checked"},
}


def escalations(handoff):
    """Fields the prompts define as routes to a human, by stage."""
    return {
        "red_flags": list(handoff.get("red_flags") or handoff.get("red_flag_findings") or []),
        "escalate_to_consultant": list(handoff.get("escalate_to_consultant") or []),
        "sentences_flagged_for_human_review": list(
            handoff.get("sentences_flagged_for_human_review") or []),
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

    flagged = escalations(handoff)
    fields = dict(STAGE_STATUS.get(stage, {}))
    if handoff.get("status"):
        fields["%s_agent_status" % stage] = handoff["status"]

    if stage == "verified":
        fields["red_flag_count"] = len(flagged["red_flags"])
        fields["escalation_count"] = len(flagged["escalate_to_consultant"])
        guidelines = handoff.get("guidelines_checked") or []
        if guidelines:
            # The homepage promises every management page records the guideline
            # version it was checked against. This is where that is kept.
            fields["guidelines_checked"] = guidelines
    if stage == "styled":
        fields["style_flag_count"] = len(flagged["sentences_flagged_for_human_review"])

    if fields:
        aws.update_tracker(page_id, fields)

    result = {"markdown_key": md_key, "handoff_key": handoff_key,
              "stage": stage, "version": version,
              "agent_status": handoff.get("status", "")}
    result.update({k: len(v) for k, v in flagged.items()})
    result["escalations"] = flagged
    return result
