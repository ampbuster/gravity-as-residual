#!/usr/bin/env python3
"""
v31_f_back_only_3d_to_4d.py
============================

USER CLARIFICATION: f_DE = 10^-85 ONLY makes sense as 3D-to-4D leakage.

The 2D-3D story does NOT have a meaningful f_back because:
  - 2D universe lifetime in 3+1D frame is short (33s for SN, hours-days for larger)
  - During this short lifetime, 2D's gravitational coupling to 3+1D is negligible
  - 2D's contribution to 3+1D happens at DEATH (100% energy return as DM)
  - This is a DEATH RETURN, not a while-alive f_back

The 3D-4D story DOES have a meaningful f_back:
  - 3+1D lifetime is long (13.8 Gyr so far, will be much longer)
  - During this long lifetime, 3+1D's coupling to 4D is meaningful
  - f_DE = 10^-85 is the 3D-to-4D while-alive leakage rate
  - This is a CLOSED LOOP (forward: 4D→3D, backward: 3D→4D)

The two stories are STRUCTURALLY DIFFERENT:
  - 2D-3D: creation by event + death return as DM (no closed loop)
  - 3D-4D: creation + while-alive leakage (closed loop, f_DE = 10^-85)

This is the proper SIDC structure:
  4D event → 3+1D universe (f_back forward = 10^-85)
  3+1D → 4D (closed loop, f_back backward = 10^-85, γ ~ 10^62)
  3+1D events → 2D universes (M^1.29 scaling law)
  2D universe → 3+1D (death return as DM, 100%)
"""

import math

# Setup
t_Pl = 5.391e-44  # s
T_universe = 13.8e9 * 3.156e7  # s
epsilon = 1e-38
gamma = 1e62
M_Pl_4 = 2.22e76  # GeV^4
rho_DE = 2.4e-47  # GeV^4
E_3plus1D = 1e71  # J

# === 3D-4D CYCLE (closed loop) ===
print('='*72)
print('3D-4D CYCLE (closed loop)')
print('='*72)
print()
T_4D_proper = T_universe * epsilon
T_4D_apparent = T_4D_proper * gamma
f_DE = t_Pl / T_4D_apparent

print(f'4D event proper time: {T_4D_proper:.2e} s')
print(f'4D event apparent duration (3+1D frame): {T_4D_apparent:.2e} s = {T_4D_apparent/3.156e7:.2e} yr')
print(f'γ (time dilation): {gamma:.2e}')
print()
print(f'Forward: 4D → 3+1D projection efficiency = f_back = {f_DE:.2e}')
print(f'Backward: 3+1D → 4D leakage rate = f_back = {f_DE:.2e}')
print(f'CLOSED LOOP: same f_back in both directions')
print()
leakage_3D_to_4D = f_DE * E_3plus1D
print(f'Energy leaked from 3+1D to 4D during 13.8 Gyr: {leakage_3D_to_4D:.2e} J')
print(f'Compare to DE total: ~{rho_DE*1e-42*1.1e80:.2e} J (in observable universe)')
print()

# DE formula check
rho_DE_pred = f_DE * epsilon * M_Pl_4
print(f'ρ_DE predicted = f_back × ε × M_Pl^4 = {rho_DE_pred:.2e} GeV^4')
print(f'ρ_DE observed = {rho_DE:.2e} GeV^4')
print(f'Match within: {rho_DE_pred/rho_DE:.3f}x')
print()

# === 2D-3D STORY (death return, NOT a closed loop) ===
print('='*72)
print('2D-3D STORY (death return, NOT a closed loop)')
print('='*72)
print()
print('Various 2D universe lifetimes:')
events = [
    ('LHC p-p', 1e-6, 1e-23),
    ('TDE', 1e-3, 1e38),
    ('Solar flare', 1e3, 1e26),
    ('SN Ia', 33, 1e44),
    ('Hypernova', 3.6e3, 1e46),
    ('BNS merger', 4.3e5*3.156e7, 1e53),
    ('AGN outburst', 1.6e8*3.156e7, 1e55),
]
print(f"{'Event':<15} {'tau_2D (s)':>12} {'E_2D (J)':>12} {'f_DM_leak':>14} {'leakage (J)':>14}")
for name, tau, E in events:
    fb = t_Pl / tau
    leak = fb * E
    print(f"{name:<15} {tau:>12.2e} {E:>12.2e} {fb:>14.2e} {leak:>14.2e}")
print()

print('Note: per 2D universe, leakage during lifetime is at most 0.16 J (SN).')
print('Compare to 2D universe total energy (10^44 J for SN): 0.16 J is 10^-45 of total.')
print('This is NEGLIGIBLE compared to the 100% death return.')
print()
print('The 2D-3D story is NOT a closed loop. It is:')
print('  - 2D universe created by 3+1D event')
print('  - 2D universe lives for tau_2D (M^1.29 scaling law)')
print('  - 2D universe dies, 100% of energy returns to 3+1D as DM')
print('  - No while-alive back-projection worth modeling')
print()

# === Why f_DE = 10^-85 is the 3D-4D cycle only ===
print('='*72)
print('WHY f_DE = 10^-85 IS ONLY 3D-to-4D')
print('='*72)
print()
print('The closed loop requires:')
print('  - f_back is small enough to bridge DE/Planck gap (10^-85)')
print('  - The relevant timescale is long enough for f_back to be meaningful')
print()
print('For 3+1D-to-4D:')
print('  - tau_4D apparent = 10^34 yr (10^24 × universe age)')
print('  - 3+1D has been alive for 13.8 Gyr (very small fraction of tau_4D)')
print('  - f_back = t_Pl/tau_4D = 10^-85 (matches DE)')
print('  - Energy leaked: 10^-14 J (small but not negligible in DE terms)')
print()
print('For 2D-to-3D:')
print('  - tau_2D = 33s (very short)')
print('  - 2D has been alive for 33s (full lifetime)')
print('  - f_back = t_Pl/tau_2D = 10^-45 (NOT 10^-85)')
print('  - Energy leaked: 0.16 J (negligible)')
print()
print('The 10^-85 makes sense ONLY because:')
print('  - 4D event is \"practically eternal\" from 3+1D frame (γ ~ 10^62)')
print('  - This makes tau_4D enormous, f_back tiny')
print('  - The 2D universe is NOT practically eternal from 3+1D frame')
print('  - It dies in 33s, so its \"while-alive\" f_back is huge (10^-45)')
print()
print('='*72)
print('SUMMARY: SIDC STRUCTURE')
print('='*72)
print()
print('SIDC has TWO different cross-dimensional stories:')
print()
print('1. 4D ↔ 3+1D (CLOSED LOOP):')
print('   - 4D event creates 3+1D (forward, f_DE = 10^-85)')
print('   - 3+1D leaks back to 4D (backward, f_DE = 10^-85)')
print('   - DE = f_back × ε × M_Pl^4 (matches observation)')
print('   - γ ~ 10^62 (within cone picture range)')
print()
print('2. 3+1D → 2D (CREATION + DEATH RETURN):')
print('   - 3+1D events create 2D universes (M^1.29 scaling law)')
print('   - 2D universes die, 100% energy returns to 3+1D as DM')
print('   - NO while-alive f_back (lifetimes too short)')
print('   - DM is cumulative 2D universe deaths')
print()
print('These are TWO DIFFERENT physical processes,')
print('both important for the dark sector:')
print('  - DE comes from 3+1D-to-4D closed loop')
print('  - DM comes from cumulative 2D universe deaths')
print()
print('SIDC name: Scale-Invariant Dimensional Cascade')
print('  - Scale-invariant: same α = 1.289 at every level')
print('  - Dimensional: across 4D, 3D, 2D')
print('  - Cascade: hierarchical transitions')
print('  - But f_back is NOT scale-invariant (10^-85 at 3D-4D, 10^-45 at 2D-3D)')
