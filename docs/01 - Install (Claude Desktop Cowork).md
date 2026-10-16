# Install: Claude Desktop with Cowork

Path A. No terminal. About 30 minutes. Facts checked against Anthropic's documentation on 16 October 2026; the app changes often, so where a button is named differently, look for the nearest thing and tell the kit's author.

> [!warning] Two things to know about this path
> Cowork does not read skills from the vault's `.claude/skills/` folder or from `~/.claude`. Skills are added through the app's **Customize** area instead, so step 5 uploads the four skills by hand. And Cowork may run code in an environment away from your Mac, so the health-check script might not run: the lint skill knows this and does the same checks by reading when the script is unavailable.

## 1. Obsidian

1. Download from https://obsidian.md and install.

2. Open it. Choose **Create new vault**. Name it (your name plus "Vault" is fine). Put it somewhere you will find again, for example `Documents/`. Click Create.

3. Settings (the cog, bottom left) → **Files and links** → turn **Automatically update internal links** on. Set **Default location for new attachments** to "In subfolder under current folder" named `attachments`.

4. Settings → **Editor** → turn **Properties in document** to "Visible" or "Source" as you prefer. Leave everything else.

5. Settings → **Core plugins** → make sure **Backlinks**, **Outgoing links** and **Search** are on.

6. Quit Obsidian for the copy step below.

## 2. Copy the template in

1. Open the kit's `template/` folder in Finder (Mac) or Explorer (Windows).

2. Show hidden files: Mac, press Cmd+Shift+. in Finder. Windows, View → Show → Hidden items.

3. Select everything inside `template/` including `.claude` and `.gitignore`, copy, and paste into your new vault folder. The vault's own `.obsidian` folder stays as it is.

4. Open Obsidian again. You should see `Inbox`, `Archive`, `Private`, `Profile`, `Wiki`. The `.claude` folder is hidden from Obsidian, which is correct.

## 3. Claude Desktop

1. Download the Claude app from https://claude.com/download and install it. Sign in with your paid account (Pro, Max, Team or Enterprise). Cowork is not on the free plan.

2. In the sidebar choose **Cowork**. If you do not see it, update the app: Cowork needs the latest version, on Windows in particular.

3. Start a new Cowork project and pick **Use an existing folder**. Choose your vault folder. Claude can only read and write inside folders you attach, so attach the vault and nothing else.

## 4. Give it the rules

Cowork's documentation is silent on whether it reads `CLAUDE.md` from the folder, so do both:

1. Keep `CLAUDE.md` in the vault (it is already there from the template).

2. Open `CLAUDE.md` in Obsidian, copy its whole contents, and paste it into the project's **Instructions** field in Cowork.

When you later edit the rules, edit both places.

## 5. Add the four skills

1. In the Claude Desktop sidebar open **Customize**, then the skills section.

2. Add a skill. If it asks for a folder, point it at `template/.claude/skills/wiki-ingest`. If it asks for a zip, right-click that folder and compress it first.

3. Repeat for `wiki-synthesise`, `wiki-lint` and `wiki-query`.

4. Back in your Cowork project, type "which skills do you have for this vault?" It should name all four.

## 6. Web Clipper

1. Install **Obsidian Web Clipper** for your browser from https://obsidian.md/clipper.

2. Open its settings. Set the vault to yours, and the note location to `Inbox/Clippings`. Keep the default template.

3. Clip any article as a test. It should appear in `Inbox/Clippings/` in Obsidian within a few seconds.

## 7. Privacy on this path

The template's `.claude/settings.json` blocks Claude Code's file tools from `Private/`. Cowork has its own file access and those rules do not carry over, so on this path the only guard is the instruction in `CLAUDE.md`. If that is not enough for what you keep there, move `Private/` out of the vault folder entirely, to a sibling folder Cowork is not attached to.

## 8. First run

Open your Cowork project and paste `prompts/P0 - Bootstrap.md`. Git will probably be reported as unavailable on this path, which is fine. Then `P1 - Setup Interview.md`.

## Sources

- Cowork overview: https://claude.com/docs/cowork/overview

- Cowork projects and folders: https://claude.com/docs/cowork/guide/projects

- Getting started with Cowork: https://support.claude.com/en/articles/13345190-getting-started-with-cowork

- Where skills load from: https://code.claude.com/docs/en/skills.md
