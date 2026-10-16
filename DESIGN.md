# Design notes

For whoever maintains the kit. The owner of a vault never needs this file.

## What is adapted and what is original

Karpathy described a method in a public post: raw sources in, an LLM compiles a markdown wiki with backlinks and an index, Obsidian as the viewer, Q&A against the wiki with outputs filed back in, periodic health checks, small CLI tools as instruments. That is a method, published openly, and this kit follows it on purpose.

Everything that turns the method into something a person can install is the kit's own work:

- The folder scheme and the three wiki layers (Sources, Knowledge, Living), with the "three articles earns a folder" growth rule.

- The scope model: `Private/` never read, `Profile/` read-only context, `Inbox/` as the only staging area, `Archive/` for processed originals.

- `CLAUDE.md` as a lean schema (scope, structure, skills, routine) with the style guide split into `Wiki/CLAUDE.md` so it loads only when wiki files are touched.

- The sources-first rule: no knowledge article is written straight from an inbox file.

- The four skills and the lint script, including the five link-resolution bugs the script exists to prevent.

- The setup interview, the prompt sequence, the weekly routine, the install guides.

Say "adapted from Karpathy's LLM wiki idea" and leave it there. The claim that matters is that this particular kit works, which is shown by the two vaults it was lifted from.

## Where the kit departs from the gist, on purpose

- **Ingest does not update Knowledge pages.** The gist has one ingest touch 10 to 15 pages. The kit writes the source page, adds Related links, flags concepts, and leaves Knowledge to a separate synthesis pass. Reason: in practice the single-pass version produced Knowledge pages that paraphrased one source, and the three-source threshold is what made them worth reading.

- **A Living layer.** The gist's examples (goals, health, trip planning) are a use, not a layer. The kit gives them one because applied pages have different rules from synthesis pages: they are about one person, they go stale, and they must never carry raw personal data.

- **Private and Profile folders.** Not in the gist. They came from running a vault that holds health and money matters next to book notes.

- **Two tool paths.** The gist assumes an agent with file access. The kit documents Cowork (no skills in the folder, code may run remotely) and Claude Code (everything local) separately, because the install and the privacy guarantees differ.

## The two source vaults

| | Personal vault (June 2026) | Dev vault (June 2026, restructured Aug 2026) |
|---|---|---|
| Layers | Sources, Knowledge, Interests, Living, plus Personal, Profile, Projects | Sources, Knowledge, Project Knowledge, plus Projects, Playbooks, Ideas, Writing, Career, Business |
| Page format | H1, summary, sections, Sources table, Related | Same shape plus a two-column header table, no YAML frontmatter anywhere |
| Source handling | Summaries, filed to Sources, then Archive | Immutable once ingested, binaries checksummed in a Library folder |
| Provenance | Sources table per article | Every claim carries its source at the point of use, three classes, unmarked claim is a defect |
| Lint | Script plus judgement, report only, appends to a log | Method note, knowledge layer only |
| Index and log | `_index.md`, `_log.md`, `changelog.md` | `index.md`, `log.md` |

For a general second brain the personal vault's layers fit better: most of what a person wants to keep is about their own life (Living), not about repos. The dev vault's conventions are the better engineering: immutable sources, a provenance rule, a scope table in `CLAUDE.md`, one log format. The kit takes the personal vault's layers (minus Interests, which folds into Living) and the dev vault's rules (lightened: a header line rather than a header table, and a provenance rule that applies to Knowledge articles rather than every sentence).

## Decisions

- **Minimal core, grows by rule.** Empty example folders from someone else's life invite misfiling. The setup interview seeds the first domains instead.

- **One log file.** The personal vault ended up with `_log.md`, `Lint Log.md` and `changelog.md` doing overlapping jobs. The kit has `_log.md` with typed entries (`ingest`, `synthesis`, `lint`, `query`, `structure`).

- **Frontmatter allowed but optional.** The dev vault bans it because it renders above the H1. Obsidian users who like Properties can use it. The lint script strips it correctly either way.

- **Skills over long prompts.** The prompts are short because the procedure lives in the skill. A prompt says what to do once. A skill says how, every time.

- **Both tool paths, same files.** `CLAUDE.md`, `Wiki/CLAUDE.md` and `.claude/skills/` are read by both Claude Desktop Cowork and Claude Code. The install guides differ, the vault does not.

- **No `Private/` content ever enters a wiki page.** Summaries of health or money matters can live in Living when the owner puts the source in Inbox first. Identifiers and file paths from `Private/` never do.

## Where this goes next

- A business variant: `Clients/`, `Projects/` and a `Procedures/` layer replace `Living/`, the scope table gains a confidentiality column, and the eval harness from the consulting work ships as a skill. The R-Codes demo template is the first instance of that shape.

- A vault MCP server so the agent gets search tools over the wiki once it passes a few hundred pages.

- An `update` script that diffs a running vault's skills against the kit version it started from.
