#!/usr/bin/env python3
"""
Per-galaxy fit of cascade's RAR to real SPARC data.
Find the best (f_active, r_core_frac, scale) for each galaxy.
"""

import math
import numpy as np
import json
import os

G = 6.674e-11
M_sun = 1.989e30
kpc_to_m = 3.086e19
g_plus_galaxy = 1.2e-10

def rar(g_bar, g_plus):
    if g_bar <= 0 or g_plus <= 0:
        return g_bar
    x = math.sqrt(g_bar / g_plus)
    return g_bar / (1 - math.exp(-x))

SPARC_DIR = '/workspace/github-repo/supporting/data/SPARC'
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

def fit_galaxy(galaxy_name, galaxy_info, m_l=0.5):
    fname = os.path.join(SPARC_DIR, f"{galaxy_name}_rotmod.dat")
    if not os.path.exists(fname):
        return None, None
    
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
    
    if len(data) < 5:
        return None, None
    
    L = galaxy_info['L'] * 1e9
    Rdisk = galaxy_info['Rdisk']
    R_halo = 8 * Rdisk
    M_disk = m_l * L * M_sun
    
    if galaxy_info.get('Vflat', 0) > 0:
        M_halo = galaxy_info['Vflat']**2 * R_halo * kpc_to_m / G / M_sun
    else:
        M_halo = data[-1]['vobs']**2 * R_halo * kpc_to_m / G / M_sun
    
    # Pre-compute g_bar and g_obs
    gbars = []
    gobs = []
    rs = []
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
        if g_bar > 0 and g_obs > 0:
            gbars.append(g_bar)
            gobs.append(g_obs)
            rs.append(r)
    
    if len(gbars) < 5:
        return None, None
    
    gbars = np.array(gbars)
    gobs = np.array(gobs)
    rs = np.array(rs)
    
    # Grid search for best params
    best = None
    best_err = float('inf')
    for f_active in [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2]:
        for r_core_frac in [0.05, 0.1, 0.2, 0.3, 0.5]:
            for scale in [0.01, 0.05, 0.1, 0.2, 0.5, 1.0]:
                preds = []
                for i, r in enumerate(rs):
                    g_cum = g_DM_iso(r, M_halo, R_halo, f_active, r_core_frac, scale)
                    g_act = g_active(r, M_disk/M_sun, Rdisk, M_halo, f_active)
                    g_cas = gbars[i] + g_cum + g_act
                    preds.append(g_cas)
                preds = np.array(preds)
                # Minimize log residual
                log_resid = np.log10(preds / gobs)
                err = np.mean(log_resid**2)
                if err < best_err:
                    best_err = err
                    best = (f_active, r_core_frac, scale, np.median(np.abs(log_resid)))
    
    return best, galaxy_info

# Fit per galaxy
print("Per-galaxy fit on real SPARC data...")
print()

good_galaxies = [g for g in galaxies if g['Q'] <= 2 and g['Inc'] > 30 and g['L'] > 0]
print(f"Fitting {len(good_galaxies)} galaxies (Q<=2, Inc>30, L>0)")
print()

best_params = []
for g in good_galaxies[:50]:  # First 50 for speed
    best, info = fit_galaxy(g['name'], g)
    if best is None:
        continue
    f_active, r_core_frac, scale, resid = best
    best_params.append({
        'name': g['name'],
        'L': g['L'], 'Rdisk': g['Rdisk'], 'Vflat': g.get('Vflat', 0),
        'f_active': f_active, 'r_core_frac': r_core_frac, 'scale': scale,
        'resid': resid
    })

# Show best-fit parameters
print("Best-fit cascade params for each galaxy (first 50):")
print()
print(f"  {'Galaxy':<12s}  {'L':>7s}  {'Rdisk':>6s}  {'Vflat':>6s}  {'f_active':>9s}  {'r_core':>7s}  {'scale':>5s}  {'resid':>7s}")
print()
for p in best_params:
    print(f"  {p['name']:<12s}  {p['L']:>7.2f}  {p['Rdisk']:>6.2f}  {p['Vflat']:>6.1f}  {p['f_active']:>9.4f}  {p['r_core_frac']:>7.2f}  {p['scale']:>5.2f}  {p['resid']:>7.2%}")

print()
print("=" * 80)
print("PARAMETER CORRELATIONS WITH GALAXY MASS")
print("=" * 80)
print()

if best_params:
    L_arr = np.array([p['L'] for p in best_params])
    fa_arr = np.array([p['f_active'] for p in best_params])
    rc_arr = np.array([p['r_core_frac'] for p in best_params])
    sc_arr = np.array([p['scale'] for p in best_params])
    res_arr = np.array([p['resid'] for p in best_params])
    
    log_L = np.log10(L_arr)
    
    def corr(x, y):
        return np.corrcoef(x, y)[0, 1]
    
    print(f"  Correlation of f_active vs log(L): {corr(log_L, fa_arr):+.3f}")
    print(f"  Correlation of r_core_frac vs log(L): {corr(log_L, rc_arr):+.3f}")
    print(f"  Correlation of scale vs log(L): {corr(log_L, sc_arr):+.3f}")
    print(f"  Correlation of residual vs log(L): {corr(log_L, res_arr):+.3f}")
    print()
    
    # Average best params by mass bin
    print("Average best params by L bin:")
    L_min, L_max = np.min(log_L), np.max(log_L)
    L_bins = np.linspace(L_min, L_max, 4)
    for i in range(len(L_bins)-1):
        in_bin = (log_L >= L_bins[i]) & (log_L < L_bins[i+1])
        if sum(in_bin) == 0:
            continue
        print(f"  L=[{10**L_bins[i]:.2f}, {10**L_bins[i+1]:.2f}]: <f_active>={np.mean(fa_arr[in_bin]):.4f}, <r_core>={np.mean(rc_arr[in_bin]):.3f}, <scale>={np.mean(sc_arr[in_bin]):.3f}, <resid>={np.mean(res_arr[in_bin]):.2%}")
    
    # Save
    with open(os.path.join(SPARC_DIR, 'sparc_per_galaxy_params.json'), 'w') as f:
        json.dump(best_params, f, indent=2)
    print()
    print(f"Saved {len(best_params)} per-galaxy fits")
