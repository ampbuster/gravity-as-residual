#!/usr/bin/env python3
"""
Test cascade's RAR prediction across the FULL mass spectrum, including extremes.

The question: where does the cascade's g_obs(g_bar) curve fall?
- On the galaxy RAR (g_+ = 1.2e-10)?
- On the cluster RAR (g_+ = 17x)?
- Somewhere else?

If the cascade's prediction lies on the galaxy RAR for low-mass systems
and shifts to the cluster RAR for high-mass systems, that would be
a smooth mass-dependent transition (interesting!).

If the cascade's prediction lies on the cluster RAR for ALL systems,
that's a uniform "off by 17x" — meaning the cascade is missing some
scaling factor.

If the cascade's prediction lies somewhere between for some systems,
that's a real testable mass-dependence.
"""

import math

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
age_universe_s = 13.8e9 * 3.15e7

# Empirical RARs
g_plus_galaxy = 1.2e-10
g_plus_cluster = 17 * g_plus_galaxy

def rar(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

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

def g_bar_disk(r_kpc, M_disk_Msun, R_disk_kpc):
    r_m = r_kpc * kpc_to_m
    M_disk_enclosed = M_disk_Msun * M_sun * (1 - (1 + r_m/(R_disk_kpc * kpc_to_m)) * math.exp(-r_m/(R_disk_kpc * kpc_to_m)))
    return G * M_disk_enclosed / r_m**2

def g_DM_model(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, N_crit):
    v_c = v_circ_total(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc)
    r_m = r_kpc * kpc_to_m
    t_dyn = 2 * math.pi * r_m / v_c if v_c > 0 else age_universe_s
    N_orbits = age_universe_s / t_dyn if t_dyn > 0 else 0
    f_mix = 1 - math.exp(-N_orbits / N_crit)
    
    f_cum = 1 - f_active
    R_halo_m = R_halo_kpc * kpc_to_m
    rho_uniform = f_cum * M_halo_Msun * M_sun / ((4/3) * math.pi * R_halo_m**3)
    
    M_disk = M_disk_Msun * M_sun
    R_d = R_disk_kpc * kpc_to_m
    h_z = 0.1 * R_d
    Sigma_0 = M_disk / (2 * math.pi * R_d**2)
    Sigma_r = Sigma_0 * math.exp(-r_kpc / R_disk_kpc)
    rho_stellar = Sigma_r / (2 * h_z)
    kappa = M_halo_Msun / M_disk_Msun if M_disk_Msun > 0 else 0
    
    M_cum_uniform_enclosed = f_mix * (r_kpc / R_halo_kpc)**3 * f_cum * M_halo_Msun * M_sun
    M_stellar_enclosed = M_disk * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    M_cum_clustered_enclosed = (1 - f_mix) * kappa * M_stellar_enclosed
    M_active_enclosed = f_active * kappa * M_stellar_enclosed
    M_DM_enclosed = M_cum_uniform_enclosed + M_cum_clustered_enclosed + M_active_enclosed
    g_dm = G * M_DM_enclosed / r_m**2 if r_m > 0 else 0
    return g_dm

def effective_g_plus(g_bar, g_obs):
    """Infer the g_+ that would give g_obs from g_bar in the RAR."""
    if g_obs <= g_bar * 1.01:
        return 0
    ratio = g_bar / g_obs
    arg = 1 - ratio
    if 0 < arg < 1:
        return g_bar / (math.log(arg))**2
    return float('inf')

# Use the best-fit parameters
f_active = 0.08
N_crit = 25

# A wide range of galaxy types, including extremes
galaxies = [
    # (name, M_disk, R_disk, M_halo, R_halo, type, expected_RAR)
    ('Ultra-faint dwarf', 1e4, 0.2, 1e7, 1, 'extreme_low', 'galaxy'),
    ('Classical dwarf', 1e7, 1, 1e9, 5, 'low', 'galaxy'),
    ('Small spiral', 1e9, 2, 1e10, 15, 'low_mid', 'galaxy'),
    ('MW-like spiral', 6e10, 4, 1e12, 30, 'mid', 'galaxy'),
    ('Large spiral', 2e11, 6, 5e12, 50, 'mid_high', 'galaxy'),
    ('Compact group', 1e11, 5, 1e13, 100, 'transition', 'cluster'),
    ('Small cluster', 5e11, 15, 5e13, 300, 'cluster_low', 'cluster'),
    ('Massive cluster', 1e12, 30, 1e14, 500, 'cluster', 'cluster'),
    ('Supercluster core', 5e12, 50, 5e14, 1000, 'cluster_high', 'cluster'),
]

print("=" * 100)
print("CASCADE RAR PREDICTIONS ACROSS THE FULL MASS SPECTRUM")
print("=" * 100)
print()
print(f"Using f_active = {f_active}, N_crit = {N_crit}")
print()
print(f"  {'Name':<22s}  {'M_halo':>10s}  {'r_test':>8s}  {'g_obs/g_bar':>12s}  {'g_+ eff':>12s}  {'g_+/g_+_gal':>12s}  {'lies on':>10s}")
print("-" * 110)

for name, M_disk, R_disk, M_halo, R_halo, gtype, expected_rar in galaxies:
    r_test = 2 * R_disk
    g_dm = g_DM_model(r_test, M_disk, R_disk, M_halo, R_halo, f_active, N_crit)
    g_b = g_bar_disk(r_test, M_disk, R_disk)
    g_obs = g_b + g_dm
    
    g_plus_eff = effective_g_plus(g_b, g_obs)
    ratio_to_galaxy = g_plus_eff / g_plus_galaxy if g_plus_eff > 0 else 0
    
    # Which RAR does it lie on?
    if 0.5 < ratio_to_galaxy < 2:
        lies_on = 'galaxy'
    elif 10 < ratio_to_galaxy < 30:
        lies_on = 'cluster'
    elif 2 < ratio_to_galaxy < 10:
        lies_on = 'transition'
    elif ratio_to_galaxy > 30:
        lies_on = 'beyond_cluster'
    elif ratio_to_galaxy < 0.5:
        lies_on = 'sub_galaxy'
    else:
        lies_on = '?'
    
    M_halo_str = f"{M_halo:.1e}"
    print(f"  {name:<22s}  {M_halo_str:>10s}  {r_test:>8.1f}  {g_obs/g_b:>12.2f}  {g_plus_eff:>12.2e}  {ratio_to_galaxy:>12.2f}  {lies_on:>10s}")

print()
print("=" * 100)
print("FULL g_obs(g_bar) CURVE for each system — where does the cascade lie?")
print("=" * 100)
print()

# Pick a few representative systems
test_systems = [
    ('Classical dwarf', 1e7, 1, 1e9, 5),
    ('MW-like spiral', 6e10, 4, 1e12, 30),
    ('Massive cluster', 1e12, 30, 1e14, 500),
]

print(f"For each system, plot g_obs vs g_bar at multiple radii, compare to RARs:")
print()

for name, M_disk, R_disk, M_halo, R_halo in test_systems:
    print(f"--- {name} (M_halo = {M_halo:.1e} M_sun) ---")
    print(f"  {'r (kpc)':>8s}  {'g_bar':>12s}  {'g_obs':>12s}  {'g_obs_RAR_gal':>14s}  {'g_obs_RAR_clus':>14s}  {'on RAR_gal':>10s}  {'on RAR_clus':>10s}")
    
    test_radii = [0.5*R_disk, R_disk, 2*R_disk, 4*R_disk, 8*R_disk, 0.5*R_halo, R_halo]
    test_radii = [r for r in test_radii if r > 0]
    
    for r in test_radii:
        g_b = g_bar_disk(r, M_disk, R_disk)
        if g_b <= 0:
            continue
        g_dm = g_DM_model(r, M_disk, R_disk, M_halo, R_halo, f_active, N_crit)
        g_obs = g_b + g_dm
        
        g_obs_rar_g = rar(g_b, g_plus_galaxy)
        g_obs_rar_c = rar(g_b, g_plus_cluster)
        
        # Which RAR is closer?
        diff_g = abs(g_obs - g_obs_rar_g) / g_obs_rar_g
        diff_c = abs(g_obs - g_obs_rar_c) / g_obs_rar_c
        
        on_g = "YES" if diff_g < 0.5 else "no"
        on_c = "YES" if diff_c < 0.5 else "no"
        
        print(f"  {r:>8.2f}  {g_b:>12.3e}  {g_obs:>12.3e}  {g_obs_rar_g:>14.3e}  {g_obs_rar_c:>14.3e}  {on_g:>10s}  {on_c:>10s}")
    print()
