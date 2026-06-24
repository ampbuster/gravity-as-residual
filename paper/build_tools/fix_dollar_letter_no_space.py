#!/usr/bin/env python3
"""
fix_dollar_letter_no_space.py — Add space after closing $ when followed by letter.

Problem: wrap_math_vars.py and other regex scripts sometimes leave patterns
like `$M_{\rm Pl,2D}$ = 2.95$TeV` or `$M_{\rm Pl,2D} = 12×$v_H` where a
closing `$` of inline math is immediately followed by a letter/Greek with
no space. This breaks GitHub GFM rendering (the `$` is treated as the end
of math mode, but then the next letter gets eaten by other Markdown syntax).

Fix: Insert a space between the closing `$` and the following letter/Greek
when there's no space already.

Examples (BEFORE -> AFTER):
  `$M_{\rm Pl,2D} = 2.95$TeV`           → `$M_{\rm Pl,2D} = 2.95$ TeV`
  `$M_{\rm Pl,2D} = 12×$v_H`            → `$M_{\rm Pl,2D} = 12×$ $v_H`
  `$N_{\rm sub} = 386 (e$vent-specific)`→ `$N_{\rm sub} = 386$ (event-specific)`
  `$M_{\rm Pl,4D}$via α-GM`             → `$M_{\rm Pl,4D}$ via α-GM`
  `$M_{\rm Pl,2D} = 12 ×$v_H`           → `$M_{\rm Pl,2D} = 12 ×$ $v_H`

Safety:
  - Skips inside code blocks (```...```)
  - Skips inside inline code (`...`)
  - Skips inside display math ($$...$$) — those $...$letter are INSIDE math
  - Only fixes inline math closing `$` followed by ASCII letter or Greek letter
  - Does NOT fix if `$` is followed by digit, punctuation, or space

Usage:
  python3 fix_dollar_letter_no_space.py [build_dir]
  python3 fix_dollar_letter_no_space.py              # default: paper/markdown/*.md
  python3 fix_dollar_letter_no_space.py --all        # also fix README, STATE_OF_THE_MODEL, etc.
"""
import re
import os
import sys
import glob


# ASCII letter OR Greek letter (Unicode block U+0370-U+03FF Greek and Coptic,
# U+1F00-U+1FFF Greek Extended)
LETTER_PATTERN = r'[A-Za-zΑ-Ωα-ωἀ-Ἇὀ-὏ᾀ-ᾟ]'


def find_inline_math_closing_positions(text):
    """Find positions of CLOSING `$` of inline math `$...$`.

    Returns list of (pos, next_char) for each closing $ whose next char
    is a letter/Greek with no space.

    Skips:
      - Display math $$...$$ (those are tracked separately)
      - Code blocks (```...```)
      - Inline code (`...`)
    """
    results = []
    state = 'text'  # 'text', 'inline_math', 'display_math', 'inline_code', 'code_block'
    i = 0
    n = len(text)

    while i < n:
        c = text[i]

        # Code block toggle
        if i + 3 <= n and text[i:i+3] == '```':
            if state == 'code_block':
                state = 'text'
            else:
                state = 'code_block'
            i += 3
            continue

        if state == 'code_block':
            i += 1
            continue

        # Inline code toggle
        if c == '`':
            if state == 'inline_code':
                state = 'text'
            else:
                state = 'inline_code'
            i += 1
            continue

        if state == 'inline_code':
            i += 1
            continue

        # Escape character
        if c == '\\' and i + 1 < n:
            i += 2
            continue

        # Math
        if c == '$':
            # Display math $$...$$
            if i + 1 < n and text[i+1] == '$':
                if state == 'text':
                    state = 'display_math'
                    i += 2
                    continue
                if state == 'display_math':
                    state = 'text'
                    i += 2
                    continue
                # Other states: $ is text
                i += 2
                continue

            # Inline math $...$
            if state == 'text':
                state = 'inline_math'
                i += 1
                continue
            if state == 'inline_math':
                # CLOSING $ of inline math
                # Check next char
                if i + 1 < n:
                    nxt = text[i + 1]
                    if re.match(LETTER_PATTERN, nxt):
                        results.append((i, nxt))
                state = 'text'
                i += 1
                continue

            # Other states: $ is text
            i += 1
            continue

        # Inline math cannot span newlines (Markdown spec).
        # If we see a newline while in inline_math, reset to 'text'.
        if c == '\n' and state == 'inline_math':
            state = 'text'

        i += 1

    return results


def fix_file(filepath, dry_run=False):
    """Fix $...$letter patterns in a single file. Return count."""
    with open(filepath) as f:
        content = f.read()

    issues = find_inline_math_closing_positions(content)
    if not issues:
        return 0

    # Apply fixes in reverse order so positions remain valid
    new_content = content
    for pos, nxt in reversed(issues):
        # Insert space between $ and nxt
        new_content = new_content[:pos+1] + ' ' + new_content[pos+1:]

    if not dry_run and new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)

    return len(issues)


def main():
    dry_run = '--dry-run' in sys.argv
    all_md = '--all' in sys.argv

    if all_md:
        files = glob.glob(os.path.join('/workspace/github-repo', 'paper', 'markdown', '*.md'))
        for top in ['README.md', 'STATE_OF_THE_MODEL.md', 'changelog.md',
                    'persistent_memory.md', 'RELEASE_DESCRIPTION_v3.5.9-A2.md',
                    'RELEASE_NOTES_v3.5.9-A2.md', 'ai_disclosure.md',
                    'ZENODO_ARXIV_PAPER.md', 'ZENODO_SETUP.md']:
            tp = os.path.join('/workspace/github-repo', top)
            if os.path.exists(tp):
                files.append(tp)
        sup = os.path.join('/workspace/github-repo', 'supporting')
        if os.path.exists(sup):
            files.extend(glob.glob(os.path.join(sup, '*.md')))
    else:
        files = glob.glob(os.path.join('/workspace/github-repo', 'paper', 'markdown', '*.md'))

    total = 0
    for fp in sorted(set(files)):
        n = fix_file(fp, dry_run=dry_run)
        if n > 0:
            print(f'  {os.path.relpath(fp, "/workspace/github-repo")}: {n} fixes')
            total += n

    if dry_run:
        print(f'\n[DRY RUN] Would fix {total} instances')
    else:
        print(f'\nFixed {total} instances')


if __name__ == '__main__':
    main()
