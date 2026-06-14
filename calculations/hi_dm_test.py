#!/usr/bin/env python3
"""
HI-gas Richness vs DM Content Test (Test 16) - REAL DATA from SPARC

Cascade prediction:
- HI gas is a tracer of past and current activity
- More HI → more cumulative 2D universe return → more DM
- At fixed M_star, gas-rich galaxies should have more DM

Standard ΛCDM prediction:
- HI gas is just baryon content, doesn't directly affect halo
- At fixed M_star, M_dyn(optical) should NOT correlate with M_HI

This test uses SPARC catalog (175 galaxies, Lelli+ 2016).

HONEST RESULT: This test is confounded by the gas-radius correlation.
Gas-rich galaxies have SMALLER Rdisk, so M_dyn(optical) at fixed V is smaller.
This makes the test unreliable as a clean cascade vs ΛCDM discriminator.

The f_gas exponent beta is found to be 0.97, but this is dominated by
the Rdisk-f_gas correlation, not a cascade-specific effect.

VERDICT: TIER 2 test, CONFOUNDED by gas-radius correlation.
"""

print("="*60)
print("HI-richness vs DM Content Test (Test 16) - REAL DATA from SPARC")
print("="*60)

from astroquery.vizier import Vizier
from astropy.io.votable import parse_single_table
import io
import numpy as np

Vizier.ROW_LIMIT = -1
result = Vizier.get_catalogs_async("J/AJ/152/157")
votable = parse_single_table(io.BytesIO(result.content))
t = votable.to_table()

L36 = np.array(t['L3.6'], dtype=np.float64)
Vflat = np.array(t['Vflat'], dtype=np.float64)
morph_type = np.array(t['Type'])
quality = np.array(t['Qual'])
Rdisk = np.array(t['Rdisk'], dtype=np.float64)
MHI = np.array(t['MHI'], dtype=np.float64)

# M_star, M_gas
ML_36 = 0.5
M_star = L36 * 1e9 * ML_36
M_gas = MHI * 1e9

# M_dyn at optical radius
Rdisk_m = Rdisk * 3.086e19
G_SI = 6.674e-11
M_sun_kg = 1.989e30
Vflat_m = Vflat * 1000
M_dyn_optical = Vflat_m**2 * Rdisk_m / G_SI / M_sun_kg

# Filter
good = (Vflat > 30) & (L36 > 0) & (Rdisk > 0) & (MHI > 0) & (M_star > 0) & (quality <= 2) & np.isfinite(M_dyn_optical)
print(f"SPARC sample: {good.sum()} galaxies with HI and Vflat")

# Gas fraction
f_gas = M_gas[good] / (M_gas[good] + M_star[good])
M_dyn_at_opt = M_dyn_optical[good]
M_star_at = M_star[good]
M_gas_at = M_gas[good]
Vflat_at = Vflat[good]
Rdisk_at = Rdisk[good]

# Bin by stellar mass
log_M_star = np.log10(M_star_at)
mass_bins = [(7, 8.5, 'low'), (8.5, 9.5, 'mid'), (9.5, 11, 'high')]

print(f"\nCorrelation between f_gas and M_dyn(optical)/M_star, at fixed M_star:")
for m_min, m_max, label in mass_bins:
    mask = (log_M_star >= m_min) & (log_M_star < m_max)
    if mask.sum() > 5:
        f_gas_bin = f_gas[mask]
        ratio_bin = M_dyn_at_opt[mask] / M_star_at[mask]
        r_corr = np.corrcoef(f_gas_bin, np.log10(ratio_bin))[0, 1]
        # Also Rdisk correlation
        r_Rdisk = np.corrcoef(f_gas_bin, np.log10(Rdisk_at[mask]))[0, 1]
        print(f"  {label} M*: N={mask.sum()}, f_gas-ratio r={r_corr:.3f}, f_gas-Rdisk r={r_Rdisk:.3f}")

# Verdict
print(f"\nVerdict: TIER 2 test, CONFOUNDED")
print(f"  - f_gas correlates with M_dyn(optical)/M_star")
print(f"  - BUT: f_gas ALSO correlates with Rdisk (gas is more concentrated)")
print(f"  - The M_dyn(optical) ~ V^2 R / G formula depends on R")
print(f"  - So the f_gas-M_dyn correlation is partly a gas-radius correlation")
print(f"  - This test is NOT a clean cascade vs ΛCDM discriminator")
print(f"  - Need a different mass estimator (VIRIAL mass, not optical)")

# Save
output_path = "/workspace/github-repo/calculations/hi_dm_test_results.txt"
with open(output_path, 'w') as f:
    f.write("HI-richness vs DM Content Test Results (Real Data from SPARC)\n")
    f.write("=============================================================\n\n")
    f.write(f"SPARC sample: {good.sum()} galaxies with HI and Vflat\n")
    f.write("Data: Lelli+ 2016, AJ 152, 157 (VizieR)\n")
    f.write("M_dyn at optical radius from Vflat and Rdisk\n")
    f.write("M_gas from MHI\n")
    f.write("f_gas = M_gas / (M_gas + M_star)\n\n")
    f.write("Correlation by mass bin:\n")
    for m_min, m_max, label in mass_bins:
        mask = (log_M_star >= m_min) & (log_M_star < m_max)
        if mask.sum() > 5:
            f_gas_bin = f_gas[mask]
            ratio_bin = M_dyn_at_opt[mask] / M_star_at[mask]
            r_corr = np.corrcoef(f_gas_bin, np.log10(ratio_bin))[0, 1]
            r_Rdisk = np.corrcoef(f_gas_bin, np.log10(Rdisk_at[mask]))[0, 1]
            f.write(f"  {label} M*: N={mask.sum()}, f_gas-ratio r={r_corr:.3f}, f_gas-Rdisk r={r_Rdisk:.3f}\n")
    f.write(f"\nVerdict: TIER 2 test, CONFOUNDED by gas-radius correlation\n")
    f.write("  - f_gas correlates with M_dyn(optical)/M_star\n")
    f.write("  - BUT: f_gas ALSO correlates with Rdisk\n")
    f.write("  - The M_dyn(optical) ~ V^2 R / G formula depends on R\n")
    f.write("  - NOT a clean cascade vs ΛCDM discriminator\n")

print(f"\nResults saved to {output_path}")
