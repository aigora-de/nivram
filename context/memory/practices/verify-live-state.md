---
id: practice-verify-live-state
title: Verify live state before acting
type: practice
status: active
triggers:
  - resuming parked work
  - issue status
  - repository change
source:
  - 'attested: adapted from a maintainer-reviewed practice in a separate private project; original correction retained privately'
created: 2026-11-17
reviewed: 2026-11-17
---

# Verify live state before acting

**When:** picking up an old issue, relying on an earlier summary, or making a
current-state claim about files, implementation, branch or decisions.

Read the current source and issue body; check whether work since the original
request overtook its premise or overlaps with another issue. Distinguish
implemented components from integrated, end-to-end-tested behaviour.

**Origin:** adapted from a private prior development lesson, not evidence of a
failure in Nivram. The maintainer must approve this attestation before merging.

**Limit:** avoid repeated retrieval when the live material was just supplied
and has not plausibly changed.
