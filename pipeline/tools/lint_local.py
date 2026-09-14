#!/usr/bin/env python3
"""Run the style gate over a markdown draft without deploying anything.

    python3 pipeline/tools/lint_local.py draft.md
    python3 pipeline/tools/lint_local.py draft.md --brief pipeline/config/briefs/1.2.3.json
    python3 pipeline/tools/lint_local.py draft.md --json > lint_report.json

Exit code 0 when the draft passes, 1 when a fail rule fires. Usable as a
pre-commit hook or a CI step on hand written copy as well as generated copy.
"""

import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "functions", "style_lint"))

import linter  # noqa: E402

COLOURS = {"fail": "\033[31m", "warn": "\033[33m", "off": "\033[0m"}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft", help="path to a markdown draft")
    ap.add_argument("--brief", help="path to the content brief JSON")
    ap.add_argument("--rules", help="path to lint_rules.json")
    ap.add_argument("--json", action="store_true", help="print the full report as JSON")
    ap.add_argument("--no-colour", action="store_true")
    args = ap.parse_args()

    with open(args.draft) as fh:
        text = fh.read()
    brief = {}
    if args.brief:
        with open(args.brief) as fh:
            brief = json.load(fh)

    rules = linter.load_rules(args.rules)
    report = linter.lint(text, brief, rules)

    if args.json:
        print(json.dumps(report, indent=2))
        return 0 if report["pass"] else 1

    tint = (lambda s, k: s) if args.no_colour or not sys.stdout.isatty() \
        else (lambda s, k: COLOURS[k] + s + COLOURS["off"])

    doc = report["document"]
    print("%s  %d words, %d sentences, tiers: %s"
          % (args.draft, doc["word_count"], doc["sentence_count"],
             ", ".join(doc["tiers_present"]) or "none detected"))

    for f in report["findings"]:
        where = " line %s" % f["line"] if f.get("line") else ""
        print("  %s %s%s  %s" % (tint(f["severity"].upper(), f["severity"]),
                                 f["rule_id"], where, f["description"]))
        if f["matched_text"]:
            print("        matched: %r" % f["matched_text"])
        if f["context"]:
            print("        context: %s" % f["context"])

    print("")
    if report["pass"]:
        print("PASS  %d warnings for the review pack" % report["warn_count"])
        return 0
    print(tint("FAIL", "fail") + "  %d blocking, %d warnings"
          % (report["fail_count"], report["warn_count"]))
    return 1


if __name__ == "__main__":
    sys.exit(main())
