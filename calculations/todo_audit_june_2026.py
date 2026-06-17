#!/usr/bin/env python3
"""
TODO Audit (June 17, 2026) — check status of 10 open research questions
==============================================================================

Walk through each TODO from README v2.7.67 and check status based on
calculations/ work done since then.

Goal: honest accounting of what's been done vs what's still open.
"""

import os
import re
from pathlib import Path

CALC_DIR = Path('calculations')
PAPER_DIR = Path('paper/markdown')

def file_contains(pattern, paths, case_insensitive=False):
    """Check if any of the paths contain the regex pattern."""
    flags = re.IGNORECASE if case_insensitive else 0
    rx = re.compile(pattern, flags)
    hits = []
    for p in paths:
        if not p.exists():
            continue
        try:
            content = p.read_text(errors='ignore')
            if rx.search(content):
                hits.append(str(p))
        except Exception:
            pass
    return hits

# Get all .py and .md files
py_files = list(CALC_DIR.glob('*.py'))
md_files = list(PAPER_DIR.glob('*.md')) + [Path('README.md')]

all_files = py_files + md_files

print("="*72)
print("TODO AUDIT (June 17, 2026) — 10 open research questions")
print("="*72)

# TODO 1: Derive 1/√N scaling rigorously
print("\n" + "="*72)
print("TODO #1: Derive 1/√N scaling rigorously")
print("="*72)
hits = file_contains(r'1/sqrt\(\{?N\}?\)|1/√N|1\.289|1/√12', all_files)
print(f"Files with 1/√N/1.289 discussion: {len(hits)}")
print(f"Sample: {hits[:3]}")
print()
print("Status: STRUCTURAL DERIVATION done in v3-v5 (lagrangian_trial_error_v3/v4/v5.py)")
print("  - Saddle-point calculation shows 1/√N from random matrix structure")
print("  - 1+1/√12 is the unique natural formula (off by 0.0003)")
print("  - But: NOT rigorous from Z (partition function) — only structural match")
print("  - LIMITATION L68/L71 remains OPEN")

# TODO 2: Test CKM/PMNS derivation
print("\n" + "="*72)
print("TODO #2: Test CKM/PMNS derivation")
print("="*72)
hits = file_contains(r'CKM|PMNS|quark mixing|neutrino mixing', all_files)
print(f"Files with CKM/PMNS: {len(hits)}")
print(f"Sample: {hits[:3]}")
print()
print("Status: NOT addressed. 495 SYK couplings vs 21 SM parameters")
print("  - L84 OPEN, requires SYK symmetry breaking pattern")

# TODO 3: Derive SM mass ratios
print("\n" + "="*72)
print("TODO #3: Derive SM mass ratios")
print("="*72)
hits = file_contains(r'mass.{0,30}ratio|m_b/m_t|mu/ms|generation mass', all_files)
print(f"Files with mass ratios: {len(hits)}")
print(f"Sample: {hits[:3]}")
print()
print("Status: NOT addressed. All 12 Majoranas have same mass in pure SYK")
print("  - L84 OPEN, requires SYK symmetry breaking")

# TODO 4: Refine BLG model for magic angle
print("\n" + "="*72)
print("TODO #4: Refine BLG model for magic angle")
print("="*72)
hits = file_contains(r'BLG|magic angle|Bistritzer', all_files, case_insensitive=True)
print(f"Files with BLG/magic angle: {len(hits)}")
print(f"Sample: {hits[:3]}")
print()
print("Status: Mentioned in §3.60 (Nariai-like, BLG at 1.5-2.0°)")
print("  - But: NOT refined with specific Bistritzer-MacDonald calculation")
print("  - L83 REVISED remains OPEN")

# TODO 5: Establish AdS₂ × S² topology
print("\n" + "="*72)
print("TODO #5: Establish AdS₂ × S² topology")
print("="*72)
hits = file_contains(r'AdS_2.*S_2|AdS₂.*S²|Nariai', all_files)
print(f"Files with AdS₂ × S²: {len(hits)}")
print(f"Sample: {hits[:3]}")
print()
print("Status: Claimed in §3.60 (Nariai-like) and Lagrangian v7 (candidates)")
print("  - But: NOT rigorously derived — claimed as 'Nariai-like' not 'exactly Nariai'")
print("  - L82 REVISED remains OPEN")

# TODO 6: Why N=12 specifically?
print("\n" + "="*72)
print("TODO #6: Why N=12 specifically?")
print("="*72)
hits = file_contains(r'N.{0,5}12|why.{0,30}12|Weyl.*generation|3 generation', all_files)
print(f"Files with N=12 discussion: {len(hits)}")
print(f"Sample: {hits[:3]}")
print()
print("Status: PARTIALLY addressed in Lagrangian v7")
print("  - 4 Weyl × 3 generations (SM connection)")
print("  - 24/2 = 12 from Majorana pairs")
print("  - SU(12) → 143 generators")
print("  - W∞: 12 higher-spin currents")
print("  - But: no first-principles derivation; multiple structural matches")
print("  - L45 remains OPEN")

# TODO 7: Numerical simulation of q=4 SYK with N=12
print("\n" + "="*72)
print("TODO #7: Numerical simulation of q=4 SYK with N=12")
print("="*72)
hits = file_contains(r'SYK.{0,30}sim|q=4 SYK|N=12.{0,20}sim|monte carlo.*SYK', all_files)
print(f"Files with SYK simulation: {len(hits)}")
print(f"Sample: {hits[:3]}")
print()
print("Status: Component-by-component done in Lagrangian v3-v6")
print("  - Component trial-and-error (not full numerical SYK sim)")
print("  - Mass scaling M_2D ~ (E_Pl/E)^0.29 forced by data")
print("  - But: full G(τ) calculation NOT done")
print("  - L81 OPEN")

# TODO 8: Test 2D universe Hawking radiation spectrum
print("\n" + "="*72)
print("TODO #8: Test 2D universe Hawking radiation spectrum")
print("="*72)
hits = file_contains(r'Hawking.{0,30}2D|Hawking spectrum|2D.*Hawking|Nariai.*T=0', all_files)
print(f"Files with 2D Hawking: {len(hits)}")
print(f"Sample: {hits[:3]}")
print()
print("Status: Mentioned in §3.60 (Nariai: T=0, no Hawking)")
print("  - But: spectrum NOT calculated")
print("  - L82 OPEN")

# TODO 9: Connect α = 1.29 to DSSYK
print("\n" + "="*72)
print("TODO #9: Connect α = 1.29 to DSSYK")
print("="*72)
hits = file_contains(r'DSSYK|double.{0,20}scale', all_files, case_insensitive=True)
print(f"Files with DSSYK: {len(hits)}")
print(f"Sample: {hits[:3]}")
print()
print("Status: Attempted in v27_derivation_attempts.py — INCONCLUSIVE")
print("  - DSSYK partition function explored")
print("  - '1/2' appears in DSSYK spectral density Gaussian (suggestive)")
print("  - But: no explicit α=1.289 derivation from DSSYK")
print("  - L68-78 status: STRUCTURAL ONLY")

# TODO 10: Check if 12 = 24/2 Leech connection holds
print("\n" + "="*72)
print("TODO #10: Check 12 = 24/2 Leech connection")
print("="*72)
hits = file_contains(r'Leech|24 dim|24/2|bosonic string', all_files, case_insensitive=True)
print(f"Files with Leech: {len(hits)}")
print(f"Sample: {hits[:3]}")
print()
print("Status: Mentioned as candidate in Lagrangian v7")
print("  - Leech lattice has 24 dimensions, /2 for Majorana = 12")
print("  - But: explicit connection to vertex operator algebra NOT made")
print("  - L75 remains STRUCTURAL ONLY")

# Summary
print("\n" + "="*72)
print("SUMMARY (June 2026 status)")
print("="*72)

print("""
CLOSED (or near-closed):
- TODO #1 (1/√N derivation): STRUCTURAL derivation done. Saddle-point +
  random matrix structure give 1/√N. Unique formula 1+1/√12 confirmed.
  REMAINING: rigorous Z derivation (likely requires 2D CFT expert).

PARTIALLY ADDRESSED:
- TODO #6 (Why N=12): Multiple structural matches identified (4×3, 24/2, SU(12)).
  REMAINING: first-principles derivation.
- TODO #9 (DSSYK): Connection suggestive, inconclusive.

OPEN (NOT addressed):
- TODO #2 (CKM/PMNS): No attempt. L84 OPEN.
- TODO #3 (SM mass ratios): No attempt. L84 OPEN.
- TODO #4 (BLG magic angle): Mentioned but not refined. L83 OPEN.
- TODO #5 (AdS₂ × S² topology): Claimed but not derived. L82 OPEN.
- TODO #7 (Full SYK simulation): Component-by-component only. L81 OPEN.
- TODO #8 (2D Hawking spectrum): Claimed T=0 (Nariai) but not derived. L82 OPEN.
- TODO #10 (Leech connection): Mentioned but not formal. L75 OPEN.

Recommendation: update README TODO section to reflect this audit.
""")