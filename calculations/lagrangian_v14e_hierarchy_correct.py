#!/usr/bin/env python3
"""
Lagrangian v14e: CORRECTED hierarchy understanding
==================================================

User correction: "3D event creates 2D universes, not 4D. read the paper properly."

The SIDC hierarchy (from §10.1, §10.2):
- **3D event** (event in 3+1D spacetime = our universe) → creates **2D universe**
- **4D event** (event in 4+1D spacetime = higher-dim) → creates **3D universe** (= us)

In SIDC's notation:
- "D" = dimension of the universe CONTAINING the event
- "D-1" = dimension of the universe CREATED
- "3D" = our universe (3 spatial + 1 time)
- "2D" = 2D universe (2 spatial + 1 time)
- "4D" = hypothetical higher-dim universe (4 spatial + 1 time)

The 33 s × (E / 10^44 J)^1.29 scaling was calibrated at the
**3D event → 2D universe** level (Type Ia SN).

For 3D events creating 2D universes:
  E_D = energy of the 3D event (SN, BNS, BBH, etc.)
  T_2D = 33 s × (E_D / 10^44 J)^1.29

For 4D events creating 3D universes (our universe):
  E_D = energy of the 4D cosmological event
  T_3D = 33 s × (E_D / 10^44 J)^1.29 (extrapolated)
  This is the SPECULATIVE extrapolation in §10.1.

v14d had the convention WRONG: it said "4D event creates 2D universe"
when it should be "3D event creates 2D universe".

This v14e CORRECTS the convention and verifies the scaling
separable at each hierarchy level.
"""

import numpy as np

T_PLANCK = 5.391e-44  # s
M_PLANCK = 2.176e-8
C = 2.998e8
E_PLANCK = M_PLANCK * C**2
ALPHA = 1.289

print("="*72)
print("LAGRANGIAN v14e: CORRECTED SIDC HIERARCHY")
print("="*72)
print(f"\nCORRECTED notation:")
print(f"  '3D event' = event in 3+1D spacetime (our universe)")
print(f"  '2D universe' = universe in 2+1D spacetime (2 space + 1 time)")
print(f"  '4D event' = event in 4+1D spacetime (higher-dim)")
print(f"  '3D universe' = our universe (3 space + 1 time)")
print(f"")
print(f"Scaling law:")
print(f"  T_{{2D, 3D-view}} = 33 s × (E_3D / 10^44 J)^{ALPHA}")
print(f"")
print(f"Where:")
print(f"  E_3D = energy of the 3D event (in our universe) creating the 2D universe")
print(f"  T_{{2D, 3D-view}} = 3D-frame lifetime of the 2D universe")

# =============================================================================
# Verify calibration
# =============================================================================
print("\n" + "="*72)
print("PART 1: SN1987A CALIBRATION CHECK")
print("="*72)

gamma_SN = (1e44 / E_PLANCK) ** ALPHA
tau_SN = gamma_SN * T_PLANCK
print(f"\nSN1987A (3D event creating 2D universe):")
print(f"  E_3D = 10^44 J (gravitational collapse energy)")
print(f"  γ = (E_3D/E_Pl)^α = {gamma_SN:.4e}")
print(f"  τ_2D = γ × t_Pl = {tau_SN:.4f} s")
print(f"  Paper says 33 s ✓ (calibration)")

# =============================================================================
# Test ALL 3D events from §10.1
# =============================================================================
print("\n" + "="*72)
print("PART 2: 3D EVENTS (creating 2D universes) — scaling verification")
print("="*72)

events_3D_to_2D = [
    # (name, E_3D J, paper T s)
    ("1 ton TNT", 4e9, 1e-43),
    ("X-class solar flare", 1e25, 1e-23),
    ("Type Ia SN (calibration)", 1e44, 33.0),
    ("Hypernova", 1e46, 3.5 * 3600),
    ("Long GRB", 1e47, 2.8 * 86400),
    ("BNS merger", 1e53, 4e5 * 3.156e7),
    ("AGN flare", 1e55, 1e8 * 3.156e7),
    ("Quasar outburst", 1e60, 5e14 * 3.156e7),
]

print(f"\n{'3D event':>30} {'E_3D (J)':>12} {'T_pred':>14} {'T_paper':>14} {'ratio':>10}")
print("-"*90)

ratios_3D = []
for name, E_3D, T_paper in events_3D_to_2D:
    T_pred = 33.0 * (E_3D / 1e44) ** ALPHA
    ratio = T_pred / T_paper
    ratios_3D.append(ratio)
    print(f"{name:>30} {E_3D:>12.1e} {T_pred:>14.3e} {T_paper:>14.3e} {ratio:>10.3f}")

# =============================================================================
# Test the 4D event (creating our 3D universe) — speculative extrapolation
# =============================================================================
print("\n" + "="*72)
print("PART 3: 4D EVENT (creating our 3D universe) — SPECULATIVE")
print("="*72)

print("\nNOTE: The 4D → 3D level is a SPECULATIVE extrapolation of the")
print("scaling. The 33 s calibration is at the 3D → 2D level.")

E_4D_cosm = 1e69  # J
T_paper_3D = 2e26 * 3.156e7  # s
T_pred_3D = 33.0 * (E_4D_cosm / 1e44) ** ALPHA

print(f"\n4D cosmological event (creating 3D universe = us):")
print(f"  E_4D = 10^69 J (rest energy of observable 3+1D universe)")
print(f"  T_pred = 33 s × (10^69/10^44)^{ALPHA} = {T_pred_3D:.3e} s = {T_pred_3D/3.156e7:.3e} yr")
print(f"  Paper says 2 × 10^26 yr = {T_paper_3D:.3e} s")
print(f"  Ratio = {T_pred_3D / T_paper_3D:.3f}")

# =============================================================================
# Verdict
# =============================================================================
print("\n" + "="*72)
print("PART 4: VERDICT (v14e)")
print("="*72)

ratios_3D_arr = np.array(ratios_3D)
print(f"\n8 events at 3D → 2D level:")
print(f"  Min ratio:    {np.min(ratios_3D_arr):.3f}")
print(f"  Max ratio:    {np.max(ratios_3D_arr):.3f}")
print(f"  Median ratio: {np.median(ratios_3D_arr):.3f}")
print(f"  Geom. mean:   {np.exp(np.mean(np.log(ratios_3D_arr))):.3f}")

print(f"\nSpeculative 4D → 3D level:")
print(f"  Ratio: {T_pred_3D / T_paper_3D:.3f}")

print("\n" + "="*72)
print("KEY CORRECTION (v14e — USER POINT):")
print("  The hierarchy is:")
print("    3D event (in our universe) creates 2D universe")
print("    4D event (in higher-dim) creates 3D universe (us)")
print("  ")
print("  v14d had this BACKWARDS — said '4D event creates 2D universe'.")
print("  The 33 s calibration is at the 3D → 2D level.")
print("  The 4D cosmological row in §10.1 is a SPECULATIVE extrapolation.")
print("  ")
print("  L93 STILL CLOSED:")
print("    - 3D → 2D scaling: 8/8 events match within factor 1.6")
print("    - 4D → 3D scaling (speculative): matches within 12%")
print("    - Both hierarchy levels work with the same FORMULA")
print("="*72)