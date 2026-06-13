#!/usr/bin/env python3
"""
Make the cascade's RAR fit generalize to a population of galaxies.

The single-parameter MW fit gives 5-13% residuals.
The 30-galaxy test (commit 128) gives 29% median residual.

The issue: parameters tuned for the MW don't generalize.

Solution: make parameters mass-dependent.
Try: f_active as a function of kappa, scale as a function of M_halo.
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

# Try MASS-DEPENDENT parameters
# f_active ∝ kappa (more active DM in clusters)
# scale ∝ kappa^1.1 (from the previous analysis)
# r_core_frac = constant (universal)

print("=" * 80)
print("MASS-DEPENDENT PARAMETERS")
print("=" * 80)
print()

# Test 1: f_active = 0.05 + 0.001 * log10(M_halo)
# f_active increases with mass (from gas consumption to cosmic SFR)

# Test 2: f_active = kappa / 100 (cluster-like for high kappa)

# Test 3: scale = scale_MW * (M_halo / 1e12)^0.3 (mass-dependent)

# Try several mass-dependent scalings
results = {}

# Case 1: f_active ∝ log10(M_halo)
print("Case 1: f_active = 0.01 + 0.005 * log10(M_halo / 1e7)")
total_chi2 = 0
total_n = 0
for name, M_disk, R_disk, M_halo, R_halo in galaxies:
    f_active = 0.01 + 0.005 * (math.log10(M_halo) - 7)
    f_active = max(0.001, min(0.5, f_active))
    r_core_frac = 0.25
    scale = 0.15
    test_radii = [0.5*R_disk, 1*R_disk, 2*R_disk, 4*R_disk, 0.7*R_halo]
    for r in test_radii:
        g_b = g_bar_disk(r, M_disk, R_disk)
        if g_b <= 0:
            continue
        g_dm = g_DM_iso(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, scale)
        g_obs = g_b + g_dm
        g_obs_rar = rar(g_b, g_plus_galaxy)
        if g_obs_rar > 0:
            total_chi2 += (math.log(g_obs / g_obs_rar))**2
            total_n += 1
print(f"  Total chi^2: {total_chi2:.2f}, mean log_err: {total_chi2/total_n:.4f}")
results['case1'] = total_chi2/total_n

# Case 2: f_active = 0.05 + 0.05 * (kappa - 17) / 83
# For MW (kappa=17): f_active = 0.05
# For cluster (kappa=100): f_active = 0.10
print()
print("Case 2: f_active = 0.05 + 0.05 * (kappa - 17) / 83")
total_chi2 = 0
total_n = 0
for name, M_disk, R_disk, M_halo, R_halo in galaxies:
    kappa = M_halo / M_disk
    f_active = 0.05 + 0.05 * (kappa - 17) / 83
    f_active = max(0.001, min(0.5, f_active))
    r_core_frac = 0.25
    scale = 0.15
    test_radii = [0.5*R_disk, 1*R_disk, 2*R_disk, 4*R_disk, 0.7*R_halo]
    for r in test_radii:
        g_b = g_bar_disk(r, M_disk, R_disk)
        if g_b <= 0:
            continue
        g_dm = g_DM_iso(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, scale)
        g_obs = g_b + g_dm
        g_obs_rar = rar(g_b, g_plus_galaxy)
        if g_obs_rar > 0:
            total_chi2 += (math.log(g_obs / g_obs_rar))**2
            total_n += 1
print(f"  Total chi^2: {total_chi2:.2f}, mean log_err: {total_chi2/total_n:.4f}")
results['case2'] = total_chi2/total_n

# Case 3: scale = 0.15 * (M_halo / 1e12)^0.3
print()
print("Case 3: scale = 0.15 * (M_halo / 1e12)^0.3")
total_chi2 = 0
total_n = 0
for name, M_disk, R_disk, M_halo, R_halo in galaxies:
    f_active = 0.05
    r_core_frac = 0.25
    scale = 0.15 * (M_halo / 1e12) ** 0.3
    scale = max(0.01, min(0.5, scale))
    test_radii = [0.5*R_disk, 1*R_disk, 2*R_disk, 4*R_disk, 0.7*R_halo]
    for r in test_radii:
        g_b = g_bar_disk(r, M_disk, R_disk)
        if g_b <= 0:
            continue
        g_dm = g_DM_iso(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, scale)
        g_obs = g_b + g_dm
        g_obs_rar = rar(g_b, g_plus_galaxy)
        if g_obs_rar > 0:
            total_chi2 += (math.log(g_obs / g_obs_rar))**2
            total_n += 1
print(f"  Total chi^2: {total_chi2:.2f}, mean log_err: {total_chi2/total_n:.4f}")
results['case3'] = total_chi2/total_n

# Case 4: BOTH mass-dependent (f_active ∝ kappa, scale ∝ M^0.3)
print()
print("Case 4: BOTH f_active (kappa) AND scale (M^0.3)")
total_chi2 = 0
total_n = 0
for name, M_disk, R_disk, M_halo, R_halo in galaxies:
    kappa = M_halo / M_disk
    f_active = 0.05 + 0.05 * (kappa - 17) / 83
    f_active = max(0.001, min(0.5, f_active))
    r_core_frac = 0.25
    scale = 0.15 * (M_halo / 1e12) ** 0.3
    scale = max(0.01, min(0.5, scale))
    test_radii = [0.5*R_disk, 1*R_disk, 2*R_disk, 4*R_disk, 0.7*R_halo]
    for r in test_radii:
        g_b = g_bar_disk(r, M_disk, R_disk)
        if g_b <= 0:
            continue
        g_dm = g_DM_iso(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, scale)
        g_obs = g_b + g_dm
        g_obs_rar = rar(g_b, g_plus_galaxy)
        if g_obs_rar > 0:
            total_chi2 += (math.log(g_obs / g_obs_rar))**2
            total_n += 1
print(f"  Total chi^2: {total_chi2:.2f}, mean log_err: {total_chi2/total_n:.4f}")
results['case4'] = total_chi2/total_n

# Case 5: scale = 0.7 at cluster, 0.1 at MW, linear in log M
print()
print("Case 5: scale = 0.1 + 0.6 * (log10(M_halo) - 12) / 2 (linear in log M)")
total_chi2 = 0
total_n = 0
for name, M_disk, R_disk, M_halo, R_halo in galaxies:
    f_active = 0.05
    r_core_frac = 0.25
    log_M = math.log10(M_halo)
    if log_M < 12:
        scale = 0.1
    elif log_M > 14:
        scale = 0.7
    else:
        scale = 0.1 + 0.3 * (log_M - 12)
    test_radii = [0.5*R_disk, 1*R_disk, 2*R_disk, 4*R_disk, 0.7*R_halo]
    for r in test_radii:
        g_b = g_bar_disk(r, M_disk, R_disk)
        if g_b <= 0:
            continue
        g_dm = g_DM_iso(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, scale)
        g_obs = g_b + g_dm
        g_obs_rar = rar(g_b, g_plus_galaxy)
        if g_obs_rar > 0:
            total_chi2 += (math.log(g_obs / g_obs_rar))**2
            total_n += 1
print(f"  Total chi^2: {total_chi2:.2f}, mean log_err: {total_chi2/total_n:.4f}")
results['case5'] = total_chi2/total_n

# Compare to baseline (single params)
print()
print("=" * 80)
print("COMPARISON")
print("=" * 80)
print()
print("  Case                                        log_err    vs single-params (0.219)")
print("  " + "-" * 70)
print(f"  Single params (f_active=0.05, scale=0.15)  0.219      (baseline, commit 128)")
for name, err in results.items():
    improvement = (0.219 - err) / 0.219 * 100
    print(f"  {name:<40s}  {err:.4f}    ({improvement:+.1f}%)")
