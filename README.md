# LLM Wiki Kit

A starter kit for a personal knowledge base that an LLM writes and you read. You collect the sources (articles, books, videos, your own notes). The agent compiles them into a linked markdown wiki, keeps the index current, checks its own health, and answers questions from it. You read it in Obsidian.

Put together by Honzik, adapted from Andrej Karpathy's LLM wiki idea and from running two vaults this way since June 2026.

## What is in the box

| Path | What it is | Who uses it |
|---|---|---|
| `template/` | A complete, empty vault: folders, `CLAUDE.md`, the wiki rules, four skills, the meta pages | Copied once into a new Obsidian vault |
| `prompts/` | Seven numbered prompts, pasted into Claude in order | The owner, on day one and then weekly |
| `docs/` | Start here, two install guides, the weekly routine, troubleshooting | The owner |
| `DESIGN.md` | Why the kit is shaped this way, what is adapted and what is original | Whoever maintains the kit |
| `VERSION`, `CHANGELOG.md` | Which cut a vault was built from, and what changed since | Both |

## Quick start

1. Read `docs/00 - Start Here.md` (five minutes).

2. Install Obsidian and one Claude path: `docs/01 - Install (Claude Desktop Cowork).md` or `docs/02 - Install (Claude Code in VS Code).md`.

3. Create an empty Obsidian vault and copy everything inside `template/` into it, including the hidden `.claude/` folder.

4. Open Claude on that folder and paste `prompts/P0 - Bootstrap.md`. Then `P1 - Setup Interview.md`.

5. Drop three things into `Inbox/` and paste `P2 - First Ingest.md`.

From there the loop is: clip or drop sources into `Inbox/`, run the ingest, read what came out, ask questions, run the health check now and then. `docs/03 - The Weekly Routine.md` holds the 20 minute version.

## The idea in one paragraph

The owner is the curator of sources and the reader of outputs. The agent is the author. Sources are kept faithfully and never edited after they land. Knowledge articles are written across sources, cite them with wikilinks, and say where sources disagree. One index page lists everything so the agent navigates by reading, with no search infrastructure. Every answer worth keeping is filed back in, so the wiki compounds. Health checks find broken links, orphans and drift before they rot the whole.

## Versions

A vault records the kit version it started from in its `CLAUDE.md` footer. To update a running vault, read `CHANGELOG.md` from that version forward and apply the entries that matter. Skills and `Wiki/CLAUDE.md` can be replaced wholesale. `CLAUDE.md` and the meta pages are owner-edited, so merge by hand.

## Attribution

Kit by Honzik. The method is adapted from Andrej Karpathy's description of LLM-maintained knowledge bases. Obsidian is by Dynalist Inc. Claude is by Anthropic. Keep the footer line in `CLAUDE.md` when you pass a vault on so the next person knows where it came from.

## References

**The idea**

- Andrej Karpathy, *LLM Wiki*, gist, 4 April 2026. Three layers (raw sources, LLM-written wiki, a schema file such as `CLAUDE.md`), three operations (ingest, query, lint), `index.md` read first and an append-only `log.md`. The kit follows this directly. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

- Karpathy's working rules for agents (think before coding, simplicity first, surgical changes, goal-driven execution), as collected by multica-ai. The `## Working rules` block in the template's `CLAUDE.md` is adapted from these. https://github.com/multica-ai/andrej-karpathy-skills

**CLAUDE.md and agent setup**

- Anthropic, *Manage Claude's memory*: `CLAUDE.md` under 200 lines, facts not procedures, nested `CLAUDE.md` files load on demand, `.claude/rules/` with `paths:` frontmatter, `@import`. The split between the template's root `CLAUDE.md` and `Wiki/CLAUDE.md` follows this page. https://code.claude.com/docs/en/memory.md

- Anthropic, *Claude Code: best practices for agentic coding*. https://www.anthropic.com/engineering/claude-code-best-practices

- Anthropic, *Skills*: the `SKILL.md` format, where skills load from on each surface, and the six frontmatter fields that are safe across Claude Code, Cowork and claude.ai (the kit's skills use only `name` and `description`). https://code.claude.com/docs/en/skills.md and the open format at https://agentskills.io

- Anthropic, *Permissions*: `Read(...)` deny rules replace `.claudeignore`, which has no effect. The template's `.claude/settings.json` follows this page. https://code.claude.com/docs/en/permissions.md

- Anthropic, *Set up Claude Code* and *VS Code*: https://code.claude.com/docs/en/setup.md and https://code.claude.com/docs/en/vs-code.md

- Anthropic, *Cowork*: overview, projects and folders, getting started. https://claude.com/docs/cowork/overview, https://claude.com/docs/cowork/guide/projects, https://support.claude.com/en/articles/13345190-getting-started-with-cowork

**Lint and maintenance**

- Karpathy's lint list in the gist: contradictions, stale claims, orphans, concepts without a page, missing cross-references, data gaps a search could fill, suggested questions. The `wiki-lint` skill covers each. The script half (broken links, orphans, index drift, stubs) and its five link-resolution rules come from running the same check on a 600-page vault for four months.

- Obsidian: Web Clipper https://obsidian.md/clipper, graph view for hubs and orphans, Dataview for tables over frontmatter, the attachments folder and the "Download attachments for current file" command for local images. All mentioned in the gist's tips and in `docs/03 - The Weekly Routine.md`.
