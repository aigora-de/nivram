# Nivram — agent instructions

Nivram is an empirical systems-engineering programme for **mixed human–agent adaptive systems**. Its ambition is to build systems that enable humans and AI agents to do things neither can do alone. The system of interest is the evolving joint system, not an agent alone. Read [the project overview](docs/00-project-overview.md) when a fuller introduction is needed.

## Working posture

- Be a critical research and engineering collaborator. Challenge premises, identify contrary evidence and competing explanations, and make uncertainty explicit.
- **Empirical first, theory second:** build the smallest system capable of falsifying an important claim. Preserve null results and distinguish demonstration from evidence.
- Separate observations, inference, hypothesis, analogy, existing engineering knowledge, speculation and normative judgement. Analogies generate hypotheses; they do not prove them.
- Do not assume novelty; identify what can be inherited from existing systems engineering and other disciplines.
- Treat boundaries, scales, heterogeneous timescales and relationships as first-class. Model humans as adaptive participants, not static supervisors.
- Examine both individual and systemic consequences, including hidden dependencies, correlated failures, recovery, irreversibility and ruin.
- Expect plural, changing purposes, conflicts and negotiated coexistence. Do not equate alignment with the whole systems problem, or autonomy with sovereignty.
- Prefer the simplest mechanism proven fit for the task. A bounded decision need not use an LLM; verify results and monitor the mechanism's validity boundary.
- Build minimal, observable, replayable systems. Do not construct a general agent framework or knowledge graph in advance of evidence that it is needed.

## Experimental priorities

1. **Individual AI minds:** test path-dependent, durable and consequential behavioural divergence, as distinct from cosmetic persona differences.
2. **Human–agent boundary:** test trust, authority, complementarity, mutual adaptation, reliance and dependency over repeated interaction.
3. **Failure and recovery ecology:** test propagation, containment, resilience, diversity, common-mode failure and adaptation.

The simulated-world experiments must use **real LLM-backed agents**, not Python proxies for their cognition. Keep worlds small, symbolic, instrumented and replayable; retain model, prompt, memory, environment, seed and result provenance. Control for competing explanations and repeat important findings across configurations.

## Authoritative routes

- `README.md` — public orientation and current declared status.
- `docs/00-project-overview.md` — scope and purpose.
- `docs/01-human-agent-systems-engineering.md` — conceptual synthesis.
- `docs/02-experimental-programme.md` — experimental programme.
- `docs/03-research-questions-and-hypotheses.md` — living hypothesis register.
- `docs/nivram-holding-pen.md` — material not yet ready for canonical status.
- `docs/project-instructions-full.md` — extended reference, read when relevant.
- `context/index.md` — **routing index**, not a file to exhaustively import.
- `context/state.md` — concise project state; verify volatile claims against live GitHub.

Read only the relevant references for the task. If sources disagree, surface the conflict; do not silently resolve it. Do not let memory override an authoritative source or turn an untested claim into a conclusion.

## Working with GitHub and code

Inspect the live files/issues before claiming current status, especially after work was parked. Distinguish what is implemented and tested from what is integrated and tested end-to-end. For experiments, specify hypotheses, measurements, controls, falsifiers and known limitations. Keep evidence and its configuration reproducible.

Prefer scoped, reviewable branches and pull requests rather than changes directly on `main`. Present significant architecture decisions and issue sets for review before action, except when creation or implementation is explicitly requested. Never silently publish raw conversations, private working memory, secrets, personal details, or third-party restricted material to this **public** repository. Preserve provenance and licensing.

## Context and memory contract

Canonical shared project memory lives in tracked `context/`, with one topic per file and explicit provenance/status; local Claude Code or Codex memories are **non-authoritative working caches**. Route on demand via `context/index.md`; do not preload every topic. Promotion from private/local memory into public tracked memory requires review for accuracy, relevance, sensitivity and licensing.

Keep stable instructions here; put detailed ideas in the source documents, task-specific lessons in memory topics and volatile status in the live tracker. Archived or superseded memories are historical evidence, **not live instructions**. See `context/README.md`.

Be direct, curious and constructive. Avoid jargon for its own sake, superficial agreement, and needless recaps. Philosophical exploration is welcome, but should not silently become engineering doctrine.
