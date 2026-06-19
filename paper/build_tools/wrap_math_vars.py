#!/usr/bin/env python3
"""
wrap_math_vars.py - Wrap physics variables in $...$ math mode
==================================================================

RULE 2 from build_pdf.sh (Section 4.3.2):
  Physical quantities with subscripts/superscripts MUST be in $...$ math.

This script wraps standalone variables like:
  H_0  ->  $H_0$
  M_Pl ->  $M_{\rm Pl}$
  f_back ->  $f_{\rm back}$
  E_4D ->  $E_{\rm 4D}$

Usage:
  python3 wrap_math_vars.py [build_dir]

If build_dir is not given, applies to paper/markdown/*.md in place.
"""
import re
import os
import sys


# Variables to wrap, with their math forms
# Format: (regex_pattern, latex_math_form)
# Order matters: more specific patterns first

VARS = [
    # M_Pl variants (most specific first)
    (r'\bM_Pl,4D\b', '$M_{\\rm Pl,4D}$'),
    (r'\bM_Pl,3\+1D\b', '$M_{\\rm Pl,3+1D}$'),
    (r'\bM_Pl,3D\b', '$M_{\\rm Pl,3D}$'),
    (r'\bM_Pl,2D\b', '$M_{\\rm Pl,2D}$'),
    (r'\bM_Pl,9D\b', '$M_{\\rm Pl,9D}$'),
    (r'\bM_Pl,N\b', '$M_{\\rm Pl,N}$'),
    (r'\bM_Pl,3\b', '$M_{\\rm Pl,3}$'),
    (r'\bM_Pl,4\b', '$M_{\\rm Pl,4}$'),
    (r'\bM_Pl\b', '$M_{\\rm Pl}$'),

    # t_Pl variants
    (r'\bt_Pl,3\b', '$t_{\\rm Pl,3}$'),
    (r'\bt_Pl,4\b', '$t_{\\rm Pl,4}$'),
    (r'\bt_Pl,N\b', '$t_{\\rm Pl,N}$'),
    (r'\bt_Pl\b', '$t_{\\rm Pl}$'),

    # Energy scales
    (r'\bE_4D\b', '$E_{\\rm 4D}$'),
    (r'\bE_5D\b', '$E_{\\rm 5D}$'),
    (r'\bE_3\+1D\b', '$E_{\\rm 3+1D}$'),
    (r'\bE_3D\b', '$E_{\\rm 3D}$'),
    (r'\bE_SN\b', '$E_{\\rm SN}$'),
    (r'\bE_AGN\b', '$E_{\\rm AGN}$'),
    (r'\bE_2D\b', '$E_{\\rm 2D}$'),

    # Mass scales
    (r'\bM_4D\b', '$M_{\\rm 4D}$'),
    (r'\bM_5D\b', '$M_{\\rm 5D}$'),
    (r'\bM_2D\b', '$M_{\\rm 2D}$'),
    (r'\bM_3\+1D\b', '$M_{\\rm 3+1D}$'),

    # Time
    (r'\btau_2D\b', '$\\tau_{\\rm 2D}$'),
    (r'\btau_3D\b', '$\\tau_{\\rm 3D}$'),
    (r'\btau_4D\b', '$\\tau_{\\rm 4D}$'),
    (r'\btau_5D\b', '$\\tau_{\\rm 5D}$'),

    # Time dilation
    (r'\bgamma_ND\b', '$\\gamma_{\\rm ND}$'),
    (r'\bgamma_4D\b', '$\\gamma_{\\rm 4D}$'),
    (r'\bgamma_5D\b', '$\\gamma_{\\rm 5D}$'),

    # Action sectors
    (r'\bS_SIDC\b', '$S_{\\rm SIDC}$'),
    (r'\bS_4D_event\b', '$S_{\\rm 4D,event}$'),
    (r'\bS_3\+1D_brane\b', '$S_{\\rm 3+1D,brane}$'),
    (r'\bS_3\+1D\b', '$S_{\\rm 3+1D}$'),
    (r'\bS_2D_universe\b', '$S_{\\rm 2D,universe}$'),
    (r'\bS_2D\b', '$S_{\\rm 2D}$'),
    (r'\bS_4D\b', '$S_{\\rm 4D}$'),
    (r'\bS_5D\b', '$S_{\\rm 5D}$'),
    (r'\bS_projection\b', '$S_{\\rm projection}$'),
    (r'\bS_Liouville\b', '$S_{\\rm Liouville}$'),
    (r'\bS_Ising\b', '$S_{\\rm Ising}$'),
    (r'\bS_SYK\b', '$S_{\\rm SYK}$'),
    (r'\bS_bdy\b', '$S_{\\rm bdy}$'),

    # User-mentioned
    (r'\bv_Higgs\b', '$v_{\\rm Higgs}$'),
    (r'\bM_string\b', '$M_{\\rm string}$'),
    (r'\bm_string\b', '$m_{\\rm string}$'),
    # f_back was renamed to f_DE / f_DM_leak / f_DM_death (v3.5.7)
    # These new names are preserved as-is (don't wrap with extra $)
    (r'\bf_DE\b', '$f_{\\rm DE}$'),
    (r'\bf_DM_leak\b', '$f_{\\rm DM,leak}$'),
    (r'\bf_DM_death\b', '$f_{\\rm DM,death}$'),
    (r'\bf_back\b(?!\d|_|\^)', '$f_{\\rm back}$'),  # legacy f_back only
    (r'\bf_active\b', '$f_{\\rm active}$'),

    # SM fermions
    (r'\bu_L\b', '$u_L$'),
    (r'\bd_L\b', '$d_L$'),
    (r'\be_L\b', '$e_L$'),
    (r'\bu_R\b', '$u_R$'),
    (r'\bd_R\b', '$d_R$'),
    (r'\be_R\b', '$e_R$'),
    (r'\bnu_L\b', '$\\nu_L$'),
    (r'\bnu_R\b', '$\\nu_R$'),

    # Mass
    (r'\bM_dyn\b', '$M_{\\rm dyn}$'),
    (r'\bM_b\b', '$M_b$'),
    (r'\bm_3\+1D\b', '$m_{3+1D}$'),
    (r'\bm_2D\b', '$m_{\\rm 2D}$'),

    # Couplings
    (r'\bg_2D\b', '$g_{\\rm 2D}$'),
    (r'\bg_\+(?=[^a-zA-Z0-9_]|$)', '$g_+$'),
    (r'\bg_-\b', '$g_-$'),

    # Other
    (r'\bF_p\b', '$F_p$'),
    (r'\bH_0\b', '$H_0$'),
    (r'\bkL\b', '$kL$'),
]


def is_in_math(text, pos):
    """Check if position is inside $...$ or $$...$$.
    Uses precomputed math ranges for speed and correctness."""
    if not hasattr(is_in_math, '_text') or is_in_math._text is not text:
        is_in_math._ranges = find_math_ranges(text)
        is_in_math._text = text
    for start, end in is_in_math._ranges:
        if start <= pos < end:
            return True
    return False


def find_math_ranges(text):
    """Find all positions where text is inside math mode (display OR inline).
    Returns list of (start, end) character ranges covering math content (excluding delimiters)."""
    ranges = []
    
    # Find ALL $$...$$ display math blocks
    i = 0
    while i < len(text) - 1:
        if text[i] == '\\' and i + 1 < len(text):
            i += 2
            continue
        if text[i] == '$' and text[i+1] == '$':
            j = i + 2
            while j < len(text) - 1:
                if text[j] == '\\' and j + 1 < len(text):
                    j += 2
                    continue
                if text[j] == '$' and text[j+1] == '$':
                    ranges.append((i+2, j))
                    i = j + 2
                    break
                j += 1
            else:
                ranges.append((i+2, len(text)))
                i = len(text)
        else:
            i += 1
    
    # Find ALL $...$ inline math blocks (skip ones that are part of $$)
    i = 0
    while i < len(text):
        if text[i] == '\\' and i + 1 < len(text):
            i += 2
            continue
        if text[i] == '$':
            # Skip if this $ is part of $$
            if i + 1 < len(text) and text[i+1] == '$':
                i += 2
                continue
            # Skip if previous char is $ (i.e., this is the second $ of $$)
            if i > 0 and text[i-1] == '$':
                i += 1
                continue
            # Find closing $
            j = i + 1
            while j < len(text):
                if text[j] == '\\' and j + 1 < len(text):
                    j += 2
                    continue
                if text[j] == '$':
                    # Check it's not $$
                    if j + 1 < len(text) and text[j+1] == '$':
                        # This is part of $$, so it's not the close of inline
                        j += 1
                        continue
                    ranges.append((i+1, j))
                    i = j + 1
                    break
                j += 1
            else:
                i += 1
        else:
            i += 1
    
    return ranges


def is_in_code(text, pos):
    """Check if position is inside a code block"""
    pat = re.compile(r'^```', re.MULTILINE)
    matches = list(pat.finditer(text, 0, pos))
    return len(matches) % 2 == 1


def process_file(filepath):
    """Wrap variables in math mode in a file."""
    with open(filepath) as f:
        content = f.read()

    changes = 0
    for pattern, repl_math in VARS:
        # Find all matches NOT in math mode
        replacements = []  # (start, end, new_text)
        for match in re.finditer(pattern, content):
            pos = match.start()
            if is_in_math(content, pos):
                continue
            if is_in_code(content, pos):
                continue
            # Skip if char immediately before or after is $ (already touching math)
            if pos > 0 and content[pos-1] == '$':
                continue
            end = match.end()
            if end < len(content) and content[end] == '$':
                continue
            replacements.append((pos, end, repl_math))

        if not replacements:
            continue

        # Apply replacements from end to start (preserves positions)
        replacements.sort(reverse=True)
        new_content = content
        for pos, end, repl in replacements:
            new_content = new_content[:pos] + repl + new_content[end:]
        content = new_content
        changes += len(replacements)

    if changes > 0:
        with open(filepath, 'w') as f:
            f.write(content)

    return changes


def main():
    if len(sys.argv) > 1:
        # Single file mode
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
        # Default: process paper/markdown/*.md
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
