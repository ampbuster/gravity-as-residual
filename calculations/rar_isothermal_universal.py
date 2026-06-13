#!/usr/bin/env python3
"""
RAR with isothermal cumulative, universal (f_active, r_core_frac),
but mass-dependent scale factor.

Hypothesis: the cascade's intrinsic M_halo (from cumulative 2D universe
gravity) is a calculable fraction of the empirical M_halo, and this
fraction depends on the system.

For MW: cascade M_halo ~ 10% of empirical
For cluster: cascade M_halo ~ 70% of empirical

The 7x difference between MW and cluster could be explained by:
- Different kappa (cluster kappa=100, MW kappa=17, 5.9x ratio)
- Different star formation history
- Baryonic effects
- Selection effects
"""

import math

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19

g_plus_galaxy = 1.2e-10
g_plus_cluster = 17 * g_plus_galaxy

def rar(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

def g_bar_disk(r_kpc, M_disk_Msun, R_disk_kpc):
    r_m = r_kpc * kpc_to_m
    M_disk_enclosed = M_disk_Msun * M_sun * (1 - (1 + r_m/(R_disk_kpc * kpc_to_m)) * math.exp(-r_m/(R_disk_kpc * kpc_to_m)))
    return G * M_disk_enclosed / r_m**2

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

print("=" * 80)
print("UNIVERSAL CASCADE RAR: f_active=0.05, r_core_frac=0.2")
print("Mass-dependent scale factor (cascade M_halo / empirical M_halo)")
print("=" * 80)
print()

f_active = 0.05
r_core_frac = 0.2

# MW with scale=0.1
print("--- MW (scale = 0.1, cascade M_halo ~ 10% of empirical) ---")
M_disk, R_disk, M_halo, R_halo = 6e10, 4, 1e12, 30
r_core = r_core_frac * R_halo
print(f"  r_core = {r_core:.1f} kpc")
print(f"  {'r (kpc)':>8s}  {'g_bar':>12s}  {'g_obs':>12s}  {'g_obs_RAR':>12s}  {'diff':>8s}")
total_err = 0
n = 0
for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]:
    g_b = g_bar_disk(r, M_disk, R_disk)
    g_dm = g_DM_iso(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, 0.1)
    g_obs = g_b + g_dm
    g_obs_rar = rar(g_b, g_plus_galaxy)
    diff = (g_obs - g_obs_rar) / g_obs_rar
    total_err += (math.log(g_obs / g_obs_rar))**2
    n += 1
    print(f"  {r:>8.1f}  {g_b:>12.3e}  {g_obs:>12.3e}  {g_obs_rar:>12.3e}  {diff:>8.2f}")
print(f"  log_err = {total_err/n:.4f}")

# Cluster with scale=0.7
print()
print("--- Cluster (scale = 0.7, cascade M_halo ~ 70% of empirical) ---")
M_disk, R_disk, M_halo, R_halo = 1e12, 30, 1e14, 500
r_core = r_core_frac * R_halo
print(f"  r_core = {r_core:.1f} kpc")
print(f"  {'r (kpc)':>8s}  {'g_bar':>12s}  {'g_obs':>12s}  {'g_obs_RAR':>12s}  {'diff':>8s}")
total_err = 0
n = 0
for r in [10, 30, 60, 100, 200, 300, 500]:
    g_b = g_bar_disk(r, M_disk, R_disk)
    g_dm = g_DM_iso(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac, 0.7)
    g_obs = g_b + g_dm
    g_obs_rar = rar(g_b, g_plus_cluster)
    diff = (g_obs - g_obs_rar) / g_obs_rar
    total_err += (math.log(g_obs / g_obs_rar))**2
    n += 1
    print(f"  {r:>8.1f}  {g_b:>12.3e}  {g_obs:>12.3e}  {g_obs_rar:>12.3e}  {diff:>8.2f}")
print(f"  log_err = {total_err/n:.4f}")

print()
print("=" * 80)
print("INTERPRETATION")
print("=" * 80)
print()
print("With f_active=0.05, r_core_frac=0.2 (UNIVERSAL across systems):")
print("  - MW: best scale = 0.1 (cascade M_halo ~ 10% of empirical)")
print("  - Cluster: best scale = 0.7 (cascade M_halo ~ 70% of empirical)")
print()
print("The scale factor is MASS-DEPENDENT. Possible explanations:")
print("  1. kappa ratio: cluster kappa=100, MW kappa=17 (5.9x ratio)")
print("  2. Baryonic effects: more gas/dust in clusters, more 'extra' DM in galaxies")
print("  3. Star formation history: cluster's stars formed earlier (different f_active)")
print("  4. Selection effects: empirical M_halo includes different things at different scales")
print()
print("A specific cascade implementation would need to derive this mass-dependent")
print("scale factor from the 4D event's physics.")
