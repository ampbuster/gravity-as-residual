#!/usr/bin/env python3
"""
Fix broken markdown patterns involving math delimiters.
"""
import os
import re
import sys


def parse_unicode_superscript(text):
    """Convert 10⁻⁴⁵ to 10^{-45}"""
    if not text.startswith('10'):
        return None
    sign = ''
    digits = ''
    sup_map = {"⁰":"0","¹":"1","²":"2","³":"3","⁴":"4","⁵":"5","⁶":"6","⁷":"7","⁸":"8","⁹":"9"}
    for c in text[2:]:
        if c == '⁻':
            sign = '-'
        elif c == '⁺':
            sign = '+'
        elif c in sup_map:
            digits += sup_map[c]
        else:
            return None
    return f'$10^{{{sign}{digits}}}$' if digits else None


def fix_broken_markdown(content):
    """Fix common broken markdown patterns."""
    changes = 0

    # Pattern 1: ** $ (bold followed by space and math)
    new_content, n = re.subn(r'\*\* \$', '**$', content)
    changes += n
    content = new_content

    # Pattern 2: ( $ (open paren followed by space and math)
    new_content, n = re.subn(r'\( \$', '($', content)
    changes += n
    content = new_content

    # Pattern 3: [ $ (open bracket, less common)
    new_content, n = re.subn(r'\[ \$', '[$', content)
    changes += n
    content = new_content

    # Pattern 4: - $ or * $ (list item + space + math)
    new_content, n = re.subn(r'^([-*])\s+\$', r'\1 $', content, flags=re.MULTILINE)
    changes += n
    content = new_content

    # Pattern 5: $X\times$ 10^{N} (split math block)
    new_content, n = re.subn(
        r'(\$[\d. ]+\\times\$)\s+(10\^[\d\-\{\}\]]+)',
        lambda m: f'{m.group(1)[:-1]} {m.group(2)}$',
        content
    )
    changes += n
    content = new_content

    # Pattern 6: **NUMBER × 10^N** (bold with Unicode superscript)
    new_content, n = re.subn(
        r'\*\*([0-9.]+)\s*×\s*(10[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)\*\*',
        lambda m: f'**${m.group(1)} \\times {parse_unicode_superscript(m.group(2))[1:-1]}$**',
        content
    )
    changes += n
    content = new_content

    # Pattern 7: **10⁻N suffix** (bold with Unicode 10^N and trailing text)
    new_content, n = re.subn(
        r'\*\*(10[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)([^*]*)\*\*',
        lambda m: f'**{parse_unicode_superscript(m.group(1))}{m.group(2)}**',
        content
    )
    changes += n
    content = new_content

    # Pattern 8: $\Omega$DM → $\Omega_{\rm DM}$
    new_content, n = re.subn(r'\$\\Omega\$DM', r'$\\Omega_{\\rm DM}$', content)
    changes += n
    content = new_content

    # Pattern 9: $$$...$ → $$...$$ (triple dollar → display math)
    new_content, n = re.subn(r'\$\$\$([^$]+)\$', r'$$\1$$', content)
    changes += n
    content = new_content

    # Pattern 10: $\Lambda$CDM → $\Lambda{\rm CDM}$
    new_content, n = re.subn(r'\$\\Lambda\$CDM', r'$\\Lambda{\\rm CDM}$', content)
    changes += n
    content = new_content

    # Pattern 11b: $X/$Y $Z$ → $X/Y \sim Z$ (chain case)
    new_content, n = re.subn(
        r'\$([^$/]+)/\$([^$]+)\s+\$([^$]+)\$',
        lambda m: f'${m.group(1)}/{m.group(2)} {m.group(3)}$' if m.group(3).startswith('\\\\') else f'${m.group(1)}/{m.group(2)} \\\\sim {m.group(3)}$',
        content
    )
    changes += n
    content = new_content

    # Pattern 11a: $X/$Y$ → $X/Y$ (simple case)
    new_content, n = re.subn(r'\$([^$/]+)/\$([^$]+)\$', r'$\1/\2$', content)
    changes += n
    content = new_content

    # Pattern 12: $X^{$Y^Z}$ → $X^{Y^Z}$ (nested math in superscript)
    new_content, n = re.subn(
        r'\$([^$]+)\^\{\$([^$]+)\^\{([^$]+)\}\s*\$\s*\}\$',
        r'$\1^{\2^{\3}}$',
        content
    )
    changes += n
    content = new_content

    # Pattern 13: X^$Y$ → $X^{Y}$ (sup symbol before math)
    new_content, n = re.subn(
        r'(\w)\^\$([^$]+)\$',
        lambda m: f'${m.group(1)}^{{{m.group(2)}}}$',
        content
    )
    changes += n
    content = new_content

    # Pattern 14: \times $X$ → \times X$
    new_content, n = re.subn(r'\\times\s+\$([^$]+)\$', r'\\times \1', content)
    changes += n
    content = new_content

    # Pattern 15: \sim $X$ → \sim X$
    new_content, n = re.subn(r'\\sim\s+\$([^$]+)\$', r'\\sim \1', content)
    changes += n
    content = new_content

    return content, changes


def process_file(filepath):
    """Fix broken markdown patterns in a single file."""
    with open(filepath, 'r') as f:
        content = f.read()
    new_content, changes = fix_broken_markdown(content)
    if changes > 0:
        with open(filepath, 'w') as f:
            f.write(new_content)
    return changes


def main():
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isfile(target):
            n = process_file(target)
            print(f"{target}: {n} substitutions")
            return
        elif os.path.isdir(target):
            total = 0
            for f in sorted(os.listdir(target)):
                if f.endswith('.md'):
                    path = os.path.join(target, f)
                    n = process_file(path)
                    if n > 0:
                        print(f"  {f}: {n}")
                        total += n
            print(f"Total: {total} substitutions")
            return

    targets = []
    if os.path.isdir('paper/markdown'):
        targets.extend([os.path.join('paper/markdown', f) for f in sorted(os.listdir('paper/markdown')) if f.endswith('.md')])
    if os.path.isdir('supporting'):
        targets.extend([os.path.join('supporting', f) for f in sorted(os.listdir('supporting')) if f.endswith('.md')])
    for fname in ['README.md', 'changelog.md', 'persistent_memory.md',
                  'layman_summary.md', 'how-did-we-get-here.md',
                  'arxiv_submission.md', 'STATE_OF_THE_MODEL.md']:
        if os.path.isfile(fname):
            targets.append(fname)

    total = 0
    for path in targets:
        n = process_file(path)
        if n > 0:
            print(f"  {path}: {n}")
            total += n
    print(f"Total: {total} substitutions")


if __name__ == '__main__':
    main()
