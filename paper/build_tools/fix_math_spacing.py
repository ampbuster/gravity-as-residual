#!/usr/bin/env python3
"""
Conservative math-spacing fix for SIDC paper.

Only adds a space BEFORE an opening $ if:
- Previous char is letter or digit (NOT punctuation, NOT space)
- We are NOT inside math mode
- Line is not in a known broken pattern

Skips lines that look broken (heuristic: math range > 30 chars).
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
            # Check for $$ display
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
    """Heuristic: a line is broken if math range > 30 chars (likely contains text)."""
    ranges = find_math_ranges(line)
    for r_start, r_end in ranges:
        content_len = r_end - r_start - 2  # exclude the $...$ delimiters
        if content_len > 30:
            return True
    return False


def fix_math_spacing(line):
    """Add space before opening $ if prev char is letter/digit. Skip broken lines."""
    # Skip code blocks (lines starting with ``` or ~~~~)
    if line.startswith('```') or line.startswith('~~~~'):
        return line
    
    # Skip lines that look broken
    if is_broken_line(line):
        return line
    
    # Skip lines with odd $ count (multi-line math)
    test = re.sub(r'\\$', '', line)
    test = re.sub(r'`[^`\n]*`', '', test)
    if test.count('$') % 2 == 1:
        return line
    
    # Process only non-code-span parts
    parts = re.split(r'(`[^`\n]*`)', line)
    result = []
    for part in parts:
        if part.startswith('`') and part.endswith('`') and len(part) >= 2:
            result.append(part)
            continue
        
        # Walk through with math-mode state
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
                    in_math = False
                    fixed.append('$')
                else:
                    # Opening - add space ONLY if prev is letter/digit
                    if fixed:
                        last_char = fixed[-1][-1] if fixed[-1] else ''
                        if last_char.isalnum() or last_char == '_':
                            fixed.append(' ')
                    in_math = True
                    fixed.append('$')
                i += 1
                continue
            fixed.append(ch)
            i += 1
        result.append(''.join(fixed))
    return ''.join(result)


def process_line(line):
    """Process a single markdown line."""
    return fix_math_spacing(line)


def process_file(path):
    """Process a markdown file, skipping code blocks."""
    with open(path) as f:
        content = f.read()
    
    lines = content.split('\n')
    in_code_block = False
    new_lines = []
    changes = 0
    
    for line in lines:
        # Track fenced code blocks
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
