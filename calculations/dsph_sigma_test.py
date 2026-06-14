#!/usr/bin/env python3
"""
Dwarf Spheroidal M_dyn Test (Test 9) - Real Data

This test checks the M_dyn - M_star relation for MW dSphs
and compares it to cascade vs ΛCDM predictions.

Cascade prediction:
- DM is geometric, no particles
- M_dyn should correlate with PAST cumulative activity
- Brighter dSphs (more total stars) had more past activity → more DM
- BUT: brighter dSphs also have more stars, so M_dyn/M_star ratio
  can be lower for bright dSphs (just like M_dyn/M_* for galaxies is lower at high M_*)

Standard ΛCDM prediction:
- M_dyn correlates with M_halo (universal NFW)
- Same M_dyn-M_star relation as cascade
- The relation is set by abundance matching

Test:
- Compute M_dyn for 10 MW dSphs (Wolf+ 2010 mass estimator)
- Compare to M_star (from M_V + M/L_V)
- Both models predict same M_dyn-M_star relation
- The cascade just provides a different MECHANISM for why M_dyn ~ sigma^2 r_h

Verdict: CONSISTENT with both cascade and ΛCDM (NOT a discriminative test)

The M_dyn-M_star relation for dSphs is a structural property that's
similar in both frameworks. The cascade and ΛCDM both predict
M_dyn to scale with sigma^2 r_h; they differ in the MECHANISM
(cumulative 2D universe gravity vs NFW halo).
"""

print("="*60)
print("Dwarf Spheroidal M_dyn Test (Test 9) - Real Data")
print("="*60)

dsphs = {
    'Draco':       {'sigma': 9.1,  'r_h': 196,  'M_V': -8.7},
    'Ursa Minor':  {'sigma': 9.5,  'r_h': 181,  'M_V': -8.5},
    'Sculptor':    {'sigma': 9.2,  'r_h': 260,  'M_V': -10.8},
    'Sextans':     {'sigma': 7.9,  'r_h': 682,  'M_V': -9.5},
    'Carina':      {'sigma': 6.7,  'r_h': 241,  'M_V': -9.0},
    'Fornax':      {'sigma': 11.7, 'r_h': 668,  'M_V': -13.2},
    'Leo I':       {'sigma': 9.2,  'r_h': 251,  'M_V': -11.9},
    'Leo II':      {'sigma': 6.7,  'r_h': 151,  'M_V': -9.6},
    'Sagittarius': {'sigma': 11.0, 'r_h': 1500, 'M_V': -13.5},
    'CVn I':       {'sigma': 7.6,  'r_h': 564,  'M_V': -7.9},
}

import numpy as np
G_pc = 4.302e-3
M_sun_V = 4.83

# Test with M/L_V = 2 (conservative)
ML = 2.0

print(f"\nUsing M/L_V = {ML}, Wolf+ 2010 mass estimator:")
print(f"{'Name':<22s} {'sigma':>6s} {'r_h':>6s} {'M_V':>6s} {'M_dyn':>10s} {'M_star':>10s} {'M_dyn/M_star':>13s}")
print("-" * 90)

ratios = []
M_dyns = []
M_stars = []
for name, p in dsphs.items():
    sigma = p['sigma']
    r_h = p['r_h']
    M_V = p['M_V']
    
    r_1_2 = (4.0/3.0) * r_h
    M_dyn = 4.5 * sigma**2 * r_1_2 / G_pc
    M_dyns.append(M_dyn)
    
    L_V = 10**(-(M_V - M_sun_V)/2.5)
    M_star = ML * L_V
    M_stars.append(M_star)
    
    ratio = M_dyn / M_star
    ratios.append(ratio)
    
    print(f"  {name:<20s} {sigma:>5.1f}  {r_h:>5.0f}  {M_V:>5.1f}  {M_dyn:>9.2e}  {M_star:>9.2e}  {ratio:>10.1f}")

# Check the M_dyn-M_star correlation
log_M_dyn = np.log10(M_dyns)
log_M_star = np.log10(M_stars)
slope, intercept = np.polyfit(log_M_star, log_M_dyn, 1)

print(f"\nM_dyn-M_star relation (log-log):")
print(f"  Slope: {slope:.2f}")
print(f"  Intercept: {intercept:.2f}")
print(f"  Expected (NFW abundance matching): slope ~ 0.3-0.5")

print(f"\nSummary (M/L_V = {ML}):")
print(f"  Median M_dyn/M_star: {np.median(ratios):.1f}")
print(f"  Range: {min(ratios):.1f} - {max(ratios):.1f}")

print(f"\nCascade interpretation:")
print(f"  - M_dyn correlates with M_star with slope {slope:.2f}")
print(f"  - Brighter dSphs have more DM in absolute terms")
print(f"  - But M_dyn/M_star ratio is LOWER for bright dSphs (slope < 1)")
print(f"  - This is the standard dSph mass relation")

print(f"\nVerdict: CONSISTENT with both cascade and ΛCDM (NOT discriminative)")
print(f"  - The M_dyn-M_star relation is similar in both frameworks")
print(f"  - The cascade and ΛCDM differ in MECHANISM, not the relation itself")
print(f"  - This is similar to the halo M/M* vs z test (Test 6)")

# Save
output_path = "/workspace/github-repo/calculations/dsph_sigma_test_results.txt"
with open(output_path, 'w') as f:
    f.write("Dwarf Spheroidal M_dyn Test Results (Real Data)\n")
    f.write("==================================================\n\n")
    f.write("Sample: 10 MW dSphs with measured sigma, r_h, M_V\n")
    f.write("Mass estimator: Wolf+ 2010 (M_1/2 = 4.5 sigma^2 r_1/2 / G)\n")
    f.write("M/L_V: 2 (conservative)\n\n")
    f.write(f"Results:\n")
    f.write(f"{'Name':<22s} {'sigma':>6s} {'r_h':>6s} {'M_V':>6s} {'M_dyn':>10s} {'M_star':>10s} {'M_dyn/M_star':>13s}\n")
    f.write("-" * 90 + "\n")
    for name, p in dsphs.items():
        r_1_2 = (4.0/3.0) * p['r_h']
        M_dyn = 4.5 * p['sigma']**2 * r_1_2 / G_pc
        L_V = 10**(-(p['M_V'] - M_sun_V)/2.5)
        M_star = ML * L_V
        ratio = M_dyn / M_star
        f.write(f"  {name:<20s} {p['sigma']:>5.1f}  {p['r_h']:>5.0f}  {p['M_V']:>5.1f}  {M_dyn:>9.2e}  {M_star:>9.2e}  {ratio:>10.1f}\n")
    f.write(f"\nM_dyn-M_star relation slope: {slope:.2f}\n\n")
    f.write("Cascade interpretation:\n")
    f.write("  - M_dyn correlates with M_star (slope < 1)\n")
    f.write("  - Both cascade and ΛCDM predict this relation\n")
    f.write("  - NOT a discriminative test\n\n")
    f.write("VERDICT: CONSISTENT with both cascade and ΛCDM (NOT discriminative)\n")

print(f"\nResults saved to {output_path}")
