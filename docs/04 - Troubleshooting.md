# Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Agent says it cannot find the skills | The hidden `.claude/` folder did not copy | Show hidden files and copy it. On Path A, upload the skills through Customize instead |
| Agent ignores the rules (writes into Knowledge from the inbox, uses em-dashes) | It has not read `CLAUDE.md`, or on Path A the Instructions field is empty | Path B: ask "read CLAUDE.md and Wiki/CLAUDE.md". Path A: paste `CLAUDE.md` into the project Instructions |
| Clipped pages land in the vault root or in `Clippings/` | Web Clipper note location not set | Clipper settings → note location `Inbox/Clippings`. The ingest skill also reads a root `Clippings/` folder, so nothing is lost |
| A link in Obsidian goes nowhere | A page was renamed or never written | Run `P4 - Health Check`. Broken links are its first finding |
| Health check script "not found" or "cannot run" | Path A runs code away from the folder, or Python is missing | The lint skill does the same checks by reading. On Path B, `python3 --version` in the terminal; install from python.org if missing |
| Agent asks permission for every command | Normal on Path B for anything outside the pre-approved list | Say yes to what you understand. To pre-approve more, edit `.claude/settings.json` allow list |
| Agent wrote something wrong about a source | Misread, or thin source | Tell it in plain words. It fixes the page and logs the correction. Sources it got badly wrong: delete the page, put the original back in the inbox, re-run |
| Two pages on the same idea | Synthesis ran twice under two names | Lint reports it as a duplicate. Pick "merge into X" |
| A page from `Private/` appears in the wiki | You copied it to the inbox and forgot | Delete the wiki page, move the original back, tell the agent what to scrub from the index and log |
| Git says "nothing to commit" after work on Path A | Git is not set up on Path A | Expected. If you want history, open the vault in Path B once a week and commit, or skip git |
| Obsidian shows YAML properties above the title | A page has frontmatter | Allowed by the kit. If you dislike it, tell the agent "no frontmatter in this vault" and add that line to `Wiki/CLAUDE.md` |
| Things got slow or confused mid-session | Long session, context full | Start a new chat. The index and log are the memory, not the conversation |

## Getting help

Describe the symptom and paste the last log entry from `Wiki/_Meta/_log.md`. The kit's author can tell most problems from that.
