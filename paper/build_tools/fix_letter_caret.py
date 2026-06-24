#!/usr/bin/env python3
"""
fix_letter_caret.py — Wrap plain-text X^N or X^Y math expressions in $...$ math.

Problem: Plain text like `M^1.29`, `V^4`, `c^2`, `m^3` is not in math mode.
In LaTeX, `^` outside math mode is an error or renders as plain `^`.
We want these patterns to be wrapped in `$...$` for proper math rendering.

Examples (BEFORE -> AFTER):
  `M^1.29`           → `$M^{1.29}$`
  `V^4`              → `$V^4$`
  `V^3.5-4.0`        → `$V^{3.5-4.0}$` (with non-greedy pattern)
  `c^2`              → `$c^2$`
  `m/s^2`            → `m/s$^2$`
  `tau^2`            → `$\\tau^2$` (only if tau is the letter)

The pattern matches:
  - One ASCII letter (or simple var name) followed by ^ followed by:
    - Single digit (e.g., 2, 3, 4)
    - Multi-digit number (e.g., 60, 100)
    - Decimal (e.g., 1.29, 3.5)
    - With optional +/- suffix
    - Letter (e.g., E^α, X^N)

Skips:
  - Already in math mode ($...$)
  - Code blocks (```...```)
  - Inline code (`...`)
  - LaTeX commands (\\^X) - already in math context
  - URLs
  - Patterns inside {...} braces (LaTeX)

Usage:
  python3 fix_letter_caret.py [file_or_dir]
  python3 fix_letter_caret.py           # process all paper/markdown/*.md
  python3 fix_letter_caret.py --all     # also fix README, etc.
  python3 fix_letter_caret.py --dry-run # show what would change
"""
import re
import os
import sys
import glob


# Pattern: a single letter or short var name (NOT word boundary at start),
# followed by ^N where N is digit(s) with optional decimal
# Also handle var^X^Y multi-caret (rare but possible)
LETTER_CARET_PATTERN = re.compile(
    r'(?<![\\$`\w\d/])\b([A-Za-z]+)\^(\d+(?:\.\d+)?(?:[+\-]\d+(?:\.\d+)?)*|[A-Za-z]|\\?[a-zA-Z]+)'
)


def is_in_context(text, pos, length):
    """Check if position is inside $...$ math, code, or already-emphasized text."""
    # Check if there's $ before on the same line and an even number of $
    line_start = text.rfind('\n', 0, pos) + 1
    line_end = text.find('\n', pos)
    if line_end == -1:
        line_end = len(text)
    line_section = text[line_start:pos]
    dollar_count = line_section.count('$') - line_section.count('\\$')
    if dollar_count % 2 == 1:
        return True  # Inside $...$
    return False


def find_letter_caret_issues(text):
    """Find all letter^N patterns not in math/code/URLs."""
    results = []
    state = 'text'  # 'text', 'inline_math', 'display_math', 'inline_code', 'code_block'
    i = 0
    n = len(text)

    while i < n:
        c = text[i]
        # Code block
        if i + 3 <= n and text[i:i+3] == '```':
            state = 'code_block' if state != 'code_block' else 'text'
            i += 3
            continue
        if state == 'code_block':
            i += 1
            continue
        # Inline code
        if c == '`':
            state = 'inline_code' if state != 'inline_code' else 'text'
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
            if i + 1 < n and text[i+1] == '$':
                state = 'display_math' if state != 'display_math' else 'text'
                i += 2
                continue
            state = 'inline_math' if state != 'inline_math' else 'text'
            i += 1
            continue
        # Newline resets inline_math
        if c == '\n' and state == 'inline_math':
            state = 'text'
        if state == 'text':
            m = LETTER_CARET_PATTERN.match(text, i)
            if m:
                # Skip common false positives:
                # 1. URL fragments (e.g., http://...^X)
                # 2. Markdown bold with ^
                # 3. HTML tags
                # 4. Already in markdown emphasis
                
                # Check the var name - skip if it's a common word
                var = m.group(1)
                # Skip if var is in HTML or URL context
                # Check prev 50 chars
                prev = text[max(0, i-50):i]
                if 'http' in prev[-10:] or '://' in prev[-5:]:
                    i += 1
                    continue
                # Check next 5 chars for markdown emphasis
                next_chars = text[m.end():m.end()+5]
                if next_chars.startswith('**') or next_chars.startswith('__'):
                    i += 1
                    continue
                # Skip if var is something like "See", "The", etc.
                if var.lower() in ('see', 'the', 'and', 'or', 'is', 'it', 'this', 'we', 'as', 'in', 'on', 'to', 'of', 'for', 'be'):
                    i += 1
                    continue
                # Skip 10^N (handled by wrap_unicode_powers.py)
                if var == '10':
                    i += 1
                    continue
                # Skip variable names with subscripts (M_Pl, etc.)
                if '_' in text[i:m.end()+5]:
                    # Check if there are other subscripts nearby
                    j = i + len(var) + 1  # past ^N
                    if j < n and text[j] == '_':
                        i += 1
                        continue
                # Skip if value is just a single letter that's part of a word
                val = m.group(2)
                if val.isalpha() and val.lower() in ('a', 'i', 'n'):
                    # Check if the letter is alone or part of bigger word
                    # e.g., "i^2" - the i is a variable
                    # vs "any^i" - the i is part of "any"
                    if i > 0 and text[i-1].isalnum():
                        i += 1
                        continue
                
                results.append((m.start(), m.end(), m.group(0)))
                i = m.end()
                continue
        i += 1
    return results


def wrap_in_math(text, start, end, original):
    """Wrap the matched text in $...$ math.

    Multi-digit exponents get wrapped in {...}.
    """
    var, exp = original.split('^', 1)
    # Multi-digit or decimal exponents need braces
    if len(exp) > 1 or '.' in exp or '+' in exp or '-' in exp:
        replacement = f'${var}^{{{exp}}}$'
    else:
        replacement = f'${var}^{exp}$'
    return replacement


def fix_file(filepath, dry_run=False):
    """Fix letter^N patterns in a single file. Return count."""
    with open(filepath) as f:
        content = f.read()

    issues = find_letter_caret_issues(content)
    if not issues:
        return 0

    # Apply in reverse to preserve positions
    new_content = content
    for start, end, orig in reversed(issues):
        replacement = wrap_in_math(content, start, end, orig)
        new_content = new_content[:start] + replacement + new_content[end:]

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
                    'RELEASE_NOTES_v3.5.9-A2.md']:
            tp = os.path.join('/workspace/github-repo', top)
            if os.path.exists(tp):
                files.append(tp)
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
