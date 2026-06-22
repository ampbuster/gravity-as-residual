#!/usr/bin/env python3
"""
RAR with SPREAD-OUT active contribution.

Hypothesis: the active (current) 2D universe gravity is not concentrated
at the source, but spread out over a characteristic scale r_active. This
is because 2D gravity has a logarithmic potential (1/r force) which is
"flatter" than 3D gravity.

Model:
  g_active(r) = G * f_active * M_halo_eff / r^2 for r > r_active
  g_active(r) = G * f_active * M_halo_eff / r_active^2 for r < r_active
  where M_halo_eff is the cumulative active mass "within r_active"

This is essentially saying the active 2D universe gravity is "smeared"
over r_active, with constant g_active inside r_active.

Combined with the cumulative (mixed profile), this gives a more nuanced
prediction that may better match the RAR.


**HISTORICAL (v2.x era, mid-2025)**: This file is from the v2.x era, predating:
- v3.0+ Lagrangian work (L102-L136)
- v3.1+ Multi-universe picture (L142-L150)
- v3.3 Bilateral cascade (E_4D = 5e79 J, M_Pl,4D = 3.93e23 GeV)
- v3.5.7+ Naming revolution (f_back -> f_DE, f_DM,leak, f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N*v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via alpha-GM, L308v)
- alpha = 1.289 (FIRST-PRINCIPLES via L308n)
- eps = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- gamma_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- tau_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v2.x era framework, not v3.5.9+ A2.

"""

import math

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19

g_plus_McGaugh = 1.2e-10

def rar(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

def g_bar_disk(r_kpc, M_disk_Msun, R_disk_kpc):
    r_m = r_kpc * kpc_to_m
    M_disk_enclosed = M_disk_Msun * M_sun * (1 - (1 + r_m/(R_disk_kpc * kpc_to_m)) * math.exp(-r_m/(R_disk_kpc * kpc_to_m)))
    return G * M_disk_enclosed / r_m**2

def g_DM(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, r_active_kpc):
    """
    Cumulative: uniform (or core+isothermal)
    Active: spread out over r_active
    """
    r_m = r_kpc * kpc_to_m
    r_active_m = r_active_kpc * kpc_to_m
    
    f_cum = 1 - f_active
    
    # Cumulative uniform
    R_halo_m = R_halo_kpc * kpc_to_m
    rho_uniform = f_cum * M_halo_Msun * M_sun / ((4/3) * math.pi * R_halo_m**3)
    M_cum_enclosed = (4/3) * math.pi * r_m**3 * rho_uniform if r_m < R_halo_m else f_cum * M_halo_Msun * M_sun
    g_cum = G * M_cum_enclosed / r_m**2 if r_m > 0 else 0
    
    # Active: spread out
    # Total active mass: f_active * M_halo
    # Spread over r_active
    M_active_total = f_active * M_halo_Msun * M_sun
    V_active = max((4/3) * math.pi * r_active_m**3, 1e-30)
    rho_active = M_active_total / V_active
    
    if r_m < r_active_m:
        M_active_enclosed = (4/3) * math.pi * r_m**3 * rho_active
    else:
        M_active_enclosed = M_active_total
    
    g_active = G * M_active_enclosed / r_m**2 if r_m > 0 else 0
    
    return g_cum + g_active

# Grid search
print("=" * 80)
print("SPREAD-OUT ACTIVE CONTRIBUTION")
print("=" * 80)
print()
print("Active is spread over r_active (not concentrated at source)")
print()
print(f"  {'f_active':>10s}  {'r_active/R_halo':>15s}  {'MW':>8s}  {'Dwarf':>8s}  {'Cluster':>8s}  {'log_err':>10s}")
print("-" * 80)

galaxies = [
    ('MW', 6e10, 4, 1e12, 30, 2.5),
    ('Dwarf', 1e7, 1, 1e9, 5, 20.0),
    ('Cluster', 1e12, 30, 1e14, 500, 50.0),
]

best = None
best_err = float('inf')

for f_active in [0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 1.0]:
    for r_active_frac in [0.0, 0.1, 0.3, 0.5, 1.0, 2.0]:
        results = []
        total_err = 0
        for name, M_disk, R_disk, M_halo, R_halo, target_ratio in galaxies:
            r_test = 2 * R_disk
            r_active = r_active_frac * R_halo
            g_dm = g_DM(r_test, M_disk, R_disk, M_halo, R_halo, f_active, r_active)
            g_b = g_bar_disk(r_test, M_disk, R_disk)
            g_obs = g_b + g_dm
            model_ratio = g_obs / g_b if g_b > 0 else 1
            err = (math.log(model_ratio / target_ratio))**2
            total_err += err
            results.append(model_ratio)
        
        if total_err < best_err:
            best_err = total_err
            best = (f_active, r_active_frac, results)

print(f"  BEST: f_active={best[0]}, r_active_frac={best[1]}, log_err={best_err:.3f}")
print()
f_active, r_active_frac, _ = best
print(f"Detailed predictions (f_active={f_active}, r_active_frac={r_active_frac}):")
for name, M_disk, R_disk, M_halo, R_halo, target_ratio in galaxies:
    r_test = 2 * R_disk
    r_active = r_active_frac * R_halo
    g_dm = g_DM(r_test, M_disk, R_disk, M_halo, R_halo, f_active, r_active)
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
    print(f"  {name}: g_obs/g_bar = {g_obs/g_b:.2f} (target {target_ratio}), g_+ = {g_plus_eff:.2e}")
