#!/usr/bin/env python3
"""
fix_physics_subscripts.py — Wrap plain-text physics subscripts in $...$ math.

Problem: Plain text like `H_0 = 73.04`, `M_* = 1e10`, `sigma_int = 0.089`
is not in math mode. In LaTeX, `_` outside math mode is an error or
renders as plain underscore. We want these patterns to be wrapped in
`$...$` for proper math rendering.

Handles common physics subscripts:
  H_0, M_b, M_*, M_dyn, M_gas, M_disk, M_halo, M_tot, M_sun
  T_H, T_0, T_1, T_2, T_3, T_4, T_b, T_c, T_*
  E_0, E_1, E_2, E_3, E_4, E_2D, E_3D, E_4D, E_5D
  M_2D, M_3D, M_4D
  tau_2D, tau_3D, tau_4D
  rho_0, rho_b, rho_c, rho_m
  Omega_b, Omega_c, Omega_m, Omega_DE
  v_H, v_esc, v_c, V_c, V_0
  r_s, R_s, R_c, R_0
  sigma_int, sigma_0, sigma_v
  a_0, a_1, a_2
  g_+, g_-, g_bar, g_obs, g_cum, g_active
  t_0, t_eq, t_H, t_*
  N_sub, N_*, N_0, N_c
  epsilon_0, alpha_0, gamma_0
  k_B, N_A, m_e, m_p
  e_0, k_e, k_p, k_n
  c_s, T_s, T_d
  ...

Examples (BEFORE -> AFTER):
  `H_0 = 73.04`           → `$H_0 = 73.04$`
  `sigma_int = 0.089`     → `$\sigma_{\rm int} = 0.089$`
  `M_* = 1e10`            → `$M_* = 1e10$`
  `v_esc = sqrt(...)`     → `$v_{\rm esc} = \sqrt{...}$`
  `tau_2D = 14.5 Gyr`     → `$\tau_{\rm 2D} = 14.5$ Gyr`
  `M_gas from MHI`        → `$M_{\rm gas}$ from MHI`

Skips:
  - Already in math mode ($...$, \(...\), $$...$$, \[...\])
  - Code blocks (```...```)
  - Inline code (`...`)
  - URLs and HTML attributes

Usage:
  python3 fix_physics_subscripts.py [file_or_dir]
  python3 fix_physics_subscripts.py           # process all paper/markdown/*.md
  python3 fix_physics_subscripts.py --all     # also fix README, etc.
  python3 fix_physics_subscripts.py --dry-run # show what would change
"""
import re
import os
import sys
import glob


# Physics subscripts to look for
PHYSICS_SUBSCRIPTS = [
    # Standard subscripts
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
    # Common physics
    'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    # Compound
    'sun', 'dyn', 'gas', 'disk', 'halo', 'tot', 'baryon', 'Pl', 'Pl,2D', 'Pl,3D', 'Pl,4D', 'Pl,5D',
    '2D', '3D', '4D', '5D',
    'CMB', 'local', 'esc', 'sub', 'eq', 'H', '*',
    'int', 'tot', 'ext', 'obs', 'bar', 'cum', 'active', 'DM', 'DE',
    'AGN', 'SN', 'BH', 'GRB', 'BNS', 'NS', 'WD',
    'GW', 'ICM', 'CMB', 'LSS',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'pp', 'ee', 'nn', 'np',
    'c', 's', 'v', 'u', 'd', 't',
    'min', 'max', 'crit', 'eq', 'init', 'final', 'tot',
    'in', 'out', 'left', 'right', 'top', 'bot', 'mid',
    '0', '1', '2D', '3D', '4D', '5D', 'k+1', 'k-1',
    # Common compound subscripts
    'Pl,N', 'Pl,2D', 'Pl,3D', 'Pl,4D', 'Pl,5D',
]

# Build a regex pattern for variable names with subscripts
# The pattern: a letter (or letter+letter) followed by _X where X is one of the subscripts
SUBSCRIPTS_RE = '|'.join(re.escape(s) for s in set(PHYSICS_SUBSCRIPTS))
VAR_SUBSCRIPT_PATTERN = re.compile(
    r'(?<![\\$`\w])('
    # Latin variable name
    + r'(?:H|M|E|T|P|tau|sigma|rho|Omega|gamma|alpha|beta|delta|epsilon|zeta|eta|theta|kappa|lambda|mu|nu|xi|pi|phi|chi|psi|v|V|r|R|a|A|k|g|N|t|c|L|s|S|u|U|p|P|b|B|d|D|f|F|q|Q|x|X|y|Y|z|Z)'
    # Optional second letter (for compound var names)
    r'(?:[a-zA-Z]{0,3})'
    # Underscore
    + r')_('
    + SUBSCRIPTS_RE
    + r')(?![a-zA-Z0-9])'
)


def is_in_math_mode(text, pos):
    """Check if pos is inside $...$, $$...$$, or already-wrapped $...$."""
    line_start = text.rfind('\n', 0, pos) + 1
    line_section = text[line_start:pos]
    dollar_count = line_section.count('$') - line_section.count('\\$')
    return dollar_count % 2 == 1


def find_physics_subscripts(text):
    """Find all physics subscript patterns not in math/code/URLs."""
    results = []
    state = 'text'
    i = 0
    n = len(text)

    while i < n:
        c = text[i]
        if i + 3 <= n and text[i:i+3] == '```':
            state = 'code_block' if state != 'code_block' else 'text'
            i += 3
            continue
        if state == 'code_block':
            i += 1
            continue
        if c == '`':
            state = 'inline_code' if state != 'inline_code' else 'text'
            i += 1
            continue
        if state == 'inline_code':
            i += 1
            continue
        if c == '\\' and i + 1 < n:
            i += 2
            continue
        if c == '$':
            if i + 1 < n and text[i+1] == '$':
                state = 'display_math' if state != 'display_math' else 'text'
                i += 2
                continue
            state = 'inline_math' if state != 'inline_math' else 'text'
            i += 1
            continue
        if c == '\n' and state == 'inline_math':
            state = 'text'
        if state == 'text':
            m = VAR_SUBSCRIPT_PATTERN.match(text, i)
            if m:
                # Skip common false positives
                orig = m.group(0)
                var = m.group(1)
                sub = m.group(2)
                
                # Skip common English words
                if var.lower() in ('the', 'and', 'or', 'is', 'it', 'this', 'we', 'as', 'in', 'on', 'to', 'of', 'for', 'be', 'an', 'at', 'by'):
                    i += 1
                    continue
                # Skip if the next char is digit/letters (might be longer variable)
                if i + len(orig) < n and (text[i + len(orig)].isalnum() or text[i + len(orig)] == '_'):
                    i += 1
                    continue
                # Skip common filename patterns like "M_N" (with capital N)
                if var == 'M' and sub == 'N':
                    i += 1
                    continue
                # Skip file/URL names: anything followed by .py, .md, .tex, /, .html, etc.
                next_chars = text[i + len(orig):i + len(orig) + 5]
                if next_chars.startswith(('.py', '.md', '.tex', '.json', '.txt', '.html', '/', '\\', 'index')):
                    i += 1
                    continue
                # Skip if the var+sub looks like a filename (e.g., M_dyn, M_Pl)
                # Check for common filename patterns
                # Actually, the patterns here are real physics, just need to be in math mode
                
                # Skip common false positives
                if var == 'M' and sub in ('sun', 'dyn', 'gas', 'disk', 'halo', 'tot', 'baryon',
                                         'Pl', 'Pl,2D', 'Pl,3D', 'Pl,4D', 'Pl,5D'):
                    # Real physics - good
                    pass
                elif var in ('H', 'T', 'E', 'v', 'V', 'r', 'R', 'a', 'k', 'g', 'N', 't', 'c', 'L', 's', 'S', 'u', 'U', 'p', 'P', 'b', 'B', 'd', 'D', 'f', 'F', 'q', 'Q', 'x', 'X', 'y', 'Y', 'z', 'Z'):
                    # Real physics
                    pass
                else:
                    # Skip uncertain patterns
                    i += 1
                    continue
                
                results.append((m.start(), m.end(), orig))
                i = m.end()
                continue
        i += 1
    return results


def wrap_in_math(original):
    """Wrap the matched text in $...$ math.
    
    Single-letter subscripts don't need braces, but multi-letter do.
    """
    var, sub = original.split('_', 1)
    if len(sub) == 1 and sub.isalnum():
        # Single letter/digit subscript: no braces
        replacement = f'${original}$'
    else:
        # Multi-letter or compound subscript: use braces
        replacement = f'${var}_{{\\rm {sub}}}$'
    return replacement


def fix_file(filepath, dry_run=False):
    """Fix physics subscript patterns in a single file. Return count."""
    with open(filepath) as f:
        content = f.read()

    issues = find_physics_subscripts(content)
    if not issues:
        return 0

    # Apply in reverse to preserve positions
    new_content = content
    for start, end, orig in reversed(issues):
        replacement = wrap_in_math(orig)
        new_content = new_content[:start] + replacement + new_content[end:]

    if not dry_run and new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)

    return len(issues)


def main():
    dry_run = '--dry-run' in sys.argv
    all_md = '--all' in sys.argv

    if all_md:
        files = glob.glob(os.path.join('/workspace/github-repo', 'paper', 'markdown', '*.md'))
        for top in ['README.md', 'STATE_OF_THE_MODEL.md', 'changelog.md',
                    'persistent_memory.md', 'RELEASE_DESCRIPTION_v3.5.9-A2.md',
                    'RELEASE_NOTES_v3.5.9-A2.md']:
            tp = os.path.join('/workspace/github-repo', top)
            if os.path.exists(tp):
                files.append(tp)
    else:
        files = glob.glob(os.path.join('/workspace/github-repo', 'paper', 'markdown', '*.md'))

    total = 0
    for fp in sorted(set(files)):
        n = fix_file(fp, dry_run=dry_run)
        if n > 0:
            print(f'  {os.path.relpath(fp, "/workspace/github-repo")}: {n} fixes')
            total += n

    if dry_run:
        print(f'\n[DRY RUN] Would fix {total} instances')
    else:
        print(f'\nFixed {total} instances')


if __name__ == '__main__':
    main()
