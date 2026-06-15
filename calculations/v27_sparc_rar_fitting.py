"""
Test #2: f_active from RAR (Radial Acceleration Relation) fitting
===================================================================

The RAR is: g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_+) ))
           or
           g_obs = g_bar / μ(g_bar/a_0)
where μ is the MOND interpolation function and a_0 = g_+ ~ 1.2e-10 m/s²

For the cascade:
- f_active determines the effective M_bar from the cascade
- The cascade predicts the SAME RAR as MOND, but with a specific
  physical mechanism (2D universe deaths provide the missing gravity)

Test: fit the RAR to SPARC galaxies and see if a_0 ~ g_+ ~ 1.2e-10 m/s²
"""

import numpy as np
import glob
import os

print("=" * 80)
print("TEST 2: RAR (RADIAL ACCELERATION RELATION) FITTING")
print("=" * 80)
print()

# Constants
G_N = 6.674e-11
kpc_m = 3.086e19
km_s_to_m_s = 1000

# =============================================================================
# Read SPARC and compute g_obs, g_bar at each radius
# =============================================================================
sparc_dir = "/workspace/github-repo/calculations/sparc_data"
files = sorted(glob.glob(f"{sparc_dir}/*_rotmod.dat"))

# Collect all (g_bar, g_obs) points
g_bars = []
g_obss = []
galaxy_names = []

for f in files:
    name = os.path.basename(f).replace("_rotmod.dat", "")
    try:
        data = np.loadtxt(f, comments='#')
        if data.shape[0] < 3:
            continue
        rad = data[:, 0]  # kpc
        vobs = data[:, 1]  # km/s
        vgas = data[:, 3]
        vdisk = data[:, 4]
        vbul = data[:, 5]

        # Vbar^2 = Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2
        vbar_sq = vgas**2 + 0.5 * vdisk**2 + 0.7 * vbul**2

        # g_obs = V^2 / r (in m/s^2)
        # Convert: V (km/s), r (kpc)
        # g = V^2 / r × (km/s)²/kpc × 1e6 (m/s)² / (1e3)² (km/s)² × 3.086e19 m/kpc
        #    = V^2 / r × 1e6 × 3.086e19 / 1e3  ... actually let me just compute carefully
        V_m_s = vobs * 1000  # m/s
        r_m = rad * kpc_m  # m
        g_obs = V_m_s**2 / r_m  # m/s²

        Vbar_m_s = np.sqrt(vbar_sq) * 1000  # m/s
        g_bar = Vbar_m_s**2 / r_m  # m/s²

        # Filter: g_bar > 1e-12 (avoid noise at large r)
        mask = (g_bar > 1e-12) & (g_obs > 1e-12)
        g_bars.extend(g_bar[mask].tolist())
        g_obss.extend(g_obs[mask].tolist())
        galaxy_names.extend([name] * np.sum(mask))
    except Exception as e:
        continue

g_bars = np.array(g_bars)
g_obss = np.array(g_obss)

print(f"Total data points: {len(g_bars)}")
print(f"g_bar range: {g_bars.min():.2e} to {g_bars.max():.2e} m/s²")
print(f"g_obs range: {g_obss.min():.2e} to {g_obss.max():.2e} m/s²")
print()

# =============================================================================
# Fit g_+ from RAR
# =============================================================================
# Use MOND interpolation: g_obs = g_bar / μ(g_bar/a_0)
# Simple form: μ(x) = x / (1 + x) where x = sqrt(g_bar / a_0)
# Or: μ(x) = x for x < 1, μ = 1 for x > 1
# Or: g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_+)))

# The cascade's prediction is: g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_+)))
# Fit g_+ to minimize residuals

def RAR(g_bar, g_plus):
    """Cascade's RAR prediction: g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_+)))"""
    return g_bar / (1 - np.exp(-np.sqrt(g_bar / g_plus)))

# Try different g_+ values
print("Fitting g_+ to minimize RMS log residuals:")
print()
print(f"{'g_+':>12} | {'RMS log':>10} | {'Mean offset':>12}")
print("-" * 45)

best_g_plus = None
best_rms = np.inf

for g_plus_log in np.linspace(-11, -9, 50):
    g_plus = 10**g_plus_log
    g_obs_pred = RAR(g_bars, g_plus)
    log_residuals = np.log10(g_obss) - np.log10(g_obs_pred)
    rms = np.sqrt(np.mean(log_residuals**2))
    mean_offset = np.mean(log_residuals)
    if rms < best_rms:
        best_rms = rms
        best_g_plus = g_plus
    if abs(g_plus_log - np.log10(1.2e-10)) < 0.1:
        print(f"{g_plus:12.2e} | {rms:10.3f} | {mean_offset:+12.3f}")

print()
print(f"Best fit g_+: {best_g_plus:.2e} m/s²")
print(f"Best fit RMS: {best_rms:.3f} dex")
print()

# Compare to MOND's a_0
a_0 = 1.2e-10  # m/s²
print(f"MOND's a_0: {a_0:.2e} m/s²")
print(f"Cascade's g_+ best fit: {best_g_plus:.2e} m/s²")
print(f"Ratio: {best_g_plus / a_0:.3f}")
print()

# =============================================================================
# Use only low-acceleration points (a < a_0)
# =============================================================================
print("=" * 80)
print("LOW-ACCELERATION SUBSET (g_bar < 1.5 × a_0)")
print("=" * 80)
print()
low_acc_mask = g_bars < 1.5 * a_0
g_bars_low = g_bars[low_acc_mask]
g_obss_low = g_obss[low_acc_mask]
print(f"Points with g_bar < 1.5 × a_0: {np.sum(low_acc_mask)}")
print()

# Fit only low-acceleration points
best_g_plus_low = None
best_rms_low = np.inf
for g_plus_log in np.linspace(-11, -9, 50):
    g_plus = 10**g_plus_log
    g_obs_pred = RAR(g_bars_low, g_plus)
    log_residuals = np.log10(g_obss_low) - np.log10(g_obs_pred)
    rms = np.sqrt(np.mean(log_residuals**2))
    if rms < best_rms_low:
        best_rms_low = rms
        best_g_plus_low = g_plus

print(f"Best fit g_+ (low accel only): {best_g_plus_low:.2e} m/s²")
print(f"Best fit RMS (low accel only): {best_rms_low:.3f} dex")
print()

# =============================================================================
# Honest verdict
# =============================================================================
print("=" * 80)
print("HONEST VERDICT: RAR TEST")
print("=" * 80)
print()
print(f"Best fit g_+: {best_g_plus:.2e} m/s²")
print(f"Reference: g_+ = 1.2e-10 m/s² (McGaugh 2016)")
print(f"Ratio: {best_g_plus / 1.2e-10:.3f}")
print()
print("If g_+ matches 1.2e-10, this CONFIRMS the cascade's MOND-like behavior")
print("The cascade's g_+ is EMPIRICAL, not derived")
print()
print("This RAR fit is the SAME as MOND's fit, not unique to cascade")
print("But it constrains the cascade's f_active to match RAR")
print()

# Save results
result = {
    'best_g_plus': float(best_g_plus),
    'best_rms': float(best_rms),
    'best_g_plus_low': float(best_g_plus_low),
    'best_rms_low': float(best_rms_low),
    'N_points': len(g_bars),
    'N_low_accel_points': np.sum(low_acc_mask),
    'reference_a_0': 1.2e-10,
}
print(f"Result: {result}")
