#!/usr/bin/env python3
"""
Compare mass-dependent parameters using the same metric as commit 128.
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

def g_DM_iso(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, r_core_frac, scale):
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

# Generate 30 galaxies
np.random.seed(42)
M_halo_values = np.logspace(7, 12, 30)
galaxies = []
for i, M_halo in enumerate(M_halo_values):
    M_disk = 0.05 * M_halo
    R_disk = 4 * (M_halo / 1e12) ** 0.4
    if R_disk < 0.2:
        R_disk = 0.2
    R_halo = 8 * R_disk
    galaxies.append((f"Galaxy_{i+1}", M_disk, R_disk, M_halo, R_halo))

def evaluate(galaxies, f_active_func, r_core_frac_func, scale_func, add_noise=False):
    """Evaluate the cascade model with mass-dependent params"""
    all_diffs = []
    per_galaxy_medians = []
    for name, M_disk, R_disk, M_halo, R_halo in galaxies:
        kappa = M_halo / M_disk
        f_active = f_active_func(M_halo, kappa)
        r_core_frac = r_core_frac_func(M_halo, kappa)
        scale = scale_func(M_halo, kappa)
        
        # 5 test radii per galaxy
        test_radii = [0.3*R_disk, 1*R_disk, 2*R_disk, 4*R_disk, 6*R_disk]
        for r in test_radii:
            if r > R_halo * 0.9:
                continue
            g_b = g_bar_disk(r, M_disk, R_disk)
            if g_b <= 0:
                continue
            g_dm = g_DM_iso(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, scale)
            g_obs = g_b + g_dm
            g_obs_rar = rar(g_b, g_plus_galaxy)
            if g_obs_rar > 0:
                diff = (g_obs - g_obs_rar) / g_obs_rar
                if add_noise:
                    diff += np.random.normal(0, 0.1)
                all_diffs.append(abs(diff))
        per_galaxy_medians.append(np.median(all_diffs[-5:]) if len(all_diffs) >= 5 else np.nan)
    
    return {
        'median': np.median(all_diffs),
        'mean': np.mean(all_diffs),
        'within_20%': sum(1 for d in all_diffs if d < 0.2) / len(all_diffs) * 100,
    }

# Single params (baseline)
f_active_const = lambda M, k: 0.05
r_core_frac_const = lambda M, k: 0.25
scale_const = lambda M, k: 0.15

# Mass-dependent
f_active_md = lambda M, k: max(0.001, min(0.3, 0.01 + 0.01 * (math.log10(M) - 7)))
r_core_frac_md = lambda M, k: 0.25
scale_md = lambda M, k: max(0.01, min(0.5, 0.1 + 0.3 * (math.log10(M) - 12) / 2))

# Best result from previous analysis (commits 117-118):
# MW: f_active=0.05, scale=0.1
# Cluster: f_active=0.05, scale=0.7
# Interpolation: scale = 0.1 + 0.3 * (log10(M) - 12)/2
f_active_phys = lambda M, k: 0.05
r_core_frac_phys = lambda M, k: 0.2
scale_phys = lambda M, k: max(0.05, min(0.7, 0.1 + 0.3 * (math.log10(M) - 12) / 2))

# Mass-dependent f_active based on the MCMC result (gas consumption ~ 0.7 Gyr)
# at galaxy scale, but cosmic SFR (~2.5 Gyr) at cluster scale
# f_active goes from 0.05 to 0.18
f_active_phys2 = lambda M, k: max(0.01, min(0.3, 0.05 + 0.13 * (math.log10(M) - 12) / 2))
r_core_frac_phys2 = lambda M, k: 0.2
scale_phys2 = lambda M, k: max(0.05, min(0.7, 0.1 + 0.3 * (math.log10(M) - 12) / 2))

print("=" * 80)
print("POPULATION METRICS - mass-dependent parameter tests")
print("=" * 80)
print()

cases = {
    'Single (baseline, commit 128)': (f_active_const, r_core_frac_const, scale_const),
    'Phys (interp scale 0.1->0.7)': (f_active_phys, r_core_frac_phys, scale_phys),
    'Phys2 (interp f_active 0.05->0.18 AND scale)': (f_active_phys2, r_core_frac_phys2, scale_phys2),
    'log-mass f_active': (f_active_md, r_core_frac_md, scale_md),
}

for name, (f_func, r_func, s_func) in cases.items():
    result = evaluate(galaxies, f_func, r_func, s_func, add_noise=True)
    print(f"  {name:<50s}")
    print(f"    median abs diff: {result['median']:.3f}")
    print(f"    mean abs diff:   {result['mean']:.3f}")
    print(f"    within 20%:      {result['within_20%']:.1f}%")
    print()

# The 29% baseline is with synthetic noise. Let me also do noise-free
print("=" * 80)
print("NOISE-FREE COMPARISON")
print("=" * 80)
print()

for name, (f_func, r_func, s_func) in cases.items():
    result = evaluate(galaxies, f_func, r_func, s_func, add_noise=False)
    print(f"  {name:<50s}")
    print(f"    median abs diff: {result['median']:.3f}")
    print(f"    mean abs diff:   {result['mean']:.3f}")
    print(f"    within 20%:      {result['within_20%']:.1f}%")
    print()
