#!/usr/bin/env python3
"""
Residual correlation test for the cascade's RAR.

The cascade predicts: f_active ∝ current SFR
This means: at FIXED g_bar, galaxies with higher SFR should have HIGHER g_obs
(their f_active is higher, so more active DM contribution)

Test: does the cascade's per-galaxy residual correlate with SFR in the
predicted way? If yes, this is a strong testable prediction. If no,
the cascade's population fit is just curve-fitting.
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

def g_DM(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, R_halo_kpc, f_active, r_core_frac, scale):
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

# Generate galaxies with realistic SFR
np.random.seed(42)
galaxies = []
M_halo_values = np.logspace(8, 13, 30)
for i, M_halo in enumerate(M_halo_values):
    kappa = 5 + (i % 10) * 10
    M_disk = M_halo / kappa
    R_disk = 4 * (M_halo / 1e12) ** 0.4
    if R_disk < 0.2:
        R_disk = 0.2
    R_halo = 8 * R_disk
    # Realistic main sequence SFR with scatter
    SFR_MS = M_disk / 1e9
    SFR = SFR_MS * 10**np.random.normal(0, 0.3)
    galaxies.append((f"Galaxy_{i+1}", M_disk, R_disk, M_halo, R_halo, kappa, SFR))

# Use SINGLE params (f_active=0.05) to test if the residual
# correlates with SFR even without using SFR in the model
# This is a stronger test

def get_residuals(galaxies, f_active_const=0.05, r_core_frac_const=0.25, scale_const=0.15):
    """Get per-galaxy residual at a specific radius (e.g., 2*R_disk)"""
    results = []
    for name, M_disk, R_disk, M_halo, R_halo, kappa, SFR in galaxies:
        # Use 2*R_disk as a representative radius
        r = 2 * R_disk
        if r > R_halo * 0.9:
            r = R_halo * 0.5
        g_b = g_bar_disk(r, M_disk, R_disk)
        if g_b <= 0:
            continue
        g_dm = g_DM(r, M_disk, R_disk, M_halo, R_halo, f_active_const, r_core_frac_const, scale_const)
        g_obs = g_b + g_dm
        g_obs_rar = rar(g_b, g_plus_galaxy)
        if g_obs_rar > 0:
            residual = (g_obs - g_obs_rar) / g_obs_rar  # signed residual
            results.append((name, M_halo, M_disk, SFR, g_b, residual))
    return results

def correlation(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    den_x = sum((xi - mean_x)**2 for xi in x) ** 0.5
    den_y = sum((yi - mean_y)**2 for yi in y) ** 0.5
    return num / (den_x * den_y) if den_x * den_y > 0 else 0

# Get residuals with single params
results = get_residuals(galaxies)
SFRs = [r[3] for r in results]
residuals = [r[5] for r in results]
M_halos = [r[1] for r in results]
g_bars = [r[4] for r in results]

print("=" * 80)
print("RESIDUAL CORRELATION TEST (using SINGLE params, no SFR in model)")
print("=" * 80)
print()
print("If the cascade's f_active ∝ SFR is the right physics, then the residual")
print("(with single params, ignoring SFR) should correlate with SFR.")
print()
print(f"  Total data points: {len(results)}")
print()
print("Predicted sign of correlation:")
print("  SFR ↑ → f_active should be higher → g_obs should be higher → residual should be MORE POSITIVE")
print("  (positive residual = cascade predicts higher g_obs than RAR)")
print()

# Compute correlations
corr_SFR = correlation([math.log10(s+1) for s in SFRs], residuals)
corr_Mhalo = correlation([math.log10(m) for m in M_halos], residuals)
corr_gbar = correlation([math.log10(g) for g in g_bars], residuals)
corr_Mstar = correlation([math.log10(m) for m in [r[2] for r in results]], residuals)

print("Correlations (using single params, f_active=0.05):")
print(f"  residual vs log(SFR):      {corr_SFR:+.3f}")
print(f"  residual vs log(M_halo):   {corr_Mhalo:+.3f}")
print(f"  residual vs log(M_star):   {corr_Mstar:+.3f}")
print(f"  residual vs log(g_bar):    {corr_gbar:+.3f}")
print()

# Interpretation
if corr_SFR > 0.3:
    print("INTERPRETATION: residual POSITIVELY correlates with SFR")
    print("  Consistent with cascade prediction: high-SFR galaxies have")
    print("  insufficient f_active in the single-params model (they need higher)")
elif corr_SFR < -0.3:
    print("INTERPRETATION: residual NEGATIVELY correlates with SFR")
    print("  OPPOSITE of cascade prediction")
else:
    print("INTERPRETATION: weak correlation, no clear SFR signal")
    print("  Cascade's SFR-f_active prediction is NOT visible in the data")

print()
print("Compare to mass correlations:")
print(f"  residual vs M_halo: {corr_Mhalo:+.3f}")
print(f"  residual vs M_star: {corr_Mstar:+.3f}")
print()

# Now try: split galaxies into HIGH-SFR and LOW-SFR bins
# Check if the cascade's fit is better for LOW-SFR galaxies
# (where single-params f_active=0.05 is more appropriate)
high_sfr = [r for r in results if math.log10(r[3]+1) > 0.5]
low_sfr = [r for r in results if math.log10(r[3]+1) <= 0.5]

print("=" * 80)
print("SPLIT ANALYSIS: residual mean by SFR bin")
print("=" * 80)
print()

if high_sfr:
    mean_resid_high = np.mean([r[5] for r in high_sfr])
    print(f"  HIGH-SFR galaxies (n={len(high_sfr)}): mean residual = {mean_resid_high:+.3f}")
if low_sfr:
    mean_resid_low = np.mean([r[5] for r in low_sfr])
    print(f"  LOW-SFR galaxies (n={len(low_sfr)}): mean residual = {mean_resid_low:+.3f}")

print()
if high_sfr and low_sfr:
    diff = mean_resid_high - mean_resid_low
    print(f"  Difference (high - low): {diff:+.3f}")
    print()
    if diff > 0.1:
        print("  Cascade PREDICTS this: high-SFR galaxies need higher f_active")
        print("  to match the RAR, so single-params UNDER-predicts for them")
    elif diff < -0.1:
        print("  OPPOSITE of cascade prediction: high-SFR galaxies are LOWER")
