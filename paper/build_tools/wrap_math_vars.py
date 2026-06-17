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
    (r'\bf_back\b(?!\d|_|\^)', '$f_{\\rm back}$'),  # NOT f_back_3 etc.
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
    (r'\bg_+\b', '$g_+$'),
    (r'\bg_-\b', '$g_-$'),

    # Other
    (r'\bF_p\b', '$F_p$'),
    (r'\bH_0\b', '$H_0$'),
    (r'\bkL\b', '$kL$'),
]


def is_in_math(text, pos):
    """Check if position is inside $...$ or $$...$$"""
    state = 'text'
    i = 0
    while i < pos:
        if text[i] == '\\' and i + 1 < len(text):
            i += 2
            continue
        if text[i] == '$':
            if i + 1 < len(text) and text[i+1] == '$':
                if state == 'display_math':
                    state = 'text'
                else:
                    state = 'display_math'
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
        candidates = []
        for match in re.finditer(pattern, content):
            if is_in_math(content, match.start()):
                continue
            if is_in_code(content, match.start()):
                continue
            candidates.append(match.group(0))

        if not candidates:
            continue

        changes += len(candidates)
        content = re.sub(pattern, lambda m: repl_math, content)

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
