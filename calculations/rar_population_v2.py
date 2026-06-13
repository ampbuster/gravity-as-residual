#!/usr/bin/env python3
"""
Population test with more careful mass-dependent parameter choices.
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

# Generate 30 galaxies with VARYING kappa
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

def evaluate(galaxies, f_active_func, r_core_frac_func, scale_func, add_noise=True):
    all_diffs = []
    per_galaxy_medians = []
    for name, M_disk, R_disk, M_halo, R_halo, kappa in galaxies:
        f_active = f_active_func(M_halo, kappa)
        r_core_frac = r_core_frac_func(M_halo, kappa)
        scale = scale_func(M_halo, kappa)
        
        gal_diffs = []
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
                gal_diffs.append(abs(diff))
        if gal_diffs:
            per_galaxy_medians.append(np.median(gal_diffs))
    
    return {
        'median': np.median(all_diffs),
        'median_gal': np.median(per_galaxy_medians),
        'mean': np.mean(all_diffs),
        'within_20%': sum(1 for d in all_diffs if d < 0.2) / len(all_diffs) * 100,
    }

# Try various functional forms
cases = {}

# Baseline
cases['Single (baseline)'] = (
    lambda M, k: 0.05,
    lambda M, k: 0.25,
    lambda M, k: 0.15,
)

# In the cascade, the "active" DM is f_active * kappa of the stellar mass
# If the baryon fraction is constant, then the active mass fraction is the same
# f_active * kappa * M_stellar / M_total
# M_stellar / M_total = 1 / (1 + kappa)
# So active mass fraction = f_active * kappa / (1 + kappa) ~ f_active for large kappa
# 
# This means f_active is actually INDEPENDENT of kappa in the cascade
# (active mass fraction is ~ f_active for any kappa)
# 
# So f_active should be constant, not kappa-dependent
# 
# What about scale?
# scale = M_cascade / M_empirical
# The cascade's M_halo is determined by the cumulative 2D universe gravity
# This is M_2D = G_4D * (sum of all 2D universe masses) * T_universe
# 
# In a galaxy, the baryonic mass distribution creates 2D universes
# More mass = more 2D universes
# But the spatial distribution also matters
# 
# Hmm let me think
# 
# Maybe scale should scale with kappa
# In a high-kappa system (cluster), M_halo / M_stellar is large
# The baryon fraction is small
# The empirical M_halo is dominated by 2D universe gravity
# 
# In a low-kappa system (dwarf galaxy), M_halo / M_stellar is small
# The baryon fraction is large
# The empirical M_halo is dominated by stars
# 
# Hmm but this would predict scale = 1 for high-kappa and small for low-kappa
# Which is what we see! (0.1 for MW, 0.7 for cluster)
# 
# So scale ∝ kappa^1.1 (from the previous analysis)
# This is a real prediction

cases['scale ∝ kappa^1.1'] = (
    lambda M, k: 0.05,
    lambda M, k: 0.2,
    lambda M, k: max(0.05, min(0.7, 0.00411 * k**1.1)),
)

# f_active as the gas consumption / cosmic SFR interpolation
# At galaxy scale (kappa=17): f_active = 0.05 (gas consumption)
# At cluster scale (kappa=100): f_active = 0.18 (cosmic SFR)
# f_active = 0.05 + 0.13 * (kappa - 17) / 83
cases['f_active ∝ kappa + scale ∝ kappa^1.1'] = (
    lambda M, k: max(0.001, min(0.3, 0.05 + 0.13 * (k - 17) / 83)),
    lambda M, k: 0.2,
    lambda M, k: max(0.05, min(0.7, 0.00411 * k**1.1)),
)

# f_active constant, scale ∝ kappa^1.1 with smaller exponent
cases['scale ∝ kappa^0.5'] = (
    lambda M, k: 0.05,
    lambda M, k: 0.2,
    lambda M, k: max(0.05, min(0.7, 0.04 * k**0.5)),
)

# Best of all worlds
cases['f_active scaled + scale ∝ kappa^1.1'] = (
    lambda M, k: max(0.001, min(0.3, 0.05 + 0.10 * (k - 17) / 83)),
    lambda M, k: 0.2,
    lambda M, k: max(0.05, min(0.7, 0.00411 * k**1.1)),
)

# Smaller active contribution (best galaxy fit was f_active=0.02)
cases['f_active=0.02, scale ∝ kappa^1.1'] = (
    lambda M, k: 0.02,
    lambda M, k: 0.2,
    lambda M, k: max(0.05, min(0.7, 0.00411 * k**1.1)),
)

# Try kappa^0.7 (intermediate)
cases['scale ∝ kappa^0.7'] = (
    lambda M, k: 0.05,
    lambda M, k: 0.2,
    lambda M, k: max(0.05, min(0.7, 0.02 * k**0.7)),
)

print("=" * 80)
print("POPULATION TEST v2 - improved mass-dependent params")
print("=" * 80)
print()
for name, (f_func, r_func, s_func) in cases.items():
    result = evaluate(galaxies, f_func, r_func, s_func)
    print(f"  {name:<55s}")
    print(f"    median abs diff: {result['median']:.3f}, per-gal: {result['median_gal']:.3f}, within 20%: {result['within_20%']:.1f}%")
    print()
