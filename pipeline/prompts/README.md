# Agent prompts

# KneeSchool AI Agent Prompts
Three-agent content pipeline for AWS (Bedrock Agents or equivalent).
Pipeline: Agent 1 (Generation) → Agent 2 (Evidence Verification) → Agent 3 (Style & Coherence) → Consultant Review → Publication.

Each agent outputs a structured handoff block so the next agent (and the article tracker) can consume it automatically.

---

Each prompt is stored here, deployed to Bedrock prompt management or Parameter Store, and versioned. The state machine passes the whole execution state as the payload; each prompt reads only the fields its stage needs.
