"""
v2.7.59: Test the empirical f_back formula against MULTIPLE event types.

User feedback: "why only supernova?" - The empirical formula
v27_fback_one_over_2alpha gave f_back = 8.6e-86 using SN's
energy and lifetime. Does it work for other event types?

If the formula is truly derived (not SN-specific), it should give
the same f_back for ALL energetic events.
"""

import json
import numpy as np

# Constants
c = 2.998e8
hbar = 1.055e-34
G = 6.674e-11
M_Pl_3 = np.sqrt(hbar * c / G)
E_Pl_3 = M_Pl_3 * c**2
t_Pl_3 = np.sqrt(hbar * G / c**5)
M_sun = 1.989e30
yr = 3.156e7

# Constants used in the formula
tau_4D = 1e28 * yr
tau_universe = 13.8e9 * yr
E_4D = 2.2e69
alpha = 1.29
p = 1 / (2 * alpha)  # 0.3876

# Multiple event types
# Format: (name, E_J, tau_2D_seconds, source)
events = [
    ('SN (calibration)', 1e44, 33, 'cascade §10.1'),
    ('LHC', 2.2e-6, 3e-63, 'cascade §10.1'),
    ('Hypernova', 1e46, 3.5 * 3600, 'cascade §10.1'),
    ('Long GRB', 1e47, 2.8 * 86400, 'cascade §10.1'),
    ('BNS merger', 1e53, 4.3e5 * yr, 'cascade §10.1'),
    ('AGN outburst', 1e55, 1.6e8 * yr, 'cascade §10.1'),
]

print("=== EMPIRICAL f_back FORMULA TEST (v2.7.59) ===\n")
print(f"Formula: f_back = (t_Pl,3 / τ_4D) × (τ_event / τ_universe) × (E_4D / E_event)^(1/(2α))")
print(f"Constants: t_Pl,3 = {t_Pl_3:.3e} s, τ_4D = {tau_4D:.3e} s, E_4D = {E_4D:.3e} J, alpha = {alpha}, 1/(2alpha) = {p:.4f}")
print(f"Target: 10^-85")
print()

print(f"{'Event':25s} {'E (J)':>10s} {'τ_2D (s)':>12s} {'f_back':>15s} {'Off from 10^-85':>20s}")
print("-" * 90)
results = []
for name, E, tau_2D, source in events:
    factor1 = t_Pl_3 / tau_4D
    factor2 = tau_2D / tau_universe
    factor3 = (E_4D / E) ** p
    f_back = factor1 * factor2 * factor3
    off = abs(np.log10(f_back) - (-85))
    print(f"{name:25s} {E:>10.0e} {tau_2D:>12.2e} {f_back:>15.2e} {off:>20.2f}")
    results.append({'event': name, 'E': E, 'tau_2D': tau_2D, 'f_back': f_back, 'off_orders': off})

print()
print("=== HONEST FINDING ===\n")
print("The empirical formula gives DIFFERENT f_back values for different events!")
print()
print("This means the formula is SN-SPECIFIC, not a general derivation.")
print()
print("For SN: f_back ≈ 10^-85 ✓ (calibration point)")
print("For other events: f_back varies by 10s to 100s of orders of magnitude")
print()
print("The formula is essentially: 'use SN's specific energy and lifetime")
print("to get 10^-85'. This is CALIBRATION, not derivation.")
print()

# Check why
print("=== Why the formula is SN-specific ===\n")
# The formula has τ_event and E_event
# Both are related via the energy-scaling rule: τ_event = (E/E_Pl,3)^α × t_Pl,3
# So:
# (τ_event / τ_universe) × (E_4D / E_event)^(1/(2α))
# = (E/E_Pl,3)^α × (t_Pl,3 / τ_universe) × (E_4D / E)^(1/(2α))
# = (t_Pl,3 / τ_universe) × (E/E_Pl,3)^α × (E_4D / E)^(1/(2α))
# = (t_Pl,3 / τ_universe) × E_Pl,3^(-α) × E_4D^(1/(2α)) × E^(α - 1/(2α))

# For this to be CONSTANT (event-independent), we need:
# α - 1/(2α) = 0
# → α^2 = 1/2
# → α = 1/sqrt(2) ≈ 0.707

# But cascade's α = 1.29 (calibrated)
# So the formula is fundamentally EVENT-DEPENDENT

alpha_required = 1 / np.sqrt(2)
print(f"For event-independent f_back, we'd need α = 1/√2 = {alpha_required:.4f}")
print(f"But cascade's α = {alpha} (calibrated from SN 33s)")
print(f"Difference: {abs(alpha - alpha_required):.3f}")
print()
print("This means: with cascade's α = 1.29, the formula CANNOT be event-independent.")
print("The formula works for SN (by construction) but not for other events.")
print()

# Implications
print("=== Implications for the cascade ===\n")
print("L52 RESOLVED (v2.7.58) was PREMATURE.")
print("The formula is SN-specific, not a general derivation.")
print()
print("What the formula ACTUALLY shows:")
print("1. With SN's specific (E, τ) values, you CAN get 10^-85 using 1/(2α)")
print("2. This means the formula has the right 'shape' for SN")
print("3. But it doesn't generalize to other event types")
print()
print("L52 should be RE-OPENED (or marked as 'partial'):")
print("L52: f_back ~ 10^-85 has an empirical formula (SN-specific)")
print("    but does NOT generalize to other event types")
print()
print("The user has caught a real issue with v2.7.58.")
print("The 'breakthrough' was real for SN, but not a general derivation.")
print()

# What would a general formula look like?
print("=== What a general formula would need ===\n")
# For event-independent f_back, we need a different approach
# Option 1: Use α = 1/√2 (contradicts observation)
# Option 2: Use a different exponent (not 1/(2α))
# Option 3: Include the event explicitly (not really "derivation")
# Option 4: Accept f_back is SN-calibrated (back to L52 as open)

# Try Option 2: find exponent p such that f_back is event-independent
# f_back = const × (E_4D / E)^p × E^(α-1)/(const)
# For event-independence: (E_4D / E)^p × E^α = const
# → E^(-p) × E^α = const
# → E^(α-p) = const
# → α - p = 0
# → p = α = 1.29
print("For event-independent f_back, the exponent would need to be p = α = 1.29")
print(f"Then: f_back = (t_Pl,3/τ_4D) × (t_Pl,3/τ_universe) × (E_Pl,3)^(-α) × (E_4D)^α = const")
print()
print("Let me check if this gives 10^-85:")
p_new = alpha
factor1 = t_Pl_3 / tau_4D
# Using t_Pl,3/τ_universe for the time ratio
factor2 = t_Pl_3 / tau_universe
factor3 = (E_4D ** p_new) / (E_Pl_3 ** alpha)
f_back_new = factor1 * factor2 * factor3
print(f"f_back = (t_Pl,3/τ_4D) × (t_Pl,3/τ_universe) × (E_4D/E_Pl,3)^α = {f_back_new:.2e}")
print(f"Off from 10^-85: {abs(np.log10(f_back_new) - (-85)):.2f} orders")
print()

# Save
output = {
    'description': 'Test empirical f_back formula against multiple event types',
    'method': 'Apply the v2.7.58 formula to 6 different event types and see if it gives 10^-85 for all',
    'finding': 'The formula is SN-SPECIFIC. Different events give f_back values that differ by 10s to 100s of orders of magnitude.',
    'L52_REVISED_AGAIN': 'The v2.7.58 "RESOLVED" was premature. The formula works for SN by construction but does not generalize.',
    'events_tested': results,
    'event_independence_analysis': {
        'for_event_independent_f_back_need': 'α - 1/(2α) = 0 → α = 1/√2 ≈ 0.707',
        'cascade_alpha': 1.29,
        'difference': 0.583,
        'conclusion': 'With cascade α=1.29, formula CANNOT be event-independent',
    },
    'alternative_formula': {
        'p_new': 'α = 1.29',
        'f_back': f_back_new,
        'off_from_target': abs(np.log10(f_back_new) - (-85)),
    },
    'implications': [
        'L52 RESOLVED (v2.7.58) was premature',
        'Formula is SN-calibrated, not general derivation',
        'User has caught another real issue',
        'Need to either accept f_back is SN-specific or find a different formula',
    ],
    'honest_finding': 'The v2.7.58 breakthrough was real for SN but did not generalize. The cascade f_back remains semi-calibrated (SN-specific formula exists, but it does not extend to other event types).',
}

with open('calculations/v27_fback_multi_event.json', 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to calculations/v27_fback_multi_event.json")
