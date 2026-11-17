# Shared context and memory

This is Nivram's **model-neutral, Git-tracked context layer**, usable by Claude Code,
Codex and future assistants. It is not experimental agents' memory and is not a
substitute for the research/evidence documents under `docs/`.

## Routing

- `AGENTS.md` is the stable instruction entry point, and `CLAUDE.md` imports it for Claude Code.
- Codex reads `AGENTS.md` directly; no separate Codex duplicate is needed.
- `index.md` contains short trigger-based routes to topical memories.
- `state.md` has pointers to current work and is not itself the authoritative issue tracker.
- Read relevant files **on demand**; never import the entire context directory into every turn.
- Use the project's source documents for factual and evidential claims.

## Record contract

Memories are Markdown with YAML frontmatter. Fields: `id`, `title`, `type`
(`principle`, `constraint`, `feedback`, `decision`, `research`), `status`
(`candidate`, `active`, `dormant`, `archived`, `superseded`),
`triggers`, `source`, `created`, `reviewed` and optionally `superseded_by`.
The `source` field records provenance, **not** automatic proof. Link to original
project evidence where possible; never fabricate a correction or conversation.

Memories should explain when they apply and where they **do not** apply. Avoid
duplicating hypothesis statuses, experiments or decisions held by authoritative docs.

## Memory lifecycle and forgetting

- **Candidate:** proposed, not yet accepted as reusable guidance.
- **Active:** eligible for normal routing.
- **Dormant:** retained but omitted from ordinary retrieval.
- **Archived:** historical, not current operational instructions.
- **Superseded:** refuted or replaced, with a successor link where available.

Compaction reduces active detail; forgetting removes ordinary recall; archival
preserves history; deletion actually removes stored bytes (which may still survive
Git history/backups). These are different operations. Never delete merely to
meet a context budget. Do not treat low retrieval frequency as low importance:
rare catastrophic failures may deserve durable retention.

Do not automatically publish personal or locally generated memories. Promotion is
a review of accuracy, usefulness, provenance, privacy, IP and suitability for a
**public** repository. Local Claude and Codex memory are caches/working notes,
not the canonical shared knowledge.

## Review/rotation policy

Check periodically or when the index grows: look for stale, duplicate, superseded,
irrelevant and orphaned records; prepare a proposed change before applying it.
Move completed material out of active routing while preserving a discoverable
historical path. Archives explicitly say they are not current instructions.
Prefer a reviewed Git diff over destructive automatic rotation.

## Budget and checking

Initial *engineering targets*, not model-specific limits:
`AGENTS.md` 5 KiB; `CLAUDE.md` 2 KiB; `index.md` 8 KiB;
`state.md` 4 KiB; topic files 16 KiB soft cap; archive files 100 KiB soft cap.
Run `python3 scripts/check-context.py` after changing the shared context.
The checks are provider-neutral and work without either coding agent installed.

See [issue #4](https://github.com/aigora-de/nivram/issues/4) for the broader
model-agnostic architecture and open research questions.
