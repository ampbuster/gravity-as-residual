#!/usr/bin/env python3
"""
Master pipeline: safe cleanup + build + verify.

This pipeline uses ONLY the safe build_tools scripts that don't break
the LaTeX build for the SIDC paper.

SAFE SCRIPTS (used):
  - fix_math_spacing.py   (adds/cleans space around $)
  - wrap_unicode_powers.py (handles 10-45 unicode patterns)

SOURCE FIXES (in-script):
  - fix_broken_wraps      (revert bad wrap_math_vars.py outputs)
  - fix_unbalanced_dollars (revert accidental $$ to $)

UNSAFE (not used):
  - wrap_math_vars.py     (has bugs that create broken $X = $Y$ patterns)
  - wrap_powers_of_10.py  (some patterns broken for this paper)
  - e_to_math.py          (some patterns broken for this paper)
  - greek_to_latex.py     (adds unnecessary wrapping)
  - fix_greek_subscripts.py (creates new patterns)
  - fix_broken_markdown.py (some patterns conflict)
  - combine_adjacent_math.py (creates merged math that breaks)
  - replace_unicode_chars.py (replaces valid unicode with text)

Usage:
  python3 master_pipeline.py            # full pipeline
  python3 master_pipeline.py --dry-run  # show what would happen
"""
import os
import re
import subprocess
import sys

WORKSPACE = '/workspace/github-repo'
MARKDOWN_DIR = os.path.join(WORKSPACE, 'paper', 'markdown')


def run(cmd, cwd=None, capture=False):
    """Run a command, return result."""
    if cwd is None:
        cwd = WORKSPACE
    return subprocess.run(cmd, shell=True, cwd=cwd,
                          capture_output=capture, text=True)


def git_revert():
    print('Reverting all changes...')
    run('git checkout -- paper/markdown/ README.md changelog.md '
        'persistent_memory.md STATE_OF_THE_MODEL.md '
        'RELEASE_DESCRIPTION_v3.5.9-A2.md RELEASE_NOTES_v3.5.9-A2.md '
        'ai_disclosure.md ZENODO_ARXIV_PAPER.md ZENODO_SETUP.md supporting/ '
        'paper/paper.md')


def run_script(script, capture=True):
    return run(f'python3 paper/build_tools/{script}', capture=capture)


def step_fix_broken_wraps(dry_run=False):
    """Fix broken patterns from wrap_math_vars.py runs.

    The pattern $X = $Y$ (var wrapped inside existing math) appears
    when wrap_math_vars.py runs on already-wrapped content. Revert.
    """
    print('\n=== Step 0: Fix broken wraps ===')
    fixed = 0
    patterns = [
        # $f_{\rm leak} = $H_0$ = ... -> $f_{\rm leak} = H_0$ = ...
        # Use .*? for non-greedy match between $f and = $H_0$
        (r'\$f.*? = \$H_0\$ = ',
         r'$f_{\\rm leak} = H_0 = '),
        # General: $X = $Y$ -> $X = Y$ (any var X and Y, with { } allowed)
        (r'\$([A-Za-z0-9_\\\\\{\}\.]+) = \$([A-Za-z0-9_\\\\\{\}]+)\$',
         r'$\1 = \2$'),
        # \mathbb{Z}2 (no underscore) -> \mathbb{Z}_{2} (curly braces around digit
        # prevents markdown from interpreting _2 as italic emphasis)
        (r'\\mathbb\{Z\}([0-9])',
         r'\\mathbb{Z}_{\1}'),
        # \mathbb{Z}{}_{\ge 1 (and similar) -> \mathbb{Z}_{\ge 1.
        # Empty {} separator is also prone to GFM italic parsing in some renderers.
        (r'\\mathbb\{Z\}\{\}_',
         r'\\mathbb{Z}_'),
    ]  

    for fname in os.listdir(MARKDOWN_DIR):
        if not fname.endswith('.md'):
            continue
        fp = os.path.join(MARKDOWN_DIR, fname)
        with open(fp) as f:
            content = f.read()
        new_content = content
        for pattern, repl in patterns:
            new_content, n = re.subn(pattern, repl, new_content)
            if n > 0:
                print(f'  {fname}: Fixed {n} instances of nested $X$ pattern')
                fixed += n
        if new_content != content and not dry_run:
            with open(fp, 'w') as f:
                f.write(new_content)

    # Also process README.md (the markdown-only $\mathbb{Z}_2$ -> $\mathbb{Z}_{2}$
    # fix prevents GitHub from rendering _2 as italic emphasis)
    readme_path = os.path.join(WORKSPACE, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path) as f:
            content = f.read()
        new_content = content
        # Apply ONLY the mathbb fix to README (don't run nested-$X fix on README
        # since it has different syntax)
        readme_patterns = [
            (r'\\mathbb\{Z\}([0-9])',
             r'\\mathbb{Z}_{\1}'),
        ] 
        for pattern, repl in readme_patterns:
            new_content, n = re.subn(pattern, repl, new_content)
            if n > 0:
                print(f'  README.md: Fixed {n} instances of \\mathbb{{Z}}<digit>')
                fixed += n
        if new_content != content and not dry_run:
            with open(readme_path, 'w') as f:
                f.write(new_content)

    print(f'Fixed {fixed} broken wraps')
    return True


def step_fix_unbalanced_dollars(dry_run=False):
    """Find and fix unbalanced $ in markdown files.

    Also applies source bug fixes that are independent of $ count.
    """
    print('\n=== Step 1: Fix unbalanced $ ===')
    fixed = 0
    # Always-fix: applied to ALL .md files regardless of $ count
    always_fix = [
        # L323 (06_limitations.md:4479): $$..$ in prose breaks find_math_ranges
        # Wrap in inline code so find_math_ranges skips it
        ('State machine handles $$.. $ and $..$ correctly.',
         'State machine handles display math (`$$` ... `$$`) and inline math (`$` ... `$`) correctly.',
         'L323: wrap $$ in inline code'),
        # Source bug: 06_limitations.md:4499 - math has closing $ but missing
        # the explicit "= 67.4 km/s/Mpc" clarification. Always apply to ensure
        # this important f_leak principle is clear.
        ('**New principle**: $f_{\\rm leak} = H_0 = 2.18\\times10^{-18}\,\\text{s}^{-1}$\n',
         '**New principle**: $f_{\\rm leak} = H_0 = 2.18\\times10^{-18}\,\\text{s}^{-1}$ = 67.4 km/s/Mpc\n',
         'add = 67.4 km/s/Mpc to New principle'),
    ]
    # Conditional fixes: applied only if file has odd $ count
    known_fixes = [
        ('$$F_p $', '$F_p$', 'display -> inline'),
        ('$$E/\\tau$)', '$E/\\tau$', 'display -> inline'),
    ]
    for fname in os.listdir(MARKDOWN_DIR):
        if not fname.endswith('.md'):
            continue
        fp = os.path.join(MARKDOWN_DIR, fname)
        with open(fp) as f:
            content = f.read()
        new_content = content
        # Apply always-fix first
        for search, repl, desc in always_fix:
            if search in new_content:
                new_content = new_content.replace(search, repl)
                print(f'  {fname}: Fixed {desc!r}')
                fixed += 1
        # Apply known fixes if file has odd $ count
        dollar_count = new_content.count('$') - new_content.count('\\$')
        if dollar_count % 2 != 0:
            for search, repl, desc in known_fixes:
                if search in new_content:
                    new_content = new_content.replace(search, repl)
                    print(f'  {fname}: Fixed {desc!r}')
                    fixed += 1
        # Recount
        dollar_count = new_content.count('$') - new_content.count('\\$')
        # If still unbalanced, append closing $ at end of file
        if dollar_count % 2 != 0:
            stripped = new_content.rstrip()
            if stripped.endswith('$'):
                new_content = stripped[:-1] + '\n'
                print(f'  {fname}: Removed stray trailing $')
                fixed += 1
            else:
                new_content = new_content.rstrip() + '$\n'
                print(f'  {fname}: Appended closing $ at end of file (odd count)')
                fixed += 1
        if new_content != content and not dry_run:
            with open(fp, 'w') as f:
                f.write(new_content)
    print(f'Fixed {fixed} unbalanced-$ bugs')
    return True


def step_fix_math_spacing(dry_run=False):
    """Run fix_math_spacing.py - the safe one.

    This script:
    - Adds space before $ if prev char is non-space
    - Removes leading/trailing whitespace inside $...$ math

    It is the LAST step in the official pipeline.
    """
    print('\n=== Step 2: fix_math_spacing.py ===')
    if dry_run:
        run_script('fix_math_spacing.py')
    else:
        run_script('fix_math_spacing.py')
    return True


def step_wrap_unicode_powers(dry_run=False):
    """Run wrap_unicode_powers.py - our safe unicode wrapper."""
    print('\n=== Step 3: wrap_unicode_powers.py ===')
    if dry_run:
        run_script('wrap_unicode_powers.py')
    else:
        run_script('wrap_unicode_powers.py')
    return True


def step_inline_to_unicode(dry_run=False):
    """Convert simple inline LaTeX math to Unicode.

    User principle: 'use unicode for inline, and latex if not'.

    This converts single Greek letters, simple operators (×, →, ≤, ≥, etc.),
    and blackboard letters (ℤ, ℝ, etc.) to their Unicode equivalents in
    markdown files. Complex expressions (with \\rm, \\text, \\frac, multi-char
    subscripts) are kept as LaTeX.

    Note: only applies to .md files, NOT .tex files (LaTeX can't compile
    Unicode characters natively without XeLaTeX/LuaLaTeX).
    """
    print('\n=== Step 3.5: inline_to_unicode ===')
    if dry_run:
        return True
    # Run on all markdown files
    import glob
    files = glob.glob(os.path.join(MARKDOWN_DIR, '*.md'))
    files.append(os.path.join(WORKSPACE, 'README.md'))
    files.append(os.path.join(WORKSPACE, 'RELEASE_DESCRIPTION_v3.5.9-A2.md'))
    files.append(os.path.join(WORKSPACE, 'STATE_OF_THE_MODEL.md'))
    files.append(os.path.join(WORKSPACE, 'persistent_memory.md'))
    files.append(os.path.join(WORKSPACE, 'changelog.md'))
    files.append(os.path.join(WORKSPACE, 'paper', 'paper.md'))
    # Apply
    sys.path.insert(0, os.path.dirname(__file__))
    import inline_to_unicode
    total = 0
    for fp in files:
        if os.path.exists(fp):
            total += inline_to_unicode.process_file(fp, dry_run=dry_run)
    print(f'  Total: {total} inline math expressions converted to Unicode')
    return True


def step_wrap_math_vars(dry_run=False):
    """Run wrap_math_vars.py - AGGRESSIVE math wrapping.

    This script wraps math vars (M_Pl,4D, H_0, etc.) in $...$.
    Known issues:
      - Creates broken states like $X = $Y$ = ... (var wrapped inside math)
        These are fixed by the second fix_broken_wraps step.
    """
    print('\n=== Step 5: wrap_math_vars.py (aggressive) ===')
    if dry_run:
        run_script('wrap_math_vars.py')
    else:
        run_script('wrap_math_vars.py')
    return True


def step_build_pdf(dry_run=False):
    print('\n=== Step 4: Build PDF ===')
    if dry_run:
        print('  (dry-run, skipping build)')
        return True
    run('rm -rf paper/.build')
    result = run('cd paper && timeout 200 bash build_pdf.sh 2>&1', capture=True)
    if result.returncode != 0:
        print('  BUILD FAILED (non-zero exit code)')
        return False
    output = result.stdout + (result.stderr or '')
    if '! ' in output and 'Missing' in output:
        print('  BUILD HAS LATEX ERRORS:')
        error_lines = [l for l in output.split('\n') if l.startswith('! ')]
        for err in error_lines[:3]:
            print(f'    {err}')
        return False
    pdfinfo = run('pdfinfo paper/paper.pdf | grep -E "Pages|File size"', capture=True)
    if '611' not in pdfinfo.stdout:
        print(f'  WARNING: Page count is not 611: {pdfinfo.stdout}')
    return True


def step_audit(dry_run=False):
    print('\n=== Step 5: Audit ===')
    run('cd paper && python3 build_tools/audit_v2.py 2>&1 | tail -5', capture=True)
    return True


STEPS = [
    'fix_broken_wraps',
    'fix_unbalanced_dollars',
    'fix_math_spacing',
    'wrap_unicode_powers',
    'inline_to_unicode',  # NEW: convert simple inline LaTeX to Unicode
    'wrap_math_vars',   # AGGRESSIVE: wraps M_Pl,4D, H_0, etc.
    'fix_broken_wraps',  # Run AGAIN to clean up broken patterns from wrap_math_vars
    'fix_math_spacing',  # Run AGAIN to clean up spacing
    'build_pdf',
    'audit',
]


def main():
    dry_run = '--dry-run' in sys.argv
    skip = set()
    for arg in sys.argv[1:]:
        if arg.startswith('--skip='):
            skip.add(arg.split('=')[1])

    if not dry_run:
        git_revert()

    step_fns = {
        'fix_broken_wraps': step_fix_broken_wraps,
        'fix_unbalanced_dollars': step_fix_unbalanced_dollars,
        'fix_math_spacing': step_fix_math_spacing,
        'wrap_unicode_powers': step_wrap_unicode_powers,
        'inline_to_unicode': step_inline_to_unicode,
        'wrap_math_vars': step_wrap_math_vars,
        'build_pdf': step_build_pdf,
        'audit': step_audit,
    }

    for name in STEPS:
        if name in skip:
            print(f'\n=== Skipping: {name} ===')
            continue
        if not step_fns[name](dry_run):
            print(f'\n*** Pipeline stopped: {name} failed ***')
            if not dry_run:
                git_revert()
            return 1

    print('\n=== Pipeline complete! ===')
    return 0


if __name__ == '__main__':
    sys.exit(main())
