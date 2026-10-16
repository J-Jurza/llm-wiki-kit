# Install: Claude Code in VS Code

Path B. A code editor, a terminal, and Claude in a side panel. About 45 minutes. Facts checked against Anthropic's documentation on 16 October 2026.

Why this path: the skills live in the vault and travel with it, the health-check script runs locally, git gives you a history of every change the agent makes, and the permission rules in `.claude/settings.json` physically block Claude from `Private/`.

## 1. Obsidian

Same as Path A, section 1: install from https://obsidian.md, create a vault, set links to auto-update, attachments to a subfolder, and quit before copying.

## 2. Copy the template in

Same as Path A, section 2. Show hidden files, copy everything inside `template/` including `.claude` and `.gitignore` into the vault folder.

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

4. In the Claude panel type `/skills` or ask "which skills are available?". The four wiki skills should be listed: Claude Code discovers them in the vault's `.claude/skills/` folder at session start.

## 6. Web Clipper

Same as Path A, section 6: install from https://obsidian.md/clipper, point it at your vault with note location `Inbox/Clippings`.

## 7. What the permissions file does

`.claude/settings.json` in the vault denies Claude's file tools any read of `Private/` and `Archive/`, denies edits to `Profile/`, blocks `git push` and `rm -rf`, and pre-approves `git status`, `diff`, `log`, `add`, `commit` and the lint script. You will still be asked before other commands run. Say no to anything you do not understand.

Two limits to know: the deny rule covers Claude's own file tools and the common shell readers (`cat`, `head`, `sed`), not every possible command, and it does not apply on Path A.

## 8. First run

In the Claude panel paste `prompts/P0 - Bootstrap.md`. It will initialise git and make the first commit. Then `P1 - Setup Interview.md`.

## Sources

- Claude Code setup and installers: https://code.claude.com/docs/en/setup.md

- VS Code extension: https://code.claude.com/docs/en/vs-code.md

- Permissions and why `.claudeignore` is not used: https://code.claude.com/docs/en/permissions.md

- Skills and where they load from: https://code.claude.com/docs/en/skills.md
