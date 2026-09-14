"""Content brief validation.

Hand rolled rather than jsonschema so the Lambda bundle stays at zero
dependencies. It checks the field rules from the configuration reference,
including the governance rule that a brief containing a junior tier can never
allow commercial content.
"""

TIERS = ["junior", "patient", "medical_student", "mrcs", "frcs", "fellowship", "consultant"]
PRIORITIES = ["high", "medium", "low"]


class BriefError(ValueError):
    """Raised when a brief is rejected. The state machine treats this as a
    terminal failure: a malformed brief is an editorial problem, not a retry."""


def _require(brief, path, kind=None):
    node = brief
    for part in path.split("."):
        if not isinstance(node, dict) or part not in node:
            raise BriefError("missing required field: %s" % path)
        node = node[part]
    if kind is not None and not isinstance(node, kind):
        raise BriefError("field %s has the wrong type" % path)
    return node


def validate(brief):
    """Return the brief unchanged, or raise BriefError."""
    if not isinstance(brief, dict):
        raise BriefError("brief is not an object")

    _require(brief, "brief_version")
    page_id = _require(brief, "page_id")
    _require(brief, "title")

    tiers = _require(brief, "tiers_required", list)
    if not tiers:
        raise BriefError("tiers_required is empty")
    unknown = [t for t in tiers if t not in TIERS]
    if unknown:
        raise BriefError("unknown tier(s): %s" % ", ".join(unknown))

    scope = _require(brief, "scope", dict)
    if not scope.get("must_cover"):
        raise BriefError("scope.must_cover is empty")
    if "must_not_cover" not in scope:
        raise BriefError("scope.must_not_cover is required; it is what enforces the spiral")

    out = _require(brief, "output_requirements", dict)
    if out.get("language") != "en-GB":
        raise BriefError("output_requirements.language must be en-GB")
    for name in ("key_learning_points_per_tier", "target_word_count"):
        block = out.get(name) or {}
        lo, hi = block.get("min"), block.get("max")
        if lo is None or hi is None:
            raise BriefError("output_requirements.%s needs min and max" % name)
        if lo > hi:
            raise BriefError("output_requirements.%s has min above max" % name)

    gov = _require(brief, "governance", dict)
    junior_flagged = bool(gov.get("junior_tier_present"))
    junior_in_tiers = "junior" in tiers
    if junior_in_tiers and not junior_flagged:
        raise BriefError("junior tier requested but governance.junior_tier_present is false")
    if (junior_flagged or junior_in_tiers) and gov.get("commercial_content_allowed"):
        raise BriefError(
            "governance conflict for page %s: a brief with a junior tier cannot set "
            "commercial_content_allowed to true" % page_id)

    pipeline = brief.get("pipeline") or {}
    if pipeline.get("priority") and pipeline["priority"] not in PRIORITIES:
        raise BriefError("pipeline.priority must be one of %s" % ", ".join(PRIORITIES))

    return brief
