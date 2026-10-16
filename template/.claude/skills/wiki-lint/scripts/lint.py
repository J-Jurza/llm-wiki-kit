#!/usr/bin/env python3
"""Mechanical half of the wiki-lint skill. Run from the vault root:

    python3 .claude/skills/wiki-lint/scripts/lint.py

Prints broken links, orphans, index drift and stub candidates. Judgement calls
(duplicates, contradictions, ready-to-synthesise) stay with the agent.

Link resolution rules this script exists to get right, each one a bug that
produced wrong findings in an earlier vault when resolution was improvised:

1. Path-qualified links ([[Folder/Page]]) resolve by path before basename.
2. Double-backtick code spans (``[[x]]``) are quoted examples, not links.
3. Only strip frontmatter that starts at byte 0 of the file.
4. An ambiguous basename resolves relative to the linking file: same folder
   first, then same top-level tree, then anything.
5. A short page whose job is to point at a longer page is not a stub.

Part of LLM Wiki Kit by Honzik. Python 3.8+, standard library only.
"""

import collections
import os
import re
import sys

VAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SKIP_TOP = {"Private", "Archive", ".git", ".obsidian", ".claude", ".trash", "node_modules"}
# Files that quote broken-link examples on purpose.
QUOTE_SOURCES = ("Wiki/_Meta/_log.md", "Wiki/CLAUDE.md", "Wiki/_Meta/How This Wiki Works.md")
# Folders navigated by a hub page instead of _index.md. Empty by default: list
# everything. Add "1. Sources/Books/" here once a Books hub page exists.
ROUTED = ()

FENCE = re.compile(r"```.*?```", re.S)
INLINE = re.compile(r"``[^\n]*?``|`[^`\n]*`")
LINK = re.compile(r"(!?)\[\[([^\]\n]+)\]\]")
POINTER = re.compile(r"(full|detailed|complete) .{0,40}(lives in|see) \[\[", re.I)


def walk_md():
    for dp, dns, fns in os.walk(VAULT):
        rel = os.path.relpath(dp, VAULT)
        top = rel.split(os.sep)[0]
        if top in SKIP_TOP:
            dns[:] = []
            continue
        dns[:] = [d for d in dns if d not in SKIP_TOP]
        for f in fns:
            if f.endswith(".md"):
                p = os.path.join(rel, f) if rel != "." else f
                yield os.path.normpath(p)


def strip_code(t):
    t = FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), t)
    return INLINE.sub("", t)


def strip_frontmatter(t):
    if t.startswith("---\n"):
        m = re.match(r"---\n.*?\n---\n", t, flags=re.S)
        if m:
            return t[m.end():]
    return t


def main():
    files = sorted(walk_md())
    byrel = {p[:-3]: p for p in files}
    by_base = collections.defaultdict(list)
    for p in files:
        by_base[os.path.splitext(os.path.basename(p))[0]].append(p)

    assets = set()
    for dp, dns, fns in os.walk(VAULT):
        top = os.path.relpath(dp, VAULT).split(os.sep)[0]
        if top in SKIP_TOP:
            dns[:] = []
            continue
        dns[:] = [d for d in dns if d not in SKIP_TOP]
        assets.update(f for f in fns if not f.endswith(".md"))

    def resolve(raw, src=None):
        t = raw.split("|")[0].split("#")[0].strip().replace("\\", "/")
        if not t:
            return "SELF"
        tn = os.path.normpath(t)
        if tn in byrel:
            return byrel[tn]
        if "/" in t:
            for q in files:
                if q[:-3].endswith("/" + tn):
                    return q
        base = os.path.basename(t)
        if base in by_base:
            cands = by_base[base]
            if len(cands) > 1 and src:
                here = os.path.dirname(src)
                same_dir = [q for q in cands if os.path.dirname(q) == here]
                if same_dir:
                    return same_dir[0]
                top = src.split(os.sep)[0]
                same_tree = [q for q in cands if q.split(os.sep)[0] == top]
                if same_tree:
                    return same_tree[0]
            return cands[0]
        if base in assets or t in assets:
            return "ASSET"
        return None

    broken = collections.defaultdict(list)
    inbound = collections.defaultdict(set)
    text = {}
    for p in files:
        with open(os.path.join(VAULT, p), encoding="utf-8", errors="replace") as fh:
            t = fh.read()
        text[p] = t
        for m in LINK.finditer(strip_code(t)):
            r = resolve(m.group(2), p)
            if r is None:
                if not p.startswith(QUOTE_SOURCES):
                    broken[p].append(m.group(2))
            elif r not in ("SELF", "ASSET") and r != p:
                inbound[r].add(p)

    wiki = [p for p in files if p.startswith("Wiki/")]
    print("scanned %d markdown files (%d in Wiki/), Private/ and Archive/ excluded\n"
          % (len(files), len(wiki)))

    print("== BROKEN LINKS ==")
    n = 0
    for src in sorted(broken):
        for t in broken[src]:
            print("  %s -> [[%s]]" % (src, t))
            n += 1
    print("  total %d\n" % n)

    print("== ORPHANS (no inbound wikilink) ==")
    orph = [p for p in wiki if not inbound.get(p)
            and not p.startswith(QUOTE_SOURCES)
            and p not in ("Wiki/_Meta/_index.md", "Wiki/CLAUDE.md")]
    for p in orph:
        print("  " + p)
    print("  total %d\n" % len(orph))

    print("== INDEX DRIFT ==")
    idx = strip_code(text.get("Wiki/_Meta/_index.md", ""))
    listed = {m.group(2).split("|")[0].split("#")[0].strip() for m in LINK.finditer(idx)}
    dead = [x for x in sorted(listed) if resolve(x) is None]
    for d in dead:
        print("  index entry resolves nowhere: [[%s]]" % d)
    missing = [p for p in wiki
               if os.path.splitext(os.path.basename(p))[0] not in listed
               and not any(p[5:].startswith(r) for r in ROUTED)
               and p not in ("Wiki/CLAUDE.md", "Wiki/_Meta/_index.md", "Wiki/_Meta/_log.md")]
    for m in missing:
        print("  page absent from _index: " + m)
    print("  dead entries %d, unlisted pages %d\n" % (len(dead), len(missing)))

    print("== STUB CANDIDATES (<200 words, <3 sections) ==")
    stubs = 0
    for p in wiki:
        if p.startswith("Wiki/_Meta/") or p == "Wiki/CLAUDE.md":
            continue
        body = strip_frontmatter(text[p])
        words = len(re.findall(r"\S+", body))
        secs = len(re.findall(r"^#{2,3}\s", body, flags=re.M))
        if words < 200 and secs < 3:
            if POINTER.search(body):
                print("  [by design] %4dw  %s" % (words, p))
            else:
                print("  %4dw %ds  %s" % (words, secs, p))
                stubs += 1
    print("  genuine stub candidates: %d" % stubs)
    return 0


if __name__ == "__main__":
    sys.exit(main())
