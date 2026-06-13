#!/usr/bin/env python3
"""
RAR with core+isothermal cumulative profile.

Hypothesis: the cumulative dark matter has a CORED profile (constant
density in the center) rather than cuspy (NFW-like). This is consistent
with the "cored DM" simulations that include baryonic feedback.

Profile:
  rho_cum(r) = rho_0 for r < r_core
  rho_cum(r) = rho_0 * (r_core/r)^2 for r > r_core

This gives:
  g_cum = const * r for r < r_core
  g_cum = const for r > r_core (FLAT rotation curve!)

The second part (g_cum = const for r > r_core) is exactly the flat
rotation curve observation!

Plus the active component (clustered, follows stellar profile).
"""

import math

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
age_universe_s = 13.8e9 * 3.15e7

# Empirical
g_plus_McGaugh = 1.2e-10

def rar(g_bar, g_plus):
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

def g_DM_core_iso(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, r_core_kpc):
    """
    Core+isothermal cumulative profile.
    
    Inside r_core: rho = const, M_cum = (4/3) pi r^3 rho_0
    Outside r_core: rho ~ 1/r^2, M_cum = M_core + 4 pi rho_0 r_core^2 (r - r_core)
    
    The total M_cum = f_cum * M_halo
    """
    f_cum = 1 - f_active
    M_cum_total_kg = f_cum * M_halo_Msun * M_sun
    
    r_core_m = r_core_kpc * kpc_to_m
    r_m = r_kpc * kpc_to_m
    
    if r_core_kpc > 0:
        # Volume of core: (4/3) pi r_core^3
        # Mass of core: M_core = (4/3) pi r_core^3 rho_0
        # Mass outside core: M_shell = 4 pi rho_0 r_core^2 (R_halo - r_core) (for 1/r^2)
        # Total: (4/3) pi r_core^3 rho_0 + 4 pi rho_0 r_core^2 (R_halo - r_core)
        #      = 4 pi rho_0 r_core^2 (r_core/3 + R_halo - r_core)
        #      = 4 pi rho_0 r_core^2 (R_halo - 2*r_core/3)
        # 
        # For r_core << R_halo: Total ~ 4 pi rho_0 r_core^2 R_halo
        R_halo_m = R_halo_kpc * kpc_to_m
        V_eff = 4 * math.pi * r_core_m**2 * (R_halo_m - 2*r_core_m/3)
        rho_0 = M_cum_total_kg / V_eff
    else:
        rho_0 = 0
    
    if r_m < r_core_m:
        # Inside core: M_enclosed = (4/3) pi r^3 rho_0
        M_cum_enclosed = (4/3) * math.pi * r_m**3 * rho_0
    else:
        # Outside core: M_enclosed = M_core + 4 pi rho_0 r_core^2 (r - r_core)
        M_core = (4/3) * math.pi * r_core_m**3 * rho_0
        M_cum_enclosed = M_core + 4 * math.pi * rho_0 * r_core_m**2 * (r_m - r_core_m)
    
    # Active contribution
    M_disk = M_disk_Msun * M_sun
    R_d = R_disk_kpc * kpc_to_m
    M_active_enclosed = f_active * (M_halo_Msun / M_disk_Msun if M_disk_Msun > 0 else 0) * M_disk * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    
    M_DM_enclosed = M_cum_enclosed + M_active_enclosed
    g_dm = G * M_DM_enclosed / r_m**2 if r_m > 0 else 0
    return g_dm

# Test with different core sizes
print("=" * 80)
print("CORE+ISOTHERMAL CUMULATIVE PROFILE")
print("=" * 80)
print()
print("Searching for r_core, f_active that fits all three scales...")
print()

# Galaxy types
galaxies = [
    ('Milky Way', 6e10, 4, 1e12, 30, 2.5, g_plus_McGaugh),
    ('Dwarf (EDGE 2025)', 1e7, 1, 1e9, 5, 20.0, 1.5e-10),
    ('Cluster (Tian 2024)', 1e12, 30, 1e14, 500, 50.0, 17 * g_plus_McGaugh),
]

best = None
best_err = float('inf')

# Grid search
for f_active in [0.0, 0.05, 0.1, 0.2, 0.3, 0.5]:
    for r_core_frac in [0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7]:
        # r_core is a FRACTION of R_halo (so it scales with mass)
        results = []
        total_err = 0
        for name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus in galaxies:
            r_core = r_core_frac * R_halo
            r_test = 2 * R_disk
            g_dm = g_DM_core_iso(r_test, M_disk, R_disk, M_halo, R_halo, f_active, r_core)
            g_b = g_bar_disk(r_test, M_disk, R_disk)
            g_obs = g_b + g_dm
            model_ratio = g_obs / g_b if g_b > 0 else 1
            err = (math.log(model_ratio / target_ratio))**2
            total_err += err
            results.append(model_ratio)
        
        if total_err < best_err:
            best_err = total_err
            best = (f_active, r_core_frac, results)

print(f"BEST: f_active = {best[0]}, r_core_frac = {best[1]}, log_err = {best_err:.3f}")
print()
print("Predictions:")
f_active, r_core_frac, results = best
for (name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus), model_ratio in zip(galaxies, results):
    r_core = r_core_frac * R_halo
    r_test = 2 * R_disk
    g_dm = g_DM_core_iso(r_test, M_disk, R_disk, M_halo, R_halo, f_active, r_core)
    g_b = g_bar_disk(r_test, M_disk, R_disk)
    g_obs = g_b + g_dm
    if g_obs > g_b * 1.01:
        arg = 1 - g_b / g_obs
        if 0 < arg < 1:
            g_plus_eff = g_b / (math.log(arg))**2
        else:
            g_plus_eff = float('inf')
    else:
        g_plus_eff = 0
    print(f"  {name} (r_core = {r_core:.1f} kpc = {r_core_frac}*R_halo): g_obs/g_bar = {model_ratio:.2f} (target {target_ratio}), g_+ = {g_plus_eff:.2e} (target {target_g_plus:.2e})")

# Compare g_obs(g_bar) curve to RAR for the best case
print()
print("=" * 80)
print("MW: g_obs(g_bar) curve vs empirical RAR (best core+iso model)")
print("=" * 80)
print()
M_disk, R_disk, M_halo, R_halo = 6e10, 4, 1e12, 30
r_core = best[1] * R_halo
print(f"  {'r (kpc)':>8s}  {'g_bar':>12s}  {'g_obs_model':>12s}  {'g_obs_RAR':>12s}  {'diff':>8s}")
for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]:
    g_b = g_bar_disk(r, M_disk, R_disk)
    g_dm = g_DM_core_iso(r, M_disk, R_disk, M_halo, R_halo, best[0], r_core)
    g_obs_model = g_b + g_dm
    g_obs_rar = rar(g_b, g_plus_McGaugh)
    diff = (g_obs_model - g_obs_rar) / g_obs_rar if g_obs_rar > 0 else 0
    print(f"  {r:>8.1f}  {g_b:>12.3e}  {g_obs_model:>12.3e}  {g_obs_rar:>12.3e}  {diff:>8.2f}")
