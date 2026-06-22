"""
v2.7.50: REVISED F_p(z) analysis with the CORRECT formula and f_back removed.

User corrections (v2.7.50):
1. The cascade's F_p(z) formula is F_p(z) = 0.7 + 0.3 × z²/(z² + z_half²)
   NOT F_p(z) = z²/(z² + z_half²). So F_p(0) = 0.7, not 0.
2. v2.7.11 adopted "deaths-only DM" — f_back has been removed.
   All 2D universe death energy comes back as DM (no f_back loss factor).

Recompute the cumulative DM contribution with these corrections:
- f_back = 1 (all SN energy becomes 2D universe)
- All 2D universe energy comes back as DM after τ_2D
- DM per SN = E_SN / c²

Cumulative DM from SN deaths in MW:
- N_SN = 5e8 over 10 Gyr
- E_SN = 10^44 J per SN
- DM per SN = 5.6e-4 M_☉
- Total = 5e8 × 5.6e-4 = 2.8e5 M_☉

F_s(0) = 0.3 → 30% of DM should be cumulative = 0.3 × Ω_DM × ρ_crit
= 0.3 × 0.265 × ρ_crit × V (volume integrated)

The cumulative calculation gives 2.8e5 M_☉ for MW.
Observed MW DM ~ 10^12 M_☉.
0.3 × 10^12 = 3e11 M_☉ expected from F_s = 0.3.

Inconsistency: 3e11 (expected from F_s=0.3) vs 2.8e5 (calculated from SN deaths)
Off by factor of 10^6.

So the F_p(z) function says 30% cumulative, but SN deaths can only supply
0.00003% of the observed DM. The F_s = 0.3 component is too large by
a factor of ~10^6.


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

# Cascade parameters
n_hill = 2.0
z_half = 3.0
f_p_0 = 0.7  # F_p(0)
E_SN = 1e44  # J
c = 2.998e8
M_sun = 1.989e30

def F_p(z):
    """CORRECT F_p(z) formula (v2.7.5+): F_p(0) = 0.7, F_p(∞) = 1.0"""
    return f_p_0 + (1 - f_p_0) * z**n_hill / (z_half**n_hill + z**n_hill)

def F_s(z):
    return 1.0 - F_p(z)

# Print F_p values
print("=== CORRECTED F_p(z) (v2.7.5+ formula) ===\n")
print(f"{'z':>8s} {'F_p(z)':>10s} {'F_s(z)':>10s}")
print("-" * 40)
for z in [0, 0.5, 1, 2, 3, 5, 10, 100, 1100]:
    print(f"{z:>8.1f} {F_p(z):>10.4f} {F_s(z):>10.4f}")

# Cumulative DM calculation
print("\n=== Cumulative DM from SN deaths (no f_back, v2.7.11 deaths-only) ===\n")

# DM per SN
DM_per_SN_kg = E_SN / c**2
DM_per_SN_M_sun = DM_per_SN_kg / M_sun
print(f"DM per SN: E_SN / c² = {DM_per_SN_M_sun:.2e} M_☉")

# For MW
N_SN_MW = 5e8
M_DM_cumulative_MW = N_SN_MW * DM_per_SN_M_sun
print(f"MW cumulative DM: {N_SN_MW:.0e} SN × {DM_per_SN_M_sun:.2e} M_☉ = {M_DM_cumulative_MW:.2e} M_☉")

# Comparison to F_s = 0.3 expectation
M_DM_total_MW = 1e12  # observed MW DM
M_DM_expected_Fs03 = F_s(0) * M_DM_total_MW
print(f"F_s(0) × M_DM_total_MW = 0.3 × 10^12 = {M_DM_expected_Fs03:.2e} M_☉ (expected from F_s=0.3)")

ratio = M_DM_expected_Fs03 / M_DM_cumulative_MW
print(f"\nInconsistency: expected / calculated = {ratio:.2e}")
print(f"SN deaths produce {ratio:.0e} times LESS DM than F_s(0)=0.3 requires")

# Find the F_s(0) that's consistent with SN deaths
F_s_required = M_DM_cumulative_MW / M_DM_total_MW
F_p_required = 1.0 - F_s_required
print(f"\nFor consistency, F_s(0) should be: {F_s_required:.2e}")
print(f"And F_p(0) should be: {F_p_required:.10f}")
print(f"\nThis means F_p(0) should be ~1.0 (essentially ALL DM is primordial),")
print(f"NOT 0.7 (with 30% cumulative).")

# Save
output = {
    'description': 'REVISED F_p(z) analysis with correct formula and f_back removed',
    'user_corrections': [
        'F_p(z) = 0.7 + 0.3 * z²/(z² + z_half²), not z²/(z² + z_half²). F_p(0) = 0.7, not 0.',
        'v2.7.11 deaths-only DM: f_back removed, all 2D universe death energy comes back as DM'
    ],
    'method': 'With f_back=1, DM per SN = E_SN/c². Cumulative DM = N_SN × E_SN/c².',
    'cascade_F_p_formula': 'F_p(z) = 0.7 + 0.3 × z^n/(z^n + z_half^n), n=2, z_half=3',
    'cumulative_dm_per_SN_M_sun': float(f"{DM_per_SN_M_sun:.2e}"),
    'cumulative_dm_MW_M_sun': float(f"{M_DM_cumulative_MW:.2e}"),
    'expected_dm_from_Fs_0.3_M_sun': float(f"{M_DM_expected_Fs03:.2e}"),
    'inconsistency_factor': float(f"{ratio:.2e}"),
    'revised_F_p_required': {
        'F_p_0_required': float(f"{F_p_required:.10f}"),
        'F_s_0_required': float(f"{F_s_required:.2e}"),
        'interpretation': 'Cascade F_p(z) should be ~1.0 at z=0 (almost all DM is primordial), not 0.7 (with 30% cumulative). The 30% cumulative cannot be supported by SN deaths alone.'
    },
    'revised_L50': {
        'old_L50_v2.7.49': 'F_p(0) = 0 makes cascade predict Ω_DM(z=0) ≈ 0 (WRONG FORMULA)',
        'revised_L50_v2.7.50': 'Cascade F_p(0) = 0.7 (70% primordial) implies F_s(0) = 0.3 (30% cumulative). But SN deaths can only produce 2.8e5 M_☉ cumulative, not 3e11 M_☉ required. Off by 10^6. Either F_p(0) should be ~1.0 (almost all primordial), or the cumulative mechanism needs revision.',
    },
    'implications': {
        'option_1': 'F_p(0) → 1.0: Almost all DM is primordial (from 4D event). Cumulative component is negligible. This is consistent with SN death calculations.',
        'option_2': 'Cumulative mechanism is more efficient than f_back × E_SN: e.g., AGN, BNS, GRB deaths are much more efficient DM producers than SN. Need to re-derive cumulative DM with all event types.',
        'option_3': 'Primordial component is not just from 4D event: there are also early-universe 2D universe deaths (e.g., from inflation-era events) that contribute to primordial DM. This could lower the F_s required.'
    },
    'honest_finding': 'The user identified a real issue with v2.7.49 (wrong F_p formula). The corrected F_p(z) = 0.7 + 0.3×z²/(z²+9) does have F_p(0) = 0.7, so v2.7.49 was over-stating the issue. But the F_s(0) = 0.3 component is still inconsistent with SN death calculations by a factor of 10^6. The cascade should revise F_p(0) to be closer to 1.0, or account for the cumulative component with additional event types.',
}

with open('json/calculations/v27_fp_z_v2.json', 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to calculations/v27_fp_z_v2.json")
