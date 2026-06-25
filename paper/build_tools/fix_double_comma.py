#!/usr/bin/env python3
"""
fix_double_comma.py — Fix redundant `\\,` (thin space) commands in math that cause double commas.

Problem: Source has patterns like `,\\,\\text` which after markdown escape
becomes `,\\,\text` in LaTeX, where `\\,` is a thin space. This results
in visible "double commas" like `τ_{2D,, our frame}`.

Examples (BEFORE -> AFTER):
  `\\tau_{2D,\\,\\text{our frame}}`    → `\\tau_{2D, \\text{our frame}}`
  `M_{Pl,3D}\\,\\text{stuff}}`         → `M_{Pl,3D} \\text{stuff}}`

Strategy: Find `\\,\\,\\w` (thin space + thin space + letter command) and
replace with `\\w` (single space + letter command).

Skips:
  - Code blocks
  - Inline code
  - Code in display math where it's a valid LaTeX command
"""
import re
import os
import sys
import glob


# Pattern: `\\,\\,\\w` (markdown source) - which is `\\,` + `\\,` (two thin spaces)
# Look for this anywhere in math context
DOUBLE_COMMA_PATTERN = re.compile(
    r'\\,\\\\,'  # \\, \\, in source
)


def fix_file(filepath, dry_run=False):
    """Fix double comma patterns in a single file. Return count."""
    with open(filepath) as f:
        content = f.read()

    in_math = False
    in_display = False
    in_code_block = False
    in_inline_code = False
    i = 0
    n = len(content)
    changes = []
    
    while i < n:
        c = content[i]
        if i + 3 <= n and content[i:i+3] == '```':
            in_code_block = not in_code_block
            i += 3
            continue
        if in_code_block:
            i += 1
            continue
        if c == '`':
            in_inline_code = not in_inline_code
            i += 1
            continue
        if in_inline_code:
            i += 1
            continue
        if c == '\\' and i + 1 < n:
            i += 2
            continue
        if c == '$':
            if i + 1 < n and content[i+1] == '$':
                in_display = not in_display
                i += 2
                continue
            in_math = not in_math
            i += 1
            continue
        # Find `\\,\\,` (markdown) which is the double-comma pattern
        m = DOUBLE_COMMA_PATTERN.match(content[i:])
        if m and (in_math or in_display):
            # Replace `\\,\\,` with `\,` (just one thin space)
            changes.append((i, i + m.end()))
            i += m.end()
            continue
        i += 1
    
    if not changes:
        return 0
    
    # Apply changes in reverse
    new_content = content
    for start, end in reversed(changes):
        # Replace `\\,\\,` (4 chars: \\, + \\,) with `\\,` (2 chars)
        new_content = new_content[:start] + '\\,\\\\' + new_content[end:]
    
    if new_content != content and not dry_run:
        with open(filepath, 'w') as f:
            f.write(new_content)
    
    return len(changes)


def main():
    dry_run = '--dry-run' in sys.argv
    all_md = '--all' in sys.argv

    if all_md:
        files = glob.glob(os.path.join('/workspace/github-repo', 'paper', 'markdown', '*.md'))
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
