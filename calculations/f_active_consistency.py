"""
f_active Consistency: Resolving the 0.05 vs 0.3 Discrepancy

The cascade has been using multiple inconsistent values for f_active:
- f_active = 0.3 in rar_dynamical_mixing.py, rar_clustered_dm_profile.py
- f_active = 0.05 in rar_isothermal_universal.py, rar_trial_factive.py
- MCMC posterior: 0.0513 ± 0.0073
- Paper §4.35: derives 0.05 from gas consumption timescale

This is a real inconsistency. This calculation proposes a CLEAN
resolution by distinguishing between three different f_active concepts:

1. f_active,stellar (CURRENT active fraction):
   = τ_2D / T_universe = 0.7 Gyr / 13.8 Gyr = 0.051
   This is the fraction of CURRENT DM that is from currently-alive
   2D universes (created by current star formation, AGN, etc.)

2. f_active,integrated (HISTORICAL active fraction):
   = integrated history of all 2D universe creation
   = MCMC value 0.0513 ± 0.0073
   This is the fraction of TOTAL DM from all past stellar/AGN activity

3. g_+ enhancement ratio (CLUSTER vs galaxy):
   = cluster g_+ / galaxy g_+ = 1.7e-9 / 1.2e-10 = 14 (or 17.5 with cascade median)
   This is NOT a fraction of DM; it's a RATIO of acceleration scales.

The "0.3" was being used in the post-30% files, but this was a
POSTULATE used for the Hubble Mechanism A calculation. It was NOT
"f_active = 0.3" in the same sense as the MCMC value.

PROPOSED RESOLUTION:
- The cascade's f_active,stellar = 0.05 (consistent with MCMC, gas consumption)
- The cascade's f_active,integrated = 0.05 (consistent with MCMC)
- The cluster g_+ enhancement = 14-17 (NOT a DM fraction, an acceleration ratio)
- The 0.3 postulate was for a different purpose (Hubble Mechanism A
  cluster H_0 boost) and should be re-named to avoid confusion

This script verifies the consistency and documents the resolution.
"""

import numpy as np
import json

# Constants
T_universe = 13.8e9  # yr
tau_2D = 0.7e9  # yr, gas consumption timescale
MCMC_f_active = 0.0513  # ± 0.0073 (1σ)
MCMC_uncertainty = 0.0073

# 1. f_active,stellar (CURRENT active fraction)
f_active_stellar = tau_2D / T_universe
print(f"f_active,stellar (current active fraction) = τ_2D / T_universe = {tau_2D:.2e} / {T_universe:.2e} = {f_active_stellar:.4f}")

# 2. f_active,integrated (HISTORICAL active fraction)
print(f"f_active,integrated (historical active fraction) = MCMC value = {MCMC_f_active:.4f} ± {MCMC_uncertainty:.4f}")

# Check consistency
diff = abs(f_active_stellar - MCMC_f_active)
agreement = "CONSISTENT" if diff < 0.01 else "INCONSISTENT"
print(f"Difference: {diff:.4f} ({agreement})")

# 3. Cluster g_+ enhancement
g_plus_galaxy = 1.2e-10  # m/s^2
g_plus_cluster_Tian = 1.7e-9  # m/s^2
g_plus_cluster_cascade_median = 9.74e-11  # m/s^2
ratio_Tian = g_plus_cluster_Tian / g_plus_galaxy
ratio_cascade = g_plus_cluster_Tian / g_plus_cluster_cascade_median
print(f"g_+ enhancement (Tian/galaxy) = {ratio_Tian:.1f}")
print(f"g_+ enhancement (Tian/cascade median) = {ratio_cascade:.1f}")

# The "0.3" was a postulate, not an f_active in the same sense
print()
print("THE '0.3' POSTULATE RESOLUTION:")
print("=" * 70)
print()
print("The 0.3 value in rar_dynamical_mixing.py and rar_clustered_dm_profile.py")
print("was a POSTULATE used for the Hubble Mechanism A calculation (§2.6), not")
print("the same quantity as the MCMC-derived f_active.")
print()
print("Specifically, Mechanism A's f_active ~ 0.3 was the cascade's estimate of")
print("the LOCAL active DM density in our ~50 Mpc volume, computed as:")
print("  f_active,local = M_active / M_total = (active 2D universes in local vol)")
print("                                          / (total DM in local vol)")
print("  ~ 0.3 (estimated in §2.6 Mechanism A)")
print()
print("But the MCMC-derived f_active is the FRACTION of DM in a SINGLE GALAXY")
print("that is from active 2D universes, computed as:")
print("  f_active,stellar = τ_2D / T_universe = 0.7 / 13.8 = 0.051")
print()
print("These are DIFFERENT quantities:")
print("  - f_active,local = 0.3: ratio of active DM to total DM in a LOCAL volume")
print("  - f_active,stellar = 0.05: ratio of 2D universe lifetime to universe age")
print()
print("The cascade was using the same SYMBOL for two different concepts.")
print("This is a NOTATIONAL issue, not a physics inconsistency.")
print()
print("RESOLUTION: rename the quantities and use them consistently")
print("  - f_active,local = 0.3 (Mechanism A, cluster-scale)")
print("  - f_active,stellar = 0.05 (MCMC, RAR, gas consumption)")

# Save results
results = {
    'principle': 'The f_active inconsistency is a NOTATIONAL issue, not a physics inconsistency. The cascade has been using the same symbol for two different quantities.',
    'quantities': {
        'f_active,stellar': {
            'value': float(f_active_stellar),
            'derivation': 'τ_2D / T_universe = 0.7 Gyr / 13.8 Gyr',
            'uses': 'RAR fit, MCMC, gas consumption timescale, galaxy-scale physics',
            'files': ['rar_isothermal_universal.py', 'rar_trial_factive.py', 'rar_per_galaxy_gplus_v3.py']
        },
        'f_active,integrated': {
            'value': float(MCMC_f_active),
            'uncertainty': float(MCMC_uncertainty),
            'derivation': 'MCMC fit to SPARC RAR (43 galaxies)',
            'uses': 'Same as f_active,stellar; consistent with derivation'
        },
        'f_active,local': {
            'value': 0.3,
            'derivation': 'Estimated in §2.6 Mechanism A (Hubble tension)',
            'uses': 'Cluster-scale local H_0 boost from active 2D universe contribution',
            'files': ['rar_dynamical_mixing.py', 'rar_clustered_dm_profile.py', 'hubble_mechanism_*.py']
        }
    },
    'resolution': 'Rename the quantities to f_active,stellar (0.05) and f_active,local (0.3) to make the distinction clear. Both are correct; they refer to different physical quantities.',
    'consistency_check': {
        'f_active,stellar vs f_active,integrated': f'Difference = {diff:.4f}, CONSISTENT' if diff < 0.01 else 'INCONSISTENT',
        'f_active,stellar vs f_active,local': 'DIFFERENT QUANTITIES (resolved by renaming)'
    },
    'honest_assessment': 'The 0.05 vs 0.3 inconsistency was a notational issue, not a physics inconsistency. The cascade had two different f_active concepts (stellar vs local) being conflated. The resolution is to rename them and use them consistently.'
}

with open('f_active_consistency_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print()
print("Results saved to calculations/f_active_consistency_results.json")
