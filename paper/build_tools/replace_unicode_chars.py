#!/usr/bin/env python3
"""
Replace Unicode characters that don't work with DejaVu Serif font
in LaTeX/XeLaTeX processing.

This runs as part of the build pipeline to fix common Unicode issues:
- ✓ → \checkmark (in math mode) or just ✓ (preserved as text)
- → → \rightarrow
- × → \times
- ≈ → \approx
- ± → \pm
- · → \cdot
"""
import re
import sys

def replace_unicode(text):
    # Replace problematic Unicode characters with text equivalents
    # that DejaVu Serif handles
    replacements = {
        '✓': '[OK]',          # checkmark
        '✗': '[X]',           # cross mark
        '→': '->',            # arrow
        '⇒': '=>',            # implies
        '×': 'x',             # times (in text mode)
        '≈': '~=',            # approx
        '±': '+/-',           # plus-minus
        '·': '.',             # dot
        '—': '--',            # em-dash
        '–': '-',             # en-dash
        '…': '...',           # ellipsis
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: replace_unicode_chars.py <file.tex>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = replace_unicode(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Replaced Unicode chars in {filepath}")
