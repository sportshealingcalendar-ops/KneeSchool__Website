"""Structural checks on the state machine definition.

These are governance tests, not style tests. The QA manual says the consultant
gate cannot be bypassed; that promise is only true if the graph makes it true,
so it is asserted here rather than trusted.
"""

import json
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASL_PATH = os.path.join(ROOT, "statemachine", "content-pipeline.asl.json")


def successors(state):
    out = []
    for key in ("Next", "Default"):
        if state.get(key):
            out.append(state[key])
    for group in ("Choices", "Catch"):
        for entry in state.get(group) or []:
            if entry.get("Next"):
                out.append(entry["Next"])
    return out


class Definition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(ASL_PATH) as fh:
            cls.raw = fh.read()
        cls.doc = json.loads(cls.raw)
        cls.states = cls.doc["States"]

    def test_is_valid_json_with_a_start_state(self):
        self.assertIn(self.doc["StartAt"], self.states)

    def test_every_transition_target_exists(self):
        for name, state in self.states.items():
            for target in successors(state):
                self.assertIn(target, self.states, "%s points at missing state %s" % (name, target))

    def test_every_state_is_reachable(self):
        seen, stack = set(), [self.doc["StartAt"]]
        while stack:
            name = stack.pop()
            if name in seen:
                continue
            seen.add(name)
            stack.extend(successors(self.states[name]))
        self.assertEqual(set(self.states) - seen, set())

    def test_every_state_terminates_or_continues(self):
        for name, state in self.states.items():
            terminal = state.get("End") or state["Type"] in ("Fail", "Succeed")
            self.assertTrue(terminal or successors(state), "%s is a dead end" % name)

    def test_publish_is_reachable_only_through_consultant_review(self):
        """Remove ConsultantReview and Publish must become unreachable."""
        seen, stack = set(), [self.doc["StartAt"]]
        while stack:
            name = stack.pop()
            if name in seen or name == "ConsultantReview":
                continue
            seen.add(name)
            stack.extend(successors(self.states[name]))
        self.assertNotIn("Publish", seen,
                         "there is a route to Publish that skips the consultant gate")

    def test_consultant_review_waits_for_a_task_token(self):
        state = self.states["ConsultantReview"]
        self.assertTrue(state["Resource"].endswith(".waitForTaskToken"))
        self.assertEqual(state["HeartbeatSeconds"], 1209600)

    def test_regeneration_is_capped(self):
        self.assertEqual(self.states["CheckRegenCount"]["Choices"][0]["NumericLessThan"], 2)

    def test_style_loop_is_capped(self):
        choice = self.states["LintOutcome"]["Choices"][0]
        limit = [c for c in choice["And"] if "NumericLessThan" in c][0]
        self.assertEqual(limit["NumericLessThan"], 2)

    def test_lint_failure_cannot_reach_publish(self):
        targets = successors(self.states["LintOutcome"])
        self.assertNotIn("Publish", targets)

    def test_all_substitutions_are_named(self):
        found = set(re.findall(r"\$\{(\w+)\}", self.raw))
        expected = {
            "LoadBriefArn", "PersistArtifactArn", "StyleLintArn", "CreateReviewTaskArn",
            "ApplyAmendmentsArn", "NotifyEditorArn", "PublishToCmsArn",
            "AgentGeneratorArn", "AgentVerifierArn", "AgentStylerArn",
        }
        self.assertEqual(found, expected)


if __name__ == "__main__":
    unittest.main()
