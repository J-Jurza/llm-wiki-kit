# How This Wiki Works

*Type: Method | Created: {{DATE}} | Kit: LLM Wiki Kit v0.2.0*

This vault is a knowledge base that an LLM writes and you read. You collect sources. The agent compiles them into linked pages, keeps the index, checks its own work and answers your questions from what it has compiled. The method is adapted from Andrej Karpathy's description of LLM-maintained knowledge bases, with the folder scheme, rules and skills put together by Honzik.

## The loop

```
Inbox/  (you drop sources)
   ↓  wiki-ingest
Wiki/1. Sources/   one faithful page per source, never edited again
   ↓  wiki-synthesise
Wiki/2. Knowledge/  one page per concept, written across sources
   ↓  applied to you
Wiki/3. Living/    plans, logs, protocols, decisions about your own life
   ↓  wiki-query
Answers, filed back in as pages
   ↺  wiki-lint keeps the whole thing honest
```

Everything feeds back in. A question the wiki answered well becomes a page. A lint finding becomes a fix. The wiki compounds.

## The three layers

**Sources** are the ground truth. One page per book, article, video or course, faithful to that source alone, in your agent's own words with short quotes where the phrasing matters. Once written, a source page is not edited. If it turns out to be wrong, the correction goes in a Knowledge page that cites it.

**Knowledge** is where thinking happens. One page per concept, organised by idea rather than by author. Each page says what the sources say, where they agree, where they disagree and why, and cites every source with a `[[wikilink]]`. A Knowledge page is only written once three or more sources touch the concept. That rule stops the wiki filling with one-source paraphrases.

**Living** is where the wiki meets your life: a training plan, a reading list, a protocol you are following, a decision you made and why. Living pages cite the Knowledge they apply and are backed by `Profile/`, which describes who you are. They never contain raw personal data: summaries and interpretations only.

## The rules that keep it working

- **Sources first.** Nothing is written into Knowledge straight from the inbox.

- **The index is the infrastructure.** `_index.md` lists every page with a one-line description. The agent reads it first, every time. No vector search is needed at this scale: a few hundred pages with a good index is navigable by reading.

- **Every page has an inbound link.** A page nothing links to is invisible to the agent during Q&A.

- **Immutable sources, editable synthesis.** Corrections and reconciliations live in Knowledge.

- **One log.** Every change gets a dated entry in `_log.md`. When something looks odd, the log says when and why it changed.

- **Private stays private.** `Private/` is never read. `Profile/` is read but not edited. If you want something sensitive analysed, copy it to `Inbox/`, let the agent write the interpretation, then move the original back.

## What to put in the inbox

Good: articles you finished and want to keep, notes on a book, a transcript of a talk, course notes, a page of your own thinking on a topic you want to formalise.

Not wiki material: to-do lists, itineraries, contracts, invoices, journal entries, half-sentence stubs. The ingest skill will skip these and tell you.

## Growth rules

- A source type earns its own folder under `1. Sources/` at three pages (Papers, Courses, Podcasts).

- A domain earns its own folder under `2. Knowledge/` at three pages.

- A Living area earns its own folder at three pages.

- Before that, pages sit at the layer's top level. Folders are for navigation, not for intent.

## The weekly routine

Twenty minutes. Open Claude on the vault and say:

1. "Process my inbox." Read what came out. Fix anything misread while the source is fresh.

2. "Is anything ready to synthesise?" If three sources now cover a concept, say yes.

3. "What's one question my wiki could answer this week?" Ask it. File the answer if it is good.

Monthly: "Run the health check." Pick two or three fixes from the report.

## Related

- [[About Me]]: the profile the Living layer is built around

## Further reading

- Andrej Karpathy, *LLM Wiki* (gist, April 2026), the idea this vault adapts: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

- Anthropic, *Manage Claude's memory* (CLAUDE.md, rules, imports): https://code.claude.com/docs/en/memory.md

- Anthropic, *Claude Code: best practices for agentic coding*: https://www.anthropic.com/engineering/claude-code-best-practices

- Anthropic, *Skills*: https://code.claude.com/docs/en/skills.md
