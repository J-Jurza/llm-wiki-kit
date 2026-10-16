---
name: wiki-lint
description: Health check across the wiki. Use when the user says "check the wiki", "run the health check", "lint", or monthly and after a large ingest. Finds broken links, orphans, index drift, stubs, duplicate concepts, contradictions and concepts ready for a Knowledge page. Report only, appended to the log. Fixes happen only when the user picks them.
---

# wiki-lint

Find what is rotting before it spreads. Report, then fix only what the owner picks.

## Scope

- **Read:** everything under `Wiki/`. Never `Private/`.

- **Write:** one report appended to `Wiki/_Meta/_log.md`. Nothing else until the owner confirms a fix.

## Step 1: the mechanical passes

If a shell is available, run from the vault root:

```
python3 .claude/skills/wiki-lint/scripts/lint.py
```

It prints broken links, orphans, index drift and stub candidates. Read its output and move to step 2.

If no shell is available, or the script is missing, do the same four passes by reading:

1. **Broken links.** Collect every `[[link]]` in `Wiki/` (ignore links inside code spans and code fences). A link resolves if a file with that basename exists anywhere under `Wiki/`, or the path-qualified file exists. List each miss with the file it sits in and the likely intended target.

2. **Orphans.** A page under `Wiki/` that no other page links to (links from `_index.md` count, links from the page to itself do not). The index links to every page, so an orphan here means a page missing from the index and from every Related section.

3. **Index drift.** Pages that exist but are not in `_index.md`, and index lines whose target does not exist.

4. **Stub candidates.** Pages under 200 words with fewer than three sections, or holding `TODO` or "to be expanded".

Do not shortcut link resolution: path-qualified links resolve by path before basename, double-backtick code spans are quotes not links, and only strip frontmatter that starts at the first byte of the file.

## Step 2: the judgement passes

These need reading, not counting. Use the index to choose which pages to open.

- **Duplicate concepts.** Two Knowledge pages that cover one idea under two names. Propose the merge direction.

- **Contradictions.** Two pages that state conflicting facts or advice on the same thing. Quote both, name both files.

- **Unlinked mentions.** A page that discusses a concept with its own Knowledge page in plain text instead of a `[[wikilink]]`.

- **Ready to synthesise.** A concept that three or more source pages touch and that has no Knowledge page. The highest-value finding: list the concept and the sources.

- **Cross-domain connections.** Two pages in different domains that share a principle worth a sentence in each other's Related section.

- **Stale claims.** A Knowledge page that states something a newer source page contradicts or supersedes. Name both and the date of the newer source.

- **Data gaps.** A claim marked as beyond the vault's sources, or a question a page leaves open, that a web search or one more source would settle. List what to look for.

- **Living pages going stale.** A plan or protocol whose Updated date is over three months old and whose topic has new sources since.

- **Questions worth asking.** Two or three questions the wiki could now answer well, and one it cannot yet answer that a named kind of source would unlock.

- **Growth rule.** Three or more pages of one type or domain sitting at a layer's top level, which should now get a folder.

## Step 3: the report

Append to `Wiki/_Meta/_log.md` as `## YYYY-MM-DD lint | <errors> errors, <warnings> warnings`:

```
### Errors (break navigation)
- `path` : issue : suggested fix

### Warnings (should be fixed)
- `path` : issue : suggested fix

### Suggestions (would improve the wiki)
- concept or pair : why : suggested action

### Summary
Pages scanned N. Errors N. Warnings N. Ready to synthesise: list. Clean pages N.
```

Errors: broken links, index drift, duplicate concepts. Warnings: orphans, stubs, contradictions, stale claims, unlinked mentions, stale Living pages. Suggestions: ready to synthesise, data gaps, questions worth asking, cross-domain connections, growth rule.

Update the `Last lint:` date in `_index.md` Stats.

## Step 4: fixes

Present the summary and the numbered list. Ask which to fix. Fix only those, one commit if git is set up, and append a short `## YYYY-MM-DD lint | fixes applied` entry naming them.
