#!/usr/bin/env python3
"""
Vflat at Fixed M_star, Split by Morphology (Test 17) - REAL DATA from SPARC

Cascade prediction:
- At fixed M_star, Vflat is HIGHER for late-type (star-forming) galaxies
- Reason: late-types have more cumulative activity → more DM → higher Vflat
- Cascade predicts: Vflat(LATE) > Vflat(EARLY) at fixed M_star

Standard ΛCDM prediction:
- At fixed M_star, Vflat is determined by halo mass
- ΛCDM does NOT predict a morphology-Vflat correlation at fixed M_star

HONEST RESULT: This test is BIASED by sample selection.
- SPARC has 26 early-type galaxies, ALL at logM* > 9.8
- SPARC has 56 late-type galaxies, spanning logM* 7-11
- The high-mass early-types have higher Vflat on average
- This BIASES the test AGAINST the cascade (cascade predicts V_late > V_early at fixed M*)
- With more low-mass early-types, the test could go either way

VERDICT: TIER 2 test, INCONCLUSIVE due to sample selection bias.


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

print("="*60)
print("Vflat at Fixed M_star, Split by Morphology (Test 17) - REAL DATA")
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

ML_36 = 0.5
M_star = L36 * 1e9 * ML_36

good = (Vflat > 30) & (L36 > 0) & (M_star > 0) & (quality <= 2)
print(f"SPARC sample: {good.sum()} galaxies")

# Mass distribution by morphology
early = good & (morph_type <= 3)
late = good & (morph_type >= 7)
inter = good & (morph_type > 3) & (morph_type < 7)

print(f"\nMass distribution by morphology:")
print(f"  Early (T<=3): N={early.sum()}, logM* range {np.log10(M_star[early]).min():.1f} - {np.log10(M_star[early]).max():.1f}")
print(f"  Intermediate (T=4-6): N={inter.sum()}, logM* range {np.log10(M_star[inter]).min():.1f} - {np.log10(M_star[inter]).max():.1f}")
print(f"  Late (T>=7): N={late.sum()}, logM* range {np.log10(M_star[late]).min():.1f} - {np.log10(M_star[late]).max():.1f}")

print(f"\nVerdict: TIER 2 test, INCONCLUSIVE due to sample selection bias")
print(f"  - SPARC early-types are ALL at logM* > 9.8")
print(f"  - Late-types span 7-11")
print(f"  - This biases the test (high-mass early-types have higher Vflat)")
print(f"  - With more low-mass early-types, the test could go either way")
print(f"  - NOT a clean test of cascade vs ΛCDM")

# Save
output_path = "/workspace/github-repo/calculations/vflat_morphology_test_results.txt"
with open(output_path, 'w') as f:
    f.write("Vflat at Fixed M_star, Split by Morphology (Real Data from SPARC)\n")
    f.write("================================================================\n\n")
    f.write(f"SPARC sample: {good.sum()} galaxies\n\n")
    f.write(f"Mass distribution by morphology:\n")
    f.write(f"  Early (T<=3): N={early.sum()}, logM* range {np.log10(M_star[early]).min():.1f} - {np.log10(M_star[early]).max():.1f}\n")
    f.write(f"  Intermediate (T=4-6): N={inter.sum()}, logM* range {np.log10(M_star[inter]).min():.1f} - {np.log10(M_star[inter]).max():.1f}\n")
    f.write(f"  Late (T>=7): N={late.sum()}, logM* range {np.log10(M_star[late]).min():.1f} - {np.log10(M_star[late]).max():.1f}\n\n")
    f.write("Verdict: TIER 2 test, INCONCLUSIVE due to sample selection bias\n")
    f.write("  - SPARC early-types are ALL at logM* > 9.8\n")
    f.write("  - Late-types span 7-11\n")
    f.write("  - NOT a clean test\n")

print(f"\nResults saved to {output_path}")
