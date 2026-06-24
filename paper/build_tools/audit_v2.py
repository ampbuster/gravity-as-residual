#!/usr/bin/env python3
"""
Fast audit that pre-computes math mode state for the entire file.
"""
import os
import re
import sys
from collections import defaultdict

def get_all_files():
    files = []
    for root, dirs, fs in os.walk('markdown'):
        for f in fs:
            if f.endswith('.md'):
                files.append(os.path.join(root, f))
    for f in ['README.md', 'changelog.md', 'STATE_OF_THE_MODEL.md',
              'RELEASE_DESCRIPTION_v3.5.9-A2.md', 'RELEASE_NOTES_v3.5.9-A2.md',
              'ai_disclosure.md']:
        if os.path.exists(f):
            files.append(f)
    return files


def build_mode_map(text):
    """Build a bytearray where each position is marked as:
    0 = normal prose
    1 = inside $...$ (inline math)
    2 = inside $$...$$ (display math)
    3 = inside ```code```
    4 = inside `inline-code`
    """
    n = len(text)
    mode = bytearray(n)

    i = 0
    while i < n:
        # Code block ```
        if text[i:i+3] == '```':
            end = text.find('```', i+3)
            if end == -1:
                end = n
            else:
                end += 3
            for j in range(i, end):
                if j < n:
                    mode[j] = 3
            i = end
            continue
        # Display math $$
        if text[i:i+2] == '$$':
            end = text.find('$$', i+2)
            if end == -1:
                end = n
            else:
                end += 2
            for j in range(i, end):
                if j < n:
                    mode[j] = 2
            i = end
            continue
        # Inline math $ (but not escaped \$)
        if text[i] == '$' and (i == 0 or text[i-1] != '\\'):
            end = text.find('$', i+1)
            if end == -1:
                end = n
            else:
                end += 1
            for j in range(i, end):
                if j < n:
                    mode[j] = 1
            i = end
            continue
        # Inline code `
        if text[i] == '`':
            end = text.find('`', i+1)
            if end == -1:
                end = n
            else:
                end += 1
            for j in range(i, end):
                if j < n:
                    mode[j] = 4
            i = end
            continue
        i += 1

    return mode


# Math vars that should be in math mode
MATH_VARS = [
    r'\bM_Pl(?:,\dD|,\d\+1D|,\dD)?\b',
    r'\bM_(?:2D|3D|4D|dyn|stars|tot|halo)\b',
    r'\bN_(?:2D|3D|4D|3\+1D|sub|eff)\b',
    r'\b(?:rho|f|g|v|tau|alpha|gamma|epsilon|mu|nu|sigma|lambda|phi|psi|omega|tau|Z)_(?:DE|DM|leak|active|critical|back|pl|obs|Higgs|2D|3D|4D|3\+1D|SIDC|\+|dyn|stars|tot|halo|sub|eff|crit|cmb|obs|src|dest|targ|em|out|in|loc|ext|bnd|spec)\b',
    r'\bg_\+',
    r'\bg_\-',
    r'\bH_0\b',
]


def audit_math_vars(text, mode, filepath):
    issues = []
    for pattern in MATH_VARS:
        for m in re.finditer(pattern, text):
            pos = m.start()
            # Only flag if in normal prose (mode 0)
            if mode[pos] != 0:
                continue
            # Skip URL/filename contexts
            ctx_start = max(0, pos - 30)
            ctx_end = min(len(text), m.end() + 30)
            ctx = text[ctx_start:ctx_end]
            if any(skip in ctx for skip in ['.md', '.py', '.tex', 'http', 'github.com']):
                continue

            line_num = text[:pos].count('\n') + 1
            line_start = text.rfind('\n', 0, pos) + 1
            line_end = text.find('\n', pos)
            if line_end == -1:
                line_end = len(text)
            line = text[line_start:line_end][:120]
            issues.append((line_num, line, f"'{m.group(0)}' not in math mode"))
    return issues


POWER_PATTERNS = [
    (r'\b10\^[+\-]?\d+\b', 'plain 10^N'),
    (r'\b10[⁻⁺][⁰¹²³⁴⁵⁶⁷⁸⁹]+\b', 'unicode 10^N'),
    (r'(?<![a-zA-Z\d])\d+e[+\-]?\d+(?![a-zA-Z\d])', 'e-notation'),
]


def audit_powers(text, mode, filepath):
    issues = []
    for pattern, label in POWER_PATTERNS:
        for m in re.finditer(pattern, text):
            pos = m.start()
            if mode[pos] != 0:
                continue
            ctx_start = max(0, pos - 30)
            ctx_end = min(len(text), m.end() + 30)
            ctx = text[ctx_start:ctx_end]
            if any(skip in ctx for skip in ['.md', '.py', '.tex', 'http', 'github.com']):
                continue

            line_num = text[:pos].count('\n') + 1
            line_start = text.rfind('\n', 0, pos) + 1
            line_end = text.find('\n', pos)
            if line_end == -1:
                line_end = len(text)
            line = text[line_start:line_end][:120]
            issues.append((line_num, line, f"{label} '{m.group(0)}' not in math"))
    return issues


def audit_inconsistencies(all_content):
    issues = []
    param_patterns = {
        'M_Pl,4D_value': r'M[_\s]?Pl,?4D?\s*[=:≈]\s*(\d+(?:\.\d+)?(?:e[+\-]?\d+|\^?\{?[+\-]?\d+\}?)?)\s*(?:GeV)',
        'M_Pl,2D_value': r'M[_\s]?Pl,?2D?\s*[=:≈]\s*(\d+(?:\.\d+)?)\s*TeV',
        'rho_DE_value': r'(?:rho[_\s]?DE|\\rho_\{?DE\}?)\s*[=:≈]\s*(\d+(?:\.\d+)?e[+\-]?\d+)',
        'gamma_4D_value': r'gamma[_\s]?4D\s*[=:≈]\s*(\d+(?:\.\d+)?e[+\-]?\d+)',
    }

    for param, pattern in param_patterns.items():
        seen = defaultdict(list)
        for filepath, content in all_content.items():
            for m in re.finditer(pattern, content):
                value = m.group(1)
                line_num = content[:m.start()].count('\n') + 1
                seen[value].append((filepath, line_num))

        if len(seen) > 1:
            issues.append((param, dict(seen)))

    return issues


def main():
    files = get_all_files()
    total_issues = 0
    all_content = {}

    print("=" * 70)
    print("MATH AUDIT (fast version)")
    print("=" * 70)

    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                content = fh.read()
        except Exception:
            continue

        all_content[f] = content
        mode = build_mode_map(content)

        issues = audit_math_vars(content, mode, f) + audit_powers(content, mode, f)

        # Dedup by line
        seen = {}
        for ln, line, msg in issues:
            seen[(ln, msg[:30])] = (ln, line, msg)

        if seen:
            print(f"\n=== {f} ({len(seen)} issues) ===")
            for ln, line, msg in list(seen.values())[:10]:
                print(f"  L{ln}: {msg}")
                print(f"    > {line}")
            if len(seen) > 10:
                print(f"  ... and {len(seen) - 10} more")
            total_issues += len(seen)

    print(f"\n=== CROSS-FILE INCONSISTENCIES ===")
    inconsistencies = audit_inconsistencies(all_content)
    for param, seen in inconsistencies:
        print(f"\n{param}:")
        for value, occurrences in sorted(seen.items()):
            for filepath, line_num in occurrences[:2]:
                rel = filepath.replace('paper/', '')
                print(f"  '{value}' in {rel}:L{line_num}")

    print(f"\n=== TOTAL: {total_issues} issues ===")
    return total_issues


if __name__ == '__main__':
    sys.exit(main())
