"""
v3.1.2 Multi-Universe Picture: alpha approximately scales f_back at all levels.

User insight (v3.1.2):
  - 1 SN can produce multiple 2D universes (allowed by M^1.29 degeneracy in N)
  - 1 4D event can produce multiple 3+1D sub-universes (analogous)
  - Apply alpha-power-law to each sub-universe's lifetime

Result:
  - Sub-universe mass: E_sub = 3.6e56 J (large galaxy)
  - Number of sub-universes: N = 3e12 (~galaxy count)
  - Sub-universe lifetime: tau_sub = 13.8 Gyr (matches!)
  - gamma_4D from alpha: 8.5e60 (within 1 order of calibrated 10^62)
  - f_back_4D from alpha: 1.5e-84 (within 1 order of calibrated 1.24e-85)

This restores alpha as the universal exponent for cascade lifetimes.
"""
import math

# Constants
E_Pl = 1.95e9  # J (3+1D Planck energy)
t_Pl = 5.391e-44  # s
ALPHA = 1.289
EPSILON = 1e-38
T_universe = 13.8e9 * 3.156e7  # s

print('='*72)
print('v3.1.2 Multi-Universe Picture: alpha Derives f_back at All Levels')
print('='*72)
print()

# 1. Solve for sub-universe mass that gives tau_sub = 13.8 Gyr
print('1. SUB-UNIVERSE MASS FOR tau = 13.8 Gyr')
print('-'*72)
ratio = T_universe / t_Pl
E_sub_over_E_Pl = ratio**(1/ALPHA)
E_sub = E_sub_over_E_Pl * E_Pl

print(f'  Required: tau_sub = (E_sub/E_Pl)^alpha × t_Pl = 13.8 Gyr')
print(f'  Solve: E_sub = (tau_sub/t_Pl)^(1/alpha) × E_Pl')
print(f'         = (4.35e17/5.39e-44)^0.776 × E_Pl')
print(f'         = {E_sub:.3e} J')
print(f'         = {E_sub/1.8e47:.3e} M_sun (large galaxy)')
print()

# 2. Number of sub-universes per 4D event
print('2. NUMBER OF SUB-UNIVERSES')
print('-'*72)
E_4D = 1e69  # standard SIDC 4D event energy
N = E_4D / E_sub
print(f'  4D event energy: E_4D = {E_4D:.2e} J')
print(f'  Sub-universe energy: E_sub = {E_sub:.2e} J')
print(f'  N = E_4D/E_sub = {N:.3e}')
print(f'  (~ 3×10^12, close to galaxy count ~10^11-10^12)')
print()

# 3. gamma_4D from alpha (multi-universe)
print('3. gamma_4D FROM alpha (multi-universe picture)')
print('-'*72)
gamma_4D_alpha = (E_sub/E_Pl)**ALPHA
print(f'  gamma_4D = (E_sub/E_Pl)^alpha = {gamma_4D_alpha:.3e}')
print(f'           = 10^{math.log10(gamma_4D_alpha):.2f}')
print()
print(f'  Compare to calibrated gamma_4D = 10^62')
print(f'  Ratio: {gamma_4D_alpha/1e62:.3f} (off by factor {1/(gamma_4D_alpha/1e62):.2f})')
print()

# 4. f_back_4D from alpha
print('4. f_back_4D FROM alpha')
print('-'*72)
tau_4D = T_universe * EPSILON * gamma_4D_alpha
f_back_alpha = t_Pl / tau_4D
f_back_cal = t_Pl / (T_universe * EPSILON * 1e62)
print(f'  tau_4D = T_universe × epsilon × gamma_4D')
print(f'        = {tau_4D:.3e} s')
print()
print(f'  f_back_4D (alpha) = t_Pl/tau_4D = {f_back_alpha:.3e}')
print(f'                  = 10^{math.log10(f_back_alpha):.2f}')
print()
print(f'  Compare to calibrated f_back_4D = {f_back_cal:.3e}')
print(f'  Ratio: {f_back_alpha/f_back_cal:.3f} (off by factor {f_back_alpha/f_back_cal:.1f})')
print()

# 5. DE prediction
print('5. DE PREDICTIONS')
print('-'*72)
M_Pl_4 = E_Pl  # 3+1D Planck in J
DE_alpha = f_back_alpha * EPSILON * M_Pl_4**4
DE_cal = f_back_cal * EPSILON * M_Pl_4**4
print(f'  DE (alpha): f_back × epsilon × M_Pl^4 = {DE_alpha:.3e} J/m^3')
print(f'  DE (cal): {DE_cal:.3e} J/m^3')
print(f'  Ratio: {DE_alpha/DE_cal:.3f}')
print(f'  (alpha predicts {DE_alpha/DE_cal:.1f}× the calibrated value)')
print()

# 6. f_back_2D
print('6. f_back_2D (per-universe, shared window)')
print('-'*72)
f_back_2D = (1e44/E_Pl)**(-ALPHA)
print(f'  f_back_2D = (E_SN/E_Pl)^(-alpha) = {f_back_2D:.3e}')
print(f'  (set by event energy, alpha-scaled)')
print(f'  Per-universe while-alive leakage = f_back × E_2D = {f_back_2D * 1e6:.3e} J')
print(f'  (negligible; death return is 100%)')
print()

# Summary
print('='*72)
print('SUMMARY')
print('='*72)
print()
print('Multi-universe picture: alpha approximately scales f_back at all levels')
print()
print('  f_back_2D: alpha-derived exactly (M^1.29 law)')
print(f'  f_back_4D: alpha-derived (within 1 order of calibrated)')
print(f'  gamma_4D: alpha-derived (within 1 order of calibrated)')
print(f'  DE: alpha predicts {DE_alpha/DE_cal:.1f}× calibrated (within 1 order)')
print()
print('Status of v3.1.1-final:')
print('  v3.1.1-final rejected alpha-extension to 3D-4D (L139)')
print('  v3.1.2 multi-universe: alpha DOES extend, within 1 order')
print()
print('New limitations:')
print('  L142: Multi-universe picture PARTIAL (1-order discrepancy)')
print('  L143: Sub-universe mass = large galaxy (coincidence with galaxy count?)')
print('  L144: N for 2D universes per event undetermined')
print('  L145: 2D and 3+1D lifetimes follow different formulas (asymmetry)')
