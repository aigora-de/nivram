# Nivram shared context and memory

This Git-tracked, model-neutral layer serves Claude Code, Codex and future
assistants. It contains **project memory**, not experimental subjects' memories.
`AGENTS.md` is the stable instruction entry point; Claude imports it through
`CLAUDE.md`. `index.md` routes to active records on demand, `state.md`
only points at current work. **Retrieval is advisory/instruction-guided**, not
a guaranteed lookup mechanism; issue #4 tracks reliability experiments.

## Authority by concern

- `AGENTS.md` governs coding-agent conduct and public publication boundaries.
- `docs/03-research-questions-and-hypotheses.md` owns hypotheses;
  `docs/02-experimental-programme.md` owns experimental protocols.
- `personas/` defines reviewer remits, not decisions or empirical evidence.
- This document governs memory lifecycle; records supplement, not overwrite,
  authoritative sources. `docs/project-instructions-full.md` is extended rationale.
- Live repository files and GitHub issues govern current implementation state.

When sources conflict, **report the discrepancy**, don't manufacture consensus.

## Memory format and provenance

One Markdown file per record, beginning with the intentionally constrained
YAML subset demonstrated in `context/memory/`: plain scalar keys and nonempty
indented dash lists. Required: `id`, `title`, `type`, `status`, `triggers`,
`source`, `created`, `reviewed`. Types: `principle`, `constraint`,
`practice`, `feedback`, `decision`, `research`. Statuses: `candidate`,
`active`, `dormant`, `archived`, `superseded`. Dates are ISO `YYYY-MM-DD`.

Sources must identify an inspectable repository path or an explicit
`attested:` provenance statement. Prefer a pinned commit/section for
historical evidence; live policy paths mean **current** policy, not proof of
an earlier conversation. `reviewed` means editorial review of the record,
not independent verification; do not imply the latter. For a new promoted
record, add `approved_by` (maintainer or delegated reviewer) and
`transition_reason` as necessary. Record what a rule adds beyond its source:
trigger, operational application, limits and exceptions; avoid duplicating
entire substantive claims from `docs/`.

## Publication and promotion

Before *any push* into the public repository (including branches and PRs):
1. Propose the record locally with type, sources, purpose and limits.
2. Identify its original provenance, source revision where possible, and
   whether the source is public or privately attested.
3. Review claims, permissions, licences, private paths, names, emails,
   confidential data and secrets. Remove or generalise sensitive information.
4. Obtain explicit maintainer approval for publishing promoted local memories.
5. Publish a reviewable diff and recheck provenance and link validity.

Local Claude/Codex memory is non-authoritative; never mirror it automatically.
A mechanical disclosure scan is a *warning signal*, not a privacy guarantee.
Once pushed, deleting in a later commit does not erase Git history.

## Lifecycle and discoverability

The `status` field states semantic status; location and indices must agree:

| Status | Storage | Discovery |
| --- | --- | --- |
| candidate | `context/memory/` | `context/archive/index.md` only |
| active | `context/memory/` | `context/index.md` |
| dormant | `context/memory/` | `context/archive/index.md` only |
| superseded | `context/memory/` | `context/archive/index.md` and successor/reason |
| archived | `context/archive/` | `context/archive/index.md` only |

For supersession provide `superseded_by` as another record ID, or
`transition_reason` explaining a withdrawal without a successor. Do not
create successor cycles. For any move out of active status, record
`transition_reason` and move its route into the historical index in the
same change. Retired text is **historical, not an instruction**; caches and
Git history may still retrieve it.

Compaction reduces active detail; forgetting removes ordinary routing;
archiving preserves discoverable history; deletion removes stored bytes
subject to Git/backup retention. A large file is not itself a reason for
deletion, and rare high-consequence lessons must not be lost by popularity
metrics. Rotation begins with a proposed diff for maintainer review.

## Checks

Engineering targets (not model limits): `AGENTS.md` 5 KiB,
`CLAUDE.md` 2 KiB, index 8 KiB, state 4 KiB, memory topic 16 KiB
soft, archive 100 KiB soft.

Run `python3 scripts/check-context.py --strict` and
`python3 -m unittest discover -s tests -p 'test_context.py'`.
Validation checks declared metadata, routes and references, lifecycle
consistency and suspicious disclosure patterns. No static checker proves
correctness, safe publication or reliable agent retrieval.

See [design issue #4](https://github.com/aigora-de/nivram/issues/4).
