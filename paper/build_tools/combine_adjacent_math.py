#!/usr/bin/env python3
"""
Combine adjacent math expressions separated by whitespace, ~, or ≈.

Patterns handled:
- $X$  $Y$       → $X Y$
- ~$X$  $Y$      → $\sim X Y$
- ≈$X$  $Y$      → $\approx X Y$
- $X$ ~ $Y$      → $X \sim Y$
- $X$ ≈ $Y$      → $X \approx Y$
- $X$  $Y$ ~ $Z$ → $X Y \sim Z$   (chain)
- $X$ ~ $Y$  $Z$ → $X \sim Y Z$   (chain)

Idempotent: re-running produces no changes.
"""
import os
import re
import sys


def find_math_ranges(line):
    """Return list of (start, end) for each $...$ math expression in line."""
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




def handle_single_math(line):
    """Handle ~ or ≈ before a single math expression (not in a pair).
    Pattern: text ~ $X$ → text $\sim X$
    Pattern: text ≈ $X$ → text $\approx X$
    """
    ranges = find_math_ranges(line)
    if not ranges:
        return line
    
    result = []
    pos = 0
    for r_start, r_end in ranges:
        prefix = line[pos:r_start]
        # Check for ~ or ≈ before
        tilde_match = re.search(r'~\s*$', prefix)
        approx_match = re.search(r'≈\s*$', prefix)
        
        if tilde_match:
            stripped = prefix[:tilde_match.start()]
            content = line[r_start + 1:r_end - 1]
            result.append(stripped)
            result.append('$\\sim ' + content + '$')
        elif approx_match:
            stripped = prefix[:approx_match.start()]
            content = line[r_start + 1:r_end - 1]
            result.append(stripped)
            result.append('$\\approx ' + content + '$')
        else:
            result.append(prefix)
            result.append(line[r_start:r_end])
        
        pos = r_end
    
    if pos < len(line):
        result.append(line[pos:])
    
    return ''.join(result)




def combine_adjacent(line):
    """Find adjacent $X$  $Y$ patterns and combine them with ~ or ≈ handling."""
    ranges = find_math_ranges(line)
    if len(ranges) < 2:
        return line

    result = []
    pos = 0
    i = 0

    while i < len(ranges):
        r1_start, r1_end = ranges[i]
        prefix = line[pos:r1_start]

        if i + 1 < len(ranges):
            r2_start, r2_end = ranges[i + 1]
            between = line[r1_end:r2_start]

            # Check what's in between
            adjacent = (between.strip() == '')
            between_tilde = bool(re.search(r'^\s*~\s*$', between))
            between_approx = bool(re.search(r'^\s*≈\s*$', between))

            if adjacent or between_tilde or between_approx:
                # Combine!
                r1_content = line[r1_start + 1:r1_end - 1]
                r2_content = line[r2_start + 1:r2_end - 1]

                # Check for ~ or ≈ before r1 (in prefix)
                tilde_match = re.search(r'~\s*$', prefix)
                approx_match = re.search(r'≈\s*$', prefix)

                # Decide what to do based on prefix and between
                if tilde_match and (adjacent or between_tilde or between_approx):
                    # Strip ~ from prefix; keep trailing space
                    stripped = prefix[:tilde_match.start()]
                    result.append(stripped)
                    if between_approx:
                        combined = r1_content + ' \\approx ' + r2_content
                    elif between_tilde:
                        combined = r1_content + ' \\sim ' + r2_content
                    else:  # adjacent
                        combined = '\\sim ' + r1_content + ' ' + r2_content
                elif approx_match and (adjacent or between_tilde or between_approx):
                    # Strip ≈ from prefix; keep trailing space
                    stripped = prefix[:approx_match.start()]
                    result.append(stripped)
                    if between_approx:
                        combined = r1_content + ' \\approx ' + r2_content
                    elif between_tilde:
                        combined = r1_content + ' \\sim ' + r2_content
                    else:  # adjacent
                        combined = '\\approx ' + r1_content + ' ' + r2_content
                elif between_approx:
                    result.append(prefix)
                    combined = r1_content + ' \\approx ' + r2_content
                elif between_tilde:
                    result.append(prefix)
                    combined = r1_content + ' \\sim ' + r2_content
                else:
                    result.append(prefix)
                    combined = r1_content + ' ' + r2_content

                result.append('$' + combined + '$')
                pos = r2_end
                i += 2
                continue

        # Not adjacent and no ~ / ≈ between
        result.append(prefix)
        result.append(line[r1_start:r1_end])
        pos = r1_end
        i += 1

    # Append remaining text
    if pos < len(line):
        result.append(line[pos:])

    return ''.join(result)


def process_line(line):
    """Process a line, skipping inline code spans.
    Safety: skip lines with odd $ count (unbalanced math per-line)."""
    # Per-line safety check
    test = re.sub(r'\\$', '', line)
    test = re.sub(r'`[^`\n]*`', '', test)
    if test.count('$') % 2 == 1:
        return line  # Skip lines with odd $ count
    parts = re.split(r'(`[^`\n]*`)', line)
    result = []
    for part in parts:
        if part.startswith('`') and part.endswith('`') and len(part) >= 2:
            result.append(part)
        else:
            # First pass: handle single-math ~ and ≈
            part = handle_single_math(part)
            # Second pass: combine adjacent math
            part = combine_adjacent(part)
            result.append(part)
    return ''.join(result)


def process_file(path):
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
