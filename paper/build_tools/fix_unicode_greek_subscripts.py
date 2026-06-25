#!/usr/bin/env python3
"""
fix_unicode_greek_subscripts.py — Wrap Unicode Greek+subscript patterns in $...$ math.

Problem: Plain text like `ρ_DE/ρ_Pl = 10⁻¹²³` or `Ω_c = 0.265` is not in math mode.
In LaTeX, `_` outside math mode is an error or renders as plain underscore.
The user wants these patterns to be wrapped in `$...$` for proper rendering.

Patterns handled:
  `ρ_DE`         → `$\rho_{\rm DE}$`
  `ρ_DE/ρ_Pl`   → `$\rho_{\rm DE}/\rho_{\rm Pl}$`
  `Ω_c`          → `$\Omega_c$` (or `$\Omega_{\rm c}$`)
  `Ω_c h²`       → `$\Omega_c h^2$` (or similar)
  `ρ_DE_obs`     → `$\rho_{\rm DE,obs}$`

Rules:
  - Only handles Greek Unicode letters: α-ω, Α-Ω (and some specific letters)
  - Only wraps patterns that contain `_` (subscript notation)
  - Skips patterns already in math mode (`$...$`)
  - Skips code blocks (```...```) and inline code (`...`)
  - Converts to LaTeX: Unicode → \\greek, `_X` → `_{X}` or `_{\\rm X}`

Usage:
  python3 fix_unicode_greek_subscripts.py [file_or_dir]
  python3 fix_unicode_greek_subscripts.py           # process all paper/markdown/*.md
  python3 fix_unicode_greek_subscripts.py --all     # also fix README, etc.
  python3 fix_unicode_greek_subscripts.py --dry-run # show what would change
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

# Combined regex: match a Greek letter + optional subscripts (one or more)
# Subscript: underscore followed by alphanumeric/word chars, or comma-separated
# Greek letter: from the map
# Subscript can be:
#   - Letter first: _DE, _D, _c, _sub, _Pl
#   - Digit first: _2D, _4D, _3+1D (alpha_2D, alpha_4D, alpha_3+1D etc.)
#   - Mixed: _D2, _2Dx
GREEK_RE = '|'.join(re.escape(g) for g in sorted(GREEK_TO_LATEX.keys(), key=len, reverse=True))
# Subscript pattern: underscore + alpha or digit-prefixed word
# Allows: _DE, _2D, _3+1D, _4D, _D2, _Pl,3D, _2D,peak, _2D,2D
SUBSCRIPT_RE = r'_([A-Za-z0-9]+(?:\+[0-9]+[A-Za-z]*)?(?:[,.][A-Za-z0-9]+)*)'
GREEK_SUBSCRIPT_PATTERN = re.compile(
    r'(?<![\\$`])('
    + GREEK_RE
    + r')(?:' + SUBSCRIPT_RE + r')+'
)


def greek_to_latex_with_subscripts(full):
    """Convert Unicode Greek+subscript to LaTeX math.

    Accepts operators between Greek+subscript sequences, e.g.
    'ρ_DE/ρ_Pl' -> '$\\rho_{\\rm DE}/\\rho_{\\rm Pl}$'
    """
    # Replace each Greek letter with its LaTeX form, and _X with _{X}
    result = ''
    i = 0
    while i < len(full):
        ch = full[i]
        if ch in GREEK_TO_LATEX:
            result += GREEK_TO_LATEX[ch]
        elif ch == '_':
            # Find the subscript
            j = i + 1
            sub = ''
            while j < len(full) and (full[j].isalnum() or full[j] == ',' or full[j] == '_'):
                sub += full[j]
                j += 1
            if sub:
                # Use \rm for letter subscripts (avoids italic)
                if sub[0].isalpha():
                    result += r'_{\rm ' + sub + r'}'
                else:
                    result += r'_{' + sub + r'}'
                i = j
                continue
        else:
            result += ch
        i += 1
    return '$' + result + '$'


def find_unicode_greek_subscripts(text):
    """Find all Unicode Greek+subscript patterns not in math/code.

    Allows operators (+, -, /, =, x, *, spaces) between Greek+subscript
    sequences, so 'ρ_DE/ρ_Pl' is caught as a single math expression.
    """
    results = []
    state = 'text'  # 'text', 'inline_math', 'display_math', 'inline_code', 'code_block'
    i = 0
    n = len(text)

    # Combined pattern: a sequence of (Greek+subscripts) separated by operators
    # Operators allowed: +, -, /, =, x, *, (, ), ^, ~, and spaces
    OPERATOR = r'(?:\s*[\+\-/\*=\^~×x\(\)\s]\s*)+'
    # Full expression: (Greek+subscript)(OPERATOR(Greek+subscript))*
    # But we want the whole expression including operators
    COMBINED_PATTERN = re.compile(
        GREEK_SUBSCRIPT_PATTERN.pattern + r'(?:' + OPERATOR + GREEK_SUBSCRIPT_PATTERN.pattern + r')*'
    )

    while i < n:
        c = text[i]
        # Code block
        if i + 3 <= n and text[i:i+3] == '```':
            state = 'code_block' if state != 'code_block' else 'text'
            i += 3
            continue
        if state == 'code_block':
            i += 1
            continue
        # Inline code
        if c == '`':
            state = 'inline_code' if state != 'inline_code' else 'text'
            i += 1
            continue
        if state == 'inline_code':
            i += 1
            continue
        # Escape
        if c == '\\' and i + 1 < n:
            i += 2
            continue
        # Math
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
        # Newline resets inline_math
        if c == '\n' and state == 'inline_math':
            state = 'text'
        if state == 'text':
            # Try to match Greek+subscript (with optional operators)
            m = COMBINED_PATTERN.match(text, i)
            if m and m.end() > m.start():
                # Skip if the match is just whitespace or single Greek
                if len(m.group(0).strip()) > 1:
                    results.append((m.start(), m.end(), m.group(0)))
                i = m.end()
                continue
        i += 1
    return results


def fix_file(filepath, dry_run=False):
    """Fix Unicode Greek+subscript patterns in a single file. Return count."""
    with open(filepath) as f:
        content = f.read()

    issues = find_unicode_greek_subscripts(content)
    if not issues:
        return 0

    # Apply in reverse
    new_content = content
    for start, end, orig in reversed(issues):
        replacement = greek_to_latex_with_subscripts(orig)
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
