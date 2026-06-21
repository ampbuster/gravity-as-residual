#!/usr/bin/env python3
"""
Fix inline math notation patterns.
"""
import re
import sys

def fix_inline_eqn(text):
    """Wrap inline equations in $..$ delimiters."""
    changes = 0
    
    value_pattern = r'(\d[\d\.×10⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺eE\s\*\+JGeVyr·^\(\)/]*)'
    
    # Use functions instead of string templates to avoid \t \r escaping
    patterns = [
        # N_sub = ...
        (r'(?<!\$)\bN_sub\s*=\s*' + value_pattern,
         lambda m: f'$N_{{\\rm sub}} = {m.group(1)}$'),
        # E_sub = ...
        (r'(?<!\$)\bE_sub\s*=\s*' + value_pattern,
         lambda m: f'$E_{{\\rm sub}} = {m.group(1)}$'),
        # E_4D = ...
        (r'(?<!\$)\bE_4D\s*=\s*' + value_pattern,
         lambda m: f'$E_{{\\rm 4D}} = {m.group(1)}$'),
        # M_Pl,N = ...
        (r'(?<!\$)\bM_Pl,(\dD)\s*=\s*' + value_pattern,
         lambda m: f'$M_{{\\rm Pl,{m.group(1)}}} = {m.group(2)}$'),
        # τ_4D = ...
        (r'(?<!\$)\bτ_4D\s*=\s*' + value_pattern,
         lambda m: f'$\\tau_{{\\rm 4D}} = {m.group(1)}$'),
    ]
    
    for pattern, replacement_func in patterns:
        new_text, n = re.subn(pattern, replacement_func, text)
        if n > 0:
            changes += n
            text = new_text
    
    return text, changes


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: fix_pl_subscripts.py <file.md> [file2.md ...]")
        sys.exit(1)

    total_changes = 0
    for filepath in sys.argv[1:]:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, changes = fix_inline_eqn(content)

        if changes > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"{filepath}: {changes} substitutions")
            total_changes += changes

    print(f"Total: {total_changes} substitutions")
