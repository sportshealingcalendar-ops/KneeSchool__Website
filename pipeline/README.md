# KneeSchool content pipeline

Infrastructure for the three agent content pipeline described in
`KneeSchool_AWS_Orchestration_Spec.md` and `KneeSchool_AI_Agent_Prompts.md`.

Generate, verify, style, lint, consultant review, publish. Step Functions
coordinates. Each agent reasons only inside its own step, because medical
content QA has to be explainable and every stage has to leave a trail.

```
EventBridge or manual start
        |
   LoadBrief ........... rejects a brief that breaks a field or governance rule
        |
   Generate ............ AgentCore agent-generator, knowledge base and PubMed
   PersistDraft
        |
   Verify .............. AgentCore agent-verifier, adversarial reference checking
   PersistVerified
        |--- FAILED? --> regenerate, twice at most, then hold for a person
        |
   Style ............... AgentCore agent-styler, verified text only, no sources
   PersistStyled
        |
   Lint ................ deterministic Lambda, no model
        |--- FAILED? --> restyle, twice at most, then hold for a person
        |
   ConsultantReview .... waitForTaskToken, fourteen day heartbeat
        |--- amend ----> ApplyAmendments, back through Lint
        |--- reject ---> hold for a person
        |
   Publish ............. S3 published/, tracker update, CMS draft
```

## What is here

```
pipeline/
  prompts/            the three agent prompts as deployed artefacts, versioned
  config/
    lint_rules.json   the style gate rule set, version 1.0
    briefs/1.2.3.json the pilot brief for Menisci
  statemachine/       the Step Functions definition
  functions/          seven Lambda handlers
    style_lint/linter.py   the style gate itself
  layers/common/      shared S3, DynamoDB and brief validation code
  infra/template.yaml SAM template: bucket, tracker, layer, functions, workflow
  tests/              47 tests, no AWS account needed
  tools/lint_local.py run the style gate over any markdown file
```

## What runs today, with no AWS account

```bash
make -C pipeline test
make -C pipeline lint DRAFT=path/to/draft.md BRIEF=pipeline/config/briefs/1.2.3.json
```

The style gate is the piece that works fully offline, and it is the piece worth
having first. It implements all thirteen rule families from `lint_rules.json`:
dash bans, the banned phrase list, UK spelling with the reference list excluded,
citation and reference bijection, no citation markers in junior or patient text,
structure against the brief, the commercial content ban and the advice pattern
scan. Warn rules go to the review pack. Fail rules block.

It is useful beyond the pipeline. Point it at hand written copy and it applies
the same standard.

## What deployment needs

Nothing here has been deployed. The template has not been run against an AWS
account, so treat the first deployment as a dev stack, not a production one.

Prerequisites:

1. An AWS account and a region where Bedrock AgentCore is available.
2. Bedrock model access enabled for the Claude model the agents will use.
3. The AWS SAM CLI and credentials for that account.
4. A globally unique bucket name.
5. An editor email address for hold notifications and the budget alarm.

```bash
cd pipeline
make validate                 # sam validate --lint
make deploy ENV=dev           # guided, asks for every parameter
```

The three AgentCore runtime ARNs are template parameters and default to blank.
Deploy the storage and workflow first, create the runtimes with the prompts in
`prompts/`, then redeploy with the ARNs filled in. The workflow is valid before
the runtimes exist; it just cannot reach the agent states.

## Build order

Following section 9 of the orchestration spec:

1. Deploy this stack. Seed the page IDs from the Master Publishing Architecture
   into the tracker table.
2. Create the knowledge base over `s3://<bucket>/sources/` with the ingestion
   role this stack outputs. Start with one topic folder. Meniscus is small and
   well bounded.
3. Create the three AgentCore runtimes from `prompts/`. Test each in isolation
   on page 1.2.3.
4. Redeploy with the runtime ARNs. Run end to end as far as the consultant gate.
5. Build the review app. Publish the first consultant approved page. Then turn
   on weekly batch runs.

## Decisions that are still open

- **Object Lock.** The bucket is created with Object Lock enabled because that
  flag cannot be set on an existing bucket. No default retention rule is set,
  and the publish handler does not yet apply per object retention. Decide the
  retention period before the first real publication.
- **Batch mode.** The spec calls for a parent state machine with a Map state at
  concurrency five for weekly runs. This stack deploys the single page workflow
  only. The Map wrapper is a small addition once the single page path is proven.
- **PubMed and Crossref tools.** The agent tool Lambdas are named in the spec
  but not built here. They need an NCBI API key and a throttle at three
  requests per second.
- **KPI stream.** The tracker has DynamoDB Streams turned on. The consumer that
  writes the weekly KPI report is not built.
- **CMS endpoint.** `publish_to_cms` posts the page as a draft if
  `CMS_ENDPOINT` is set, and skips the call if it is not. The CMS receives a
  draft on purpose. Going live stays a human action.

## Escalation routes

The handoff blocks define fields whose only purpose is to reach a person.
Agent 2 raises `red_flags` and lists `escalate_to_consultant` for anything it
cannot settle from the literature. Agent 3 lists
`sentences_flagged_for_human_review` for anything it would not rewrite without
risking meaning.

Those travel inside the review notification under `needs_your_judgement`,
rather than sitting in an artefact for someone to go and find. The counts are
also written to the tracker, so the consultant queue can be sorted by how much
judgement each page actually needs. `tests/test_escalations.py` covers the
plumbing.

## The rule the graph enforces

`tests/test_statemachine.py` asserts that removing `ConsultantReview` from the
graph makes `Publish` unreachable. The QA manual says the consultant gate cannot
be bypassed. That is only true if the graph makes it true, so it is tested
rather than trusted.
