# P2: First ingest

**When:** the first time there is something in `Inbox/`. Three to five items is the right first batch: enough to see the pattern, few enough to read everything that comes out.

**Before you paste:** put the files in `Inbox/`. An article clipped with the Web Clipper, a few paragraphs of your own notes on a book, a transcript, a PDF. Name them so the agent can tell what they are.

## Paste this

```
Run the wiki-ingest skill on everything in Inbox/ and Inbox/Clippings/. This is the first ingest, so after the report walk me through one of the pages you wrote: show me the header line, the summary paragraph and the Related section, and tell me what you chose to leave out of the source and why. If anything in the inbox was not wiki material, say so and leave it where it is.
```

## After it runs

Read every page it wrote, with the source open next to it. The checks that matter on a first run:

- Did it get the author, title and date right?

- Does the summary paragraph match what the source actually argues?

- Is anything there that the source did not say?

- Did it link the page from somewhere, so it is not an orphan?

Tell the agent what to fix in plain words. It will fix the page and the log. Once you trust the ingest, the weekly version is just "process my inbox".

---
*LLM Wiki Kit v0.1.0 by Honzik, adapted from Andrej Karpathy's LLM wiki idea. Prompts are tool-agnostic: paste into Claude Desktop Cowork or Claude Code.*
