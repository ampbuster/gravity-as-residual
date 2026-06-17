#!/usr/bin/env python3
"""
e_to_math.py - Convert e-notation (1.5e10, 2.4e-15) to math form
====================================================================

RULE 6 from build_pdf.sh (Section 4.3.2):
  e-notation (1.5e10, 2.4e-15) is a CALCULATOR format, not typesetting.
  In body text, ALWAYS convert to math form:
    $1.5 \times 10^{10}$
    $2.4 \times 10^{-15}$

Converts standalone e-notation in body text to proper math form.
Skips code blocks and table cells.

Usage:
  python3 e_to_math.py [build_dir]
"""
import re
import os
import sys


# Match e-notation: 1.5e10, 2.4e-15, 1.5E10, etc.
# Must NOT be inside $...$ math or code blocks
E_PATTERN = r'(?<![$\w.])(\d+(?:\.\d+)?)[eE]([+-]?\d+)(?![\w])'


def is_in_math(text, pos):
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
    """Check if position is in a code block"""
    pat = re.compile(r'^```', re.MULTILINE)
    matches = list(pat.finditer(text, 0, pos))
    return len(matches) % 2 == 1


def is_in_table_cell(text, pos):
    """Heuristic: check if position is in a table cell"""
    line_start = text.rfind('\n', 0, pos) + 1
    line_end = text.find('\n', pos)
    if line_end < 0:
        line_end = len(text)
    line = text[line_start:line_end]
    if line.count('|') >= 2:
        return True
    return False


def process_file(filepath):
    """Convert e-notation in body text to math form."""
    with open(filepath) as f:
        content = f.read()

    candidates = []
    for match in re.finditer(E_PATTERN, content):
        if is_in_math(content, match.start()):
            continue
        if is_in_code(content, match.start()):
            continue
        if is_in_table_cell(content, match.start()):
            continue
        candidates.append((match.start(), match.end(), match.group(1), match.group(2)))

    if not candidates:
        return 0

    changes = len(candidates)
    new_content = content
    for start, end, mantissa, exponent in reversed(candidates):
        sign = ''
        if exponent.startswith('-'):
            sign = '-'
            exp_digits = exponent[1:]
        elif exponent.startswith('+'):
            exp_digits = exponent[1:]
        else:
            exp_digits = exponent
        wrapped = f'${mantissa} \\times 10^{{{sign}{exp_digits}}}$'
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
