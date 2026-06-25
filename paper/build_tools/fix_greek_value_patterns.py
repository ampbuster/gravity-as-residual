#!/usr/bin/env python3
"""
fix_greek_value_patterns.py — Wrap standalone Greek letters followed by = <value> in $...$.

Catches patterns like:
  ε = 6.32×10⁻³⁴        →  $\epsilon = 6.32\times 10^{-34}$
  ε = 1×10⁻³⁸           →  $\epsilon = 1\times 10^{-38}$
  ε = 6.32 × 10⁻³⁴      →  same
  ρ_DE = 2.5×10⁻⁴⁷ GeV⁴ →  $\rho_{\rm DE} = 2.5\times 10^{-47}\text{ GeV}^4$

Patterns handled:
  - ε, γ, τ, ρ, α, β, μ, σ, Ω, ω, δ, η, ν, λ, φ, π, χ, θ
  - Optional _subscript before =
  - = followed by number, ×, 10, Unicode superscript, unit

Rules:
  - Skips code blocks (```...```) and inline code (`...`)
  - Skips existing math mode ($...$)
  - Converts Unicode Greek to LaTeX
  - Converts × to \times
  - Converts 10ⁿ to 10^{n}
  - Converts GeV⁴ to \text{ GeV}^4

Usage:
  python3 fix_greek_value_patterns.py [file_or_dir]
  python3 fix_greek_value_patterns.py           # process all paper/markdown/*.md
  python3 fix_greek_value_patterns.py --all     # also fix README, etc.
  python3 fix_greek_value_patterns.py --dry-run # show what would change
"""
import re
import os
import sys
import glob

# Greek letter Unicode → LaTeX mapping
GREEK_TO_LATEX = {
    'α': r'\alpha', 'β': r'\beta', 'γ': r'\gamma', 'δ': r'\delta',
    'ε': r'\epsilon', 'ζ': r'\zeta', 'η': r'\eta', 'θ': r'\theta',
    'ι': r'\iota', 'κ': r'\kappa', 'λ': r'\lambda', 'μ': r'\mu',
    'ν': r'\nu', 'ξ': r'\xi', 'π': r'\pi', 'ρ': r'\rho',
    'σ': r'\sigma', 'ς': r'\varsigma', 'τ': r'\tau', 'υ': r'\upsilon',
    'φ': r'\phi', 'χ': r'\chi', 'ψ': r'\psi', 'ω': r'\omega',
    'Α': r'A', 'Β': r'B', 'Γ': r'\Gamma', 'Δ': r'\Delta',
    'Ε': r'E', 'Ζ': r'Z', 'Η': r'H', 'Θ': r'\Theta',
    'Ι': r'I', 'Κ': r'K', 'Λ': r'\Lambda', 'Μ': r'M',
    'Ν': r'N', 'Ξ': r'\Xi', 'Π': r'\Pi', 'Ρ': r'R',
    'Σ': r'\Sigma', 'Τ': r'T', 'Υ': r'\Upsilon', 'Φ': r'\Phi',
    'Χ': r'X', 'Ψ': r'\Psi', 'Ω': r'\Omega',
}

# Unicode superscript → ASCII mapping
UNICODE_SUPERSCRIPT_TO_ASCII = {
    '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
    '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
    '⁻': '-', '⁺': '+',
}

GREEK_RE = '|'.join(re.escape(g) for g in sorted(GREEK_TO_LATEX.keys(), key=len, reverse=True))

# Pattern: Greek letter (with optional _subscript) followed by = and a value
# Value can be: number with decimal, ×, 10, Unicode superscript, optional unit
# Requires: value to be a complete number (decimal point AND/OR 10^N) - not just bare integer
GREEK_VALUE_PATTERN = re.compile(
    r'(?<![\\$`])(' + GREEK_RE + r')'
    r'(?:_([A-Za-z0-9]+(?:[,.][A-Za-z0-9]+)*))?'
    r'\s*=\s*'
    r'([\d.]+\s*×?\s*10[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+'
    r'|[\d]+\.\d+'
    r')'
    r'(?:\s*([A-Za-z]+(?:\^[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺])?))?'
)


def convert_to_latex(greek_letter, subscript, value, unit):
    """Convert a Greek=value pattern to LaTeX math."""
    # Greek letter
    result = GREEK_TO_LATEX[greek_letter]
    # Subscript
    if subscript:
        if subscript[0].isalpha():
            result += r'_{\rm ' + subscript + r'}'
        else:
            result += r'_{' + subscript + r'}'
    # =
    result += ' = '
    # Value
    # Replace × with \times, 10ⁿ with 10^{n}
    if '10' in value:
        m = re.match(r'([\d.]+)\s*×?\s*10([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)', value)
        if m:
            num = m.group(1)
            superscript = m.group(2)
            # Convert Unicode superscript to ASCII
            ascii_super = ''.join(UNICODE_SUPERSCRIPT_TO_ASCII.get(c, c) for c in superscript)
            result += f'{num} \\times 10^{{{ascii_super}}}'
        else:
            result += value.replace('×', r'\times')
    else:
        result += value.replace('×', r'\times')
    # Unit
    if unit:
        # Convert Unicode superscript in unit
        unit_converted = re.sub(r'\^([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)', lambda m: '^{' + ''.join(UNICODE_SUPERSCRIPT_TO_ASCII.get(c, c) for c in m.group(1)) + '}', unit)
        # If unit has ^N, separate
        if '^' in unit_converted:
            # e.g., GeV^4 → \text{ GeV}^4
            unit_part, _, exp_part = unit_converted.partition('^')
            exp_content = exp_part.strip('{}')
            result += f'\\text{{ {unit_part}}}^{{{exp_content}}}'
        else:
            result += f'\\text{{ {unit_converted}}}'
    return '$' + result + '$'


def find_greek_value_patterns(text):
    """Find all Greek=value patterns not in math/code."""
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
                if state == 'text':
                    state = 'display_math'
                elif state == 'display_math':
                    state = 'text'
                i += 2
                continue
            if state == 'text':
                state = 'inline_math'
            elif state == 'inline_math':
                state = 'text'
            i += 1
            continue
        if c == '\n' and state == 'inline_math':
            state = 'text'
        if state == 'text':
            m = GREEK_VALUE_PATTERN.match(text, i)
            if m:
                greek_letter = m.group(1)
                subscript = m.group(2)
                value = m.group(3)
                unit = m.group(4)
                # Only process if value starts with digit and ends with unit or just number
                if value and value[0].isdigit():
                    results.append((m.start(), m.end(), m.group(0), greek_letter, subscript, value, unit))
                i = m.end()
                continue
        i += 1
    return results


def fix_file(filepath, dry_run=False):
    """Fix Greek=value patterns in a single file."""
    with open(filepath) as f:
        content = f.read()
    
    issues = find_greek_value_patterns(content)
    if not issues:
        return 0
    
    new_content = content
    for start, end, orig, greek, sub, val, unit in reversed(issues):
        replacement = convert_to_latex(greek, sub, val, unit)
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