---
name: wiki-synthesise
description: Write or update a Knowledge page by synthesising across three or more source pages. Use when the user says "synthesise", "write up what I know about X", "is anything ready to synthesise", or when wiki-ingest reports a concept covered by three or more sources. Organises by concept not by source, cites every claim with a wikilink, records disagreement, never edits Sources.
---

# wiki-synthesise

Build the Knowledge layer from the Sources layer. One page per concept, written across sources.

## Scope

- **Read:** `Wiki/_Meta/_index.md`, `Wiki/1. Sources/`, existing `Wiki/2. Knowledge/` pages, `Profile/About Me.md`.

- **Write:** `Wiki/2. Knowledge/` (new or updated pages), `Wiki/_Meta/_index.md`, `Wiki/_Meta/_log.md`, a reciprocal Related line on cited pages.

- **Never:** edit a source page. A source that is wrong is corrected here, with the correction attributed.

## When a concept is ready

Three or more source pages touch it. Fewer than three is a paraphrase of one or two sources and belongs in their Related sections, not in a Knowledge page. If the user asks for a concept with fewer sources, say so and offer to write it anyway with the thinness marked in the header line.

## Steps

1. **Read the index** and list the candidate source pages for the concept. Grep `Wiki/1. Sources/` for the concept's terms and its synonyms, then read the candidates in full.

2. **Check for an existing page.** If `Wiki/2. Knowledge/` already has this concept or an overlapping one, update it rather than writing a neighbour. Two pages on one concept is a defect the lint will find.

3. **Organise by idea.** Draft the H2s as the concept's own structure (definition, mechanism, evidence, how to apply, open questions), not as one section per source.

4. **Write with provenance.** Every claim cites its source inline: `[[Newport, Cal - Deep Work]]`, with a chapter or section when the source is long. Where sources agree, say so and cite all of them. Where they disagree, give each position its sentence, cite it, and say why they differ (different evidence, different context, different definition). A claim from outside the vault is marked: the work named in the sentence plus a `## References` row with a link and a retrieved date, or a `> [!warning] Beyond the vault's sources` callout naming exactly which claims. An unmarked outside claim is a defect.

5. **Apply to the owner, lightly.** One short section, `## For {{OWNER}}` or `## How This Applies`, when `Profile/About Me.md` makes the link obvious. Anything that is a plan or a protocol belongs in `Wiki/3. Living/`, so offer that rather than writing it here.

6. **Link both ways.** `## Sources` table lists every cited page. `## Related` lists neighbouring Knowledge pages. Add a reciprocal Related line to each cited source page? No: source pages are immutable. Add the reciprocal line to neighbouring Knowledge and Living pages only.

7. **Place it.** `Wiki/2. Knowledge/` directly, or in a domain folder once that domain has three pages. Creating the third page in a domain is the moment to create the folder and move the other two, updating the index.

8. **Index and log.** Index line under `## 2. Knowledge`. Log entry `## YYYY-MM-DD synthesis | <Concept>` with **What** (sources used, new or updated) and **Decisions** (disagreements left open, claims marked as outside the sources, anything merged).

9. **Report:** the page path, the sources it drew on, the disagreements it records, and any further concept that now looks ready.

## Header line

`*Type: Concept | Sources: [[A]], [[B]], [[C]] | Created: YYYY-MM-DD | Updated: YYYY-MM-DD*`

Types: Concept (what something is), Method (how to do something), Comparison (A against B), Map (an overview page that routes to others).

## Style

As `Wiki/CLAUDE.md`. In particular: state disagreement plainly, never average it away.
