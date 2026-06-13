#!/usr/bin/env python3
"""
Test: does the per-galaxy g_+ variation come from M/L ratio variations?

If M/L is wrong for some galaxies, g_bar is wrong, and the inferred g_+ is wrong.
Lelli+ 2016 use M/L = 0.5 with scatter.
"""

import math
import numpy as np
import json
import os

SPARC_DIR = '/workspace/github-repo/supporting/data/SPARC'
M_sun = 1.989e30
kpc_to_m = 3.086e19
G = 6.674e-11

def mond(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

with open(os.path.join(SPARC_DIR, 'galaxies_sample.json'), 'r') as f:
    galaxies = json.load(f)
with open(os.path.join(SPARC_DIR, 'mond_fit_results.json'), 'r') as f:
    mond_results = json.load(f)

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

def fit_galaxy_ml(galaxy_name, galaxy_info, ml_value):
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
        vbar_sq = ml_value * d['vdisk']**2 + d['vgas']**2 + d['vbul']**2
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
    
    best_g_plus = None
    best_err = float('inf')
    for log_gp in np.linspace(-13, -8, 100):
        g_plus = 10**log_gp
        preds = np.array([mond(gb, g_plus) for gb in gbars])
        with np.errstate(divide='ignore', invalid='ignore'):
            log_resid = np.log10(preds / gobs)
        log_resid = log_resid[np.isfinite(log_resid)]
        if len(log_resid) > 0:
            err = np.mean(log_resid**2)
            if err < best_err:
                best_err = err
                best_g_plus = g_plus
    
    return best_g_plus, math.log10(best_g_plus) if best_g_plus else None

# Test how g_+ varies with M/L
print("=" * 80)
print("M/L RATIO SENSITIVITY")
print("=" * 80)
print()

ml_values = [0.3, 0.4, 0.5, 0.6, 0.7, 1.0]

# Test on a few galaxies
test_galaxies = ['NGC6503', 'DDO154', 'NGC2403', 'UGC1281', 'CamB', 'NGC3741']

print(f"  {'Galaxy':<12s}", end='')
for ml in ml_values:
    print(f"  {'M/L='+str(ml):>10s}", end='')
print()
print()

for g_name in test_galaxies:
    g_info = [g for g in galaxies if g['name'] == g_name][0]
    print(f"  {g_name:<12s}", end='')
    for ml in ml_values:
        result = fit_galaxy_ml(g_name, g_info, ml)
        if result is None:
            print(f"  {'N/A':>10s}", end='')
        else:
            g_plus, log_gp = result
            print(f"  {g_plus:>10.2e}", end='')
    print()

# Key question: if I fix M/L = 0.5 but vary it per galaxy to find best fit,
# does the per-galaxy g_+ scatter reduce?

print()
print("=" * 80)
print("FREE M/L vs FIXED M/L COMPARISON")
print("=" * 80)
print()

# For each galaxy, find best (M/L, g_+) pair
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
                    best = (ml, g_plus, np.median(np.abs(np.array([mond(gb, g_plus) for gb in gbars]) - gobs[:len(gbars)]) / gobs[:len(gbars)]))
    
    return best

# Test on a few galaxies
print(f"  {'Galaxy':<12s}  {'best M/L':>10s}  {'best g_+':>12s}  {'median resid':>14s}")
print()
for g_name in ['NGC6503', 'DDO154', 'NGC2403', 'UGC1281', 'CamB', 'NGC3741', 'NGC6946', 'NGC891']:
    g_info = [g for g in galaxies if g['name'] == g_name][0]
    result = fit_joint(g_name, g_info)
    if result is not None:
        ml, g_plus, resid = result
        print(f"  {g_name:<12s}  {ml:>10.2f}  {g_plus:>12.2e}  {resid:>13.2%}")
