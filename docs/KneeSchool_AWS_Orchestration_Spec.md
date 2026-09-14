# KneeSchool Content Pipeline — AWS Orchestration Specification

Version 0.1 (draft for technical review). Companion to KneeSchool_AI_Agent_Prompts.md.
Verified against AWS capabilities as of mid-2026: Bedrock AgentCore (GA April 2026), Step Functions native AgentCore integration, Strands Agents SDK, Bedrock Knowledge Bases and Guardrails.

---

## 1. Architecture Overview

Deterministic, auditable pipeline. Step Functions is the coordination layer (which agent runs, in what order, error handling); agents reason only within their bounded step. This rule-based pattern is preferred over a supervisor-agent pattern because medical content QA must be explainable and every stage must leave an audit trail.

```
EventBridge (tracker status change)
        |
        v
AWS Step Functions: kneeschool-content-pipeline
        |
  [1] Generate ----> AgentCore Runtime: agent-generator  (Claude, KB + PubMed tools)
        |
  [2] Verify ------> AgentCore Runtime: agent-verifier   (Claude, KB + PubMed tools)
        |----- FAILED? ----> loop to [1] (max 2 retries) ----> else HOLD queue
        |
  [3] Style -------> AgentCore Runtime: agent-styler     (Claude, no external tools)
        |
  [4] Dash/AI-tell lint (Lambda, deterministic regex gate)
        |
  [5] Human gate --> waitForTaskToken -> Consultant review app (Amplify) 
        |                                   approve / amend / reject
        |
  [6] Publish -----> Lambda -> CMS API (draft status) + S3 published/ + tracker update
        |
CloudWatch + X-Ray + AgentCore Observability (OpenTelemetry) throughout
DynamoDB: kneeschool-article-tracker (single source of truth for status)
```

---

## 2. S3 Layout (bucket: kneeschool-content)

Mirrors the Playbook repository structure and the Operations Handbook version-control rule (draft, checked, reviewed, published). Versioning ON; Object Lock (governance mode) on published/.

```
kneeschool-content/
  sources/                      <- knowledge base ingestion root
    acl/  pcl/  mcl/  plc/  meniscus/  cartilage/  patellofemoral/
    osteotomy/  arthroplasty/  paediatric/  rehabilitation/
    womens-health/  imaging/  research/  anatomy/  examination/
      textbook-extracts/   reviews/   landmark-papers/   guidelines/
      internal/            (own publications, lectures, surgical notes)
      metadata.jsonl       (one record per source: title, authors, year,
                            type, topic, quality_level, licence, notes)
  pipeline/
    {page_id}/
      brief.json            <- content brief (input to Agent 1)
      draft_v{n}.md         <- Agent 1 output
      draft_v{n}.handoff.json
      verified_v{n}.md      <- Agent 2 output + handoff
      verified_v{n}.handoff.json
      styled_v{n}.md        <- Agent 3 output + handoff
      styled_v{n}.handoff.json
      lint_report.json
      consultant_review.json
  published/
    {page_id}/final.md  final.html  references.json  curriculum_tags.json
```

Copyright rule enforced at ingestion: sources/ objects are tagged licence=internal-review-only; a bucket policy denies any Lambda except the KB ingestion role from reading textbook-extracts/, and agents are instructed to paraphrase, never reproduce.

---

## 3. Bedrock Knowledge Base

- Name: kb-kneeschool-sources. Vector store: S3 Vectors (cheapest at this scale) or OpenSearch Serverless if sub-second retrieval latency matters.
- Data source: s3://kneeschool-content/sources/ with metadata sidecar files enabling filtered retrieval: topic, source_type (review | landmark | textbook | guideline | internal), year, quality_level, tier_relevance.
- Chunking: hierarchical (parent 1500 tokens, child 300) — anatomy and technique material benefits from surrounding context.
- Sync: EventBridge rule on S3 PUT to sources/ triggers ingestion job; weekly full re-sync Sunday night per the weekly operating schedule (Monday = source day).
- Retrieval config per agent call: metadata filter on topic derived from page_id prefix, top-k 12, reranking on.

---

## 4. Agent Configurations (AgentCore Runtime, Strands Agents SDK)

Common: Claude (latest Sonnet-class on Bedrock) as foundation model; temperature 0.3 generator, 0.0 verifier, 0.4 styler; structured output schema = the handoff JSON contracts from the prompts document; AgentCore Observability enabled; session TTL 1 hour; each agent 3-5 tools maximum (tool-selection accuracy degrades beyond that).

### agent-generator
- System prompt: Agent 1 prompt.
- Tools (via AgentCore Gateway, MCP):
  1. kb_retrieve — Bedrock KB retrieval with metadata filters
  2. pubmed_search — Lambda wrapping NCBI E-utilities (esearch/efetch; API key; 3 req/s throttle)
  3. get_syllabus_page — Lambda reading the Master Architecture from DynamoDB (page, siblings, tiers required)
  4. get_style_guide — static S3 fetch
- Guardrail: gr-kneeschool-generate — denies individualised medical advice patterns, product/supplement promotion, PII echo.

### agent-verifier
- System prompt: Agent 2 prompt.
- Tools:
  1. pubmed_lookup — resolve PMID/DOI to authoritative record (existence check)
  2. crossref_lookup — DOI metadata verification
  3. kb_retrieve — confirm claims against repository sources
  4. guideline_fetch — allow-listed fetch of NICE/BOAST/society pages
- Hard rule in runtime config: verifier may not call any generation-oriented tool; output schema requires before/after for every correction.

### agent-styler
- System prompt: Agent 3 prompt. No external tools (deliberate — it must not introduce new facts).
- max_tokens sized to full article length; input = verified draft only, never the sources (prevents fact drift).

---

## 5. Step Functions State Machine (kneeschool-content-pipeline)

Standard workflow (not Express): executions may span days across the human gate; full execution history needed for audit. Sketch of states (ASL abbreviated):

```json
{
  "StartAt": "LoadBrief",
  "States": {
    "LoadBrief":   { "Type": "Task", "Resource": "lambda:load-brief", "Next": "Generate" },
    "Generate":    { "Type": "Task",
                     "Resource": "aws-sdk:bedrockagentcore:invokeAgentRuntime",
                     "Parameters": { "AgentRuntimeArn": "arn:...:agent-generator", "Payload.$": "$.brief" },
                     "Retry": [{ "ErrorEquals": ["States.TaskFailed"], "MaxAttempts": 2, "BackoffRate": 2 }],
                     "ResultPath": "$.draft", "Next": "PersistDraft" },
    "PersistDraft":{ "Type": "Task", "Resource": "lambda:persist-artifact", "Next": "Verify" },
    "Verify":      { "Type": "Task",
                     "Resource": "aws-sdk:bedrockagentcore:invokeAgentRuntime",
                     "Parameters": { "AgentRuntimeArn": "arn:...:agent-verifier" },
                     "ResultPath": "$.verified", "Next": "VerifyOutcome" },
    "VerifyOutcome": { "Type": "Choice",
                     "Choices": [
                       { "Variable": "$.verified.status", "StringEquals": "FAILED_RETURN_TO_GENERATION",
                         "Next": "CheckRegenCount" }],
                     "Default": "Style" },
    "CheckRegenCount": { "Type": "Choice",
                     "Choices": [{ "Variable": "$.regen_count", "NumericLessThan": 2, "Next": "Generate" }],
                     "Default": "HoldForHuman" },
    "HoldForHuman": { "Type": "Task", "Resource": "lambda:notify-editor",
                     "Comment": "2 regen failures = systemic problem; human triage, not more retries",
                     "End": true },
    "Style":       { "Type": "Task",
                     "Resource": "aws-sdk:bedrockagentcore:invokeAgentRuntime",
                     "Parameters": { "AgentRuntimeArn": "arn:...:agent-styler" },
                     "ResultPath": "$.styled", "Next": "Lint" },
    "Lint":        { "Type": "Task", "Resource": "lambda:style-lint", "Next": "LintOutcome" },
    "LintOutcome": { "Type": "Choice",
                     "Choices": [{ "Variable": "$.lint.pass", "BooleanEquals": false, "Next": "Style" }],
                     "Default": "ConsultantReview" },
    "ConsultantReview": { "Type": "Task",
                     "Resource": "lambda:create-review-task.waitForTaskToken",
                     "HeartbeatSeconds": 1209600,
                     "Next": "ReviewOutcome" },
    "ReviewOutcome": { "Type": "Choice",
                     "Choices": [
                       { "Variable": "$.review.decision", "StringEquals": "approve", "Next": "Publish" },
                       { "Variable": "$.review.decision", "StringEquals": "amend",   "Next": "ApplyAmendments" }],
                     "Default": "HoldForHuman" },
    "ApplyAmendments": { "Type": "Task", "Resource": "lambda:apply-amendments", "Next": "Lint" },
    "Publish":     { "Type": "Task", "Resource": "lambda:publish-to-cms", "End": true }
  }
}
```

Notes:
- The Lint state is a deterministic Lambda, not an LLM: regex scan for U+2013/U+2014 (en/em dashes), the banned-phrase list, UK-spelling check, citation-marker/reference-list consistency, and heading structure. LLM stylers occasionally miss their own rules; a regex gate never does. Max 2 style/lint loops, then HoldForHuman.
- waitForTaskToken implements the consultant gate: the review app calls SendTaskSuccess with {decision, comments, edited_text?}. Heartbeat 14 days; timeout pings the editor.
- Batch mode: a parent state machine with a Map state (concurrency 5) fans out page_ids for weekly batch runs, matching the Tuesday drafting day.

---

## 6. DynamoDB Article Tracker (table: kneeschool-article-tracker)

Single source of truth; implements the Production Status Fields from the Operations Handbook.

- PK: page_id (e.g. "2.7.6"). GSI1: status. GSI2: section_id. GSI3: curriculum_tag.
- Attributes:
  - title, section, chapter, tiers_required []
  - priority (high | medium | low)
  - source_status (not_started | partial | complete)
  - draft_status (not_started | ai_draft | edited)
  - qa_status (assistant_checked | evidence_checked | consultant_reviewed)
  - publication_status (ready | scheduled | published | refresh_due)
  - curriculum_tags [] (e.g. "ISCP-T&O-2021:knee:elective", "FRCS-S1", "MRCS-A")
  - execution_arn, artifact_prefix, regen_count, red_flag_count
  - consultant, reviewed_at, published_at, next_review_due (published_at + 12 months, per annual review rule)
- DynamoDB Streams -> Lambda -> weekly KPI report (pages by status, curriculum coverage %, red flags, consultant queue depth) to the reporting dashboard (QuickSight).

---

## 7. Consultant Review Interface

Lightweight Amplify web app (Cognito auth, consultant + editor groups):
- Queue view from GSI1 (qa_status = evidence_checked and styled artifact present).
- Side-by-side: styled draft, Agent 2 verification report (corrections, red flags, escalations), source list with links.
- Actions: Approve, Amend (inline edits captured as consultant_review.json), Reject with reason.
- Action calls API Gateway -> Lambda -> SendTaskSuccess with the stored task token.
- Nothing publishes without this step. This is Tier 4 of the QA Manual and is not bypassable in the state machine (there is no path from Lint to Publish).

---

## 8. Security, Cost and Operations

Security
- Separate IAM execution roles per agent runtime; generator/verifier scoped to KB retrieval + their Lambdas; styler has no network egress.
- Guardrails applied at model invocation for generation; CloudTrail on all Bedrock and S3 access.
- No patient data anywhere in the system; imaging examples must be pre-anonymised before entering sources/ (QA checklist item).

Cost controls
- Standard Step Functions pricing is per transition (trivial here); dominant cost is model tokens. Estimate per article at 2026 Sonnet-class pricing: roughly 60-150k tokens total across three agents ≈ low single-digit USD per page; 1000 pages is a modest four-figure model spend. Set an AWS Budget alarm anyway.
- Map concurrency capped at 5; PubMed Lambda throttled to respect NCBI limits.

Observability
- AgentCore OpenTelemetry traces + X-Ray give per-step visibility; CloudWatch dashboard: executions, failure rate at Verify, average regen_count, lint failures, consultant queue age.
- Alarm: any article with red_flag_count > 0 published (should be impossible; alarm = defect).

Environments
- dev / prod stacks via CDK or Terraform; prompts stored in the Bedrock prompt management / parameter store and versioned — a prompt change is a deployment, recorded against every execution for auditability.

---

## 9. Build Order (2-3 weeks of engineering)

1. S3 bucket + tracker table + seed the architecture (page IDs) into DynamoDB.
2. Knowledge base + ingestion of first topic folder (suggest: meniscus, small and well-bounded).
3. Deploy three AgentCore runtimes with the prompts; test each in isolation on page 1.2.3 Menisci.
4. State machine + lint Lambda; run end-to-end to the human gate.
5. Review app; first consultant-approved page published; then enable weekly batch Map runs.
