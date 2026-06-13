#!/usr/bin/env python3
"""
Cone-shape: 4D's m/DM/DE ratio (and asymmetry across levels)

Question: in cone-shape, does 4D have a 5/27/68 split?

The answer is NO, not in 4D's own frame. The cone-shape implies
an ASYMMETRIC structure across levels:

  - 4D (top, no parent, has child 3+1D): 32/68 only
    * 4D's frame: 32% energetic / 68% vacuum
    * No 5/27 split (4D has no children to back-project as DM)
    * 4D's "DM" doesn't exist in the usual sense

  - 3+1D (middle, has parent 4D, has children 2D): 5/27/68
    * 3+1D's frame: 5% matter / 27% DM (from 2D back-projection) / 68% DE
    * The 5/27 split EMERGES because 3+1D has 2D children

  - 2D (bottom, has parent 3+1D, no children): 32/68 (or 5/27/68?)
    * 2D's frame: depends on interpretation
    * 2D has no children, so 2D's "27% DM" is INTERNAL
    * Best interpretation: 2D's "DM" is 3+1D's antigravity in 2D's frame
      (parent-child DM symmetry)

So the cone-shape is INHOMOGENEOUS:
  - Top level (4D): 32/68, no DM
  - Middle level (3+1D): 5/27/68, full 3-way
  - Bottom level (2D): 32/68 (or 5/27/68 with internal-DM interpretation)

The cascade's "universal 5/27/68" is really:
  - Universal 32/68 outer split (cascade-derived, applies at all levels)
  - 5/27 inner split only at levels that have children (3+1D, possibly 2D)
  - Top level (4D) has no 5/27 split

This script computes the asymmetry explicitly.
"""

import math
import sys
sys.path.insert(0, ".")
sys.path.insert(0, "calculations")

from cascade_model import Constants, CascadeParams, our_3plus1d_universe


def hr(ch="="):
    print()
    print(ch * 78)
    print(ch * 78)


def main():
    hr()
    print("CONE-SHAPE: 4D'S M/DM/DE RATIO (AND ASYMMETRY ACROSS LEVELS)")
    hr()

    print(f"\n  Step 1: Recall the cone-shape structure")
    print(f"  ----------------------------------------------------------------")
    print(f"  Cone-shaped cascade (3 levels, depth=2):")
    print(f"    Level 0: 4D event (top, no parent)")
    print(f"    Level 1: 3+1D universe (middle, has parent 4D, has children 2D)")
    print(f"    Level 2: 2D universes (bottom, has parent 3+1D, no children)")
    print()
    print(f"  Question: what is each level's m/DM/DE ratio?")

    print(f"\n\n  Step 2: 4D event's m/DM/DE (in 4D's frame)")
    print(f"  ----------------------------------------------------------------")
    print(f"  4D is at the TOP of the cone. It has:")
    print(f"    - No PARENT (nothing to back-project from)")
    print(f"    - One CHILD: 3+1D universe")
    print()
    print(f"  In 4D's frame, the cascade's universal-split gives:")
    print(f"    4D energetic: 32% (projects DOWN to 3+1D as our universe)")
    print(f"    4D vacuum: 68% (projects DOWN to 3+1D as our DE)")
    print()
    print(f"  But what is 4D's 'DM'?")
    print(f"  - DM = back-projection of CHILDREN universes")
    print(f"  - 4D's only child is 3+1D (us)")
    print(f"  - 3+1D's attractive gravity projected UP to 4D = 4D's 'DM'")
    print(f"  - But 4D's 'frame' is not a universe frame (it's the parent)")
    print()
    print(f"  The question: in cone-shape, does 4D have 'DM' in the same sense?")
    print()
    print(f"  Answer: NO. 4D's frame is the parent frame, not a child universe.")
    print(f"  The 'DM' concept only makes sense for a UNIVERSE (a child),")
    print(f"  not for a parent event.")
    print()
    print(f"  So 4D's m/DM/DE in 4D's own frame is just 32/68:")
    print(f"    4D: 32% energetic / 68% vacuum / 0% DM (no DM in 4D's frame)")

    print(f"\n\n  Step 3: 3+1D's m/DM/DE (in 3+1D's frame, observed)")
    print(f"  ----------------------------------------------------------------")
    print(f"  3+1D is in the MIDDLE of the cone. It has:")
    print(f"    - PARENT: 4D event (provides DE)")
    print(f"    - CHILDREN: 2D universes (provide DM)")
    print()
    print(f"  In 3+1D's frame:")
    print(f"    3+1D matter: 5% (the 4D event's direct projection)")
    print(f"    3+1D DM: 27% (back-projection of 2D universe attractive gravity)")
    print(f"    3+1D DE: 68% (the 4D event's antigravity)")
    print()
    print(f"  This is the OBSERVED 5/27/68 split (Planck 2018).")
    print(f"  Status: 3+1D is the only level with the FULL 3-way split.")

    print(f"\n\n  Step 4: 2D's m/DM/DE (in 2D's frame)")
    print(f"  ----------------------------------------------------------------")
    print(f"  2D is at the BOTTOM of the cone (terminal). It has:")
    print(f"    - PARENT: 3+1D event (provides 2D's DE)")
    print(f"    - NO CHILDREN (cone terminates)")
    print()
    print(f"  In 2D's frame, the cascade's universal-split:")
    print(f"    2D energetic: 32%")
    print(f"    2D vacuum: 68%")
    print()
    print(f"  What is 2D's 'DM'?")
    print(f"  - DM = back-projection of CHILDREN universes")
    print(f"  - 2D has no children (cone terminates)")
    print(f"  - So 2D has NO DM in the usual sense")
    print()
    print(f"  Possibility A: 2D's 'DM' is INTERNAL self-attraction residue")
    print(f"    - 2D universe has its own self-gravity (after bulk-brane cancellation)")
    print(f"    - 27% of 2D's mass-energy is this self-gravity")
    print(f"    - This is INTERNAL to 2D, not from children")
    print()
    print(f"  Possibility B: 2D has no DM, just matter + DE")
    print(f"    - 2D's energetic 32% is all 'matter' (5% + 27% = 32%)")
    print(f"    - The 5/27 split is meaningless at 2D level")
    print(f"    - 2D is just 32% matter / 68% vacuum")
    print()
    print(f"  Possibility C: 2D's '27% DM' is parent's antigravity (parent-child DM)")
    print(f"    - 3+1D event's antigravity projects to 2D")
    print(f"    - In 2D's frame, this is perceived as 2D's 'DM'")
    print(f"    - Symmetric to: 2D's attractive gravity projects UP to 3+1D as our DM")
    print()
    print(f"  Per cascade, Possibility C is the parent-child DM symmetry.")
    print(f"  So 2D's frame: 5% matter / 27% 'DM' (parent's antigravity) / 68% DE")

    # Compute the asymmetry
    print(f"\n\n  Step 5: The asymmetry across levels")
    print(f"  ----------------------------------------------------------------")
    print(f"  {'Level':>10} | {'Has parent':>12} | {'Has children':>14} | {'m/DM/DE':>20} | {'5/27 split?':>15}")
    print(f"  {'-'*10} | {'-'*12} | {'-'*14} | {'-'*20} | {'-'*15}")
    print(f"  {'4D':>10} | {'NO':>12} | {'YES (3+1D)':>14} | {'32/0/68':>20} | {'NO (no children)':>15}")
    print(f"  {'3+1D':>10} | {'YES (4D)':>12} | {'YES (2D)':>14} | {'5/27/68':>20} | {'YES':>15}")
    print(f"  {'2D':>10} | {'YES (3+1D)':>12} | {'NO (terminal)':>14} | {'5/27/68*':>20} | {'YES (parent)':>15}")
    print()
    print(f"  * 2D's '27% DM' is the parent's antigravity in 2D's frame (parent-child DM symmetry).")
    print(f"  In cone-shape, 2D's 'DM' is NOT from children (which don't exist).")
    print()
    print(f"  The asymmetry: only the MIDDLE level (3+1D) has a 'true' 3-way split,")
    print(f"  with DM coming from CHILDREN (2D back-projection).")
    print(f"  Top (4D) and bottom (2D) have DM coming from PARENT (or none).")

    print(f"\n\n  Step 6: 4D's specific m/DM/DE ratio")
    print(f"  ----------------------------------------------------------------")
    print(f"  In 4D's frame, the cascade's universal-split gives:")
    print(f"    4D: 32% energetic / 68% vacuum")
    print(f"  There's no separate 'matter' and 'DM' distinction in 4D's frame")
    print(f"  because 4D has no children to back-project.")
    print()
    print(f"  When 4D's 32% projects DOWN to 3+1D:")
    print(f"    - 5% becomes 3+1D's ordinary matter (direct projection)")
    print(f"    - 27% becomes 3+1D's DM (via 2D back-projection)")
    print()
    print(f"  The 5/27 split EMERGES from how 4D's 32% projects to 3+1D.")
    print(f"  It's not a feature of 4D's own frame.")
    print()
    print(f"  In 4D's frame: 32/68 (no 5/27, no DM)")
    print(f"  In 3+1D's frame: 5/27/68 (5/27 emerges from 2D children)")
    print()
    print(f"  So 4D's m/DM/DE ratio IS different from 3+1D's!")
    print(f"  4D doesn't have a 5/27/68 split in its own frame.")
    print(f"  It only has 32/68.")

    print(f"\n\n  Step 7: Implications for the cascade's 'universal split'")
    print(f"  ----------------------------------------------------------------")
    print(f"  The cascade POSTULATES a universal 5/27/68 split at all levels.")
    print(f"  But: in cone-shape, this postulate is INCONSISTENT with the structure.")
    print()
    print(f"  Refined postulate: 'universal 32/68 OUTER split'")
    print(f"    - All levels have 32% energetic / 68% vacuum")
    print(f"    - This IS universal (cascade-derived)")
    print()
    print(f"  NOT universal: '5/27 INNER split'")
    print(f"    - Only levels with CHILDREN have a meaningful 5/27 split")
    print(f"    - Top level (4D, no parent) and bottom level (2D, no children) have")
    print(f"      different inner splits")
    print(f"    - The 5/27 inner split is a property of the parent-child geometry,")
    print(f"      not a universal 4D event parameter")
    print()
    print(f"  This is a more honest cascade:")
    print(f"    - Universal: 32/68 (cascade-derived)")
    print(f"    - Level-specific: 5/27 (depends on parent/children structure)")

    print(f"\n\n  Step 8: What does this mean for our universe's 5/27/68?")
    print(f"  ----------------------------------------------------------------")
    print(f"  In our 3+1D universe, 5/27/68 is observed.")
    print(f"  This is because 3+1D has children (2D) that provide DM via back-projection.")
    print()
    print(f"  The 5/27 ratio depends on:")
    print(f"    - 3+1D's children (2D universes) - their rate, energy, lifetime")
    print(f"    - The back-projection efficiency (1/G_2D per cascade)")
    print()
    print(f"  Different 3+1D universes (from different 4D events) could have")
    print(f"  different 5/27 ratios, depending on their specific 2D universe population.")
    print()
    print(f"  So the 5/27 ratio is a property of the SPECIFIC 3+1D universe,")
    print(f"  not a universal cascade parameter.")
    print()
    print(f"  This is consistent with the cone-shape refinement:")
    print(f"    - 32/68 universal: cascade-derived")
    print(f"    - 5/27 specific to level: depends on local structure")

    # Numerical estimates
    print(f"\n\n  Step 9: Numerical estimates of 4D vs 3+1D vs 2D budgets")
    print(f"  ----------------------------------------------------------------")
    rho_c = 8.5e-27  # kg/m^3
    c = Constants.c
    R_observable = 4.4e26  # m
    V_observable = (4/3) * math.pi * R_observable**3
    E_3plus1D_observable = rho_c * c**2 * V_observable
    E_4D = E_3plus1D_observable / 0.32
    
    print(f"  Energy budgets (cone-shape):")
    print(f"    4D total:           E_4D = {E_4D:.3e} J")
    print(f"    4D energetic (32%): {0.32*E_4D:.3e} J")
    print(f"    4D vacuum (68%):    {0.68*E_4D:.3e} J")
    print(f"    [No 5/27 split in 4D's frame]")
    print()
    print(f"    3+1D total (obs):   E_3plus1D = {E_3plus1D_observable:.3e} J (= 4D's 32% projection)")
    print(f"    3+1D matter (5%):   {0.05*E_3plus1D_observable:.3e} J")
    print(f"    3+1D DM (27%):      {0.27*E_3plus1D_observable:.3e} J")
    print(f"    3+1D DE (68%):      {0.68*E_3plus1D_observable:.3e} J (= 4D's 68% projection)")
    print()
    print(f"  Mass-equivalent (dividing by c^2):")
    print(f"    M_4D = {E_4D/c**2:.3e} kg (~3x our universe's mass)")
    print(f"    M_3plus1D = {E_3plus1D_observable/c**2:.3e} kg")
    print(f"    M_3plus1D_matter = {0.05*E_3plus1D_observable/c**2:.3e} kg")
    print(f"    M_3plus1D_DM = {0.27*E_3plus1D_observable/c**2:.3e} kg")
    print()
    print(f"  2D universe (per SN-scale event, in 2D's frame):")
    E_SN = 1.6e41  # J (typical SN)
    G_2D = 1.03e10  # from GrowthFactorCalculator
    M_2D_peak = 20 * G_2D * (E_SN / c**2)
    print(f"    M_2D_peak (5% of which is original event):")
    print(f"      M_2D_peak = 20 * G_2D * M_event = 2.06e11 * M_event")
    print(f"      = 2.06e11 * {E_SN/c**2:.3e} kg = {M_2D_peak:.3e} kg")
    print(f"    Within M_2D_peak:")
    print(f"      M_2D_o (5%): {0.05*M_2D_peak:.3e} kg (= M_event)")
    print(f"      M_2D_DM (27%): {0.27*M_2D_peak:.3e} kg (= 5.4 * M_event)")
    print(f"      M_2D_DE (68%): {0.68*M_2D_peak:.3e} kg (= 13.6 * M_event)")
    print(f"    [Cone-shape: 2D's 27% 'DM' is parent's antigravity in 2D frame]")

    # Summary
    hr()
    print("SUMMARY")
    hr()
    print(f"\n  Cone-shape implies ASYMMETRY across levels:")
    print(f"    4D:    32/68 (no DM, no 5/27 in 4D's frame)")
    print(f"    3+1D:  5/27/68 (full 3-way, DM from 2D children)")
    print(f"    2D:    5/27/68 (full 3-way, but '27% DM' is parent's antigravity)")
    print()
    print(f"  What IS universal in cone-shape:")
    print(f"    - 32/68 OUTER split (energetic vs vacuum)")
    print(f"    - Cascade-derived from dimensional-projection kinematics")
    print()
    print(f"  What is NOT universal:")
    print(f"    - 5/27 INNER split (depends on level's children/parent structure)")
    print(f"    - Top level (4D) has no DM, no 5/27")
    print(f"    - Bottom level (2D) has 'DM' from parent, not children")
    print()
    print(f"  This refines the universal-split postulate:")
    print(f"    OLD: 5/27/68 universal at all levels")
    print(f"    NEW: 32/68 universal; 5/27 is level-specific (depends on structure)")
    print()
    print(f"  4D's m/DM/DE ratio is DIFFERENT from 3+1D's:")
    print(f"    4D has 32/68 (no 5/27, no DM in 4D's frame)")
    print(f"    3+1D has 5/27/68 (the OBSERVED ratio)")
    print()
    print(f"  The 5/27 split in 3+1D is a property of 3+1D's specific structure")
    print(f"  (its 2D universe population), not a universal cascade parameter.")


if __name__ == "__main__":
    main()
