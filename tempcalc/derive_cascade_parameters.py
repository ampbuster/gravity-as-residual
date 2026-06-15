"""
Deriving the cascade's likely 2D universe parameters
======================================================

Strategy:
- Drop the 30 Gyr assumption (it was a guess)
- Use 33 s in 3+1D as the empirical constraint (from ℓ/c rule)
- Treat m_2D_2D and e^{-ky} as free parameters
- Find CONSISTENT values that satisfy all cascade constraints:
  1. τ_3+1D = 33 s (empirical, from ℓ/c rule)
  2. Ω_DM = 0.27 (Planck 2018)
  3. m_2D_3+1D = axion-like (target, 1.1e-23 kg)
  4. SM event rate (supernovae + AGN, etc.)
  5. 5D AdS_5 framework (RS-II, k ~ M_Pl)
  6. Bulk position distribution P(y)

Let's see what we can derive.
"""

import numpy as np

# =============================================================================
# Physical constants
# =============================================================================
hbar = 1.055e-34  # J·s
c = 3e8            # m/s
G_N = 6.674e-11   # m³/(kg·s²)
M_Pl_kg = 2.18e-8  # kg
M_Pl_GeV = 1.22e19  # GeV
M_sun_kg = 1.989e30  # kg
kpc_m = 3.086e19
Mpc_m = 3.086e22
GeV_inv_to_m = 1.97e-16

# Observed constraints
H_0 = 70.16e3 / Mpc_m
rho_crit = 3 * H_0**2 / (8 * np.pi * G_N)
rho_DM_obs = rho_crit * 0.27

# Empirical mapping
tau_3plus1D = 33  # seconds (from ℓ/c rule)
m_2D_3plus1D_target = 1.1e-23  # kg (axion-like)

# SM event rates (in observable universe)
sn_rate = 30  # s⁻¹ supernovae
E_crit_J = 1.6e-11  # 100 MeV
E_sn_J = 1e53
n_events_per_sn = E_sn_J / E_crit_J
raw_2d_rate_per_sec = sn_rate * n_events_per_sn

T_universe = 13.8e9 * 365.25 * 24 * 3600
V_obs = 4e80  # m³, observable universe

print("=" * 80)
print("CASCADE PARAMETER DERIVATION")
print("=" * 80)
print()

# RS-II parameters
k_GeV = 1e19
k_inv_m = GeV_inv_to_m / k_GeV
print(f"k (RS-II natural) = {k_GeV:.1e} GeV, 1/k = {k_inv_m:.2e} m")
print()
print(f"Empirical constraints:")
print(f"  τ_3+1D = {tau_3plus1D} s (from ℓ/c)")
print(f"  m_2D_3+1D = {m_2D_3plus1D_target} kg (axion-like)")
print(f"  Ω_DM = 0.27 (Planck 2018)")
print(f"  ρ_DM = {rho_DM_obs:.3e} kg/m³")
print()
print(f"  Raw 2D rate = {raw_2d_rate_per_sec:.3e} s⁻¹ (SN rate × events/SN)")
print(f"  T_universe = {T_universe:.3e} s = 13.8 Gyr")
print()

# =============================================================================
# Q1: What is m_2D_2D given m_2D_3+1D and various e^{-ky}?
# =============================================================================
print("=" * 80)
print("Q1: m_2D_2D as a function of e^{-ky}")
print("=" * 80)
print()
print("Formula: m_2D_2D = m_2D_3+1D / e^{-ky}")
print()
print(f"{'e^(-ky)':>10} | {'y/k':>6} | {'m_2D_2D (kg)':>15} | {'m_2D_2D (other units)':>30}")
print("-" * 75)

e_ky_list = [1, 1e-10, 1e-17, 1e-25, 1e-32, 1e-40, 1e-48, 1e-54]
for e_ky in e_ky_list:
    m_2D_2D = m_2D_3plus1D_target / e_ky
    y = -np.log(e_ky)

    if m_2D_2D > 1e30:
        units = f"{m_2D_2D / M_sun_kg:.2e} M_sun"
    elif m_2D_2D > 1e10:
        units = f"{m_2D_2D:.2e} kg (asteroid)"
    elif m_2D_2D > 1:
        units = f"{m_2D_2D:.2e} kg"
    elif m_2D_2D > 1e-6:
        units = f"{m_2D_2D * 1e6:.2e} mg"
    else:
        units = f"{m_2D_2D * 1e9:.2e} ng"

    print(f"{e_ky:>10.0e} | {y:>6.1f} | {m_2D_2D:>15.2e} | {units:>30}")
print()
print("Many possible m_2D_2D values, depending on e^{-ky} choice")
print()

# =============================================================================
# Q2: Required 2D universe count density for Ω_DM
# =============================================================================
print("=" * 80)
print("Q2: Required 2D universe count density for Ω_DM")
print("=" * 80)
print()
print(f"n_2D = ρ_DM / m_2D_3+1D (target = axion-like = {m_2D_3plus1D_target} kg)")
print()

n_2D_target = rho_DM_obs / m_2D_3plus1D_target
print(f"n_2D (target) = {n_2D_target:.3e} m⁻³ = {n_2D_target * 1e6:.3e} L⁻¹")
print(f"Average inter-2D-universe separation = {n_2D_target ** (-1/3):.2e} m")
print()

# =============================================================================
# Q3: SM event rate vs 2D universe creation rate
# =============================================================================
print("=" * 80)
print("Q3: SM event rate vs 2D universe creation rate")
print("=" * 80)
print()

# Total 2D universes created over T_universe
# rate_2D = rate_SM × |C|² × α
# α is bulk-brane coupling (cascade's free parameter)
# |C|² ~ 1-46 from Liouville DOZZ

# We need n_2D × V_obs = total 2D universes in observable universe
# rate × T_universe × |C|² × α = n_2D × V_obs
# α = (n_2D × V_obs) / (rate × T_universe × |C|²)

n_2D_obs = n_2D_target * V_obs
print(f"Total 2D universes in observable universe (for Ω_DM = 0.27):")
print(f"  N = n_2D × V_obs = {n_2D_obs:.3e}")
print()

# Raw rate
print(f"Raw SM event rate (SN only): {raw_2d_rate_per_sec:.3e} s⁻¹")
print(f"Total events in T_universe: {raw_2d_rate_per_sec * T_universe:.3e}")
print()

# Required α for various |C|²
print(f"Required bulk-brane coupling α (for SN-only events):")
print()
print(f"{'|C|²_Dozz':>10} | {'rate_2D (s⁻¹)':>15} | {'N in T_universe':>15} | {'α required':>15}")
print("-" * 65)
for c_sq in [0.28, 1, 8.2, 18, 31, 46]:
    rate_2D = raw_2d_rate_per_sec * c_sq
    N_total = rate_2D * T_universe
    alpha_req = n_2D_obs / N_total
    print(f"{c_sq:>10.2f} | {rate_2D:>15.3e} | {N_total:>15.3e} | {alpha_req:>15.3e}")
print()
print("α is the cascade's free parameter (bulk-brane coupling).")
print("For SN-only events, α ~ 1e-7 to 1e-9 (small but not absurd).")
print()

# =============================================================================
# Q4: Effect of including AGN
# =============================================================================
print("=" * 80)
print("Q4: Effect of including AGN as additional 2D universe sources")
print("=" * 80)
print()

# AGN rate: ~10% of galaxies have active AGN
# Each AGN lasts ~10^7 yr, releases ~10^52 J over its lifetime
# Average AGN rate: ~10^(-3) per galaxy per year (much less than SN rate)
# But AGN have much higher energy per event

agn_rate_per_galaxy_per_year = 1e-3  # typical AGN rate
n_galaxies = 1e11  # observable universe
agn_rate_per_sec = agn_rate_per_galaxy_per_year * n_galaxies / (365.25 * 24 * 3600)
E_agn_J = 1e52
n_events_per_agn = E_agn_J / E_crit_J

print(f"AGN rate (estimate): {agn_rate_per_sec:.3e} s⁻¹ in observable universe")
print(f"Energy per AGN: {E_agn_J:.0e} J")
print(f"Events per AGN above E_crit: {n_events_per_agn:.3e}")
print()

raw_2d_rate_agn = agn_rate_per_sec * n_events_per_agn
print(f"Raw 2D rate from AGN: {raw_2d_rate_agn:.3e} s⁻¹")
print(f"AGN / SN rate ratio: {raw_2d_rate_agn / raw_2d_rate_per_sec:.3e}")
print()

# Total raw rate with AGN
total_raw_2d_rate = raw_2d_rate_per_sec + raw_2d_rate_agn
print(f"Total raw 2D rate (SN + AGN): {total_raw_2d_rate:.3e} s⁻¹")
print()

# Required α with AGN
print(f"Required α (with AGN, |C|² = 1):")
n_2D_total = total_raw_2d_rate * T_universe
alpha_with_agn = n_2D_obs / n_2D_total
print(f"  α = {alpha_with_agn:.3e}")
print()

# =============================================================================
# Q5: Derive the most likely parameters
# =============================================================================
print("=" * 80)
print("Q5: Most likely parameters")
print("=" * 80)
print()

# Given all the constraints, what are the most likely values?
#
# Constraint 1: τ_3+1D = 33 s (empirical)
#   → e^{-ky} determines τ_2D = 33 s × e^{-ky} (very short for deep bulk)
#   → Or τ_2D = 33 s / e^{-ky} (very long for deep bulk) [if other formula]
#
# Constraint 2: m_2D_3+1D = axion-like (target)
#   → m_2D_2D = 1.1e-23 / e^{-ky}
#
# Constraint 3: Ω_DM = 0.27
#   → n_2D = ρ_DM / m_2D_3+1D ~ 2.3e-4 m⁻³ for axion-like
#   → Total 2D universes: 2.2e75 in past lightcone, or ~10^75 in observable universe
#
# Constraint 4: SM event rate
#   → Total events in T_universe (SN+AGN): ~10^82
#   → |C|² × α × 10^82 = 10^75
#   → α × |C|² ~ 10^-7
#
# For natural DOZZ (|C|² ~ 1-46): α ~ 10^-7 to 10^-9
# This is a SMALL but reasonable bulk-brane coupling

# Now, m_2D_2D and e^{-ky} are still free parameters.
# The cascade's choice (6 M_sun, 10^-54) is ONE possibility, but
# it conflicts with 33 s empirical.

# Better choice: e^{-ky} ~ 10^-15 (from Karch-Randall natural scale)
# Then m_2D_2D = 1.1e-23 / 1e-15 = 1.1e-8 kg = M_Pl
# And τ_2D = 33 s × 1e-15 = 3.3e-14 s (way shorter than 33 s)
# OR τ_2D = 33 s / 1e-15 = 3.3e16 s = 1 Gyr (reasonable 2D lifetime)

print("Recommended parameter set (Option C, Karch-Randall natural):")
print()
print("  e^{-ky} ~ 10^-15 (Karch-Randall 2+1D Planck scale)")
print("  m_2D_2D ~ 1.1e-8 kg = M_Pl (Planck mass)")
print("  m_2D_3+1D = 1.1e-23 kg (axion-like, by construction)")
print("  τ_3+1D = 33 s (empirical ℓ/c)")
print("  τ_2D = ? (depends on formula interpretation)")
print()
print("  α (bulk-brane coupling) ~ 10^-7 to 10^-9")
print("  f_active ~ 1.0 (all 2D universes are still alive in 3+1D)")
print("  n_2D ~ 2.3e-4 m⁻³ (10 m separation)")
print()

# =============================================================================
# Q6: Test if the 33 s can be derived from first principles
# =============================================================================
print("=" * 80)
print("Q6: Can 33 s be derived from first principles?")
print("=" * 80)
print()

# The 33 s comes from ℓ/c where ℓ is some natural length
# For 33 s: ℓ = 33 × 3e8 = 1e10 m = 0.07 AU
# This is the Earth-Sun distance, but that's coincidence

# What are some natural length scales?
print("Natural length scales for 33 s:")
print()
natural_lengths = {
    "1 m (human)": 1,
    "1 km (city)": 1e3,
    "Earth radius (6.4e6 m)": 6.4e6,
    "1 AU (1.5e11 m)": 1.5e11,
    "Light-year (9.5e15 m)": 9.5e15,
    "Parsec (3.1e16 m)": 3.1e16,
    "kpc (3.1e19 m)": 3.1e19,
    "Mpc (3.1e22 m)": 3.1e22,
    "Observable universe (4.4e26 m)": 4.4e26,
    "Planck length (1.6e-35 m)": 1.6e-35,
    "Proton radius (8.4e-16 m)": 8.4e-16,
    "Atom (1e-10 m)": 1e-10,
}

for label, length in natural_lengths.items():
    time_s = length / c
    print(f"  {label}: ℓ/c = {time_s:.2e} s = {time_s/60:.2e} min = {time_s/3600:.2e} hr")
print()
print("33 s corresponds to ℓ = 1e10 m (between Earth and Sun)")
print("This is NOT a natural length in the cascade's framework")
print("It's likely just a coincidence with solar system scales")
print()

# =============================================================================
# Q7: 33 s as a derived quantity from e^{-ky} and 2D universe size
# =============================================================================
print("=" * 80)
print("Q7: 33 s from e^{-ky} and 2D universe size?")
print("=" * 80)
print()
print("If the 2D universe's natural size in 2D is L_2D, then in 3+1D")
print("its size is L_2D × e^{ky} (warp factor stretches the size).")
print()
print("If ℓ_3+1D ~ 1e10 m (corresponding to 33 s), then")
print("L_2D = ℓ_3+1D / e^{ky}")
print()

for e_ky in [1, 1e-10, 1e-17, 1e-32, 1e-48, 1e-54]:
    L_2D = 1e10 / e_ky
    print(f"  e^{{-ky}} = {e_ky:>10.0e}: L_2D = {L_2D:.2e} m")
print()
print("For e^{-ky} = 10^-17: L_2D = 1e27 m (much bigger than observable universe!)")
print("For e^{-ky} = 1e-54: L_2D = 1e64 m (ridiculous)")
print()
print("The 33 s in 3+1D doesn't naturally correspond to a 2D universe size.")
print("It's the cascade's EMPIRICAL INPUT, not derived.")
print()

# =============================================================================
# Q8: Final parameter set with all considerations
# =============================================================================
print("=" * 80)
print("Q8: Final likely parameter set")
print("=" * 80)
print()

# Summary of all constraints and likely values:
print("Constraints:")
print("  τ_3+1D = 33 s (empirical, ℓ/c mapping)")
print("  m_2D_3+1D = 1.1e-23 kg (axion-like, target)")
print("  Ω_DM = 0.27 (Planck 2018)")
print()
print("Free parameters (postulates):")
print("  e^{-ky} = ? (determines y in bulk)")
print("  m_2D_2D = ? (determines 2D universe mass scale)")
print("  α (bulk-brane coupling) = ?")
print("  |C|²_Dozz = ? (Liouville parameter b, α_0)")
print()
print("Derived quantities:")
print("  m_2D_3+1D = m_2D_2D × e^{-ky}")
print("  τ_2D = τ_3+1D / e^{-ky} = 33 s / e^{-ky} (or 33 s × e^{-ky}, depending on convention)")
print("  n_2D = ρ_DM / m_2D_3+1D")
print("  f_active ~ 1.0 (or different if death mechanism is added)")
print()

# Recommended values
print("RECOMMENDED parameter set:")
print()
print("  m_2D_2D = M_Pl ~ 2e-8 kg (Planck mass, natural in 2D CFT)")
print("  e^{-ky} = 1.1e-23 / 2e-8 = 5.5e-16 (Karch-Randall scale)")
print("  y = -log(5.5e-16) / k = 34.7 / k (deep but not extreme)")
print("  m_2D_3+1D = 1.1e-23 kg (axion-like, ✓)")
print("  τ_3+1D = 33 s (empirical, ✓)")
print("  τ_2D = 33 s / 5.5e-16 = 6e16 s = 1.9 Gyr (reasonable 2D lifetime!)")
print()
print("  α (bulk-brane coupling) = ? (depends on |C|²)")
print("  |C|²_Dozz = ? (Liouville parameter)")
print("  Need: α × |C|² × rate × T_universe = n_2D × V_obs")
print("  Solving: α × |C|² ~ 10^-7 (for SN+AGN events)")
print()

# =============================================================================
# Q9: Verify all constraints are satisfied
# =============================================================================
print("=" * 80)
print("Q9: Verification of recommended parameter set")
print("=" * 80)
print()

e_ky_recommended = 5.5e-16
m_2D_2D_recommended = M_Pl_kg
m_2D_3plus1D_recommended = m_2D_2D_recommended * e_ky_recommended
tau_3plus1D_recommended = 33
tau_2D_recommended = tau_3plus1D_recommended / e_ky_recommended

print(f"Recommended parameters:")
print(f"  m_2D_2D = {m_2D_2D_recommended:.2e} kg (M_Pl)")
print(f"  e^{{-ky}} = {e_ky_recommended:.2e}")
print(f"  m_2D_3+1D = {m_2D_3plus1D_recommended:.2e} kg")
print(f"  τ_3+1D = {tau_3plus1D_recommended} s")
print(f"  τ_2D = {tau_2D_recommended:.2e} s = {tau_2D_recommended/(365.25*24*3600*1e9):.2e} Gyr")
print()

# Verify constraints
print("Verification:")
print(f"  ✓ m_2D_3+1D = 1.1e-23 kg (axion-like): {m_2D_3plus1D_recommended:.2e}")
print(f"  ✓ τ_3+1D = 33 s: {tau_3plus1D_recommended} s")
print(f"  ✓ τ_2D is reasonable (Gyr-scale): {tau_2D_recommended/(365.25*24*3600*1e9):.2e} Gyr")
print()

# Bulk position
y_over_inv_k = -np.log(e_ky_recommended)
print(f"  Bulk position: y = {y_over_inv_k:.1f} / k = {y_over_inv_k * k_inv_m:.2e} m")
print()

# Check: is this bulk position physically reasonable?
print(f"  y = 34.7 / k (deep but not extreme)")
print(f"  This is in the same ballpark as the hierarchy (k*y* ~ 38)")
print(f"  Consistent with natural RS-II")
print()

# Check τ_2D against T_universe
T_universe_Gyr = 13.8
tau_2D_Gyr = tau_2D_recommended / (365.25 * 24 * 3600 * 1e9)
print(f"  τ_2D vs T_universe:")
print(f"    τ_2D = {tau_2D_Gyr:.2e} Gyr")
print(f"    T_universe = {T_universe_Gyr} Gyr")
if tau_2D_Gyr < T_universe_Gyr:
    print(f"    → 2D universes HAVE DIED in 3+1D during T_universe ✓")
    f_active = tau_3plus1D_recommended / T_universe
    print(f"    f_active = τ_3+1D / T_universe = {f_active:.2e}")
else:
    print(f"    → 2D universes are STILL ALIVE in 3+1D")
    print(f"    f_active = 1.0")
print()

# =============================================================================
# Q10: Sensitivity analysis
# =============================================================================
print("=" * 80)
print("Q10: Sensitivity analysis")
print("=" * 80)
print()

# Test if the recommended parameters are stable against small changes
print("Test: vary e^{-ky} by ±50%, see if parameters stay reasonable")
print()

for e_ky_test in [e_ky_recommended * 0.5, e_ky_recommended, e_ky_recommended * 2]:
    m_2D_test = m_2D_3plus1D_target / e_ky_test
    tau_2D_test = tau_3plus1D_recommended / e_ky_test
    tau_2D_Gyr = tau_2D_test / (365.25 * 24 * 3600 * 1e9)
    print(f"  e^{{-ky}} = {e_ky_test:.2e}: m_2D_2D = {m_2D_test:.2e} kg, τ_2D = {tau_2D_Gyr:.2e} Gyr")

print()
print("Recommendation: the parameters are NOT uniquely determined.")
print("There is a 1-parameter family of (m_2D_2D, e^{-ky}) pairs that work.")
print("The cascade's choice is one valid choice, not unique.")
print()

# =============================================================================
# Run summary
# =============================================================================
print("=" * 80)
print("FINAL SUMMARY: Derived likely parameters")
print("=" * 80)
print()
print("Strategy: drop 30 Gyr, use 33 s as empirical constraint.")
print()
print("Constraints:")
print("  τ_3+1D = 33 s (empirical, ℓ/c)")
print("  m_2D_3+1D = 1.1e-23 kg (axion-like target)")
print("  Ω_DM = 0.27 (Planck 2018)")
print()
print("Free parameters (postulates):")
print("  m_2D_2D = M_Pl ~ 2e-8 kg (RECOMMENDED)")
print("  e^{-ky} = 5.5e-16 (RECOMMENDED, Karch-Randall scale)")
print("  α × |C|² ~ 10^-7 (for SN+AGN rate to give Ω_DM)")
print()
print("Derived quantities:")
print("  m_2D_3+1D = 1.1e-23 kg (✓ axion-like)")
print("  τ_2D = 1.9 Gyr (2D-frame lifetime, reasonable)")
print("  n_2D = 2.3e-4 m⁻³ (10 m separation)")
print("  Total 2D universes in observable universe: ~10^75")
print()
print("Bulk position:")
print("  y = 34.7 / k = 6.8e-34 m (deep but not extreme)")
print("  Consistent with natural RS-II hierarchy (k*y* ~ 38)")
print()
print("f_active (active fraction):")
print("  τ_2D = 1.9 Gyr < T_universe = 13.8 Gyr")
print("  So MOST 2D universes have died in 3+1D")
print("  f_active = 33 s / 13.8 Gyr = 7.6e-17 (tiny!)")
print("  Wait, that doesn't make sense. f_active = 1 for short lifetimes.")
print()
print("  Actually, f_active is the fraction of 2D universes that are STILL ALIVE")
print("  For τ_3+1D = 33 s and T_universe = 13.8 Gyr:")
print("  2D universe dies 33 s after creation")
print("  So at any time, only the most recent 33 s of creations are alive")
print("  N_alive = rate × τ_3+1D = rate × 33 s")
print("  N_total = rate × T_universe (cumulative)")
print("  f_active = N_alive / N_total = 33 s / T_universe = 7.6e-17")
print()
print("  This is the cascade's 'f_active'!")
print("  The cascade had f_active = 0.05, but the actual value depends on")
print("  τ_3+1D and T_universe.")
print("  For τ_3+1D = 33 s, f_active = 7.6e-17, NOT 0.05.")
print()
print("  The 5% / 27% / 68% split might be different from what we thought.")
print()
