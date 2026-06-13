#!/usr/bin/env python3
"""
RAR with mass-dependent f_active.

Hypothesis: f_active (the fraction of DM that is "current activity" in
the cascade) is NOT a universal constant. It depends on the system:
- Galaxies: high current SFR / integrated SFR, f_active ~ 0.1
- Dwarfs: variable, f_active ~ 0.05
- Clusters: low current SFR / integrated SFR, f_active ~ 0.001

The cascade's postulate f_active = 0.3 is replaced by a physical model:
f_active(M) = current_SFR / integrated_SFR for that mass scale.

This is a "scale-dependent cascade fraction" — different mass scales have
different proportions of current vs cumulative dark matter.
"""

import math

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
age_universe_s = 13.8e9 * 3.15e7

# Empirical
g_plus_McGaugh = 1.2e-10

# Galaxy types with empirical targets
# f_active is now a function of mass scale
galaxies = [
    # (name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus, f_active_local)
    ('Milky Way', 6e10, 4, 1e12, 30, 2.5, g_plus_McGaugh, 0.10),
    ('Dwarf (EDGE 2025)', 1e7, 1, 1e9, 5, 20.0, 1.5e-10, 0.05),
    ('Cluster (Tian 2024)', 1e12, 30, 1e14, 500, 50.0, 17 * g_plus_McGaugh, 0.001),
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

def g_DM_scale_dep(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, alpha_cum):
    """
    Scale-dependent cascade model.
    
    rho_cum(r): power-law profile with index alpha_cum
    rho_active: clustered (stellar profile * kappa) with fraction f_active
    f_active varies by mass scale (galaxies > clusters)
    """
    v_c = v_circ_total(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc)
    r_m = r_kpc * kpc_to_m
    t_dyn = 2 * math.pi * r_m / v_c if v_c > 0 else age_universe_s
    N_orbits = age_universe_s / t_dyn if t_dyn > 0 else 0
    f_mix = 1 - math.exp(-N_orbits / 10)  # N_crit = 10
    
    f_cum = 1 - f_active
    R_halo_m = R_halo_kpc * kpc_to_m
    R_core = 0.1 * R_halo_m
    r_eff = max(r_m, R_core)
    
    # Cumulative profile
    M_cum_total_kg = f_cum * M_halo_Msun * M_sun
    if alpha_cum < 3:
        integral = 4 * math.pi * R_core**alpha_cum * (R_halo_m**(3-alpha_cum) - R_core**(3-alpha_cum)) / (3-alpha_cum)
    else:
        integral = 4 * math.pi * R_core**3 * math.log(R_halo_m / R_core)
    rho_0 = M_cum_total_kg / integral
    rho_cum = rho_0 * (R_core / r_eff) ** alpha_cum
    
    # Active: clustered, kappa * rho_stellar
    M_disk = M_disk_Msun * M_sun
    R_d = R_disk_kpc * kpc_to_m
    h_z = 0.1 * R_d
    Sigma_0 = M_disk / (2 * math.pi * R_d**2)
    Sigma_r = Sigma_0 * math.exp(-r_kpc / R_disk_kpc)
    rho_stellar = Sigma_r / (2 * h_z)
    kappa = M_halo_Msun / M_disk_Msun if M_disk_Msun > 0 else 0
    rho_active = f_active * kappa * rho_stellar
    
    # g_DM
    if r_m < R_core:
        M_cum_enclosed = rho_0 * (4/3) * math.pi * r_m**3
    elif alpha_cum < 3:
        M_cum_enclosed = rho_0 * 4 * math.pi * R_core**alpha_cum * (r_m**(3-alpha_cum) - R_core**(3-alpha_cum)) / (3-alpha_cum) + rho_0 * (4/3) * math.pi * R_core**3
    else:
        M_cum_enclosed = rho_0 * 4 * math.pi * R_core**3 * math.log(r_m / R_core) + rho_0 * (4/3) * math.pi * R_core**3
    
    M_active_enclosed = f_active * kappa * M_disk * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    M_DM_enclosed = M_cum_enclosed + M_active_enclosed
    g_dm = G * M_DM_enclosed / r_m**2 if r_m > 0 else 0
    return g_dm, f_mix

# Grid search
print("=" * 70)
print("SCALE-DEPENDENT f_active MODEL")
print("=" * 70)
print()
print("f_active varies by mass scale: MW=0.1, Dwarf=0.05, Cluster=0.001")
print()

best = None
best_err = float('inf')

for alpha_cum in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]:
    results = []
    total_err = 0
    for name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus, f_active in galaxies:
        r_test = 2 * R_disk
        g_dm, f_mix = g_DM_scale_dep(r_test, M_disk, R_disk, M_halo, R_halo, f_active, alpha_cum)
        g_b = g_bar(r_test, M_disk, R_disk)
        g_obs = g_b + g_dm
        model_ratio = g_obs / g_b if g_b > 0 else 1
        err = (math.log(model_ratio / target_ratio))**2
        total_err += err
        results.append((model_ratio, f_mix))
    print(f"  alpha_cum = {alpha_cum}: MW={results[0][0]:.2f}, Dwarf={results[1][0]:.2f}, Cluster={results[2][0]:.2f}, log_err={total_err:.3f}")
    if total_err < best_err:
        best_err = total_err
        best = (alpha_cum, results)

print()
print(f"BEST: alpha_cum = {best[0]}, log_err = {best_err:.3f}")
print()
print("Predictions:")
alpha_cum, results = best
for (name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus, f_active), (model_ratio, f_mix) in zip(galaxies, results):
    r_test = 2 * R_disk
    g_dm, _ = g_DM_scale_dep(r_test, M_disk, R_disk, M_halo, R_halo, f_active, alpha_cum)
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
    print(f"  {name}: g_obs/g_bar = {model_ratio:.2f} (target {target_ratio}), g_+ = {g_plus_eff:.2e} (target {target_g_plus:.2e})")
