#!/usr/bin/env python3
"""
Audit for various broken math patterns that may have been missed.

Look for:
1. Pattern 22 collateral damage: X.$\math$ where X. was outside
2. Multiple consecutive $ (e.g., $$..$ or $..$$)
3. Spaces inside math that should be outside
4. Missing { } for subscript/superscript
5. Other LaTeX errors
"""
import os
import re
import sys

def get_files():
    files = []
    for root, dirs, fs in os.walk('paper/markdown'):
        for f in fs:
            if f.endswith('.md'):
                files.append(os.path.join(root, f))
    files += ['README.md', 'changelog.md', 'persistent_memory.md', 'STATE_OF_THE_MODEL.md']
    return [f for f in files if os.path.exists(f)]


def find_pattern22_collateral(content):
    """Find X.$\math$ where Pattern 22 may have inserted orphan $"""
    # Looking for any 'X.$\\Y$' where it looks like the $ is in wrong place
    issues = []
    # digit.$\digit (where this could have been X.X$\sigma$ before)
    for m in re.finditer(r'(\d+)\.\$(\d+)', content):
        line_start = content.rfind('\n', 0, m.start()) + 1
        line_end = content.find('\n', m.start())
        line = content[line_start:line_end]
        line_num = content[:m.start()].count('\n') + 1
        issues.append((line_num, line, f"Possible Pattern 22 collateral: '{m.group(0)}'"))
    return issues


def find_unbalanced_braces_in_math(content):
    """Find { in math without matching }"""
    issues = []
    in_math = False
    in_code = False
    brace_depth = 0
    
    for i, char in enumerate(content):
        if content[i:i+3] == '```':
            in_code = not in_code
            continue
        if in_code:
            continue
        if char == '$':
            in_math = not in_math
            if not in_math and brace_depth > 0:
                # Math ended with unbalanced
                line_start = content.rfind('\n', 0, i) + 1
                line_end = content.find('\n', i)
                line = content[line_start:line_end]
                line_num = content[:i].count('\n') + 1
                issues.append((line_num, line, f"Unbalanced {{ in math (depth {brace_depth})"))
            brace_depth = 0
            continue
        if in_math:
            if char == '{':
                brace_depth += 1
            elif char == '}':
                brace_depth -= 1
    return issues


def find_double_dollars(content):
    """Find $$$ or $$..$$ that might be wrong"""
    issues = []
    for m in re.finditer(r'\$\$\$(?!\$)', content):
        line_start = content.rfind('\n', 0, m.start()) + 1
        line_end = content.find('\n', m.start())
        line = content[line_start:line_end]
        line_num = content[:m.start()].count('\n') + 1
        issues.append((line_num, line, f"Triple $$$ (should be $$)"))
    return issues


def find_orphan_close(content):
    """Find $ at end of line that might be orphan"""
    issues = []
    in_code = False
    for i, line in enumerate(content.split('\n'), 1):
        if line.strip().startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        # Strip trailing whitespace
        s = line.rstrip()
        # Count $ in line
        dollar_count = s.count('$')
        if dollar_count % 2 != 0:
            # Odd number - check if last $ is "dangling"
            issues.append((i, line, f"Odd $ count ({dollar_count})"))
    return issues


def main():
    files = get_files()
    total_issues = 0
    for fp in files:
        with open(fp, 'r') as f:
            content = f.read()
        
        all_issues = []
        all_issues += find_pattern22_collateral(content)
        all_issues += find_unbalanced_braces_in_math(content)
        all_issues += find_double_dollars(content)
        # Skip orphan close - too noisy for short lines
        
        if all_issues:
            print(f"\n=== {fp} ===")
            for line_num, line, issue in all_issues[:10]:
                print(f"  L{line_num}: {issue}")
                print(f"    {line[:150]}")
                total_issues += 1
    
    print(f"\n\nTotal issues: {total_issues}")


if __name__ == '__main__':
    main()
