#!/usr/bin/env python3
"""
Try Einasto profile for g_cum to see if it closes the 8% residual.

The cascade's isothermal profile (1/r^2 density, g_cum ~ 1/r) is the
LIMIT of an Einasto profile with shape parameter alpha = 1/2 (very flat core).
Real galaxies often have alpha = 0.1-0.3 (mild cores).

If the cascade's g_cum follows an Einasto profile with the right alpha,
the RAR fit might be better than 8%.
"""

import math
import numpy as np

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
g_plus_galaxy = 1.2e-10

def rar(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

def g_bar_disk(r_kpc, M_disk_Msun, R_disk_kpc):
    r_m = r_kpc * kpc_to_m
    M_disk_enclosed = M_disk_Msun * M_sun * (1 - (1 + r_m/(R_disk_kpc * kpc_to_m)) * math.exp(-r_m/(R_disk_kpc * kpc_to_m)))
    return G * M_disk_enclosed / r_m**2 if r_m > 0 else 0

def g_cum_einasto(r_kpc, M_halo_Msun, R_halo_kpc, alpha=0.2, r_s_frac=0.1):
    """Einasto cumulative mass profile.
    rho(r) = rho_s * exp(-2/alpha * ((r/r_s)^alpha - 1))
    M(r) = integral
    """
    r_m = r_kpc * kpc_to_m
    r_s = r_s_frac * R_halo_kpc * kpc_to_m
    R_halo_m = R_halo_kpc * kpc_to_m
    if r_m <= 0:
        return 0
    # M(r) = 4*pi*rho_s*r_s^3 * (alpha/2)^(3/alpha) * exp(3/alpha) * gamma(3/alpha) * P(3/alpha, 2/alpha * (r/r_s)^alpha)
    # This is complex; use numerical integration
    n_steps = 200
    r_max = min(r_m, R_halo_m)
    dr = r_max / n_steps
    integral = 0
    for i in range(n_steps):
        r = (i + 0.5) * dr
        # Einasto density
        rho = math.exp(-2.0/alpha * ((r/r_s)**alpha - 1))
        shell_vol = 4 * math.pi * r**2 * dr
        integral += rho * shell_vol
    # Normalize so that M(R_halo) = M_halo
    n_norm = 200
    r_max_norm = R_halo_m
    dr_norm = r_max_norm / n_norm
    integral_norm = 0
    for i in range(n_norm):
        r = (i + 0.5) * dr_norm
        rho = math.exp(-2.0/alpha * ((r/r_s)**alpha - 1))
        shell_vol = 4 * math.pi * r**2 * dr_norm
        integral_norm += rho * shell_vol
    # M_halo = M_halo (kg)
    M_halo_kg = M_halo_Msun * M_sun
    rho_s = M_halo_kg / integral_norm
    M_enclosed_kg = rho_s * integral
    return G * M_enclosed_kg / r_m**2

def g_active(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, r_core_frac):
    """Active DM contribution (clustered with stars)"""
    r_core_m = r_core_frac * R_halo_kpc * kpc_to_m
    r_m = r_kpc * kpc_to_m
    M_disk = M_disk_Msun * M_sun
    R_d = R_disk_kpc * kpc_to_m
    kappa = M_halo_Msun / M_disk_Msun if M_disk_Msun > 0 else 0
    M_stellar_enclosed = M_disk * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    M_active_enclosed = f_active * kappa * M_stellar_enclosed
    return G * M_active_enclosed / r_m**2 if r_m > 0 else 0

# Test on MW
M_disk, R_disk, M_halo, R_halo = 6e10, 4, 1e12, 30

print("=" * 80)
print("EINASTO PROFILE TEST")
print("=" * 80)
print()
print(f"  MW: M_disk={M_disk:.1e}, R_disk={R_disk}, M_halo={M_halo:.1e}, R_halo={R_halo}")
print()

# Grid search over Einasto alpha and f_active, r_core_frac, scale
best = None
best_err = float('inf')
for alpha in [0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5]:
    for r_s_frac in [0.05, 0.1, 0.2, 0.3]:
        for f_active in [0.005, 0.01, 0.02, 0.05, 0.1]:
            for r_core_frac in [0.1, 0.2, 0.3, 0.4]:
                for scale in [0.05, 0.1, 0.15, 0.2, 0.3]:
                    total_err = 0
                    n = 0
                    max_off = 0
                    for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]:
                        g_b = g_bar_disk(r, M_disk, R_disk)
                        if g_b <= 0:
                            continue
                        # Cumulative
                        g_cum = g_cum_einasto(r, scale * M_halo, R_halo, alpha, r_s_frac)
                        # Active
                        g_act = g_active(r, M_disk, R_disk, scale * M_halo, R_halo, f_active, r_core_frac)
                        # Wait - in the hybrid, active uses scale*M_halo? 
                        # No, in pure cascade, M_cascade = scale * M_halo
                        # The active contribution is f_active * kappa of the STELLAR mass
                        # kappa here is M_cascade / M_disk
                        g_obs = g_b + g_cum + g_act
                        g_obs_rar = rar(g_b, g_plus_galaxy)
                        if g_obs_rar > 0:
                            total_err += (math.log(g_obs / g_obs_rar))**2
                            diff = abs((g_obs - g_obs_rar) / g_obs_rar)
                            max_off = max(max_off, diff)
                            n += 1
                    if n > 0:
                        total_err /= n
                    if total_err < best_err:
                        best_err = total_err
                        best = (alpha, r_s_frac, f_active, r_core_frac, scale, max_off)

alpha, r_s_frac, f_active, r_core_frac, scale, max_off = best
print(f"Best Einasto fit: alpha={alpha}, r_s_frac={r_s_frac}, f_active={f_active}, r_core_frac={r_core_frac}, scale={scale}")
print(f"  log_err={best_err:.5f}, max_off={max_off*100:.2f}%")
print()
print("Detailed fit:")
print(f"  {'r (kpc)':>8s}  {'g_bar':>12s}  {'g_cum':>12s}  {'g_act':>12s}  {'g_obs':>12s}  {'RAR':>12s}  {'diff':>8s}")
for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]:
    g_b = g_bar_disk(r, M_disk, R_disk)
    if g_b <= 0:
        continue
    g_cum = g_cum_einasto(r, scale * M_halo, R_halo, alpha, r_s_frac)
    g_act = g_active(r, M_disk, R_disk, scale * M_halo, R_halo, f_active, r_core_frac)
    g_obs = g_b + g_cum + g_act
    g_rar = rar(g_b, g_plus_galaxy)
    diff = (g_obs - g_rar) / g_rar
    print(f"  {r:>8.1f}  {g_b:>12.3e}  {g_cum:>12.3e}  {g_act:>12.3e}  {g_obs:>12.3e}  {g_rar:>12.3e}  {diff:>+7.2%}")

print()
print("=" * 80)
print("COMPARISON TO ISOTHERMAL")
print("=" * 80)
print()
print("Isothermal baseline (Limitation 19):")
print("  f_active=0.02, r_core_frac=0.25, scale=0.15")
print("  log_err=0.00046, max_off=8.0%")
print()
print(f"Einasto best: log_err={best_err:.5f}, max_off={max_off*100:.2f}%")
if best_err < 0.00046:
    print("EINASTO IMPROVES the fit")
else:
    print("EINASTO does NOT improve over isothermal")
