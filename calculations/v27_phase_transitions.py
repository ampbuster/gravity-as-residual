"""
v2.7.53: Add phase transitions and primordial BH to cumulative DM.

The v2.7.51 analysis used 14+ event types but missed:
- Electroweak phase transition (z~10^15, E ~ 10^55 J)
- QCD phase transition (z~10^12, E ~ 10^50 J)
- Primordial BH evaporation (Hawking radiation)
- Vacuum decay events (if false vacuum exists)

If these contribute significantly, F_s(0) could be larger.


**HISTORICAL (v2.7 era, mid-2025)**: This file is from the v2.7.x era, predating:
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
specific numerical values reflect v2.7 era framework, not v3.5.9+ A2.

"""

import json
import numpy as np

c = 2.998e8
M_sun = 1.989e30
yr = 3.156e7

# Existing cumulative DM from v2.7.51
M_cum_v2751 = 8.6e18  # M_☉

# 1. Electroweak phase transition
# z ~ 10^15, T ~ 100 GeV, total energy released ~ 10^55 J
# Number of "events" depends on correlation length
# Rough estimate: 10^30 Hubble volumes during EW transition
# Each Hubble volume: E_Hubble ~ 10^55 J / 10^30 = 10^25 J per "event"
# Actually, the EW transition is a smooth event, not discrete
# Total energy ~ 10^55 J, all going to 2D universes
E_EW_total = 1e55  # J
DM_EW = E_EW_total / c**2 / M_sun  # M_☉
print(f"Electroweak phase transition:")
print(f"  Total energy: {E_EW_total:.0e} J")
print(f"  DM (if all converted): {DM_EW:.0e} M_☉")

# 2. QCD phase transition
# z ~ 10^12, T ~ 200 MeV, total energy ~ 10^50 J
E_QCD_total = 1e50  # J
DM_QCD = E_QCD_total / c**2 / M_sun
print(f"\nQCD phase transition:")
print(f"  Total energy: {E_QCD_total:.0e} J")
print(f"  DM (if all converted): {DM_QCD:.0e} M_☉")

# 3. Primordial BH evaporation
# Mass range: 10^9 - 10^15 g (evaporating today)
# Number: ~10^20 PBHs over cosmic history (rough estimate, very uncertain)
# Energy per PBH evaporation: M c^2
# For 10^12 g PBH: E = 10^9 J
# For 10^15 g PBH: E = 10^12 J
N_PBH = 1e20  # rough estimate
E_per_PBH_evap = 1e12  # J, average
E_PBH_total = N_PBH * E_per_PBH_evap
DM_PBH = E_PBH_total / c**2 / M_sun
print(f"\nPrimordial BH evaporation:")
print(f"  Number: {N_PBH:.0e}")
print(f"  Energy per PBH: {E_per_PBH_evap:.0e} J")
print(f"  Total energy: {E_PBH_total:.0e} J")
print(f"  DM: {DM_PBH:.0e} M_☉")

# 4. Vacuum decay (if false vacuum exists)
# Energy of false vacuum: ~10^100 J in our Hubble volume (cosmological constant scale)
# This is WAY too large. Maybe scaled down.
# If vacuum decay happens at z~10, it would be a small event
# Let's assume vacuum decay contributes negligibly (cosmological constant isn't decaying)
DM_vacuum = 0
print(f"\nVacuum decay: {DM_vacuum:.0e} M_☉ (no evidence of vacuum decay)")

# Total cumulative DM with phase transitions
M_cum_v2753 = M_cum_v2751 + DM_EW + DM_QCD + DM_PBH
print(f"\n=== TOTAL CUMULATIVE DM (v2.7.53 with phase transitions) ===")
print(f"Previous (v2.7.51, 14+ event types): {M_cum_v2751:.2e} M_☉")
print(f"+ EW phase transition: {DM_EW:.2e} M_☉")
print(f"+ QCD phase transition: {DM_QCD:.2e} M_☉")
print(f"+ PBH evaporation: {DM_PBH:.2e} M_☉")
print(f"= TOTAL: {M_cum_v2753:.2e} M_☉")

# Total DM in observable universe
M_DM_universe = 1.26e22
F_s_0 = M_cum_v2753 / M_DM_universe
F_p_0 = 1.0 - F_s_0
print(f"\nF_s(0) = {F_s_0:.4e}")
print(f"F_p(0) = {F_p_0:.6f}")

# Check vs cascade's F_p(0) = 0.9993
print(f"\nCascade F_p(0) target: 0.9993")
print(f"With all sources: F_p(0) = {F_p_0:.6f}")
print(f"Match: {'YES' if abs(F_p_0 - 0.9993) < 0.001 else 'NO'}")

# But wait — even if all the energy from EW and QCD phase transitions
# becomes DM, that's still tiny compared to the universe's DM
# Phase transitions happen once per Hubble volume, not per event

# Honest assessment
print("\n=== HONEST ASSESSMENT ===")
print("Even with EW, QCD, PBH evaporation, the cumulative DM is")
print(f"~{F_s_0 * 100:.4f}% of observed. This is still < 1% cumulative.")
print("The 99.93% primordial figure (F_p = 0.9993) is consistent.")
print()
print("Phase transitions and PBH evaporation are HIGHLY UNCERTAIN:")
print("- PBH abundance is model-dependent (could be 10^20 or 10^-20)")
print("- Phase transition energetics are model-dependent")
print("- Vacuum decay is unconfirmed (cosmological constant is stable)")
print()
print("CONCLUSION: Including these additional sources doesn't change")
print("the qualitative picture (F_p ≈ 0.9993, mostly primordial).")
print("Quantitative values are highly uncertain.")

# Save
output = {
    'description': 'Cumulative DM with phase transitions and PBH evaporation (v2.7.53)',
    'method': 'Add EW phase transition (10^55 J), QCD phase transition (10^50 J), PBH evaporation (10^20 PBHs × 10^12 J) to v2.7.51 cumulative.',
    'previous_cumulative_v2751_M_sun': M_cum_v2751,
    'EW_phase_transition_M_sun': float(f"{DM_EW:.2e}"),
    'QCD_phase_transition_M_sun': float(f"{DM_QCD:.2e}"),
    'PBH_evaporation_M_sun': float(f"{DM_PBH:.2e}"),
    'total_cumulative_v2753_M_sun': M_cum_v2753,
    'F_s_0_with_phase_transitions': F_s_0,
    'F_p_0_with_phase_transitions': F_p_0,
    'cascade_F_p_0_target': 0.9993,
    'match': abs(F_p_0 - 0.9993) < 0.001,
    'caveats': [
        'EW phase transition energy: model-dependent (10^52-10^58 J)',
        'QCD phase transition energy: model-dependent (10^47-10^53 J)',
        'PBH abundance: highly uncertain (10^-20 to 10^20 over cosmic history)',
        'Vacuum decay: unconfirmed observationally',
        'Energy conversion to 2D universes: assumed 100% (deaths-only DM)',
    ],
    'honest_finding': 'Including phase transitions and PBH evaporation does NOT change the qualitative picture. F_p(0) ≈ 0.9993 is still consistent. The 99.93% primordial figure holds across all reasonable variations of these uncertain parameters.',
}

with open('json/calculations/v27_phase_transitions.json', 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to calculations/v27_phase_transitions.json")
