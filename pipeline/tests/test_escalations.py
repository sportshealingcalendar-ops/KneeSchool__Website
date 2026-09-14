"""The handoff blocks define fields whose only purpose is to reach a person:
Agent 2 raises red flags and lists what it could not settle from the
literature, Agent 3 lists sentences it would not rewrite without risking
meaning. Orchestration that drops them makes the consultant gate decorative,
so the plumbing is tested.
"""

import importlib.util
import os
import sys
import types
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class FakeTable(object):
    def __init__(self):
        self.updates = []

    def update_item(self, **kwargs):
        self.updates.append(kwargs)


def load(name, stored_objects=None):
    """Import a handler with the AWS layer replaced by recording fakes."""
    if "boto3" not in sys.modules:
        mod = types.ModuleType("boto3")
        mod.client = lambda *a, **k: None
        mod.resource = lambda *a, **k: types.SimpleNamespace(Table=lambda n: None)
        sys.modules["boto3"] = mod
    layer = os.path.join(ROOT, "layers", "common", "python")
    if layer not in sys.path:
        sys.path.insert(0, layer)

    from kneeschool_common import aws
    recorder = types.SimpleNamespace(published=[], written={}, table=FakeTable())
    stored = stored_objects or {}

    aws.put_text = lambda k, t, **kw: recorder.written.setdefault(k, t) or k
    aws.put_json = lambda k, o: recorder.written.setdefault(k, o) or k
    aws.get_json = lambda k: stored[k]
    aws.update_tracker = lambda pid, f: recorder.table.updates.append({"page_id": pid, "fields": f})
    aws.tracker = lambda: recorder.table
    aws.publish = lambda topic, subject, message: recorder.published.append(
        {"topic": topic, "subject": subject, "message": message})

    path = os.path.join(ROOT, "functions", name, "handler.py")
    sys.path.insert(0, os.path.dirname(path))
    try:
        spec = importlib.util.spec_from_file_location("esc_" + name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(os.path.dirname(path))
    return module, recorder


VERIFIED_HANDOFF = {
    "page_id": "1.2.3",
    "claims_checked": 24,
    "verified": 22,
    "corrected": [{"before": "always", "after": "usually", "reason": "source is weaker",
                   "source": "ref 2"}],
    "red_flags": ["unsupported incidence figure in the MRCS block"],
    "guidelines_checked": [{"guideline": "NICE NG226", "version_or_date": "2024-06"}],
    "escalate_to_consultant": [
        "whether to describe root repair as standard of care in a UK setting"],
    "status": "EVIDENCE_VERIFIED",
}

STYLED_HANDOFF = {
    "page_id": "1.2.3",
    "dashes_removed": 7,
    "ai_phrases_removed": ["delve"],
    "sentences_flagged_for_human_review": [
        "Hoop stress is resisted by the roots in tension."],
    "status": "STYLE_COMPLETE_READY_FOR_CONSULTANT_REVIEW",
}


class PersistArtifact(unittest.TestCase):
    def run_stage(self, stage, handoff):
        mod, rec = load("persist_artifact")
        result = mod.handler({"page_id": "1.2.3", "stage": stage, "version": 1,
                              "payload": {"markdown": "# Menisci\n", "handoff": handoff}}, None)
        return result, rec.table.updates[0]["fields"]

    def test_verifier_red_flags_and_escalations_are_counted(self):
        result, fields = self.run_stage("verified", VERIFIED_HANDOFF)
        self.assertEqual(fields["red_flag_count"], 1)
        self.assertEqual(fields["escalation_count"], 1)
        self.assertEqual(result["red_flags"], 1)
        self.assertEqual(result["escalate_to_consultant"], 1)

    def test_guidelines_checked_reach_the_tracker(self):
        _, fields = self.run_stage("verified", VERIFIED_HANDOFF)
        self.assertEqual(fields["guidelines_checked"][0]["guideline"], "NICE NG226")

    def test_agent_status_is_recorded_per_stage(self):
        _, fields = self.run_stage("verified", VERIFIED_HANDOFF)
        self.assertEqual(fields["verified_agent_status"], "EVIDENCE_VERIFIED")
        _, fields = self.run_stage("styled", STYLED_HANDOFF)
        self.assertEqual(fields["styled_agent_status"],
                         "STYLE_COMPLETE_READY_FOR_CONSULTANT_REVIEW")

    def test_styler_flags_are_counted(self):
        _, fields = self.run_stage("styled", STYLED_HANDOFF)
        self.assertEqual(fields["style_flag_count"], 1)

    def test_empty_handoff_does_not_raise(self):
        result, _ = self.run_stage("draft", {})
        self.assertEqual(result["red_flags"], 0)


class ConsultantGate(unittest.TestCase):
    stored = {
        "pipeline/1.2.3/verified_v1.handoff.json": VERIFIED_HANDOFF,
        "pipeline/1.2.3/styled_v1.handoff.json": STYLED_HANDOFF,
    }

    def invoke(self, stored=None):
        mod, rec = load("create_review_task", stored if stored is not None else self.stored)
        mod.handler({"task_token": "tok-1",
                     "payload": {"page_id": "1.2.3", "version": 1,
                                 "brief": {"title": "Menisci",
                                           "tiers_required": ["junior", "patient"]},
                                 "lint": {"warn_count": 3}}}, None)
        return rec

    def test_escalations_travel_with_the_review_request(self):
        msg = self.invoke().published[0]["message"]
        needs = msg["needs_your_judgement"]
        self.assertEqual(needs["red_flags"], VERIFIED_HANDOFF["red_flags"])
        self.assertEqual(needs["escalate_to_consultant"],
                         VERIFIED_HANDOFF["escalate_to_consultant"])
        self.assertEqual(needs["sentences_flagged_for_human_review"],
                         STYLED_HANDOFF["sentences_flagged_for_human_review"])

    def test_audit_detail_is_included(self):
        msg = self.invoke().published[0]["message"]
        self.assertEqual(msg["for_audit"]["corrections_made"], 1)
        self.assertEqual(msg["for_audit"]["lint_warnings"], 3)
        self.assertEqual(msg["for_audit"]["guidelines_checked"][0]["guideline"], "NICE NG226")

    def test_escalation_count_recorded_against_the_page(self):
        rec = self.invoke()
        values = rec.table.updates[0]["ExpressionAttributeValues"]
        self.assertEqual(values[":e"], 3)
        self.assertEqual(values[":q"], "awaiting_consultant")
        self.assertEqual(values[":t"], "tok-1")

    def test_missing_handoffs_do_not_strand_the_execution(self):
        rec = self.invoke(stored={})
        msg = rec.published[0]["message"]
        self.assertEqual(msg["needs_your_judgement"]["red_flags"], [])
        self.assertTrue(msg["artefacts"]["styled_key"].endswith("styled_v1.md"))


if __name__ == "__main__":
    unittest.main()
