#!/usr/bin/env python3
"""
Comprehensive inline notation fixer for SIDC paper markdown files.

This script fixes inline math notation patterns that need proper LaTeX
formatting. It consolidates fixes from 21+ passes of notation cleanup.

CATEGORIES (run in order, idempotent):
  A. Parenthesized ratio formulas (E_ND/M_Pl,ND)^α
  B. Bare subscript LaTeX fixes (E_{ND} → E_{\rm ND})
  C. Unicode superscript fixes (M_Pl⁴ → $M_{\rm Pl}^4$)
  D. Inline equations (X_sub = value)
  E. γ/τ inline notation in descriptive text
  F. Specific inline equation patterns
  G. Special broken delimiter fixes (4.$4)

USAGE:
  python3 fix_notation.py <file.md> [file2.md ...]
  python3 fix_notation.py paper/markdown/*.md README.md

The script is IDEMPOTENT - running it multiple times produces the same output.
"""
import re
import sys


def fix_pass_a_parenthesized_ratios(text):
    """
    Pass A: Convert bare (X_Y/X_Z)^α to proper LaTeX math.

    Examples:
      (E_3D/M_Pl,3D)^α → $(E_{3D}/M_{\rm Pl,3D})^{\alpha}$
      (E_4D/M_Pl,3D)^α → $(E_{4D}/M_{\rm Pl,3D})^{\alpha}$
      (E_parent/M_Pl,child)^α → $(E_{\rm parent}/M_{\rm Pl,child})^{\alpha}$
      (E/M_Pl,parent)^α → $(E/M_{\rm Pl,parent})^{\alpha}$
    """
    changes = 0

    # Pattern 1: (E_ND/M_Pl,ND)^α
    pattern1 = r'\(E_(\d)D/M_Pl,(\d)D\)\^α'
    text, n = re.subn(pattern1,
        lambda m: f'$(E_{{{m.group(1).strip()}D}}/M_{{\\rm Pl,{m.group(2).strip()}D}})^{{\\alpha}}$',
        text)
    changes += n

    # Pattern 2: (E_word/M_Pl,word)^α
    pattern2 = r'\(E_([a-zA-Z]+)/M_Pl,([a-zA-Z]+)\)\^α'
    text, n = re.subn(pattern2,
        lambda m: f'$(E_{{\\rm {m.group(1).strip()}}}/M_{{\\rm Pl,{m.group(2).strip()}}})^{{\\alpha}}$',
        text)
    changes += n

    # Pattern 3: (E/M_Pl,parent)^α (E without subscript)
    pattern3 = r'\(E/M_Pl,([a-zA-Z]+)\)\^α'
    text, n = re.subn(pattern3,
        lambda m: f'$(E/M_{{\\rm Pl,{m.group(1).strip()}}})^{{\\alpha}}$',
        text)
    changes += n

    return text, changes


def fix_pass_b_missing_rm(text):
    """
    Pass B: Fix bare {X}_{Y} or X_{Y} where \\rm is missing.

    Examples:
      E_{4D} → E_{\rm 4D}
      E_{3D} → E_{\rm 3D}
      M_{Pl,N} → M_{\rm Pl,N}
    """
    changes = 0

    # Pattern: E_{ND} → E_{\rm ND} (only if not already \rm)
    pattern1 = r'E_\{(\d)D\}(?!\\rm)'
    text, n = re.subn(pattern1,
        lambda m: f'E_{{\\rm {m.group(1).strip()}D}}', text)
    changes += n

    # Pattern: M_{Pl,N} → M_{\rm Pl,N}
    pattern2 = r'M_\{Pl,(\dD)\}(?!\\rm)'
    text, n = re.subn(pattern2,
        lambda m: f'M_{{\\rm Pl,{m.group(1).strip()}}}', text)
    changes += n

    return text, changes


def fix_pass_c_unicode_superscripts(text):
    """
    Pass C: Replace Unicode superscripts in inline notation.

    Examples:
      M_Pl⁴ → $M_{\rm Pl}^4$
      M_Pl² → $M_{\rm Pl}^2$
      M_Pl³ → $M_{\rm Pl}^3$
    """
    changes = 0

    unicode_to_latex = {
        '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
        '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
    }

    for unicode_exp, latex_exp in unicode_to_latex.items():
        old = f'M_Pl{unicode_exp}'
        new = f'$M_{{\\rm Pl}}^{{{latex_exp}}}$'
        count = text.count(old)
        if count > 0:
            text = text.replace(old, new)
            changes += count

    return text, changes


def fix_pass_d_inline_equations(text):
    """
    Pass D: Wrap inline equations in $..$ delimiters.

    Examples:
      N_sub = 386 → $N_{\rm sub} = 386$
      E_4D = 5×10⁷⁹ J → $E_{\rm 4D} = 5×10⁷⁹$ J
      E_sub = 1.3×10⁷⁷ J → $E_{\rm sub} = 1.3×10⁷⁷$ J
      M_Pl,N = X GeV → $M_{\rm Pl,N} = X$ GeV
      τ_4D = 1.51×10³⁴ yr → $\tau_{\rm 4D} = 1.51×10³⁴$ yr
    """
    changes = 0

    # Value pattern: numbers with optional units/exponents
    value_pattern = r'(\d[\d\.×10⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺eE\s\*\+JGeVyr·^\(\)/]*)'

    patterns = [
        # N_sub = ...
        (r'(?<!\$)\bN_sub\s*=\s*' + value_pattern,
         lambda m: f'$N_{{\\rm sub}} = {m.group(1).strip()}$'),
        # E_sub = ...
        (r'(?<!\$)\bE_sub\s*=\s*' + value_pattern,
         lambda m: f'$E_{{\\rm sub}} = {m.group(1).strip()}$'),
        # E_4D = ...
        (r'(?<!\$)\bE_4D\s*=\s*' + value_pattern,
         lambda m: f'$E_{{\\rm 4D}} = {m.group(1).strip()}$'),
        # M_Pl,N = ...
        (r'(?<!\$)\bM_Pl,(\dD)\s*=\s*' + value_pattern,
         lambda m: f'$M_{{\\rm Pl,{m.group(1).strip()}}} = {m.group(2).strip()}$'),
        # τ_4D = ...
        (r'(?<!\$)\bτ_4D\s*=\s*' + value_pattern,
         lambda m: f'$\\tau_{{\\rm 4D}} = {m.group(1).strip()}$'),
    ]

    for pattern, replacement_func in patterns:
        new_text, n = re.subn(pattern, replacement_func, text)
        if n > 0:
            changes += n
            text = new_text

    return text, changes


def fix_pass_e_greek_inline(text):
    """
    Pass E: Fix γ/τ inline notation in descriptive text.

    Examples:
      γ_2D = 5.5e44 → $\gamma_{\rm 2D} = 5.5e44$
      γ_4D = 5.93e90 → $\gamma_{\rm 4D} = 5.93e90$
      τ_2D, τ_4D, τ_DM → $\tau_{\rm 2D}$, etc.

    CONSERVATIVE: only matches when followed by = and a value with units/space.
    """
    changes = 0

    # γ_ND = <value> where value ends with non-numeric character
    # This ensures we don't break "5.5e44" into "5" then ".5e44"
    # We require the value to end with: , . ) } space | letter (J, GeV, yr, s)
    pattern1 = r'(?<![\\$a-zA-Z_\\])γ_(\dD)\s*=\s*(\d[\d\.×10⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺eE]*)(?=[,\s\.\)\}\|\w])'
    text, n = re.subn(pattern1,
        lambda m: f'$\\gamma_{{\\rm {m.group(1).strip()}}} = {m.group(2).strip()}$',
        text)
    changes += n

    # τ_X = <value> (τ with subscript)
    pattern2 = r'(?<![\\$a-zA-Z_\\])τ_([a-zA-Z0-9,]+)\s*=\s*(\d[\d\.×10⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺eE]*)(?=[,\s\.\)\}\|\w])'
    text, n = re.subn(pattern2,
        lambda m: f'$\\tau_{{\\rm {m.group(1).strip()}}} = {m.group(2).strip()}$',
        text)
    changes += n

    return text, changes


def fix_pass_f_specific_inline(text):
    """
    Pass F: Specific inline equation patterns that came up in manual cleanup.

    CONSERVATIVE: only matches when the surrounding context is clearly math.
    """
    changes = 0

    # γ_4D = $(E_4D/M_Pl,3D)^α = 5.93e90 (already partially in math)
    pattern1 = r'(?<![\\$a-zA-Z_])γ_4D\s*=\s*\$(.+?)\$\^\{?α\}?\s*=\s*(\d[\d\.eExX×10⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]*)(?=[,\s\.\)\}])'
    text, n = re.subn(pattern1,
        lambda m: f'$\\gamma_{{\\rm 4D}} = ({m.group(1).strip()})^{{\\alpha}} = {m.group(2).strip()}$',
        text)
    changes += n

    # γ_2D = $(E_3D/M_Pl,3D)^α = 5.5e44
    pattern2 = r'(?<![\\$a-zA-Z_])γ_2D\s*=\s*\$(.+?)\$\^\{?α\}?\s*=\s*(\d[\d\.eExX×10⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]*)(?=[,\s\.\)\}])'
    text, n = re.subn(pattern2,
        lambda m: f'$\\gamma_{{\\rm 2D}} = ({m.group(1).strip()})^{{\\alpha}} = {m.group(2).strip()}$',
        text)
    changes += n

    return text, changes


def fix_pass_g_special_broken(text):
    """
    Pass G: Fix special broken math delimiter patterns.

    Examples:
      4.$4 × 10²³ → $4.4 × 10²³ (period followed by $)
    """
    changes = 0

    # Pattern: digit.$digit (broken delimiter)
    pattern = r'(\d)\.\$(\d)'
    text, n = re.subn(pattern, lambda m: f'${m.group(1).strip()}.{m.group(2).strip()}', text)
    changes += n

    return text, changes


def fix_all(text):
    """Run all notation fixes in order."""
    total = 0

    for pass_func in [
        fix_pass_a_parenthesized_ratios,
        fix_pass_b_missing_rm,
        fix_pass_c_unicode_superscripts,
        fix_pass_d_inline_equations,
        fix_pass_e_greek_inline,
        fix_pass_f_specific_inline,
        fix_pass_g_special_broken,
    ]:
        text, n = pass_func(text)
        total += n

    return text, total


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: fix_notation.py <file.md> [file2.md ...]")
        print("")
        print("Categories of fixes (run in order, idempotent):")
        print("  A. (E_ND/M_Pl,ND)^α formulas → $(...)^{α}$")
        print("  B. E_{ND} / M_{Pl,N} missing \\rm → E_{\\rm ND}")
        print("  C. Unicode superscripts (M_Pl⁴) → $M_{\\rm Pl}^4$")
        print("  D. Inline equations (N_sub = X, E_4D = X, τ_4D = X)")
        print("  E. γ/τ inline notation in descriptive text")
        print("  F. Specific inline equation patterns")
        print("  G. Special broken delimiter fixes (4.$4)")
        sys.exit(1)

    total_changes = 0
    files_changed = 0
    for filepath in sys.argv[1:]:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, changes = fix_all(content)

        if changes > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"{filepath}: {changes} substitutions")
            total_changes += changes
            files_changed += 1
        else:
            print(f"{filepath}: no changes")

    print(f"\nTotal: {total_changes} substitutions across {files_changed} files")
