#!/usr/bin/env python3
"""
Fix g_+ to a constant (MOND's value) and see how well it fits the SPARC population.
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

with open(os.path.join(SPARC_DIR, 'mond_fit_results.json'), 'r') as f:
    mond_results = json.load(f)

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

def evaluate(galaxy_name, g_plus_const, m_l=0.5):
    data = load_data(galaxy_name)
    if data is None or len(data) < 5:
        return None
    Inc = [g for g in galaxies if g['name'] == galaxy_name][0]['Inc']
    sin_i = math.sin(math.radians(Inc))
    
    abs_diffs = []
    for d in data:
        r = d['r']
        if r <= 0 or sin_i <= 0:
            continue
        r_m = r * kpc_to_m
        vbar_sq = m_l * d['vdisk']**2 + d['vgas']**2 + d['vbul']**2
        if vbar_sq <= 0:
            continue
        g_bar = vbar_sq * 1e6 / r_m
        g_obs = d['vobs']**2 * 1e6 / r_m
        if g_bar > 0 and g_obs > 0:
            g_mond = mond(g_bar, g_plus_const)
            abs_diffs.append(abs(g_mond - g_obs) / g_obs)
    
    if len(abs_diffs) == 0:
        return None
    return np.median(abs_diffs)

# Test different fixed g_+ values
test_gps = [1e-11, 3e-11, 6e-11, 1e-10, 1.2e-10, 1.5e-10, 2e-10, 3e-10]

print("=" * 80)
print("FIXED g_+ VALUES ON REAL SPARC")
print("=" * 80)
print()
print(f"  {'g_+ (m/s^2)':>14s}  {'median resid':>14s}  {'within 10%':>12s}  {'within 20%':>12s}")
print()

for g_plus in test_gps:
    resids = []
    for r in mond_results:
        rr = evaluate(r['name'], g_plus)
        if rr is not None:
            resids.append(rr)
    
    if len(resids) > 0:
        med = np.median(resids)
        within_10 = sum(1 for r in resids if r < 0.10) / len(resids) * 100
        within_20 = sum(1 for r in resids if r < 0.20) / len(resids) * 100
        print(f"  {g_plus:>14.2e}  {med:>14.2%}  {within_10:>11.1f}%  {within_20:>11.1f}%")
