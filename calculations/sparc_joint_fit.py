#!/usr/bin/env python3
"""
Joint fit of (M/L, g_+) on real SPARC data.
Tests if the per-galaxy g_+ variation is just M/L noise.


**HISTORICAL (v2.x era, mid-2025)**: This file is from the v2.x era, predating:
- v3.0+ Lagrangian work (L102-L136)
- v3.1+ Multi-universe picture (L142-L150)
- v3.3 Bilateral cascade (E_4D = 5e79 J, M_Pl,4D = 3.93e23 GeV)
- v3.5.7+ Naming revolution (f_back -> f_DE, f_DM,leak, f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N*v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via alpha-GM, L308v)
- alpha = 1.289 (FIRST-PRINCIPLES via L308n)
- eps = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- gamma_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- tau_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v2.x era framework, not v3.5.9+ A2.

"""

import math
import numpy as np
import json
import os

SPARC_DIR = '/workspace/github-repo/supporting/data/SPARC'
M_sun = 1.989e30
kpc_to_m = 3.086e19

def mond(g_bar, g_plus):
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

def fit_joint(galaxy_name, galaxy_info):
    data = load_data(galaxy_name)
    if data is None or len(data) < 5:
        return None
    Inc = galaxy_info['Inc']
    sin_i = math.sin(math.radians(Inc))
    
    gbars_by_ml = {}
    gobs = []
    for d in data:
        r = d['r']
        if r <= 0 or sin_i <= 0:
            continue
        r_m = r * kpc_to_m
        vobs = d['vobs']**2 * 1e6 / r_m
        if vobs > 0:
            gobs.append(vobs)
        for ml in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0]:
            vbar_sq = ml * d['vdisk']**2 + d['vgas']**2 + d['vbul']**2
            if vbar_sq > 0:
                g_bar = vbar_sq * 1e6 / r_m
                gbars_by_ml.setdefault(ml, []).append(g_bar)
    
    if not gbars_by_ml:
        return None
    
    gobs = np.array(gobs)
    
    best = None
    best_err = float('inf')
    for ml, gbars in gbars_by_ml.items():
        gbars = np.array(gbars)
        for log_gp in np.linspace(-12, -8, 50):
            g_plus = 10**log_gp
            preds = np.array([mond(gb, g_plus) for gb in gbars])
            with np.errstate(divide='ignore', invalid='ignore'):
                log_resid = np.log10(preds / gobs[:len(gbars)])
            log_resid = log_resid[np.isfinite(log_resid)]
            if len(log_resid) > 0:
                err = np.mean(log_resid**2)
                if err < best_err:
                    best_err = err
                    abs_diff = np.abs(preds - gobs[:len(gbars)]) / gobs[:len(gbars)]
                    best = (ml, g_plus, np.median(abs_diff))
    
    return best

# Run on all good galaxies
good_galaxies = [g for g in galaxies if g['Q'] <= 2 and g['Inc'] > 30 and g['L'] > 0]
print(f"Joint (M/L, g_+) fit on {len(good_galaxies)} SPARC galaxies")
print()

results = []
for g in good_galaxies:
    r = fit_joint(g['name'], g)
    if r is not None:
        ml, g_plus, resid = r
        results.append({
            'name': g['name'],
            'L': g['L'],
            'Vflat': g.get('Vflat', 0),
            'ml': ml, 'g_plus': g_plus,
            'resid': resid
        })

mls = np.array([r['ml'] for r in results])
gps = np.array([r['g_plus'] for r in results])
resids = np.array([r['resid'] for r in results])

print(f"  Galaxies fit: {len(results)}")
print()
print(f"  Best M/L distribution:")
print(f"    median: {np.median(mls):.2f}")
print(f"    mean: {np.mean(mls):.2f}")
print(f"    std: {np.std(mls):.2f}")
print()
print(f"  Best g_+ distribution:")
print(f"    median: {np.median(gps):.2e}")
print(f"    mean: {np.mean(gps):.2e}")
print(f"    std: {np.std(np.log10(gps)):.2f} dex")
print()
print(f"  Residual distribution:")
print(f"    median: {np.median(resids):.2%}")
print(f"    within 5%: {sum(1 for r in resids if r < 0.05) / len(resids) * 100:.1f}%")
print(f"    within 10%: {sum(1 for r in resids if r < 0.10) / len(resids) * 100:.1f}%")
print(f"    within 20%: {sum(1 for r in resids if r < 0.20) / len(resids) * 100:.1f}%")
print()
print(f"  Correlation: M/L vs log(g_+): {np.corrcoef(mls, np.log10(gps))[0, 1]:+.3f}")
print()

# Compare to fixed M/L = 0.5
fixed_ml_resids = []
for g in good_galaxies:
    fname = os.path.join(SPARC_DIR, f"{g['name']}_mond_fixed.json")
    # Skip if not computed
    pass

# Save
with open(os.path.join(SPARC_DIR, 'joint_ml_gplus_fit.json'), 'w') as f:
    json.dump(results, f, indent=2)
print(f"Saved {len(results)} results")
print()

# Best galaxies
print("Top 20 best fits (joint M/L, g_+):")
for r in sorted(results, key=lambda x: x['resid'])[:20]:
    print(f"  {r['name']:<12s} L={r['L']:>6.2f} Vflat={r['Vflat']:>5.1f} M/L={r['ml']:.2f} g_+={r['g_plus']:.2e} resid={r['resid']:.2%}")
