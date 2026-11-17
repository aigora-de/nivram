---
id: practice-verify-live-state
title: Verify live state before acting
type: feedback
status: active
triggers:
  - resuming parked work
  - issue status
  - repository change
source:
  - https://github.com/aigora-de/marvin/blob/main/docs/claude/feedback/feedback-sweep-before-you-start.md
created: 2026-11-17
reviewed: 2026-11-17
---

# Verify live state before acting

**When:** picking up an old issue, relying on an earlier summary, or making a
current-state claim about files, implementation, branch or decisions.

Read the current source and issue body; check whether work since the original
request overtook its premise or overlaps with another issue. Distinguish
implemented components from integrated, end-to-end-tested behaviour.

**Origin:** adapted as a Nivram practice from an explicitly documented Marvin
development lesson, *not* misrepresented as a Nivram failure.

**Limit:** avoid repeated retrieval when the live material was just supplied
and has not plausibly changed.
