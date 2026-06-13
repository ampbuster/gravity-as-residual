#!/usr/bin/env python3
"""
Test the cascade's RAR prediction on real SPARC galaxies.
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

# Load sample table
with open('galaxies_sample.json', 'r') as f:
    galaxies = json.load(f)

print(f"Loaded {len(galaxies)} galaxies from sample table")
print()

# Test on a few galaxies
# M_disk_Lelli16 uses L[3.6] * 0.5 (Lelli+ 2016 mass-to-light ratio)
# Or M_disk = L[3.6] * 0.5 * (1e9 L_sun) * M_sun_per_L_sun

def load_rotmod(galaxy_name):
    """Load rotation curve data for a galaxy"""
    fname = f"{galaxy_name}_rotmod.dat"
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
                    r = float(parts[0])  # kpc
                    vobs = float(parts[1])  # km/s
                    vgas = float(parts[3])  # km/s
                    vdisk = float(parts[4])  # km/s
                    vbul = float(parts[5])  # km/s
                    data.append({
                        'r': r, 'vobs': vobs, 'vgas': vgas, 'vdisk': vdisk, 'vbul': vbul
                    })
                except (ValueError, IndexError):
                    continue
    return data

def compute_gbar_gobs(galaxy, data, m_l=0.5):
    """Compute g_bar and g_obs from rotation curve data.
    SPARC gives vgas, vdisk, vbul in km/s. These are the contributions
    to the rotation curve. vobs is the total observed velocity.
    
    g_bar = vbar^2 / r (with inclination correction)
    g_obs = vobs^2 / r
    
    The inclination is in galaxy['Inc'] in degrees.
    We assume cos(i) correction.
    """
    results = []
    Inc = galaxy['Inc']
    sin_i = math.sin(math.radians(Inc))
    
    for d in data:
        r_kpc = d['r']
        if r_kpc <= 0 or sin_i <= 0:
            continue
        # vbar (in km/s) from squared sum
        vbar_sq = m_l * d['vdisk']**2 + d['vgas']**2 + d['vbul']**2
        vobs = d['vobs']
        r_m = r_kpc * kpc_to_m
        # Convert to m/s, then g = v^2/r
        g_bar = (math.sqrt(vbar_sq) * 1000)**2 / r_m
        g_obs = (vobs * 1000)**2 / r_m
        if g_bar > 0 and g_obs > 0:
            results.append((g_bar, g_obs, r_kpc))
    return results

# Test on Milky Way analog (NGC 2403, NGC 3198, etc.)
test_galaxies = ['NGC2403', 'NGC3198', 'NGC6503', 'NGC3741', 'DDO154', 'DDO168', 'UGC1281', 'CamB']

print("Testing cascade's RAR on real SPARC galaxies...")
print("=" * 80)
print()

all_data = []
for g_name in test_galaxies:
    # Find galaxy in sample
    g_info = None
    for g in galaxies:
        if g['name'] == g_name:
            g_info = g
            break
    if g_info is None:
        print(f"{g_name}: not found in sample")
        continue
    
    data = load_rotmod(g_name)
    if data is None or len(data) == 0:
        print(f"{g_name}: no rotation curve data")
        continue
    
    gbar_gobs = compute_gbar_gobs(g_info, data)
    if len(gbar_gobs) == 0:
        print(f"{g_name}: no valid data points")
        continue
    
    print(f"{g_name}: D={g_info['D']:.2f} Mpc, L={g_info['L']:.3f} L_sun, Rdisk={g_info['Rdisk']:.2f} kpc, Q={g_info['Q']}")
    print(f"  Data points: {len(gbar_gobs)}")
    print(f"  g_bar range: {min(p[0] for p in gbar_gobs):.2e} to {max(p[0] for p in gbar_gobs):.2e}")
    print(f"  g_obs range: {min(p[1] for p in gbar_gobs):.2e} to {max(p[1] for p in gbar_gobs):.2e}")
    
    # Check RAR fit: log(g_obs) vs log(g_bar)
    # The empirical RAR: g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_+)))
    # We just want to see if data points fall on this curve
    print(f"  RAR (g_+={g_plus_galaxy:.1e}):")
    for gbar, gobs, r in gbar_gobs[:5]:
        gobs_rar = rar(gbar, g_plus_galaxy)
        diff = (gobs - gobs_rar) / gobs_rar
        print(f"    r={r:.2f} kpc: g_bar={gbar:.2e}, g_obs={gobs:.2e}, RAR={gobs_rar:.2e}, diff={diff:+.2%}")
    
    all_data.append((g_name, gbar_gobs))
    print()

# Combined plot would be next
# Save combined data
combined = []
for g_name, gbar_gobs in all_data:
    for gbar, gobs, r in gbar_gobs:
        combined.append({'galaxy': g_name, 'g_bar': gbar, 'g_obs': gobs, 'r': r})

with open('sparc_rar_data.json', 'w') as f:
    json.dump(combined, f, indent=2)
print(f"Saved {len(combined)} data points to sparc_rar_data.json")
