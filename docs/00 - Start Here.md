# Start here

You are about to set up a knowledge base that an AI writes and you read. This page is the map. Read it once, then follow the numbered steps.

## What you are building

An Obsidian vault with three jobs:

1. **Collect.** You drop articles, book notes, transcripts and your own thinking into an `Inbox/` folder. A browser extension clips web pages straight into it.

2. **Compile.** You tell Claude "process my inbox". It writes one faithful page per source, links them, and keeps an index. When three sources cover the same idea, it writes a page about the idea itself, citing all three. When you ask it a question, it answers from those pages and offers to keep the answer.

3. **Keep honest.** Once a month you tell it "run the health check". It finds broken links, forgotten pages, contradictions and ideas that are ready to be written up, and asks you which to fix.

You never have to write a wiki page yourself. You read, you ask, you decide what goes in.

## What you need

- A computer running macOS 13 or later, or Windows 10 (1809) or later.

- **Obsidian**, free, from obsidian.md. It is the reader: a folder of markdown files shown as a linked notebook.

- A paid Claude plan (Pro is enough). Claude is the writer.

- **VS Code** with the **Claude Code** extension, free. A code editor with Claude in a side panel and a terminal. You will not write code. It is the way to run Claude on a folder so the skills travel with the vault, the health-check script runs locally and git keeps a history.

## The steps

| Step | What | Doc or prompt | Time |
|---|---|---|---|
| 1 | Install Obsidian, VS Code, Claude Code and the Web Clipper | `01 - Install.md` | 45 min |
| 2 | Create an empty vault and copy the template in | Same install doc, last section | 5 min |
| 3 | Bootstrap: check, name, first commit | `prompts/P0 - Bootstrap.md` | 2 min |
| 4 | Setup interview: who you are, what the wiki serves | `prompts/P1 - Setup Interview.md` | 15 min |
| 5 | Put three to five things in `Inbox/`, run the first ingest, read what came out | `prompts/P2 - First Ingest.md` | 20 min |
| 6 | After about ten sources: first synthesis | `prompts/P3 - First Synthesis.md` | 10 min |
| 7 | Every week from then on | `prompts/P6 - Weekly Routine.md` and `02 - The Weekly Routine.md` | 20 min a week |

`P4 - Health Check` and `P5 - Ask the Wiki` are for whenever you need them.

## Three rules to hold onto

- **Sources go in the inbox, nowhere else.** Dropping a file straight into `Wiki/` skips the step that makes it findable.

- **Anything you would not want the AI to read goes in `Private/`.** It is told never to open that folder. If you want something from there analysed, copy it to the inbox first and move the original back after.

- **Read what comes out, at least at first.** The agent is good and it is not perfect. Ten minutes of checking on the first three ingests teaches it your corrections and teaches you what to trust.

## When something goes wrong

`03 - Troubleshooting.md`. The three most common: the hidden `.claude/` folder did not copy, the Web Clipper is saving to the wrong folder, and a link in Obsidian goes nowhere (run the health check).
