# Nivram — development and research review perspectives

This directory is the **canonical, model-neutral** definition of reviewer roles
for *developing Nivram*. It is not the runtime population of agents used as
experimental subjects. A persona is a **remit/lens**, not a model, an independent
mind, a source of evidence or an authority. Claude Code and Codex can enact the
same roles using these files without provider-specific forks.

## Small core, specialists on demand

The three standing perspectives are:

- [Systems engineer](systems-engineer.md) — coherent boundaries, mechanisms and consequences.
- [Experimental scientist](experimental-scientist.md) — falsifiable claims and evidential quality.
- [Critical reviewer](critical-reviewer.md) — alternatives, contradictions and decision lineage.

The following perspectives are **convened only when pertinent**, not a permanent
seven-voice panel:

- [Human–agent researcher](human-agent-researcher.md) — reciprocal human/agent adaptation.
- [Complexity researcher](complexity-researcher.md) — nonlinear dynamics, scale and ecology.
- [Implementation engineer](implementation-engineer.md) — real LLM integration and reproducibility.
- [Adversarial reviewer](adversarial-reviewer.md) — concrete witnesses that break plausible claims.

The core is an available set of lenses, **not three compulsory speeches**.
Use one reviewer if that is enough; ask for a panel when the question benefits
from multiple distinct perspectives. Specialists may be added or replaced as
the work evolves; avoid forcing every topic through this roster.

## Convening convention

1. Name the **proposal, research question or artefact** being reviewed and
   whether this is exploratory discovery or implementation review.
2. Select the smallest relevant panel. Explain any unusual specialist choice.
3. Give each role its own remit and access to the relevant evidence; do not
   fabricate contributions to fill seats. Silence is permitted.
4. Each contributor identifies substantive claims, concerns, their basis,
   counterexamples, tests and remaining uncertainty. Label inferences.
5. Keep disagreements explicit rather than aggregating them into false consensus.
6. Close with a *synthesis*, not a vote: strongest arguments, blocking defects,
   proposed discriminating evidence, decisions for the maintainer and open questions.
7. Do not open issues, implement changes or treat panel conclusions as accepted
   decisions without authorisation or an explicit request.

## What a panel run **is** and **is not**

A single coding agent enacting several roles provides **structured critique,
not independent review**. Separate model calls may reduce conversational
contamination but need not remove common biases. Heterogeneous models and
human reviewers are distinct arrangements. State which arrangement was used
when reporting results, and never call simulated disagreement empirical evidence.

These roles are *not* personas for Experimental Programme agents and should not
become hidden experimental treatments. If used during an experiment's design,
record the actual model, prompts and context to make the process reproducible.

Individual invocation: “Review this as the experimental scientist.”
Panel invocation: “Convene a small Nivram panel on this proposal, including
the adversarial reviewer only if there is something testable to break.”

No runtime orchestration, model API, tooling framework, ontology or autonomous
review schedule is implied. Revisit runtime design only when actual use requires it.
