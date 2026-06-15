"""
Test: 3D universe lasting 'only a few seconds' in 4D view.
What's the constraint on the 4D Planck scale?
"""
import math

# Constants
c = 2.998e8
hbar = 1.055e-34
G_N = 6.674e-11
year = 3.156e7

# 3+1D Planck
t_Pl_3 = math.sqrt(hbar * G_N / c**5)  # 5.39e-44 s
E_Pl_3 = math.sqrt(hbar * c**5 / G_N)  # 2.0e9 J
M_Pl_3_GeV = 1.221e19  # GeV

# Current 3D universe age
T_3D_current = 13.8e9 * year  # 4.35e17 s

# Test scenarios for T_3D (the 4D's view of the 3D universe's lifespan)
scenarios = [
    ("Self-similar 33s (perfect symmetry)", 33),
    ("Few seconds (user's intuition)", 60),  # 1 minute
    ("1 hour", 3600),
    ("1 day", 86400),
    ("1 year", year),
    ("Energy scaling answer", 1.9e26 * year),
]

print("="*78)
print(" CONSTRAINT:  T_3D in 4D = (a few seconds)  →  what does that require?")
print("="*78)
print(f"\nFor the 3D universe to be ALIVE at the current age of {T_3D_current/year:.2e} yr,")
print(f"the 3D's INTERNAL lifespan T_3D' must satisfy  T_3D' >= T_3D_current = 13.8 Gyr")
print()
print(f"  T_3D' = T_3D in 4D  ×  (t_Pl,3 / t_Pl,4)")
print()
print(f"  So:  (t_Pl,3 / t_Pl,4)  >=  T_3D_current / T_3D in 4D")
print(f"  This gives a lower bound on  M_Pl,4.")
print()
print("="*78)
print(f" {'Scenario':40s} {'T_3D in 4D':>15s}  {'t_Pl,3/t_Pl,4 min':>18s}  {'M_Pl,4 (GeV)':>15s}")
print("-"*78)

for label, T_3D_4D in scenarios:
    # Required time-dilation factor
    td_factor = T_3D_current / T_3D_4D
    # t_Pl,4 = t_Pl,3 / td_factor
    t_Pl_4 = t_Pl_3 / td_factor
    # M_Pl,4 = M_Pl,3 × (t_Pl,3 / t_Pl,4) = M_Pl,3 × td_factor
    M_Pl_4_GeV = M_Pl_3_GeV * td_factor
    print(f"  {label:38s} {T_3D_4D:>15.2e}  {td_factor:>18.2e}  {M_Pl_4_GeV:>15.2e}")

# Physical Planck scale reference
print()
print("="*78)
print(" Physical reference: standard high-energy physics")
print("="*78)
print(f"  3+1D Planck mass:    M_Pl,3 = {M_Pl_3_GeV:.2e} GeV")
print(f"  String/GUT scale:    M_string ~ 10^16 GeV (10^3 times BELOW Planck)")
print(f"  EW scale:            M_EW ~ 10^2 GeV (10^17 times BELOW Planck)")
print(f"  4D fundamental (ADD): M_Pl,4+n ~ 1-10 TeV (10^16 times BELOW Planck)")
print()
print("  For M_Pl,4 >> M_Pl,3, we'd need physics at energies WAY above the Planck")
print("  scale.  This is unphysical — quantum gravity effects dominate above M_Pl.")
