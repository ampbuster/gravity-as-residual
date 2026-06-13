#!/usr/bin/env python3
"""
Test MOND-like interpolation on real SPARC data.
Find best g_+ for each galaxy.
"""

import math
import numpy as np
import json
import os

SPARC_DIR = '/workspace/github-repo/supporting/data/SPARC'
M_sun = 1.989e30
kpc_to_m = 3.086e19

def mond(g_bar, g_plus):
    """MOND-like interpolation function"""
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

with open(os.path.join(SPARC_DIR, 'galaxies_sample.json'), 'r') as f:
    galaxies = json.load(f)

def load_data(galaxy_name):
    fname = os.path.join(SPARC_DIR, f"{galaxy_name}_rotmod.dat")
    if not os.path.exists(fname):
        return None
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
                        'vgas': float(parts[3]),
                        'vdisk': float(parts[4]),
                        'vbul': float(parts[5]),
                    })
                except (ValueError, IndexError):
                    continue
    return data

def fit_galaxy(galaxy_name, galaxy_info, m_l=0.5):
    data = load_data(galaxy_name)
    if data is None or len(data) < 5:
        return None
    
    Inc = galaxy_info['Inc']
    sin_i = math.sin(math.radians(Inc))
    
    gbars = []
    gobs = []
    for d in data:
        r = d['r']
        if r <= 0 or sin_i <= 0:
            continue
        r_m = r * kpc_to_m
        # vbar^2 (without inclination since SPARC gives v in plane)
        vbar_sq = m_l * d['vdisk']**2 + d['vgas']**2 + d['vbul']**2
        if vbar_sq <= 0:
            continue
        g_bar = vbar_sq * 1e6 / r_m
        g_obs = d['vobs']**2 * 1e6 / r_m
        if g_bar > 0 and g_obs > 0:
            gbars.append(g_bar)
            gobs.append(g_obs)
    
    if len(gbars) < 5:
        return None
    
    gbars = np.array(gbars)
    gobs = np.array(gobs)
    
    # Fit g_+: find g_plus that minimizes |log(g_obs / MOND(g_bar, g_plus))|^2
    best_g_plus = None
    best_err = float('inf')
    for log_gp in np.linspace(-13, -8, 100):
        g_plus = 10**log_gp
        preds = np.array([mond(gb, g_plus) for gb in gbars])
        # log residual
        with np.errstate(divide='ignore', invalid='ignore'):
            log_resid = np.log10(preds / gobs)
        log_resid = log_resid[np.isfinite(log_resid)]
        if len(log_resid) > 0:
            err = np.mean(log_resid**2)
            if err < best_err:
                best_err = err
                best_g_plus = g_plus
    
    if best_g_plus is None:
        return None
    
    # Compute residual with best g_plus
    preds = np.array([mond(gb, best_g_plus) for gb in gbars])
    abs_diff = np.abs(preds - gobs) / gobs
    median_resid = np.median(abs_diff)
    
    return {
        'name': galaxy_name,
        'L': galaxy_info['L'],
        'Vflat': galaxy_info.get('Vflat', 0),
        'g_plus': best_g_plus,
        'log_g_plus': math.log10(best_g_plus),
        'median_resid': median_resid,
        'n_points': len(gbars),
    }

# Fit all good galaxies
good_galaxies = [g for g in galaxies if g['Q'] <= 2 and g['Inc'] > 30 and g['L'] > 0]
print(f"Fitting MOND interpolation to {len(good_galaxies)} SPARC galaxies")
print()

results = []
for g in good_galaxies:
    r = fit_galaxy(g['name'], g)
    if r is None:
        continue
    results.append(r)

print(f"Successfully fit {len(results)} galaxies")
print()

# Distribution of best-fit g_+
log_gps = np.array([r['log_g_plus'] for r in results])
Ls = np.array([r['L'] for r in results])
Vflats = np.array([r['Vflat'] for r in results])
resids = np.array([r['median_resid'] for r in results])

print("=" * 80)
print("MOND FIT RESULTS")
print("=" * 80)
print()
print(f"  log10(g_+) distribution:")
print(f"    mean: {np.mean(log_gps):+.2f}")
print(f"    median: {np.median(log_gps):+.2f}")
print(f"    std: {np.std(log_gps):.2f}")
print(f"    min: {np.min(log_gps):+.2f}")
print(f"    max: {np.max(log_gps):+.2f}")
print()
print(f"  g_+ in physical units: median = {10**np.median(log_gps):.2e} m/s^2")
print(f"  MOND predicts g_+ = 1.2e-10 (McGaugh+ 2016)")
print()
print(f"  Median residual distribution:")
print(f"    mean: {np.mean(resids):.2%}")
print(f"    median: {np.median(resids):.2%}")
print(f"    within 5%: {sum(1 for r in resids if r < 0.05) / len(resids) * 100:.1f}%")
print(f"    within 10%: {sum(1 for r in resids if r < 0.10) / len(resids) * 100:.1f}%")
print(f"    within 20%: {sum(1 for r in resids if r < 0.20) / len(resids) * 100:.1f}%")
print()

# Correlation of g_+ with galaxy properties
def correlation(x, y):
    return np.corrcoef(x, y)[0, 1]

print("Correlations:")
print(f"  log(g_+) vs log(L): {correlation(np.log10(Ls+1), log_gps):+.3f}")
print(f"  log(g_+) vs Vflat:  {correlation(np.log10(Vflats+1), log_gps):+.3f}")
print()

# Best fit galaxies
print("Top 20 best fits:")
for r in sorted(results, key=lambda x: x['median_resid'])[:20]:
    print(f"  {r['name']:<12s} L={r['L']:>6.2f} Vflat={r['Vflat']:>5.1f} g_+={r['g_plus']:.2e} resid={r['median_resid']:.2%}")

print()
print("Top 20 worst fits:")
for r in sorted(results, key=lambda x: -x['median_resid'])[:20]:
    print(f"  {r['name']:<12s} L={r['L']:>6.2f} Vflat={r['Vflat']:>5.1f} g_+={r['g_plus']:.2e} resid={r['median_resid']:.2%}")

# Save
with open(os.path.join(SPARC_DIR, 'mond_fit_results.json'), 'w') as f:
    json.dump(results, f, indent=2)
print()
print(f"Saved {len(results)} results")
