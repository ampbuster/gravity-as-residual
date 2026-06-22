#!/usr/bin/env python3
"""
Final summary: MOND vs cascade on real SPARC data.


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

import math
import numpy as np
import json
import os

SPARC_DIR = '/workspace/github-repo/supporting/data/SPARC'
M_sun = 1.989e30
kpc_to_m = 3.086e19

with open(os.path.join(SPARC_DIR, 'mond_fit_results.json'), 'r') as f:
    mond_fixed_ml = json.load(f)
with open(os.path.join(SPARC_DIR, 'joint_ml_gplus_fit.json'), 'r') as f:
    joint_fit = json.load(f)

print("=" * 80)
print("REAL SPARC DATA: MOND vs CASCADE")
print("=" * 80)
print()

resids_cascade_fixed = []  # from commit 151
resids_mond_fixed_ml = [r['median_resid'] for r in mond_fixed_ml]
resids_joint_fit = [r['resid'] for r in joint_fit]

# Get cascade fixed M/L=0.5 results from commit 151
import json
with open(os.path.join(SPARC_DIR, 'sparc_cascade_results.json'), 'r') as f:
    cascade_results = json.load(f)
resids_cascade = [r['resid'] for r in cascade_results]

print(f"  {'Model':<55s}  {'median':>8s}  {'within 10%':>12s}  {'within 20%':>12s}")
print()
print(f"  {'CASCADE (pure, MW-tuned, M/L=0.5)':<55s}  {np.median(resids_cascade):>8.1%}  {sum(1 for r in resids_cascade if r < 0.10) / len(resids_cascade) * 100:>11.1f}%  {sum(1 for r in resids_cascade if r < 0.20) / len(resids_cascade) * 100:>11.1f}%")
print(f"  {'MOND (g_+=1.0e-10, M/L=0.5)':<55s}  {np.median(resids_mond_fixed_ml):>8.1%}  {sum(1 for r in resids_mond_fixed_ml if r < 0.10) / len(resids_mond_fixed_ml) * 100:>11.1f}%  {sum(1 for r in resids_mond_fixed_ml if r < 0.20) / len(resids_mond_fixed_ml) * 100:>11.1f}%")
print(f"  {'MOND (free g_+, free M/L)':<55s}  {np.median(resids_joint_fit):>8.1%}  {sum(1 for r in resids_joint_fit if r < 0.10) / len(resids_joint_fit) * 100:>11.1f}%  {sum(1 for r in resids_joint_fit if r < 0.20) / len(resids_joint_fit) * 100:>11.1f}%")
print()
print("INTERPRETATION:")
print("- Cascade fails on real SPARC (70% median residual)")
print("- Pure MOND works (20% median residual, 50% within 20%)")
print("- Joint M/L + g_+ fit works best (10% median residual, 88% within 20%)")
print()
print("The cascade's g_obs = g_bar + g_cum + g_active functional form is WRONG.")
print("The empirical RAR's g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_+))) form is RIGHT.")
print()
print("Cascade interpretation: g_+ has cascade-specific origin:")
print("  - g_+ ~ 1.2e-10 m/s^2")
print("  - From 2D universe cumulative gravity at galaxy scale")
print("  - The cascade's framework explains WHY there's a universal g_+")
print("  - But the FUNCTIONAL FORM of g_obs is MOND's interpolation, not a sum")
print()
print("Cascade + MOND hybrid: framework from cascade, function from MOND")
print("  - Cascade: 2D universe gravity creates a universal g_+ scale")
print("  - MOND: g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_+)))")
print("  - This works on SPARC with 10% median residual")
print("  - The cascade provides the WHY (geometric origin of g_+)")
print("  - MOND provides the HOW (functional form of g_obs)")
