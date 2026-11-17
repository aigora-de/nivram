# Nivram — Claude Code adapter

@AGENTS.md

Use the shared, tracked `AGENTS.md` as the authoritative project instructions.
The model-neutral memory router is `context/index.md`; read it when deciding which
topic files matter and retrieve only those topics. `context/state.md` is a pointer
to current work, not a substitute for checking live repository state.

Claude's local `~/.claude/projects/.../memory/MEMORY.md` and its topic files are
private, non-authoritative working memory. Do not automatically mirror or commit
their contents into this public repository. Follow `context/README.md` when
proposing promotion, archival or supersession.

Claude-specific conventions belong here, not in `AGENTS.md`.
