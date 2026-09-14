"""Deterministic style gate for KneeSchool article drafts.

The gate is regex and counting only. No model call. A language model asked to
police its own style will occasionally let something through; a rule will not.

Document conventions this linter expects from Agent 3:

  # Title
  ## Junior            <- tier block, one heading per tier in brief.tiers_required
  ...body...
  ### Key learning points
  - point
  ## Patient
  ...
  ### Frequently asked questions
  **Q.** ...
  ## References
  1. Author A, Author B. Title. Journal. 2024. doi:10.xxxx/yyyy

Tier headings are matched case insensitively against the aliases in TIER_ALIASES.
Everything from the References heading to the end of the document is the
reference list, which is excluded from the body scopes.
"""

import json
import os
import re
import statistics

TIERS = ["junior", "patient", "medical_student", "mrcs", "frcs", "fellowship", "consultant"]

TIER_ALIASES = {
    "junior": ["junior", "junior academy", "school", "school age"],
    "patient": ["patient", "patient academy", "for patients"],
    "medical_student": ["medical student", "student", "student academy", "undergraduate"],
    "mrcs": ["mrcs", "mrcs academy", "core trainee"],
    "frcs": ["frcs", "frcs academy", "frcs (tr and orth)", "frcs tr and orth", "higher trainee"],
    "fellowship": ["fellowship", "fellow", "fellowship academy"],
    "consultant": ["consultant", "consultant masterclass"],
}

REFERENCE_HEADINGS = ["references", "reference list", "sources"]
KLP_HEADINGS = ["key learning points", "key learning point"]
FAQ_HEADINGS = ["frequently asked questions", "faqs", "faq", "common questions"]

ABBREVIATIONS = [
    "e.g.", "i.e.", "vs.", "cf.", "approx.", "Dr.", "Mr.", "Mrs.", "Ms.", "Prof.",
    "Fig.", "no.", "et al.", "St.", "Inc.", "Ltd.",
]

CODE_FENCE = re.compile(r"```.*?```", re.DOTALL)


# ---------------------------------------------------------------- document


class Document(object):
    """A parsed draft: raw text, tier blocks, reference list, body."""

    def __init__(self, text):
        self.raw = text or ""
        self.lines = self.raw.split("\n")
        self.sections = self._split_headings()
        self.reference_span = self._find_reference_span()
        self.tier_spans = self._find_tier_spans()

    # -- parsing ---------------------------------------------------

    def _split_headings(self):
        """Return [(level, title, start_line, end_line_exclusive)] for every heading."""
        found = []
        in_fence = False
        for i, line in enumerate(self.lines):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
            if m:
                found.append([len(m.group(1)), m.group(2), i, None])
        for idx, item in enumerate(found):
            level = item[0]
            end = len(self.lines)
            for later in found[idx + 1:]:
                if later[0] <= level:
                    end = later[2]
                    break
            item[3] = end
        return [tuple(x) for x in found]

    @staticmethod
    def _normalise(title):
        t = title.lower().strip()
        t = re.sub(r"^tier\s*[:.]?\s*", "", t)
        t = re.sub(r"[^a-z0-9 ()]+", " ", t)
        return re.sub(r"\s+", " ", t).strip()

    def _find_reference_span(self):
        for level, title, start, end in self.sections:
            if self._normalise(title) in REFERENCE_HEADINGS:
                return (start, len(self.lines))
        return None

    def _find_tier_spans(self):
        spans = {}
        for level, title, start, end in self.sections:
            norm = self._normalise(title)
            for tier, aliases in TIER_ALIASES.items():
                if norm in aliases and tier not in spans:
                    spans[tier] = (start, end)
        return spans

    # -- views -----------------------------------------------------

    def full_text(self):
        return self.raw

    def body_text(self):
        """Everything except the reference list and fenced code."""
        if self.reference_span:
            text = "\n".join(self.lines[: self.reference_span[0]])
        else:
            text = self.raw
        return CODE_FENCE.sub("", text)

    def reference_text(self):
        if not self.reference_span:
            return ""
        return "\n".join(self.lines[self.reference_span[0]: self.reference_span[1]])

    def tier_text(self, tier):
        span = self.tier_spans.get(tier)
        if not span:
            return ""
        return "\n".join(self.lines[span[0]: span[1]])

    def tiers_present(self):
        return sorted(self.tier_spans.keys())

    def prose_sentences(self):
        text = self.body_text()
        text = re.sub(r"^\s{0,3}#{1,6}\s.*$", "", text, flags=re.MULTILINE)   # headings
        text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)          # bullets
        text = re.sub(r"\[\d+\]", "", text)                                    # citations
        text = re.sub(r"[*_`]", "", text)
        guard = text
        for abbr in ABBREVIATIONS:
            guard = guard.replace(abbr, abbr.replace(".", "\x00"))
        parts = re.split(r"(?<=[.!?])\s+", guard)
        out = []
        for part in parts:
            part = part.replace("\x00", ".").strip()
            if len(part.split()) >= 3:
                out.append(part)
        return out

    def word_count(self):
        text = re.sub(r"^\s{0,3}#{1,6}\s", "", self.body_text(), flags=re.MULTILINE)
        return len(re.findall(r"[A-Za-z0-9']+", text))

    def subsection_titles_within(self, span):
        titles = []
        for level, title, start, end in self.sections:
            if span[0] < start < span[1]:
                titles.append((self._normalise(title), start, end))
        return titles

    def bullet_count(self, start, end):
        n = 0
        for line in self.lines[start:end]:
            if re.match(r"^\s*(?:[-*+]|\d+\.)\s+\S", line):
                n += 1
        return n


# ---------------------------------------------------------------- helpers


def context(text, start, end, width=50):
    lo = max(0, start - width)
    hi = min(len(text), end + width)
    return re.sub(r"\s+", " ", text[lo:hi]).strip()


def finding(rule_id, severity, description, matched, ctx, line=None):
    item = {
        "rule_id": rule_id,
        "severity": severity,
        "description": description,
        "matched_text": matched,
        "context": ctx,
    }
    if line is not None:
        item["line"] = line
    return item


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def phrase_pattern(phrase):
    """Word-boundary, case-insensitive pattern that tolerates the trailing comma
    variants in the banned list (for example 'additionally,')."""
    escaped = re.escape(phrase)
    lead = r"(?<![A-Za-z])" if phrase[:1].isalnum() else ""
    trail = r"(?![A-Za-z])" if phrase[-1:].isalnum() else ""
    return re.compile(lead + escaped + trail, re.IGNORECASE)


# ---------------------------------------------------------------- rules


def scope_text(doc, scope, brief=None):
    """Resolve a rule scope string to the text it applies to."""
    if scope in (None, "body_and_headings"):
        return [("document", doc.full_text())]
    if scope == "body":
        return [("body", doc.body_text())]
    if scope and scope.startswith("tier:"):
        out = []
        for tier in scope.split(":", 1)[1].split(","):
            tier = tier.strip()
            text = doc.tier_text(tier)
            if text:
                out.append(("tier:" + tier, text))
        return out
    return [("document", doc.full_text())]


def run_pattern_rule(doc, rule, brief):
    out = []
    pattern = re.compile(rule["pattern"])
    for label, text in scope_text(doc, rule.get("scope"), brief):
        for m in pattern.finditer(text):
            out.append(finding(rule["id"], rule["severity"],
                               rule["description"] + " (" + label + ")",
                               m.group(0), context(text, m.start(), m.end()),
                               line_of(text, m.start())))
    return out


def run_phrase_rule(doc, rule, brief):
    out = []
    exclude_refs = rule["id"].startswith("UK-")
    for label, text in scope_text(doc, rule.get("scope"), brief):
        if exclude_refs and label == "document":
            text = doc.body_text()
            label = "body (reference list excluded)"
        for phrase in rule.get("banned_phrases", []):
            for m in phrase_pattern(phrase).finditer(text):
                out.append(finding(rule["id"], rule["severity"],
                                   rule["description"] + " (" + label + ")",
                                   m.group(0), context(text, m.start(), m.end()),
                                   line_of(text, m.start())))
    return out


LIST_MARKER = re.compile(r"^(\s*)(?:[-*+]|\d+[.)])(\s)", re.MULTILINE)
HRULE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$", re.MULTILINE)
TABLE_RULE = re.compile(r"^\s*\|?[\s:|-]{5,}\|?\s*$", re.MULTILINE)


def rule_dash_002(doc, rule):
    """Space-hyphen-space in prose.

    Markdown structure uses the same character sequence for list markers,
    horizontal rules and table separators. Those are blanked out before the
    configured pattern runs, so the rule catches a parenthetical dash in a
    sentence and leaves valid markup alone.
    """
    text = doc.body_text()
    cleaned = HRULE.sub(lambda m: " " * len(m.group(0)), text)
    cleaned = TABLE_RULE.sub(lambda m: " " * len(m.group(0)), cleaned)
    cleaned = LIST_MARKER.sub(lambda m: m.group(1) + " " * (m.end() - m.start() - len(m.group(1))),
                              cleaned)
    out = []
    for m in re.compile(rule["pattern"]).finditer(cleaned):
        out.append(finding(rule["id"], rule["severity"],
                           rule["description"] + " (body)",
                           m.group(0), context(text, m.start(), m.end()),
                           line_of(text, m.start())))
    return out


def rule_phrase_002(doc, rule):
    """Warn when more than max_allowed_per_article paragraphs open with a
    transition word."""
    pattern = re.compile(rule["pattern"])
    text = doc.body_text()
    hits = list(pattern.finditer(text))
    limit = rule.get("max_allowed_per_article", 2)
    if len(hits) <= limit:
        return []
    out = []
    for m in hits[limit:]:
        out.append(finding(rule["id"], rule["severity"],
                           rule["description"] + " (limit " + str(limit) + ")",
                           m.group(0), context(text, m.start(), m.end()),
                           line_of(text, m.start())))
    return out


THREE_ITEM = re.compile(
    r"\b[^,.;:]{2,40},\s+[^,.;:]{2,40}[,]?\s+(?:and|or)\s+[^,.;:]{2,40}", re.IGNORECASE)


def rule_phrase_003(doc, rule):
    sentences = doc.prose_sentences()
    if len(sentences) < 8:
        return []
    hits = [s for s in sentences if THREE_ITEM.search(s)]
    ratio = float(len(hits)) / len(sentences)
    if ratio <= rule.get("threshold", 0.3):
        return []
    return [finding(rule["id"], rule["severity"],
                    rule["description"],
                    "%d of %d sentences (%.0f%%)" % (len(hits), len(sentences), ratio * 100),
                    " | ".join(s[:70] for s in hits[:3]))]


def rule_phrase_004(doc, rule):
    sentences = doc.prose_sentences()
    if len(sentences) < 8:
        return []
    lengths = [len(s.split()) for s in sentences]
    sd = statistics.pstdev(lengths)
    if sd >= rule.get("threshold", 4):
        return []
    return [finding(rule["id"], rule["severity"],
                    rule["description"],
                    "standard deviation %.1f words over %d sentences" % (sd, len(sentences)),
                    "mean %.1f words" % (sum(lengths) / float(len(lengths))))]


CITE_MARKER = re.compile(r"\[(\d{1,3})\]")
REF_ENTRY = re.compile(r"^\s*(?:\[(\d{1,3})\]|(\d{1,3})[.)])\s+\S", re.MULTILINE)


def rule_cite_001(doc, rule):
    body = doc.body_text()
    refs = doc.reference_text()
    used = set(int(m.group(1)) for m in CITE_MARKER.finditer(body))
    listed = set()
    for m in REF_ENTRY.finditer(refs):
        listed.add(int(m.group(1) or m.group(2)))
    out = []
    if not refs and used:
        out.append(finding(rule["id"], rule["severity"],
                           "Citation markers present but no reference list found",
                           sorted(used).__repr__(), ""))
        return out
    missing = sorted(used - listed)
    orphan = sorted(listed - used)
    if missing:
        out.append(finding(rule["id"], rule["severity"],
                           "In-text markers with no reference entry",
                           ", ".join("[%d]" % n for n in missing), ""))
    if orphan:
        out.append(finding(rule["id"], rule["severity"],
                           "Reference entries never cited in the text",
                           ", ".join(str(n) for n in orphan), ""))
    return out


def rule_cite_002(doc, rule):
    out = []
    for label, text in scope_text(doc, rule.get("scope")):
        for m in CITE_MARKER.finditer(text):
            out.append(finding(rule["id"], rule["severity"],
                               rule["description"] + " (" + label + ")",
                               m.group(0), context(text, m.start(), m.end()),
                               line_of(text, m.start())))
    return out


def rule_struct_001(doc, rule, brief):
    """Structure against the brief: tier blocks, key learning points, FAQs,
    reference list, word count."""
    out = []
    sev = rule["severity"]
    desc = rule["description"]

    def fail(msg, matched=""):
        out.append(finding(rule["id"], sev, desc + ": " + msg, matched, ""))

    required = brief.get("tiers_required") or []
    for tier in required:
        if tier not in doc.tier_spans:
            fail("no content block found for tier '%s'" % tier, tier)

    outreq = brief.get("output_requirements") or {}
    klp = outreq.get("key_learning_points_per_tier") or {}
    lo, hi = klp.get("min"), klp.get("max")
    for tier in required:
        span = doc.tier_spans.get(tier)
        if not span:
            continue
        block = None
        for title, start, end in doc.subsection_titles_within(span):
            if title in KLP_HEADINGS:
                block = (start, end)
                break
        if block is None:
            fail("tier '%s' has no key learning points block" % tier, tier)
            continue
        n = doc.bullet_count(block[0] + 1, block[1])
        if lo is not None and n < lo:
            fail("tier '%s' has %d key learning points, minimum %d" % (tier, n, lo), tier)
        elif hi is not None and n > hi:
            fail("tier '%s' has %d key learning points, maximum %d" % (tier, n, hi), tier)

    faq = outreq.get("faqs_patient_level") or {}
    if faq and "patient" in required:
        span = doc.tier_spans.get("patient")
        block = None
        if span:
            for title, start, end in doc.subsection_titles_within(span):
                if title in FAQ_HEADINGS:
                    block = (start, end)
                    break
        if block is None:
            fail("patient tier has no FAQ block")
        else:
            n = len(re.findall(r"^\s*(?:\*\*Q|Q[.:]|####\s)", "\n".join(
                doc.lines[block[0] + 1: block[1]]), re.MULTILINE))
            if faq.get("min") is not None and n < faq["min"]:
                fail("patient FAQ block has %d questions, minimum %d" % (n, faq["min"]))
            elif faq.get("max") is not None and n > faq["max"]:
                fail("patient FAQ block has %d questions, maximum %d" % (n, faq["max"]))

    if doc.reference_span is None and CITE_MARKER.search(doc.body_text()):
        fail("no reference list")

    wc = outreq.get("target_word_count") or {}
    n = doc.word_count()
    if wc.get("min") is not None and n < wc["min"]:
        fail("word count %d below the brief minimum %d" % (n, wc["min"]))
    elif wc.get("max") is not None and n > wc["max"]:
        fail("word count %d above the brief maximum %d" % (n, wc["max"]))

    return out


def condition_met(expr, brief):
    """Evaluate the small set of conditional_on expressions the config uses."""
    if not expr:
        return True
    m = re.match(r"^\s*brief\.([A-Za-z0-9_.]+)\s*==\s*(true|false)\s*$", expr)
    if not m:
        return True
    node = brief
    for part in m.group(1).split("."):
        if not isinstance(node, dict):
            return False
        node = node.get(part)
    return bool(node) is (m.group(2) == "true")


# ---------------------------------------------------------------- entry point


def load_rules(path=None):
    """Find lint_rules.json. In Lambda the config is packaged next to this file;
    in the repo it lives under pipeline/config/. LINT_RULES_PATH overrides both."""
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        path,
        os.environ.get("LINT_RULES_PATH"),
        os.path.join(here, "lint_rules.json"),
        os.path.join(here, "..", "..", "config", "lint_rules.json"),
    ]
    for candidate in candidates:
        if candidate and os.path.exists(candidate):
            with open(candidate, "r") as fh:
                return json.load(fh)
    raise IOError("lint_rules.json not found; set LINT_RULES_PATH")


def lint(text, brief=None, rules=None):
    """Return a lint report dict. pass is False if any 'fail' rule fired."""
    brief = brief or {}
    rules = rules or load_rules()
    doc = Document(text)
    findings = []

    for rule in rules.get("rules", []):
        rid = rule["id"]
        if not condition_met(rule.get("conditional_on"), brief):
            continue
        if rid == "DASH-002":
            findings += rule_dash_002(doc, rule)
        elif rid == "PHRASE-002":
            findings += rule_phrase_002(doc, rule)
        elif rid == "PHRASE-003":
            findings += rule_phrase_003(doc, rule)
        elif rid == "PHRASE-004":
            findings += rule_phrase_004(doc, rule)
        elif rid == "CITE-001":
            findings += rule_cite_001(doc, rule)
        elif rid == "CITE-002":
            findings += rule_cite_002(doc, rule)
        elif rid == "STRUCT-001":
            findings += rule_struct_001(doc, rule, brief)
        elif rule.get("banned_phrases"):
            findings += run_phrase_rule(doc, rule, brief)
        elif rule.get("pattern"):
            findings += run_pattern_rule(doc, rule, brief)

    fails = [f for f in findings if f["severity"] == "fail"]
    warns = [f for f in findings if f["severity"] == "warn"]
    return {
        "lint_version": rules.get("lint_version"),
        "pass": len(fails) == 0,
        "fail_count": len(fails),
        "warn_count": len(warns),
        "findings": findings,
        "document": {
            "word_count": doc.word_count(),
            "tiers_present": doc.tiers_present(),
            "has_reference_list": doc.reference_span is not None,
            "sentence_count": len(doc.prose_sentences()),
        },
    }


def autofix_quotes(text):
    """QUOTE-001 autofix: normalise curly quotation marks to straight."""
    for bad, good in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"')):
        text = text.replace(bad, good)
    return text
