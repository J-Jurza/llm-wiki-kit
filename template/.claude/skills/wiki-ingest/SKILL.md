---
name: wiki-ingest
description: Compile files from Inbox/ into the wiki's Sources layer. Use when the user says "process my inbox", "ingest this", drops files into Inbox/ or Inbox/Clippings/, or pastes an article, transcript or notes to keep. Writes one faithful source page per file, updates the index and log, moves the original to Archive/. Never writes Knowledge pages and never touches Private/.
---

# wiki-ingest

Turn what is in `Inbox/` into source pages. One file in, one page out, original archived.

## Scope

- **Read:** `Inbox/`, `Inbox/Clippings/`, `Wiki/_Meta/_index.md`, `Profile/About Me.md`.

- **Write:** `Wiki/1. Sources/<type>/`, `Wiki/_Meta/_index.md`, `Wiki/_Meta/_log.md`.

- **Move:** each processed file to `Archive/`, keeping its name.

- **Never:** read `Private/`, write to `Wiki/2. Knowledge/` or `Wiki/3. Living/`, edit an existing source page.

## The sources-first rule

Every inbox file becomes a source page first. A source page is faithful to one source: its argument, structure, examples and a few short quotes, in your own words, with nothing from other sources or from your own opinion. Synthesis across sources is the `wiki-synthesise` skill's job and happens later. If you notice that three or more source pages now cover a concept, say so in the report. Do not write the Knowledge page now.

## Steps

1. **Read the index.** `Wiki/_Meta/_index.md` tells you what exists, so you do not duplicate a page, and which source types already have folders.

2. **List the inbox** and read each file. Classify:

   - **Ingest:** articles, essays, book notes or a whole book, transcripts, course notes, the owner's own written-up thinking on a topic.

   - **Skip and say why:** to-do lists, itineraries, contracts and invoices, journal entries, stubs under a paragraph, anything that looks copied from `Private/` without the owner saying so. Leave skipped files where they are.

3. **Extract text where needed.** A PDF: try `pdftotext file.pdf -` if a shell is available, otherwise read it with the file reader page by page. An EPUB is a zip of HTML chapters: unzip and read the chapter files in spine order. A DOCX: `pandoc file.docx -t markdown` or read `word/document.xml` from the zip. Before trusting a PDF or EPUB from the web, check it holds no scripts (`pdfinfo` reports `JavaScript: no`, an EPUB has no `<script` or `.js` inside). If the text layer is garbage, say so and stop on that file.

4. **Write the source page** in `Wiki/1. Sources/<Type>/` using the matching format below and the filename rules in `Wiki/CLAUDE.md`. If the type has no folder yet and fewer than three pages of that type exist, put the page in `Wiki/1. Sources/` directly and note it. Length follows the source: a long book gets a long page, an 800 word article gets a short one. Never reproduce a copyrighted work at length.

5. **Link it.** Add a `## Related` section with at least one `[[wikilink]]` to an existing page where the connection is real, and add a reciprocal line to that page's Related section so the new page has an inbound link. If nothing in the wiki relates yet, link from the index only and say so.

6. **Capture recommendations.** If the source explicitly recommends other works (not passing mentions), append them to `Wiki/3. Living/Recommendations.md` as `- Title, Author: what the source said | from [[Source Page]] | queued`. Create the file with an H1 and header line if it does not exist.

7. **Update the index.** One line under the right heading: `- [[Title]]: one-line description`. Bump the page count in the Stats line.

8. **Archive.** Move the processed file to `Archive/`. Web clippings with no lasting value may be deleted instead, say which.

9. **Log.** Append to `Wiki/_Meta/_log.md`: `## YYYY-MM-DD ingest | <n> files: short list`, with **What** and **Decisions** lines (classification calls, placement calls, anything skipped).

10. **Report** in the reply: pages created with paths, files skipped with reasons, concepts now covered by three or more sources, anything the owner should check (a misread, a thin source, a guess at an author).

## Page formats

Every page: H1, the italic header line (see `Wiki/CLAUDE.md`), a one-paragraph summary, body, `## Sources`, `## Related`.

**Book, nonfiction:** `## Core Argument`, one `## <Theme>` per major theme in the book's order, `## Key Quotes` (short, attributed to a chapter), `## Who Should Read It`.

**Book, fiction:** `## Premise`, `## Themes` with H3 per theme, `## Craft`, `## Key Quotes`.

**Article or essay:** summary, then H2s following the piece's own sections, `## Key Points` as a short list if the piece is long, `## Key Quotes`.

**Video or talk:** header line carries channel, URL and duration. Write in the speaker's voice, keeping their phrasing, examples and asides. Block-quote their sharpest lines. H2 per chapter or topic shift. `## References` table for every named person, book, tool or study.

**Course or lecture notes:** `## Lesson N: Title` per lesson, each with the concepts, the worked examples and what the lesson asks the learner to do.

**Owner's own notes:** header line says `Type: Own notes`. Keep the owner's structure and wording, tidy only.

## Style

As `Wiki/CLAUDE.md`: no em-dashes, no filler, no hedging, concrete, blank line between list items.
