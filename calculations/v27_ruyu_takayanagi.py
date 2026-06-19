#!/usr/bin/env python3
"""
v27_ruyu_takayanagi.py
========================

Test: Does the Ryu-Takayanagi (2006) holographic entanglement entropy formula
give the cascade's 2D universe back-projection structure?

RT formula (Ryu 2006, Takayanagi 2006, hub-hep-th/0603001):
  S_A = Area(γ_A) / (4 G_N)
where γ_A is the minimal surface in the bulk that is homologous to the
boundary region A. This is the holographic entanglement entropy formula
in AdS/CFT.

Application to the cascade:
- 3+1D brane = boundary (our observable universe)
- 4D bulk = AdS_5 bulk
- 2D universes in the 4D bulk = "branes" (in the bulk) with area A_2D
- Cascade DM = 2D universe back-projection = the holographic entanglement
  entropy of the bulk region bounded by 2D universes

Question: Does the RT formula give the cascade's
- 2D universe back-projection = DM ?
- f_DE ~ 10^-85 back-projection efficiency ?
- Inversion (4D attractive → 3+1D repulsive) ?

Test 1: RT formula and 2D universe area.

For a 2D universe of lifetime τ_2D, the 2D universe's "boundary area" in
the 3+1D brane is
  A_2D = 4π (c τ_2D)² [2-sphere area in 3+1D, radius c τ_2D]

The RT formula gives the entanglement entropy:
  S_2D = A_2D / (4 l_P²) = 4π (c τ_2D)² / (4 l_P²) = π c² τ_2D² / l_P²

In natural units (c = ℏ = 1, l_P = 1):
  S_2D = π τ_2D²

For a 2D universe of lifetime τ_2D = 33 s (SN-calibrated):
  τ_2D_Pl = 33 / 5.39e-44 = 6.12e44 t_Pl
  S_2D = π (6.12e44)² = 1.18e90 (in natural units, dimensionless)

This is a HUGE entanglement entropy. The 2D universe is a "small" object
(in 2D), but its boundary in 3+1D is a 2-sphere of radius c τ_2D = 1e10 m,
which is much larger than the 2D universe's intrinsic size.

Test 2: Does this match the cascade's "f_DE ~ 10^-85"?

The cascade's f_back is the BACK-PROJECTION EFFICIENCY: the fraction of the
SN's energy that ends up in 2D universe gravity. If the 2D universe's
"holographic" content is its boundary area in 3+1D, then:

  M_2D_holo = S_2D × T_H = (π τ_2D² / l_P²) × (1 / (2π τ_2D))
            = τ_2D / (2 l_P²) = τ_2D / (2 G) [in natural units]

This is EXACTLY the same as Jacobson's first law! (M_2D = T × S = τ_2D / (2G))

So RT + Bekenstein-Hawking = Jacobson derivation. They all give the same
relation M_2D = τ_2D / (2G), not the cascade's power law.

Test 3: Does RT give the cascade's DM as missing bulk entanglement?

Yes, structurally: the cascade's DM = 2D universe back-projection, and the
RT formula gives the entanglement entropy of the bulk region. The 2D
universes' "area" in the bulk is the RT surface for the 3+1D boundary
region.

But this is a STRUCTURAL match, not a quantitative derivation. The
cascade's specific f_DE ~ 10^-85 is a SEPARATE input.

Test 4: Does RT give the inversion (4D attractive → 3+1D repulsive)?

No. RT is a formula for entanglement entropy; it doesn't predict sign
changes in the gravitational coupling. The cascade's inversion is a
SEPARATE POSTULATE, not derived from RT.

Test 5: Does RT give the cascade's f_split = 32/68 (5/27/68)?

No. The 5/27/68 split comes from observational data (Planck 2018), not
from RT. RT doesn't predict specific values for matter/energy fractions.

Quantitative check:
For the cascade's 2D universe of lifetime τ_2D, the RT formula gives
  S_2D = π τ_2D²
The first law gives
  M_2D = S_2D × T_H = π τ_2D² × 1/(2π τ_2D) = τ_2D / 2
(in Planck units, G=1)

So the holographic derivation gives M_2D = τ_2D / 2, the same as Jacobson.
This is the LINEAR scaling τ_2D = 2 M_2D.

Cascade's τ_2D = (M_2D)^1.29 × t_Pl is a power law, not linear.
RT does not derive α = 1.29.

Verdict:
- RT provides a STRUCTURAL match to the cascade's 2D universe back-projection
- RT does NOT derive α = 1.29, f_split, or the inversion
- RT + Bekenstein-Hawking + Jacobson all give the SAME linear τ_2D ~ M_2D
- The cascade's power law α = 1.29 is NOT from RT, it's a dynamical
  parameter set by the 2D universe formation physics (e.g., CGHS, D-brane)

The RT formula is most useful for the cascade as a *consistency check* on
the relationship between 2D universe area and 3+1D back-projection, not as
a derivation of the cascade's specific phenomenology.
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

# Cascade's SN calibration
tau_2D_SN = 33.0  # s
E_SN = 1e44       # J
M_SN_bary = 10 * M_sun

print("=" * 70)
print("RYU-TAKAYANAGI (2006) vs CASCADE")
print("=" * 70)
print()
print("RT formula: S_A = Area(γ_A) / (4 G_N)")
print("Cascade: 2D universe back-projection = DM (holographic bulk content)")
print()

print("=" * 70)
print("TEST 1: 2D universe's boundary area in 3+1D")
print("=" * 70)
print()
print("For a 2D universe of lifetime τ_2D:")
print("  Boundary in 3+1D: 2-sphere of radius c τ_2D")
print(f"  A_2D = 4π (c τ_2D)²")
print()

R_2D = c * tau_2D_SN  # 2D universe boundary radius in 3+1D
A_2D = 4 * np.pi * R_2D**2
print(f"For SN (τ_2D = {tau_2D_SN} s):")
print(f"  R_2D = c × τ_2D = {R_2D:.2e} m = {R_2D/9.461e15:.2e} light-years")
print(f"  A_2D = 4π R_2D² = {A_2D:.2e} m²")
print(f"  A_2D / l_P² = {A_2D / l_P**2:.2e}")
print()

# RT formula
S_2D = A_2D / (4 * l_P**2)
print(f"RT entanglement entropy: S_2D = A / (4 l_P²) = {S_2D:.2e}")
print()

print("=" * 70)
print("TEST 2: RT + first law = Jacobson derivation")
print("=" * 70)
print()
print("RT: S_2D = A / (4 G) = π (c τ_2D)² / l_P² [natural units: S_2D = π τ_2D²]")
print("Hawking temp: T_H = 1 / (2π τ_2D) [Unruh]")
print("First law: M_2D = T_H × S_2D = (1/(2π τ_2D)) × π τ_2D² = τ_2D / 2")
print()

# In Planck units
tau_2D_Pl = tau_2D_SN / t_P
M_2D_Pl = tau_2D_Pl / 2
M_2D_kg = M_2D_Pl * M_P

print(f"In Planck units: M_2D = τ_2D / 2")
print(f"  τ_2D(SN) = {tau_2D_Pl:.2e} t_Pl")
print(f"  M_2D(SN) = {M_2D_Pl:.2e} M_Pl = {M_2D_kg:.2e} kg = {M_2D_kg/M_sun:.2e} M_sun")
print()
print(f"For reference: M_SN_bary = {M_SN_bary/M_sun:.0f} M_sun")
print(f"Ratio: M_2D / M_SN_bary = {M_2D_kg/M_SN_bary:.2e}")
print()

print("Verdict: RT + Bekenstein-Hawking + Unruh = Jacobson. All give the same")
print("linear τ_2D = 2 M_2D, NOT the cascade's power law τ_2D ~ M_2D^1.29.")
print()

print("=" * 70)
print("TEST 3: RT for cascade's DM as missing bulk entanglement")
print("=" * 70)
print()
print("Cascade DM = 2D universe back-projection (cumulative, all 2D universes)")
print("RT: DM (boundary) = missing bulk entanglement entropy")
print()
print("Structural match: YES")
print("Quantitative derivation: NO (cascade's f_DE ~ 10^-85 is separate input)")
print()

print("=" * 70)
print("TEST 4: RT and the cascade's inversion")
print("=" * 70)
print()
print("Cascade: 4D event gravity in 4D = attractive")
print("Cascade: 4D event gravity in 3+1D = repulsive (inversion)")
print()
print("RT: entanglement entropy formula; no sign change mechanism")
print()
print("Verdict: RT DOES NOT DERIVE THE INVERSION. Cascade-specific postulate.")
print()

print("=" * 70)
print("SUMMARY: Ryu-Takayanagi (2006) vs Cascade")
print("=" * 70)
print()
print("✓ STRUCTURAL: RT formula gives cascade DM as missing bulk entanglement")
print("  (2D universe area → 3+1D boundary entropy)")
print()
print("✗ NOT A DERIVATION: RT + BH + Unruh = Jacobson. All give linear τ ~ M,")
print("  not cascade's power law τ ~ M^1.29")
print()
print("✗ INVERSION NOT DERIVED: RT doesn't predict sign changes in coupling")
print()
print("RT provides a CONSISTENCY CHECK on the cascade's f_back, not a derivation")
print("of α = 1.29. The α remains a dynamical parameter.")

results = {
    "test": "Ryu-Takayanagi (2006) holographic entanglement entropy vs cascade",
    "rt_formula": "S_A = Area(γ_A) / (4 G_N)",
    "cascade_2D_universe_area_in_3plus1D": {
        "tau_2D_SN_s": tau_2D_SN,
        "R_2D_m": R_2D,
        "R_2D_ly": R_2D / 9.461e15,
        "A_2D_m^2": A_2D,
        "S_2D": S_2D,
    },
    "rt_jacobson_consistency": "RT + Bekenstein-Hawking + Unruh = Jacobson. All give linear τ = 2M, not power law τ ~ M^1.29",
    "verdict": {
        "structural_match": True,
        "DM_as_missing_bulk_entropy": True,
        "alpha_derived": False,
        "inversion_derived": False,
        "linear_scaling_only": True,
    },
    "conclusion": "RT provides structural match for cascade DM as missing bulk entanglement entropy, but does NOT derive α=1.29, f_split, or the inversion. RT + BH + Unruh = Jacobson = linear scaling, not power law."
}

with open('/workspace/github-repo/calculations/v27_ruyu_takayanagi_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print()
print("Results saved to calculations/v27_ruyu_takayanagi_results.json")
