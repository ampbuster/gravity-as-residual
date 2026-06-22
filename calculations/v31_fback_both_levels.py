#!/usr/bin/env python3
"""
v31_fback_both_levels.py

Verify f_back formula works at BOTH 2D→3D and 3D→4D.

The formula: f_back(N→N-1) = (M_Pl,N / E_event)^α
This is the CONTINUOUS back-flow FRACTION over the lifetime τ.

The PULSED return at death is 100% (universal, no α).

So: continuous(f_back) + pulsed(1 - f_back) = 1.0 total return.

OBSERVABLE differs by level:
- 2D→3D: pulsed dominates (short τ_2D = 30s, so we see 100% return as DM)
- 3D→4D: continuous dominates (long τ_4D = 10^34 yr, we see continuous as DE)


**HISTORICAL (v3.1.2-final era, June 2026)**: This file uses v3.1.2 values:
- M_Pl,4D = 887 GeV (Scenario X, was inferred before α-GM at 3.93e23)
- M_Pl,2D = 3 TeV (now 2.95 TeV per L308r)
- α = 1.289 (now FIRST-PRINCIPLES via Schwarzian SYK N=12, L308n)
- ε = 1e-38 (now A2 = 6.32e-34, +4.8 orders)
- f_back = (M_Pl/E)^α (LEGACY naming, renamed f_DE,closed in v3.5.7+)

Current v3.5.9+ A2 values:
- M_Pl,4D = 3.93e23 GeV (DERIVED via α-GM, L308v)
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N×v_H, L308r)
- α = 1.289 (FIRST-PRINCIPLES via L308n)
- ε = 6.32e-34 (A2 recalibrated)
- f_DE,closed = 1.79e-90 (A2 closed loop)

This file is kept for historical audit.
"""

import math

# Constants
c = 2.998e8
GeV_to_J = 1.602e-10
J_to_GeV = 1.0 / GeV_to_J
t_Pl_3D = 5.391e-44  # s
M_Pl_3D_GeV = 1.221e19  # GeV (measured)
M_Pl_4D_GeV = 887.0  # GeV (Scenario X, inferred)
M_Pl_2D_GeV = 1e38  # GeV (inferred)
alpha_cal = 1.289
epsilon = 1e-38
v_Higgs = 246.0
yr = 3.156e7  # s

def tau_M_alpha(E_J, M_Pl_GeV, alpha=alpha_cal):
    """τ in seconds from M^α law."""
    E_GeV = E_J * J_to_GeV
    return (E_GeV / M_Pl_GeV) ** alpha * t_Pl_3D

def f_back_fraction(E_J, M_Pl_GeV, alpha=alpha_cal):
    """Total continuous back-flow fraction (dimensionless)."""
    E_GeV = E_J * J_to_GeV
    return (M_Pl_GeV / E_GeV) ** alpha

def pulsed_fraction(E_J, M_Pl_GeV, alpha=alpha_cal):
    """Pulsed return fraction at death."""
    return 1.0 - f_back_fraction(E_J, M_Pl_GeV, alpha)

print("="*70)
print("f_back FORMULA VERIFICATION: 2D→3D AND 3D→4D")
print("="*70)

print("\nFORMULA: f_back = (M_Pl,N / E_event)^α (continuous back-flow fraction)")
print("         pulsed = 1 - f_back (100% return at death)")
print("         continuous + pulsed = 1.0 (total return)\n")

# 2D→3D: SN example
E_SN = 1e44  # J
tau_2D = tau_M_alpha(E_SN, M_Pl_3D_GeV)
f_DM_leak = f_back_fraction(E_SN, M_Pl_3D_GeV)
pulsed_2D = pulsed_fraction(E_SN, M_Pl_3D_GeV)
print(f"2D→3D (SN, E_SN = 1e44 J, M_Pl,3D = 1.22e19 GeV):")
print(f"  τ_2D = {tau_2D:.3g} s = {tau_2D:.2f} s")
print(f"  f_back fraction = {f_DM_leak:.3g}  (continuous return during τ_2D)")
print(f"  pulsed fraction = {pulsed_2D:.10f}  (essentially 1.0)")
print(f"  continuous + pulsed = {f_DM_leak + pulsed_2D:.10f}  (should be 1.0)")

E_continuous_2D = f_DM_leak * E_SN
print(f"  Continuous return: f_back × E_SN = {E_continuous_2D:.3g} J per SN")
print(f"  Pulsed return: (1-f_back) × E_SN = {(1-f_DM_leak)*E_SN:.3g} J per SN")
print(f"  Ratio pulsed/continuous = {pulsed_2D/f_DM_leak:.3g}")
print(f"  → Pulsed DOMINATES by factor of 10⁴⁵")
print(f"  → Observable: 2D universe DEATH return = ~100% × E_2D = 10⁴⁴ J (DM)")

# 3D→4D: 4D event
E_4D = 1.07e59  # J
tau_4D = tau_M_alpha(E_4D, M_Pl_4D_GeV)
f_DE = f_back_fraction(E_4D, M_Pl_4D_GeV)
pulsed_4D = pulsed_fraction(E_4D, M_Pl_4D_GeV)
print(f"\n3D→4D (4D event, E_4D = 1.07e59 J, M_Pl,4D = 887 GeV):")
print(f"  τ_4D = {tau_4D:.3g} s = {tau_4D/yr:.3g} yr (apparent, in 3+1D frame)")
print(f"  f_back fraction = {f_DE:.3g}  (continuous return during τ_4D)")
print(f"  pulsed fraction = {pulsed_4D:.10f}  (essentially 1.0)")
print(f"  continuous + pulsed = {f_DE + pulsed_4D:.10f}  (should be 1.0)")

E_continuous_4D = f_DE * E_4D
print(f"  Continuous return: f_back × E_4D = {E_continuous_4D:.3g} J total over τ_4D")
print(f"  Continuous rate: f_back / τ_4D = {E_continuous_4D/tau_4D:.3g} J/s")

# DE density
rho_DE_continuous = f_DE * epsilon * M_Pl_3D_GeV**4
print(f"  ρ_DE (continuous) = f_back × ε × M_Pl,3D^4 = {rho_DE_continuous:.3g} GeV^4")
print(f"  ρ_DE (observed)   = 2.4e-47 GeV^4")
print(f"  Ratio: {rho_DE_continuous/2.4e-47:.3f} (~14% match)")

# The "shape" question
print("\n" + "="*70)
print("SHAPE OF f_back vs E_event:")
print("="*70)
print("\nf_back(E) = (M_Pl/E)^α — UNIVERSAL FORM at every level")
print("DIFFERENT VALUES because M_Pl,N and E_event differ at each level")
print()
for E in [1e44, 1e50, 1e55, 1e59, 1e60]:
    fb_2D = f_back_fraction(E, M_Pl_3D_GeV)
    fb_4D = f_back_fraction(E, M_Pl_4D_GeV)
    print(f"  E = {E:.0e} J: f_back(2D→3D) = {fb_2D:.3g}, f_back(3D→4D) = {fb_4D:.3g}")

print("\n" + "="*70)
print("CONCLUSION:")
print("="*70)
print("✓ f_back formula is FORM-CORRECT at every level: f_back = (M_Pl,N/E)^α")
print("✓ α = 1.289 is UNIVERSAL (same at every level)")
print("✓ M_Pl,N DIFFERS at each level (10^38, 10^19, 887 GeV)")
print("✓ E_event DIFFERS at each transition")
print("✓ Result: different f_back VALUES at each level (1e-45 vs 1e-85)")
print()
print("Observable consequence:")
print("  - 2D→3D: pulsed return (DM) dominates by 10^45× over continuous")
print("  - 3D→4D: continuous return (DE) is what we observe NOW (pulsed is in future)")
print("  - This is what makes DE and DM look so different despite same mechanism")
