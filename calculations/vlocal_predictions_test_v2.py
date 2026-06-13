#!/usr/bin/env python3
"""
Test V_local predictions on Tian+ 2024 BCG data, v2.
Uses deep MOND approximation: g_+ = g_obs^2 / g_bar
"""

import json
import numpy as np

# Load BCG data
with open('supporting/data/Tian/tian_bcgs.json', 'r') as f:
    bcgs = json.load(f)

print(f"Loaded {len(bcgs)} BCGs from Tian+ 2024")
print()

# For each BCG, estimate g_+ using deep MOND approximation
g_plus_arr = []
log_Mbar_arr = []
sigma_arr = []
z_arr = []
g_bar_arr = []
g_obs_arr = []
N_Sersic_arr = []
Reff_arr = []

for bcg in bcgs:
    g_bar = 10**bcg['log_gbar']
    g_obs = 10**bcg['log_gobs']
    g_plus = g_obs**2 / g_bar  # deep MOND limit
    g_plus_arr.append(g_plus)
    log_Mbar_arr.append(bcg['log_Mbar'])
    sigma_arr.append(bcg['sigma_los'])
    z_arr.append(bcg['z'])
    g_bar_arr.append(g_bar)
    g_obs_arr.append(g_obs)
    N_Sersic_arr.append(bcg['N_Sersic'])
    Reff_arr.append(bcg['Reff_kpc'])

g_plus_arr = np.array(g_plus_arr)
log_g_plus = np.log10(g_plus_arr)
log_Mbar_arr = np.array(log_Mbar_arr)
sigma_arr = np.array(sigma_arr)
log_sigma = np.log10(sigma_arr)
z_arr = np.array(z_arr)
g_bar_arr = np.array(g_bar_arr)
g_obs_arr = np.array(g_obs_arr)
N_Sersic_arr = np.array(N_Sersic_arr)
Reff_arr = np.array(Reff_arr)

print(f"Computed g_+ for {len(g_plus_arr)} BCGs")
print(f"Median g_+: {np.median(g_plus_arr):.3e} m/s^2")
print(f"Mean log g_+: {np.mean(log_g_plus):.3f} ± {np.std(log_g_plus):.3f}")
print()

# === Test prediction 1: g_+ correlates with M_bar ===
print("=" * 80)
print("PREDICTION 1: g_+ correlates with M_bar (MOND-like scaling)")
print("=" * 80)
print()
correlation_mass = np.corrcoef(log_g_plus, log_Mbar_arr)[0, 1]
slope_mass = np.polyfit(log_Mbar_arr, log_g_plus, 1)[0]
intercept_mass = np.polyfit(log_Mbar_arr, log_g_plus, 1)[1]
print(f"Correlation (log g_+, log M_bar): r = {correlation_mass:.3f}")
print(f"Slope: {slope_mass:.3f}")
print(f"Intercept: {intercept_mass:.3f}")
print()
print("Expected: slope ~ 0.5-0.6 (Tian+ 2024 scaling, MOND EFE)")
print(f"Observed: slope = {slope_mass:.3f}")
print()

# === Test prediction 2: g_+ correlates with sigma ===
print("=" * 80)
print("PREDICTION 2: g_+ correlates with sigma (cluster dynamical mass proxy)")
print("=" * 80)
print()
correlation_sigma = np.corrcoef(log_g_plus, log_sigma)[0, 1]
slope_sigma = np.polyfit(log_sigma, log_g_plus, 1)[0]
print(f"Correlation (log g_+, log sigma): r = {correlation_sigma:.3f}")
print(f"Slope: {slope_sigma:.3f}")
print()
print("Expected: g_+ ∝ sigma^2 (MOND EFE)")
print(f"Observed: g_+ ∝ sigma^{slope_sigma:.2f}")
print()

# === Test prediction 3: g_+ vs z (cosmic time) ===
print("=" * 80)
print("PREDICTION 3: g_+ evolves with z?")
print("=" * 80)
print()
correlation_z = np.corrcoef(log_g_plus, z_arr)[0, 1]
print(f"Correlation (log g_+, z): r = {correlation_z:.3f}")
print()
print("If non-zero, suggests g_+ evolves with cosmic time")
print()

# === Test prediction 4: g_+ depends on Reff (size) ===
print("=" * 80)
print("PREDICTION 4: g_+ depends on Reff (BCG size)?")
print("=" * 80)
print()
log_Reff = np.log10(Reff_arr)
correlation_Reff = np.corrcoef(log_g_plus, log_Reff)[0, 1]
slope_Reff = np.polyfit(log_Reff, log_g_plus, 1)[0]
print(f"Correlation (log g_+, log Reff): r = {correlation_Reff:.3f}")
print(f"Slope: {slope_Reff:.3f}")
print()

# === Test prediction 5: Split by Sersic index ===
print("=" * 80)
print("PREDICTION 5: g_+ by BCG morphology (Sersic index)")
print("=" * 80)
print()
core_BCGs = N_Sersic_arr > 4
print(f"Core BCGs (N > 4): {np.sum(core_BCGs)}")
print(f"Median g_+ (core): {np.median(g_plus_arr[core_BCGs]):.3e} m/s^2")
print(f"Median g_+ (non-core): {np.median(g_plus_arr[~core_BCGs]):.3e} m/s^2")
ratio_core = np.median(g_plus_arr[core_BCGs]) / np.median(g_plus_arr[~core_BCGs])
print(f"Ratio (core/non-core): {ratio_core:.2f}")
print()

# === Summary ===
print("=" * 80)
print("SUMMARY: V_local PREDICTIONS vs DATA")
print("=" * 80)
print()
print(f"1. g_+ ∝ M_b^{slope_mass:.2f}  (Tian+ 2024 expects ~0.5-0.6)")
print(f"2. g_+ ∝ σ^{slope_sigma:.2f}    (MOND EFE expects ~2)")
print(f"3. g_+ vs z: r = {correlation_z:.3f}  (cascade expects ~0)")
print(f"4. g_+ vs Reff: slope = {slope_Reff:.2f}  (cascade expects weakly negative)")
print(f"5. Core vs non-core BCGs: {ratio_core:.2f}x  (cascade expects >1)")
print()

# Save results
results = {
    "n_bcgs": len(bcgs),
    "median_g_plus": float(np.median(g_plus_arr)),
    "mean_log_g_plus": float(np.mean(log_g_plus)),
    "std_log_g_plus": float(np.std(log_g_plus)),
    "predictions": {
        "g_plus_vs_Mbar": {
            "correlation": float(correlation_mass),
            "slope": float(slope_mass),
            "intercept": float(intercept_mass)
        },
        "g_plus_vs_sigma": {
            "correlation": float(correlation_sigma),
            "slope": float(slope_sigma)
        },
        "g_plus_vs_z": {
            "correlation": float(correlation_z)
        },
        "g_plus_vs_Reff": {
            "correlation": float(correlation_Reff),
            "slope": float(slope_Reff)
        },
        "core_vs_noncore": {
            "core_median": float(np.median(g_plus_arr[core_BCGs])),
            "noncore_median": float(np.median(g_plus_arr[~core_BCGs])),
            "ratio": float(ratio_core)
        }
    }
}

with open('supporting/data/Tian/vlocal_predictions_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Results saved.")
