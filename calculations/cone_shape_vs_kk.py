#!/usr/bin/env python3
"""
Cone-shape and Kaluza-Klein: are they the same thing?

Kaluza-Klein (KK) theory:
  - Extra dimensions are 'compactified' (rolled up small)
  - Standard Model + gravity in higher-D unifies forces
  - Extra dimensions have a 'compactification radius' R_KK
  - Particles have KK modes with mass m_n ~ n / R_KK

The cone-shape cascade:
  - Hierarchy: 4D event -> 3+1D universe -> 2D universes (terminal)
  - Each level has its own 'dimension'
  - Lower levels are 'nested' within higher levels (like KK)
  - But: lower levels have their OWN physics, not KK modes of higher-D

This script explores the relationship: is the cascade KK? Is it a
novel brane-world? Or something else?

Key differences:
  1. KK has continuous extra dim; cone has DISCRETE hierarchy
  2. KK extra dim is SPATIAL; cone lower levels are FULL UNIVERSES (with time)
  3. KK has infinite tower of modes; cone has TERMINAL 2 levels
  4. KK modes are vibrations; cone 'modes' (2D universes) are CREATIONS from events
  5. KK modes have infinite lifetime; cone modes have FINITE lifetime (33s for SN)

Similarities:
  1. Both have extra 'dimensions' (cone: lower-D universes; KK: compactified dims)
  2. Both have hierarchical structure
  3. Both embed higher-D physics into lower-D observations
  4. Both have a 'compactification scale' (cone: time-dilation; KK: R_KK)

Conclusion: cone-shape is INSPIRED by KK-like ideas but is a SPECIFIC
brane-world realization. It's not standard KK, but it's "KK-flavored"
with some unique features (cone termination, parent-child DM symmetry).
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
    print("CONE-SHAPE AND KALUZA-KLEIN: ARE THEY THE SAME?")
    hr()

    print(f"\n  Step 1: Recall KK theory basics")
    print(f"  ----------------------------------------------------------------")
    print(f"  Kaluza-Klein (KK) theory:")
    print(f"    - Extra dimensions are 'compactified' (rolled up small)")
    print(f"    - In (4+1)D: 1 extra spatial dim, compactified on circle S^1 of radius R")
    print(f"    - Particles have KK modes with mass m_n = n/R (n = 0, 1, 2, ...)")
    print(f"    - Modes are 'vibrations' of the extra dim")
    print(f"    - Infinite tower of states (n=0, 1, 2, ...)")
    print()
    print(f"  Examples:")
    print(f"    - Standard KK: extra dim at Planck scale, modes at M_Pl ~ 1e19 GeV")
    print(f"    - ADD (Arkani-Hamed et al.): n extra dims at ~mm, modes at ~TeV")
    print(f"    - RS (Randall-Sundrum): warped extra dim, modes at ~TeV")

    print(f"\n\n  Step 2: Recall the cone-shape cascade")
    print(f"  ----------------------------------------------------------------")
    print(f"  Cone-shape (per commit 67-68):")
    print(f"    - Hierarchy: 4D event -> 3+1D universe -> 2D universes (terminal)")
    print(f"    - 2 levels of cascade (depth = 2)")
    print(f"    - Each level has its own 'dimension' and physics")
    print(f"    - Lower levels are 'created' by energetic events in higher levels")
    print(f"    - 2D universes are 'terminal' (no further cascade)")
    print()
    print(f"  Examples:")
    print(f"    - 2D universe from SN: lifetime 33 s in 3+1D frame, M_2D_peak ~ 2e9 * M_SN")
    print(f"    - 2D universe from LHC: lifetime 3e-24 s, M_2D_peak ~ 2e9 * M_LHC")

    print(f"\n\n  Step 3: Comparing KK and cone-shape")
    print(f"  ----------------------------------------------------------------")
    print(f"  {'Feature':<35} | {'KK':>20} | {'Cone-shape':>20}")
    print(f"  {'-'*35} | {'-'*20} | {'-'*20}")
    print(f"  {'Extra structure':<35} | {'Compactified space':>20} | {'Hierarchy of universes':>20}")
    print(f"  {'Dim type':<35} | {'Spatial (continuous)':>20} | {'Spacetime (discrete)':>20}")
    print(f"  {'Levels':<35} | {'Infinite tower (n=0,1,2,...)':>20} | {'2 levels (terminal)':>20}")
    print(f"  {'Modes':<35} | {'Vibrations (Fourier)':>20} | {'Universe creations':>20}")
    print(f"  {'Mode lifetime':<35} | {'Infinite (stable)':>20} | {'Finite (e.g., 33s)':>20}")
    print(f"  {'Mode creation':<35} | {'Continuous (always)':>20} | {'Discrete (events)':>20}")
    print(f"  {'Compactification scale':<35} | {'R_KK (e.g., 1 mm)':>20} | {'Dimensional time-dilation':>20}")
    print(f"  {'Mass spectrum':<35} | {'m_n ~ n/R_KK':>20} | {'M_2D_peak (per event)':>20}")
    print(f"  {'Force unification':<35} | {'Yes (KK unifies)':>20} | {'No (just structure)':>20}")
    print(f"  {'Observable signature':<35} | {'KK mode particles':>20} | {'DM at galactic scales':>20}")

    print(f"\n\n  Step 4: Key differences")
    print(f"  ----------------------------------------------------------------")
    print(f"  1. KK: extra dim is SMOOTH (continuous topology)")
    print(f"     Cone: extra 'dim' is DISCRETE (each level is a separate universe)")
    print()
    print(f"  2. KK: extra dim is SPATIAL (just one more spatial dim)")
    print(f"     Cone: lower levels are FULL UNIVERSES (with their own time)")
    print()
    print(f"  3. KK: infinite tower of modes (n = 0, 1, 2, ...)")
    print(f"     Cone: 2 levels only (4D -> 3+1D -> 2D, terminal)")
    print()
    print(f"  4. KK: modes are vibrations (Fourier modes of extra dim)")
    print(f"     Cone: 'modes' are universe CREATIONS from energetic events")
    print()
    print(f"  5. KK: modes are stable (infinite lifetime in standard KK)")
    print(f"     Cone: 2D universes are TRANSIENT (lifetime 33s for SN-scale)")
    print()
    print(f"  6. KK: modes are always present (continuous Fourier expansion)")
    print(f"     Cone: 2D universes are CREATED by 3+1D events (discrete)")
    print()
    print(f"  7. KK: force unification (gravity + EM in 5D, etc.)")
    print(f"     Cone: no force unification (just structure)")
    print()
    print(f"  8. KK: observable as KK mode particles at colliders")
    print(f"     Cone: observable as DM at galactic scales")

    print(f"\n\n  Step 5: Key similarities")
    print(f"  ----------------------------------------------------------------")
    print(f"  1. Both have 'extra' structure beyond 3+1D")
    print(f"  2. Both have hierarchical structure")
    print(f"  3. Both embed higher-D physics into lower-D observations")
    print(f"  4. Both have a 'compactification scale' (KK: R_KK; cone: time-dilation)")
    print(f"  5. Both can be tested against observations")
    print(f"  6. Both are brane-world variants (3+1D brane in higher-D bulk)")

    print(f"\n\n  Step 6: Cone-shape as a SPECIFIC KK-like framework")
    print(f"  ----------------------------------------------------------------")
    print(f"  Cone-shape can be viewed as a NOVEL VARIANT of KK where:")
    print(f"    - The 'extra dim' is realized as a HIERARCHY of universes")
    print(f"    - The 'KK modes' are the 2D universe CREATIONS")
    print(f"    - The 'mode mass' is M_2D_peak (per event energy)")
    print(f"    - The 'mode lifetime' is tau_2D (dimensional time-dilation)")
    print(f"    - The 'KK tower' is discrete (one mode per 3+1D event)")
    print()
    print(f"  In this view, the cone-shape is:")
    print(f"    KK + discrete modes + transient modes + hierarchical structure")
    print()
    print(f"  This is a NON-STANDARD KK, but it's 'KK-flavored'.")
    print()
    print(f"  Specifically:")
    print(f"    - Standard KK: continuous spectrum, infinite tower, stable modes")
    print(f"    - Cone: discrete spectrum (per event), 2 levels, transient modes")
    print()
    print(f"  The cone-shape is a 'finite, transient, hierarchical' KK.")

    print(f"\n\n  Step 7: Are they the same thing?")
    print(f"  ----------------------------------------------------------------")
    print(f"  Strictly: NO, they are not the same.")
    print(f"    - KK is a continuous theory (smooth extra dim)")
    print(f"    - Cone is a discrete theory (discrete hierarchy of universes)")
    print(f"    - KK has infinite modes; cone has terminal 2 levels")
    print(f"    - KK unifies forces; cone doesn't")
    print()
    print(f"  But: cone-shape is INSPIRED by KK-like ideas and shares some features.")
    print(f"  The cascade is a 'brane-world with discrete, hierarchical modes'.")
    print()
    print(f"  More accurately: cone-shape is a BRANE-WORLD variant with KK flavor.")
    print(f"  It's not KK proper, but it's in the same 'family' of theories.")
    print()
    print(f"  Family tree:")
    print(f"    KK (1920s)")
    print(f"      -> ADD (1998, large extra dims)")
    print(f"      -> RS (1999, warped extra dims)")
    print(f"      -> Universal extra dims (UED)")
    print(f"      -> Cone-shape cascade (this paper, 2026)")

    print(f"\n\n  Step 8: Implications for the cascade's testable predictions")
    print(f"  ----------------------------------------------------------------")
    print(f"  If the cone is KK-like, its predictions overlap with KK:")
    print(f"    - Both predict 'extra' structure beyond 3+1D")
    print(f"    - Both can be tested via precision measurements")
    print()
    print(f"  But the cone makes DIFFERENT predictions:")
    print(f"    - KK: KK mode particles at colliders (m ~ TeV for ADD)")
    print(f"    - Cone: 2D universe back-projection as DM (cumulative effect)")
    print()
    print(f"  These are different signatures, distinguishable by experiment:")
    print(f"    - KK modes would show up in collider data (specific mass peaks)")
    print(f"    - Cone's 2D universes would NOT show up in collider data")
    print(f"      (they're 'absorbed' in 3+1D as DM, not as particles)")
    print()
    print(f"  So: cone is testable DIFFERENTLY from KK.")
    print(f"  If we see KK modes at colliders, cone is wrong (or cone is a sub-case of KK).")
    print(f"  If we DON'T see KK modes but see DM as predicted by cone, cone is favored.")

    print(f"\n\n  Step 9: What if cone-shape and KK are BOTH correct?")
    print(f"  ----------------------------------------------------------------")
    print(f"  A possibility: cone-shape is a SPECIFIC REALIZATION of KK where")
    print(f"  the 'extra dim' is realized as a discrete hierarchy of universes.")
    print()
    print(f"  In this hybrid view:")
    print(f"    - KK: the underlying framework (extra dim exists)")
    print(f"    - Cone: the specific realization (extra dim is discrete hierarchy)")
    print()
    print(f"  This is like saying: 'there ARE extra dimensions, but they're not")
    print(f"  smooth circles - they're discrete hierarchies of universes.'")
    print()
    print(f"  In this view, cone-shape IS a variant of KK, just one with")
    print(f"  discrete (not continuous) extra structure.")
    print()
    print(f"  Testable signature: the 'KK modes' would be the 2D universe")
    print(f"  CREATIONS, with specific masses M_2D_peak and lifetimes tau_2D.")
    print(f"  These are different from standard KK mode predictions.")
    print()
    print(f"  Status: cone-shape is a NON-STANDARD but KK-INSPIRED framework.")

    print(f"\n\n  Step 10: Honest assessment")
    print(f"  ----------------------------------------------------------------")
    print(f"  Question: is cone-shape the same as KK?")
    print(f"  Honest answer: NO, not the same. But RELATED.")
    print()
    print(f"  Cone-shape is a SPECIFIC BRANE-WORLD variant that:")
    print(f"    - Has KK-like features (extra structure, hierarchical, testable)")
    print(f"    - Has UNIQUE features (cone termination, parent-child DM, discrete modes)")
    print(f"    - Is INSPIRED by KK ideas but is NOT standard KK")
    print()
    print(f"  The cone-shape says:")
    print(f"    'Extra dimensions exist, but they're not smooth circles.")
    print(f"     They're discrete hierarchies of universes with their own physics.")
    print(f"     Each level has its own dimensional structure and dynamics.")
    print(f"     The hierarchy TERMINATES at 2D (cone, not fractal).'")
    print()
    print(f"  This is a novel proposal. It could be right or wrong.")
    print(f"  The cascade is testable via DM observations (per Mechanism B/F).")
    print(f"  If those tests pass, the cone-shape is supported.")
    print(f"  If KK modes show up at colliders first, standard KK is favored.")
    print()
    print(f"  The two are not mutually exclusive: cone-shape could be")
    print(f"  a sub-case of a more general KK-like framework.")

    # Summary
    hr()
    print("SUMMARY")
    hr()
    print(f"\n  Cone-shape and KK: related but not the same.")
    print()
    print(f"  KK (Kaluza-Klein):")
    print(f"    - Continuous extra dim (smooth topology)")
    print(f"    - Infinite tower of modes (Fourier)")
    print(f"    - Stable modes (infinite lifetime)")
    print(f"    - Force unification (gravity + EM, etc.)")
    print(f"    - Observable: KK mode particles at colliders")
    print()
    print(f"  Cone-shape cascade:")
    print(f"    - Discrete hierarchy of universes")
    print(f"    - 2 levels (terminal)")
    print(f"    - Transient modes (finite lifetime, e.g., 33s for SN)")
    print(f"    - No force unification (just structure)")
    print(f"    - Observable: cumulative 2D back-projection as DM")
    print()
    print(f"  What they share:")
    print(f"    - Both have 'extra' structure beyond 3+1D")
    print(f"    - Both have hierarchical structure")
    print(f"    - Both are brane-world variants")
    print(f"    - Both are testable")
    print()
    print(f"  Key insight: the cascade is a 'KK-flavored' brane-world, not KK proper.")
    print(f"  It can be viewed as a 'finite, transient, hierarchical' KK variant.")
    print(f"  Or as a 'discrete-mode brane-world' inspired by KK ideas.")
    print()
    print(f"  Status: cone-shape is a novel brane-world proposal, RELATED to KK")
    print(f"  but with its own unique features. It is testable differently from")
    print(f"  standard KK (DM at galactic scales vs KK modes at colliders).")


if __name__ == "__main__":
    main()
