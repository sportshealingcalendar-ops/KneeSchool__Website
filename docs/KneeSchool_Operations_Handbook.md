# KneeSchool Operations Handbook

Version 1.0. 22 September 2026.
Owner: Editor in Chief. Review cycle: quarterly, or immediately on any pipeline change.

---

## 1. Purpose and Authority

This handbook is the single operating reference for KneeSchool content production. It defines the article template, editorial standards, the QA Manual, the approved prompt library, version control, and the operating calendar.

**Authority rule.** Where this handbook and any other document disagree, this handbook wins. That includes KneeSchool_AI_Agent_Prompts.md, the build handover, the brief template, and prior playbook drafts. Machine configuration (config/lint_rules.json, the brief template, the Bedrock prompt store) must be regenerated from this handbook, never the reverse. The machine-readable template block in Section 10 exists for that purpose.

**Adjudications made in this version:**

1. **Key Learning Points are per tier, not per article.** Each tier block ends with its own Key Learning Points, 3 to 5 bullets. The build handover's single-section wording is superseded and should be corrected or retired. Rationale: a single summary cannot serve reading age 12 and a consultant at the same time; the spiral principle requires each tier to close its own loop; and the deployed machine configuration (brief template field key_learning_points_per_tier and lint rule STRUCT-001) already enforces the per-tier form. The handbook confirms the machine configuration.
2. **FAQs are per article, carried by the Patient tier.** 3 to 5 question-and-answer pairs, present exactly when the Patient tier is present, located inside the Patient tier block. This matches both the agent prompts and the brief template; no other tier carries FAQs.
3. **QA order is verify before style.** The original playbook wording listed assistant edit before evidence check. The built pipeline verifies facts first, then styles, so that styling can never alter unverified prose and verification is never invalidated by later edits. The handbook adopts the pipeline order (Section 5).

---

## 2. The Seven-Tier Spiral

The spiral has seven tiers. Section 0 Junior Academy sits below Patient. Every page declares in its brief which tiers it carries; few pages carry all seven.

| # | Tier | Audience | Register |
|---|------|----------|----------|
| 1 | Junior | School age, roughly 13 to 18 | Plain English, reading age 12 to 14 |
| 2 | Patient | Adults seeking to understand their knee | Plain English, warm, precise |
| 3 | Medical Student | Undergraduate medicine | Foundation academic |
| 4 | MRCS | Core surgical trainees | Applied academic |
| 5 | FRCS (Tr and Orth) | Higher specialty trainees | Examination-standard academic |
| 6 | Fellowship | Post-CCT knee fellows | Advanced technical |
| 7 | Consultant | Established consultants | Peer to peer, controversy and evidence |

Spiral rule: each tier deepens the tier below and never repeats it. Nothing in a lower tier may contradict a higher tier. Duplication across pages is controlled by the brief's must_not_cover list.

---

## 3. The Article Template

This section is definitive. Agent 1 drafts to it, lint rule STRUCT-001 enforces it, and consultants review against it. Where any other document describes a different structure, this section governs.

### 3.1 Core skeleton (all page types)

Order is fixed:

1. **Title** (H1). Matches the Master Publishing Architecture page title.
2. **Summary line.** One sentence, plain English, no citation markers.
3. **Tier blocks**, in ascending tier order, only the tiers the brief requires. Tier block headings are exact strings (H2):
   - `For Young Learners` (Junior)
   - `For Patients` (Patient)
   - `For Medical Students` (Medical Student)
   - `MRCS Level` (MRCS)
   - `FRCS Level` (FRCS)
   - `Fellowship Level` (Fellowship)
   - `Consultant Perspective` (Consultant)
4. **Explore Further** (H2). Internal cross-links to sibling and deeper spiral pages, as placeholders in the format `[[page_id | link text]]`.
5. **References** (H2). One numbered list for the whole article. Never per tier.

### 3.2 Inside a tier block

Every tier block, whatever the page type, has this shape:

1. Body sections for the page type (Section 3.4), headed at H3.
2. **Key Learning Points** (H3). 3 to 5 bullets. Genuine summaries of the block above, not copied sentences. Present in every tier block without exception.
3. Tier-specific closers:
   - **Junior:** where the page touches symptoms or injury, the block ends with the standard message: "If any of this sounds like something happening to you, speak to a parent, teacher, coach or doctor." No citation markers anywhere in the block. No FAQs.
   - **Patient:** after Key Learning Points, a **Frequently Asked Questions** (H3) section of 3 to 5 question-and-answer pairs, then the standard when-to-seek-help message. No citation markers anywhere in the block.
   - **Medical Student and above:** in-text citation markers `[n]` are required for every statistic, incidence figure, indication, outcome claim and guideline statement.

FAQ rule stated plainly: FAQs are required exactly when the Patient tier is present, they live inside the Patient tier block, and they number 3 to 5. No other tier carries FAQs.

### 3.3 References

- Position: article level, final section.
- Numbering: order of first citation in the body (Medical Student tier onward, since lower tiers carry no markers).
- Format, journal article: Authors (first six, then et al). Title. Journal abbreviation. Year;volume(issue):pages. DOI or PMID.
- Format, book: Authors or editors. Title. Edition. Publisher; year. Chapter and pages where used.
- Format, guideline: Issuing body. Title. Reference code where one exists. Year. Date last verified by KneeSchool.
- Every entry must have been retrieved and read during generation or verification. A missing reference is acceptable. An invented one is a critical failure and fails the page.
- US spellings inside verbatim titles are left untouched; the reference list is excluded from UK spelling lint.

### 3.4 Page types

Three page types genuinely differ in body structure. Any page not listed maps to the nearest type; the brief names the type.

**Anatomy page.** Body sections per tier, in order, drawn from: Structure and Location; Relations; Blood Supply and Innervation; Function; Clinical Relevance. Lower tiers use the subset that fits their depth (Junior typically Structure and Function only). FRCS and above add surgical anatomy, variants and footprint or attachment detail under Clinical Relevance.
Word count: 800 to 1800 for the whole article.

**Condition page.** Body sections per tier, in order, drawn from: Definition; Who Gets It (epidemiology); Causes and Risk Factors; How It Presents; Examination; Investigations and Imaging; Management Overview; Rehabilitation Outline; Complications and Prognosis; Controversies and Evidence (FRCS and above only). Management is educational, never individualised advice; Patient and Junior tiers describe what clinicians may do, not what the reader should do.
Word count: 1200 to 2500.

**Procedure page.** Body sections per tier, in order, drawn from: What the Operation Is; Indications; Contraindications; Before the Operation (work-up and consent points); The Operation (plain overview at Patient tier; structured technique summary at FRCS and above; never step-by-step operative instruction below FRCS); After the Operation and Rehabilitation; Risks and Complications; Outcomes and Evidence; Variations and Controversies (Fellowship and Consultant only). Junior tier on procedure pages is careers-flavoured (what the operation is and who performs it), never technique.
Word count: 1500 to 3000.

Word count ranges are handbook defaults; a brief may override within reason via output_requirements, and the brief value then governs that page.

### 3.5 What the template forbids

- Key Learning Points at article level.
- FAQs outside the Patient tier block.
- Citation markers in Junior or Patient tier body text.
- Per-tier reference lists.
- Any section order other than the one above.
- Em dashes, en dashes, figure dashes, horizontal bars, and space-hyphen-space, anywhere, including ranges. Ranges are written "5 to 10 years".

---

## 4. Editorial Standards

**Language.** British English throughout body text and headings. Paracetamol, not the US name. Orthopaedic, paediatric, oedema, haemarthrosis, anaesthetic, randomised, analysed, artefact, ageing.

**Voice per tier.**
- Junior: friendly, concrete, curious. Short sentences. No jargon without an immediate plain gloss.
- Patient: warm, precise, honest about uncertainty, never patronising.
- Medical Student: clear foundations. Definitions before detail.
- MRCS: applied and examination-aware.
- FRCS: evidence-led, decision-focused, viva-ready reasoning.
- Fellowship: technical depth, honest about technique variation.
- Consultant: peer register, evidence appraisal, open controversy.

**Sentence and paragraph discipline.** Vary sentence length deliberately; mix short declaratives with longer explanatory sentences. Paragraphs of 2 to 5 sentences. Headed sections stay short; no unbroken textbook prose. At most two paragraph-opening transition words per article. Avoid the three-item list as a default rhythm.

**Terminology consistency.** One term per concept per article: define the full term once with its abbreviation, for example anterior cruciate ligament (ACL), then use the abbreviation. Units are SI and consistent. Eponyms carry a plain descriptor at first mention.

**Stating uncertainty.** Where evidence is conflicting, weak or absent, say so in the body, in the tier where it matters. FRCS and above use a Controversies or Evidence heading for it. Never manufacture consensus, and never soften a limitation out of a lower tier if it changes what a patient would understand.

**Expert opinion versus evidence.** Any claim resting on expert opinion rather than published evidence is labelled in the text, for example "(expert consensus)" or "in the senior author's practice", and is never given a citation marker that implies trial evidence.

**Banned phrasing.** The banned phrase list in config/lint_rules.json is authoritative for all published prose and for this handbook itself. Additions to the list follow the monthly sampling routine in Section 8.

---

## 5. The QA Manual

Four tiers, in pipeline order. A page must pass each tier in sequence. Tier 4 is mandatory and cannot be bypassed; the state machine contains no path to publication that skips it.

**Tier 1. AI draft (Agent 1 plus automated gates).** Checklist:
- Brief loaded and scope statement present; page type identified.
- Every required tier block present; no extra tiers.
- Source minimum met: at least one textbook or review source, peer-reviewed support for every clinical claim.
- No source cited that was not retrieved in session.
- Handoff JSON complete, including claims_needing_verification.

**Tier 2. Evidence verification (Agent 2 plus human evidence checker).** Checklist:
- Every reference located and confirmed to exist as cited.
- Every listed claim classified (verified, partially supported, unsupported, contradicted, unverifiable), with before-and-after text for any correction.
- Five highest-stakes claims independently checked against current literature.
- Guideline versions confirmed current and dated.
- Red flag scan run (list below); more than three failed claims returns the page to Tier 1.
- Human evidence checker spot-checks at least two corrections per page and signs the verification report.

**Tier 3. Editorial and style (Agent 3, lint gate, assistant editor).** Checklist:
- No fact, figure, citation marker, drug name, procedure name or safety statement altered.
- Dash, banned phrase, UK spelling, citation bijection and structure lint all pass.
- Junior and Patient tiers read at target level; plain-English review recorded.
- Terminology standardised; tier layering coherent; no lower tier contradicting a higher tier.
- Assistant editor reads the full article once, top to bottom, as a reader.

**Tier 4. Consultant review.** Checklist:
- Clinical accuracy and safety across every tier.
- Verification report and warn-level lint flags reviewed.
- Escalated judgement calls resolved.
- Decision recorded: approve, amend (edits captured), or reject with reason.
- Sign-off named and dated. No publication without it.

**Red flag list** (any hit is reported; fabrication fails the page outright):
- Fabricated or unlocatable citation.
- Unsupported statistic or overconfident claim.
- Incorrect anatomy or wrong examination interpretation.
- Outdated surgical recommendation or superseded guideline.
- Product, supplement or clinical service promotion; any commercial content at all in a page carrying the Junior tier.
- Clinical advice patterns in Junior or Patient tiers.
- Close paraphrase or reproduction of copyrighted source text.
- Missing safety caveat, consent point or complication that a reasonable reviewer would expect.
- Tier contradiction within the article.

---

## 6. Approved Prompt Library

The prompt library is the versioned set of texts that may run in production. Nothing else may run.

| Item | Version | Location |
|------|---------|----------|
| Agent 1 Generator prompt | 1.0 | KneeSchool_AI_Agent_Prompts.md; Bedrock prompt store |
| Agent 2 Verifier prompt | 1.0 | same |
| Agent 3 Style prompt | 1.0 | same |
| Content brief template | 1.0 | config/brief_template_example_1.2.3.json |
| Lint rules | 1.0 | config/lint_rules.json |

Governance:
- Only the Editor in Chief approves prompt changes.
- A change is a deployment: new version number, tracker entry, and every execution records which versions it ran under.
- Prompt experiments run in the dev stack only.
- The Agent 1 prompt and STRUCT-001 must be updated to cite this handbook (Sections 3 and 10) as their source of structure. Until then, this handbook's per-tier ruling governs.

Note: the build handover is referenced as also listing prompt library contents. That document was not available when this handbook was written; if its list differs from the table above, the table governs and the handover should be corrected (see Open Questions).

---

## 7. Version Control and Production Status

### 7.1 Artefact states

Each page moves through four states, stored under pipeline/{page_id}/ with S3 versioning on:

| State | Artefact | Requires |
|-------|----------|----------|
| Draft | draft_vN.md plus handoff | Tier 1 checklist passed |
| Checked | verified_vN.md and styled_vN.md plus reports | Tiers 2 and 3 passed, lint clean |
| Reviewed | consultant_review.json | Tier 4 approval recorded |
| Published | published/{page_id}/ | CMS live, metadata and curriculum tags written, tracker updated |

A page moves forward one state at a time. Any content change after Reviewed returns the page to Checked and re-triggers Tier 4.

### 7.2 Production status fields (tracker)

- source_status: not_started, partial, complete
- draft_status: not_started, ai_draft, edited
- qa_status: assistant_checked, evidence_checked, consultant_reviewed
- publication_status: ready, scheduled, published, refresh_due
- Plus: priority, tiers_required, curriculum_tags, consultant, reviewed_at, published_at, next_review_due, regen_count, red_flag_count.

---

## 8. Operating Calendar

**Weekly schedule:**
- Monday: source day. Acquire and ingest sources for the coming batch; knowledge base sync check.
- Tuesday: drafting day. Batch pipeline runs (concurrency 5); Tier 1 outputs land.
- Wednesday: verification day. Tier 2 triage; failed pages investigated for source gaps rather than blindly retried.
- Thursday: editorial day. Tier 3; assistant editor pass; consultant review packs assembled.
- Friday: review and publication day. Consultant sign-offs; approved pages published; weekly KPI report (pages by state, curriculum coverage, red flags, queue age) issued.

**Monthly:** sample five published pages for residual AI tells; add findings to the banned list as a lint config deployment. Review warn-level lint trends.

**Annual review and refresh:** next_review_due is set at publication plus 12 months. A due page re-enters the pipeline at Tier 2 with a refresh brief; guideline currency is re-checked; the page returns to Reviewed before the refreshed version replaces the live one. A guideline watch task also runs quarterly against NICE, BOAST and society updates, and may pull a page's review forward.

---

## 9. Junior Tier Governance (restated, binding)

- No commercial content of any kind in any page carrying the Junior tier: no product placement, no supplements, no clinical service promotion. This applies to the whole of Section 0.
- No clinical advice. Symptom-related Junior content ends with the standard speak-to-an-adult message.
- Reading age 12 to 14, with plain-English review recorded at Tier 3.
- Interactive features are pre-moderated; no open chat or direct messaging for under-18s.
- Data protection by design under UK GDPR and the ICO Age Appropriate Design Code: minimal data collection, no behavioural advertising, parental consent where accounts exist, high-privacy defaults.
- A named safeguarding lead signs off outreach activity and any content featuring identifiable young people.

---

## 10. Machine-Readable Article Template

Regenerate STRUCT-001 and the brief template defaults from this block. Do not hand-edit the lint config independently of it.

```json
{
  "article_template_version": "1.0",
  "source_of_truth": "KneeSchool_Operations_Handbook.md section 3",
  "tier_order": ["junior", "patient", "medical_student", "mrcs", "frcs", "fellowship", "consultant"],
  "tier_headings": {
    "junior": "For Young Learners",
    "patient": "For Patients",
    "medical_student": "For Medical Students",
    "mrcs": "MRCS Level",
    "frcs": "FRCS Level",
    "fellowship": "Fellowship Level",
    "consultant": "Consultant Perspective"
  },
  "article_sections_order": ["title", "summary_line", "tier_blocks", "explore_further", "references"],
  "tier_block_sections_order": ["body_sections", "key_learning_points", "tier_closers"],
  "key_learning_points": {
    "policy": "per_tier",
    "per_article": false,
    "heading": "Key Learning Points",
    "min_bullets": 3,
    "max_bullets": 5,
    "required_in_every_tier_block": true
  },
  "faqs": {
    "required_when": "patient_tier_present",
    "location": "patient_tier_block",
    "heading": "Frequently Asked Questions",
    "min": 3,
    "max": 5,
    "allowed_in_other_tiers": false
  },
  "citations": {
    "marker_format": "[n]",
    "markers_allowed_tiers": ["medical_student", "mrcs", "frcs", "fellowship", "consultant"],
    "markers_forbidden_tiers": ["junior", "patient"],
    "reference_list": {
      "location": "article_level_final_section",
      "heading": "References",
      "numbering": "order_of_first_citation",
      "per_tier_lists_allowed": false,
      "uk_spelling_lint_excluded": true
    }
  },
  "tier_closers": {
    "junior": {
      "speak_to_adult_message_required_when": "symptom_or_injury_content_present",
      "message": "If any of this sounds like something happening to you, speak to a parent, teacher, coach or doctor."
    },
    "patient": {
      "when_to_seek_help_message_required": true
    }
  },
  "page_types": {
    "anatomy": {
      "body_sections": ["structure_and_location", "relations", "blood_supply_and_innervation", "function", "clinical_relevance"],
      "body_sections_rule": "ordered_subset_per_tier",
      "word_count": {"min": 800, "max": 1800}
    },
    "condition": {
      "body_sections": ["definition", "epidemiology", "causes_and_risk_factors", "presentation", "examination", "investigations_and_imaging", "management_overview", "rehabilitation_outline", "complications_and_prognosis", "controversies_and_evidence"],
      "body_sections_rule": "ordered_subset_per_tier; controversies_and_evidence frcs_and_above_only",
      "word_count": {"min": 1200, "max": 2500}
    },
    "procedure": {
      "body_sections": ["what_the_operation_is", "indications", "contraindications", "before_the_operation", "the_operation", "after_the_operation_and_rehabilitation", "risks_and_complications", "outcomes_and_evidence", "variations_and_controversies"],
      "body_sections_rule": "ordered_subset_per_tier; technique_detail frcs_and_above_only; variations_and_controversies fellowship_and_above_only; junior_block_careers_framing_only",
      "word_count": {"min": 1500, "max": 3000}
    }
  },
  "word_count_override": "brief.output_requirements.target_word_count overrides page_type default when present",
  "cross_links": {
    "heading": "Explore Further",
    "placeholder_format": "[[page_id | link text]]"
  },
  "forbidden": [
    "article_level_key_learning_points",
    "faqs_outside_patient_tier",
    "citation_markers_in_junior_or_patient_body",
    "per_tier_reference_lists",
    "em_dash", "en_dash", "figure_dash", "horizontal_bar", "space_hyphen_space"
  ]
}
```

---

## 11. Open Questions

1. **Build handover reconciliation.** The build handover document was not available when this handbook was written. Its single Key Learning Points section is overruled here; someone holding the document should correct or retire that wording, and confirm its prompt library list matches Section 6.
2. **Word count defaults.** The anatomy, condition and procedure ranges are proposed defaults extending the pilot brief's 800 to 1600. Editor in Chief to confirm or adjust before the next batch run.
3. **Tier heading strings.** The seven exact heading strings must match the CMS and site templates. Engineering to confirm they render as designed before STRUCT-001 is regenerated; if the site uses different labels, change them here first, then regenerate.
4. **Reference style.** A Vancouver-derived format is specified. Confirm no society partnership requires a different house style.
5. **Additional page types.** Case pages (Section 13), examination pages (Section 4) and Junior careers pages may need variants of their own. Until defined here, they map to the nearest of the three types via the brief. Workable, but revisit after the first fifty pages.
6. **Named safeguarding lead.** Required by Junior governance; not yet appointed in any document available to me.
