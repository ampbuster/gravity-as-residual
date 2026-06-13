#!/usr/bin/env python3
"""
Trial and error: find f_active that makes the cascade's g_obs(g_bar) match
the empirical RAR for the Milky Way at the typical test radius (2R_d = 8 kpc).

Key insight: f_active is the fraction of dark matter that is "current
activity" in the cascade. The empirical RAR constrains the g_obs(g_bar)
curve, which depends on f_active through:
  g_obs = g_bar + g_cum + g_active
  g_active = f_active * kappa * g_stellar (clustered, follows stellar)
  g_cum = (1-f_active) * G * M_halo_enclosed / r^2 (mixed profile)

The f_active that gives the correct g_obs at 2R_d = 8 kpc for MW is what
we want to find.
"""

import math

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
age_universe_s = 13.8e9 * 3.15e7

# Empirical
g_plus_McGaugh = 1.2e-10

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

def g_DM_model(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, N_crit=25):
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

# Test 1: find f_active that gives g_obs = RAR(g_bar) at r=8 kpc for MW
print("=" * 80)
print("TEST 1: Find f_active that matches RAR at r = 2R_d = 8 kpc for MW")
print("=" * 80)
print()
M_disk, R_disk, M_halo, R_halo = 6e10, 4, 1e12, 30
r = 2 * R_disk  # 8 kpc
g_b = g_bar_disk(r, M_disk, R_disk)
g_obs_rar = rar(g_b, g_plus_McGaugh)
g_DM_needed = g_obs_rar - g_b
print(f"g_bar at 8 kpc: {g_b:.3e}")
print(f"RAR g_obs: {g_obs_rar:.3e}")
print(f"g_DM_needed: {g_DM_needed:.3e}")
print()

print(f"  {'f_active':>10s}  {'g_DM':>12s}  {'g_obs':>12s}  {'diff_from_RAR':>15s}")
for f_active in [0.0, 0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.1, 0.15, 0.2, 0.3, 0.5, 0.7, 0.9, 1.0]:
    g_dm = g_DM_model(r, M_disk, R_disk, M_halo, R_halo, f_active, 25)
    g_obs = g_b + g_dm
    diff = (g_obs - g_obs_rar) / g_obs_rar
    print(f"  {f_active:>10.3f}  {g_dm:>12.3e}  {g_obs:>12.3e}  {diff:>15.3f}")

# Test 2: find f_active that matches RAR across the FULL g_bar range
# This is more demanding: the curve should match the RAR at all radii
print()
print("=" * 80)
print("TEST 2: Find f_active that gives best g_obs(g_bar) match to RAR")
print("=" * 80)
print()
print("Best f_active by minimizing log-error across all radii (0.5-30 kpc):")
print()

def total_log_error(f_active, M_disk, R_disk, M_halo, R_halo):
    """Sum of squared log-errors vs RAR across multiple radii"""
    total = 0
    for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]:
        if r > R_halo * 0.8:
            continue
        g_b = g_bar_disk(r, M_disk, R_disk)
        if g_b <= 0:
            continue
        g_dm = g_DM_model(r, M_disk, R_disk, M_halo, R_halo, f_active, 25)
        g_obs = g_b + g_dm
        g_obs_rar = rar(g_b, g_plus_McGaugh)
        if g_obs_rar > 0:
            err = (math.log(g_obs / g_obs_rar))**2
            total += err
    return total

# Fine search
print(f"  {'f_active':>10s}  {'log_err':>10s}")
best_fa = None
best_err = float('inf')
for f_active in [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3]:
    err = total_log_error(f_active, M_disk, R_disk, M_halo, R_halo)
    print(f"  {f_active:>10.3f}  {err:>10.3f}")
    if err < best_err:
        best_err = err
        best_fa = f_active

print()
print(f"BEST f_active (by full-curve fit): {best_fa}, log_err = {best_err:.3f}")
print()

# Detailed comparison for best f_active
print(f"Detailed g_obs(g_bar) for f_active = {best_fa}:")
print(f"  {'r (kpc)':>8s}  {'g_bar':>12s}  {'g_obs':>12s}  {'g_obs_RAR':>12s}  {'diff':>8s}")
for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]:
    if r > R_halo * 0.8:
        continue
    g_b = g_bar_disk(r, M_disk, R_disk)
    g_dm = g_DM_model(r, M_disk, R_disk, M_halo, R_halo, best_fa, 25)
    g_obs = g_b + g_dm
    g_obs_rar = rar(g_b, g_plus_McGaugh)
    diff = (g_obs - g_obs_rar) / g_obs_rar if g_obs_rar > 0 else 0
    print(f"  {r:>8.1f}  {g_b:>12.3e}  {g_obs:>12.3e}  {g_obs_rar:>12.3e}  {diff:>8.2f}")

# Test 3: same for cluster
print()
print("=" * 80)
print("TEST 3: Find f_active that matches RAR for cluster (using g_+=17x)")
print("=" * 80)
print()
M_disk, R_disk, M_halo, R_halo = 1e12, 30, 1e14, 500
g_plus_cluster = 17 * g_plus_McGaugh

# At what r does the cluster RAR give a meaningful comparison?
# Cluster g_bar peaks at ~30 kpc (~R_d)
# At r=60 kpc, g_bar ~ 2.3e-11
# RAR g_obs = 2.3e-11 * ~10 = 2.3e-10
r = 2 * R_disk  # 60 kpc
g_b = g_bar_disk(r, M_disk, R_disk)
g_obs_rar = rar(g_b, g_plus_cluster)
print(f"Cluster at r=60 kpc: g_bar={g_b:.3e}, RAR_cluster g_obs={g_obs_rar:.3e}")
print()

print(f"  {'f_active':>10s}  {'g_DM':>12s}  {'g_obs':>12s}  {'diff_from_RAR':>15s}")
for f_active in [0.0, 0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.1, 0.15, 0.2, 0.3]:
    g_dm = g_DM_model(r, M_disk, R_disk, M_halo, R_halo, f_active, 25)
    g_obs = g_b + g_dm
    diff = (g_obs - g_obs_rar) / g_obs_rar
    print(f"  {f_active:>10.3f}  {g_dm:>12.3e}  {g_obs:>12.3e}  {diff:>15.3f}")

# Best cluster f_active
print()
best_fa_c = None
best_err_c = float('inf')
for f_active in [0.0, 0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.1, 0.15, 0.2, 0.3]:
    err = total_log_error(f_active, M_disk, R_disk, M_halo, R_halo)
    if err < best_err_c:
        best_err_c = err
        best_fa_c = f_active
print(f"BEST f_active for cluster (full-curve fit): {best_fa_c}, log_err = {best_err_c:.3f}")
