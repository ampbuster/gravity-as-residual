#!/usr/bin/env python3
"""
Test the cascade's RAR prediction on REAL SPARC data (175 galaxies).
"""

import math
import numpy as np
import json
import os
import sys

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
g_plus_galaxy = 1.2e-10

def rar(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

# Get the directory where the SPARC data is
SPARC_DIR = '/workspace/github-repo/supporting/data/SPARC'

# Load sample
with open(os.path.join(SPARC_DIR, 'galaxies_sample.json'), 'r') as f:
    galaxies = json.load(f)

def g_DM_iso(r_kpc, M_halo_Msun, R_halo_kpc, f_active, r_core_frac, scale):
    M_cum_total_kg = scale * (1 - f_active) * M_halo_Msun * M_sun
    r_core_m = r_core_frac * R_halo_kpc * kpc_to_m
    r_m = r_kpc * kpc_to_m
    R_halo_m = R_halo_kpc * kpc_to_m
    V_eff = 4 * math.pi * r_core_m**2 * (R_halo_m - 2 * r_core_m / 3)
    rho_0 = M_cum_total_kg / V_eff if V_eff > 0 else 0
    if r_m < r_core_m:
        M_cum_enclosed = (4/3) * math.pi * r_m**3 * rho_0
    else:
        M_core = (4/3) * math.pi * r_core_m**3 * rho_0
        M_cum_enclosed = M_core + 4 * math.pi * rho_0 * r_core_m**2 * (r_m - r_core_m)
    return G * M_cum_enclosed / r_m**2 if r_m > 0 else 0

def g_active(r_kpc, M_disk_Msun, R_disk_kpc, M_halo_Msun, f_active):
    r_m = r_kpc * kpc_to_m
    R_d = R_disk_kpc * kpc_to_m
    kappa = M_halo_Msun / M_disk_Msun if M_disk_Msun > 0 else 0
    M_stellar_enclosed = M_disk_Msun * M_sun * (1 - (1 + r_m/R_d) * math.exp(-r_m/R_d))
    return G * f_active * kappa * M_stellar_enclosed / r_m**2 if r_m > 0 else 0

def fit_galaxy(galaxy_name, galaxy_info, m_l=0.5, f_active=0.05, r_core_frac=0.25, scale=0.15):
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
                    r = float(parts[0])
                    vobs = float(parts[1])
                    vgas = float(parts[3])
                    vdisk = float(parts[4])
                    vbul = float(parts[5])
                    data.append({'r': r, 'vobs': vobs, 'vgas': vgas, 'vdisk': vdisk, 'vbul': vbul})
                except (ValueError, IndexError):
                    continue
    
    if len(data) == 0:
        return None
    
    L = galaxy_info['L'] * 1e9
    Rdisk = galaxy_info['Rdisk']
    R_halo = 8 * Rdisk
    M_disk = m_l * L * M_sun
    
    if galaxy_info.get('Vflat', 0) > 0:
        M_halo = galaxy_info['Vflat']**2 * R_halo * kpc_to_m / G / M_sun
    else:
        M_halo = data[-1]['vobs']**2 * R_halo * kpc_to_m / G / M_sun
    
    residuals = []
    for d in data:
        r = d['r']
        if r <= 0:
            continue
        r_m = r * kpc_to_m
        vbar_sq = m_l * d['vdisk']**2 + d['vgas']**2 + d['vbul']**2
        if vbar_sq <= 0:
            continue
        g_bar = vbar_sq * 1e6 / r_m
        g_obs = d['vobs']**2 * 1e6 / r_m
        g_cum = g_DM_iso(r, M_halo, R_halo, f_active, r_core_frac, scale)
        g_act = g_active(r, M_disk/M_sun, Rdisk, M_halo, f_active)
        g_cascade = g_bar + g_cum + g_act
        g_rar = rar(g_bar, g_plus_galaxy)
        if g_rar > 0:
            resid = (g_cascade - g_rar) / g_rar
            residuals.append(abs(resid))
    
    if len(residuals) == 0:
        return None
    return np.median(residuals), len(residuals)

# Main
good_galaxies = [g for g in galaxies if g['Q'] <= 2 and g['Inc'] > 30 and g['L'] > 0]
print(f"Testing {len(good_galaxies)} SPARC galaxies (Q<=2, Inc>30, L>0)")
print("Using cascade params: f_active=0.05, r_core_frac=0.25, scale=0.15 (MW-tuned)")
print()

results = []
for g in good_galaxies:
    result = fit_galaxy(g['name'], g)
    if result is None:
        continue
    resid, n = result
    if resid > 5:
        continue
    results.append((g['name'], g['Q'], g['L'], g['Rdisk'], g.get('Vflat', 0), resid, n))

if results:
    all_resids = [r[5] for r in results]
    print("=" * 80)
    print("SUMMARY on REAL SPARC DATA")
    print("=" * 80)
    print()
    print(f"  Galaxies fit: {len(results)}")
    print(f"  Median abs residual: {np.median(all_resids):.3f}")
    print(f"  Mean abs residual:   {np.mean(all_resids):.3f}")
    print(f"  Min residual:        {min(all_resids):.3f}")
    print(f"  Max residual:        {max(all_resids):.3f}")
    print(f"  Within 20%:          {sum(1 for r in all_resids if r < 0.2) / len(all_resids) * 100:.1f}%")
    print(f"  Within 30%:          {sum(1 for r in all_resids if r < 0.3) / len(all_resids) * 100:.1f}%")
    print(f"  Within 50%:          {sum(1 for r in all_resids if r < 0.5) / len(all_resids) * 100:.1f}%")
    
    # Save for later analysis
    with open('/workspace/github-repo/supporting/data/SPARC/sparc_cascade_results.json', 'w') as f:
        json.dump([{
            'name': r[0], 'Q': r[1], 'L': r[2], 'Rdisk': r[3], 'Vflat': r[4],
            'resid': r[5], 'n': r[6]
        } for r in results], f, indent=2)
    print()
    print("Top 10 worst fits:")
    for r in sorted(results, key=lambda x: -x[5])[:10]:
        print(f"  {r[0]:<12s} Q={r[1]} L={r[2]:.3f} Rdisk={r[3]:.2f} resid={r[5]:.2%}")
    print()
    print("Top 10 best fits:")
    for r in sorted(results, key=lambda x: x[5])[:10]:
        print(f"  {r[0]:<12s} Q={r[1]} L={r[2]:.3f} Rdisk={r[3]:.2f} resid={r[5]:.2%}")
