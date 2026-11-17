---
id: constraint-llm-backed-agents
title: Genuine LLM-backed experimental agents
type: constraint
status: active
triggers:
  - agent implementation
  - experimental substrate
source:
  - docs/02-experimental-programme.md
  - docs/03-research-questions-and-hypotheses.md
created: 2026-11-17
reviewed: 2026-11-17
---

# Genuine LLM-backed agents

**When:** implementing or choosing actors for Nivram's experimental worlds.

The experimental agents must be driven by actual LLM-based inference, not
Python scripts imitating their cognition. Keep deterministic world mechanics,
instrumentation and deliberately labelled control baselines where helpful.

**Limit:** a tabular or scripted baseline is permitted as a comparator, but
must not be presented as the experimental LLM agent itself.
