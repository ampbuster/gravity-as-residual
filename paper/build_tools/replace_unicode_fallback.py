#!/usr/bin/env python3
"""
replace_unicode_fallback.py — Replace Unicode characters that DejaVu Serif can't render.

DejaVu Serif doesn't have these characters:
  - ℓ (U+2113) - script l
  - ⋆ (U+22C6) - star operator
  - 🎯 (U+1F3AF) - target emoji
  - ✅ (U+2705) - check mark
  - ❌ (U+274C) - cross mark
  - ⏳ (U+23F3) - hourglass
  - ≪ (U+226A) - much less than

Strategy:
  - ℓ (U+2113) → $\\ell$ if in math context, or just `l` in text
  - ⋆ (U+22C6) → $\\star$ if in math context, or just `*` in text
  - 🎯, ✅, ❌, ⏳ → remove or replace with text equivalent
  - ≪ (U+226A) → $\\ll$ if in math context, or `<<` in text

Usage:
  python3 replace_unicode_fallback.py [file_or_dir]
  python3 replace_unicode_fallback.py --dry-run
"""
import re
import os
import sys
import glob


# Map of Unicode → LaTeX replacement
# For each char, we have:
#   in_math: replacement when in math mode
#   in_text: replacement when in plain text (with safe text alternative)
UNICODE_REPLACEMENTS = {
    'ℓ': {'in_math': r'\ell', 'in_text': 'l'},  # script l
    '⋆': {'in_math': r'\star', 'in_text': '*'},  # star operator
    '≪': {'in_math': r'\ll', 'in_text': '<<'},  # much less than
    '🎯': {'in_text': '[TARGET]'},  # target emoji
    '✅': {'in_text': '[OK]'},  # check mark
    '❌': {'in_text': '[FAIL]'},  # cross mark
    '⏳': {'in_text': '[WAIT]'},  # hourglass
}


def fix_file(filepath, dry_run=False):
    """Fix Unicode fallback characters in a single file. Return count."""
    with open(filepath) as f:
        content = f.read()

    in_math = False
    in_display = False
    in_code_block = False
    in_inline_code = False
    i = 0
    n = len(content)
    new_content = content
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
        if c == '\n' and in_math:
            in_math = False
        # Check for Unicode chars to replace
        if c in UNICODE_REPLACEMENTS:
            replacement = UNICODE_REPLACEMENTS[c].get('in_math' if in_math or in_display else 'in_text', None)
            if replacement:
                # Calculate position in new_content
                # We need to track position offset
                new_pos = sum(1 for x in new_content[:i] if x == c) - 1  # Hmm, this is getting complex
                # Just use string replace approach
                # Actually let's just track in old content
                changes.append((i, c, replacement, in_math or in_display))
                i += 1
                continue
        i += 1
    
    if not changes:
        return 0
    
    # Apply changes in reverse
    # But we need to map old positions to new positions
    # Easier: rebuild content with replacements applied based on state tracking
    new_content = ''
    in_math = False
    in_display = False
    in_code_block = False
    in_inline_code = False
    i = 0
    n = len(content)
    
    while i < n:
        c = content[i]
        if i + 3 <= n and content[i:i+3] == '```':
            in_code_block = not in_code_block
            new_content += content[i:i+3]
            i += 3
            continue
        if in_code_block:
            new_content += c
            i += 1
            continue
        if c == '`':
            in_inline_code = not in_inline_code
            new_content += c
            i += 1
            continue
        if in_inline_code:
            new_content += c
            i += 1
            continue
        if c == '\\' and i + 1 < n:
            new_content += content[i:i+2]
            i += 2
            continue
        if c == '$':
            if i + 1 < n and content[i+1] == '$':
                in_display = not in_display
                new_content += '$$'
                i += 2
                continue
            in_math = not in_math
            new_content += c
            i += 1
            continue
        if c == '\n' and in_math:
            in_math = False
        # Replace Unicode char
        if c in UNICODE_REPLACEMENTS:
            repl = UNICODE_REPLACEMENTS[c].get('in_math' if in_math or in_display else 'in_text', None)
            if repl:
                new_content += repl
                i += 1
                continue
        new_content += c
        i += 1
    
    if new_content != content and not dry_run:
        with open(filepath, 'w') as f:
            f.write(new_content)
    
    return sum(1 for _, _, _, _ in changes)


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
