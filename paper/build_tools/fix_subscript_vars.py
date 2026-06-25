#!/usr/bin/env python3
"""
fix_subscript_vars.py - Wrap subscript variable references in math mode.

Problem: Plain text like 'l_12', 'r_12', 'D_A', 'θ_*', 'r_s', 'ω_b' etc.
appears in narrative without being wrapped in $...$ math mode. In LaTeX,
'_' followed by a letter outside math mode is either an error or renders
as a plain underscore.

What it does:
- Tracks math state ($...$, $$...$$, code blocks, code spans)
- Outside math, finds patterns like X_Y where X is letter and Y is letter/digit
- Wraps them in $...$ with proper LaTeX subscript: $X_{Y}$
- Skips common false positives: URLs, filenames, code blocks
- Handles compound subscripts: r_12_disk → $r_{\rm 12,disk}$

Pattern categories (from SIDC paper):
- CMB/cosmology: l_12, r_12, D_A, θ_*, r_s, ω_b, ω_c
- SIDC variables: τ_2D, τ_4D, γ_4D, α_2D, f_leak, N_sub, M_Pl,3D
- Mathematical: x_y (general)

Usage:
    python3 fix_subscript_vars.py FILE [FILE ...]   # fix specific files
    python3 fix_subscript_vars.py --all            # fix all paper files
"""

import os
import re
import sys

# Common false positives that should NOT be wrapped
SKIP_PATTERNS = [
    re.compile(r'https?://\S+'),          # URLs
    re.compile(r'\S+\.(?:md|pdf|tex|py|json|toml|yaml|yml|cff)\b'),  # filenames
    re.compile(r'paper_arxiv|legacy_paper|ai_disclosure|persistent_memory'),  # specific filenames
    re.compile(r'^[a-z]_[a-z]$'),  # Common two-letter combinations like i_e, e_g
]

# Compound subscript patterns (handle first, more specific)
COMPOUND_PATTERNS = [
    # r_12_disk, r_12_halo, r_12_cluster, r_12_galaxy, r_12_group
    (re.compile(r'\br_12_(disk|halo|cluster|galaxy|group)\b'),
     r'$r_{\rm 12,\1}$'),
    # l_12_disk, l_12_halo etc. (probably rare but for completeness)
    (re.compile(r'\bl_12_(disk|halo|cluster|galaxy|group)\b'),
     r'$l_{\rm 12,\1}$'),
    # M_Pl,3D / M_Pl,4D / M_Pl,2D (compound with comma)
    (re.compile(r'\bM_Pl,(\dD|\d\+1D|\d\+1D)\b'),
     r'$M_{\rm Pl,\1}$'),
    # τ_3D,apparent / τ_3+1D
    (re.compile(r'\bτ_(\dD,apparent|\d\+1D)\b'),
     r'$\\tau_{\\rm \1}$'),
]

# Single subscript patterns
SINGLE_PATTERNS = [
    (re.compile(r'\br_12\b'),     r'$r_{12}$'),
    (re.compile(r'\bl_12\b'),     r'$l_{12}$'),
    (re.compile(r'\bD_A\b'),      r'$D_A$'),
    (re.compile(r'\br_s\b'),      r'$r_s$'),
    (re.compile(r'\bθ_\*'),       r'$\\theta_*$'),
    (re.compile(r'\bω_b\b'),      r'$\\omega_b$'),
    (re.compile(r'\bω_c\b'),      r'$\\omega_c$'),
    (re.compile(r'\bω_m\b'),      r'$\\omega_m$'),
    (re.compile(r'\bτ_2D\b'),     r'$\\tau_{\\rm 2D}$'),
    (re.compile(r'\bτ_4D\b'),     r'$\\tau_{\\rm 4D}$'),
    (re.compile(r'\bτ_3D\b'),     r'$\\tau_{\\rm 3D}$'),
    (re.compile(r'\bγ_2D\b'),     r'$\\gamma_{\\rm 2D}$'),
    (re.compile(r'\bγ_4D\b'),     r'$\\gamma_{\\rm 4D}$'),
    (re.compile(r'\bα_2D\b'),     r'$\\alpha_{\\rm 2D}$'),
    (re.compile(r'\bα_4D\b'),     r'$\\alpha_{\\rm 4D}$'),
    (re.compile(r'\bα_3\+1D\b'),  r'$\\alpha_{\\rm 3+1D}$'),
    (re.compile(r'\bZ_12\b'),     r'$Z_{12}$'),
    (re.compile(r'\bZ_2\b'),      r'$Z_2$'),
]


def is_in_math(line_so_far):
    """Return True if the position is inside math mode for the given line so far."""
    n_dollars = 0
    i = 0
    while i < len(line_so_far):
        ch = line_so_far[i]
        if ch == '\\' and i + 1 < len(line_so_far):
            i += 2
            continue
        if ch == '$':
            n_dollars += 1
        i += 1
    return n_dollars % 2 == 1


def is_in_code_block(lines, line_idx):
    """Return True if line_idx is inside a code block (```...```)."""
    in_code = False
    for i in range(line_idx):
        if lines[i].strip().startswith('```'):
            in_code = not in_code
    return in_code


def is_in_inline_code(line, pos):
    """Return True if pos is inside an inline code span `...`."""
    # Look for `...` on the line
    i = 0
    while i < pos:
        if line[i] == '`':
            # Find closing backtick
            j = i + 1
            while j < len(line) and line[j] != '`':
                j += 1
            if j < len(line):
                # Have closing
                if i < pos < j:
                    return True
                i = j + 1
            else:
                i += 1
        else:
            i += 1
    return False


def should_skip_line(line):
    """Skip lines that are URLs, code, etc."""
    for pat in SKIP_PATTERNS:
        if pat.search(line):
            return True
    return False


def fix_line(line, compound_patterns, single_patterns):
    """Apply patterns to a single line. Track math state."""
    if should_skip_line(line):
        return line, 0

    # Apply compound patterns first
    n_fixes = 0
    new_line = line

    # Process patterns, but skip if in math
    for pat, repl in compound_patterns + single_patterns:
        result = ''
        i = 0
        while i < len(new_line):
            m = pat.match(new_line, i)
            if m:
                # Check math context up to here
                if is_in_math(result) or is_in_inline_code(new_line, i):
                    result += new_line[i:i+1]
                    i += 1
                    continue
                # Apply replacement
                replacement_text = m.expand(repl)
                # Check if we just added math - if so, that's a fix
                if '$' in replacement_text and m.group(0) not in replacement_text:
                    n_fixes += 1
                result += replacement_text
                i = m.end()
            else:
                result += new_line[i]
                i += 1
        new_line = result

    return new_line, n_fixes


def fix_file(filepath):
    """Fix all subscript variables in a file."""
    if not os.path.exists(filepath):
        print(f'  SKIP (not found): {filepath}')
        return 0

    with open(filepath) as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    total_fixes = 0

    for idx, line in enumerate(lines):
        if is_in_code_block(lines, idx):
            new_lines.append(line)
            continue
        new_line, n = fix_line(line, COMPOUND_PATTERNS, SINGLE_PATTERNS)
        new_lines.append(new_line)
        total_fixes += n

    new_content = '\n'.join(new_lines)
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        if total_fixes > 0:
            print(f'  {filepath}: {total_fixes} fixes')

    return total_fixes


def main():
    # Determine target files
    if '--all' in sys.argv:
        files = [
            'README.md', 'STATE_OF_THE_MODEL.md', 'changelog.md',
            'persistent_memory.md',
        ]
        md_dir = 'paper/markdown'
        if os.path.isdir(md_dir):
            for f in sorted(os.listdir(md_dir)):
                if f.endswith('.md'):
                    files.append(os.path.join(md_dir, f))
    else:
        files = [f for f in sys.argv[1:] if not f.startswith('--')]

    if not files:
        print('Usage: fix_subscript_vars.py FILE [FILE ...] | --all')
        sys.exit(1)

    grand_total = 0
    for fp in files:
        n = fix_file(fp)
        grand_total += n

    print(f'\nTotal: {grand_total} subscript variable fixes')


if __name__ == '__main__':
    main()