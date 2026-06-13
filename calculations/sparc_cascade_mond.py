#!/usr/bin/env python3
"""
Try cascade-MOND hybrid: 
g_obs = g_bar / (1 - exp(-sqrt(g_bar / g_+)))
where g_+ is set by the cascade's 2D universe gravity (mass-dependent)

In MOND: g_+ = constant (1.2e-10)
In cascade: g_+ = function of M_halo (per Tian+ 2024: g_+ = 17 * galaxy g_+ for clusters)

Test: does the cascade's mass-dependent g_+ fit real SPARC data better than
a constant g_+?
"""

import math
import numpy as np
import json
import os

SPARC_DIR = '/workspace/github-repo/supporting/data/SPARC'
M_sun = 1.989e30
kpc_to_m = 3.086e19
g_plus_galaxy = 1.2e-10

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

def evaluate(galaxy_name, galaxy_info, g_plus_func, m_l=0.5):
    data = load_data(galaxy_name)
    if data is None or len(data) < 5:
        return None
    Inc = galaxy_info['Inc']
    sin_i = math.sin(math.radians(Inc))
    
    L = galaxy_info['L'] * 1e9
    Rdisk = galaxy_info['Rdisk']
    M_disk = m_l * L * M_sun
    if galaxy_info.get('Vflat', 0) > 0:
        M_halo = galaxy_info['Vflat']**2 * 8 * Rdisk * kpc_to_m / G / M_sun
    else:
        M_halo = M_disk * 10
    
    g_plus = g_plus_func(M_halo, M_disk/M_sun)
    
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
            g_mond = mond(g_bar, g_plus)
            abs_diffs.append(abs(g_mond - g_obs) / g_obs)
    
    if len(abs_diffs) == 0:
        return None
    return np.median(abs_diffs)

# Different g_+ functional forms
cases = {
    'g_+ = 1.2e-10 (MOND constant)': lambda M_h, M_d: 1.2e-10,
    'g_+ = 1.0e-10 (best constant)': lambda M_h, M_d: 1.0e-10,
    'g_+ ∝ kappa = M_h/M_d': lambda M_h, M_d: 1.2e-10 * (M_h / M_d / 17) if M_d > 0 else 1.2e-10,
    'g_+ ∝ sqrt(kappa)': lambda M_h, M_d: 1.2e-10 * math.sqrt((M_h / M_d / 17)) if M_d > 0 else 1.2e-10,
    'g_+ = 1.2e-10 * (1 + 0.01 * log10(M_h/1e10))': lambda M_h, M_d: 1.2e-10 * (1 + 0.01 * math.log10(M_h/1e10)) if M_h > 0 else 1.2e-10,
    'g_+ = 1.2e-10 * (M_h/1e12)^0.05': lambda M_h, M_d: 1.2e-10 * (M_h/1e12)**0.05 if M_h > 0 else 1.2e-10,
    'g_+ = 1.2e-10 * (M_h/1e12)^0.1': lambda M_h, M_d: 1.2e-10 * (M_h/1e12)**0.1 if M_h > 0 else 1.2e-10,
    'g_+ = 1.2e-10 * (M_h/1e12)^0.2': lambda M_h, M_d: 1.2e-10 * (M_h/1e12)**0.2 if M_h > 0 else 1.2e-10,
}

# Evaluate
G = 6.674e-11

good_galaxies = [g for g in galaxies if g['Q'] <= 2 and g['Inc'] > 30 and g['L'] > 0]
print(f"Testing cascade-MOND hybrids on {len(good_galaxies)} SPARC galaxies")
print()
print(f"  {'g_+ form':<55s}  {'median':>8s}  {'within 20%':>12s}")
print()

for name, g_func in cases.items():
    resids = []
    for g in good_galaxies:
        # Compute M_halo
        L = g['L'] * 1e9
        Rdisk = g['Rdisk']
        M_disk = 0.5 * L * M_sun
        if g.get('Vflat', 0) > 0:
            M_halo = g['Vflat']**2 * 8 * Rdisk * kpc_to_m / G / M_sun
        else:
            M_halo = M_disk * 10
        
        r = evaluate(g['name'], g, g_func)
        if r is not None:
            resids.append(r)
    
    if len(resids) > 0:
        med = np.median(resids)
        within_20 = sum(1 for r in resids if r < 0.20) / len(resids) * 100
        print(f"  {name:<55s}  {med:>8.2%}  {within_20:>11.1f}%")
