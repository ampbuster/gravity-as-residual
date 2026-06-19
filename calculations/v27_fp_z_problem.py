"""
v2.7.49: User identified a real inconsistency in the cascade's F_p(z) model.

Cascade's F_p(z) (v2.7.5+):
  F_p(z) = z^n / (z^n + z_half^n), n=2, z_half=3
  F_s(z) = 1 - F_p(z)
  r(z) = (1+z)^3 × F_p(z) + F_s(z)
  Where r(z) is the ratio of DM density at z to DM density at z=0

The problem:
  At z=0: F_p(0) = 0, F_s(0) = 1
  So r(0) = 1 × 0 + 1 = 1 ✓
  But r(z) decomposes as:
    r(z) = (1+z)^3 × F_p(z)  [primordial component]
         + F_s(z)             [recent component]
  At z=0: primordial contribution = 0, recent contribution = 1
  But the recent component is f_back × SN deaths ≈ 10^-91 × M_b
  This is NEGLIGIBLE compared to observed Ω_DM = 0.265!

So the cascade's F_p(z) model predicts Ω_DM(z=0) ≈ 0, but
observation gives 0.265. This is a REAL INCONSISTENCY in the cascade.

Possible fixes:
1. F_p(z=0) should be NON-ZERO (a constant floor)
2. The "recent" component should be much larger than f_back × SN
3. There should be a third component (e.g., constant DM)
"""

import json
import numpy as np

# Hill function
n_hill = 2.0
z_half = 3.0

def F_p(z, n=2.0, z_h=3.0):
    return z**n / (z**n + z_h**n)

def F_s(z, n=2.0, z_h=3.0):
    return 1.0 - F_p(z, n, z_h)

def r_z(z):
    """Cascade's r(z)"""
    return (1+z)**3 * F_p(z) + F_s(z)

# Print the issue
print("=== CASCADE F_p(z) INCONSISTENCY (USER IDENTIFIED, v2.7.49) ===\n")
print(f"{'z':>8s} {'F_p(z)':>10s} {'F_s(z)':>10s} {'(1+z)^3*F_p':>15s} {'F_s alone':>12s} {'r(z)':>10s}")
print("-" * 80)
for z in [0, 0.5, 1, 2, 3, 5, 10, 100, 1100]:
    Fp = F_p(z)
    Fs = F_s(z)
    prim = (1+z)**3 * Fp
    rec = Fs
    r = r_z(z)
    print(f"{z:>8.1f} {Fp:>10.4f} {Fs:>10.4f} {prim:>15.2e} {rec:>12.4f} {r:>10.2e}")

print("\n=== THE PROBLEM ===")
print("At z=0:")
print("  F_p(0) = 0  → primordial component is ZERO")
print("  F_s(0) = 1  → all DM should be 'recent' (from SN deaths)")
print("  But recent DM = f_back × SN deaths = 10^-85 × M_SN_energy / c^2")
print("  For MW (M_b ~ 5e10 M_☉, N_SN ~ 5e8):")
print("    M_recent = 10^-85 × 5e8 × 10^44 / (3e8)^2 = 5.6e-80 M_☉")
print("    Ω_DM_recent ≈ 5.6e-80 / 5e10 = 10^-90 (NEGLIGIBLE)")
print("  But OBSERVATION: Ω_DM(z=0) = 0.265")
print("  CASCADE PREDICTS: Ω_DM(z=0) ≈ 0 (from F_s)")
print("  INCONSISTENCY: cascade is off by ~10^90!")

# Possible fixes
print("\n=== POSSIBLE FIXES ===\n")

# Fix 1: Add a constant floor to F_p
print("Fix 1: F_p(z=0) = ε, where ε ≈ 0.5-0.9 (constant floor)")
print("  This means most DM at z=0 is primordial (not recent)")
print("  F_p(0) ≠ 0, e.g., F_p(z) = ε + (1-ε) × z^n / (z^n + z_half^n)")
print("  But this is ad hoc; not derived from first principles")

# Fix 2: The recent component is much larger
print("\nFix 2: Recent DM is much larger than f_back × SN deaths")
print("  Maybe f_back is wrong (SN 33s calibration is wrong)")
print("  Or there's a different mechanism for 'recent' DM")
print("  But f_DE ~ 10^-85 is well-calibrated from SN 33s lifetime (L9)")

# Fix 3: Add a third component (constant DM)
print("\nFix 3: Add a third (constant) DM component")
print("  DM = F_p × DM_primordial + F_s × DM_recent + DM_constant")
print("  Where DM_constant ~ 0.265 (today, constant in absolute terms)")
print("  This is a 'hidden' third component that the cascade doesn't derive")

# Comparison to observations
print("\n=== COMPARISON TO OBSERVATIONS (Planck 2018) ===\n")
print("Observation: Ω_DM = 0.265 at z=1100 (CMB) and z=0 (today)")
print("Ω_DM is approximately constant across all z (matter-like dilution)")
print()
print("Cascade prediction (current F_p model):")
print("  At z=1100: r(1100) ~ 1.33e9, so Ω_DM/Ω_total = Ω_DM_0 × r(1100) / total(1100)")
print("    = 0.265 × 1.33e9 / ~10^12 (radiation-dominated) ~ 10^-4")
print("    BUT OBSERVATION: Ω_DM = 0.265 at z=1100")
print("  INCONSISTENCY: cascade over-predicts DM at z=1100 by factor ~10^3")
print()
print("OR alternative interpretation:")
print("  r(z) is the ratio of DM density to Ω_DM_0 (not the absolute density)")
print("  Then r(1100) × Ω_DM_0 = Ω_DM(1100) absolute")
print("  But Ω_DM(1100) absolute = Ω_DM_total × (1+1100)^3 = 0.265 × 1.33e9 = 3.5e8")
print("  This is much bigger than total density at z=1100, so unphysical")

# Save
output = {
    'description': 'User-identified inconsistency in cascade F_p(z) model',
    'method': 'Cascade F_p(z) = z^n/(z^n+z_half^n), n=2, z_half=3. r(z) = (1+z)^3 * F_p + F_s. At z=0, F_p(0)=0, F_s(0)=1.',
    'problem': 'Cascade predicts Ω_DM(z=0) ≈ 0 (since F_s component is f_back × SN deaths ≈ 10^-91 × M_b), but observation gives Ω_DM(z=0) = 0.265. INCONSISTENCY of ~10^90.',
    'problem_alt': 'Alternative interpretation: r(z) gives ratio of DM density to today. At z=1100, r=1.33e9, so DM(1100)/DM(0) = 1.33e9. But if DM(0) = 0.265 (absolute), then DM(1100) = 3.5e8, which is more than total density at z=1100. UNPHYSICAL.',
    'three_possible_fixes': {
        'fix_1_constant_floor': 'F_p(z=0) = ε ≈ 0.5-0.9 (constant primordial floor). Ad hoc, not derived.',
        'fix_2_recent_larger': 'Recent DM is much larger than f_back × SN. But f_back is calibrated from SN 33s lifetime.',
        'fix_3_third_component': 'Add constant DM component (DM_constant ~ 0.265). Hidden parameter, not derived.',
    },
    'honest_finding': 'The cascade F_p(z) model has a real inconsistency. The model needs revision. This is a new honest limitation (L50).',
    'implications_for_observation': {
        'observed_DE_density': 'Approximately constant (consistent with ΛCDM w=-1)',
        'observed_DM_density': 'Approximately (1+z)^3 × Ω_DM_0 (matter-like dilution)',
        'observed_Ω_DM': 'Constant at 0.265 across all z (Planck 2018)',
        'cascade_match': 'Cascade agrees with observation qualitatively (DM dilutes as (1+z)^3, Ω_DM ~ constant) but quantitatively wrong at z=0 (predicts ~0 instead of 0.265).',
    },
    'next_steps': 'L50 added: cascade F_p(z) model has internal inconsistency. The user identified this by asking a simple observational question. The fix requires a new parameter (F_p(0) floor or constant DM component) that the cascade should derive from first principles.',
}

with open('json/calculations/v27_fp_z_problem.json', 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to calculations/v27_fp_z_problem.json")
