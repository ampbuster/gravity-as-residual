"""
v3.1.2 Multi-Universe Picture: alpha approximately scales f_back at all levels.

User insight (v3.1.2):
  - 1 SN can produce multiple 2D universes (allowed by M^1.29 degeneracy in N)
  - 1 4D event can produce multiple 3+1D sub-universes (analogous)
  - Apply alpha-power-law to each sub-universe's lifetime

Result:
  - Sub-universe mass: E_sub = 3.6e56 J = 2e9 M_sun (small/dwarf galaxy)
  - Number of sub-universes: N = 3e12 (~galaxy count)
  - Sub-universe lifetime: tau_sub = 13.8 Gyr (matches!)
  - gamma_4D = 4pi × gamma_sub = 1.015e62 (within 1.5% of calibrated 10^62)
  - f_DE = 1.22e-85 (within 1.7% of calibrated 1.24e-85)

v3.1.2 FINAL: alpha_cal = 1.289 (Interpretation A only)
  - Interpretation B (alpha_true = 1.258 with 4pi hidden) was tested and
    REJECTED by the 14-event M^1.29 fit. See §3.60.4 in paper for details.
  - This script preserves the historical calculation for traceability.
                      E_sub = AVERAGE galaxy, 9D = v_Higgs off by 14%

The 4pi factor can be placed in TWO ways. Both interpretations are presented.
"""
import math

# Constants
E_Pl = 1.95e9  # J (3+1D Planck energy)
t_Pl = 5.391e-44  # s
ALPHA_CAL = 1.289
ALPHA_TRUE = 1.258
EPSILON = 1e-38
T_universe = 13.8e9 * 3.156e7  # s

print('='*72)
print('v3.1.2 Multi-Universe Picture (DUAL FRAMING)')
print('='*72)
print()

# ============================================================
# INTERPRETATION A: alpha_cal = 1.289 (4pi explicit at 3D->4D)
# ============================================================
print('='*72)
print('INTERPRETATION A: alpha_cal = 1.289 (4pi at 3D->4D only)')
print('='*72)
print()

ratio_A = T_universe / t_Pl
E_sub_A = ratio_A**(1/ALPHA_CAL) * E_Pl
gamma_sub = T_universe / t_Pl
gamma_4D_A = 4 * math.pi * gamma_sub
f_back_A = t_Pl / (T_universe * EPSILON * gamma_4D_A)

print(f'Sub-universe mass (alpha_cal):')
print(f'  E_sub = (T_universe/t_Pl)^(1/alpha_cal) × E_Pl = {E_sub_A:.3e} J')
print(f'        = {E_sub_A/1.8e47:.3e} M_sun (small/dwarf galaxy)')
print()
print(f'gamma_4D = 4pi × gamma_sub = 4pi × T_universe/t_Pl = {gamma_4D_A:.3e}')
print(f'f_DE = {f_back_A:.3e}')
print(f'Calibrated: 1.24e-85, off by {(f_back_A/1.24e-85 - 1)*100:.2f}%')
print()

# 9D = v_Higgs check
M_Pl_4_GeV = 887
M_Pl_9_A = M_Pl_4_GeV / ALPHA_CAL**5
print(f'9D Planck: M_Pl,9 = 887 / alpha^5 = {M_Pl_9_A:.1f} GeV')
print(f'v_Higgs = 246 GeV, off by {(M_Pl_9_A/246 - 1)*100:.2f}%')
print()

# ============================================================
# INTERPRETATION B: alpha_true = 1.258 (4pi hidden in alpha)
# ============================================================
print('='*72)
print('INTERPRETATION B: alpha_true = 1.258 (4pi hidden in alpha at 2D->3D)')
print('='*72)
print()

E_sub_B = ratio_A**(1/ALPHA_TRUE) * E_Pl
gamma_4D_B = 4 * math.pi * gamma_sub
f_back_B = t_Pl / (T_universe * EPSILON * gamma_4D_B)

print(f'Why alpha_true?')
print(f'  If M^1.29 has 4pi factor: tau = 4pi × (E/E_Pl)^alpha_true × t_Pl')
print(f'  Calibrated alpha includes 4pi, so:')
print(f'  alpha_true = log(33/(4pi × t_Pl))/log(E_SN/E_Pl) = {ALPHA_TRUE}')
print()
print(f'Sub-universe mass (alpha_true):')
print(f'  E_sub = (T_universe/t_Pl)^(1/alpha_true) × E_Pl = {E_sub_B:.3e} J')
print(f'        = {E_sub_B/1.8e47:.3e} M_sun (AVERAGE galaxy)')
print()
print(f'gamma_4D = 4pi × gamma_sub = {gamma_4D_B:.3e}')
print(f'f_DE = {f_back_B:.3e}')
print(f'Calibrated: 1.24e-85, off by {(f_back_B/1.24e-85 - 1)*100:.2f}%')
print()

M_Pl_9_B = M_Pl_4_GeV / ALPHA_TRUE**5
print(f'9D Planck: M_Pl,9 = 887 / alpha^5 = {M_Pl_9_B:.1f} GeV')
print(f'v_Higgs = 246 GeV, off by {(M_Pl_9_B/246 - 1)*100:.2f}%')
print()

# ============================================================
# COMPARISON
# ============================================================
print('='*72)
print('COMPARISON: INTERPRETATION A vs B')
print('='*72)
print()
print(f'{"Property":<30} {"A (alpha_cal)":<20} {"B (alpha_true)":<20}')
print('-'*72)
print(f'{"alpha":<30} {ALPHA_CAL:<20} {ALPHA_TRUE:<20}')
print(f'{"alpha = 1 + 1/sqrt(N)":<30} {"N=12 (SM)":<20} {"N=15 (no clean N)":<20}')
print(f'{"E_sub (M_sun)":<30} {E_sub_A/1.8e47:<20.2e} {E_sub_B/1.8e47:<20.2e}')
print(f'{"Galaxy identification":<30} {"small/dwarf":<20} {"AVERAGE":<20}')
print(f'{"9D = v_Higgs match":<30} {"1.3%":<20} {"14%":<20}')
print(f'{"f_DE match":<30} {"1.7%":<20} {"1.7%":<20}')
print(f'{"4pi at 2D->3D?":<30} {"NO":<20} {"YES (hidden)":<20}')
print(f'{"4pi at 3D->4D?":<30} {"YES":<20} {"YES":<20}')
print()

# Summary
print('='*72)
print('SUMMARY (DUAL FRAMING)')
print('='*72)
print()
print('Both interpretations are mathematically valid.')
print('They differ in WHERE the 4pi factor is placed:')
print('  A: 4pi explicit at 3D->4D (gamma_4D = 4pi × gamma_sub)')
print('  B: 4pi hidden in alpha at 2D->3D (alpha_true = 1.258)')
print()
print('Trade-offs:')
print('  A optimizes: 9D = v_Higgs match (1.3%), alpha = 1 + 1/sqrt(12) (SM)')
print('  B optimizes: average galaxy identification, geometric consistency')
print()
print('The "true" alpha depends on which structural feature is more fundamental.')
print('Both are presented honestly in v3.1.2.')
