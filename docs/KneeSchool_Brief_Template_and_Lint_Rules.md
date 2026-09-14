# KneeSchool Pipeline Configuration
Two artefacts: (1) the content brief JSON template that starts every pipeline run, and (2) the lint configuration used by the deterministic style-gate Lambda.

---

## 1. Content Brief JSON Template

One brief per page, stored at s3://kneeschool-content/pipeline/{page_id}/brief.json. This is the input to Agent 1 and travels through the whole execution. Example populated for the pilot page.

```json
{
  "brief_version": "1.0",
  "page_id": "1.2.3",
  "title": "Menisci",
  "section": { "id": "1", "name": "Knee Fundamentals" },
  "chapter": { "id": "1.2", "name": "Basic Knee Anatomy" },

  "tiers_required": ["junior", "patient", "medical_student"],
  "tier_notes": {
    "junior": "Reading age 12 to 14. No clinical management content.",
    "patient": "Plain language. End with when-to-seek-help message.",
    "medical_student": "Foundation anatomy and function. No surgical technique."
  },

  "scope": {
    "must_cover": [
      "What the menisci are and where they sit",
      "Medial versus lateral meniscus basics",
      "Function: load sharing, stability, lubrication",
      "Why tears matter, in outline only",
      "Blood supply zones in simple terms (red, red-white, white)"
    ],
    "must_not_cover": [
      "Detailed MRI grading (belongs to 5.x Imaging)",
      "Repair versus meniscectomy decision-making (belongs to 7.x Surgery Academy)",
      "Root tear biomechanics (belongs to 2.5.7 and 2.6.4)"
    ],
    "sibling_pages": ["1.2.1", "1.2.2", "1.2.4", "1.2.5"],
    "deeper_spiral_pages": ["2.5", "2.6", "6.x meniscal tears", "7.x meniscal surgery"]
  },

  "curriculum_tags": ["MedStudent-Anatomy", "MRCS-A-feeder"],

  "source_requirements": {
    "kb_topic_filter": "meniscus",
    "minimum": {
      "textbook_or_review": 1,
      "peer_reviewed_for_clinical_claims": true
    },
    "preferred_recency_years": 10,
    "guidelines_expected": []
  },

  "output_requirements": {
    "language": "en-GB",
    "format": "markdown",
    "key_learning_points_per_tier": { "min": 3, "max": 5 },
    "faqs_patient_level": { "min": 3, "max": 5 },
    "target_word_count": { "min": 800, "max": 1600 },
    "internal_link_placeholders": true
  },

  "governance": {
    "commercial_content_allowed": false,
    "clinical_advice_allowed": false,
    "junior_tier_present": true
  },

  "pipeline": {
    "priority": "high",
    "requested_by": "editor",
    "created_at": "2026-08-28T00:00:00Z",
    "regen_count": 0,
    "consultant_assigned": null
  }
}
```

Field rules:
- governance.junior_tier_present = true automatically forces commercial_content_allowed = false (validated by the load-brief Lambda; a brief violating this is rejected before Generate runs).
- must_not_cover is as important as must_cover: it is what enforces the spiral and prevents duplication across 3000 pages.
- curriculum_tags are copied to the tracker and to published metadata unchanged.

---

## 2. Lint Configuration (style-lint Lambda)

Stored at s3://kneeschool-content/config/lint_rules.json, versioned. The Lambda applies rules in order; any "fail" rule failing returns pass=false and the offending matches, sending the draft back to Agent 3 (max 2 loops).

```json
{
  "lint_version": "1.0",
  "rules": [

    {
      "id": "DASH-001",
      "severity": "fail",
      "description": "No em dashes or en dashes anywhere, including ranges",
      "pattern": "[\\u2013\\u2014\\u2012\\u2015]",
      "scope": "body_and_headings",
      "note": "U+2012 figure dash and U+2015 horizontal bar included for completeness"
    },
    {
      "id": "DASH-002",
      "severity": "fail",
      "description": "Hyphen used as a range or parenthetical dash (space-hyphen-space)",
      "pattern": "\\s-\\s",
      "scope": "body"
    },
    {
      "id": "QUOTE-001",
      "severity": "warn",
      "description": "Curly quotes and apostrophes normalised to straight",
      "pattern": "[\\u2018\\u2019\\u201C\\u201D]",
      "autofix": "normalise"
    },

    {
      "id": "PHRASE-001",
      "severity": "fail",
      "description": "Banned AI-tell words and phrases (case-insensitive, word-boundary)",
      "banned_phrases": [
        "delve", "delves", "delving",
        "it is important to note", "it's important to note",
        "it is worth noting", "it's worth noting",
        "it should be noted",
        "in today's world", "in this day and age", "in the modern era",
        "in the realm of", "in the landscape of", "the landscape of",
        "in the world of", "the world of medicine",
        "plays a crucial role", "plays a vital role", "plays a key role",
        "plays a pivotal role", "plays an essential role",
        "a testament to", "stands as a testament",
        "navigate the complexities", "navigating the complexities",
        "unlock the", "unlocking the", "unleash",
        "harness the power", "harnessing the power",
        "leverage", "leveraging", "leverages",
        "seamless", "seamlessly",
        "robust framework",
        "game-changer", "game changer", "revolutionize", "revolutionise",
        "cutting-edge", "state-of-the-art",
        "embark on", "embarking on", "journey of discovery",
        "dive into", "diving into", "deep dive",
        "shed light on", "shedding light on",
        "at the end of the day",
        "when it comes to",
        "needless to say",
        "first and foremost",
        "last but not least",
        "in conclusion",
        "in summary, it is clear",
        "the bottom line is",
        "whether you are a", "whether you're a",
        "look no further",
        "rest assured",
        "elevate your", "empower", "empowering",
        "foster a deeper", "fostering a deeper",
        "a myriad of", "myriad of",
        "a plethora of",
        "vast array", "wide array of",
        "ever-evolving", "rapidly evolving landscape",
        "holistic approach",
        "tapestry", "rich tapestry",
        "underscores the importance", "underscore the importance",
        "highlights the importance of understanding",
        "crucial to understand",
        "vital to understand",
        "not only",
        "moreover",
        "furthermore",
        "additionally,",
        "overall,",
        "ultimately,",
        "notably,",
        "importantly,",
        "interestingly,",
        "let's explore", "let us explore",
        "let's take a look", "let's break down",
        "you might be wondering",
        "have you ever wondered",
        "picture this",
        "enter the",
        "meet the",
        "the beauty of",
        "the key takeaway",
        "key takeaways",
        "actionable insights",
        "best practices",
        "comprehensive guide", "comprehensive overview",
        "ultimate guide"
      ],
      "notes": [
        "not only: bans the 'not only X but also Y' construction; verifier-approved clinical text never needs it",
        "moreover/furthermore/additionally/overall/ultimately/notably/importantly/interestingly: banned as sentence openers; the trailing comma variants catch this",
        "best practices: allowed only inside a direct quotation from a cited guideline title"
      ]
    },
    {
      "id": "PHRASE-002",
      "severity": "warn",
      "description": "Flag (do not fail) if any paragraph opens with a transition word",
      "pattern": "(?m)^(However|Therefore|Thus|Hence|Consequently|Nevertheless|Nonetheless|Indeed|Similarly|Likewise|Meanwhile|Subsequently),",
      "max_allowed_per_article": 2
    },
    {
      "id": "PHRASE-003",
      "severity": "warn",
      "description": "Rule-of-three rhythm: flag if more than 30 percent of sentences contain a three-item comma list",
      "heuristic": "three_item_list_ratio",
      "threshold": 0.3
    },
    {
      "id": "PHRASE-004",
      "severity": "warn",
      "description": "Sentence length variance too low (uniform rhythm is an AI tell)",
      "heuristic": "sentence_length_stddev_min_words",
      "threshold": 4
    },

    {
      "id": "UK-001",
      "severity": "fail",
      "description": "US spellings banned",
      "banned_phrases": [
        "orthopedic", "orthopedics", "pediatric", "pediatrics",
        "anesthesia", "anesthetic", "hemorrhage", "hematoma", "hemarthrosis",
        "edema", "esophagus", "estrogen", "fetus" ,
        "center", "fiber", "tumor", "color", "labeled", "modeling",
        "randomized", "minimized", "stabilized", "immobilized", "analyzed",
        "counseling", "aging", "artifact",
        "gray zone", "acetaminophen"
      ],
      "exceptions": [
        "verbatim journal titles, society names and cited paper titles in the reference list (reference list is excluded from UK-001 scope)",
        "randomized/randomised: -ize forms permitted only inside reference list entries",
        "acetaminophen: body text must use paracetamol"
      ],
      "scope": "body_and_headings"
    },

    {
      "id": "CITE-001",
      "severity": "fail",
      "description": "Every in-text [n] marker has a matching reference entry and vice versa",
      "heuristic": "citation_reference_bijection"
    },
    {
      "id": "CITE-002",
      "severity": "fail",
      "description": "No citation markers inside Junior or Patient tier body text (references live at article level; lower tiers stay clean)",
      "scope": "tier:junior,patient",
      "pattern": "\\[\\d+\\]"
    },
    {
      "id": "STRUCT-001",
      "severity": "fail",
      "description": "Required blocks present per brief: tier blocks, key learning points, FAQs where required, reference list",
      "heuristic": "structure_against_brief"
    },
    {
      "id": "GOV-001",
      "severity": "fail",
      "description": "Commercial terms banned when brief.governance.commercial_content_allowed is false",
      "banned_phrases": ["OmKneeHealth", "Sportshealing", "our clinic", "book a consultation", "our products", "buy", "purchase", "discount"],
      "conditional_on": "brief.governance.commercial_content_allowed == false"
    },
    {
      "id": "GOV-002",
      "severity": "fail",
      "description": "Advice-pattern scan on Junior and Patient tiers",
      "banned_phrases": ["you should take", "we recommend you", "stop taking", "increase your dose", "you do not need to see a doctor"],
      "scope": "tier:junior,patient"
    }
  ],

  "reporting": {
    "output": "lint_report.json",
    "include_matched_text_with_50_char_context": true,
    "fail_fast": false
  }
}
```

Operating notes:
- fail rules block progression; warn rules go to the consultant review pack so a human sees them but the pipeline continues.
- fail_fast is off: the Lambda collects every violation in one pass so Agent 3 fixes them all in a single loop rather than ping-ponging.
- The banned list will grow. Treat lint_rules.json as versioned config: additions are a config deployment, logged in the tracker against every execution, so you can always answer "which rule set was this page published under".
- Suggested maintenance: monthly, sample five published pages, have a human note any residual AI tells, add them to PHRASE-001.
