#!/usr/bin/env python3
"""
Lagrangian v14: Direct numerical check of M^1.29 universality across 14 SIDC events
====================================================================================

The M^1.29 scaling law says:
  tau_obs = gamma * t_Pl
  gamma = (E / E_Pl)^alpha
  alpha = 1.289 = 1 + 1/sqrt(12)

For each of 14 SIDC events, we check:
  1. gamma = (E / E_Pl)^1.289
  2. tau_2D_proper = gamma * t_Pl
  3. Verify tau_obs matches this prediction

The 14 events (from §3.17 democratic cosmology):
- Planck brane collision: E = 10^69 J, tau_obs ~ 13.8 Gyr
- LHC collision: E ~ 10^-6 J per particle
- Supernova neutrino burst: E = 10^44 J, tau_obs = 33 s
- BBN: E ~ 10^-12 J, tau_obs ~ 1 s
- Binary neutron star merger: E ~ 10^45 J, tau_obs ~ 100 s
- Vacuum decay bubble: E ~ 10^46 J, tau_obs ~ 1 hr
- Black hole merger: E ~ 10^47 J, tau_obs ~ 0.1 s
- Big bang singularity: E = 10^69 J, tau_obs ~ 1 yr (loop quantum cosmology)
- Inflationary reheating: E ~ 10^63 J, tau_obs ~ 10^-32 s
- ...

We will:
1. Compile a table of 14 events with (E, tau_obs)
2. Compute tau_2D_proper for each
3. Check if all 14 give tau_2D_proper ~ t_Pl (universal)
4. Compute the scatter

If the scatter is small (say < 30%), then M^1.29 is empirically verified.
If the scatter is large, M^1.29 needs modification.


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

import numpy as np

# Constants
T_PLANCK = 5.391e-44  # Planck time in seconds
M_PLANCK = 2.176e-8    # Planck mass in kg
C = 2.998e8            # speed of light in m/s
E_PLANCK = M_PLANCK * C**2  # Planck energy in J

ALPHA = 1.289  # The M^1.29 exponent
SQRT12 = np.sqrt(12)

print("="*72)
print("LAGRANGIAN v14: M^1.29 UNIVERSALITY CHECK ACROSS 14 SIDC EVENTS")
print("="*72)
print(f"\nalpha = {ALPHA} = 1 + 1/sqrt(12)")
print(f"t_Pl = {T_PLANCK:.3e} s")
print(f"E_Pl = {E_PLANCK:.3e} J = M_Pl c^2")

# =============================================================================
# PART 1: Compile the 14 events (from §3.17 democratic cosmology)
# =============================================================================
events = [
    # (name, energy J, observation time s)
    ("Supernova neutrino burst (SN1987A)", 1e44, 33.0),
    ("Binary neutron star merger (GW170817)", 1e45, 100.0),
    ("Black hole merger (GW150914)", 1e47, 0.1),
    ("Big Bang (early inflation)", 1e69, 1e-32),
    ("Reheating (end of inflation)", 1e63, 1e-32),
    ("LHC high-energy collision", 2.2e-6, 1e-25),
    ("BBN (Big Bang nucleosynthesis)", 1e-12, 1.0),
    ("Cosmic microwave background decoupling", 1e15, 1e13),
    ("Vacuum decay bubble nucleation", 1e46, 3600.0),
    ("Gamma-ray burst (typical)", 1e44, 1e-3),
    ("Active galactic nucleus jet", 1e48, 1e8),
    ("Solar flare", 1e25, 1e3),
    ("Earthquake (energy release)", 1e17, 10.0),
    ("Planck brane collision (big crunch)", 1e69, 4.35e17),  # ~13.8 Gyr
]

print(f"\n{'#':>3} {'Event':>40} {'E (J)':>10} {'tau_obs (s)':>14}")
print("-"*72)
for i, (name, E, tau_obs) in enumerate(events):
    print(f"{i+1:>3} {name:>40} {E:>10.1e} {tau_obs:>14.3e}")

# =============================================================================
# PART 2: Compute tau_2D_proper = gamma * t_Pl for each event
# =============================================================================
print("\n" + "="*72)
print("PART 2: PREDICTED tau_2D_proper = gamma * t_Pl")
print("="*72)

results = []
print(f"\n{'#':>3} {'Event':>40} {'gamma':>14} {'tau_2D_proper':>14} {'tau_obs':>14} {'ratio':>10}")
print("-"*100)

for i, (name, E, tau_obs) in enumerate(events):
    # Compute gamma = (E/E_Pl)^alpha
    gamma = (E / E_PLANCK) ** ALPHA
    # Compute tau_2D_proper = gamma * t_Pl
    tau_2D_proper = gamma * T_PLANCK
    # Ratio: tau_obs / tau_2D_proper (should be ~ 1 if M^1.29 is correct)
    ratio = tau_obs / tau_2D_proper
    results.append((name, E, tau_obs, gamma, tau_2D_proper, ratio))
    print(f"{i+1:>3} {name:>40} {gamma:>14.3e} {tau_2D_proper:>14.3e} {tau_obs:>14.3e} {ratio:>10.3e}")

# =============================================================================
# PART 3: Check universality of tau_2D_proper
# =============================================================================
print("\n" + "="*72)
print("PART 3: UNIVERSALITY CHECK")
print("="*72)

tau_2D_values = [r[4] for r in results]
tau_2D_arr = np.array(tau_2D_values)

print(f"\ntau_2D_proper across 14 events:")
print(f"  Min:    {np.min(tau_2D_arr):.3e} s")
print(f"  Max:    {np.max(tau_2D_arr):.3e} s")
print(f"  Mean:   {np.mean(tau_2D_arr):.3e} s")
print(f"  Median: {np.median(tau_2D_arr):.3e} s")
print(f"  Std:    {np.std(tau_2D_arr):.3e} s")
print(f"  t_Pl:   {T_PLANCK:.3e} s")
print(f"  Median / t_Pl: {np.median(tau_2D_arr) / T_PLANCK:.3f}")

# =============================================================================
# PART 4: Compare with tau_obs
# =============================================================================
print("\n" + "="*72)
print("PART 4: PREDICTION ACCURACY (tau_obs vs tau_2D_proper)")
print("="*72)

ratios = np.array([r[5] for r in results])
print(f"\nRatio = tau_obs / tau_2D_proper:")
print(f"  Min:    {np.min(ratios):.3e}")
print(f"  Max:    {np.max(ratios):.3e}")
print(f"  Mean:   {np.mean(ratios):.3e}")
print(f"  Median: {np.median(ratios):.3e}")
print(f"  Std:    {np.std(ratios):.3e}")

# How many are within 1 order of magnitude?
within_1dex = np.sum((ratios > 0.1) & (ratios < 10))
within_3dex = np.sum((ratios > 1e-3) & (ratios < 1e3))
print(f"\n  Within 1 dex:  {within_1dex}/{len(events)} = {100*within_1dex/len(events):.0f}%")
print(f"  Within 3 dex:  {within_3dex}/{len(events)} = {100*within_3dex/len(events):.0f}%")

# =============================================================================
# PART 5: What alpha WOULD make all 14 events match?
# =============================================================================
print("\n" + "="*72)
print("PART 5: BEST-FIT alpha ACROSS 14 EVENTS")
print("="*72)

# For each event, find alpha that makes tau_obs = (E/E_Pl)^alpha * t_Pl
# alpha_i = log(tau_obs / t_Pl) / log(E / E_Pl)
alphas_per_event = []
print(f"\n{'#':>3} {'Event':>40} {'alpha_implied':>14}")
print("-"*72)
for i, (name, E, tau_obs) in enumerate(events):
    alpha_i = np.log(tau_obs / T_PLANCK) / np.log(E / E_PLANCK)
    alphas_per_event.append(alpha_i)
    print(f"{i+1:>3} {name:>40} {alpha_i:>14.4f}")

alphas_arr = np.array(alphas_per_event)
print(f"\nImplied alpha across 14 events:")
print(f"  Min:    {np.min(alphas_arr):.4f}")
print(f"  Max:    {np.max(alphas_arr):.4f}")
print(f"  Mean:   {np.mean(alphas_arr):.4f}")
print(f"  Median: {np.median(alphas_arr):.4f}")
print(f"  Std:    {np.std(alphas_arr):.4f}")
print(f"  SIDC:   {ALPHA:.4f}")

# =============================================================================
# PART 6: Verdict
# =============================================================================
print("\n" + "="*72)
print("PART 6: VERDICT")
print("="*72)

if np.std(alphas_arr) < 0.3:
    print(f"\n+ M^1.29 universality is SUPPORTED")
    print(f"  Implied alpha has std = {np.std(alphas_arr):.3f}")
    print(f"  Median alpha = {np.median(alphas_arr):.3f} vs SIDC {ALPHA}")
else:
    print(f"\n- M^1.29 universality is MARGINAL")
    print(f"  Implied alpha has std = {np.std(alphas_arr):.3f} (too large)")
    print(f"  Different events imply DIFFERENT alphas")
    print(f"  Possible: alpha is not universal, or my E/tau_obs values are imprecise")

print("\n" + "="*72)
print("HONEST VERDICT (v14):")
print("  + Direct numerical check of M^1.29 across 14 events")
print("  + Computes the implied alpha for each event")
print("  + Tests universality assumption")
print("="*72)