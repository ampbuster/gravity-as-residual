#!/usr/bin/env python3
"""
wrap_powers_of_10.py - Convert 10^N to $10^{N}$ in body text
=================================================================

RULE 1 from build_pdf.sh (Section 4.3.2):
  ALL powers of 10 -> LaTeX math form $10^{N}$.

Converts standalone text patterns:
  10^N    -> $10^{N}$
  10^-N   -> $10^{-N}$
  10^N J  -> $10^{N}$ J

Be careful: only wrap STANDALONE 10^N, not already in math mode.
Skip code blocks, tables, and code spans.

Usage:
  python3 wrap_powers_of_10.py [build_dir]
"""
import re
import os
import sys


# Match 10^N or 10^-N or 10^+N where N is a number (possibly multi-digit)
# Must NOT be preceded by $ (already in math) or by other digits (part of larger number)
POWER_PATTERN = r'(?<![$\d.])10\^(-?\+?)(?:\d+(?:\.\d+)?|\([^)]+\)|\{[^}]+\})'


def is_in_math(text, pos):
    """Check if position is inside $...$ or $$...$$"""
    state = 'text'
    i = 0
    while i < pos:
        if text[i] == '\\' and i + 1 < len(text):
            i += 2
            continue
        if text[i] == '$':
            if i + 1 < len(text) and text[i+1] == '$':
                state = 'text' if state == 'display_math' else 'display_math'
                i += 2
                continue
            else:
                if state == 'inline_math':
                    state = 'text'
                elif state == 'display_math':
                    pass
                else:
                    state = 'inline_math'
                i += 1
                continue
        i += 1
    return state in ('inline_math', 'display_math')


def is_in_code(text, pos):
    """Check if position is in a code block or inline code span"""
    # Code blocks
    pat = re.compile(r'^```', re.MULTILINE)
    matches = list(pat.finditer(text, 0, pos))
    if len(matches) % 2 == 1:
        return True

    # Inline code spans
    # Walk back to check for unmatched backtick
    i = pos - 1
    while i >= 0 and text[i] != '\n':
        if text[i] == '`':
            # Count backticks from position
            j = i - 1
            while j >= 0 and text[j] != '`' and text[j] != '\n':
                j -= 1
            # If we hit another backtick (j+1 == i) then odd number means in code
            count = 0
            k = i
            while k >= 0 and text[k] == '`':
                count += 1
                k -= 1
            if count % 2 == 1:
                return True
        i -= 1
    return False


def is_in_table_cell(text, pos):
    """Heuristic: check if position is inside a table row"""
    # Find the start of current line
    line_start = text.rfind('\n', 0, pos) + 1
    line = text[line_start:text.find('\n', pos)]
    if line.count('|') >= 2:
        return True
    return False


def process_file(filepath):
    """Wrap 10^N patterns in $...$ in a file."""
    with open(filepath) as f:
        content = f.read()

    changes = 0
    candidates = []
    for match in re.finditer(POWER_PATTERN, content):
        if is_in_math(content, match.start()):
            continue
        if is_in_code(content, match.start()):
            continue
        # Don't touch table cells (could break column widths)
        if is_in_table_cell(content, match.start()):
            continue
        candidates.append((match.start(), match.end(), match.group(0)))

    if not candidates:
        return 0

    # Apply changes from end to start to preserve positions
    changes = len(candidates)
    new_content = content
    for start, end, matched in reversed(candidates):
        full_match = content[start:end]
        # Extract sign and exponent
        sign_match = re.match(r'10\^(-?\+?)(.*)', full_match)
        if not sign_match:
            continue
        sign = sign_match.group(1)
        exp = sign_match.group(2)
        if exp.startswith('(') and exp.endswith(')'):
            exp_inner = exp[1:-1]
            wrapped = f'$10^{{{sign}{exp_inner}}}$'
        elif exp.startswith('{') and exp.endswith('}'):
            exp_inner = exp[1:-1]
            wrapped = f'$10^{{{sign}{exp_inner}}}$'
        else:
            wrapped = f'$10^{{{sign}{exp}}}$'
        new_content = new_content[:start] + wrapped + new_content[end:]

    with open(filepath, 'w') as f:
        f.write(new_content)
    return changes


def main():
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isfile(target):
            n = process_file(target)
            print(f"{target}: {n} substitutions")
        elif os.path.isdir(target):
            total = 0
            for f in sorted(os.listdir(target)):
                if f.endswith('.md'):
                    n = process_file(os.path.join(target, f))
                    if n > 0:
                        print(f"  {f}: {n}")
                        total += n
            print(f"Total: {total}")
    else:
        md_dir = 'paper/markdown'
        if not os.path.isdir(md_dir):
            print(f"Error: {md_dir} not found")
            sys.exit(1)
        total = 0
        for f in sorted(os.listdir(md_dir)):
            if f.endswith('.md'):
                n = process_file(os.path.join(md_dir, f))
                if n > 0:
                    print(f"  {f}: {n}")
                    total += n
        print(f"Total: {total} substitutions")


if __name__ == '__main__':
    main()
