"""
v27_recursive_structure.py
===========================

§3.21: The full recursive structure of the cascade.

§3.17-§3.18 established:
- 2D universe proper lifetime: t_Pl,3 in 2D frame
- 3+1D universe proper lifetime: t_Pl,4 in 3+1D frame
- 4D universe proper lifetime: t_Pl,5 (if §3.10 extension)
- Pattern: each level's proper lifetime = next-dim Planck time

This script generalizes the cascade to N dimensions and shows the pattern.
"""

import math
import json

# Planck units at each level
c = 3e8
t_Pl_3 = 5.39e-44  # 3+1D Planck time
M_Pl_3 = 1.22e19   # 3+1D Planck mass (GeV)

# For D dimensions, Planck time scales as:
# t_Pl,D = t_Pl,3 × (M_Pl,3 / M_Pl,D)^(D-4)
# (Generalized Planck units in D dimensions)

# If M_Pl,D is at the cascade's floor (887 GeV) for all D >= 4:
M_Pl_floor = 887  # GeV

# Calculate Planck times at each level
print("=== §3.21: Full recursive structure ===\n")
print("Each level's proper lifetime = next-dimension's Planck time")
print("If M_Pl,D = 887 GeV (floor) for all D >= 4:")
print()

levels = [
    ('0D', 'point', 0, 'no proper time'),
    ('1D', '1D', t_Pl_3 * (M_Pl_3 / M_Pl_floor)**(1-4), '1 Planck time in 1D'),
    ('2D', '2D', t_Pl_3 * (M_Pl_3 / M_Pl_floor)**(2-4), '1 Planck time in 2D'),
    ('3+1D', '3+1D', t_Pl_3, '1 Planck time in 3+1D'),
    ('4D', '4D', t_Pl_3 * (M_Pl_3 / M_Pl_floor)**(4-4), '1 Planck time in 4D'),
    ('5D', '5D', t_Pl_3 * (M_Pl_3 / M_Pl_floor)**(5-4), '1 Planck time in 5D'),
    ('6D', '6D', t_Pl_3 * (M_Pl_3 / M_Pl_floor)**(6-4), '1 Planck time in 6D'),
]

print(f"{'Level':<10} {'D':<8} {'t_Pl,D (s)':<20} {'Proper lifetime':<30}")
print("-" * 70)
for name, dim, t_Pl_D, proper in levels:
    print(f"{name:<10} {dim:<8} {t_Pl_D:<20.2e} {proper:<30}")

print()
print("=== Time dilation factors for various event energies ===\n")
print("If E_4D = 10^69 J (our Big Bang) and 4D has its own universe creation,")
print("4D's proper lifetime is t_Pl,5 = 7.4e-28 s")
print("4D's 5D-frame lifetime = γ_4D × t_Pl,5 = (E_5D/E_Pl,5)^1.29 × t_Pl,5")
print()

# If we assume 5D has the same E_5D ~ 10^69 J for its own Big Bang
E_5D = 1e69  # J (hypothetical 5D event)
E_Pl_5_J = M_Pl_floor * 1.602e-10  # J
t_Pl_5 = t_Pl_3 * (M_Pl_3 / M_Pl_floor)**(5-4)  # s

gamma_4D = (E_5D / E_Pl_5_J) ** 1.29
tau_4D_5D = gamma_4D * t_Pl_5
tau_4D_5D_yr = tau_4D_5D / 3.15e7

print(f"4D universe's 5D-frame lifetime:")
print(f"  E_5D = {E_5D:.0e} J")
print(f"  γ_4D = {gamma_4D:.2e}")
print(f"  τ_4D_5D = {tau_4D_5D_yr:.2e} yr")
print(f"  τ_4D_proper = t_Pl,5 = {t_Pl_5:.2e} s")

print()
print("=== The cascade's full recursive structure ===\n")
print("| Level | D | Proper lifetime | Time dilation | Frame lifetime (yr) |")
print("|-------|---|------------------|---------------|----------------------|")
print("| 0D    | 0 | none | — | — |")
print(f"| 1D    | 1 | {t_Pl_3 * (M_Pl_3 / M_Pl_floor)**(1-4):.2e} s | γ_1D = (E/E_Pl,1)^1.29 | varies |")
print(f"| 2D    | 2 | {t_Pl_3 * (M_Pl_3 / M_Pl_floor)**(2-4):.2e} s | γ_2D = (E/E_Pl,2)^1.29 | 10^-63 to 10^8 (events) |")
print(f"| 3+1D  | 4 | {t_Pl_3:.2e} s | γ_3+1D = (E_4D/E_Pl,4)^1.29 | 2×10^26 (our universe) |")
print(f"| 4D    | 5 | {t_Pl_5:.2e} s | γ_4D = (E_5D/E_Pl,5)^1.29 | {tau_4D_5D_yr:.2e} |")
print(f"| 5D    | 6 | {t_Pl_3 * (M_Pl_3 / M_Pl_floor)**(6-4):.2e} s | γ_5D = (E_6D/E_Pl,6)^1.29 | varies |")
print(f"| ...   | N | t_Pl,N | γ_N = (E/E_Pl,N)^1.29 | varies |")
print()
print("The pattern: same α = 1.29 at every level")
print("The pattern: each level's proper lifetime = next-dim Planck time")
print("The pattern: 'democratic' cosmology at every level")
print()

print("=== Implications ===\n")
print("1. The cascade is naturally recursive")
print("   - The same physics at every level")
print("   - The same α = 1.29 at every level")
print("   - Each level is 'democratic' in its own frame")
print()
print("2. The cone-shape (§2.6) terminates at 4D by default")
print("   - But §3.10 + §3.21 allow extension to N dimensions")
print("   - The pattern continues")
print()
print("3. The 'parent' dimension sees vastly different child lifetimes")
print("   - 3+1D sees 2D universes: 10^-63 s to 10^8 yr")
print("   - 4D sees 3+1D universes: 10^-19 s to 10^40 yr")
print("   - 5D sees 4D universes: ??? to ???")
print("   - Each parent is in awe of its children's lifespans")
print()
print("4. The cascade's framework is GENERAL")
print("   - Not specific to 4D, 3+1D, 2D")
print("   - Applies to any N-dimensional universe")
print("   - The 'universe creation' principle is universal")

results = {
    'pattern': 'Same α = 1.29 at every level',
    'proper_lifetime_rule': 'Each level = next-dim Planck time',
    'levels_analyzed': 7,
    'extension': 'Cascade naturally extends to N dimensions',
    'cone_shape_default': '4D is the top by default, but §3.10/§3.21 allow extension',
    'implication': 'Cascade is a general framework, not specific to 4D-3+1D-2D'
}

with open('v27_recursive_structure.json', 'w') as f:
    json.dump(results, f, indent=2)

print()
print("Results saved to: calculations/v27_recursive_structure.json")
