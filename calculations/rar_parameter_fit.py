#!/usr/bin/env python3
"""
Trial-and-error parameter search for the cascade's dynamical-mixing model.

Goal: find f_active, f_cum, N_crit, kappa, and any other tunable parameters
that best match the empirical RAR across the mass spectrum.

Empirical targets (from McGaugh+ 2016, EDGE 2025, Tian 2024):
- Galaxy (R~8 kpc, M_halo=1e12): g_obs/g_bar ~ 2.5, effective g_+ ~ 1.2e-10
- Dwarf (R~2 kpc, M_halo=1e9): g_obs/g_bar ~ 10-30, EDGE dwarfs above RAR
- Cluster (R~60 kpc, M_halo=1e14): g_obs/g_bar ~ 50 with g_+ 17x galaxy
"""

import math

# Constants
G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
age_universe_s = 13.8e9 * 3.15e7

# Empirical targets
g_plus_McGaugh = 1.2e-10  # m/s^2 (galaxies)

# Galaxy types with empirical targets
galaxies = [
    # (name, M_disk, R_disk, M_halo, R_halo, target_g_obs_g_bar, target_g_plus)
    ('Milky Way', 6e10, 4, 1e12, 30, 2.5, g_plus_McGaugh),
    ('Dwarf (EDGE 2025)', 1e7, 1, 1e9, 5, 20.0, 1.5e-10),  # EDGE: above RAR
    ('Cluster (Tian 2024)', 1e12, 30, 1e14, 500, 50.0, 17 * g_plus_McGaugh),
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

def g_DM_mixing(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, N_crit):
    """Compute g_DM with mixing model. f_cum is implicit (1-f_active)."""
    v_c = v_circ_total(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc)
    r_m = r_kpc * kpc_to_m
    t_dyn = 2 * math.pi * r_m / v_c if v_c > 0 else age_universe_s
    N_orbits = age_universe_s / t_dyn if t_dyn > 0 else 0
    f_mix = 1 - math.exp(-N_orbits / N_crit)
    
    # kappa (the effective ratio)
    kappa = M_halo_Msun / M_disk_Msun if M_disk_Msun > 0 else 0
    
    # Cumulative contribution (mixed)
    # Uniform component: M_cum / (4/3 pi R^3) = f_cum * M_halo / V
    f_cum = 1 - f_active
    R = R_halo_kpc * kpc_to_m
    rho_uniform = f_cum * M_halo_Msun * M_sun / ((4/3) * math.pi * R**3)
    
    # Clustered component: kappa * rho_stellar
    M_disk = M_disk_Msun * M_sun
    R_d = R_disk_kpc * kpc_to_m
    h_z = 0.1 * R_d
    Sigma_0 = M_disk / (2 * math.pi * R_d**2)
    Sigma_r = Sigma_0 * math.exp(-r_kpc / R_disk_kpc)
    rho_stellar = Sigma_r / (2 * h_z)
    rho_clustered = kappa * rho_stellar
    
    # Mixed cumulative
    rho_cum_mixed = f_mix * rho_uniform + (1 - f_mix) * rho_clustered
    
    # Active contribution
    rho_active = f_active * rho_clustered
    
    rho_DM_total = rho_cum_mixed + rho_active
    
    # g_DM = G * M_enclosed / r^2
    # For the cumulative: M_enclosed_cum = f_mix * (r/R)^3 * f_cum * M_halo + (1-f_mix) * kappa * M_stellar_enclosed
    M_stellar_enclosed = M_disk * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    M_cum_enclosed = f_mix * (r_kpc / R_halo_kpc)**3 * f_cum * M_halo_Msun * M_sun + (1 - f_mix) * kappa * M_stellar_enclosed
    M_active_enclosed = f_active * kappa * M_stellar_enclosed
    M_DM_enclosed = M_cum_enclosed + M_active_enclosed
    
    g_dm = G * M_DM_enclosed / r_m**2 if r_m > 0 else 0
    return g_dm, f_mix

def evaluate(f_active, N_crit):
    """Return total log-deviation from empirical targets."""
    total_err = 0
    for name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus in galaxies:
        r_test = 2 * R_disk
        g_dm, f_mix = g_DM_mixing(r_test, M_disk, R_disk, M_halo, R_halo, f_active, N_crit)
        g_b = g_bar(r_test, M_disk, R_disk)
        g_obs = g_b + g_dm
        if g_b > 0:
            model_ratio = g_obs / g_b
            err_ratio = math.log(model_ratio / target_ratio) ** 2
            total_err += err_ratio
    return total_err

# Grid search
print("=" * 70)
print("PARAMETER SEARCH: f_active, N_crit")
print("=" * 70)
print(f"{'f_active':>10s}  {'N_crit':>10s}  {'log_err':>10s}")
print("-" * 35)

best_params = None
best_err = float('inf')

# Coarse grid first
for f_active in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5]:
    for N_crit in [1, 3, 5, 10, 20, 50, 100]:
        err = evaluate(f_active, N_crit)
        print(f"{f_active:>10.2f}  {N_crit:>10.1f}  {err:>10.3f}")
        if err < best_err:
            best_err = err
            best_params = (f_active, N_crit)

print()
print(f"Best coarse: f_active={best_params[0]}, N_crit={best_params[1]}, err={best_err:.3f}")

# Fine grid around best
print()
print("Fine search around best:")
print(f"{'f_active':>10s}  {'N_crit':>10s}  {'log_err':>10s}")
print("-" * 35)

f_a_best, N_crit_best = best_params
for f_active in [f_a_best - 0.05, f_a_best - 0.02, f_a_best, f_a_best + 0.02, f_a_best + 0.05]:
    for N_crit in [N_crit_best - 2, N_crit_best, N_crit_best + 2, N_crit_best + 5]:
        if f_active <= 0 or N_crit <= 0:
            continue
        err = evaluate(f_active, N_crit)
        print(f"{f_active:>10.3f}  {N_crit:>10.1f}  {err:>10.3f}")
        if err < best_err:
            best_err = err
            best_params = (f_active, N_crit)

print()
print(f"=" * 70)
print(f"BEST FIT: f_active={best_params[0]:.3f}, N_crit={best_params[1]:.1f}, log_err={best_err:.3f}")
print(f"=" * 70)
print()
print("Predictions with best-fit parameters:")
print(f"  {'Object':<20s}  {'r (kpc)':>8s}  {'g_obs/g_bar':>12s}  {'g_+ effective':>14s}")
for name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus in galaxies:
    r_test = 2 * R_disk
    g_dm, f_mix = g_DM_mixing(r_test, M_disk, R_disk, M_halo, R_halo, best_params[0], best_params[1])
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
    print(f"  {name:<20s}  {r_test:>8.1f}  {g_obs/g_b if g_b>0 else 0:>12.2f}  {g_plus_eff:>14.3e}")
print()
print("Empirical targets:")
print(f"  {'Object':<20s}  {'r (kpc)':>8s}  {'g_obs/g_bar':>12s}  {'g_+ effective':>14s}")
for name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus in galaxies:
    r_test = 2 * R_disk
    g_b = g_bar(r_test, M_disk, R_disk)
    print(f"  {name:<20s}  {r_test:>8.1f}  {target_ratio:>12.2f}  {target_g_plus:>14.3e}")
