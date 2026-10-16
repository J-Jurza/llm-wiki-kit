# Install

Obsidian to read, VS Code with Claude Code to run the agent. A code editor, a terminal, and Claude in a side panel. About 45 minutes. Facts checked against Anthropic's documentation on 16 October 2026.

Why this setup: the skills live in the vault and travel with it, the health-check script runs locally, git gives you a history of every change the agent makes, and the permission rules in `.claude/settings.json` block Claude's file tools from `Private/`. The Claude Desktop app's Cowork mode can also open a folder, but it loads skills differently and may run code away from your machine, so this kit does not cover it yet.

## 1. Obsidian

1. Download from https://obsidian.md and install.

2. Open it. Choose **Create new vault**. Name it (your name plus "Vault" is fine). Put it somewhere you will find again, for example `Documents/`. Click Create.

3. Settings (the cog, bottom left) → **Files and links** → turn **Automatically update internal links** on. Set **Default location for new attachments** to "In subfolder under current folder" named `attachments`.

4. Settings → **Core plugins** → make sure **Backlinks**, **Outgoing links** and **Search** are on.

5. Quit Obsidian for the copy step below.

## 2. Copy the template in

1. Open the kit's `template/` folder in Finder (Mac) or Explorer (Windows).

2. Show hidden files: Mac, press Cmd+Shift+. in Finder. Windows, View → Show → Hidden items.

3. Select everything inside `template/` including `.claude` and `.gitignore`, copy, and paste into your new vault folder. The vault's own `.obsidian` folder stays as it is.

4. Open Obsidian again. You should see `Inbox`, `Archive`, `Private`, `Profile`, `Wiki`. The `.claude` folder is hidden from Obsidian, which is correct.

## 3. Git

Mac: open Terminal (Spotlight, type Terminal) and run:

```
git --version
```

If it offers to install developer tools, accept. Windows: install Git for Windows from https://git-scm.com/download/win with the defaults. Git lets Claude Code use its normal shell on Windows and gives you an undo history for the vault.

## 4. VS Code

1. Install from https://code.visualstudio.com (version 1.94 or later).

2. Open it. **File → Open Folder** and choose your vault folder.

3. When asked whether to trust the authors of the folder, say yes: it is your folder.

## 5. Claude Code

1. In VS Code press Cmd+Shift+X (Mac) or Ctrl+Shift+X (Windows), search **Claude Code**, click Install.

2. Open the Claude panel (the icon in the activity bar). Click **Sign in** and finish in the browser. A paid Claude plan (Pro, Max, Team, Enterprise) is required.

3. Optional but recommended, the standalone command-line tool, so `claude` also works in the terminal:

   Mac:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```

   Windows PowerShell:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```

   Then `claude --version`. No Node.js is needed for this installer.

4. In the Claude panel type `/skills` or ask "which skills are available?". The four wiki skills and `wr-unslop` should be listed: Claude Code discovers them in the vault's `.claude/skills/` folder at session start.

## 6. Web Clipper

1. Install **Obsidian Web Clipper** for your browser from https://obsidian.md/clipper.

2. Open its settings. Set the vault to yours, and the note location to `Inbox/Clippings`. Keep the default template.

3. Clip any article as a test. It should appear in `Inbox/Clippings/` in Obsidian within a few seconds.

## 7. What the permissions file does

`.claude/settings.json` in the vault denies Claude's file tools any read of `Private/` and `Archive/`, denies edits to `Profile/`, blocks `git push` and `rm -rf`, and pre-approves `git status`, `diff`, `log`, `add`, `commit` and the lint script. You will still be asked before other commands run. Say no to anything you do not understand.

One limit to know: the deny rule covers Claude's own file tools and the common shell readers (`cat`, `head`, `sed`), not every possible command.

## 8. First run

In the Claude panel paste `prompts/P0 - Bootstrap.md`. It will initialise git and make the first commit. Then `P1 - Setup Interview.md`.

## Sources

- Claude Code setup and installers: https://code.claude.com/docs/en/setup.md

- VS Code extension: https://code.claude.com/docs/en/vs-code.md

- Permissions and why `.claudeignore` is not used: https://code.claude.com/docs/en/permissions.md

- Skills and where they load from: https://code.claude.com/docs/en/skills.md
