#!/usr/bin/env python3
"""
RAR FUNCTIONAL FORM FROM CASCADE PRINCIPLES - g_+ from cumulative return

A different approach: derive g_+ from first principles using the cascade's
own 2D universe physics, not by fitting to NFW profiles.

The cascade says:
  - g_+ is the cumulative-return contribution to g_DM
  - The cumulative return is roughly uniform in space
  - g_+(cumulative) ~ G * rho_cumulative * (some length scale)

For a 2D universe of mass M_2D_peak, the cumulative return is a
fraction of M_2D_peak that's distributed over a large volume.

Empirically, g_+ ~ 1.2e-10 m/s^2 = G * rho_c * R_c
  where rho_c is the cumulative DM density and R_c is some characteristic length.

For the cascade:
  rho_c ~ f_cumulative * M_DM_halo / V_halo
  R_c ~ halo scale radius

So g_+_cascade = G * (f_cumulative * M_DM_halo / V_halo) * R_halo
              = G * f_cumulative * M_DM_halo / (4/3 * pi * R_halo^2)
              = (3/4) * G * f_cumulative * M_DM_halo / (pi * R_halo^2)

Let me compute this for the Milky Way and compare.


**HISTORICAL (v2.x era, mid-2025)**: This file is from the v2.x era, predating:
- v3.0+ Lagrangian work (L102-L136)
- v3.1+ Multi-universe picture (L142-L150)
- v3.3 Bilateral cascade (E_4D = 5e79 J, M_Pl,4D = 3.93e23 GeV)
- v3.5.7+ Naming revolution (f_back -> f_DE, f_DM,leak, f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N*v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via alpha-GM, L308v)
- alpha = 1.289 (FIRST-PRINCIPLES via L308n)
- eps = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- gamma_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- tau_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v2.x era framework, not v3.5.9+ A2.

"""

import math

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19

# Milky Way
M_DM_halo = 1e12 * M_sun  # 1e12 M_sun
R_halo = 30 * kpc_to_m  # 30 kpc scale radius
f_cumulative = 0.7

# Compute cascade's g_+ from cumulative return
g_plus_cascade = (3/4) * G * f_cumulative * M_DM_halo / (math.pi * R_halo**2)

print("=" * 80)
print("RAR g_+ FROM CASCADE'S CUMULATIVE RETURN (v4)")
print("=" * 80)
print()
print("Milky Way-like galaxy:")
print(f"  M_DM_halo = {M_DM_halo/M_sun:.1e} M_sun = {M_DM_halo:.3e} kg")
print(f"  R_halo = {R_halo/kpc_to_m:.1f} kpc = {R_halo:.3e} m")
print(f"  f_cumulative (cascade) = {f_cumulative}")
print()
print("Cascade's g_+ from cumulative return:")
print(f"  g_+ = (3/4) * G * f_cumulative * M_DM_halo / (pi * R_halo^2)")
print(f"      = {g_plus_cascade:.3e} m/s^2")
print()
print(f"  Empirical g_+ (McGaugh+ 2016): 1.20e-10 m/s^2")
print(f"  Ratio (cascade/empirical): {g_plus_cascade/1.2e-10:.2f}")
print()

# For different galaxy types
print("=" * 80)
print("RAR g_+ ACROSS DIFFERENT GALAXY TYPES")
print("=" * 80)
print()
print(f"  {'Galaxy type':>20s}  {'M_DM (M_sun)':>12s}  {'R_halo (kpc)':>12s}  {'g_+ (m/s^2)':>12s}  {'ratio':>8s}")
print(f"  {'-'*20}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*8}")

galaxies = [
    ("Dwarf", 1e9, 5),
    ("Small spiral", 1e10, 10),
    ("Milky Way", 1e12, 30),
    ("Large spiral", 5e12, 50),
    ("Cluster", 1e14, 500),
    ("Supercluster", 1e15, 3000),
]

for name, M_DM_Msun, R_halo_kpc in galaxies:
    M_DM = M_DM_Msun * M_sun
    R = R_halo_kpc * kpc_to_m
    g_plus = (3/4) * G * f_cumulative * M_DM / (math.pi * R**2)
    print(f"  {name:>20s}  {M_DM_Msun:12.2e}  {R_halo_kpc:12.1f}  {g_plus:12.3e}  {g_plus/1.2e-10:8.2f}")

print()
print("=" * 80)
print("RAR FUNCTIONAL FORM PREDICTION")
print("=" * 80)
print()
print("Empirical RAR (McGaugh+ 2016):")
print("  g_obs = g_bar / (1 - exp(-sqrt(g_bar / g_+)))")
print("  with g_+ ~ 1.2e-10 m/s^2 (CONSTANT across galaxy types)")
print()
print("Cascade's RAR:")
print("  g_obs = g_bar + g_DM")
print("  g_DM = G * M_DM_enclosed(r) / r^2")
print("  M_DM_enclosed(r) = M_active_enclosed(r) + M_cumulative_enclosed(r)")
print()
print("Cascade's g_+ (the empirical 'floor' parameter):")
print("  g_+_cascade = (3/4) * G * f_cumulative * M_DM / (pi * R_halo^2)")
print()
print("If g_+ is CONSTANT across galaxy types (as observed), then:")
print("  G * f_cumulative * M_DM / R_halo^2 = constant")
print("  M_DM / R_halo^2 = constant")
print("  M_DM ~ R_halo^2 (not R_halo^3, which would be constant density)")
print()
print("This is the famous 'M_DM ~ R^2' baryonic Tully-Fisher-like relation!")
print("  (Empirically: M_baryon ~ R^4, but M_DM ~ R^2 in the cascade's picture)")
print()
print("  This is a TESTABLE PREDICTION of the cascade.")
print("  If future observations show M_DM ~ R^2 (not R^3), it supports the cascade.")

