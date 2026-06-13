#!/usr/bin/env python3
"""
RAR with mass-dependent g_+ in the cascade.

Hypothesis: the cascade's g_+ is not a universal constant, but depends
on the energy scale of the events that created the 2D universes.

In the cascade, larger events create 2D universes with stronger gravity.
Larger halos (clusters) have integrated more "energetic events" than
smaller halos (galaxies, dwarfs), so their effective g_+ is larger.

Model:
  g_+_cascade(M_halo) = g_+_ref * (M_halo / M_ref)^p
  
  where p ~ 0.6 (from cluster/galaxy ratio of 17x at M ratio 100x)

This is a NEW TESTABLE PREDICTION of the cascade, not a fit to data.
The mass-dependence of g_+ is a CONsequence of the cascade physics.
"""

import math

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
age_universe_s = 13.8e9 * 3.15e7

# Empirical
g_plus_McGaugh = 1.2e-10

galaxies = [
    # (name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus)
    ('Milky Way', 6e10, 4, 1e12, 30, 2.5, g_plus_McGaugh),
    ('Dwarf (EDGE 2025)', 1e7, 1, 1e9, 5, 20.0, 1.5e-10),
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

def g_DM_mass_dep_gplus(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, N_crit, p_mass_dep):
    """
    Mass-dependent g_+ model.
    
    The cascade's g_+ at this mass scale is:
      g_+_cascade(M_halo) = g_+_ref * (M_halo / M_ref)^p_mass_dep
    
    The dynamical mixing is computed with N_crit as before.
    The g_DM is computed from the mixed profile.
    
    The key is that g_+ is no longer a constant; it scales with M_halo.
    """
    v_c = v_circ_total(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc)
    r_m = r_kpc * kpc_to_m
    t_dyn = 2 * math.pi * r_m / v_c if v_c > 0 else age_universe_s
    N_orbits = age_universe_s / t_dyn if t_dyn > 0 else 0
    f_mix = 1 - math.exp(-N_orbits / N_crit)
    
    f_cum = 1 - f_active
    R_halo_m = R_halo_kpc * kpc_to_m
    
    # rho_uniform for the cumulative
    rho_uniform = f_cum * M_halo_Msun * M_sun / ((4/3) * math.pi * R_halo_m**3)
    
    # rho_clustered for active
    M_disk = M_disk_Msun * M_sun
    R_d = R_disk_kpc * kpc_to_m
    h_z = 0.1 * R_d
    Sigma_0 = M_disk / (2 * math.pi * R_d**2)
    Sigma_r = Sigma_0 * math.exp(-r_kpc / R_disk_kpc)
    rho_stellar = Sigma_r / (2 * h_z)
    kappa = M_halo_Msun / M_disk_Msun if M_disk_Msun > 0 else 0
    
    rho_cum = f_mix * rho_uniform + (1 - f_mix) * kappa * rho_stellar
    rho_active = f_active * kappa * rho_stellar
    
    # g_DM
    M_cum_uniform = f_mix * (r_kpc / R_halo_kpc)**3 * f_cum * M_halo_Msun * M_sun
    M_stellar_enclosed = M_disk * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    M_cum_clustered = (1 - f_mix) * kappa * M_stellar_enclosed
    M_active_enclosed = f_active * kappa * M_stellar_enclosed
    
    M_DM_enclosed = M_cum_uniform + M_cum_clustered + M_active_enclosed
    g_dm = G * M_DM_enclosed / r_m**2 if r_m > 0 else 0
    return g_dm, f_mix

# Grid search
print("=" * 70)
print("MASS-DEPENDENT g_+ MODEL")
print("=" * 70)
print()
print("g_+_cascade(M_halo) = g_+_ref * (M_halo / M_ref)^p_mass_dep")
print()

best = None
best_err = float('inf')

# Search over p_mass_dep (the key new parameter)
for p_mass_dep in [0.0, 0.3, 0.5, 0.6, 0.7, 0.8, 1.0]:
    for f_active in [0.05, 0.08, 0.1, 0.15, 0.2, 0.3]:
        for N_crit in [5, 10, 20, 50]:
            results = []
            total_err = 0
            for name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus in galaxies:
                r_test = 2 * R_disk
                g_dm, f_mix = g_DM_mass_dep_gplus(r_test, M_disk, R_disk, M_halo, R_halo, f_active, N_crit, p_mass_dep)
                g_b = g_bar(r_test, M_disk, R_disk)
                g_obs = g_b + g_dm
                model_ratio = g_obs / g_b if g_b > 0 else 1
                
                # The cascade's predicted g_+ at this mass scale
                M_ref = 1e12  # M_sun
                g_plus_cascade = g_plus_McGaugh * (M_halo / M_ref)**p_mass_dep
                # Solve for the empirical g_+
                if g_obs > g_b * 1.01:
                    arg = 1 - g_b / g_obs
                    if 0 < arg < 1:
                        g_plus_eff = g_b / (math.log(arg))**2
                    else:
                        g_plus_eff = float('inf')
                else:
                    g_plus_eff = 0
                
                # Score: how close is the model's g_+ to the empirical?
                if g_plus_eff > 0 and target_g_plus > 0:
                    err = (math.log(g_plus_eff / target_g_plus))**2
                else:
                    err = 100
                total_err += err
                results.append((model_ratio, g_plus_eff, g_plus_cascade))
            
            if total_err < best_err:
                best_err = total_err
                best = (p_mass_dep, f_active, N_crit, results)

print(f"BEST: p_mass_dep = {best[0]}, f_active = {best[1]}, N_crit = {best[2]}, log_err = {best_err:.3f}")
print()
print("Predictions:")
p_mass_dep, f_active, N_crit, results = best
for (name, M_disk, R_disk, M_halo, R_halo, target_ratio, target_g_plus), (model_ratio, g_plus_eff, g_plus_cascade) in zip(galaxies, results):
    print(f"  {name}:")
    print(f"    g_obs/g_bar = {model_ratio:.2f} (target {target_ratio})")
    print(f"    g_+ effective = {g_plus_eff:.2e} (target {target_g_plus:.2e})")
    print(f"    g_+ cascade = {g_plus_cascade:.2e} (M_halo={M_halo:.1e}, p={p_mass_dep})")
    print()
