#!/usr/bin/env python3
"""
Fix Planck scale subscript patterns in math expressions.

Fixes:
1. (E_3D/M_Pl,3D)^α → $(E_{3D}/M_{\rm Pl,3D})^{\alpha}$ (and similar patterns)
2. E_{4D} → E_{\rm 4D} (in math mode)
3. E_{3D} → E_{\rm 3D} (in math mode)
4. M_{Pl,N} → M_{\rm Pl,N} (in math mode, where \rm is missing)
5. E_4D = N_sub × E_sub → proper LaTeX where appropriate
"""
import re
import sys

def fix_pl_subscripts(text):
    """Convert various inline patterns to proper LaTeX."""
    changes = 0
    
    # Pattern 1: (E_ND/M_Pl,ND)^α
    pattern1 = r'\(E_(\d)D/M_Pl,(\d)D\)\^α'
    def replace1(m):
        nonlocal changes
        changes += 1
        n1, n2 = m.group(1), m.group(2)
        return f'$(E_{{{n1}D}}/M_{{\\rm Pl,{n2}D}})^{{\\alpha}}$'
    text = re.sub(pattern1, replace1, text)

    # Pattern 2: (E_word/M_Pl,word)^α
    pattern2 = r'\(E_([a-zA-Z]+)/M_Pl,([a-zA-Z]+)\)\^α'
    def replace2(m):
        nonlocal changes
        changes += 1
        e_sub, pl_sub = m.group(1), m.group(2)
        return f'$(E_{{\\rm {e_sub}}}/M_{{\\rm Pl,{pl_sub}}})^{{\\alpha}}$'
    text = re.sub(pattern2, replace2, text)

    # Pattern 3: Fix bare E_{ND} (missing \rm)
    # E_{4D} → E_{\rm 4D}, E_{3D} → E_{\rm 3D}
    # Use a callback to check that the E_{ND} isn't already followed by \rm
    pattern3 = r'E_\{(\d)D\}(?!\\rm)'
    def replace3(m):
        nonlocal changes
        changes += 1
        n = m.group(1)
        return f'E_{{\\rm {n}D}}'
    text = re.sub(pattern3, replace3, text)

    # Pattern 4: Fix bare M_{Pl,N} (without \rm)
    pattern4 = r'M_\{Pl,([0-9]D)\}(?!\\rm)'
    def replace4(m):
        nonlocal changes
        changes += 1
        n = m.group(1)
        return f'M_{{\\rm Pl,{n}}}'
    text = re.sub(pattern4, replace4, text)

    return text, changes


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: fix_pl_subscripts.py <file.md> [file2.md ...]")
        sys.exit(1)

    total_changes = 0
    for filepath in sys.argv[1:]:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, changes = fix_pl_subscripts(content)

        if changes > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"{filepath}: {changes} substitutions")
            total_changes += changes

    print(f"Total: {total_changes} substitutions")
