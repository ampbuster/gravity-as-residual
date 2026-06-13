#!/usr/bin/env python3
"""
Test the cascade's V_local predictions on Tian+ 2024 BCG data.

Predictions:
1. BCG g_+ correlates with cluster ICM activity (cooling flow vs non-cooling flow)
2. BCG g_+ correlates with cluster mass (more massive = more g_+)
3. BCG g_+ correlates with velocity dispersion
4. BCG g_+ does NOT correlate with BCG's own M_bar alone (the cluster matters)
"""

import json
import numpy as np

# Load BCG data
with open('supporting/data/Tian/tian_bcgs.json', 'r') as f:
    bcgs = json.load(f)

print(f"Loaded {len(bcgs)} BCGs from Tian+ 2024")
print()

# For each BCG, estimate g_+ from MOND fit
# g_obs = g_bar / (1 - exp(-sqrt(g_bar / g_+)))
# This is hard to invert analytically, so use Newton's method

def estimate_g_plus(g_bar, g_obs, g_plus_init=1e-9, tol=1e-12, max_iter=100):
    """Estimate g_+ from g_bar and g_obs using MOND-like formula."""
    g_plus = g_plus_init
    for _ in range(max_iter):
        # g_obs = g_bar / (1 - exp(-sqrt(g_bar / g_plus)))
        ratio = g_bar / g_plus
        sqrt_ratio = np.sqrt(ratio)
        # Forward prediction
        g_obs_pred = g_bar / (1 - np.exp(-sqrt_ratio))
        # Derivative
        # d(g_obs)/d(g_+) is complex; use numerical
        dp = 1e-9 * g_plus
        g_obs_pred_p = g_bar / (1 - np.exp(-np.sqrt(g_bar / (g_plus + dp))))
        dg_obs_dg_plus = (g_obs_pred_p - g_obs_pred) / dp
        # Update
        if abs(dg_obs_dg_plus) < 1e-30:
            break
        delta = (g_obs - g_obs_pred) / dg_obs_dg_plus
        g_plus -= delta
        if abs(delta) < tol * g_plus:
            break
    return g_plus

# Compute g_+ for each BCG
g_plus_arr = []
log_Mbar_arr = []
sigma_arr = []
z_arr = []
g_bar_arr = []
g_obs_arr = []

for bcg in bcgs:
    g_bar = 10**bcg['log_gbar']
    g_obs = 10**bcg['log_gobs']
    g_plus = estimate_g_plus(g_bar, g_obs)
    g_plus_arr.append(g_plus)
    log_Mbar_arr.append(bcg['log_Mbar'])
    sigma_arr.append(bcg['sigma_los'])
    z_arr.append(bcg['z'])
    g_bar_arr.append(g_bar)
    g_obs_arr.append(g_obs)

g_plus_arr = np.array(g_plus_arr)
log_Mbar_arr = np.array(log_Mbar_arr)
sigma_arr = np.array(sigma_arr)
z_arr = np.array(z_arr)
g_bar_arr = np.array(g_bar_arr)
g_obs_arr = np.array(g_obs_arr)

print(f"Computed g_+ for {len(g_plus_arr)} BCGs")
print(f"Median g_+: {np.median(g_plus_arr):.3e} m/s^2")
print(f"Mean log(g_+): {np.mean(np.log10(g_plus_arr)):.3f} ± {np.std(np.log10(g_plus_arr)):.3f}")
print()

# === Test prediction: g_+ correlates with mass (M_bar) ===
print("=" * 80)
print("PREDICTION 1: g_+ correlates with M_bar")
print("=" * 80)
print()
log_g_plus = np.log10(g_plus_arr)
correlation_mass = np.corrcoef(log_g_plus, log_Mbar_arr)[0, 1]
print(f"Correlation (log g_+, log M_bar): r = {correlation_mass:.3f}")
print(f"Slope: {np.polyfit(log_Mbar_arr, log_g_plus, 1)[0]:.3f}")
print()

# Tian+ 2024 finds: g_+ ∝ M^0.5 (slope ~ 0.5 in log-log)
# Galaxy M_bar ~ 1e10, BCG M_bar ~ 1e12, ratio 100, g_+ ratio 14, log ratio 1.15
# log g_+ ratio / log M ratio = 1.15 / 2 = 0.57
print(f"Expected slope: 0.5-0.6 (Tian+ 2024)")
print(f"Observed slope: {np.polyfit(log_Mbar_arr, log_g_plus, 1)[0]:.3f}")
print()

# === Test prediction: g_+ correlates with sigma (velocity dispersion) ===
print("=" * 80)
print("PREDICTION 2: g_+ correlates with sigma (cluster dynamical mass proxy)")
print("=" * 80)
print()
log_sigma = np.log10(sigma_arr)
correlation_sigma = np.corrcoef(log_g_plus, log_sigma)[0, 1]
print(f"Correlation (log g_+, log sigma): r = {correlation_sigma:.3f}")
slope_sigma = np.polyfit(log_sigma, log_g_plus, 1)[0]
print(f"Slope: {slope_sigma:.3f}")
print()
print(f"Expected: g_+ ∝ sigma^2 (MOND EFE: g_+,ext = G*M/r^2 = sigma^2/r)")
print(f"Observed: g_+ ∝ sigma^{slope_sigma:.2f}")
print()

# === Test prediction: g_+ correlates with z (cosmic time)? ===
print("=" * 80)
print("PREDICTION 3: g_+ evolves with z (cosmic time)?")
print("=" * 80)
print()
correlation_z = np.corrcoef(log_g_plus, z_arr)[0, 1]
print(f"Correlation (log g_+, z): r = {correlation_z:.3f}")
print()
print("If non-zero, suggests g_+ evolves with cosmic time")
print("(cascade predicts g_+ should be approximately constant for similar-mass systems)")
print()

# === Test prediction: split by BCG "type" proxy ===
# 
# Sersic index N: low N (1-2) = disk-like, high N (3-5) = elliptical
# Core BCGs (N > 3) tend to be in more massive clusters with more cooling flow activity
# 
# Let me split and see if g_+ differs

print("=" * 80)
print("PREDICTION 4: g_+ depends on BCG Sersic index (proxy for cluster type)")
print("=" * 80)
print()
N_Sersic = np.array([bcg['N_Sersic'] for bcg in bcgs])
core_BCGs = N_Sersic > 4  # classical BCG morphology
print(f"Core BCGs (N > 4): {np.sum(core_BCGs)}")
print(f"Median g_+ (core): {np.median(g_plus_arr[core_BCGs]):.3e} m/s^2")
print(f"Median g_+ (non-core): {np.median(g_plus_arr[~core_BCGs]):.3e} m/s^2")
ratio = np.median(g_plus_arr[core_BCGs]) / np.median(g_plus_arr[~core_BCGs])
print(f"Ratio (core/non-core): {ratio:.2f}")
print()
print("Cascade V_local prediction: cluster type matters (cooling flow vs not)")
print("BUT without external cluster data (cluster mass, ICM properties),")
print("we can't directly test this.")
print()

# === Save results for paper ===
results = {
    "n_bcgs": len(bcgs),
    "median_g_plus": float(np.median(g_plus_arr)),
    "mean_log_g_plus": float(np.mean(log_g_plus)),
    "std_log_g_plus": float(np.std(log_g_plus)),
    "correlation_log_g_plus_vs_log_Mbar": float(correlation_mass),
    "slope_log_g_plus_vs_log_Mbar": float(np.polyfit(log_Mbar_arr, log_g_plus, 1)[0]),
    "correlation_log_g_plus_vs_log_sigma": float(correlation_sigma),
    "slope_log_g_plus_vs_log_sigma": float(slope_sigma),
    "correlation_log_g_plus_vs_z": float(correlation_z),
    "core_BCG_median_g_plus": float(np.median(g_plus_arr[core_BCGs])),
    "non_core_BCG_median_g_plus": float(np.median(g_plus_arr[~core_BCGs])),
    "ratio_core_to_noncore": float(ratio)
}

with open('supporting/data/Tian/vlocal_predictions_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("=" * 80)
print("SUMMARY OF V_local PREDICTION TESTS")
print("=" * 80)
print()
print(f"1. g_+ vs M_bar: r = {correlation_mass:.3f}, slope = {np.polyfit(log_Mbar_arr, log_g_plus, 1)[0]:.3f}")
print(f"   Expected: ~0.5-0.6 (Tian+ 2024 scaling)")
print(f"   Observed: {np.polyfit(log_Mbar_arr, log_g_plus, 1)[0]:.3f}")
print()
print(f"2. g_+ vs sigma: r = {correlation_sigma:.3f}, slope = {slope_sigma:.3f}")
print(f"   Expected: ~2 (MOND EFE: g_+ ∝ sigma^2/r)")
print(f"   Observed: {slope_sigma:.3f}")
print()
print(f"3. g_+ vs z: r = {correlation_z:.3f}")
print(f"   Expected: ~0 (cascade predicts constant g_+ for similar mass)")
print(f"   Observed: {correlation_z:.3f}")
print()
print(f"4. Core vs non-core BCGs: ratio = {ratio:.2f}")
print(f"   Expected: core > non-core (cooling flow more energetic)")
print(f"   Observed: {'YES' if ratio > 1 else 'NO'}")
