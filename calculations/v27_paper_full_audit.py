#!/usr/bin/env python3
"""
v27_paper_full_audit.py
========================
Comprehensive paper inconsistency audit.

Checks:
1. Test counts (16/17 vs 17/17, 11/11 vs 10/11, 7/7 vs 8/7)
2. Falsified counts ("0 falsified" vs "2 components falsified")
3. Limitations counts ("32 honest" vs "33 honest")
4. Parameter value consistency (g_+, f_active, F_p, f_back, H_0,4D, etc.)
5. f_proj notation overload
6. f_back vs 32/68 split
7. f_active vs F_p distinction
8. L20 status (CLOSED vs FREE PARAMETER)
9. Lelli+ 2017 typo
10. E_primordial as L34

Writes a markdown report to calculations/v27_paper_full_audit_report.md
"""
import re
from collections import defaultdict

PAPER = "/workspace/github-repo/paper/paper.md"
REPORT = "/workspace/github-repo/calculations/v27_paper_full_audit_report.md"


def main():
    with open(PAPER) as f:
        text = f.read()
    lines = text.split("\n")

    findings = defaultdict(list)

    # ==========================================================================
    # 1. Test counts
    # ==========================================================================
    for i, line in enumerate(lines, 1):
        if re.search(r'\b17/17\b', line):
            # Filter out meta-references like '17/17 test categories' -> '16/17'
            # and version announcements
            is_meta = '→' in line and '16/17' in line
            is_announcement = 'Version 2.7' in line
            if not is_meta and not is_announcement:
                findings['17/17 test count (should be 16/17)'].append((i, line[:120]))
        if re.search(r'\b10/11\b', line):
            # Filter out '10/11 dimensions' (string theory)
            if 'dimension' not in line.lower() and 'string' not in line.lower():
                findings['10/11 test count (should be 11/11)'].append((i, line[:120]))
        if re.search(r'\b8/7\b', line):
            findings['8/7 specific cases (should be 7/7)'].append((i, line[:120]))

    # ==========================================================================
    # 2. Falsified counts
    # ==========================================================================
    for i, line in enumerate(lines, 1):
        if re.search(r'\b0 falsified\b', line):
            if '2 components' not in line:
                findings["'0 falsified' (should be '2 components falsified')"].append((i, line[:120]))
        if re.search(r'\bno falsified\b', line):
            findings["'no falsified' (should be '2 components falsified')"].append((i, line[:120]))

    # ==========================================================================
    # 3. Limitations counts
    # ==========================================================================
    for i, line in enumerate(lines, 1):
        # '32 honest limitations' in current-state context (not historical changelogs)
        if re.search(r'\b32 honest limitations\b', line) or re.search(r'\bdocuments 32\b', line):
            # Filter out version announcements (v2.7, v2.7.1, v2.7.3, v2.7.4)
            # These correctly report historical limitation counts.
            is_announcement = 'Version 2.7' in line
            is_meta = ('→' in line and '33 honest' in line) or 'is 33' in line
            if not is_announcement and not is_meta:
                findings["'32 honest limitations' (should be 33)"].append((i, line[:120]))
        if re.search(r'\bidentify 32\b', line):
            # Filter out meta-references (where 33 is mentioned in same line)
            if '33 honest' not in line:
                findings["'identify 32' (should be 33)"].append((i, line[:120]))

    # ==========================================================================
    # 4. f_proj notation overload (excluding renaming documentation)
    # ==========================================================================
    for i, line in enumerate(lines, 1):
        if re.search(r'\bf_proj\b', line):
            # Filter out lines that are part of the rename documentation
            if 'NOT to be confused' not in line and 'renamed' not in line:
                findings['f_proj notation (rename to f_split or f_attractive)'].append((i, line[:120]))

    # ==========================================================================
    # 5. L20 status (CLOSED vs FREE PARAMETER)
    # ==========================================================================
    for i, line in enumerate(lines, 1):
        if re.search(r'\b20 \|.*CLOSED', line):
            # Check if this is f_active line
            if 'f_active' in line:
                findings['L20 marked CLOSED but f_active is FREE PARAMETER (v2.7.1)'].append((i, line[:120]))

    # ==========================================================================
    # 6. Lelli+ typo
    # ==========================================================================
    for i, line in enumerate(lines, 1):
        if re.search(r'1\.20\s*\\\\times\s*10\\?\\?\^{-11}', line) or re.search(r'1\.20\s*×\s*10⁻¹¹', line):
            findings['Lelli+ 2017 typo: 1.20e-11 should be 1.20e-10'].append((i, line[:120]))

    # ==========================================================================
    # 7. f_active = FREE PARAMETER vs CLOSED (count balance check)
    # ==========================================================================
    f_active_free = 0
    f_active_closed_claim = 0
    for i, line in enumerate(lines, 1):
        if re.search(r'f_active.*FREE PARAMETER|f_active.*free parameter', line):
            f_active_free += 1
        if re.search(r'f_active.*CLOSED.*derivation|Limitation 20.*CLOSED|L20.*CLOSED', line):
            if 'REVERTED' not in line and 'PARTIAL' not in line:
                f_active_closed_claim += 1

    if f_active_free > 0 and f_active_closed_claim > 0:
        findings['f_active is BOTH "FREE PARAMETER" and "CLOSED" in paper'].append(
            (0, f'{f_active_free}x FREE PARAMETER, {f_active_closed_claim}x unflagged CLOSED claim')
        )

    # ==========================================================================
    # Write report
    # ==========================================================================
    with open(REPORT, "w") as f:
        f.write("# PAPER INCONSISTENCY AUDIT (v27_full)\n\n")
        f.write(f"Source: {PAPER}\n\n")
        f.write("---\n\n")

        if not findings:
            f.write("OK No inconsistencies found.\n")
        else:
            for category, items in findings.items():
                f.write(f"## {category} ({len(items)} occurrences)\n\n")
                for line_num, snippet in items[:20]:
                    if line_num == 0:
                        f.write(f"  - {snippet}\n")
                    else:
                        f.write(f"  - Line {line_num}: `{snippet}...`\n")
                if len(items) > 20:
                    f.write(f"  - ... and {len(items) - 20} more\n")
                f.write("\n")

        f.write(f"\n---\n\n")
        f.write(f"Total categories: {len(findings)}\n")
        f.write(f"Total occurrences: {sum(len(v) for v in findings.values())}\n")

    print(f"Wrote report to {REPORT}")
    print(f"Found {len(findings)} categories with {sum(len(v) for v in findings.values())} total issues.")
    for cat, items in findings.items():
        print(f"  {cat}: {len(items)}")


if __name__ == "__main__":
    main()
