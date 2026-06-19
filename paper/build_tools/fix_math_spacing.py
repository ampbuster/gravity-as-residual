#!/usr/bin/env python3
"""
Two-pass math spacing fix for SIDC paper.

PASS 1 (aggressive): Add space before any $ that follows a non-space char.
  - Catches all `text$math$` cases, including punctuation.

PASS 2 (cleanup): Remove leading/trailing whitespace inside $...$ math.
  - Fixes cases where Pass 1 added space INSIDE math (e.g., `X $` -> `X$`).

Idempotent: re-running produces no changes.
"""
import os
import re
import sys


def find_math_ranges(line):
    """Find ranges of math expressions (both inline $...$ and display $$...$$)."""
    ranges = []
    i = 0
    while i < len(line):
        if line[i] == '\\' and i + 1 < len(line):
            i += 2
            continue
        if line[i] == '$':
            if i + 1 < len(line) and line[i + 1] == '$':
                j = i + 2
                while j < len(line) - 1:
                    if line[j] == '\\' and j + 1 < len(line):
                        j += 2
                        continue
                    if line[j] == '$' and line[j + 1] == '$':
                        ranges.append((i, j + 2))
                        i = j + 2
                        break
                    j += 1
                else:
                    i += 2
            else:
                j = i + 1
                while j < len(line):
                    if line[j] == '\\' and j + 1 < len(line):
                        j += 2
                        continue
                    if line[j] == '$':
                        ranges.append((i, j + 1))
                        i = j + 1
                        break
                    j += 1
                else:
                    i += 1
        else:
            i += 1
    return ranges


def is_broken_line(line):
    """Heuristic: skip lines with math range > 30 chars (likely contains text)."""
    ranges = find_math_ranges(line)
    for r_start, r_end in ranges:
        content_len = r_end - r_start - 2
        if content_len > 30:
            return True
    return False


def add_space_before_dollar(part):
    """PASS 1: Aggressive - add space before $ if prev char is non-space, non-backslash."""
    fixed = []
    i = 0
    while i < len(part):
        ch = part[i]
        if ch == '\\' and i + 1 < len(part):
            # Escape pair: take both chars and advance index
            fixed.append(part[i:i + 2])
            i += 2
            continue
        if ch == '$':
            if fixed and fixed[-1] and not fixed[-1].endswith(' '):
                last_char = fixed[-1][-1]
                if last_char not in (' ', '\n', '\\'):
                    fixed.append(' ')
            fixed.append('$')
            i += 1
            continue
        fixed.append(ch)
        i += 1
    return ''.join(fixed)


def strip_space_inside_math(part):
    """PASS 2: Remove leading/trailing whitespace inside $...$ math."""
    fixed = []
    i = 0
    in_math = False
    while i < len(part):
        ch = part[i]
        if ch == '\\' and i + 1 < len(part):
            fixed.append(part[i:i + 2])
            i += 2
            continue
        if ch == '$':
            if in_math:
                # Closing $ - strip trailing space before this $
                while fixed and fixed and (fixed[-1] == '' or fixed[-1].endswith(' ')):
                    if fixed[-1] == '':
                        fixed.pop()
                    else:
                        fixed[-1] = fixed[-1].rstrip(' ')
                        if fixed[-1] == '':
                            fixed.pop()
                            break
                in_math = False
                fixed.append('$')
                i += 1
                continue
            else:
                # Opening $ - strip leading space after this $
                fixed.append('$')
                in_math = True
                i += 1
                # Skip leading whitespace inside math
                while i < len(part) and part[i] == ' ':
                    i += 1
                continue
        fixed.append(ch)
        i += 1
    return ''.join(fixed)


def process_line(line):
    """Apply both passes to a single line."""
    if line.startswith('```') or line.startswith('~~~~'):
        return line
    if is_broken_line(line):
        return line
    test = re.sub(r'\\$', '', line)
    test = re.sub(r'`[^`\n]*`', '', test)
    if test.count('$') % 2 == 1:
        return line
    
    parts = re.split(r'(`[^`\n]*`)', line)
    result = []
    for part in parts:
        if part.startswith('`') and part.endswith('`') and len(part) >= 2:
            result.append(part)
            continue
        # Pass 1: add space before $ (aggressive)
        part = add_space_before_dollar(part)
        # Pass 2: strip leading/trailing space inside math
        part = strip_space_inside_math(part)
        result.append(part)
    return ''.join(result)


def process_file(path):
    """Process a markdown file, skipping code blocks."""
    with open(path) as f:
        content = f.read()
    
    lines = content.split('\n')
    in_code_block = False
    new_lines = []
    changes = 0
    
    for line in lines:
        if line.startswith('```') or line.startswith('~~~'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
        
        if in_code_block:
            new_lines.append(line)
            continue
        
        new_line = process_line(line)
        if new_line != line:
            changes += 1
        new_lines.append(new_line)
    
    new_content = '\n'.join(new_lines)
    if new_content != content:
        with open(path, 'w') as f:
            f.write(new_content)
    
    return changes


def main():
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isfile(target):
            n = process_file(target)
            print(f"{target}: {n} lines changed")
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
        total = 0
        for f in sorted(os.listdir(md_dir)):
            if f.endswith('.md'):
                n = process_file(os.path.join(md_dir, f))
                if n > 0:
                    print(f"  {f}: {n}")
                    total += n
        print(f"Total: {total} lines changed")


if __name__ == '__main__':
    main()
