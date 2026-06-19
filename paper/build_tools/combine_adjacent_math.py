#!/usr/bin/env python3
"""
Combine adjacent math expressions separated only by whitespace.

Patterns handled:
- $X$  $Y$ → $X Y$
- ~$X$  $Y$ → $\sim X Y$
- $X$  $Y$ J → $X Y$ J
- ~$X$  $Y$ J → $\sim X Y$ J

Idempotent: re-running produces no changes.
"""
import os
import re
import sys


def find_math_ranges(line):
    """Return list of (start, end) for each $...$ math expression in line.
    Skips escaped \\$. Handles both inline ($X$) and display ($$X$$)."""
    ranges = []
    i = 0
    while i < len(line):
        if line[i] == '\\' and i + 1 < len(line):
            i += 2
            continue
        if line[i] == '$':
            # Check for $$ (display math)
            if i + 1 < len(line) and line[i + 1] == '$':
                # Find closing $$
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
                # Inline math
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


def combine_adjacent(line):
    """Find adjacent $X$  $Y$ patterns and combine them."""
    ranges = find_math_ranges(line)
    if len(ranges) < 2:
        return line
    
    # Build new line by walking through ranges
    result = []
    pos = 0
    
    i = 0
    while i < len(ranges):
        r1_start, r1_end = ranges[i]
        prefix = line[pos:r1_start]
        
        # Check if next range is adjacent (only whitespace between)
        if i + 1 < len(ranges):
            r2_start, r2_end = ranges[i + 1]
            between = line[r1_end:r2_start]
            
            if between.strip() == '':
                # Adjacent! Combine
                r1_content = line[r1_start + 1:r1_end - 1]
                r2_content = line[r2_start + 1:r2_end - 1]
                
                # Check for ~ in prefix
                tilde_match = re.search(r'~\s*$', prefix)
                
                if tilde_match:
                    # Strip ~ entirely from prefix; add \sim in math
                    stripped = prefix[:tilde_match.start()].rstrip()
                    result.append(stripped)
                    combined = '\\sim ' + r1_content + ' ' + r2_content
                else:
                    result.append(prefix)
                    combined = r1_content + ' ' + r2_content
                
                result.append('$' + combined + '$')
                pos = r2_end
                i += 2
                continue
        
        # Not adjacent, append prefix + r1 as-is
        result.append(prefix)
        result.append(line[r1_start:r1_end])
        pos = r1_end
        i += 1
    
    # Append remaining text
    result.append(line[pos:])
    
    return ''.join(result)


def process_line(line):
    """Process a line, skipping inline code spans."""
    parts = re.split(r'(`[^`\n]*`)', line)
    result = []
    for part in parts:
        if part.startswith('`') and part.endswith('`') and len(part) >= 2:
            result.append(part)
        else:
            result.append(combine_adjacent(part))
    return ''.join(result)


def process_file(path):
    """Process a markdown file, skipping fenced code blocks."""
    with open(path) as f:
        content = f.read()
    
    lines = content.split('\n')
    in_code_block = False
    new_lines = []
    total_subs = 0
    
    for line in lines:
        if line.startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
        
        if in_code_block:
            new_lines.append(line)
            continue
        
        new_line = process_line(line)
        if new_line != line:
            total_subs += 1
        new_lines.append(new_line)
    
    new_content = '\n'.join(new_lines)
    if new_content != content:
        with open(path, 'w') as f:
            f.write(new_content)
    
    return total_subs


def process_all(targets):
    """Process all targets until convergence."""
    total_runs = 0
    max_runs = 5
    while total_runs < max_runs:
        total_subs = 0
        for path in targets:
            if os.path.isfile(path):
                n = process_file(path)
                if n > 0:
                    print(f"  {path}: {n}")
                    total_subs += n
            elif os.path.isdir(path):
                for f in sorted(os.listdir(path)):
                    if f.endswith('.md'):
                        n = process_file(os.path.join(path, f))
                        if n > 0:
                            print(f"  {os.path.join(path, f)}: {n}")
                            total_subs += n
        total_runs += 1
        if total_subs == 0:
            break
        print(f"Pass {total_runs}: {total_subs} lines changed")
    return total_runs


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
        targets = [md_dir]
        print("Running until convergence...")
        runs = process_all(targets)
        print(f"Converged after {runs} pass(es)")


if __name__ == '__main__':
    main()
