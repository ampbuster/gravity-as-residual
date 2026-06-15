#!/usr/bin/env python3
"""
v27_kaluza_klein.py
====================

Test: Does Kaluza-Klein (1921) original 5D unification give the cascade's
4D → 3+1D dimensional projection structure?

Kaluza (1921) + Klein (1926): the original 5D unification of gravity and
electromagnetism. Key idea:
  - Start with 5D spacetime (4 space + 1 time, or 3 space + 1 time + 1 extra)
  - 5D metric G_MN (M, N = 0,1,2,3,4)
  - 5D Einstein-Hilbert action
  - Compactify 1 extra dimension on a circle S^1 of radius R
  - The 5D metric decomposes into:
    * g_μν (4D graviton, 10 components)
    * A_μ = G_μ4 (4D gauge field, 4 components = EM vector potential)
    * φ = G_44 (4D scalar = dilaton, 1 component)
  - 5D gravity → 4D gravity + EM + dilaton

So KK is a 5D → 4D reduction that gives 4D gravity, 4D EM, and a dilaton.

Application to the cascade:
- Cascade is 4D event → 3+1D us → 2D children
- KK is 5D → 4D us (+ EM + dilaton)
- Question: Can the cascade's 4D → 3+1D projection be modeled as a
  KK-style compactification?

Test 1: KK's 5D → 4D structure vs cascade's 4D → 3+1D structure.

KK's structure:
  - 5D bulk (4+1)
  - 1 compact dimension (circle S^1 of radius R)
  - 4D effective theory on the brane (after KK reduction)
  - Effective 4D action: 4D gravity + EM + dilaton

Cascade's structure:
  - 4D "event" (parent)
  - 3+1D "us" (child)
  - 1 "extra" dimension (compact? extended? cascade says spatially extended)
  - Effective 3+1D theory: SM + gravity + (cascade's 2D children)

Structural match: PARTIAL. Both are dimensional reductions, but:
- KK's extra dim is COMPACT (circle S^1)
- Cascade's "4D event" is SPATIALLY EXTENDED (per §2.4)
- KK gives 4D gravity + EM + dilaton
- Cascade's 4D → 3+1D gives 3+1D gravity + SM (per cascade, the 2D children
  are not from the projection but from energetic events)

Test 2: KK gravity weakening.

KK's 5D Planck mass M_5 is related to 4D Newton constant G_4 by
  G_4 = G_5 / (2π R)  [in KK units, R = compactification radius]
So G_4 is WEAKER than G_5 (by factor 1/R, the compactification volume).

Cascade's gravity weakening:
- 4D gravity is G_4
- 3+1D gravity is G_3+1D << G_4
- Weakening by factor f_split ~ 32/68 = 0.47 (from 5/27/68 ratio)

Both have gravity weakening, but:
- KK's weakening is from COMPACTIFICATION (factor 1/V_extra)
- Cascade's weakening is from 4D event → 3+1D projection (factor f_split)

Structural match: PARTIAL. The cascade's f_split is NOT 1/(2πR); it's
a separate number.

Test 3: KK's gauge field from metric.

KK's beautiful result: the 5D metric G_μ4 (off-diagonal component) becomes
the 4D EM vector potential A_μ. The 5D Einstein equations give 4D Einstein
equations + 4D Maxwell equations.

Cascade's analog: does the cascade's 4D event → 3+1D projection give
SM forces from higher-D geometry?

The cascade does NOT claim this. The cascade takes the SM as given and
focuses on DM/DE/gravity. The 4D → 3+1D projection gives:
- 3+1D gravity (weakened)
- 3+1D SM (assumed given, not derived)
- 3+1D DE (from inverted 4D gravity)
- 3+1D DM (from 2D universe back-projection)

So the cascade's 4D → 3+1D is DIFFERENT from KK's 5D → 4D:
- KK derives EM from geometry
- Cascade doesn't derive SM from geometry (it assumes SM is given)

Test 4: KK inversion.

KK's projection: 5D gravity → 4D gravity + EM + dilaton. The 4D gravity
is ATTRACTIVE (standard). The dilaton is a scalar with specific potential.

Cascade's projection: 4D gravity → 3+1D gravity + 2D universes. The
3+1D gravity is ATTRACTIVE (cascade agrees). The "2D universe back-
projection" is the inversion-like effect (cascade's DE = inverted 4D
gravity, separate from 2D universes).

KK does NOT have a sign-change mechanism. KK's 4D gravity is attractive,
same as 5D gravity (just weaker). The cascade's INVERSION is NOT
present in KK.

Test 5: KK's compactification scale.

KK's compactification radius R is a free parameter. For KK to give
4D gravity of the right strength, R is fixed:
  R = ℏ / (M_Pl c) × (1 / √(α_EM × something))
Actually, R is set by the 5D Planck mass M_5.

For the cascade, the "compactification scale" is replaced by the "4D
event's spatial extent". Cascade says the 4D event is SPATIALLY EXTENDED
(not compact), with spatial extent ~ c τ_4D where τ_4D ~ 10^28 yr
(per Padmanabhan calculation in §3.8.2).

Structural difference: KK has compact extra dim, cascade has extended
parent dimension.

Verdict:
- KK is a STRUCTURAL PROTOTYPE for dimensional reduction, but differs
  significantly from the cascade's 4D event → 3+1D structure
- KK does NOT derive the cascade's α = 1.29, f_split, f_back, or the
  inversion
- KK's compactification is different from cascade's spatially extended
  parent
- KK's beautiful result (EM from geometry) is NOT replicated in the
  cascade (cascade assumes SM is given)

KK is a HISTORICAL PROTOTYPE for dimensional reduction, not a derivation
of the cascade. The cascade's 4D event → 3+1D is a generalization of
KK's 5D → 4D, with different assumptions and different outputs.
"""
import numpy as np
import json

# Constants
c = 2.998e8
hbar = 1.055e-34
G = 6.674e-11
k_B = 1.381e-23
l_P = np.sqrt(hbar * G / c**3)
t_P = l_P / c
M_P = np.sqrt(hbar * c / G)
M_sun = 1.989e30
yr = 3.156e7
e = 1.602e-19  # C, electron charge
epsilon_0 = 8.854e-12  # F/m

print("=" * 70)
print("KALUZA-KLEIN (1921) 5D UNIFICATION vs CASCADE")
print("=" * 70)
print()
print("KK: 5D → 4D reduction via S^1 compactification")
print("  - 5D Einstein-Hilbert → 4D gravity + EM + dilaton")
print("  - Off-diagonal metric G_μ4 = EM vector potential A_μ")
print()

print("=" * 70)
print("TEST 1: Structural match (KK 5D→4D vs cascade 4D→3+1D)")
print("=" * 70)
print()
print("KK:")
print("  - 5D bulk (4+1)")
print("  - 1 compact dim (S^1 of radius R)")
print("  - 4D effective theory: gravity + EM + dilaton")
print()
print("Cascade:")
print("  - 4D 'event' (parent, spatially extended)")
print("  - 3+1D 'us' (child brane)")
print("  - 3+1D effective theory: gravity + SM + DE + DM")
print()
print("Structural match: PARTIAL. Both are dimensional reductions, but")
print("KK's extra dim is COMPACT, cascade's 4D event is SPATIALLY EXTENDED.")
print()

print("=" * 70)
print("TEST 2: Gravity weakening")
print("=" * 70)
print()
print("KK: G_4 = G_5 / (2π R)")
print("  - G_4 weakened by factor 1/(2πR) (compactification volume)")
print()
print("Cascade: G_3+1D = f_split × G_4 with f_split = 32/68 = 0.47")
print("  - G_3+1D weakened by factor 0.47 (5/27/68 ratio)")
print()
print("Both have gravity weakening, but:")
print("  - KK: factor 1/(2πR) is COMPACTIFICATION-GEOMETRIC")
print("  - Cascade: factor 0.47 is EMPIRICAL (from 5/27/68)")
print()
print("Verdict: STRUCTURAL MATCH. Both have gravity weakening, but the")
print("specific factors are different (geometric vs empirical).")
print()

print("=" * 70)
print("TEST 3: SM forces from geometry (KK vs cascade)")
print("=" * 70)
print()
print("KK's beautiful result: 5D Einstein equations → 4D Einstein + 4D Maxwell")
print("  - EM is derived from off-diagonal metric G_μ4")
print("  - 4D gauge symmetry from 5D coordinate invariance")
print()
print("Cascade: 3+1D SM is ASSUMED, not derived")
print("  - Cascade focuses on DM/DE/gravity")
print("  - SM is taken as given (the cascade doesn't derive it from geometry)")
print()
print("Verdict: KK derives EM from geometry; cascade does NOT derive SM from")
print("geometry. This is a STRUCTURAL DIFFERENCE between the two.")
print()

print("=" * 70)
print("TEST 4: KK's compactification scale vs cascade's 4D event extent")
print("=" * 70)
print()
print("KK: extra dim is COMPACT, R is a free parameter")
print("  - If we want standard EM coupling, R is set by M_5")
print("  - Typical: R ~ 10^-30 m (way below experimental reach)")
print()
print("Cascade: 4D event is SPATIALLY EXTENDED")
print("  - Extent ~ c τ_4D ~ 10^28 yr × c = 10^36 m (per Padmanabhan §3.8.2)")
print("  - This is MUCH LARGER than the observable universe (10^26 m)")
print()
print("Verdict: STRUCTURAL DIFFERENCE. KK has compact extra dim, cascade has")
print("spatially extended parent. Different scales, different physics.")
print()

print("=" * 70)
print("TEST 5: Inversion (cascade-specific, not in KK)")
print("=" * 70)
print()
print("KK: 5D gravity → 4D gravity (no sign change)")
print("  - 4D gravity is attractive (standard GR)")
print("  - KK preserves the sign of gravity")
print()
print("Cascade: 4D gravity → 3+1D gravity + 3+1D DE (with sign change for DE)")
print("  - 3+1D gravity is attractive (cascade agrees)")
print("  - DE = inverted 4D gravity (repulsive in 3+1D)")
print()
print("Verdict: KK does NOT have a sign-change mechanism. The cascade's")
print("INVERSION is a cascade-specific POSTULATE, not from KK.")
print()

print("=" * 70)
print("SUMMARY: Kaluza-Klein (1921) vs Cascade")
print("=" * 70)
print()
print("✓ STRUCTURAL PROTOTYPE: KK is the original dimensional reduction,")
print("  cascade is a generalization (4D → 3+1D instead of 5D → 4D)")
print()
print("△ PARTIAL MATCH: gravity weakening in both (KK: 1/R, cascade: 0.47)")
print()
print("✗ STRUCTURAL DIFFERENCE: KK derives EM from geometry, cascade does")
print("  NOT derive SM from geometry")
print()
print("✗ NO INVERSION: KK has no sign-change mechanism; cascade's inversion")
print("  is a separate postulate")
print()
print("✗ DIFFERENT SCALES: KK's extra dim is compact (R ~ 10^-30 m),")
print("  cascade's 4D event is spatially extended (~ 10^36 m)")
print()
print("KK is a HISTORICAL PROTOTYPE for dimensional reduction, not a")
print("derivation of the cascade. The cascade's 4D event → 3+1D is a")
print("generalization of KK's 5D → 4D, with different assumptions.")

results = {
    "test": "Kaluza-Klein (1921) 5D unification vs cascade 4D → 3+1D structure",
    "KK_formula": "G_4 = G_5 / (2π R), with R = compactification radius",
    "KK_features": {
        "extra_dim": "COMPACT (S^1 of radius R)",
        "EM_derivation": "From off-diagonal metric G_μ4",
        "gravity_weakening": "By factor 1/(2πR)",
        "sign_change": "NO (4D gravity attractive)",
    },
    "cascade_features": {
        "extra_dim": "SPATIALLY EXTENDED (4D event, extent ~ 10^36 m)",
        "SM_derivation": "NOT derived (assumed given)",
        "gravity_weakening": "By factor 0.47 (empirical 5/27/68)",
        "sign_change": "YES (cascade DE = inverted 4D gravity)",
    },
    "verdict": {
        "structural_prototype": True,
        "cascade_generalization": True,
        "EM_derivation_in_cascade": False,
        "inversion_in_KK": False,
        "scales_different": True,
    },
    "conclusion": "KK is the historical prototype for dimensional reduction, but the cascade's 4D event → 3+1D differs significantly: extended (not compact), no SM derivation, has inversion. KK is a useful framing reference, not a derivation."
}

with open('/workspace/github-repo/calculations/v27_kaluza_klein_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print()
print("Results saved to calculations/v27_kaluza_klein_results.json")
