#!/usr/bin/env python3
"""
fix_unicode_times_powers.py — Wrap plain text 'number × 10^N [unit]' in $...$ math.

Problem: Plain text like '3.93×10²³ GeV' or '1.79×10⁻⁹⁰' is not in math mode.
The Unicode × (U+00D7) and Unicode superscript digits (⁰¹²³⁴⁵⁶⁷⁸⁹) don't
render correctly in plain text outside LaTeX math mode.

Examples:
  '$f_{\\rm DE,closed}$ = 1.79×10⁻⁹⁰'  → '$f_{\\rm DE,closed} = 1.79 \\times 10^{-90}$'
  '$\\rho_{\\rm DE}$ = 2.5×10⁻⁴⁷ GeV⁴' → '$\\rho_{\\rm DE} = 2.5 \\times 10^{-47}\\,\\text{GeV}^4$'
  '5.7×10³⁸ yr' (in plain text) → '$5.7 \\times 10^{38}$ yr'

Patterns handled:
  - X.XX×10ⁿ, X.XX× 10ⁿ, X.XX × 10ⁿ, X.XX x 10ⁿ (with various spacing)
  - X.XX×10ⁿ [unit], where unit can be GeV, J, yr, Hz, etc.
  - Unit with superscript (GeV⁴, cm²) → \\text{unit}^N

Rules:
  - Skips code blocks (```...```) and inline code (`...`)
  - Skips existing math mode ($...$)
  - Converts × to \\times
  - Converts 10ⁿ to 10^{n}
  - Converts unit GeV⁴ to \\text{GeV}^4
  - Preserves spacing around unit (yr, J, etc. stay in text)

Usage:
  python3 fix_unicode_times_powers.py [file_or_dir]
  python3 fix_unicode_times_powers.py           # process all paper/markdown/*.md
  python3 fix_unicode_times_powers.py --all     # also fix README, etc.
  python3 fix_unicode_times_powers.py --dry-run # show what would change
"""
import re
import os
import sys
import glob

# Unicode superscript → ASCII
SUPER_MAP = {
    '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
    '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
    '⁻': '-', '⁺': '+',
}

# Common physics units
COMMON_UNITS = ('GeV', 'MeV', 'TeV', 'keV', 'eV', 'J', 'kg', 'm', 'cm',
                'km', 'Mpc', 'kpc', 'pc', 'ly', 'yr', 'Myr', 'Gyr', 's',
                'Hz', 'kHz', 'MHz', 'GHz', 'erg', 'W', 'K', 'm/s')

# Pattern: number [×/x] 10[Unicode_superscript] [unit_with_optional_caret]
PATTERN = re.compile(
    r'(\d+\.?\d*)\s*[×x]\s*10([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)\s*'
    r'(?P<unit>[A-Za-z]+(?:[\^][⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺])?)?'
)


def convert_to_math(match):
    """Convert a match to LaTeX math."""
    num = match.group(1)
    superscript = match.group(2)
    unit = match.group('unit')
    ascii_super = ''.join(SUPER_MAP.get(c, c) for c in superscript)
    result = f'${num} \\times 10^{{{ascii_super}}}'
    if unit:
        unit_match = re.match(r'([A-Za-z]+)\^([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)', unit)
        if unit_match:
            unit_name = unit_match.group(1)
            unit_exp = ''.join(SUPER_MAP.get(c, c) for c in unit_match.group(2))
            result += f'\\,\\text{{{unit_name}}}^{{{unit_exp}}}'
        else:
            # Only wrap in \text if it's a known unit
            if unit in COMMON_UNITS or any(unit.startswith(u) for u in COMMON_UNITS):
                result += f'\\,\\text{{{unit}}}'
            else:
                result += f'\\,{unit}'
    result += '$'
    return result


def is_in_math_mode(content, idx):
    """Check if position idx is inside $...$ math mode."""
    before = content[:idx]
    n = 0
    i = 0
    while i < len(before):
        if before[i] == '\\' and i + 1 < len(before):
            i += 2
            continue
        if before[i] == '$':
            n += 1
        i += 1
    return n % 2 == 1


def is_in_code_block(content, idx):
    """Check if position idx is inside a ```...``` code block."""
    fences = 0
    i = 0
    while i < idx - 2:
        if content[i:i+3] == '```':
            fences += 1
            i += 3
        else:
            i += 1
    return fences % 2 == 1


def convert_inside_math(match):
    """Convert a match to LaTeX math (no surrounding $ since already in math)."""
    num = match.group(1)
    superscript = match.group(2)
    unit = match.group('unit')
    ascii_super = ''.join(SUPER_MAP.get(c, c) for c in superscript)
    result = f'{num} \\times 10^{{{ascii_super}}}'
    if unit:
        unit_match = re.match(r'([A-Za-z]+)\^([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)', unit)
        if unit_match:
            unit_name = unit_match.group(1)
            unit_exp = ''.join(SUPER_MAP.get(c, c) for c in unit_match.group(2))
            result += f'\\,\\text{{{unit_name}}}^{{{unit_exp}}}'
        else:
            if unit in COMMON_UNITS or any(unit.startswith(u) for u in COMMON_UNITS):
                result += f'\\,\\text{{{unit}}}'
            else:
                result += f'\\,{unit}'
    return result


def fix_file(filepath, dry_run=False):
    """Fix ×10ⁿ patterns in a single file."""
    with open(filepath) as f:
        content = f.read()

    matches = list(PATTERN.finditer(content))
    if not matches:
        return 0

    new_content = content
    n_changes = 0
    for m in reversed(matches):
        idx = m.start()
        if is_in_code_block(content, idx):
            continue
        if is_in_math_mode(content, idx):
            # Inside math: convert in place (no $...$ wrapping)
            replacement = convert_inside_math(m)
        else:
            # Outside math: wrap in $...$
            replacement = convert_to_math(m)
        new_content = new_content[:m.start()] + replacement + new_content[m.end():]
        n_changes += 1

    if not dry_run and new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)

    return n_changes


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