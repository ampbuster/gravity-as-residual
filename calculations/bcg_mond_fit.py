#!/usr/bin/env python3
"""
Test the cascade-MOND hybrid on Tian+ 2024 cluster data (50 BCGs).
"""

import math
import numpy as np
import json
import os

def mond(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

# Load Tian+ 2024 data
with open('/workspace/github-repo/supporting/data/Tian/tian_bcgs.json', 'r') as f:
    bcgs = json.load(f)

# Extract g_bar and g_obs
g_bars = np.array([10**b['log_gbar'] for b in bcgs])
g_obss = np.array([10**b['log_gobs'] for b in bcgs])
M_bars = np.array([10**b['log_Mbar'] for b in bcgs])
zs = np.array([b['z'] for b in bcgs])

print("=" * 80)
print("TIAN+ 2024 BCG CLUSTER DATA (50 BCGs)")
print("=" * 80)
print()
print(f"  N galaxies: {len(bcgs)}")
print(f"  M_bar range: {min(M_bars):.2e} - {max(M_bars):.2e} M_sun")
print(f"  g_bar range: {min(g_bars):.2e} - {max(g_bars):.2e} m/s^2")
print(f"  g_obs range: {min(g_obss):.2e} - {max(g_obss):.2e} m/s^2")
print(f"  g_obs/g_bar range: {min(g_obss/g_bars):.2f} - {max(g_obss/g_bars):.2f}")
print()

# Test MOND with various g_+
# Per Tian+ 2024: g_+ = 1.7e-9 m/s^2 for clusters
# Per McGaugh+ 2016: g_+ = 1.2e-10 m/s^2 for galaxies
# Test both

g_plus_values = [1.2e-10, 5e-10, 1e-9, 1.7e-9, 2e-9, 3e-9, 5e-9, 1e-8]
print(f"  {'g_+ (m/s^2)':>14s}  {'median abs diff':>16s}  {'within 20%':>12s}  {'within 50%':>12s}")
print()

best_g_plus = None
best_median = float('inf')
for g_plus in g_plus_values:
    abs_diffs = []
    for g_b, g_o in zip(g_bars, g_obss):
        g_mond = mond(g_b, g_plus)
        abs_diffs.append(abs(g_mond - g_o) / g_o)
    median = np.median(abs_diffs)
    within_20 = sum(1 for d in abs_diffs if d < 0.20) / len(abs_diffs) * 100
    within_50 = sum(1 for d in abs_diffs if d < 0.50) / len(abs_diffs) * 100
    print(f"  {g_plus:>14.2e}  {median:>16.2%}  {within_20:>11.1f}%  {within_50:>11.1f}%")
    if median < best_median:
        best_median = median
        best_g_plus = g_plus

# Best fit
print()
print(f"Best g_+: {best_g_plus:.2e} (median residual: {best_median:.2%})")
print()

# Now do a per-galaxy best fit
print("=" * 80)
print("PER-BCG BEST FIT (find g_+ per galaxy)")
print("=" * 80)
print()

best_gps = []
for g_b, g_o, z, M_b in zip(g_bars, g_obss, zs, M_bars):
    best_gp = None
    best_err = float('inf')
    for log_gp in np.linspace(-11, -7, 100):
        g_plus = 10**log_gp
        g_mond = mond(g_b, g_plus)
        if g_mond > 0:
            err = abs(g_mond - g_o) / g_o
            if err < best_err:
                best_err = err
                best_gp = g_plus
    best_gps.append(best_gp)

best_gps = np.array(best_gps)

print(f"  log10(g_+) distribution:")
print(f"    mean: {np.mean(np.log10(best_gps)):+.2f}")
print(f"    median: {np.median(np.log10(best_gps)):+.2f}")
print(f"    std: {np.std(np.log10(best_gps)):.2f}")
print(f"    physical median: {np.median(best_gps):.2e} m/s^2")
print()
print(f"  Tian+ 2024 measured: g_+ = 1.7e-9 m/s^2")
print()

# Correlations
print("Correlations:")
print(f"  log(g_+) vs z: {np.corrcoef(zs, np.log10(best_gps))[0, 1]:+.3f}")
print(f"  log(g_+) vs log(M_bar): {np.corrcoef(np.log10(M_bars), np.log10(best_gps))[0, 1]:+.3f}")
print()

# Save
results = {
    'n_bcgs': len(bcgs),
    'best_fixed_g_plus': best_g_plus,
    'best_fixed_median_resid': best_median,
    'per_bcg_g_plus': {
        'mean_log': float(np.mean(np.log10(best_gps))),
        'median_log': float(np.median(np.log10(best_gps))),
        'std_log': float(np.std(np.log10(best_gps))),
        'physical_median': float(np.median(best_gps))
    },
    'tian_2024_g_plus': 1.7e-9
}
with open('/workspace/github-repo/supporting/data/Tian/bcg_mond_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print("Saved to bcg_mond_results.json")
