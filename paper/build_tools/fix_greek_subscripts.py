#!/usr/bin/env python3
"""
fix_greek_subscripts.py - Fix broken Greek+subscript patterns
==================================================================

When greek_to_latex.py wraps Greek letters, it only wraps the Greek
character and leaves the subscript outside the math. This creates
broken patterns like:

  $\tau$_obs        (should be $\tau_{\rm obs}$)
  $\rho$_Pl          (should be $\rho_{\rm Pl}$)
  $\Omega$_DM        (should be $\Omega_{\rm DM}$)
  $\gamma$_4D        (should be $\gamma_{\rm 4D}$)

This script finds and fixes these patterns.

Usage:
  python3 fix_greek_subscripts.py [file_or_dir]
  python3 fix_greek_subscripts.py                  # Process all paper/markdown/*.md
  python3 fix_greek_subscripts.py path/to/file.md # Process single file
"""
import os
import re
import sys


# Greek letters that can be wrapped
GREEK_LETTERS = [
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta',
    'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'pi', 'rho', 'sigma',
    'tau', 'phi', 'chi', 'psi', 'omega',
    'Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta',
    'Iota', 'Kappa', 'Lambda', 'Mu', 'Nu', 'Xi', 'Pi', 'Rho', 'Sigma',
    'Tau', 'Phi', 'Chi', 'Psi', 'Omega',
]


def fix_broken_greek_subscripts(content):
    """
    Fix patterns like $\\tau$_obs to $\\tau_{\\rm obs}$.
    
    Looks for:
    - $\\greek$_<word>  where <word> is alphanumeric (with optional underscores)
    - $\\greek$_<digits>  where <digits> is a number
    
    Replaces with:
    - $\\greek_{\\rm <word>}$
    - $\\greek_{<digits>}$
    """
    changes = 0
    for greek in GREEK_LETTERS:
        # Pattern 1: $\greek$_<word>  (single word subscript)
        # e.g., $\tau$_obs, $\rho$_Pl, $\Omega$_DM
        pattern_word = r'\$\\' + greek + r'\$_(\w+)(?!\})'
        def repl_word(m, g=greek):
            return f'$\\{g}_{{\\rm {m.group(1)}}}$'
        new_content = re.sub(pattern_word, repl_word, content)
        changes += len(re.findall(pattern_word, content))
        content = new_content

        # Pattern 2: $\greek$_<digits>  (numeric subscript)
        # e.g., $\tau$_2D, $\gamma$_4D, $\rho$_DE
        pattern_num = r'\$\\' + greek + r'\$_(\d+\w*)'
        def repl_num(m, g=greek):
            return f'$\\{g}_{{{m.group(1)}}}$'
        new_content = re.sub(pattern_num, repl_num, content)
        changes += len(re.findall(pattern_num, content))
        content = new_content

        # Pattern 3: $\greek$ <word>  (space, no underscore, but should be subscript)
        # This is rarer but handles cases like $\tau$ 2D
        # Skip for now - too ambiguous

    return content, changes


def process_file(filepath):
    """Fix broken Greek subscript patterns in a single file."""
    with open(filepath, 'r') as f:
        content = f.read()

    new_content, changes = fix_broken_greek_subscripts(content)

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

    # Default: process all paper/markdown/*.md AND supporting/*.md
    # Also process a few root files
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
