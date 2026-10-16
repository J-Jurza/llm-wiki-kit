# LLM Wiki Kit

A knowledge base that an AI writes and you read. You drop articles, book notes and transcripts into an inbox. Claude turns each one into a linked wiki page in Obsidian, keeps the index, checks its own work, and answers your questions from what it has written. You never write a wiki page yourself.

Put together by Honzik, adapted from Andrej Karpathy's LLM wiki idea. Version 0.2.0.

## What you need

| Install | What it is for | Cost | Get it |
|---|---|---|---|
| **Obsidian** | The reader. Shows a folder of markdown files as a linked notebook | Free | https://obsidian.md |
| **Obsidian Web Clipper** | Browser extension. One click saves an article into your inbox | Free | https://obsidian.md/clipper |
| **VS Code** | The editor Claude runs inside. You will not write code in it | Free | https://code.visualstudio.com |
| **Claude Code extension** | Claude, with access to your vault folder and nothing else | Needs a paid Claude plan (Pro is enough) | Installed from inside VS Code, step 5 below |
| **Git** | Keeps a history of every change Claude makes, so anything can be undone | Free | Mac: comes with the developer tools, see step 3. Windows: https://git-scm.com/download/win |
| **GitHub Desktop** (optional) | Only if you got this kit from GitHub rather than a zip. Downloads it and pulls updates later | Free | https://desktop.github.com |
| **Python 3** | Runs the health-check script | Free | Mac: already installed. Windows: https://python.org |

Works on macOS 13 or later and Windows 10 (1809) or later.

## Set up in seven steps

About 45 minutes of installing, then 30 minutes of talking to Claude. The full version with every click is `docs/01 - Install.md`.

**1. Get the kit.** Unzip the file you were sent. Or, in GitHub Desktop, File, Clone repository, paste this repo's address.

**2. Install Obsidian and create a vault.** Open Obsidian, choose Create new vault, name it, put it in Documents. Quit Obsidian.

**3. Install Git.** Mac: open Terminal, type `git --version`, accept the offer to install developer tools. Windows: run the Git installer with the defaults.

**4. Copy the template into your vault.** Show hidden files (Mac: Cmd+Shift+. in Finder. Windows: View, Show, Hidden items). Copy everything inside the kit's `template/` folder, including the hidden `.claude` folder, into your vault folder. Open Obsidian: you should see Inbox, Archive, Private, Profile, Wiki.

**5. Install VS Code and Claude Code.** Install VS Code. Open it, File, Open Folder, choose your vault. Press Cmd+Shift+X (Mac) or Ctrl+Shift+X (Windows), search Claude Code, Install. Open the Claude panel from the left bar, Sign in, finish in the browser.

**6. Install the Web Clipper.** Add it to your browser. In its settings, choose your vault and set the note location to `Inbox/Clippings`.

**7. Run the first two prompts.** In the Claude panel, paste the contents of `prompts/P0 - Bootstrap.md`. It checks the setup, asks your name and makes the first commit. Then paste `prompts/P1 - Setup Interview.md` and answer its questions. Fifteen minutes. It writes your profile and names your first topic areas.

You are set up. Put three things in `Inbox/` and paste `prompts/P2 - First Ingest.md`.

## How you use it from then on

| When | Do |
|---|---|
| Any time | Clip an article, drop a file or a note into `Inbox/` |
| Weekly, 20 minutes | Paste `prompts/P6 - Weekly Routine.md`. Claude processes the inbox, says what is ready to synthesise, suggests one question |
| When you have a question | Paste `prompts/P5 - Ask the Wiki.md` with your question. File the good answers |
| Monthly | Paste `prompts/P4 - Health Check.md`. Pick two or three fixes from the report |

Three rules: sources go in the inbox and nowhere else, anything you do not want Claude to read goes in `Private/`, and read what Claude writes for the first few weeks.

## What is in the box

| Path | What it is |
|---|---|
| `template/` | The empty vault: folders, `CLAUDE.md` (the rules Claude follows), a style guide, the index and log pages, five skills |
| `template/.claude/skills/` | `wiki-ingest`, `wiki-synthesise`, `wiki-lint` (with the health-check script), `wiki-query`, and `wr-unslop` for de-AI editing |
| `prompts/` | P0 to P6, pasted in order |
| `docs/` | `00 - Start Here`, `01 - Install`, `02 - The Weekly Routine`, `03 - Troubleshooting` |
| `DESIGN.md`, `CHANGELOG.md`, `VERSION` | Why it is shaped this way, what changed, which version you have |

## How it works, in one paragraph

Three layers. Sources: one faithful page per article, book or video, never edited after it is written. Knowledge: one page per concept, written only once three or more sources touch it, citing them with links and saying where they disagree. Living: plans, logs and decisions about your own life, built on the other two. One index page lists everything, so Claude navigates by reading it, with no search infrastructure. A log records every change. A monthly health check finds broken links, forgotten pages and ideas ready to be written up. `template/Wiki/_Meta/How This Wiki Works.md` is the long version.

## If something goes wrong

`docs/03 - Troubleshooting.md`. The three most common: the hidden `.claude` folder did not copy (Claude says it cannot find the skills), the Web Clipper is saving to the wrong folder, and a link in Obsidian goes nowhere (run the health check).

## Goes well with

- [Learning Skills](https://github.com/J-Jurza/learning-skills): four skills that teach you a topic instead of answering for you. Inside a vault built from this kit, what you learn is saved as wiki pages.

- `wr-unslop`, included: the de-AI editing pass from [theclaymethod/unslop](https://github.com/theclaymethod/unslop) (MIT), for anything Claude drafts that other people will read.

## Versions and updates

Your vault records the kit version in the footer of `CLAUDE.md`. To update, read `CHANGELOG.md` from your version forward. Skills and `Wiki/CLAUDE.md` can be replaced wholesale. The root `CLAUDE.md` and the meta pages are yours, so merge by hand. Keep the footer line when you pass a vault on, so the next person knows where it came from.

## References

**The idea**

- Andrej Karpathy, *LLM Wiki*, gist, 4 April 2026. Three layers (raw sources, LLM-written wiki, a schema file such as `CLAUDE.md`), three operations (ingest, query, lint), `index.md` read first and an append-only `log.md`. The kit follows this directly. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

- Karpathy's working rules for agents (think before coding, simplicity first, surgical changes, goal-driven execution), as collected by multica-ai. The `## Working rules` block in the template's `CLAUDE.md` is adapted from these. https://github.com/multica-ai/andrej-karpathy-skills

**CLAUDE.md and agent setup**

- Anthropic, *Manage Claude's memory*: `CLAUDE.md` under 200 lines, facts not procedures, nested `CLAUDE.md` files load on demand, `.claude/rules/` with `paths:` frontmatter, `@import`. The split between the template's root `CLAUDE.md` and `Wiki/CLAUDE.md` follows this page. https://code.claude.com/docs/en/memory.md

- Anthropic, *Claude Code: best practices for agentic coding*. https://www.anthropic.com/engineering/claude-code-best-practices

- Anthropic, *Skills*: the `SKILL.md` format, where skills load from on each surface, and the six frontmatter fields that are safe across Claude Code, Claude Desktop and claude.ai (the kit's skills use only `name` and `description`). https://code.claude.com/docs/en/skills.md and the open format at https://agentskills.io

- Anthropic, *Permissions*: `Read(...)` deny rules replace `.claudeignore`, which has no effect. The template's `.claude/settings.json` follows this page. https://code.claude.com/docs/en/permissions.md

- Anthropic, *Set up Claude Code* and *VS Code*: https://code.claude.com/docs/en/setup.md and https://code.claude.com/docs/en/vs-code.md

**Lint and maintenance**

- Karpathy's lint list in the gist: contradictions, stale claims, orphans, concepts without a page, missing cross-references, data gaps a search could fill, suggested questions. The `wiki-lint` skill covers each. The script half (broken links, orphans, index drift, stubs) and its five link-resolution rules come from running the same check on a 600-page vault for four months.

- Obsidian: Web Clipper https://obsidian.md/clipper, graph view for hubs and orphans, Dataview for tables over frontmatter, the attachments folder and the "Download attachments for current file" command for local images. All mentioned in the gist's tips and in `docs/02 - The Weekly Routine.md`.
