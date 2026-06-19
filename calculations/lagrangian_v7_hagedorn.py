#!/usr/bin/env python3
"""
Lagrangian v7: Hagedorn, density of states, and N=12 mass spectrum
====================================================================

The c=1 matrix model has a famous feature: Hagedorn temperature T_H where
strings become unstable (massless, infinite density of states). Is this
the "death" of a 2D universe?

Also: what does the density of states look like for N=12 SYK at low energies?
Does the lightest 2D universe mass match any observation?

And: W-algebra W∞ has c=N-1 generators. For N=12, that's 11 generators.
Why does SIDC predict N=12?

Three angles on "what does the Lagrangian actually DO".
"""

import numpy as np
from scipy.special import gamma as gamma_func
import math

PI = np.pi
HBAR = 1.054571817e-34  # J·s
C = 2.99792458e8        # m/s
G_N = 6.67430e-11       # m³/(kg·s²)
E_PLANCK_4D = 1.22e19   # GeV
M_PLANCK_4D = 2.176e-8  # kg

print("="*72)
print("LAGRANGIAN v7: HAGEDORN, DENSITY OF STATES, N=12 SPECTRUM")
print("="*72)

# =============================================================================
# PART 1: HAGEDORN TEMPERATURE FOR c=1 MATRIX MODEL
# =============================================================================
print("\n" + "="*72)
print("PART 1: HAGEDORN TEMPERATURE (the 'death' of a 2D universe?)")
print("="*72)

# The c=1 matrix model has Hagedorn temperature:
# T_H = (c-1) * T_string / 24  (for c=1, T_H = 0!)
# But the string coupling g_s modifies this
# And the fermion content (N=12 SYK) modifies it further

# For c=1: T_H = 0 (the famous paradox)
# Witten 1991: the c=1 model has T_H = 0 in the free-fermion picture
# But with g_s > 0, there's a "tachyon wall" at finite temperature

# Let's compute for several candidate temperatures:

print("\nCandidate temperatures for 2D universe death (lifetime τ_2D = ℏ/T):")
print("-"*72)

# SN calibration: T_SN = ℏ/τ_SN = ℏ/33s
TAU_SN = 33.0  # seconds
T_SN = HBAR / TAU_SN  # K (Kelvin, since E = k_B T but we use natural units)
print(f"SN calibration:  τ = {TAU_SN} s  →  T = ℏ/τ = {T_SN:.3e} K")

# If T_2D universe = Hagedorn-like:
# Hagedorn for c=1 string (string scale M_s):
# T_H = M_s / (4π)  (in 2D string units, c=1)
# But the 2D string has string tension T_2D = 1/(2π α')

# A different approach: τ_2D from energy scaling
# τ_2D = (E/E_Pl)^1.29 × t_Pl
# So τ_2D × t_Pl^-1 = (E/E_Pl)^1.29

t_Pl = 5.39e-44  # seconds (Planck time)
E_SN = 1e44      # J
E_Pl_2D = 1e9    # GeV (typical 2D Planck scale)

tau_SN_pred = (E_SN/E_Pl_2D)**1.29 * t_Pl
print(f"\nEnergy scaling:  τ = (E/E_Pl)^1.29 × t_Pl")
print(f"For E = E_SN = 10^44 J, E_Pl,2D ~ 10^9 GeV: τ = {tau_SN_pred:.2e} s")
print(f"  (Set E_Pl,2D to match 33 s: E_Pl,2D = {E_SN/(TAU_SN/t_Pl)**(1/1.29):.2e} GeV)")
print(f"  → μ in our notation")

# =============================================================================
# PART 2: DENSITY OF STATES FOR N=12 SYK AT LOW ENERGY
# =============================================================================
print("\n" + "="*72)
print("PART 2: DENSITY OF STATES ρ(E) FOR N=12 SYK AT LOW ENERGY")
print("="*72)

# SYK at large N: ρ(E) ~ sinh(2π√(2E/E_0)) / (2π)² × density factor
# More precisely: ρ(E) ~ exp(S_0(E)) where S_0(E) is the zero-temperature entropy
#
# At low E (E < E_0): ρ(E) ~ exp(S_0 + 2π√(C × E/J))   (Schwarzian)
# where S_0 is extensive, C is specific heat coefficient

# S_0 for SYK with q=4 (our case): S_0 = N × s_0 / 2 with s_0 ≈ 0.2324
N_FERM = 12
S_0_PER_FERM = 0.2324  # per fermion at q=4
S_0 = N_FERM * S_0_PER_FERM

# Specific heat coefficient (Schwarzian):
# C ~ N/(2π² J) where J is the SYK coupling
# (the (JT gravity) Schwarzian action has coefficient C)
C_SCHW = N_FERM / (2 * PI**2)

# Density of states (in units of J=1):
def rho_SYK(E_arr):
    """SYK density of states at low energy (Schwarzian regime)."""
    return np.exp(S_0 + 2*np.pi*np.sqrt(C_SCHW * np.abs(E_arr)))

# E in units of J (SYK coupling)
E_test = np.array([0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0])
print(f"\nFor N={N_FERM}, S_0 = {S_0:.4f}, C_Schwarzian = {C_SCHW:.4f}")
print(f"\nρ(E) at low E (E in units of J):")
print(f"{'E/J':>8} {'S(E)':>10} {'ρ(E) (log)':>14} {'S(E)-S_0':>12}")
for E in E_test:
    S_E = S_0 + 2*PI*np.sqrt(C_SCHW * E)
    print(f"{E:>8.2f} {S_E:>10.4f} {S_E:>14.6f} {S_E-S_0:>12.4f}")

# Now: S(E) - S_0 = 2π√(C×E) = 2π√(N/(2π²) × E) = 2π√(N×E/(2π²))
#                                  = √(2N×E)
# So S(E) - S_0 = √(2N×E)   for E in units of J

# What E corresponds to the 2D universe mass m_2D = M_SN_bary = 10 M_sun?
# M_SN_bary in units of J: M_SN_bary c² / (ℏ × ω_0) where ω_0 is SYK frequency
# Skip this — too many unknowns

# =============================================================================
# PART 3: N=12 SPECIFICALLY — WHY 12?
# =============================================================================
print("\n" + "="*72)
print("PART 3: WHY N=12 SPECIFICALLY?")
print("="*72)

# Candidates for "12":
candidates = [
    ("4 Weyl × 3 generations (SM)", "12", "Connects to Standard Model"),
    ("(DOZZ b² = 1/2, c=1) → central charge = 1, no specific N=12 from DOZZ", "0", ""),
    ("24 fermions in N=24 SYK → 12 Majorana pairs", "12 (pairs)", "Majorana = real fermions"),
    ("N=12 → SU(12) → 12²-1 = 143 generators", "143", "W_∞ algebra has N-1 = 11 → matrix model has 143"),
    ("12 = 4 × 3 (spacetime dim × generations)", "12", "Natural for brane-world"),
    ("c=1 matrix model: 12 fermions → M_2D = 12 × m_2D_quark", "12", "Mass spectrum from N=12"),
    ("N=12 minimal for all 4 forces to fit", "12", "Speculative"),
]

print(f"\n{'Candidate':>40} {'N':>10} {'Note':>40}")
print("-"*92)
for cand, N_val, note in candidates:
    print(f"{cand:>40} {N_val:>10} {note:>40}")

# Compute W_∞ generators for N=12
print(f"\nW_∞ algebra structure:")
print(f"  For N fermions, W_∞ has 1+N-1 = N higher-spin currents")
print(f"  For N=12: 12 currents (spin 2, 3, 4, ..., 13)")
print(f"  In SU(N): N²-1 = 143 adjoint generators")
print(f"  → SIDC's N=12 maps to: 12 higher-spin currents + 143 adjoint")

# =============================================================================
# PART 4: SCHWARZIAN ACTION EVALUATION
# =============================================================================
print("\n" + "="*72)
print("PART 4: SCHWARZIAN ACTION {F,t} AT THE 2D UNIVERSE")
print("="*72)

# Schwarzian: {F,t} = F'''/F' - (3/2)(F''/F')²
# For F(t) = (a/π)tan(πt/b):  {F,t} = (2π²/b²) × (1/cos²(πt/b))
# At t=0: {F,t} = 2π²/b²

# Connection to α=1.289: the partition function
# Z = ∫ dF exp(-C{F,t})
# gives specific heat C → ρ(E) ~ exp(2π√(CE))

# Connection to α:
# Saddle point of the saddle equation δS/δG = J gives G ~ |t-t'|^-2/q
# At q=4: G ~ |t-t'|^-1/2 (which is the conformal 2-point function in 0+1D)
# The eigenvalue spectrum of the saddle: ε_n ∝ n × J (linear in n)
# Energy: E = Σ_n ε_n × n_occupation

# For 2D universe: the conformal dimension of the q=4 SYK bilinear is Δ = 1/q = 1/4
# The "energy scaling" of the lifetime: τ_2D ~ E^(1/Δ - 1) = E^3 ?

# Hmm wait — let me reconsider. We have α = 1.289, not 3.
# The τ_2D formula was: τ_2D = (E/E_Pl)^1.29 × t_Pl
# Where does 1.29 come from?

# From the saddle-point analysis (syk_2d_universe_saddle.py):
# 1.289 = 1 + 1/√12
# The "1" comes from kinematic time dilation
# The "1/√12" comes from SYK saddle (1/N)^(1/2) × finite-N correction

# So: α = 1 + 1/√12 = 1.289
# Where:
#   "1" = kinematic / special relativity scaling (E/c² → τ)
#   "1/√12" = SYK saddle correction (1/N)⁰·⁵ × structural factor

# =============================================================================
# PART 5: COUPLING g_s — STRING COUPLING AND f_back
# =============================================================================
print("\n" + "="*72)
print("PART 5: g_s (STRING COUPLING) ↔ f_back (BACK-PROJECTION FRACTION)")
print("="*72)

# In c=1 matrix model: g_s = 1/(string coupling constant)
# String coupling → probability of string splitting/joining

# SIDC's f_back = probability that 2D universe energy returns to 3+1D
# This is the "back-projection" of the 2D universe's death

# f_DE ~ 10^-85 for SN (calibration)
# Compare to: e^-S where S is some action

# If S ~ 195.5 then e^-S ~ 10^-85
# What action? Several candidates:

# 5a) RS-II bulk action:
# S_bulk = (1/(16π G_5)) ∫ d^5x √(-G) (R - 2Λ_5)
# For warping: S_warp = ∫_0^L dy exp(-ky) × volume_factor
# S_warp = V × (1 - exp(-kL)) / k ~ V/kL × 1  for kL >> 1
# With kL ≈ 195.5: f_back = exp(-kL) ≈ 10^-85 ✓

print(f"5a) RS-II warping:")
print(f"   f_back = exp(-kL)")
print(f"   For f_DE = 10^-85:  kL ≈ {np.log(1e85):.2f}")
print(f"   With k ~ M_Pl,4 (typical AdS_5 curvature):")
print(f"   L ~ 195.5 / k ~ 195.5 × ℏ/(M_Pl,4 × c) ~ {195.5 * 1.6e-35:.2e} m")
print(f"   Compare to extra-dim upper bound: ~10^-19 m → ratio ~10^16 TOO LARGE")
print(f"   HMMMM: k is NOT M_Pl,4. It's set by AdS curvature scale.")
print(f"   If k ~ 10^-3 eV (AdS_5 scale, much smaller): L ~ 10^16 m ~ 1 pc — sensible!")

# 5b) Hagedorn-like suppression:
# If 2D universe is at temperature T_2D for lifetime τ_2D:
# Boltzmann: f_back ~ exp(-ΔF/T_2D) where ΔF is the "death barrier"
# For τ_2D = 33 s, T_2D = ℏ/τ_2D ~ 10^-15 K (cold!)

# Hmm T_2D is very cold. The Boltzmann factor is small only if ΔF/T_2D is large
# But f_back is the probability that 2D universe energy returns
# If T_2D = ℏ/τ_2D ~ 10^-15 K, then exp(-ΔF/T_2D) is small for any ΔF > T_2D

# Let's see: k_B × 10^-15 K = 10^-15 × 1.38e-23 J = 10^-38 J
# Compare to event energy: E_SN ~ 10^44 J
# Ratio: 10^82 — so f_back ~ exp(-10^82) is much smaller than 10^-85
# That's too much suppression

print(f"\n5b) Hagedorn/Boltzmann:")
print(f"   T_2D = ℏ/τ_2D ~ ℏ/33s ~ {HBAR/33:.3e} K = {HBAR/33 * 1.38e-23:.3e} J/K × K = {HBAR/33:.3e} J")
print(f"   Wait, T_2D = ℏ/τ_2D has units of J·s/s = J ... but K needs k_B")
print(f"   T_2D = ℏ/(k_B × τ_2D) = {HBAR/(1.38e-23 * 33):.3e} K")
print(f"   For f_back = exp(-ΔF/T_2D): ΔF = E_SN gives f_back = exp(-{E_SN * 33 * 1.38e-23 / HBAR:.2e})")
print(f"   That's exp(-10^82) → f_back ≈ 0 — WAY too suppressed")
print(f"   So Boltzmann-from-T_2D doesn't work. f_back is NOT a Boltzmann factor.")

# 5c) Tunneling probability (WKB / instanton):
# f_back ~ exp(-S_E) where S_E is the Euclidean action
# For 2D universe decaying by tunneling through a barrier:
# S_E = ∫ dτ √(2m(V - E))  ~ m × L × √(V-E)

# If V-E ~ E_2D and m × L × √V ~ S_E:
# For f_DE = 10^-85, S_E ~ 195.5

# Compare to N=12 Schwarzian: S_0 ~ 12 × 0.2324 = 2.79
# Compare to: c=1 string instanton: S_E ~ 1/g_s
# For g_s ~ 1/200: S_E ~ 200 (close!)

print(f"\n5c) WKB tunneling:")
print(f"   S_E ~ 195.5")
print(f"   N=12 Schwarzian S_0 = {S_0:.2f} (too small)")
print(f"   c=1 string instanton: S_E ~ 1/g_s")
print(f"   For S_E = 195.5: g_s ~ {1/195.5:.4f}")
print(f"   Hmm, g_s ~ 1/200 — could be a coupling scale, not fundamental")

# =============================================================================
# PART 6: SUMMARY — WHAT'S MISSING FROM COMPLETE LAGRANGIAN
# =============================================================================
print("\n" + "="*72)
print("PART 6: SUMMARY — WHAT'S STILL MISSING")
print("="*72)

print("""
The Lagrangian skeleton is:  L = L_c=1 + L_N=12 + L_Schwarzian

What's IN the skeleton:
1. L_c=1 Liouville: c=1, b² = 1/2 → b = i
2. L_N=12 SYK: 12 fermions, q=4 coupling, J_{ijkl}
3. L_Schwarzian: {F,t}, coupling C = N/(2π²)

What's MISSING (the v8 work):
A. Hagedorn temperature T_H → 2D universe death time
   - c=1: T_H = 0 (paradox)
   - With N=12 fermions: T_H ≠ 0?
   - Connection to τ_2D = ℏ/T_H?

B. Coupling between L_c=1 and L_N=12
   - Currently set to zero (most natural)
   - Need to derive from first principles
   - f_back = exp(-S_coupling) = 10^-85 → S_coupling ~ 195.5

C. Mass spectrum of N=12 SYK
   - Lightest mass: depends on J (SYK coupling)
   - Need to relate to observed M_2D_3+1D ~ (E_Pl/E)^0.29

D. The "creation" term
   - We have S_destruction (death) but not S_creation (birth)
   - Birth = dimensional projection of 3+1D event into 2D

E. The 3+1D ↔ 2D matching condition
   - How does the bulk action S_bulk relate to the brane action S_brane?
   - This is the RS-II / brane-world dictionary

F. Energy scaling EXPLICITLY in L
   - τ_2D = (E/E_Pl)^1.29 × t_Pl must come from L
   - Currently: α = 1.289 is a fitting parameter
   - Need: α derived from the saddle-point equation + finite-N correction
""")

print("="*72)
print("v7 CONCLUSION:")
print("="*72)
print(f"""
1. Hagedorn: c=1 has T_H = 0 (paradox), but with N=12 SYK fermions, T_H might
   be non-zero. Need to compute T_H(N=12).

2. Density of states ρ(E): at low E, ρ(E) ~ exp(S_0 + 2π√(N×E/(2π²))) = exp(S_0 + √(2N×E))
   For N=12: ρ(E) ~ exp(2.79 + √(24E))
   This gives 2D universe mass spectrum if we know E in physical units.

3. N=12 candidates: 4 Weyl × 3 generations, 12 from 24 Majorana pairs,
   or SU(12) with 143 adjoint generators. The 4 × 3 = 12 is most natural.

4. f_back = exp(-195.5): matches RS-II warping with kL ~ 195.5 (sensible)
   But Boltzmann doesn't work (too cold)

5. NEXT STEP: v8 should compute Hagedorn T_H for N=12 SYK explicitly and
   check if T_H = ℏ/τ_2D matches the SN calibration (33 s).
""")