"""Import and wiring checks for the Lambda handlers.

boto3 is provided by the Lambda runtime rather than the repository, so it is
stubbed here. The point of these tests is that every handler imports cleanly
against the shared layer and exposes the entry point the state machine calls.
"""

import os
import sys
import types
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _stub_boto3():
    if "boto3" in sys.modules:
        return
    mod = types.ModuleType("boto3")
    mod.client = lambda *a, **k: None
    mod.resource = lambda *a, **k: types.SimpleNamespace(Table=lambda n: None)
    sys.modules["boto3"] = mod


class Handlers(unittest.TestCase):
    names = ["load_brief", "persist_artifact", "style_lint", "create_review_task",
             "apply_amendments", "notify_editor", "publish_to_cms"]

    @classmethod
    def setUpClass(cls):
        _stub_boto3()
        sys.path.insert(0, os.path.join(ROOT, "layers", "common", "python"))

    def test_every_handler_imports_and_exposes_an_entry_point(self):
        import importlib.util
        for name in self.names:
            path = os.path.join(ROOT, "functions", name, "handler.py")
            extra = os.path.dirname(path)
            sys.path.insert(0, extra)
            try:
                spec = importlib.util.spec_from_file_location("h_" + name, path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                self.assertTrue(callable(getattr(mod, "handler", None)),
                                "%s has no callable handler" % name)
            finally:
                sys.path.remove(extra)


class BriefValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _stub_boto3()
        sys.path.insert(0, os.path.join(ROOT, "layers", "common", "python"))

    def setUp(self):
        import json
        from kneeschool_common import brief
        self.brief = brief
        with open(os.path.join(ROOT, "config", "briefs", "1.2.3.json")) as fh:
            self.pilot = json.load(fh)

    def test_pilot_brief_is_valid(self):
        self.assertIs(self.brief.validate(self.pilot), self.pilot)

    def test_junior_tier_cannot_allow_commercial_content(self):
        bad = dict(self.pilot)
        bad["governance"] = dict(self.pilot["governance"], commercial_content_allowed=True)
        with self.assertRaises(self.brief.BriefError) as cm:
            self.brief.validate(bad)
        self.assertIn("commercial_content_allowed", str(cm.exception))

    def test_missing_must_not_cover_is_rejected(self):
        bad = dict(self.pilot)
        bad["scope"] = {"must_cover": ["something"]}
        with self.assertRaises(self.brief.BriefError):
            self.brief.validate(bad)

    def test_unknown_tier_is_rejected(self):
        bad = dict(self.pilot, tiers_required=["patient", "postgrad"])
        with self.assertRaises(self.brief.BriefError):
            self.brief.validate(bad)

    def test_language_must_be_en_gb(self):
        bad = dict(self.pilot)
        bad["output_requirements"] = dict(self.pilot["output_requirements"], language="en-US")
        with self.assertRaises(self.brief.BriefError):
            self.brief.validate(bad)


if __name__ == "__main__":
    unittest.main()
