#!/usr/bin/env python3
"""
Test: does SFR-dependent f_active help the cascade fit a galaxy population?

Hypothesis: f_active should be higher in actively star-forming galaxies
(because they're currently creating 2D universes) and lower in quenched
galaxies (because they're not).

If true, the cascade's RAR scatter should correlate with SFR.
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

# Generate 30 galaxies with VARYING SFR
np.random.seed(42)
M_halo_values = np.logspace(8, 13, 30)
galaxies = []
for i, M_halo in enumerate(M_halo_values):
    kappa = 5 + (i % 10) * 10
    M_disk = M_halo / kappa
    R_disk = 4 * (M_halo / 1e12) ** 0.4
    if R_disk < 0.2:
        R_disk = 0.2
    R_halo = 8 * R_disk
    # SFR: log-uniform from 0.001 to 10 M_sun/yr
    log_SFR = -3 + 4 * (i % 5) / 4
    SFR = 10**log_SFR
    galaxies.append((f"Galaxy_{i+1}", M_disk, R_disk, M_halo, R_halo, kappa, SFR))

def evaluate(galaxies, f_active_func, r_core_frac_func, scale_func, add_noise=True):
    all_diffs = []
    per_galaxy_medians = []
    sfr_values = []
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
            sfr_values.append(SFR)
    
    return {
        'median': np.median(all_diffs),
        'median_gal': np.median(per_galaxy_medians),
        'mean': np.mean(all_diffs),
        'within_20%': sum(1 for d in all_diffs if d < 0.2) / len(all_diffs) * 100,
        'sfr': sfr_values,
        'medians': per_galaxy_medians,
    }

# Test 1: Single params (baseline)
f_active_const = lambda M, k, s: 0.05
r_core_frac_const = lambda M, k, s: 0.25
scale_const = lambda M, k, s: 0.15

# Test 2: f_active depends on SFR
# f_active = f_base + f_SFR * log10(SFR)
# Higher SFR = more 2D universe creation = higher f_active
f_active_sfr = lambda M, k, s: max(0.001, min(0.3, 0.02 + 0.01 * math.log10(s + 1)))
r_core_frac_sfr = lambda M, k, s: 0.25
scale_sfr = lambda M, k, s: 0.15

# Test 3: f_active depends on sSFR (specific SFR = SFR / M_disk)
# f_active_sSFR = f_base * sSFR / sSFR_ref
# But sSFR is per galaxy, varies a lot

# Test 4: SFR-dependent scale
# Higher SFR = more 2D universes = more cumulative return = larger scale
scale_sfr = lambda M, k, s: max(0.05, min(0.5, 0.1 + 0.05 * math.log10(s + 1)))

# Test 5: BOTH f_active and scale depend on SFR
f_active_both_sfr = lambda M, k, s: max(0.001, min(0.3, 0.02 + 0.01 * math.log10(s + 1)))
scale_both_sfr = lambda M, k, s: max(0.05, min(0.5, 0.1 + 0.05 * math.log10(s + 1)))

# Test 6: sSFR dependence (mass-normalized)
# sSFR = SFR / M_disk
# f_active = 0.05 * sqrt(sSFR / sSFR_MW)
# MW sSFR ~ 1e-10 /yr
sSFR_ref = 1e-10
f_active_sSFR = lambda M, k, s: 0.05 * math.sqrt((s / M) / sSFR_ref) if M > 0 else 0.05

print("=" * 80)
print("SFR-DEPENDENT PARAMETERS")
print("=" * 80)
print()

cases = {
    'Single (baseline)': (f_active_const, r_core_frac_const, scale_const),
    'f_active ∝ log(SFR)': (f_active_sfr, r_core_frac_const, scale_const),
    'scale ∝ log(SFR)': (f_active_const, r_core_frac_const, scale_sfr),
    'f_active + scale ∝ log(SFR)': (f_active_both_sfr, r_core_frac_const, scale_both_sfr),
    'f_active ∝ sqrt(sSFR/sSFR_MW)': (f_active_sSFR, r_core_frac_const, scale_const),
}

for name, (f_func, r_func, s_func) in cases.items():
    result = evaluate(galaxies, f_func, r_func, s_func)
    print(f"  {name:<55s}")
    print(f"    median abs diff: {result['median']:.3f}, per-gal: {result['median_gal']:.3f}, within 20%: {result['within_20%']:.1f}%")
    print()
