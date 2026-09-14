"""Terminal hold. Two failed regenerations, two failed style loops or a reject
decision all land here. Repeated failure is a systemic problem, so it goes to a
person rather than back around the loop."""

import time

from kneeschool_common import aws


def handler(event, context):
    page_id = event["page_id"]
    reason = event.get("reason", "unspecified")

    aws.update_tracker(page_id, {"draft_status": "held_for_triage",
                                 "hold_reason": reason,
                                 "held_at": int(time.time())})
    aws.publish(aws.EDITOR_TOPIC,
                "KneeSchool pipeline hold: %s" % page_id,
                {"page_id": page_id, "reason": reason,
                 "regen_count": event.get("regen_count"),
                 "style_loops": event.get("style_loops"),
                 "artifact_prefix": aws.prefix(page_id)})

    return {"page_id": page_id, "status": "held_for_triage", "reason": reason}
