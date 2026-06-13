#!/usr/bin/env python3
"""
5D in the cascade: gives 4D DE, gains DM from 4D (per parent-child DM symmetry)

User's question: what about 5D? Doesn't it give 4D DE and gain DM from 4D?

Per parent-child DM symmetry (commit 69):
  - Parent's antigravity (in child) = child's DE
  - Child's attractive gravity (in parent) = parent's DM

For 5D->4D pair:
  - 5D is parent of 4D
  - 5D's antigravity (in 4D frame) = 4D's DE
  - 4D's attractive (back-projected to 5D) = 5D's DM

YES, 5D gives 4D DE (via 5D's antigravity projection).
YES, 5D gains DM from 4D (via 4D's back-projection).

This script:
  1. Confirms 5D's role per parent-child DM symmetry
  2. Computes the chain 5D->4D->3+1D->2D in detail
  3. Compares Cone 1 (no 5D) vs Cone 2 (with 5D)
  4. Asks: does Cone 2 make more sense than Cone 1?

Caveat: my earlier claim in commit 69 had the symmetry INVERTED.
Let me re-derive carefully.

Original commit 69 said:
  "Parent's antigravity (in child) = child's DM"
  "Child's attractive gravity (in parent) = parent's DM"

But the cascade actually says:
  - 4D's antigravity (in 3+1D frame) = 3+1D's DE (not DM!)

So the symmetry I claimed was wrong. The correct symmetry is:
  - Parent's antigravity (in child) = child's DE (not DM)
  - Child's attractive gravity (in parent) = parent's DM

This changes the analysis. Let me redo it carefully.
"""

import math
import sys
sys.path.insert(0, ".")
sys.path.insert(0, "calculations")

from cascade_model import Constants


def hr(ch="="):
    print()
    print(ch * 78)
    print(ch * 78)


def main():
    hr()
    print("5D IN THE CASCADE: GIVES 4D DE, GAINS DM FROM 4D")
    hr()

    print(f"\n  Step 1: Correct the parent-child DM symmetry")
    print(f"  ----------------------------------------------------------------")
    print(f"  Original claim (commit 69):")
    print(f"    'Parent's antigravity (in child) = child's DM'")
    print(f"    'Child's attractive gravity (in parent) = parent's DM'")
    print()
    print(f"  PROBLEM: this contradicts the cascade's known claims.")
    print(f"    - 4D's antigravity (in 3+1D frame) = 3+1D's DE (per cascade)")
    print(f"    - So 4D's antigravity in child = child's DE, not child's DM")
    print()
    print(f"  CORRECTED symmetry:")
    print(f"    - Parent's antigravity (in child) = child's DE")
    print(f"    - Child's attractive gravity (in parent) = parent's DM")
    print()
    print(f"  Let me redo the analysis with the corrected symmetry.")

    print(f"\n\n  Step 2: Apply corrected symmetry to 5D->4D->3+1D->2D chain")
    print(f"  ----------------------------------------------------------------")
    print(f"  In Cone 2 (5D->4D->3+1D->2D):")
    print()
    print(f"  5D's antigravity (in 4D frame) = 4D's DE")
    print(f"    - 5D is parent of 4D")
    print(f"    - 5D's 68% vacuum residue projects DOWN to 4D as 4D's DE")
    print()
    print(f"  4D's attractive (in 5D frame) = 5D's DM")
    print(f"    - 4D is child of 5D")
    print(f"    - 4D's energetic content (32% of 4D) back-projects UP to 5D as 5D's DM")
    print()
    print(f"  4D's antigravity (in 3+1D frame) = 3+1D's DE")
    print(f"    - 4D is parent of 3+1D")
    print(f"    - 4D's 68% vacuum residue projects DOWN to 3+1D as 3+1D's DE")
    print(f"    - This is the cascade's known claim: 3+1D's DE = 4D's antigravity")
    print()
    print(f"  3+1D's attractive (in 4D frame) = 4D's DM")
    print(f"    - 3+1D is child of 4D")
    print(f"    - 3+1D's energetic content back-projects UP to 4D as 4D's DM")
    print(f"    - This is the cascade's known claim: 4D's DM = 3+1D's back-projection")
    print()
    print(f"  3+1D's antigravity (in 2D frame) = 2D's DE")
    print(f"    - 3+1D is parent of 2D")
    print(f"    - 3+1D's 68% vacuum projects DOWN to 2D as 2D's DE")
    print()
    print(f"  2D's attractive (in 3+1D frame) = 3+1D's DM")
    print(f"    - 2D is child of 3+1D")
    print(f"    - 2D's energetic back-projects UP to 3+1D as 3+1D's DM")
    print(f"    - This is the cascade's known claim: 3+1D's DM = 2D back-projection")
    print()
    print(f"  2D has no children, so 2D's DM = 0 in 2D's frame.")

    print(f"\n\n  Step 3: Summary of the chain in Cone 2")
    print(f"  ----------------------------------------------------------------")
    print(f"  {'Level':>6} | {'Parent':>10} | {'Children':>10} | {'m source':>20} | {'DM source':>25} | {'DE source':>25}")
    print(f"  {'-'*6} | {'-'*10} | {'-'*10} | {'-'*20} | {'-'*25} | {'-'*25}")
    print(f"  {'5D':>6} | {'(none)':>10} | {'4D':>10} | {'5D intrinsic':>20} | {'4D back-projection':>25} | {'5D vacuum (no parent)':>25}")
    print(f"  {'4D':>6} | {'5D':>10} | {'3+1D':>10} | {'4D intrinsic':>20} | {'3+1D back-projection':>25} | {'5D antigravity':>25}")
    print(f"  {'3+1D':>6} | {'4D':>10} | {'2D':>10} | {'direct projection':>20} | {'2D back-projection':>25} | {'4D antigravity':>25}")
    print(f"  {'2D':>6} | {'3+1D':>10} | {'(none)':>10} | {'original event':>20} | {'(none, no children)':>25} | {'3+1D antigravity':>25}")
    print()
    print(f"  Pattern: every level has DM from children and DE from parent.")
    print(f"  Top level (5D): no parent, so DE is just '5D's own vacuum'")
    print(f"  Bottom level (2D): no children, so DM is just 0")

    print(f"\n\n  Step 4: User's specific question")
    print(f"  ----------------------------------------------------------------")
    print(f"  Q: 'doesn't 5D give 4D DE, and gain DM from 4D?'")
    print()
    print(f"  A: YES, exactly. Per parent-child DM symmetry:")
    print(f"    - 5D's antigravity (in 4D frame) = 4D's DE")
    print(f"    - 4D's attractive (in 5D frame) = 5D's DM")
    print()
    print(f"  This is consistent with the corrected symmetry.")
    print()
    print(f"  In Cone 1 (no 5D):")
    print(f"    - 4D has no parent, so 4D's DE = 4D's own vacuum (no source)")
    print(f"    - 4D's 'DM' is 3+1D's back-projection (per cascade)")
    print(f"    - 4D has DE (from 4D's own vacuum) and DM (from 3+1D)")
    print()
    print(f"  In Cone 2 (with 5D):")
    print(f"    - 4D has 5D as parent, so 4D's DE = 5D's antigravity (with source)")
    print(f"    - 4D's DM = 3+1D's back-projection (same as Cone 1)")
    print(f"    - 4D has DE (from 5D) and DM (from 3+1D)")

    print(f"\n\n  Step 5: Does Cone 2 make MORE sense than Cone 1?")
    print(f"  ----------------------------------------------------------------")
    print(f"  Cone 2 advantage: 4D's DE has a SOURCE (5D's antigravity).")
    print(f"    - In Cone 1, 4D's DE is just '4D's own vacuum' (no source)")
    print(f"    - In Cone 2, 4D's DE is '5D's antigravity projection' (with source)")
    print(f"  Cone 2 is more 'complete': every level's DE has a parent source.")
    print()
    print(f"  Cone 1 advantage: parsimony (1 parameter vs 2)")
    print(f"    - Cone 1: depth=2 (1 parameter)")
    print(f"    - Cone 2: depth=3 with 5D above (2 parameters)")
    print()
    print(f"  Which is 'more sense'?")
    print(f"    - Cone 2 has more structure (every level has DE source)")
    print(f"    - Cone 1 is more parsimonious")
    print(f"    - Both are consistent with the cascade's framework")
    print()
    print(f"  The cascade's derivation (commit 76) prefers Cone 1 (parsimony).")
    print(f"  But: if you value 'completeness' over parsimony, Cone 2 is better.")
    print()
    print(f"  This is a choice, not derivable from cascade alone.")
    print()
    print(f"  Status: Cone 2 is the user's intuition, and it has merit.")
    print(f"  But the cascade's principled derivation prefers Cone 1 (parsimony).")

    print(f"\n\n  Step 6: Implications of Cone 2 for 4D's m/DM/DE")
    print(f"  ----------------------------------------------------------------")
    print(f"  In Cone 2, 4D's m/DM/DE in 4D's frame:")
    print(f"    - 4D's matter (X%): 4D's intrinsic matter (X is 4D-specific)")
    print(f"    - 4D's DM (Y%): 3+1D's back-projection = 32% of 4D's energetic = 0.32 * 0.32 * E_5D")
    print(f"    - 4D's DE (Z%): 5D's antigravity = 68% of E_5D's vacuum")
    print()
    print(f"  Within 4D's frame, 4D's m+DM = 32% of 4D (cone-shape universal)")
    print(f"  So: X + Y = 32%")
    print()
    print(f"  If 4D's DM = 3+1D's full back-projection (32% of 4D):")
    print(f"    - Y = 32%, so X = 0%")
    print(f"    - 4D's m/DM/DE = 0/32/68")
    print()
    print(f"  If 4D has some intrinsic matter:")
    print(f"    - X = some value, Y = 32 - X")
    print(f"    - 4D's m/DM/DE = (X, 32-X, 68) for some X")
    print()
    print(f"  In Cone 2, 4D's m is 4D's intrinsic matter (X).")
    print(f"  4D's DE is 5D's antigravity (= 68% of 4D in cone-shape).")
    print(f"  4D's DM is 3+1D's back-projection.")
    print()
    print(f"  The DE source is now EXTERNAL (5D), not INTERNAL (4D's own vacuum).")
    print(f"  This is a more 'complete' picture.")

    print(f"\n\n  Step 7: Numerical comparison")
    print(f"  ----------------------------------------------------------------")
    rho_c = 8.5e-27  # kg/m^3
    c = Constants.c
    R_observable = 4.4e26  # m
    V_observable = (4/3) * math.pi * R_observable**3
    E_3plus1D = rho_c * c**2 * V_observable
    E_4D = E_3plus1D / 0.32
    E_5D = E_4D / 0.32
    
    print(f"  Cone 2 (5D->4D->3+1D->2D) energy hierarchy:")
    print(f"    E_5D = E_4D / 0.32 = {E_5D:.3e} J (~3x E_4D)")
    print(f"    E_4D = E_3plus1D / 0.32 = {E_4D:.3e} J (~3x E_3plus1D)")
    print(f"    E_3plus1D = {E_3plus1D:.3e} J (observed)")
    print()
    print(f"  In Cone 2:")
    print(f"    5D's total: {E_5D:.3e} J")
    print(f"    5D's energetic (32%): {0.32*E_5D:.3e} J = E_4D")
    print(f"    5D's vacuum (68%): {0.68*E_5D:.3e} J (5D's antigravity)")
    print()
    print(f"    4D's total: {E_4D:.3e} J")
    print(f"    4D's energetic (32%): {0.32*E_4D:.3e} J = E_3plus1D")
    print(f"    4D's vacuum (68%): {0.68*E_4D:.3e} J (4D's antigravity = 3+1D's DE)")
    print(f"    In Cone 2: 4D's DE is also 5D's antigravity projection (same value)")
    print()
    print(f"    3+1D's total: {E_3plus1D:.3e} J")
    print(f"    3+1D's matter (5%): {0.05*E_3plus1D:.3e} J")
    print(f"    3+1D's DM (27%): {0.27*E_3plus1D:.3e} J")
    print(f"    3+1D's DE (68%): {0.68*E_3plus1D:.3e} J")
    print()
    print(f"    2D's total: per SN-scale event, M_2D_peak ~ 2e9 * M_event")
    print(f"    (2D is a child universe, energy scales per event)")

    # Summary
    hr()
    print("SUMMARY")
    hr()
    print(f"\n  User's question: 'doesn't 5D give 4D DE, and gain DM from 4D?'")
    print()
    print(f"  YES, exactly. Per parent-child DM symmetry (corrected):")
    print(f"    - 5D's antigravity (in 4D frame) = 4D's DE")
    print(f"    - 4D's attractive (in 5D frame) = 5D's DM")
    print()
    print(f"  In Cone 2 (5D->4D->3+1D->2D), every level has:")
    print(f"    - DM from children (back-projection)")
    print(f"    - DE from parent (antigravity projection)")
    print(f"    - m = intrinsic content")
    print()
    print(f"  Top level (5D): no parent, so DE = 5D's own vacuum (no source)")
    print(f"  Bottom level (2D): no children, so DM = 0 (no back-projection)")
    print()
    print(f"  Cone 2 is more 'complete' than Cone 1 (every level has DE source).")
    print(f"  But Cone 1 is more parsimonious (1 parameter vs 2).")
    print()
    print(f"  The cascade's derivation (commit 76) prefers Cone 1 (parsimony).")
    print(f"  But Cone 2 has merit (completeness, every level has DE source).")
    print()
    print(f"  Status: Cone 2 is a valid alternative. The choice is a")
    print(f"  theoretical preference, not derivable from cascade alone.")


if __name__ == "__main__":
    main()
