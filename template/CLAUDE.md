# Agent Instructions: {{OWNER}}'s Knowledge Vault

<!-- Schema only. Style, page format, filenames: Wiki/CLAUDE.md (loads when editing Wiki/). Procedures: the skills below. Keep this file lean: every line costs tokens on every session. Prune test: would removing this line cause a mistake? Guidance followed: https://code.claude.com/docs/en/memory.md (under 200 lines, facts not procedures, procedures in skills, style in a nested CLAUDE.md). -->

This is an Obsidian vault. {{OWNER}} collects sources and reads the wiki. You write and maintain the wiki. Read `Wiki/_Meta/_index.md` before any wiki task.

## Working rules

- **Think before acting.** State assumptions. When a request has two readings, ask once, propose the one you would pick, and batch your questions. Never work through confusion.

- **Simplicity first.** The minimum change that does the job. No speculative structure, no "improving" adjacent pages.

- **Surgical changes.** Every changed line traces to the request. Match existing style. Mention what looks wrong rather than fixing it unasked.

- **Check your work.** Turn the task into a check before starting (a lint run, a count, a link that resolves) and verify against it at the end.

## Scope

| Folder | Read | Write | Notes |
|---|---|---|---|
| `Private/` | **Never** | **Never** | Raw sensitive files. If {{OWNER}} wants something analysed, they copy it to `Inbox/` first and move the original back afterwards |
| `Profile/` | Yes | Never after setup | Who {{OWNER}} is, what they care about. Read it to personalise. Written once by the setup interview, then owner-edited |
| `Inbox/`, `Inbox/Clippings/` | Yes | Move or delete after ingest | Staging only. Never a permanent home |
| `Archive/` | Only when asked | Move into | Processed originals. The wiki page is the reference, the original is kept |
| `Wiki/1. Sources/` | Yes | Once, at ingest | One page per source. Immutable once written. Corrections go in Knowledge |
| `Wiki/2. Knowledge/`, `Wiki/3. Living/` | Yes | Yes | Synthesis and applied pages. Linted |
| `Wiki/_Meta/` | Yes | Yes | Index, log, how-it-works |

**Never write raw personal data into a wiki page.** Summaries and interpretations are fine. Identifiers, account numbers and file paths from `Private/` are not.

## Wiki layers

| Layer | Path | Rule |
|---|---|---|
| Sources | `Wiki/1. Sources/<type>/` | Faithful to one source. Books, Articles, Videos to start. A new type earns a folder at three pages |
| Knowledge | `Wiki/2. Knowledge/<domain>/` | One concept per page, synthesised across sources, cites them with `[[wikilinks]]`, says where they disagree. A domain earns a folder at three pages |
| Living | `Wiki/3. Living/<area>/` | Knowledge applied to {{OWNER}}'s own situation: plans, logs, protocols, decisions. Backed by `Profile/` |
| Meta | `Wiki/_Meta/` | `_index.md` (read first), `_log.md` (append only), `How This Wiki Works.md` |

**Sources first.** No Knowledge page is written straight from an inbox file. Ingest to Sources, then synthesise.

## Skills

| When | Skill |
|---|---|
| Files in `Inbox/` or "process my inbox" | `wiki-ingest` |
| Three or more sources cover a concept, or "synthesise", "write up what I know about" | `wiki-synthesise` |
| "Check the wiki", monthly, or after a big ingest | `wiki-lint` (report only, fixes on confirmation) |
| A question that spans pages, "what does my wiki say about" | `wiki-query` |

## After any wiki work

1. Update `Wiki/_Meta/_index.md` (one line per page).

2. Append one entry to `Wiki/_Meta/_log.md`: `## YYYY-MM-DD type | short title`, then **What** and **Decisions** lines. If nothing changed, no entry.

3. If git is set up: commit with a one-line message naming what changed.

## Ask before

Deleting anything outside `Inbox/`. Moving a page out of `Wiki/`. Editing `Profile/`. Creating a new top-level folder. Anything that touches `Private/` (the answer is no).

## Style

No em-dashes. No filler. Concrete over abstract. Blank line between list items. Full guide and page format: `Wiki/CLAUDE.md`.

---
*Built from LLM Wiki Kit v0.1.0 by Honzik, adapted from Andrej Karpathy's LLM wiki idea.*
