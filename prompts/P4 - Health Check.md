# P4: Health check

**When:** monthly, after a large ingest, or when a link in Obsidian goes to a page that does not exist.

**What it produces:** a report in the log and a numbered list of fixes to pick from. Nothing is changed until you pick.

## Paste this

```
Run the wiki-lint skill. Append the report to Wiki/_Meta/_log.md, then give me the numbered list of findings grouped as errors, warnings and suggestions. Do not fix anything yet. For each error, tell me in one line what you would do to fix it.
```

Then pick: "Fix 1, 2 and 5. Leave the rest." The agent fixes those, logs what it did, and commits if git is on.

## What to expect

Errors should be rare and mechanical: a broken link from a renamed page, a page missing from the index. Warnings are where the value is: an orphan nobody will ever find, two pages on one idea, a plan that has gone stale. Suggestions are the wiki telling you what it wants to become: "these four sources are ready for a Knowledge page" is the best finding a lint can make.

---
*LLM Wiki Kit v0.1.0 by Honzik, adapted from Andrej Karpathy's LLM wiki idea. Prompts are tool-agnostic: paste into Claude Desktop Cowork or Claude Code.*
