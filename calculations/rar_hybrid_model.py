#!/usr/bin/env python3
"""
Hybrid DM model: cascade 2D universe gravity (10% of M_halo for MW)
plus standard NFW particle DM (90%).

This converts the 90% "missing DM" (Limitation 24) from a feature
into a testable prediction: the cascade's RAR fit should only
account for 10% of the total DM, with the rest from standard
particle DM following an NFW profile.

Test: does this hybrid model fit the RAR to a population?
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

def g_cascade(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, r_core_frac, scale_cascade):
    """Cascade's contribution: scale_cascade * M_halo (10% for MW)"""
    M_cum_total_kg = scale_cascade * (1 - f_active) * M_halo_Msun * M_sun
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

def g_NFW(r_kpc, M_halo_Msun, R_halo_kpc, c=10, scale_NFW=0.9):
    """NFW profile: rho(r) = rho_s / [(r/r_s)(1+r/r_s)^2]
    Mass within r: M(r) = 4*pi*rho_s*r_s^3 * [ln(1+r/r_s) - r/(r+r_s)]
    """
    r_m = r_kpc * kpc_to_m
    R_halo_m = R_halo_kpc * kpc_to_m
    r_s = R_halo_m / c
    # NFW characteristic density
    # M_halo = 4*pi*rho_s*r_s^3 * [ln(1+c) - c/(1+c)]
    M_halo_kg = scale_NFW * M_halo_Msun * M_sun
    factor = math.log(1 + c) - c / (1 + c)
    rho_s = M_halo_kg / (4 * math.pi * r_s**3 * factor) if factor > 0 else 0
    if r_m <= 0:
        return 0
    # Enclosed mass
    x = r_m / r_s
    M_enclosed = 4 * math.pi * rho_s * r_s**3 * (math.log(1 + x) - x / (1 + x))
    return G * M_enclosed / r_m**2

def g_hybrid(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, 
             f_active=0.05, r_core_frac=0.25, scale_cascade=0.1, scale_NFW=0.9, c=10):
    """Hybrid: cascade (10% of M_halo) + NFW (90% of M_halo)"""
    g_cas = g_cascade(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, r_core_frac, scale_cascade)
    g_nfw = g_NFW(r_kpc, M_halo_Msun, R_halo_kpc, c, scale_NFW)
    return g_cas + g_nfw

# Test on MW first
M_disk, R_disk, M_halo, R_halo = 6e10, 4, 1e12, 30

print("=" * 80)
print("HYBRID MODEL: cascade (10%) + NFW (90%) for MW")
print("=" * 80)
print()
print(f"  MW: M_disk = {M_disk:.1e}, R_disk = {R_disk}, M_halo = {M_halo:.1e}, R_halo = {R_halo}")
print()

print(f"  {'r (kpc)':>8s}  {'g_bar':>12s}  {'g_cas':>12s}  {'g_NFW':>12s}  {'g_obs_hyb':>12s}  {'g_obs_RAR':>12s}  {'diff':>8s}")
print()

for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]:
    g_b = g_bar_disk(r, M_disk, R_disk)
    if g_b <= 0:
        continue
    g_cas = g_cascade(r, M_disk, R_disk, M_halo, R_halo, 0.05, 0.25, 0.1)
    g_nfw = g_NFW(r, M_halo, R_halo, c=10, scale_NFW=0.9)
    g_obs = g_b + g_cas + g_nfw
    g_obs_rar = rar(g_b, g_plus_galaxy)
    diff = (g_obs - g_obs_rar) / g_obs_rar
    print(f"  {r:>8.1f}  {g_b:>12.3e}  {g_cas:>12.3e}  {g_nfw:>12.3e}  {g_obs:>12.3e}  {g_obs_rar:>12.3e}  {diff:>8.2f}")

print()
print("OBSERVATION: NFW dominates by 9x over cascade, so the cascade's")
print("             contribution to g_obs is small. The fit is mostly NFW + g_bar.")
print()

# Now test on population with hybrid model
print("=" * 80)
print("POPULATION TEST: hybrid model with VARYING kappa")
print("=" * 80)
print()

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
    galaxies.append((f"Galaxy_{i+1}", M_disk, R_disk, M_halo, R_halo, kappa))

def evaluate(galaxies, f_active_func, r_core_frac_func, scale_cascade_func, scale_NFW_func=0.9, c=10, add_noise=True):
    all_diffs = []
    per_galaxy_medians = []
    for name, M_disk, R_disk, M_halo, R_halo, kappa in galaxies:
        f_active = f_active_func(M_halo, kappa)
        r_core_frac = r_core_frac_func(M_halo, kappa)
        scale_cascade = scale_cascade_func(M_halo, kappa)
        scale_NFW = scale_NFW_func(M_halo, kappa) if callable(scale_NFW_func) else scale_NFW_func
        
        gal_diffs = []
        test_radii = [0.3*R_disk, 1*R_disk, 2*R_disk, 4*R_disk, 6*R_disk]
        for r in test_radii:
            if r > R_halo * 0.9:
                continue
            g_b = g_bar_disk(r, M_disk, R_disk)
            if g_b <= 0:
                continue
            g_cas = g_cascade(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, scale_cascade)
            g_nfw = g_NFW(r, M_halo, R_halo, c, scale_NFW)
            g_obs = g_b + g_cas + g_nfw
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
        'mean': np.mean(all_diffs),
        'within_20%': sum(1 for d in all_diffs if d < 0.2) / len(all_diffs) * 100,
    }

# Test cases
cases = {}

# Baseline: pure cascade (Limitation 25)
cases['Pure cascade (baseline)'] = (
    lambda M, k: 0.05, lambda M, k: 0.25, lambda M, k: 0.15,
    0  # scale_NFW = 0 means no NFW
)

# Hybrid 1: 10% cascade + 90% NFW (constant)
cases['Hybrid: 10% cascade + 90% NFW (const)'] = (
    lambda M, k: 0.05, lambda M, k: 0.25, lambda M, k: 0.1,
    0.9
)

# Hybrid 2: 30% cascade + 70% NFW
cases['Hybrid: 30% cascade + 70% NFW'] = (
    lambda M, k: 0.05, lambda M, k: 0.25, lambda M, k: 0.3,
    0.7
)

# Hybrid 3: 70% cascade + 30% NFW (Limitation 24 says scale=0.7 for cluster)
cases['Hybrid: 70% cascade + 30% NFW'] = (
    lambda M, k: 0.05, lambda M, k: 0.25, lambda M, k: 0.7,
    0.3
)

# Hybrid 4: mass-dependent cascade + mass-dependent NFW
# scale_cascade = 0.00411 * kappa^1.1, NFW = 1 - cascade
cases['Hybrid: cascade(kappa^1.1) + NFW(1-cascade)'] = (
    lambda M, k: 0.05, lambda M, k: 0.25, 
    lambda M, k: max(0.05, min(0.7, 0.00411 * k**1.1)),
    lambda M, k: max(0.3, min(0.95, 1 - 0.00411 * k**1.1))
)

# Hybrid 5: 50/50 split
cases['Hybrid: 50% cascade + 50% NFW'] = (
    lambda M, k: 0.05, lambda M, k: 0.25, lambda M, k: 0.5,
    0.5
)

# Pure NFW
cases['Pure NFW (sanity check)'] = (
    lambda M, k: 0, lambda M, k: 0, lambda M, k: 0,
    1.0
)

for name, (f_func, r_func, s_func, nfw) in cases.items():
    if name == 'Pure NFW (sanity check)':
        # Special case: no cascade
        result = evaluate(galaxies, lambda M, k: 0, lambda M, k: 0, lambda M, k: 0, 1.0)
    else:
        if callable(nfw):
            result = evaluate(galaxies, f_func, r_func, s_func, nfw)
        else:
            result = evaluate(galaxies, f_func, r_func, s_func, nfw)
    print(f"  {name:<55s}")
    print(f"    median abs diff: {result['median']:.3f}, per-gal: {result['median_gal']:.3f}, within 20%: {result['within_20%']:.1f}%")
    print()
