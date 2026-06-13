#!/usr/bin/env python3
"""
RAR with ISOTHERMAL cumulative + small f_active.

Hypothesis: the cumulative dark matter follows an isothermal profile
(rho_cum ~ 1/r^2) at large r, with a small core at small r. This is
what dynamical mixing would produce over many dynamical times (not
uniform, but a flatter-than-NFW profile).

Combined with small f_active (matching the RAR at high g_bar), this
should give the MOND-like behavior at large r (g_obs ~ 1/r).
"""

import math

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
age_universe_s = 13.8e9 * 3.15e7

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

def g_DM_isothermal(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, r_core_frac):
    """
    Isothermal cumulative + active clustered.
    
    Cumulative profile:
      rho_cum(r) = rho_0 for r < r_core (constant in core)
      rho_cum(r) = rho_0 * (r_core/r)^2 for r > r_core (isothermal)
    
    This is what mixing produces after a long time (a flatter-than-NFW
    profile, with isothermal behavior at large r).
    
    Active: f_active * kappa * rho_stellar (clustered)
    """
    f_cum = 1 - f_active
    r_core_m = r_core_frac * R_halo_kpc * kpc_to_m
    r_m = r_kpc * kpc_to_m
    M_cum_total_kg = f_cum * M_halo_Msun * M_sun
    R_halo_m = R_halo_kpc * kpc_to_m
    
    # Compute rho_0 by integrating the profile over the halo
    # Integral: V_core + V_shell
    # V_core = (4/3) pi r_core^3
    # V_shell = integral from r_core to R_halo of 4 pi r^2 * rho_0 * (r_core/r)^2 dr
    #         = 4 pi rho_0 r_core^2 * integral from r_core to R_halo of dr
    #         = 4 pi rho_0 r_core^2 * (R_halo - r_core)
    # M_cum = rho_0 * V_core + 4 pi rho_0 r_core^2 * (R_halo - r_core)
    #       = rho_0 * [(4/3) pi r_core^3 + 4 pi r_core^2 (R_halo - r_core)]
    #       = rho_0 * 4 pi r_core^2 * [r_core/3 + R_halo - r_core]
    #       = rho_0 * 4 pi r_core^2 * [R_halo - 2 r_core/3]
    V_eff = 4 * math.pi * r_core_m**2 * (R_halo_m - 2 * r_core_m / 3)
    rho_0 = M_cum_total_kg / V_eff if V_eff > 0 else 0
    
    if r_m < r_core_m:
        # Inside core: M_enclosed = (4/3) pi r^3 rho_0
        M_cum_enclosed = (4/3) * math.pi * r_m**3 * rho_0
    else:
        # Outside core: M_enclosed = M_core + 4 pi rho_0 r_core^2 (r - r_core)
        M_core = (4/3) * math.pi * r_core_m**3 * rho_0
        M_cum_enclosed = M_core + 4 * math.pi * rho_0 * r_core_m**2 * (r_m - r_core_m)
    
    # Active contribution (clustered, follows stellar)
    M_disk = M_disk_Msun * M_sun
    R_d = R_disk_kpc * kpc_to_m
    kappa = M_halo_Msun / M_disk_Msun if M_disk_Msun > 0 else 0
    M_stellar_enclosed = M_disk * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    M_active_enclosed = f_active * kappa * M_stellar_enclosed
    
    M_DM_enclosed = M_cum_enclosed + M_active_enclosed
    g_dm = G * M_DM_enclosed / r_m**2 if r_m > 0 else 0
    return g_dm

# Test 1: MW with isothermal + small f_active
print("=" * 80)
print("MW: ISOTHERMAL CUMULATIVE + SMALL f_active")
print("=" * 80)
print()
M_disk, R_disk, M_halo, R_halo = 6e10, 4, 1e12, 30

# Search over f_active, r_core_frac
print(f"  {'f_active':>10s}  {'r_core':>10s}  {'log_err':>10s}")
print("-" * 50)

best = None
best_err = float('inf')
for f_active in [0.0, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3]:
    for r_core_frac in [0.01, 0.05, 0.1, 0.2, 0.3, 0.5]:
        total_err = 0
        n_radii = 0
        for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]:
            if r > R_halo * 0.8:
                continue
            g_b = g_bar_disk(r, M_disk, R_disk)
            if g_b <= 0:
                continue
            g_dm = g_DM_isothermal(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac)
            g_obs = g_b + g_dm
            g_obs_rar = rar(g_b, g_plus_galaxy)
            if g_obs_rar > 0:
                err = (math.log(g_obs / g_obs_rar))**2
                total_err += err
                n_radii += 1
        if n_radii > 0:
            total_err /= n_radii
        if total_err < best_err:
            best_err = total_err
            best = (f_active, r_core_frac)

print(f"BEST: f_active={best[0]}, r_core_frac={best[1]}, log_err={best_err:.3f}")
print()

f_active, r_core_frac = best
r_core = r_core_frac * R_halo
print(f"Detailed g_obs(g_bar) for f_active={f_active}, r_core={r_core:.1f} kpc:")
print(f"  {'r (kpc)':>8s}  {'g_bar':>12s}  {'g_obs':>12s}  {'g_obs_RAR':>12s}  {'diff':>8s}")
for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]:
    g_b = g_bar_disk(r, M_disk, R_disk)
    g_dm = g_DM_isothermal(r, M_disk, R_disk, M_halo, R_halo, f_active, r_core_frac)
    g_obs = g_b + g_dm
    g_obs_rar = rar(g_b, g_plus_galaxy)
    diff = (g_obs - g_obs_rar) / g_obs_rar
    print(f"  {r:>8.1f}  {g_b:>12.3e}  {g_obs:>12.3e}  {g_obs_rar:>12.3e}  {diff:>8.2f}")
