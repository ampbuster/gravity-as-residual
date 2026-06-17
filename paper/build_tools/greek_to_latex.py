#!/usr/bin/env python3
"""
greek_to_latex.py - Convert Unicode Greek letters to LaTeX commands
=====================================================================

RULE 8 from build_pdf.sh (Section 4.3.2):
  Greek letters always as \alpha not α

Converts standalone Unicode Greek letters (outside math mode) to LaTeX
commands wrapped in $...$.

NOTE: Most Greek letters in this paper are ALREADY in math mode.
This script targets standalone Greek in body text.

Usage:
  python3 greek_to_latex.py [build_dir]
"""
import re
import os
import sys


# Map of Unicode Greek letter -> LaTeX command
GREEK_MAP = {
    'α': r'\alpha', 'β': r'\beta', 'γ': r'\gamma', 'δ': r'\delta',
    'ε': r'\epsilon', 'ζ': r'\zeta', 'η': r'\eta', 'θ': r'\theta',
    'ι': r'\iota', 'κ': r'\kappa', 'λ': r'\lambda', 'μ': r'\mu',
    'ν': r'\nu', 'ξ': r'\xi', 'π': r'\pi', 'ρ': r'\rho',
    'σ': r'\sigma', 'τ': r'\tau', 'φ': r'\phi', 'χ': r'\chi',
    'ψ': r'\psi', 'ω': r'\omega',
    'Γ': r'\Gamma', 'Δ': r'\Delta', 'Θ': r'\Theta', 'Λ': r'\Lambda',
    'Ξ': r'\Xi', 'Π': r'\Pi', 'Σ': r'\Sigma', 'Φ': r'\Phi',
    'Ψ': r'\Psi', 'Ω': r'\Omega',
}


def is_in_math(text, pos):
    """Check if position pos is inside math mode ($...$ or $$...$$)."""
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
    """Check if position pos is inside a code block (```...```)."""
    pat = re.compile(r'^```', re.MULTILINE)
    matches = list(pat.finditer(text, 0, pos))
    return len(matches) % 2 == 1


def process_file(filepath):
    """
    Convert standalone Greek letters to LaTeX.
    Uses a SINGLE pass: builds a list of replacements, then applies them.
    """
    with open(filepath) as f:
        content = f.read()

    # Find all positions for each Greek char (in original content)
    # Build a list of (position, original_char, latex_cmd) for chars NOT in math/code
    candidates = []  # (position, char, latex_cmd)
    for unicode_char, latex_cmd in GREEK_MAP.items():
        for match in re.finditer(re.escape(unicode_char), content):
            pos = match.start()
            if is_in_math(content, pos):
                continue
            if is_in_code(content, pos):
                continue
            candidates.append((pos, unicode_char, latex_cmd))

    if not candidates:
        return 0

    # Sort by position (descending so we can apply from end to start)
    candidates.sort(key=lambda x: x[0], reverse=True)

    # Apply replacements from end to start
    # Each replacement: standalone Greek -> $\command$
    new_content = content
    for pos, char, cmd in candidates:
        # Check if already wrapped (e.g., user wrote $α$)
        before = new_content[max(0, pos-1):pos]
        after = new_content[pos+1:pos+2]
        if before == '$' and after == '$':
            # Already in math mode, just replace char
            new_content = new_content[:pos] + cmd + new_content[pos+1:]
        else:
            # Wrap in $...$
            new_content = new_content[:pos] + '$' + cmd + '$' + new_content[pos+1:]

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
    return len(candidates)


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
