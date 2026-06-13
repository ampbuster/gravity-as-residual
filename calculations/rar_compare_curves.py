#!/usr/bin/env python3
"""
Direct comparison: cascade's g_obs(g_bar) curve vs empirical RAR.

This plots the cascade's g_obs as a function of g_bar (parametric in r)
and compares to the empirical RAR.

If the cascade's curve lies ON TOP of the RAR, the model matches.
"""

import math

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
age_universe_s = 13.8e9 * 3.15e7

# Best-fit parameters
f_active = 0.08
N_crit = 25

# Empirical RAR (McGaugh+ 2016)
g_plus_McGaugh = 1.2e-10  # m/s^2

def rar(g_bar, g_plus):
    """Empirical RAR: g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_+)))"""
    if g_bar <= 0:
        return 0
    if g_plus <= 0:
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
    if r_m <= 0:
        return 0
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

# Test: MW
M_disk, R_disk, M_halo, R_halo = 6e10, 4, 1e12, 30

print("=" * 80)
print("MILKY WAY: cascade's g_obs(g_bar) vs empirical RAR")
print("=" * 80)
print()
print(f"  {'r (kpc)':>8s}  {'g_bar':>12s}  {'g_obs_cascade':>14s}  {'g_obs_RAR':>12s}  {'g_obs_RAR_17x':>14s}  {'diff_cascade':>12s}  {'diff_17x':>10s}")
print("-" * 110)

# Compute g_obs and g_bar at various radii
for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30, 40, 50]:
    g_b = g_bar_disk(r, M_disk, R_disk)
    g_dm = g_DM_model(r, M_disk, R_disk, M_halo, R_halo, f_active, N_crit)
    g_obs_cascade = g_b + g_dm
    g_obs_rar = rar(g_b, g_plus_McGaugh)
    g_obs_rar_17x = rar(g_b, 17 * g_plus_McGaugh)
    
    diff_cascade = (g_obs_cascade - g_obs_rar) / g_obs_rar if g_obs_rar > 0 else 0
    diff_17x = (g_obs_cascade - g_obs_rar_17x) / g_obs_rar_17x if g_obs_rar_17x > 0 else 0
    
    print(f"  {r:>8.1f}  {g_b:>12.3e}  {g_obs_cascade:>14.3e}  {g_obs_rar:>12.3e}  {g_obs_rar_17x:>14.3e}  {diff_cascade:>12.2f}  {diff_17x:>10.2f}")

print()
print("diff_cascade: cascade vs RAR with g_+=1.2e-10 (galaxy RAR)")
print("diff_17x:     cascade vs RAR with g_+=2e-9 (cluster RAR)")
print()
print("If the cascade's curve matches the empirical RAR, the model works.")

