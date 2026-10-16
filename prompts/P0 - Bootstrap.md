# P0: Bootstrap the vault

**When:** once, right after you copied the contents of `template/` into your new Obsidian vault and opened Claude on that folder.

**Takes:** two minutes. The agent checks the structure, puts your name in, starts git if it can, and runs the first health check.

**Before you paste:** have the vault folder open in VS Code with the Claude Code panel. Know what you want to be called in the vault.

## Paste this

```
You are setting up my knowledge vault from the LLM Wiki Kit. Do these in order and report at the end.

1. Read CLAUDE.md, Wiki/CLAUDE.md and Wiki/_Meta/How This Wiki Works.md so you know the rules.

2. Check the structure. These must exist: Inbox/, Inbox/Clippings/, Archive/, Private/, Profile/About Me.md, Wiki/_Meta/_index.md, Wiki/_Meta/_log.md, Wiki/1. Sources/ (Books, Articles, Videos), Wiki/2. Knowledge/, Wiki/3. Living/, .claude/skills/ with wiki-ingest, wiki-synthesise, wiki-lint, wiki-query and wr-unslop. List anything missing and stop if CLAUDE.md or the skills are missing.

3. Ask me one question: what name should the vault use for me? Then replace every {{OWNER}} in CLAUDE.md and in the skills with that name, and every {{DATE}} in Profile/About Me.md and Wiki/_Meta/How This Wiki Works.md with today's date.

4. If git is available and the folder is not a repository, run git init and make a first commit named "Vault bootstrapped from LLM Wiki Kit v0.2.0". If git is not available, say so and skip.

5. Run the wiki-lint skill. On an empty vault it should report zero errors. If it reports anything, show me.

6. Append a structure entry to Wiki/_Meta/_log.md: what was set up, which version of the kit, and whether git is on.

Report: what exists, what you changed, what the lint said, and the one next step (run P1, the setup interview).
```

## What good looks like

A short report, zero lint errors, your name in `CLAUDE.md`, one log entry. If the agent says it cannot find the skills, the hidden `.claude/` folder was not copied: show hidden files in Finder or Explorer and copy it.

---
*LLM Wiki Kit v0.2.0 by Honzik, adapted from Andrej Karpathy's LLM wiki idea. Paste each prompt into the Claude Code panel.*
