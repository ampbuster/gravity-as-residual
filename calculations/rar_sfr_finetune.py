#!/usr/bin/env python3
"""
Fine-tune the f_active(SFR) relationship.
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

def g_DM(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, r_core_frac, scale):
    M_cum_total_kg = scale * (1 - f_active) * M_halo_Msun * M_sun
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
    kappa = M_halo_Msun / M_disk_Msun if M_disk_Msun > 0 else 0
    M_stellar_enclosed = M_disk * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    M_active_enclosed = f_active * kappa * M_stellar_enclosed
    M_DM_enclosed = M_cum_enclosed + M_active_enclosed
    g_dm = G * M_DM_enclosed / r_m**2 if r_m > 0 else 0
    return g_dm

np.random.seed(42)
galaxies = []
M_halo_values = np.logspace(8, 13, 30)
for i, M_halo in enumerate(M_halo_values):
    kappa = 5 + (i % 10) * 10
    M_disk = M_halo / kappa
    R_disk = 4 * (M_halo / 1e12) ** 0.4
    if R_disk < 0.2:
        R_disk = 0.2
    R_halo = 8 * R_disk
    log_SFR = -3 + 4 * (i % 5) / 4
    SFR = 10**log_SFR
    galaxies.append((f"Galaxy_{i+1}", M_disk, R_disk, M_halo, R_halo, kappa, SFR))

def evaluate(galaxies, f_active_func, r_core_frac_func, scale_func, add_noise=True):
    all_diffs = []
    per_galaxy_medians = []
    for name, M_disk, R_disk, M_halo, R_halo, kappa, SFR in galaxies:
        f_active = f_active_func(M_halo, kappa, SFR)
        r_core_frac = r_core_frac_func(M_halo, kappa, SFR)
        scale = scale_func(M_halo, kappa, SFR)
        
        gal_diffs = []
        test_radii = [0.3*R_disk, 1*R_disk, 2*R_disk, 4*R_disk, 6*R_disk]
        for r in test_radii:
            if r > R_halo * 0.9:
                continue
            g_b = g_bar_disk(r, M_disk, R_disk)
            if g_b <= 0:
                continue
            g_dm = g_DM(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, scale)
            g_obs = g_b + g_dm
            g_obs_rar = rar(g_b, g_plus_galaxy)
            if g_obs_rar > 0:
                diff = (g_obs - g_obs_rar) / g_obs_rar
                if add_noise:
                    diff += np.random.normal(0, 0.1)
                all_diffs.append(abs(diff))
                gal_diffs.append(abs(diff))
        if gal_diffs:
            per_galaxy_medians.append(np.median(gal_diffs))
    
    return {
        'median': np.median(all_diffs),
        'median_gal': np.median(per_galaxy_medians),
        'within_20%': sum(1 for d in all_diffs if d < 0.2) / len(all_diffs) * 100,
    }

# Fine grid search around f_active = 0.02 + 0.01 * log10(SFR + 1)
print("=" * 80)
print("FINE-TUNE: f_active = a + b * log10(SFR + 1)")
print("=" * 80)
print()
print("  a        b        median    per-gal   within 20%")
print()

best = None
best_err = float('inf')
for a in [0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.04, 0.05]:
    for b in [0.001, 0.003, 0.005, 0.008, 0.01, 0.015, 0.02, 0.03]:
        f_func = lambda M, k, s, a=a, b=b: max(0.001, min(0.3, a + b * math.log10(s + 1)))
        r_func = lambda M, k, s: 0.25
        s_func = lambda M, k, s: 0.15
        result = evaluate(galaxies, f_func, r_func, s_func)
        if result['median'] < best_err:
            best_err = result['median']
            best = (a, b, result)
        print(f"  {a:.3f}   {b:.3f}   {result['median']:.3f}    {result['median_gal']:.3f}    {result['within_20%']:.1f}%")

print()
print(f"Best: a={best[0]}, b={best[1]}, median={best[2]['median']:.3f}, within 20%={best[2]['within_20%']:.1f}%")
