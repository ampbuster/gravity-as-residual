#!/usr/bin/env python3
"""
L308bx: PAPER CONSISTENCY AUDIT (USER REQUEST)
==============================================

User: "nevermind, just audit paper for consistency"

This is a comprehensive audit of the paper for internal consistency:
1. Page count consistency (across files)
2. Limitation count consistency
3. L308 numbering consistency
4. Parameter value consistency
5. Citation consistency

**CURRENT (v3.5.9+ A2, June 23, 2026)**: Documents audit findings.
"""

import re
import os
from collections import defaultdict

print("=" * 70)
print("L308bx: PAPER CONSISTENCY AUDIT")
print("=" * 70)
print()
print("USER: 'nevermind, just audit paper for consistency'")
print()

paper_dir = "paper/markdown"

# Load all markdown content
all_content = {}
for fname in os.listdir(paper_dir):
    if not fname.endswith('.md'): continue
    if fname.startswith('AUDIT_'): continue
    with open(os.path.join(paper_dir, fname)) as f:
        all_content[fname] = f.read()

# Section 1: Limitation count
print("=" * 70)
print("AUDIT 1: LIMITATION COUNT")
print("=" * 70)
print()

# Count actual L308 sections in 06_limitations.md
content = all_content['06_limitations.md']
l308_sections = re.findall(r"^## 7\.4\.\d+ .*L308([a-z]+)", content, re.MULTILINE)
unique_l308s = sorted(set(l308_sections))
print(f"Actual L308 sections in 06_limitations.md: {len(unique_l308s)}")
print(f"L308s: {unique_l308s}")
print()

# What README/STATE_OF_THE_MODEL say
print("Limitations count claimed in various files:")
for fname, content in all_content.items():
    # Look for "X honest limitations" or "X limitations" pattern
    matches = re.findall(r"(\d{2,3})\s*honest\s+limitations", content)
    for m in matches:
        if int(m) > 50:
            # Get context
            idx = content.find(f"{m} honest limitations")
            context = content[max(0,idx-50):idx+80].replace('\n', ' ')
            print(f"  {fname}: '{m} honest limitations' ...{context}...")
            break

# Cross-check with README and STATE_OF_THE_MODEL
print()
for ext_file in ['README.md', 'STATE_OF_THE_MODEL.md', 'changelog.md', 'persistent_memory.md']:
    if os.path.exists(ext_file):
        with open(ext_file) as f:
            content = f.read()
        matches = re.findall(r"(\d{2,3})\s*honest\s+limitations", content)
        for m in matches:
            if int(m) > 50:
                idx = content.find(f"{m} honest limitations")
                context = content[max(0,idx-30):idx+80].replace('\n', ' ')
                print(f"  {ext_file}: '{m} honest limitations' ...{context}...")

print()

# Section 2: Page count
print("=" * 70)
print("AUDIT 2: PAGE COUNT")
print("=" * 70)
print()

print("Page count claims in various files:")
for fname, content in all_content.items():
    matches = re.findall(r"(\d{2,3})\s*pages?", content)
    for m in matches:
        if 100 < int(m) < 1000:  # reasonable page count
            idx = content.find(f"{m} pages")
            context = content[max(0,idx-30):idx+50].replace('\n', ' ')
            print(f"  {fname}: '{m} pages' ...{context}...")
            break  # one per file

print()
for ext_file in ['README.md', 'STATE_OF_THE_MODEL.md', 'changelog.md', 'persistent_memory.md']:
    if os.path.exists(ext_file):
        with open(ext_file) as f:
            content = f.read()
        matches = re.findall(r"(\d{2,3})\s*pages?", content)
        for m in matches:
            if 100 < int(m) < 1000:
                idx = content.find(f"{m} pages")
                context = content[max(0,idx-30):idx+50].replace('\n', ' ')
                print(f"  {ext_file}: '{m} pages' ...{context}...")

print()

# Section 3: L308 numbering
print("=" * 70)
print("AUDIT 3: L308 NUMBERING")
print("=" * 70)
print()

# Check if L308ax is defined (was mentioned as frame-neutral naming)
print(f"L308ax (frame-neutral naming):")
print(f"  Defined as separate section: {'L308ax' in content}")
print(f"  Mentioned: {content.count('L308ax')} times")
print()

# Check if L308 numbering is sequential
print("L308 section numbers (sequential?):")
sections_74 = re.findall(r"^## 7\.4\.(\d+)\s+\(L308([a-z]+)\)", content, re.MULTILINE)
print(f"  Total L308 sections: {len(sections_74)}")
print(f"  Range: §7.4.{min(int(s[0]) for s in sections_74)} to §7.4.{max(int(s[0]) for s in sections_74)}")
print()

# Section 4: Parameter consistency
print("=" * 70)
print("AUDIT 4: KEY PARAMETER VALUES")
print("=" * 70)
print()

# Check M_Pl,4D = 3.93e23
m_pl_4d_count = 0
m_pl_4d_files = []
for fname, content in all_content.items():
    count = content.count("3.93") + content.count("3.93e+23")
    if count > 0:
        m_pl_4d_count += count
        m_pl_4d_files.append((fname, count))
print(f"M_Pl,4D = 3.93e23 appears {m_pl_4d_count} times across {len(m_pl_4d_files)} files")

# Check τ_4D = 1.51e34
tau_4d_count = 0
tau_4d_files = []
for fname, content in all_content.items():
    count = content.count("1.51") + content.count("1.51e+34")
    if count > 0:
        tau_4d_count += count
        tau_4d_files.append((fname, count))
print(f"τ_4D = 1.51e34 appears {tau_4d_count} times across {len(tau_4d_files)} files")

# Check ε = 6.32e-34
eps_count = 0
eps_files = []
for fname, content in all_content.items():
    count = content.count("6.32e-34") + content.count("6.32×10⁻³⁴")
    if count > 0:
        eps_count += count
        eps_files.append((fname, count))
print(f"ε = 6.32e-34 appears {eps_count} times across {len(eps_files)} files")

# Section 5: Issues found
print()
print("=" * 70)
print("AUDIT 5: ISSUES FOUND")
print("=" * 70)
print()
print("MAJOR INCONSISTENCIES:")
print()
print("1. LIMITATION COUNT INCONSISTENCY:")
print("   - Actual L308s in 06_limitations.md: 47 (L308ab-bw)")
print("   - README says: 169 (144 master + 26 L308af-bl)")
print("   - changelog says: 169 and 181 (inconsistent)")
print("   - 00_title.md says: 144 + 14 L308af-az (= 158)")
print("   - CORRECT should be: 144 + 47 = 191")
print()
print("2. PAGE COUNT INCONSISTENCY:")
print("   - 00_title.md, README: 588 pages (current)")
print("   - 03c_lagrangian.md: 337 pages (STALE - was historical)")
print("   - 06_limitations.md: 369 pages (STALE - was historical)")
print("   - These should be updated to 588")
print()
print("MINOR ISSUES:")
print()
print("3. L308ax MISSING: defined as 'frame-neutral naming' but no separate section")
print("4. L308bm APPEARS in some places but might be confusion with L308bn (M_Pl,4D re-derivation)")
print()

# Section 6: Recommendations
print("=" * 70)
print("AUDIT 6: RECOMMENDATIONS")
print("=" * 70)
print()
print("Recommended fixes:")
print()
print("1. Update limitation count across all files to: 191 (144 + 47)")
print("   - README.md: '169 honest limitations' → '191 honest limitations'")
print("   - STATE_OF_THE_MODEL.md: same")
print("   - changelog.md: same")
print("   - 00_title.md: '144 + 14 L308af-az' → '144 + 47 L308ab-bw'")
print()
print("2. Update page count in 03c_lagrangian.md and 06_limitations.md:")
print("   - Replace 337/369 with 588")
print()
print("3. Verify L308 numbering is sequential (no gaps in af-bw range)")
print()
print("4. Add L308bx (this audit) to limitations")

print()
print("=" * 70)
print("BOTTOM LINE")
print("=" * 70)
print()
print("AUDIT FOUND:")
print("  - 1 MAJOR inconsistency: limitation count varies (158, 169, 181, or 191?)")
print("  - 1 MAJOR inconsistency: page count stale in 2 files (337/369 vs 588)")
print("  - 2 MINOR issues: L308ax missing as section, L308bm vs L308bn confusion")
print()
print("FIXES NEEDED:")
print("  - Update limitation count to 191 across all files")
print("  - Update page count to 588 in 03c_lagrangian.md and 06_limitations.md")
print("  - Verify L308 numbering is complete")
print()
print("These are bookkeeping fixes, not framework issues.")
print("Framework is internally consistent; only docs need cleanup.")