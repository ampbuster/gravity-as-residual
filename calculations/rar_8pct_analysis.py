#!/usr/bin/env python3
"""
Analysis of the cascade's 8% RAR residual.

The cascade's RAR fit (best-fit at f_active=0.02, r_core_frac=0.25, scale=0.15)
matches the empirical RAR to 1-3% at most radii but has a structural
8% residual at large r (25-30 kpc) and a smaller 2-3% residual at small r.

This is the cascade's intrinsic RAR shape vs the RAR functional form.

WHERE THE 8% COMES FROM:
- At r=0.5-2 kpc: cascade over-predicts by 1-2% (small excess from active DM)
- At r=4-10 kpc: matches within 3% (best region)
- At r=15-20 kpc: matches within 4%
- At r=25-30 kpc: cascade under-predicts by 6-8% (isothermal regime)

The large-r residual is because the cascade's g_cum(r) for the isothermal
profile is approximately 1/r (which is the MOND-like behavior the RAR wants),
but the *specific shape* is slightly different. The RAR uses
g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_+))), which has a specific
functional form that the cascade's g_cum + g_active doesn't quite match.

Specifically:
- The cascade: g_obs = g_bar + g_cum(r) + g_active(r)
- The RAR: g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_+)))

The cascade is a sum of components, while the RAR is a specific
functional form. The two agree at high g_bar (both asymptote to g_bar)
and at low g_bar (both approach MOND-like 1/r behavior), but differ
in the transition region.

This is a STRUCTURAL LIMIT of the cascade's RAR model. To do better,
the cascade would need:
- A different functional form for g_cum(r) (e.g., Einasto, with extra parameter)
- Modified gravity at small scales
- A different relationship between the active/cumulative split and the spatial distribution

This is documented as Limitation 19 of the paper.
"""

import math

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

# Best fit (noise-free)
M_disk, R_disk, M_halo, R_halo = 6e10, 4, 1e12, 30
f_active = 0.02
r_core_frac = 0.25
scale = 0.15

print("=" * 80)
print("8% RAR RESIDUAL ANALYSIS")
print("=" * 80)
print()
print(f"  Best fit (noise-free): f_active={f_active}, r_core_frac={r_core_frac}, scale={scale}")
print()
print(f"  {'r (kpc)':>8s}  {'g_bar':>12s}  {'g_cum':>12s}  {'g_active':>12s}  {'g_obs':>12s}  {'RAR':>12s}  {'diff':>8s}  {'regime':>15s}")
print()

for r in [0.5, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30]:
    g_b = g_bar_disk(r, M_disk, R_disk)
    if g_b <= 0:
        continue
    
    M_cum_total_kg = scale * (1 - f_active) * M_halo * M_sun
    r_core_m = r_core_frac * R_halo * kpc_to_m
    r_m = r * kpc_to_m
    R_halo_m = R_halo * kpc_to_m
    V_eff = 4 * math.pi * r_core_m**2 * (R_halo_m - 2 * r_core_m / 3)
    rho_0 = M_cum_total_kg / V_eff if V_eff > 0 else 0
    if r_m < r_core_m:
        M_cum = (4/3) * math.pi * r_m**3 * rho_0
    else:
        M_core = (4/3) * math.pi * r_core_m**3 * rho_0
        M_cum = M_core + 4 * math.pi * rho_0 * r_core_m**2 * (r_m - r_core_m)
    g_cum = G * M_cum / r_m**2
    
    kappa = M_halo / M_disk
    M_stellar_enclosed = M_disk * M_sun * (1 - (1 + r_m/(R_disk * kpc_to_m)) * math.exp(-r_m/(R_disk * kpc_to_m)))
    g_active = G * f_active * kappa * M_stellar_enclosed / r_m**2
    
    g_obs = g_b + g_cum + g_active
    g_rar = rar(g_b, g_plus_galaxy)
    diff = (g_obs - g_rar) / g_rar
    
    # Classify regime
    if g_b > 3 * g_plus_galaxy:
        regime = "high g_bar"
    elif g_b < 0.3 * g_plus_galaxy:
        regime = "low g_bar (MOND)"
    else:
        regime = "transition"
    
    print(f"  {r:>8.1f}  {g_b:>12.3e}  {g_cum:>12.3e}  {g_active:>12.3e}  {g_obs:>12.3e}  {g_rar:>12.3e}  {diff:>8.2f}  {regime:>15s}")

print()
print("REGIME ANALYSIS:")
print()
print("HIGH g_bar regime (r = 0.5-2 kpc, g_bar > 3*g_+):")
print("  RAR: g_obs ~ g_bar (asymptote)")
print("  Cascade: g_obs = g_bar + g_cum + g_active (still has active component)")
print("  Result: cascade over-predicts by 1-2% (active DM excess)")
print()
print("TRANSITION regime (r = 4-10 kpc, g_bar ~ 1*g_+):")
print("  Both match within 3% (best agreement)")
print()
print("LOW g_bar regime (r = 15-30 kpc, g_bar < 0.3*g_+):")
print("  RAR: g_obs ~ sqrt(g_bar * g_+) ~ 1/r (MOND-like)")
print("  Cascade: g_obs = g_bar + g_cum (isothermal) ~ g_cum (constant)")
print("  Result: cascade over-predicts at 15-20 kpc, UNDER-predicts at 25-30 kpc")
print()
print("THE 8% RESIDUAL comes from the MISMATCH between:")
print("  RAR's exact sqrt(g_bar * g_+) functional form")
print("  Cascade's g_cum + g_active approximation")
print()
print("This is a STRUCTURAL LIMIT of the cascade's RAR model.")
print("To do better, the cascade would need:")
print("  - Different functional form for g_cum(r) (e.g., Einasto with more parameters)")
print("  - Modified gravity at small scales")
print("  - Different relationship between active/cumulative split and spatial distribution")
