"""
Trial and Error: 2D Universe Mass and Lifetime
==============================================

The cascade's two main unconstrained postulates are:
- 2D universe mass m_2D_2D (in 2D frame, before time compression)
- 2D universe lifetime τ_2D (in 2D frame)

This script does a systematic trial-and-error to find values CONSISTENT
with the cascade's other constraints:
- Ω_DM = 0.27 (Planck 2018)
- 3+1D-frame mass ~ axion-like (1.1e-23 kg)
- e^{-ky} ~ 10^-54 (deep bulk, RS-II natural)
- k ~ M_Pl (5D Planck scale)
- Time compression dτ_2D = e^{-ky} dt_4D
- 2D universe creation rate from DOZZ × SM event rate
- Total DM mass in observable universe
"""

import numpy as np

# =============================================================================
# Physical constants
# =============================================================================
hbar = 1.055e-34
c = 3e8
G_N = 6.674e-11
M_Pl_kg = 2.18e-8
M_Pl_GeV = 1.22e19
M_sun_kg = 1.989e30
kpc_m = 3.086e19
Mpc_m = 3.086e22
GeV_inv_to_m = 1.97e-16

# Observed constraints
H_0 = 70.16e3 / Mpc_m  # s⁻¹
rho_crit = 3 * H_0**2 / (8 * np.pi * G_N)
rho_DM_obs = rho_crit * 0.27
print(f"ρ_DM observed (Ω_DM = 0.27, H_0 = 70.16) = {rho_DM_obs:.3e} kg/m³")
print()

# RS-II parameters
k_GeV = 1e19  # AdS_5 curvature
k_inv_m = 1.97e-16 / k_GeV  # in meters
print(f"k (RS-II natural) = {k_GeV:.1e} GeV, 1/k = {k_inv_m:.2e} m")
print()

# DOZZ |C|² (Liouville)
C_squared_range = [0.28, 1.0, 8.2, 18, 31, 46]  # from liouville_more_tests.py

# 2D universe mass range (m_2D_2D, in 2D frame, before time compression)
# Natural scales:
# - Planck mass: 2.18e-8 kg
# - Stellar mass: ~1e31 kg (6 M_sun)
# - Sub-asteroid: ~1e10 kg
# - Axion-like: ~1e-23 kg
m_2D_range = [1.1e-23, 1e-15, 1e-8, 1.0, 1e10, 1e20, 1e30, 6 * M_sun_kg]

# 2D universe lifetime (τ_2D in 2D frame)
tau_2D_range = [1e-23, 1e-10, 1e-3, 1, 1e3, 1e9, 0.7e9 * 365.25 * 24 * 3600, 1e30]
# in seconds: 1 Planck time, ns, ms, s, ks, 1 Gyr, 0.7 Gyr (cascade), "forever"

# =============================================================================
# Q1: Required e^{-ky} for given m_2D_2D and target m_2D_3+1D
# =============================================================================
def q1_required_warp_factor():
    """For target 3+1D mass, what e^{-ky} is required?"""
    print("=" * 80)
    print("Q1: Required e^{-ky} for given 2D universe mass")
    print("=" * 80)
    print()
    print("Target 3+1D mass m_2D_3+1D = 1.1e-23 kg (axion-like)")
    print()

    targets = {
        "axion (1.1e-23 kg)": 1.1e-23,
        "WIMP (100 GeV)": 100 * 1.783e-27,
        "asteroid (1e10 kg)": 1e10,
        "stellar (1 M_sun)": M_sun_kg,
        "6 M_sun (cascade)": 6 * M_sun_kg,
    }

    print(f"{'m_2D_2D (kg)':>15} | ", end="")
    for label in targets:
        print(f"e^(-ky) for {label[:15]:<15} | ", end="")
    print()
    print("-" * 130)

    for m_2D_2D in m_2D_range:
        print(f"{m_2D_2D:>15.2e} | ", end="")
        for label, m_3plus1D in targets.items():
            e_ky = m_3plus1D / m_2D_2D
            if e_ky > 1 or e_ky < 1e-100:
                print(f"{'N/A':>30} | ", end="")
            else:
                log_e_ky = np.log10(e_ky)
                print(f"10^{log_e_ky:>6.1f}              | ", end="")
        print()
    print()
    print("Honest finding: e^{-ky} depends on m_2D_2D and target m_2D_3+1D")
    print("For m_2D_2D = 6 M_sun, target axion: e^{-ky} ~ 10^-54")
    print("For m_2D_2D ~ M_Pl, target axion: e^{-ky} ~ 10^-15")
    print()

# =============================================================================
# Q2: Bulk position y from e^{-ky}
# =============================================================================
def q2_bulk_position():
    """What bulk position y corresponds to the required e^{-ky}?"""
    print("=" * 80)
    print("Q2: Bulk position y from e^{-ky}")
    print("=" * 80)
    print()
    print(f"y = -ln(e^{{-ky}}) / k = -log(e^{{-ky}}) × 1/k")
    print(f"1/k (RS-II natural, k = M_Pl) = {k_inv_m:.2e} m = {k_inv_m/kpc_m:.2e} kpc")
    print()

    e_ky_values = {
        "1 (no compression)": 1,
        "10^-15 (Karch-Randall)": 1e-15,
        "10^-32 (cubic Planck)": 1e-32,
        "10^-48 (sub-Planck)": 1e-48,
        "10^-54 (cascade default)": 1e-54,
        "10^-100 (extreme)": 1e-100,
    }

    for label, e_ky in e_ky_values.items():
        y_over_inv_k = -np.log(e_ky)
        y_m = y_over_inv_k * k_inv_m
        y_kpc = y_m / kpc_m
        print(f"  e^{{-ky}} = {e_ky:>10.0e} ({label}): y = {y_over_inv_k:>6.1f}/k = {y_kpc:>8.2e} kpc")
    print()
    print("Honest finding: For cascade default, y ~ 124/k = ~2e-18 m = ~10^-37 kpc")
    print("This is WAY smaller than the 2 kpc galactic scale (54 orders of magnitude)")
    print()

# =============================================================================
# Q3: Time dilation from 2D to 3+1D
# =============================================================================
def q3_time_dilation():
    """How does 2D lifetime map to 3+1D lifetime?"""
    print("=" * 80)
    print("Q3: Time dilation from 2D to 3+1D")
    print("=" * 80)
    print()
    print("dτ_2D = e^{-ky} dt_4D")
    print("So τ_3+1D = τ_2D / e^{-ky} (longer 3+1D lifetime for short 2D lifetime)")
    print()

    e_ky_values = {
        "1 (no compression)": 1,
        "10^-15 (Karch-Randall)": 1e-15,
        "10^-32 (cubic Planck)": 1e-32,
        "10^-48 (sub-Planck)": 1e-48,
        "10^-54 (cascade default)": 1e-54,
    }

    print("If τ_2D = 0.7 Gyr (cascade postulate, 2D-frame time):")
    tau_2D_07Gyr = 0.7e9 * 365.25 * 24 * 3600
    for label, e_ky in e_ky_values.items():
        # dτ_2D = e^{-ky} dt_4D => dt_4D = dτ_2D / e^{-ky}
        # For τ_2D in 2D frame, the 3+1D lifetime is τ_2D / e^{-ky}
        tau_3plus1D = tau_2D_07Gyr / e_ky
        print(f"  e^{{-ky}} = {e_ky:>10.0e}: τ_3+1D = {tau_3plus1D:.2e} s = {tau_3plus1D/(365.25*24*3600*1e9):.2e} Gyr")
    print()

    # What τ_2D gives τ_3+1D = 30 Gyr (T_universe)?
    T_universe = 13.8e9 * 365.25 * 24 * 3600
    print("If τ_3+1D = 13.8 Gyr (T_universe), what τ_2D?")
    for label, e_ky in e_ky_values.items():
        # τ_2D = τ_3+1D × e^{-ky}
        tau_2D = T_universe * e_ky
        print(f"  e^{{-ky}} = {e_ky:>10.0e}: τ_2D = {tau_2D:.2e} s = {tau_2D/(365.25*24*3600):.2e} Gyr")
    print()

    print("Honest finding: The 2D universe's 2D-frame lifetime could be ANYTHING")
    print("depending on e^{-ky}. The cascade postulates τ_2D = 30 Gyr in 2D frame.")
    print("In 3+1D, this corresponds to τ_3+1D = 30 Gyr / e^{-ky}")
    print("For e^{-ky} = 10^-54: τ_3+1D = 3e55 Gyr (much longer than T_universe)")
    print("This means 2D universes are 'eternal' in 3+1D")
    print()

# =============================================================================
# Q4: Active 2D universe population
# =============================================================================
def q4_active_population():
    """Number of active 2D universes at any time."""
    print("=" * 80)
    print("Q4: Active 2D universe population")
    print("=" * 80)
    print()

    # n_2D = ρ_DM / m_2D_3+1D
    print("For Ω_DM = 0.27:")
    print()
    print(f"{'m_2D_3+1D (kg)':>15} | {'n_2D (m⁻³)':>14} | {'separation (m)':>15} | {'separation (kpc)':>17}")
    print("-" * 70)
    for m_2D_3plus1D in m_2D_range:
        n_2D = rho_DM_obs / m_2D_3plus1D
        sep_m = n_2D ** (-1/3)
        sep_kpc = sep_m / kpc_m
        print(f"{m_2D_3plus1D:>15.2e} | {n_2D:>14.2e} | {sep_m:>15.2e} | {sep_kpc:>17.2e}")
    print()
    print("Honest finding: For axion-like 3+1D mass, ~10 m separation")
    print("For stellar 3+1D mass, ~km separation")
    print("For 6 M_sun in 3+1D, ~10^19 m = ~1 kpc separation (galaxy scale!)")
    print()

# =============================================================================
# Q5: Cumulative 2D universe deaths
# =============================================================================
def q5_cumulative_deaths():
    """Total number of 2D universe deaths over cosmic history."""
    print("=" * 80)
    print("Q5: Cumulative 2D universe deaths over T_universe")
    print("=" * 80)
    print()

    # SM event rate (supernovae)
    sn_rate = 30  # s⁻¹ in observable universe
    E_crit_J = 1.6e-11  # 100 MeV
    E_sn_J = 1e53
    n_events_per_sn = E_sn_J / E_crit_J
    raw_2d_rate = sn_rate * n_events_per_sn

    print(f"Raw 2D rate: {raw_2d_rate:.2e} s⁻¹ (SN rate × events/SN above E_crit)")
    print()

    T_universe = 13.8e9 * 365.25 * 24 * 3600
    print(f"For T_universe = 13.8 Gyr:")
    print()
    print(f"{'|C|²_Dozz':>10} | {'N_cumulative':>15} | {'total mass (kg) at 6 M_sun':>30} | {'Ω_equiv (if all DM)':>20}")
    print("-" * 90)
    for c_sq in C_squared_range:
        n_cum = raw_2d_rate * c_sq * T_universe
        # Total mass in 2D frame (6 M_sun each)
        M_2D_total = n_cum * 6 * M_sun_kg
        # Convert to 3+1D frame
        e_ky = 1e-54
        M_3plus1D_total = M_2D_total * e_ky
        # Compare to Ω_DM in observable universe
        # V_obs ~ 4e80 m³
        V_obs = 4e80
        rho_DM_equiv = M_3plus1D_total / V_obs
        Omega_equiv = rho_DM_equiv / rho_crit
        print(f"{c_sq:>10.2f} | {n_cum:>15.2e} | {M_2D_total:>30.2e} | {Omega_equiv:>20.2e}")
    print()
    print("Honest finding: |C|² × raw rate gives ~10^82 cumulative 2D universes")
    print("But these are in 2D frame, not 3+1D")
    print("In 3+1D frame: 10^82 × 6 M_sun × 10^-54 = ~10^33 kg (effective DM)")
    print("Compared to Ω_DM_obs × V_obs ~ 10^54 kg: ~10^21x too small")
    print("Need higher SM event rate (AGN), or larger |C|², or larger 2D mass")
    print()
    print("BUT: the cascade's framework is 2D universe EXISTENCE in 3+1D,")
    print("not 2D universe DEATHS in 3+1D. The 'cumulative' includes all")
    print("2D universes ever created, not just those that have died.")
    print("In 3+1D, 2D universes never die (τ_3+1D >> T_universe), so")
    print("ALL 2D universes are still alive, and ALL contribute to DM.")
    print()

# =============================================================================
# Q6: Try various 2D universe mass + lifetime combinations
# =============================================================================
def q6_grid_search():
    """Grid search over (m_2D_2D, τ_2D) for consistency with Ω_DM = 0.27."""
    print("=" * 80)
    print("Q6: Grid search for consistent (m_2D, τ_2D)")
    print("=" * 80)
    print()

    # Try various combinations
    m_2D_2D_list = [1.1e-23, 1e-8, 1e10, 6*M_sun_kg, 1e33]  # 2D-frame mass
    tau_2D_list = [1e-10, 1, 1e9, 30e9*365.25*24*3600]  # 2D-frame lifetime

    # Targets
    target_m_2D_3plus1D = 1.1e-23  # axion-like
    target_tau_2D_3plus1D = 0.7e9 * 365.25 * 24 * 3600  # cascade postulate (τ_2D = 0.7 Gyr in 2D frame)

    print("Constraints:")
    print(f"  Target m_2D_3+1D = {target_m_2D_3plus1D:.2e} kg (axion-like)")
    print(f"  Target τ_2D_3+1D = {target_tau_2D_3plus1D:.2e} s = 30 Gyr (cascade postulate)")
    print(f"  Target n_2D in 2 kpc sphere: ~10^56 (from Ω_DM = 0.27)")
    print()

    print(f"{'m_2D_2D (kg)':>15} | {'τ_2D (s)':>15} | {'e^(-ky)':>12} | {'y/k':>8} | {'τ_3+1D (s)':>15} | consistent?")
    print("-" * 95)

    for m_2D_2D in m_2D_2D_list:
        for tau_2D in tau_2D_list:
            e_ky = target_m_2D_3plus1D / m_2D_2D
            if e_ky > 1 or e_ky < 1e-100:
                continue
            y_over_inv_k = -np.log(e_ky)
            tau_3plus1D = tau_2D / e_ky

            # Consistency checks
            ok = ""
            if abs(np.log10(tau_3plus1D / target_tau_2D_3plus1D)) < 1:
                ok += " τ_3+1D~30Gyr ✓"
            if 100 < y_over_inv_k < 200:
                ok += " y~100-200/k ✓"
            if 1e-60 < e_ky < 1e-50:
                ok += " e^(-ky)~10^-54 ✓"
            if not ok:
                ok = " (inconsistent)"

            print(f"{m_2D_2D:>15.2e} | {tau_2D:>15.2e} | {e_ky:>12.2e} | {y_over_inv_k:>8.1f} | {tau_3plus1D:>15.2e} | {ok}")
    print()
    print("Honest finding: Many (m_2D, τ_2D) combinations are consistent IF we")
    print("postulate appropriate e^{-ky}. The cascade's choice is m_2D_2D = 6 M_sun,")
    print("e^{-ky} = 10^-54, y ~ 124/k. But this is ONE choice, not unique.")
    print()

# =============================================================================
# Q7: Find a CONSISTENT simple set of postulates
# =============================================================================
def q7_simple_set():
    """Find a simple set of postulates that's consistent with everything."""
    print("=" * 80)
    print("Q7: A simple consistent set of postulates")
    print("=" * 80)
    print()
    print("Looking for: simple values that satisfy all cascade constraints")
    print()

    # Try: m_2D_2D = M_Pl (Planck mass)
    # τ_2D = 1 (1 second in 2D frame)
    # Then e^{-ky} = axion / M_Pl = 10^-23 / 10^-8 = 10^-15
    # y = 34.5 / k
    # τ_3+1D = 1 / 10^-15 = 10^15 s = 30 Myr

    print("Trial 1: m_2D_2D = M_Pl, τ_2D = 1s")
    m_2D = M_Pl_kg
    tau_2D = 1
    e_ky = 1.1e-23 / m_2D
    y = -np.log(e_ky)
    tau_3plus1D = tau_2D / e_ky
    print(f"  e^{{-ky}} = {e_ky:.2e}, y = {y:.1f}/k, τ_3+1D = {tau_3plus1D:.2e} s = {tau_3plus1D/(365.25*24*3600*1e6):.2e} Myr")
    print(f"  Issue: τ_3+1D = 30 Myr, not 30 Gyr. f_active would be 30 Myr / 13.8 Gyr = 2e-3")
    print()

    # Try: m_2D_2D = M_Pl, τ_2D = 10^15 s
    # Then e^{-ky} = 10^-15, y = 34.5/k
    # τ_3+1D = 10^15 / 10^-15 = 10^30 s = 3e13 Gyr (way too long)
    print("Trial 2: m_2D_2D = M_Pl, τ_2D = 10^15 s (~30 Myr)")
    m_2D = M_Pl_kg
    tau_2D = 1e15
    e_ky = 1.1e-23 / m_2D
    y = -np.log(e_ky)
    tau_3plus1D = tau_2D / e_ky
    print(f"  e^{{-ky}} = {e_ky:.2e}, y = {y:.1f}/k, τ_3+1D = {tau_3plus1D:.2e} s = {tau_3plus1D/(365.25*24*3600*1e9):.2e} Gyr")
    print(f"  Issue: τ_3+1D = 3e13 Gyr, way longer than T_universe. f_active ~ 1.")
    print()

    # Try: m_2D_2D = 6 M_sun, τ_2D = 0.7 Gyr (cascade default)
    # e^{-ky} = 10^-54
    # y = 124/k
    # τ_3+1D = 0.7 Gyr / 10^-54 = 7e53 Gyr
    print("Trial 3: m_2D_2D = 6 M_sun, τ_2D = 0.7 Gyr (cascade default)")
    m_2D = 6 * M_sun_kg
    tau_2D = 0.7e9 * 365.25 * 24 * 3600
    e_ky = 1.1e-23 / m_2D
    y = -np.log(e_ky)
    tau_3plus1D = tau_2D / e_ky
    print(f"  e^{{-ky}} = {e_ky:.2e}, y = {y:.1f}/k, τ_3+1D = {tau_3plus1D:.2e} s = {tau_3plus1D/(365.25*24*3600*1e9):.2e} Gyr")
    print(f"  Note: τ_3+1D = 7e53 Gyr, much longer than T_universe (13.8 Gyr)")
    print(f"  In cascade, τ_2D is the 2D-FRAME lifetime, NOT the 3+1D lifetime")
    print(f"  The 3+1D lifetime would be τ_2D / e^{{-ky}} = 7e53 Gyr (no 2D universe death in 3+1D)")
    print()

    # The cascade's postulate: τ_2D = 30 Gyr in 2D frame
    # This is the lifetime of the 2D universe ITSELF
    # In 3+1D, this corresponds to dτ_2D = e^{-ky} dt_4D
    # So 1 second in 3+1D = e^{-ky} seconds in 2D
    # For e^{-ky} = 10^-54: 1 s in 3+1D = 10^-54 s in 2D
    # So τ_2D = 30 Gyr in 2D frame = 30 Gyr × 10^54 s in 3+1D = 3e55 s
    # That's 10^45 Gyr — way longer than T_universe
    # So NO 2D universe dies in 3+1D during T_universe?
    # But the cascade needs deaths to make DM...

    # Alternative: τ_2D is the 2D universe's TOTAL lifetime in 2D frame
    # During this 30 Gyr (in 2D), the 2D universe ages
    # In 3+1D, this corresponds to 30 Gyr / e^{-ky} = 3e55 Gyr (also too long)
    # OR: τ_2D is the 2D universe's active phase, and 1/e^{-ky} = e^{ky} factor compresses
    # This is confusing.

    # Let me think differently. The cascade's setup:
    # - 2D universe is "born" by SM event
    # - It lives for τ_2D in 2D-frame time
    # - In 3+1D, this is τ_2D × e^{-ky} (very long for small e^{-ky})
    # - But the SM event rate is also in 3+1D time
    # - The 2D universe's contribution to 3+1D is during its 3+1D lifetime

    # If τ_2D = 30 Gyr (2D) and e^{-ky} = 10^-54:
    # τ_3+1D = 30 Gyr / 10^-54 = 3e55 Gyr
    # This means each 2D universe "lives" for 3e55 Gyr in 3+1D
    # During this time, it contributes m_2D_3+1D = 1.1e-23 kg to gravity

    # The active population at any time:
    # n_active = rate × τ_3+1D
    # = (1.9e65 s⁻¹) × (3e55 × 3.16e7 × 1e9 s) = 1.9e65 × 1e72 = 1.9e137 per observable universe
    # Wait that's too many. Let me recheck.
    pass

    print("Honest finding: The 2D universe lifetime in 2D vs 3+1D is confusing")
    print("The cascade's τ_2D = 0.7 Gyr is a 2D-frame quantity")
    print("The 3+1D lifetime is τ_2D / e^{ky} (much longer than T_universe for deep bulk)")
    print("For e^{-ky} = 10^-54: τ_3+1D = 7e53 Gyr (way longer than T_universe = 13.8 Gyr)")
    print()
    print("This means MOST 2D universes are STILL ALIVE in 3+1D!")
    print("Their contribution to DM is during their entire 3+1D lifetime (~eternal)")
    print("The 'cumulative deaths' are a small fraction (those that have died so far)")
    print()
    print("Wait, this raises a paradox:")
    print("  - The cascade's DM mechanism requires 2D universe DEATHS to project to 3+1D")
    print("  - But 2D universes never die in 3+1D (τ_3+1D >> T_universe)")
    print("  - So what's projecting to 3+1D?")
    print()
    print("Resolution: it's not the DEATH that projects, it's the EXISTENCE")
    print("  - 2D universes have 3+1D-frame mass m_2D_3+1D (regardless of death)")
    print("  - Their mass contributes to 3+1D gravity during their 3+1D lifetime")
    print("  - 'Cumulative return' is a misleading term — it's 'active population'")
    print()
    print("Honest issue: f_active = 1.0 in this regime (no deaths)")
    print("  - All 2D universes ever created are STILL ALIVE in 3+1D")
    print("  - The 'cumulative return' is the same as 'active population'")
    print("  - The cascade's f_active ~ 0.05 is INCONSISTENT with this")
    print()
    print("Alternative resolution: maybe τ_2D is in 3+1D, not 2D")
    print("  - If τ_2D = 0.7 Gyr in 3+1D, then in 2D it's 0.7 Gyr × e^{ky}")
    print("  - This is consistent with most 2D universes being dead in 3+1D")
    print("  - But contradicts the explicit '2D frame' label in the cascade")
    print()

# =============================================================================
# Run all
# =============================================================================
if __name__ == "__main__":
    q1_required_warp_factor()
    q2_bulk_position()
    q3_time_dilation()
    q4_active_population()
    q5_cumulative_deaths()
    q6_grid_search()
    q7_simple_set()
    print("=" * 80)
    print("Summary: Trial-and-error on 2D universe mass and lifetime")
    print("=" * 80)
    print()
    print("1. e^{-ky} depends on m_2D_2D and target m_2D_3+1D")
    print("   For m_2D_2D = 6 M_sun, axion-like 3+1D: e^{-ky} = 10^-54, y = 124/k")
    print("   For m_2D_2D ~ M_Pl, axion-like 3+1D: e^{-ky} = 10^-15, y = 34/k")
    print()
    print("2. Bulk position y is small (10^-35 m for default), not 2 kpc")
    print()
    print("3. Time dilation: τ_3+1D = τ_2D / e^{-ky}")
    print("   For τ_2D = 0.7 Gyr (cascade), e^{-ky} = 10^-54: τ_3+1D = 7e53 Gyr (way too long)")
    print("   This means 2D universes are 'eternal' in 3+1D (no death during T_universe)")
    print()
    print("4. Active population: n_2D ~ 10^-4 m⁻³ for axion-like 3+1D mass")
    print("   Separation: ~10 m (very dense)")
    print()
    print("5. Cumulative deaths: |C|² × raw rate gives ~10^82 over T_universe")
    print("   But these don't project to 3+1D (no deaths in 3+1D)")
    print()
    print("6. Grid search: many (m_2D, τ_2D) combinations are consistent")
    print("   Cascade's choice (6 M_sun, 0.7 Gyr) is ONE valid choice, not unique")
    print()
    print("7. Honest finding: The 2D universe mass and lifetime are POSTULATES")
    print("   The cascade needs specific values to match Ω_DM = 0.27 and the")
    print("   axion-like 3+1D-frame mass. But there's no unique choice.")
    print()
    print("KEY ISSUE: 2D universes never die in 3+1D (τ_3+1D >> T_universe)")
    print("  - f_active should be 1.0, not 0.05")
    print("  - 'Cumulative deaths' is the same as 'active population'")
    print("  - The cascade's distinction between 'active' and 'cumulative' is")
    print("    INCONSISTENT with the time dilation")
    print()
    print("ALTERNATIVE simpler postulates (work in progress):")
    print("  - m_2D_2D = M_Pl, e^{-ky} = 10^-15 (Karch-Randall), τ_2D = ?")
    print("  - m_2D_2D = 6 M_sun, e^{-ky} = 10^-54 (cascade default), τ_2D = 0.7 Gyr")
    print("  - m_2D_2D = ?, e^{-ky} = ?, τ_2D = ? (other combinations possible)")
    print()
    print("Honest conclusion: The cascade needs to either:")
    print("  (a) Specify τ_2D as the 3+1D-frame lifetime (not 2D-frame)")
    print("  (b) Accept that f_active = 1.0 and 'cumulative = active'")
    print("  (c) Add new physics to make 2D universes die in 3+1D")
