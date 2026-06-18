#!/usr/bin/env python3
"""
v31_fp_z_derivation.py
======================

Can the v3.1 cone depth framing REPLACE the Hill function F_p(z)?

OLD PICTURE (v2.7.52):
  F_p(z) = 0.9993 + 0.0007 * z^2/(z_half^2 + z^2)
  Hill n=2, z_half=3
  No basis - just a phenomenological fit
  L100: F_p(z) is a FIT, not a derivation

NEW PICTURE (v3.1):
  f_back varies with event energy
  - 4D event (depth +53.8 alpha): f_back ≈ 1
  - SN (depth +26.93 alpha): f_back ≈ 10^-85
  - Sun (depth +3.6 to +17.3): f_back in between

F_p(z) = projected_primordial_DM / total_projected_DM

The key insight: f_back_4D ≈ 1 means ALL the 4D event's energy gets
back-projected. f_back_SN ≈ 10^-85 means the SN contribution is
suppressed by 85 orders of magnitude. So F_p(z) ≈ 1 naturally.

This calculation:
1. Computes F_p(z) in the v3.1 picture from first principles
2. Compares to the Hill function fit
3. Shows the Hill function can be replaced
"""

import math
import numpy as np

# Constants
T_PLANCK_3 = 5.391e-44  # s, 3+1D Planck time
T_PLANCK_2D = 2e-28     # s, 2D Planck time (holographic estimate)
E_PLANCK_3 = 1.22e19    # GeV, 3+1D Planck energy = 1.95e9 J
ALPHA = 1.289           # energy scaling exponent
M_4D = 1e69             # J, 4D event energy (calibration)
TAU_4D = 4.1e32        # s, 4D event eternal lifetime (~10^25 yr)

# 2D universe lifetimes (scaling law)
def tau_2D(E_3D):
    """2D universe lifetime in 3+1D view"""
    return T_PLANCK_3 * (E_3D / E_PLANCK_3 / 1.602e-10) ** ALPHA

# f_back formula (closed loop, simplified)
def f_back(E_event, E_SN=1e44):
    """f_back varies with event energy"""
    # The closed loop formula: f_back = (t_Pl,3/tau_4D) * (tau_SN/tau_universe) * (E_4D/E_SN)^(1/(2*alpha))
    # We use a simpler form: f_back scales as E^(1/(2*alpha))
    f_back_SN = 1e-85  # at SN scale
    ratio = (E_event / E_SN) ** (1 / (2 * ALPHA))
    return f_back_SN * ratio

# Cone depth (in alpha units)
def cone_depth(E_3D):
    """Cone depth in alpha units"""
    tau = tau_2D(E_3D)
    return math.log10(tau / T_PLANCK_2D) / ALPHA

# Verify known depths
print("=== Cone depth verification ===")
print(f"LHC p-p (14 TeV = 2.24e-6 J): depth = {cone_depth(2.24e-6):.2f} (expected: -11.86)")
print(f"SN (1e44 J): depth = {cone_depth(1e44):.2f} (expected: +26.93)")
print(f"Sun flare (1e26 J): depth = {cone_depth(1e26):.2f} (computed)")
print(f"Sun total (5e43 J): depth = {cone_depth(5e43):.2f} (computed)")
print(f"4D event (1e69 J): depth = {cone_depth(1e69):.2f} (computed)")
print()

# Event types and rates (from v21 / L100)
EVENTS = [
    # (name, E_per_event_J, rate_per_galaxy_per_Gyr)
    ("Core-collapse SN", 1e44, 1e-2),
    ("Type Ia SN", 1e43, 1e-3),
    ("NS-NS merger", 1e53, 1e-5),
    ("NS-BH merger", 1e53, 1e-7),
    ("BH-BH merger", 1e47, 1e-4),
    ("AGN outburst", 1e55, 1e-3),
    ("TDE", 1e38, 1e-4),
    ("Solar flare", 1e26, 1e4),  # high rate but low energy
]

# Number of galaxies
N_GAL = 1e11
T_UNIVERSE = 13.8e9 * 365.25 * 24 * 3600  # s

# Compute total cumulative energy
print("=== Cumulative 2D universe energy (v3.1 picture) ===")
total_E_3plus1D = 0
total_DM_3plus1D = 0
for name, E, rate in EVENTS:
    # Total number of events over cosmic history
    N_total = N_GAL * rate * T_UNIVERSE / 1e9 / 365.25 / 24 / 3600  # in Gyr
    # Total energy
    E_total = N_total * E
    # 2D universe lifetime
    tau = tau_2D(E)
    # f_back at this event
    fb = f_back(E)
    # Projected DM (f_back × energy)
    DM = fb * E_total
    total_E_3plus1D += E_total
    total_DM_3plus1D += DM
    print(f"  {name:20s} E={E:.0e} J, N={N_total:.2e}, "
          f"tau={tau:.2e} s, f_back={fb:.2e}, DM={DM:.2e} J")

print(f"\nTotal cumulative energy: {total_E_3plus1D:.2e} J")
print(f"Total cumulative DM (projected): {total_DM_3plus1D:.2e} J")

# Primordial 2D universe (from 4D event)
print()
print("=== Primordial 2D universe (from 4D event) ===")
tau_primordial = tau_2D(M_4D)
depth_primordial = cone_depth(M_4D)
fb_primordial = f_back(M_4D)
print(f"4D event: E = {M_4D:.0e} J")
print(f"2D universe lifetime: {tau_primordial:.2e} s = {tau_primordial/365.25/24/3600:.2e} yr")
print(f"Cone depth: {depth_primordial:.2f} alpha units")
print(f"f_back: {fb_primordial:.2e}")
print(f"Projected primordial DM: {fb_primordial * M_4D:.2e} J")

# F_p = projected_primordial / total_projected
total_projected = fb_primordial * M_4D + total_DM_3plus1D
F_p_primordial = fb_primordial * M_4D / total_projected
F_p_cumulative = total_DM_3plus1D / total_projected

print()
print("=== F_p(z=0) in v3.1 picture ===")
print(f"Projected primordial DM: {fb_primordial * M_4D:.2e} J")
print(f"Projected cumulative DM:  {total_DM_3plus1D:.2e} J")
print(f"Total projected DM:        {total_projected:.2e} J")
print(f"F_p (primordial fraction): {F_p_primordial:.6f}")
print(f"F_cum (cumulative fraction): {F_p_cumulative:.2e}")
print()
print(f"OLD picture (v2.7.52): F_p(0) = 0.9993 (Hill n=2, z_half=3)")
print(f"NEW picture (v3.1):    F_p(0) = {F_p_primordial:.6f}")
print()
print(f"Match: {abs(F_p_primordial - 0.9993) < 0.01}")
print()
print("=== F_p(z) at different redshifts ===")
# At higher z, only 2D universes with tau < age_at_z contribute
# age_at_z = 13.8 Gyr / (1+z)^1.5 (approximate)
# A 2D universe is "alive" if tau_2D > age_at_z

z_values = [0, 0.5, 1, 2, 3, 5, 10, 100, 1100]
print(f"{'z':>6s} {'age (Gyr)':>10s} {'F_p (v3.1)':>12s} {'F_p (Hill)':>12s} {'diff':>10s}")
for z in z_values:
    age_Gyr = 13.8 / (1+z)**1.5
    age_s = age_Gyr * 1e9 * 365.25 * 24 * 3600
    
    # Primordial 2D universe: ALWAYS dead by age ~ 1e-2 yr (tau_primordial ~ 10 yr)
    # So it ALWAYS contributes to DM at all z > 0
    
    # Cumulative 2D universe: contributes if its tau < age (i.e., already dead)
    # For z = 1100 (380 kyr), only events with tau_2D < 380 kyr contribute
    # For SN, tau_2D = 33 s << 380 kyr, so SN contributes at all z > 0
    
    # Actually for F_p(z) we want: at time t, what fraction of DM is primordial?
    # F_p(t) = (primordial DM) / (primordial DM + cumulative DM at time t)
    # The cumulative DM at time t = f_back × Σ E_events that died before time t
    
    # The cumulative DM is the integral of all 2D universe deaths up to time t
    # At time t = 0 (BB), no deaths yet
    # At time t = 13.8 Gyr, all 2D universes that ever lived have died
    
    # For our purposes, F_p(z) ≈ F_p(0) since all events have died by now
    # (primordial died at t = 1e-2 yr after BB, SN died at 33 s after creation, etc.)
    # 
    # So F_p(z) ≈ F_p(0) for all z > a few
    
    F_p_v31 = F_p_primordial
    F_p_hill = 0.9993 + 0.0007 * z**2 / (3**2 + z**2)
    diff = F_p_v31 - F_p_hill
    print(f"{z:>6.1f} {age_Gyr:>10.2e} {F_p_v31:>12.6f} {F_p_hill:>12.6f} {diff:>10.2e}")

print()
print("=== HONEST CONCLUSION (REVISED, June 18 2026) ===")
print()
print("Naive v3.1 calculation gives F_p(z=0) ~ 1.0 (all primordial).")
print("This result is WRONG. See the REVISION below.")
print()
print("USER FEEDBACK (June 18 2026):")
print("  If F_p = 1 (all DM from 4D event), DM would be UNIFORM background.")
print("  But SIDC's whole point is that DM varies between galaxies based on")
print("  their star formation history (DF2/DF4/AGC 114905: no DM; KKR 25: DM).")
print("  F_p = 1 cannot explain local DM variation.")
print()
print("ROOT CAUSE: §3.67 'f_back_4D → 1' is overloading the variable.")
print("  - f_back_SN (depth +26.93): fraction of 2D universe energy that")
print("    back-projects to 3+1D as DM (~10^-85)")
print("  - f_back_4D (depth +53.8): the 4D event CREATES our 3+1D universe")
print("    f_back = 1 means 'fully projects to 3+1D' (by definition,")
print("    since our universe IS the 4D event's projection).")
print("  These are NOT the same quantity. Comparing f_back_4D = 1 to")
print("  f_back_SN = 10^-85 is comparing apples to oranges.")
print()
print("Closed loop formula f_back = 10^-85 × (E/E_SN)^(1/(2α))")
print("extrapolates to f_back_4D ~ 10^-75 for E_4D = 10^69 J.")
print("But this formula may not apply to the 4D event (qualitatively")
print("different — it creates a 3+1D universe, not a 2D universe).")
print()
print("INTERNAL INCONSISTENCY in paper (L137 NEW):")
print("  §3.67 says f_back_4D → 1 (L114)")
print("  Closed loop formula gives f_back_4D ~ 10^-75")
print("  These cannot both be right.")
print()
print("NET RESULT: F_p(z) CANNOT be derived from the v3.1 framing as")
print("currently written. The Hill function (n=2, z_half=3) MUST stay")
print("until the 4D event's effective DM contribution is properly derived.")
print()
print("L100, L35 remain OPEN. L34 remains CLOSED (v2.7.52).")
print()
print("NEW LIMITATION L137 (June 18 2026): §3.67 f_back_4D = 1 is")
print("  INCONSISTENT with the closed loop formula. The 'fully")
print("  back-projected substrate' claim needs a clearer definition")
print("  of what 'f_back' means at the 4D-event level.")
