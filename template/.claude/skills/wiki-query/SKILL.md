---
name: wiki-query
description: Answer a question from the wiki with inline wikilink citations, then offer to file the answer back as a page. Use when the user says "what does my wiki say about", "ask the wiki", "what have I read on", "what did I decide about", or asks anything that spans more than one page. Read-only unless the user accepts the offer to file.
---

# wiki-query

The wiki grows every time it is asked a good question. Answer from the pages, cite them, and offer to keep the answer.

## Steps

1. **Read the index.** `Wiki/_Meta/_index.md` in full. Pick the 5 to 15 pages whose one-line descriptions bear on the question. For fuzzy questions also grep `Wiki/` for the key terms. Do not read the whole wiki.

2. **Read the candidates** in full and follow their `[[wikilinks]]` where the trail is live. Knowledge pages for "what is" and "how does", Living pages for "what did I decide" and "where am I up to", Source pages when the owner wants the underlying evidence.

3. **Answer directly.** Lead with the answer. Cite every claim inline with the `[[page]]` it came from. Surface disagreement between pages rather than averaging it. If the wiki cannot answer, say so plainly and name the kind of source that would fill the gap.

4. **Offer to file it**, and only offer. A non-trivial synthesis (a comparison, a connection across domains, a worked explanation that no single page holds) is worth keeping as:

   - a Knowledge page, when the insight is general, or

   - a Living page or an update to one, when it is about the owner's own situation or a decision they made, or

   - a `## Related` line on two existing pages, when it is a connection and nothing more.

   A lookup already held on one page needs no filing.

5. **If filed:** write the page per `Wiki/CLAUDE.md`, give it an inbound link, add the index line, and append `## YYYY-MM-DD query | <question>` to `_log.md` with `Saved as: [[page]]`. If not filed, no log entry.

## Style

No preamble. Cite pages, not domains. Short quotes beat vague paraphrase. Say what the wiki does not know.
