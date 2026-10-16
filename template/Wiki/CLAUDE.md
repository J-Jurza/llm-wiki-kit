# Wiki: writing style, page format, filenames

<!-- Loads when editing any file under Wiki/. The root CLAUDE.md holds scope and structure only. -->

## Writing style

Written for a human reading fast on a screen.

- **No em-dashes.** Use a colon, a comma, or two sentences. No `--` substitutes.

- **No filler.** Cut *it is important to note*, *in order to*, *as well as*, *the fact that*. No preamble: start with the information.

- **No false hedging.** Drop *it seems*, *arguably*, *one might say* unless something is genuinely uncertain. Then say what is uncertain.

- **Never narrate the alternative you rejected.** State the fact and stop.

- **Concrete over abstract.** "3 files" beats "a number of files". Numbers, names, dates.

- **Every sentence earns its place.** If removing it loses nothing, remove it.

## Readability

- Blank line between every list item, at every level.

- Paragraphs of two or three sentences. Past four, split or make a list.

- Tables for comparisons of three or more things and for numbers.

- One bold phrase per paragraph at most: the term being defined or the rule.

- Headings are noun phrases. An H2 past about 40 lines gets H3s.

- Callouts with one job each: `> [!warning]` for gaps and contradictions, `> [!tip]` for techniques, `> [!quote]` for quotes over two lines.

## Page format

Every page: H1 title, a header line, a one-paragraph summary, H2/H3 body, then `## Sources` and `## Related` at the end.

**Header line**, in italics directly under the H1:

- Source page: `*Type: Book | Author: Surname, First | Published: YYYY | Ingested: YYYY-MM-DD | Status: immutable*` (adapt the fields to the type: URL and retrieved date for articles, channel and URL for videos).

- Knowledge page: `*Type: Concept | Sources: [[A]], [[B]], [[C]] | Created: YYYY-MM-DD | Updated: YYYY-MM-DD*`

- Living page: `*Type: Plan | Area: Health | Updated: YYYY-MM-DD*` (Plan, Log, Protocol, Decision, Register).

YAML frontmatter is optional. If used, it goes above the H1 and holds only `tags` and `type`. The header line stays either way so the page reads the same in any viewer.

**Source pages** follow the source's own order. Own words for argument and prose, short quotes only where the phrasing is the point. Never reproduce a whole copyrighted work. A source page is faithful to one source and does not bring in other sources or outside opinion.

**Knowledge pages** are organised by concept, not by source or author. State what the sources say, where they agree, where they disagree and why. Cite the source inline with a `[[wikilink]]` at the point of use. A claim from outside the vault's sources is marked: name the work in the sentence and add a `## References` row with a link and a retrieved date, or put the claim under a `> [!warning] Beyond the vault's sources` callout. An unmarked outside claim is a defect.

**Living pages** are about the owner. They cite the Knowledge and Source pages they apply. They never contain raw personal data from `Private/`.

`## Sources` is a table: `| Source | Type |` with one row per `[[wikilink]]` or URL. `## Related` lists `[[Page]]` with a one-line note on the relationship. Every page needs at least one inbound link from another page.

## Filenames

| Kind | Format | Example |
|---|---|---|
| Book | `Surname, First - Title` | `Newport, Cal - Deep Work` |
| Two authors | `A, First & B, First - Title` | `Heath, Chip & Heath, Dan - Made to Stick` |
| Three or more | `Surname et al - Title` | `Doidge et al - The Brain That Changes Itself` |
| Article | `Surname, First - Title`, or `Publisher - Title` when unsigned | `Graham, Paul - How to Do Great Work` |
| Video | `Creator - Title` | `Huberman Lab - Sleep Toolkit` |
| Knowledge page | Title Case concept name, one concept per file | `Deliberate Practice` |
| Living page | Title Case, what it is | `Morning Routine`, `Bloodwork Results` |

Accents folded to ASCII in filenames. Wikilinks resolve by basename, so never path-qualify a link unless two files share a name.

## Index and log

After any wiki work, update `_Meta/_index.md` (one line per page: `- [[Title]]: one-line description`) under the right heading, and append to `_Meta/_log.md`:

```
## YYYY-MM-DD ingest | Three articles on sleep

**What:** one or two sentences.
**Decisions:** non-obvious choices and why. "None" is a valid answer.
```

Entry types: `ingest`, `synthesis`, `lint`, `query`, `structure`. If nothing changed, no entry.
