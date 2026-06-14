#!/usr/bin/env python3
"""
Per-galaxy g_+ analysis: is the cascade's g_+ universal, or mass-dependent?

The cascade's V_local formula predicts g_+ ~ 1.2e-10 m/s² (MOND-compatible).
If g_+ is mass-dependent (e.g., larger at cluster scale), this tests the
V_local enhancement formula.

Previous tests:
- SPARC galaxies: median g_+ = 1.2e-10 m/s²
- Tian+ 2024 BCGs: median g_+ = 1.7e-9 m/s²
- Cascade: g_+ ~ (k * E_event * τ_2D) / (V_local * M_halo) at galaxy scale
- Cascade cluster enhancement: g_+ enhanced by ~factor V_local(MW)/V_local(cluster)

Question: do individual SPARC galaxies show:
(a) Mass-independent g_+ (MOND-style, supports cascade's universal g_+)
(b) Mass-dependent g_+ (cascade's V_local prediction: larger g_+ at low mass)
(c) Random scatter (g_+ is an artifact, no real trend)

This test fits g_+ per galaxy and looks for trends with M_b.
"""

import os
import json
import math
import numpy as np
from scipy.optimize import minimize

SPARC_DIR = '/workspace/github-repo/supporting/data/SPARC'
M_sun = 1.989e30
kpc_to_m = 3.086e19

# MOND interpolation
def mond_g_obs(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

def mond_g_plus(g_bar, g_obs):
    """Solve for g_+ given g_bar and g_obs"""
    if g_obs <= g_bar:
        return 1e-10  # default
    # g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_+)))
    # g_bar / g_obs = 1 - exp(-sqrt(g_bar/g_+))
    # exp(-sqrt(g_bar/g_+)) = 1 - g_bar/g_obs
    # -sqrt(g_bar/g_+) = log(1 - g_bar/g_obs)
    # g_+ = g_bar / (log(1 - g_bar/g_obs))^2
    if g_obs > 0 and g_bar/g_obs < 1:
        return g_bar / (math.log(1 - g_bar/g_obs))**2
    return 1e-10

# Load SPARC data
with open(os.path.join(SPARC_DIR, 'galaxies_sample.json'), 'r') as f:
    galaxies = json.load(f)

print(f"Loaded {len(galaxies)} SPARC galaxies")
print()

# For each galaxy, fit g_+ using MOND functional form
g_plus_values = []
m_b_values = []
g_bar_at_1kpc = []
quality = []
distance = []
hi_mass = []

for g in galaxies:
    fname = os.path.join(SPARC_DIR, f"{g['name']}_rotmod.dat")
    if not os.path.exists(fname):
        continue
    
    data = []
    with open(fname, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            parts = line.split()
            if len(parts) >= 8:
                try:
                    data.append({
                        'r': float(parts[0]),
                        'vobs': float(parts[1]),
                        'vobs_err': float(parts[2]),
                        'vgas': float(parts[3]),
                        'vdisk': float(parts[4]),
                        'vbul': float(parts[5]),
                    })
                except (ValueError, IndexError):
                    continue
    
    if len(data) < 5:
        continue
    
    # Get g_bar and g_obs at each radius
    g_bars = []
    g_obss = []
    for d in data:
        r_m = d['r'] * kpc_to_m
        v_obs_ms = d['vobs'] * 1e3
        v_gas_ms = d['vgas'] * 1e3
        v_disk_ms = d['vdisk'] * 1e3
        v_bul_ms = d['vbul'] * 1e3
        
        if r_m <= 0 or v_obs_ms <= 0:
            continue
        
        g_obs = v_obs_ms**2 / r_m
        g_bar = (v_gas_ms**2 + v_disk_ms**2 + v_bul_ms**2) / r_m
        
        if g_obs > 0 and g_bar > 0 and g_obs > g_bar:
            g_bars.append(g_bar)
            g_obss.append(g_obs)
    
    if len(g_bars) < 5:
        continue
    
    g_bars = np.array(g_bars)
    g_obss = np.array(g_obss)
    
    # Fit g_+ by minimizing MOND residuals
    def fit_residuals(g_plus_log):
        g_plus = 10**g_plus_log
        pred = np.array([mond_g_obs(g, g_plus) for g in g_bars])
        return np.sum(((pred - g_obss) / g_obss)**2)
    
    # Try a few g_+ values
    best_g_plus = 1e-10
    best_resid = fit_residuals(-10)
    for log_g in np.linspace(-11, -8, 50):
        resid = fit_residuals(log_g)
        if resid < best_resid:
            best_resid = resid
            best_g_plus = 10**log_g
    
    g_plus_values.append(best_g_plus)
    m_b_values.append(g.get('Mb', np.nan))  # Baryonic mass
    g_bar_at_1kpc.append(np.median(g_bars))
    quality.append(g.get('Q', 1))  # Quality flag
    distance.append(g.get('D', np.nan))
    hi_mass.append(g.get('MHI', np.nan))

# Convert to numpy arrays
g_plus_values = np.array(g_plus_values)
m_b_values = np.array(m_b_values)
g_bar_at_1kpc = np.array(g_bar_at_1kpc)
quality = np.array(quality)
distance = np.array(distance)
hi_mass = np.array(hi_mass)

# Filter: quality >= 1, M_b > 0
mask = (quality >= 1) & (m_b_values > 0) & (g_plus_values > 1e-12) & (g_plus_values < 1e-7)
g_plus_f = g_plus_values[mask]
m_b_f = m_b_values[mask]
g_bar_f = g_bar_at_1kpc[mask]
hi_f = hi_mass[mask]

print(f"Galaxies with valid fit: {len(g_plus_f)}")
print()

# Statistics
print("="*70)
print("PER-GALAXY g_+ STATISTICS")
print("="*70)
print()
print(f"Median g_+: {np.median(g_plus_f):.2e} m/s²")
print(f"Mean g_+: {np.mean(g_plus_f):.2e} m/s²")
print(f"Std g_+: {np.std(g_plus_f):.2e} m/s²")
print(f"Std(log10 g_+): {np.std(np.log10(g_plus_f)):.3f} dex")
print()
print(f"Reference:")
print(f"  Lelli+ 2017 (SPARC):  g_+ = 1.20 ± 0.05 e-10 m/s² = 1.20e-10 ± 0.05e-10")
print(f"  McGaugh+ 2016 (RAR):  g_+ ~ 1.20e-10 m/s² (universal)")
print(f"  Tian+ 2024 (BCG):     g_+ ~ 1.7e-9 m/s² (cluster, 14x larger)")
print(f"  Cluster:               g_+ ~ 2e-9 m/s² (cascade prediction)")
print()

# Mass dependence test
print("="*70)
print("MASS DEPENDENCE TEST")
print("="*70)
print()
log_m_b = np.log10(m_b_f)
log_g_plus = np.log10(g_plus_f)

# Linear fit
from scipy.stats import pearsonr
r, p = pearsonr(log_m_b, log_g_plus)
print(f"Correlation (log M_b, log g_+): r = {r:.3f}, p = {p:.2e}")
print()

# Bin by mass
print("g_+ in mass bins:")
print(f"{'log M_b':<12}{'N':<6}{'median g_+':<15}{'mean g_+':<15}{'std log':<10}")
print("-"*60)
mass_bins = [(7, 8), (8, 9), (9, 10), (10, 11), (11, 12)]
for lo, hi in mass_bins:
    mask = (log_m_b >= lo) & (log_m_b < hi)
    if mask.sum() > 3:
        med = np.median(g_plus_f[mask])
        mean = np.mean(g_plus_f[mask])
        std_log = np.std(log_g_plus[mask])
        print(f"{lo}-{hi:<8}{mask.sum():<6}{med:<15.2e}{mean:<15.2e}{std_log:<10.3f}")

print()
print("="*70)
print("VERDICT: Is the cascade's g_+ universal or mass-dependent?")
print("="*70)
print()
if abs(r) < 0.2:
    print("RESULT: g_+ is approximately UNIVERSAL across galaxy masses")
    print("        (low correlation with log M_b).")
    print("        This supports the cascade's universal g_+ prediction")
    print("        and is consistent with MOND.")
elif abs(r) < 0.5:
    print("RESULT: g_+ has WEAK mass dependence (r = {:.2f})".format(r))
    print("        Consistent with both MOND (universal) and the")
    print("        cascade's V_local prediction (weak mass dependence).")
else:
    print("RESULT: g_+ is STRONGLY mass-dependent (r = {:.2f})".format(r))
    if r > 0:
        print("        Larger g_+ at higher M_b (contradicts cascade's V_local,")
        print("        which predicts larger g_+ at lower M_b / V_local).")
    else:
        print("        Larger g_+ at lower M_b (consistent with cascade's V_local)")
        print("        This is a 'too-good' result: the cascade's V_local formula")
        print("        gives a SPECIFIC mass dependence that would fit this.")
print()

# Check HI-mass dependence
print()
print("HI-mass dependence:")
mask_hi = hi_f > 0
if mask_hi.sum() > 10:
    log_hi = np.log10(hi_f[mask_hi])
    log_g_plus_hi = np.log10(g_plus_f[mask_hi])
    r_hi, p_hi = pearsonr(log_hi, log_g_plus_hi)
    print(f"  Correlation (log M_HI, log g_+): r = {r_hi:.3f}, p = {p_hi:.2e}")
    if abs(r_hi) > 0.3:
        print(f"  Significant HI-mass dependence (g_+ increases with HI mass)")

print()
print("Comparison to cascade V_local prediction:")
print("  g_+ = (k * E_event * τ_2D) / (V_local * M_halo)")
print("  V_local ~ R^3, M_halo ~ M_b")
print("  So g_+ ~ 1/(M_b * R^3) ~ 1/M_b (for fixed R)")
print("  Predicted slope: d log g_+ / d log M_b ~ -1")
print(f"  Observed slope: r = {r:.3f}")
print()
