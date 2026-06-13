#!/usr/bin/env python3
"""
RAR with NFW-like cumulative profile (cuspy version).

Hypothesis: the cumulative dark matter is NOT uniformly distributed, but
follows a cuspy profile similar to NFW. The mixing "smooths" the inner
profile but doesn't make it uniform. This is option E above.

This is a more physical model: the cumulative return comes from many
events, each of which would be ~clustered. Without mixing, the
cumulative is highly clustered. With mixing, the inner profile smooths
out but the outer profile stays cuspy.
"""

import math

# Constants
G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
age_universe_s = 13.8e9 * 3.15e7

# Empirical RAR scales
g_plus_McGaugh = 1.2e-10  # m/s^2 (galaxies)
g_plus_Tian_cluster = 17 * g_plus_McGaugh  # 17x for clusters

# Galaxy types
galaxies = [
    ('Milky Way', 6e10, 4, 1e12, 30, 2.5, g_plus_McGaugh),
    ('Dwarf (EDGE 2025)', 1e7, 1, 1e9, 5, 20.0, 1.5e-10),
    ('Cluster (Tian 2024)', 1e12, 30, 1e14, 500, 50.0, g_plus_Tian_cluster),
]

def v_circ_total(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, c=10):
    r_m = r_kpc * kpc_to_m
    if r_m <= 0:
        return 0
    M_disk_enclosed = M_disk_Msun * M_sun * (1 - (1 + r_m/(R_disk_kpc * kpc_to_m)) * math.exp(-r_m/(R_disk_kpc * kpc_to_m)))
    R_s_kpc = R_halo_kpc / c
    x = r_kpc / R_s_kpc
    f_c = math.log(1+c) - c/(1+c)
    f_r = math.log(1+x) - x/(1+x)
    M_halo_enclosed = M_halo_Msun * M_sun * f_r / f_c if f_c > 0 else 0
    M_total = M_disk_enclosed + M_halo_enclosed
    return math.sqrt(G * M_total / r_m)

def g_bar(r_kpc, M_disk_Msun, R_disk_kpc):
    r_m = r_kpc * kpc_to_m
    if r_m <= 0:
        return 0
    M_disk_enclosed = M_disk_Msun * M_sun * (1 - (1 + r_m/(R_disk_kpc * kpc_to_m)) * math.exp(-r_m/(R_disk_kpc * kpc_to_m)))
    return G * M_disk_enclosed / r_m**2

def g_DM_power_law(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, alpha):
    """
    Power-law cumulative profile:
      rho_cum(r) = rho_0 * (R_cum / max(r, R_core))^alpha
    
    alpha=0: uniform
    alpha=1: 1/r (log divergent)
    alpha=2: 1/r^2 (isothermal, g_cum=const outside core)
    alpha=3: NFW-like inner (cuspy)
    
    Active: clustered, follows stellar profile with kappa
    """
    # Compute normalization: integrate rho_cum over halo
    # For alpha < 3, integral converges in finite volume
    R_halo_m = R_halo_kpc * kpc_to_m
    R_core = 0.1 * R_halo_m  # core radius (small fraction of R_halo)
    r_m = r_kpc * kpc_to_m
    r_eff = max(r_m, R_core)
    
    # Mixing factor (mimics dynamical mixing)
    v_c = v_circ_total(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc)
    t_dyn = 2 * math.pi * r_m / v_c if v_c > 0 else age_universe_s
    N_orbits = age_universe_s / t_dyn if t_dyn > 0 else 0
    f_mix = 1 - math.exp(-N_orbits / 10)  # N_crit = 10
    
    # Cumulative profile
    # rho_cum_total integrated over halo should give f_cum * M_halo
    f_cum = 1 - f_active
    M_cum_total_kg = f_cum * M_halo_Msun * M_sun
    
    # For alpha < 3, the integral is finite
    # rho_cum(r) = rho_0 * (R_core / r_eff)^alpha for r > R_core
    # rho_0 = (3-alpha) * M_cum_total / (4*pi * R_core^3 * (R_halo/R_core)^(3-alpha) - R_core^3)
    # Simplified: assume the profile is well-fit by a power law from R_core to R_halo
    
    if alpha < 3:
        # Integral from R_core to R_halo of (R_core/r)^alpha * 4*pi*r^2 dr
        # = 4*pi*R_core^alpha * (R_halo^(3-alpha) - R_core^(3-alpha)) / (3-alpha)
        integral = 4 * math.pi * R_core**alpha * (R_halo_m**(3-alpha) - R_core**(3-alpha)) / (3-alpha)
    else:
        # alpha >= 3: divergent in infinite volume, but truncated at R_halo
        integral = 4 * math.pi * R_core**3 * math.log(R_halo_m / R_core)
    
    rho_0 = M_cum_total_kg / integral
    rho_cum = rho_0 * (R_core / r_eff) ** alpha
    
    # Clustered (stellar-like) profile for active contribution
    M_disk = M_disk_Msun * M_sun
    R_d = R_disk_kpc * kpc_to_m
    h_z = 0.1 * R_d
    Sigma_0 = M_disk / (2 * math.pi * R_d**2)
    Sigma_r = Sigma_0 * math.exp(-r_kpc / R_disk_kpc)
    rho_stellar = Sigma_r / (2 * h_z)
    kappa = M_halo_Msun / M_disk_Msun if M_disk_Msun > 0 else 0
    
    # Active contribution (clustered)
    rho_active = f_active * kappa * rho_stellar
    
    # Total DM density
    rho_DM_total = rho_cum + rho_active
    
    # g_DM = G * M_DM_enclosed / r^2
    # For power-law: M_cum_enclosed(r) = integral from 0 to r
    if r_m < R_core:
        # Inside core: assume uniform
        M_cum_enclosed = rho_0 * (4/3) * math.pi * r_m**3
    elif alpha < 3:
        # Outside core: integrate from R_core to r
        M_cum_enclosed = rho_0 * 4 * math.pi * R_core**alpha * (r_m**(3-alpha) - R_core**(3-alpha)) / (3-alpha) + rho_0 * (4/3) * math.pi * R_core**3
    else:
        # alpha >= 3
        M_cum_enclosed = rho_0 * 4 * math.pi * R_core**3 * math.log(r_m / R_core) + rho_0 * (4/3) * math.pi * R_core**3
    
    M_active_enclosed = f_active * kappa * M_disk * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    M_DM_enclosed = M_cum_enclosed + M_active_enclosed
    
    g_dm = G * M_DM_enclosed / r_m**2 if r_m > 0 else 0
    return g_dm, f_mix

# Grid search over alpha
print("=" * 70)
print("POWER-LAW CUMULATIVE PROFILE SEARCH")
print("=" * 70)
print()
print(f"{'alpha':>8s}  {'f_active':>10s}  {'MW':>10s}  {'Dwarf':>10s}  {'Cluster':>10s}  {'log_err':>10s}")
print("-" * 70)

best = None
best_err = float('inf')

for alpha in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
    for f_active in [0.05, 0.1, 0.15, 0.2, 0.3, 0.5]:
        results = []
        total_err = 0
        for name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus in galaxies:
            r_test = 2 * R_disk
            g_dm, f_mix = g_DM_power_law(r_test, M_disk, R_disk, M_halo, R_halo, f_active, alpha)
            g_b = g_bar(r_test, M_disk, R_disk)
            g_obs = g_b + g_dm
            model_ratio = g_obs / g_b if g_b > 0 else 1
            err = (math.log(model_ratio / target_ratio))**2
            total_err += err
            results.append(model_ratio)
        
        if total_err < best_err:
            best_err = total_err
            best = (alpha, f_active, results)
        
        if alpha in [1.0, 1.5, 2.0, 2.5]:
            print(f"{alpha:>8.2f}  {f_active:>10.2f}  {results[0]:>10.2f}  {results[1]:>10.2f}  {results[2]:>10.2f}  {total_err:>10.3f}")

print()
print(f"BEST FIT: alpha={best[0]}, f_active={best[1]}, log_err={best_err:.3f}")
print(f"  MW:     g_obs/g_bar = {best[2][0]:.2f} (target 2.5)")
print(f"  Dwarf:  g_obs/g_bar = {best[2][1]:.2f} (target 20)")
print(f"  Cluster: g_obs/g_bar = {best[2][2]:.2f} (target 50)")

# Compare to best case
print()
print("Best case predictions:")
alpha, f_active, _ = best
for name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus in galaxies:
    r_test = 2 * R_disk
    g_dm, f_mix = g_DM_power_law(r_test, M_disk, R_disk, M_halo, R_halo, f_active, alpha)
    g_b = g_bar(r_test, M_disk, R_disk)
    g_obs = g_b + g_dm
    if g_obs > g_b * 1.01:
        arg = 1 - g_b / g_obs
        if 0 < arg < 1:
            g_plus_eff = g_b / (math.log(arg))**2
        else:
            g_plus_eff = float('inf')
    else:
        g_plus_eff = 0
    print(f"  {name}: g_obs/g_bar = {g_obs/g_b:.2f} (target {target_ratio}), g_+ = {g_plus_eff:.2e} (target {target_g_plus:.2e})")
