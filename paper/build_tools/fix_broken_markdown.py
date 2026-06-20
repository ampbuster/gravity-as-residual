#!/usr/bin/env python3
"""
fix_broken_markdown.py - Fix broken markdown patterns
======================================================

When math is inserted into bold/italic/parentheses markup, the space
between the markup and the math creates visual issues in the rendered
output. This tool finds and fixes these patterns:

  '** $math'      -> '**$math'    (bold + space + math)
  '( $math'       -> '($math'     (open paren + space + math)
  ' $math' at EOL -> '$math'      (rare, trailing space)
  '$math  $math'  -> '$math $math' (multiple spaces between math)

Common offenders:
  - ** $\alpha$ = 1.258   ->  **$\alpha$ = 1.258
  - ( $M_{\rm 2D}$ is ...  ->  ($M_{\rm 2D}$ is ...
  - ratio ( $\tau$_pred ... ->  ratio ($\tau$_pred ...

Usage:
  python3 fix_broken_markdown.py [file_or_dir]
  python3 fix_broken_markdown.py                # Process all paper/markdown/*.md
  python3 fix_broken_markdown.py path/to/file.md # Process single file
"""
import os
import re
import sys


def fix_broken_markdown(content):
    """
    Fix common broken markdown patterns involving math delimiters.

    The issue: when math is inserted into markdown markup (bold, parens),
    a space between the markup and the first $ creates visual issues.

    Patterns fixed:
    1. '** $math' -> '**$math'   (bold + space + math)
    2. '( $math'  -> '($math'    (open paren + space + math)
    3. ' $math' at start of emphasis -> '$math' (rare, just in case)
    """
    changes = 0

    # Pattern 1: ** $ (bold followed by space and math)
    # This is the most common offender
    new_content, n = re.subn(r'\*\* \$', '**$', content)
    changes += n
    content = new_content

    # Pattern 2: ( $ (open paren followed by space and math)
    new_content, n = re.subn(r'\( \$', '($', content)
    changes += n
    content = new_content

    # Pattern 3: [ $ (open bracket, less common)
    new_content, n = re.subn(r'\[ \$', '[$', content)
    changes += n
    content = new_content

    # Pattern 4: - $ or * $ (list item + space + math)
    # Less common, but can happen
    new_content, n = re.subn(r'^([-*])\s+\$', r'\1 $', content, flags=re.MULTILINE)
    changes += n
    content = new_content

    return content, changes


def process_file(filepath):
    """Fix broken markdown patterns in a single file."""
    with open(filepath, 'r') as f:
        content = f.read()

    new_content, changes = fix_broken_markdown(content)

    if changes > 0:
        with open(filepath, 'w') as f:
            f.write(new_content)

    return changes


def main():
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isfile(target):
            n = process_file(target)
            print(f"{target}: {n} substitutions")
            print(f"Total: {n} substitutions")
            return
        elif os.path.isdir(target):
            total = 0
            for f in sorted(os.listdir(target)):
                if f.endswith('.md'):
                    path = os.path.join(target, f)
                    n = process_file(path)
                    if n > 0:
                        print(f"  {f}: {n}")
                        total += n
            print(f"Total: {total} substitutions")
            return

    # Default: process all markdown files in the repo
    targets = []
    if os.path.isdir('paper/markdown'):
        targets.extend([os.path.join('paper/markdown', f) for f in sorted(os.listdir('paper/markdown')) if f.endswith('.md')])
    if os.path.isdir('supporting'):
        targets.extend([os.path.join('supporting', f) for f in sorted(os.listdir('supporting')) if f.endswith('.md')])
    for fname in ['README.md', 'changelog.md', 'persistent_memory.md',
                  'layman_summary.md', 'how-did-we-get-here.md',
                  'arxiv_submission.md', 'STATE_OF_THE_MODEL.md']:
        if os.path.isfile(fname):
            targets.append(fname)

    if not targets:
        print("Error: no markdown files found")
        sys.exit(1)

    total = 0
    for path in targets:
        n = process_file(path)
        if n > 0:
            print(f"  {path}: {n}")
            total += n
    print(f"Total: {total} substitutions")


if __name__ == '__main__':
    main()
