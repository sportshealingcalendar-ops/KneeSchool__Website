# KneeSchool Team Pack
Deliverables for the KneeSchool content platform build. 28 August 2026.

## Contents

1. KneeSchool_Junior_Academy_and_Curriculum_Mapping.docx
   Part A: Section 0 Junior Academy (pre-university tier) architecture, governance
   rules and spiral linkage map. Part B: MRCS and FRCS (Tr & Orth) / ISCP 2021
   curriculum mapping tables, implementation actions and risks.
   Status: draft for consultant review. Verify ISCP appendix references before
   publishing any alignment claims.

2. KneeSchool_AI_Agent_Prompts.md
   System prompts for the three-agent pipeline:
   Agent 1 Generator (syllabus-driven, source-grounded drafting)
   Agent 2 Evidence Verifier (adversarial fact and reference checking)
   Agent 3 Style and Coherence (humanisation; no em/en dashes; AI-tell removal)
   Each ends with a JSON handoff contract for orchestration.

3. KneeSchool_AWS_Orchestration_Spec.md
   AWS build spec: Step Functions coordination, Bedrock AgentCore runtimes,
   Knowledge Base, S3 layout, DynamoDB tracker schema, consultant review gate,
   lint gate, security, cost and build order. Pilot page: 1.2.3 Menisci.

4. KneeSchool_Brief_Template_and_Lint_Rules.md
   Annotated reference for the two config artefacts, with field rules and
   operating notes.

5. config/brief_template_example_1.2.3.json
   Machine-readable content brief template, populated for the pilot page.
   JSON-validated.

6. config/lint_rules.json
   Machine-readable lint configuration for the style-gate Lambda (13 rule
   families incl. dash bans, ~90 banned AI phrases, UK spelling, citation
   integrity, governance scans). JSON-validated. Version 1.0.

## Suggested reading order
Strategy/clinical team: 1 then 2. Engineering team: 3 then config/ then 2.

## Hard rules carried through every document
- Consultant review (QA Tier 4) is mandatory and non-bypassable before publication.
- No fabricated citations; a missing reference is acceptable, an invented one is not.
- No commercial content in any tier aimed at minors.
- No em or en dashes in published prose.
