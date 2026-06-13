#!/usr/bin/env python3
"""
REVISED test: SFR-M_star correlated (as in real data).

In the previous test, SFR was randomly assigned. In reality, SFR correlates
strongly with M_star. So SFR is NOT an independent degree of freedom.

This test uses a realistic SFR-M_star relation to check if the "SFR 
breakthrough" survives.
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

# Generate galaxies with REALISTIC SFR-M_star relation
# Kennicutt-Schmidt: SFR ∝ M_star^1.4 (but with scatter)
# Use main sequence galaxies
np.random.seed(42)
galaxies_realistic = []
galaxies_random_sfr = []
galaxies_quenched = []

M_halo_values = np.logspace(8, 13, 30)
for i, M_halo in enumerate(M_halo_values):
    kappa = 5 + (i % 10) * 10
    M_disk = M_halo / kappa  # M_star
    R_disk = 4 * (M_halo / 1e12) ** 0.4
    if R_disk < 0.2:
        R_disk = 0.2
    R_halo = 8 * R_disk
    
    # Realistic SFR: main sequence, with log scatter 0.3 dex
    # SFR_MS ~ M_star^0.8 in linear units (Genzel+ 2015)
    # Or SFR ∝ M_star / t_depletion where t_depletion ~ 1-2 Gyr
    SFR_MS = M_disk / 1e9  # Very rough MS: 1 M_sun/yr per 1e9 M_sun
    # Add scatter
    SFR_realistic = SFR_MS * 10**np.random.normal(0, 0.3)
    
    # Random SFR (independent of M_disk)
    log_SFR_random = -3 + 4 * (i % 5) / 4
    SFR_random = 10**log_SFR_random
    
    # Quenched: 30% of galaxies are quenched
    if i % 3 == 0:
        SFR_quenched = SFR_realistic * 0.01
    else:
        SFR_quenched = SFR_realistic
    
    galaxies_realistic.append((f"Galaxy_{i+1}", M_disk, R_disk, M_halo, R_halo, kappa, SFR_realistic))
    galaxies_random_sfr.append((f"Galaxy_{i+1}", M_disk, R_disk, M_halo, R_halo, kappa, SFR_random))
    galaxies_quenched.append((f"Galaxy_{i+1}", M_disk, R_disk, M_halo, R_halo, kappa, SFR_quenched))

# Print sample
print("Realistic SFR values:")
for g in galaxies_realistic[:10]:
    print(f"  M_disk={g[1]:.2e}, SFR={g[6]:.3f}, SFR/M_disk={g[6]/g[1]:.2e}")
print()

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

# Test cases
f_active_const = lambda M, k, s: 0.05
r_core_frac_const = lambda M, k, s: 0.25
scale_const = lambda M, k, s: 0.15

f_active_sfr = lambda M, k, s: max(0.001, min(0.3, 0.02 + 0.01 * math.log10(s + 1)))
f_active_best = lambda M, k, s: max(0.001, min(0.3, 0.015 + 0.003 * math.log10(s + 1)))

# Pure MASS-DEPENDENT (the original "Limitation 25" attempt)
f_active_md = lambda M, k, s: 0.05
r_core_frac_md = lambda M, k, s: 0.25
scale_md = lambda M, k, s: max(0.05, min(0.5, 0.00411 * k**1.1))

print("=" * 80)
print("REALISTIC SFR TESTS")
print("=" * 80)
print()
print("Case 1: Random SFR (previous test, INFLATED improvement)")
for name, galaxies, label in [
    ('Random SFR (independent)', galaxies_random_sfr, 'random'),
    ('Realistic SFR (correlated with M_star)', galaxies_realistic, 'realistic'),
    ('Quenched (30% low SFR)', galaxies_quenched, 'quenched'),
]:
    print()
    print(f"  --- {label} SFR ---")
    for case_name, (f_func, r_func, s_func) in {
        'Single (baseline)': (f_active_const, r_core_frac_const, scale_const),
        'f_active ∝ log(SFR) [a=0.02, b=0.01]': (f_active_sfr, r_core_frac_const, scale_const),
        'f_active ∝ log(SFR) [a=0.015, b=0.003]': (f_active_best, r_core_frac_const, scale_const),
        'scale ∝ kappa^1.1 (mass-dep)': (f_active_md, r_core_frac_md, scale_md),
    }.items():
        result = evaluate(galaxies, f_func, r_func, s_func)
        print(f"    {case_name:<55s} median={result['median']:.3f}, within 20%={result['within_20%']:.1f}%")
