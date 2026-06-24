#!/usr/bin/env python3
"""
Safe wrapper for unicode power-of-10 patterns.

Converts standalone Unicode power patterns in prose to LaTeX math form.
Safe because:
- Only converts Unicode 10^N patterns (which are unambiguous)
- Skips if already inside $...$ math mode
- Skips if in code blocks or inline code
- Skips if part of a larger number (preceded by another digit)
- Does NOT touch ASCII 10^N (those are handled by wrap_powers_of_10.py)

Usage:
  python3 wrap_unicode_powers.py [build_dir_or_file]
  python3 wrap_unicode_powers.py                    # default: paper/markdown/*.md
"""
import re
import os
import sys


# Unicode power notation: 10⁻⁴⁵, 10⁺²³, etc.
# Pattern breakdown:
#   10              literal "10"
#   [⁻⁺]            unicode superscript minus or plus
#   [⁰¹²³⁴⁵⁶⁷⁸⁹]+   unicode superscript digits
UNICODE_POWER = r'(?<![$\d.])10[⁻⁺][⁰¹²³⁴⁵⁶⁷⁸⁹]+(?![⁰¹²³⁴⁵⁶⁷⁸⁹])'

# ASCII power notation: 10^{-18}, 10^{+23}, etc.
# DISABLED by default — wrapping these in $...$ creates broken states when
# the surrounding math is already broken (e.g., $\sigma < 9.2 \times 10^{-48}$ {\rm cm}^2$
# becomes $\sigma < 9.2 \times $10^{-48}$ {\rm cm}^2$, which is worse).
# Source-level fixes for ASCII 10^{-N} are preferred.
# ASCII_NEG_POWER = r'(?<![\$\d.])10\^\{?-\d+\}?(?![0-9])'
# ASCII_POS_POWER = r'(?<![\$\d.])10\^\{?\+\d+\}?(?![0-9])'


def find_math_ranges(text):
    """Find character positions inside $...$ or $$...$$.

    Handles inline code (`...`) and code blocks (```...```) — their
    contents are NOT math, even if they contain $ or $$.
    """
    ranges = []
    state = 0  # 0=text, 1=inline math, 2=display math
    in_code_block = False
    in_inline_code = False
    open_pos = 0
    i = 0
    while i < len(text):
        # Code block: ``` ... ```
        if i + 3 <= len(text) and text[i:i+3] == '```':
            in_code_block = not in_code_block
            i += 3
            continue
        if in_code_block:
            i += 1
            continue
        # Inline code: ` ... `
        if text[i] == '`':
            in_inline_code = not in_inline_code
            i += 1
            continue
        if in_inline_code:
            i += 1
            continue
        # Escape: \\X
        c = text[i]
        if c == '\\' and i + 1 < len(text):
            i += 2
            continue
        # Math: $...$ or $$...$$
        if c == '$':
            if i + 1 < len(text) and text[i+1] == '$':
                if state == 0:
                    state = 2
                    open_pos = i
                    i += 2
                    continue
                if state == 2:
                    ranges.append((open_pos + 2, i))
                    state = 0
                    i += 2
                    continue
                # inline state, $$ is text
                i += 2
                continue
            # Single $
            if state == 0:
                state = 1
                open_pos = i
                i += 1
                continue
            if state == 1:
                ranges.append((open_pos + 1, i))
                state = 0
                i += 1
                continue
            # state == 2 (display): single $ is text
            i += 1
            continue
        i += 1
    return ranges


def is_in_math(pos, ranges):
    for s, e in ranges:
        if s <= pos < e:
            return True
    return False


def is_in_code(text, pos):
    """Check if pos is inside ``` code block or ` inline code.

    Uses a stateful scan (proper handling of paired backticks).
    """
    in_code_block = False
    in_inline = False
    inline_open = 0
    i = 0
    while i < pos:
        # Check for ``` code block start/end
        if i + 3 <= len(text) and text[i:i+3] == '```':
            if in_code_block:
                # End of code block
                in_code_block = False
                i += 3
                continue
            else:
                in_code_block = True
                i += 3
                continue
        if in_code_block:
            i += 1
            continue
        # Check for ` inline code
        if text[i] == '`':
            if in_inline:
                # Closing
                in_inline = False
                i += 1
                continue
            else:
                in_inline = True
                inline_open = i
                i += 1
                continue
        if not in_inline:
            i += 1
            continue
        i += 1
    return in_code_block or in_inline


def unicode_to_latex(power_str):
    """Convert unicode power notation to LaTeX math form.
    e.g., '10⁻⁴⁵' -> '10^{-45}'
    """
    # Extract the sign
    sign = ''
    rest = power_str[2:]  # skip "10"
    if rest and rest[0] in '⁻⁺':
        if rest[0] == '⁻':
            sign = '-'
        rest = rest[1:]

    # Convert unicode superscript digits to regular digits
    sup_map = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
               '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'}
    digits = ''.join(sup_map.get(c, c) for c in rest)

    return f'$10^{{{sign}{digits}}}$'


def process_file(filepath):
    """Process one file for unicode 10^N patterns."""
    with open(filepath) as f:
        content = f.read()

    ranges = find_math_ranges(content)
    replacements = []

    for m in re.finditer(UNICODE_POWER, content):
        pos = m.start()
        # Skip if in math mode
        if is_in_math(pos, ranges):
            continue
        # Skip if in code
        if is_in_code(content, pos):
            continue
        # Skip if in URL or filename
        ctx = content[max(0, pos-30):m.end()+30]
        if any(skip in ctx for skip in ['.md', '.py', '.tex', 'http', 'github.com']):
            continue
        replacements.append((pos, m.end(), unicode_to_latex(m.group(0))))

    # ASCII 10^{-N} handler DISABLED (see top of file for rationale).
    # Wrapping ASCII patterns can break already-broken math contexts.
    # Source-level fixes are preferred for ASCII 10^{-N}.
    # for pattern in [ASCII_NEG_POWER, ASCII_POS_POWER]:
    #     for m in re.finditer(pattern, content):
    #         ...

    if not replacements:
        return 0

    # Apply replacements from end to start
    replacements.sort(reverse=True)
    new_content = content
    for pos, end, repl in replacements:
        new_content = new_content[:pos] + repl + new_content[end:]

    with open(filepath, 'w') as f:
        f.write(new_content)
    return len(replacements)


def main():
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = 'paper/markdown'

    total = 0
    if os.path.isfile(target):
        n = process_file(target)
        print(f'{target}: {n} substitutions')
        total = n
    elif os.path.isdir(target):
        for f in sorted(os.listdir(target)):
            if f.endswith('.md'):
                fp = os.path.join(target, f)
                n = process_file(fp)
                if n > 0:
                    print(f'  {f}: {n}')
                    total += n
        print(f'Total: {total} substitutions')
    print(f'Total: {total}')


if __name__ == '__main__':
    main()
