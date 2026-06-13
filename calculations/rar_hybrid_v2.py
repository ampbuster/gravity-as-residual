#!/usr/bin/env python3
"""
Hybrid DM model v2: properly account for the M_halo decomposition.

The total empirical M_halo = M_cascade + M_NFW
M_cascade = scale * M_halo_empirical (10% for MW)
M_NFW = (1 - scale) * M_halo_empirical (90% for MW)

For the RAR to be fit, the SUM of g_cascade + g_NFW must match the
RAR's g_obs at every radius.

The NFW c parameter (concentration) affects the SHAPE of g_NFW.
The cascade's r_core_frac affects the SHAPE of g_cascade.

Test: does the hybrid model fit the RAR with reasonable parameters?
"""

import math
import numpy as np

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
g_plus_galaxy = 1.2e-10

def rar(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

def g_bar_disk(r_kpc, M_disk_Msun, R_disk_kpc):
    r_m = r_kpc * kpc_to_m
    M_disk_enclosed = M_disk_Msun * M_sun * (1 - (1 + r_m/(R_disk_kpc * kpc_to_m)) * math.exp(-r_m/(R_disk_kpc * kpc_to_m)))
    return G * M_disk_enclosed / r_m**2 if r_m > 0 else 0

def g_cascade(r_kpc, M_cascade_Msun, R_halo_kpc, f_active, M_disk_Msun, R_disk_kpc, r_core_frac):
    """Cascade contribution from M_cascade (scale * M_halo)"""
    M_cum_total_kg = (1 - f_active) * M_cascade_Msun * M_sun
    r_core_m = r_core_frac * R_halo_kpc * kpc_to_m
    r_m = r_kpc * kpc_to_m
    R_halo_m = R_halo_kpc * kpc_to_m
    V_eff = 4 * math.pi * r_core_m**2 * (R_halo_m - 2 * r_core_m / 3)
    rho_0 = M_cum_total_kg / V_eff if V_eff > 0 else 0
    if r_m < r_core_m:
        M_cum_enclosed = (4/3) * math.pi * r_m**3 * rho_0
    else:
        M_core = (4/3) * math.pi * r_core_m**3 * rho_0
        M_cum_enclosed = M_core + 4 * math.pi * rho_0 * r_core_m**2 * (r_m - r_core_m)
    M_disk = M_disk_Msun * M_sun
    R_d = R_disk_kpc * kpc_to_m
    # active contribution needs kappa = M_halo / M_disk
    # but in hybrid model, M_halo = M_cascade (the cascade's share)
    # Hmm, this is ambiguous
    # Let me set: kappa = M_cascade / M_disk (the cascade's kappa)
    kappa = M_cascade_Msun / M_disk_Msun if M_disk_Msun > 0 else 0
    M_stellar_enclosed = M_disk * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    M_active_enclosed = f_active * kappa * M_stellar_enclosed
    M_DM_enclosed = M_cum_enclosed + M_active_enclosed
    g_dm = G * M_DM_enclosed / r_m**2 if r_m > 0 else 0
    return g_dm

def g_NFW(r_kpc, M_NFW_Msun, R_halo_kpc, c):
    r_m = r_kpc * kpc_to_m
    R_halo_m = R_halo_kpc * kpc_to_m
    r_s = R_halo_m / c
    M_NFW_kg = M_NFW_Msun * M_sun
    factor = math.log(1 + c) - c / (1 + c)
    rho_s = M_NFW_kg / (4 * math.pi * r_s**3 * factor) if factor > 0 else 0
    if r_m <= 0:
        return 0
    x = r_m / r_s
    M_enclosed = 4 * math.pi * rho_s * r_s**3 * (math.log(1 + x) - x / (1 + x))
    return G * M_enclosed / r_m**2

# Test on MW
M_disk, R_disk = 6e10, 4
M_halo_empirical = 1e12
R_halo = 30

print("=" * 80)
print("HYBRID MODEL v2 on MW")
print("=" * 80)
print()
print(f"  M_halo_empirical = {M_halo_empirical:.1e}")
print(f"  Split: scale=0.1, so M_cascade = 1e11, M_NFW = 9e11")
print()

# Try different (scale, c) combinations
best_result = None
best_err = float('inf')

for scale in [0.05, 0.1, 0.2, 0.3, 0.5, 0.7]:
    for c in [3, 5, 8, 10, 15, 20, 30]:
        for f_active in [0.02, 0.05, 0.1]:
            for r_core_frac in [0.15, 0.2, 0.25, 0.3]:
                M_cascade = scale * M_halo_empirical
                M_NFW = (1 - scale) * M_halo_empirical
                
                # Compute residuals
                test_radii = [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]
                total_err = 0
                n = 0
                for r in test_radii:
                    g_b = g_bar_disk(r, M_disk, R_disk)
                    if g_b <= 0:
                        continue
                    g_cas = g_cascade(r, M_cascade, R_halo, f_active, M_disk, R_disk, r_core_frac)
                    g_nfw = g_NFW(r, M_NFW, R_halo, c)
                    g_obs = g_b + g_cas + g_nfw
                    g_rar = rar(g_b, g_plus_galaxy)
                    if g_rar > 0:
                        total_err += (math.log(g_obs / g_rar))**2
                        n += 1
                if n > 0:
                    total_err /= n
                if total_err < best_err:
                    best_err = total_err
                    best_result = (scale, c, f_active, r_core_frac)

scale, c, f_active, r_core_frac = best_result
print(f"Best fit: scale={scale}, c={c}, f_active={f_active}, r_core_frac={r_core_frac}, log_err={best_err:.5f}")
print()

# Detailed fit
M_cascade = scale * M_halo_empirical
M_NFW = (1 - scale) * M_halo_empirical
print(f"Detailed fit: M_cascade = {M_cascade:.2e}, M_NFW = {M_NFW:.2e}")
print()
print(f"  {'r (kpc)':>8s}  {'g_bar':>12s}  {'g_cas':>12s}  {'g_NFW':>12s}  {'g_obs':>12s}  {'RAR':>12s}  {'diff':>8s}")
print()
for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]:
    g_b = g_bar_disk(r, M_disk, R_disk)
    if g_b <= 0:
        continue
    g_cas = g_cascade(r, M_cascade, R_halo, f_active, M_disk, R_disk, r_core_frac)
    g_nfw = g_NFW(r, M_NFW, R_halo, c)
    g_obs = g_b + g_cas + g_nfw
    g_rar = rar(g_b, g_plus_galaxy)
    diff = (g_obs - g_rar) / g_rar
    print(f"  {r:>8.1f}  {g_b:>12.3e}  {g_cas:>12.3e}  {g_nfw:>12.3e}  {g_obs:>12.3e}  {g_rar:>12.3e}  {diff:>8.2f}")
