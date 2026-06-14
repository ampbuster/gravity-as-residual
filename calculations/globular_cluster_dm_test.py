#!/usr/bin/env python3
"""
Globular Cluster Dark Matter Null Test (Test 2)

Cascade prediction: GCs should have ZERO dark matter because they are
old stellar systems with no high-energy events above E_crit. All GCs
should have M/L ratio consistent with a pure stellar population
(M/L_V ~ 1-3 for old metal-poor populations).

Standard prediction: GCs may have DM (especially massive GCs at large
Galactocentric distance), or may not (they're often assumed to be
"baryonic-only" benchmarks).

Data sources:
- Harris 1996 catalog (146 GCs, V magnitudes, distances)
- Usher+ 2013 catalog (143 GCs, velocity dispersions, distances)
- Cross-matched to compute M_dyn / L ratio

Result: Test the cascade's prediction that GCs are DM-free.
"""

import numpy as np
import math
from astroquery.vizier import Vizier
from astropy.io.votable import parse_single_table
from astropy.table import Table, join
import io

# Constants
G = 6.674e-11  # m^3 / (kg s^2)
M_sun = 1.989e30  # kg
kpc_to_m = 3.086e19
km_s_to_m_s = 1000
M_sun_V = 4.83  # absolute V magnitude of Sun

Vizier.ROW_LIMIT = -1

print("="*60)
print("Globular Cluster Dark Matter Null Test")
print("Cascade prediction: M/L_V ~ 1-3 (no DM)")
print("="*60)

# 1. Get Harris 1996 catalog (basic GC properties)
print("\n1. Downloading Harris 1996 catalog (146 GCs)...")
result = Vizier.get_catalogs_async("VII/195")
harris = parse_single_table(io.BytesIO(result.content)).to_table()
print(f"   Got {len(harris)} GCs")

# 2. Get Usher+ 2013 catalog (velocity dispersions)
print("\n2. Downloading Usher+ 2013 catalog (143 GCs with sigma)...")
result = Vizier.get_catalogs_async("J/ApJ/766/136")
usher = parse_single_table(io.BytesIO(result.content)).to_table()
print(f"   Got {len(usher)} GCs")

# 3. Normalize names for cross-matching
harris['Name'] = [str(n).lower().replace(' ', '').replace('m', 'm') for n in harris['ID']]
usher['Name'] = [str(n).lower().strip() for n in usher['Name']]

# 4. Cross-match
harris_sub = harris[['Name', 'Rsun', 'Vt', '__Fe_H_', 'c', 'Rgc']]
joined = join(usher, harris_sub, keys='Name', join_type='inner')
print(f"   Cross-matched: {len(joined)} GCs")

# 5. Compute M_dyn for each GC
# M_dyn ≈ k * sigma^2 * r_h / G (Wolf+ 2010, k=9.3 for King model)
# We don't have r_h directly, so use the Baumgardt+ 2019 median r_h = 3.0 pc

# Without r_h, we need a proxy
# The mass estimator for King models with no r_h is:
# M = 4.5 * sigma^2 * r_half / G  (Wolf+ 2010)
# 
# For typical GCs, r_half = 1-10 pc
# We use the median r_half from Baumgardt+ 2019 = 3.5 pc for Milky Way GCs

# r_h from Harris concentration c
# For King model: r_half = r_c * f(c)
# f(c) varies from ~0.5 (c=1) to ~5 (c=2.5)
# Without r_c, we can't compute r_half exactly
# 
# But we can use a proxy: sigma_0 vs r_half relation
# r_half ≈ 1.0 * sigma_0^0.5 (in pc, km/s) - very rough
# 
# Let me use a fixed r_half = 3.5 pc (median from Baumgardt+ 2019)

r_h_pc = 3.5  # median half-light radius for MW GCs

print(f"\n3. Computing M_dyn (assuming r_h = {r_h_pc} pc, fixed median)...")
print(f"   (real r_h varies 1-10 pc, see Baumgardt+ 2019)")

m_dyn_arr = []
L_arr = []  # luminosity in L_sun
Rgc_arr = []
M_V_arr = []
sigma_arr = []
name_arr = []

for row in joined:
    if row['sigma'] <= 0 or row['Vt'] <= 0:
        continue
    
    # Distance
    if row['Dist'] > 0:
        dist_kpc = row['Dist']
    elif row['m-M'] > 0:
        dist_kpc = 10**((row['m-M']+5)/5) / 100
    else:
        continue
    
    # Absolute V magnitude
    M_V = row['Vt'] - 5 * np.log10(dist_kpc) - 10
    
    # Luminosity in L_sun (using M_sun_V = 4.83)
    L_sun = 10**(-0.4 * (M_V - M_sun_V))
    
    # Velocity dispersion in m/s
    sigma_m_s = row['sigma'] * km_s_to_m_s
    
    # Half-light radius in m
    r_h_m = r_h_pc * kpc_to_m / 1000  # pc to m
    
    # Dynamical mass (Wolf+ 2010 estimator)
    m_dyn_kg = 4.5 * sigma_m_s**2 * r_h_m / G
    
    m_dyn_arr.append(m_dyn_kg)
    L_arr.append(L_sun)
    M_V_arr.append(M_V)
    Rgc_arr.append(row['Rgc'])
    sigma_arr.append(row['sigma'])
    name_arr.append(row['Name'])

m_dyn_arr = np.array(m_dyn_arr)
L_arr = np.array(L_arr)
M_V_arr = np.array(M_V_arr)
Rgc_arr = np.array(Rgc_arr)
sigma_arr = np.array(sigma_arr)

# Dynamical mass in M_sun
m_dyn_Msun = m_dyn_arr / M_sun

# Stellar mass assuming M/L_V = 2 (typical for old metal-poor)
# M/L_V for metal-poor GCs is ~1.5-2.5 in V band
m_stellar_Msun = 2.0 * L_arr

# M_dyn / M_stellar ratio (the DM indicator)
ML_ratio = m_dyn_Msun / m_stellar_Msun

print(f"\n4. Results:")
print(f"   Number of GCs: {len(ML_ratio)}")
print(f"   M_V range: {M_V_arr.min():.2f} to {M_V_arr.max():.2f}")
print(f"   M_dyn median: {np.median(m_dyn_Msun):.2e} M_sun")
print(f"   L/L_sun median: {np.median(L_arr):.2e}")
print(f"   M_stellar median (M/L=2): {np.median(m_stellar_Msun):.2e} M_sun")
print(f"   M_dyn/M_stellar ratio (median): {np.median(ML_ratio):.2f}")
print(f"   M_dyn/M_stellar ratio (16-84 percentile): {np.percentile(ML_ratio, 16):.2f} - {np.percentile(ML_ratio, 84):.2f}")
print(f"   Frac with ratio > 3: {100*np.sum(ML_ratio > 3)/len(ML_ratio):.1f}%")
print(f"   Frac with ratio > 5: {100*np.sum(ML_ratio > 5)/len(ML_ratio):.1f}%")
print(f"   Frac with ratio > 10: {100*np.sum(ML_ratio > 10)/len(ML_ratio):.1f}%")

# Sensitivity check: what if r_h is different?
print(f"\n5. Sensitivity to r_h (sensitivity test):")
for r_h_test in [1.5, 2.5, 3.5, 5.0, 7.0]:
    m_dyn_test = 4.5 * (sigma_arr * km_s_to_m_s)**2 * (r_h_test * kpc_to_m / 1000) / G / M_sun
    m_stellar_test = 2.0 * L_arr
    ml_test = m_dyn_test / m_stellar_test
    print(f"   r_h = {r_h_test} pc: median M_dyn/M_stellar = {np.median(ml_test):.2f}")

# M/L vs Galactocentric distance
print(f"\n6. M_dyn/M_stellar vs Galactocentric distance:")
bin_edges = [0, 3, 6, 10, 15, 25, 50]
for i in range(len(bin_edges)-1):
    mask = (Rgc_arr >= bin_edges[i]) & (Rgc_arr < bin_edges[i+1])
    if np.sum(mask) > 0:
        mls = ML_ratio[mask]
        n = len(mls)
        median_ml = np.median(mls)
        std_ml = np.std(mls)
        print(f"   {bin_edges[i]:3d}-{bin_edges[i+1]:3d} kpc: N={n:3d}, median M_dyn/M_stellar = {median_ml:.2f} ± {std_ml:.2f}")

# Verdict
print(f"\n7. Verdict:")
print(f"   Cascade prediction: M_dyn/M_stellar ~ 1-3 for all GCs (no DM)")
print(f"   Observed (median): {np.median(ML_ratio):.2f}")
if np.median(ML_ratio) < 3:
    print(f"   Result: ✓ CONSISTENT with cascade (M_dyn ~ M_stellar, no DM excess)")
elif np.median(ML_ratio) < 5:
    print(f"   Result: PARTIALLY consistent (some excess but within stellar range)")
else:
    print(f"   Result: TENSION for cascade (excess suggests DM)")

# Honest caveats
print(f"\n8. Caveats:")
print(f"   - Used fixed r_h = 3.5 pc for all GCs (real r_h varies 1-10 pc)")
print(f"   - Used M/L_V_stellar = 2 (real range is 1.5-2.5)")
print(f"   - The M_dyn/M_stellar ratio scales linearly with r_h")
print(f"   - For a fair test, need individual r_h from HST or ground-based imaging")
print(f"   - This is a QUALITATIVE test, not a precision measurement")

# Save results
output_path = "/workspace/github-repo/calculations/globular_cluster_dm_test_results.txt"
with open(output_path, 'w') as f:
    f.write(f"Globular Cluster DM Test Results\n")
    f.write(f"================================\n\n")
    f.write(f"Sample size: {len(ML_ratio)} GCs (cross-matched from Harris 1996 + Usher+ 2013)\n")
    f.write(f"Assumed r_h: {r_h_pc} pc (fixed median; real r_h varies 1-10 pc)\n")
    f.write(f"Assumed M/L_V_stellar: 2.0 (typical for old metal-poor GCs)\n\n")
    f.write(f"M_V range: {M_V_arr.min():.2f} to {M_V_arr.max():.2f}\n")
    f.write(f"M_dyn median: {np.median(m_dyn_Msun):.2e} M_sun\n")
    f.write(f"L/L_sun median: {np.median(L_arr):.2e}\n")
    f.write(f"M_stellar median: {np.median(m_stellar_Msun):.2e} M_sun\n")
    f.write(f"M_dyn/M_stellar ratio (median): {np.median(ML_ratio):.2f}\n")
    f.write(f"M_dyn/M_stellar ratio (16-84 percentile): {np.percentile(ML_ratio, 16):.2f} - {np.percentile(ML_ratio, 84):.2f}\n")
    f.write(f"Frac with ratio > 3: {100*np.sum(ML_ratio > 3)/len(ML_ratio):.1f}%\n")
    f.write(f"Frac with ratio > 5: {100*np.sum(ML_ratio > 5)/len(ML_ratio):.1f}%\n")
    f.write(f"Frac with ratio > 10: {100*np.sum(ML_ratio > 10)/len(ML_ratio):.1f}%\n\n")
    f.write(f"Verdict: ")
    if np.median(ML_ratio) < 3:
        f.write(f"CONSISTENT with cascade (no DM)\n")
    elif np.median(ML_ratio) < 5:
        f.write(f"PARTIALLY consistent\n")
    else:
        f.write(f"TENSION for cascade\n")
    f.write(f"\nSensitivity to r_h:\n")
    for r_h_test in [1.5, 2.5, 3.5, 5.0, 7.0]:
        m_dyn_test = 4.5 * (sigma_arr * km_s_to_m_s)**2 * (r_h_test * kpc_to_m / 1000) / G / M_sun
        m_stellar_test = 2.0 * L_arr
        ml_test = m_dyn_test / m_stellar_test
        f.write(f"  r_h = {r_h_test} pc: median = {np.median(ml_test):.2f}\n")

print(f"\nResults saved to {output_path}")
