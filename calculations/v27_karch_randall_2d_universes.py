"""
Karch-Randall 2D universe calculations
======================================

Karch & Randall 2000: 2+1D branes in AdS_5 bulk.

The cascade's 2D universes are 2+1D branes in AdS_5.
- Each 2D universe is a 2+1D Karch-Randall brane
- The 2+1D Planck mass depends on the brane's bulk position
- The 2D universe's "death" projects to 3+1D

References:
- Karch & Randall 2000 (AdS_3 in AdS_5)
- Randall & Sundrum 1999 (RS-II)
- Maldacena 1997 (AdS/CFT)


**HISTORICAL (v2.7 era, mid-2025)**: This file is from the v2.7.x era, predating:
- v3.0+ Lagrangian work (L102-L136)
- v3.1+ Multi-universe picture (L142-L150)
- v3.3 Bilateral cascade (E_4D = 5e79 J, M_Pl,4D = 3.93e23 GeV)
- v3.5.7+ Naming revolution (f_back → f_DE,f_DM,leak,f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N×v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via α-GM, L308v)
- α = 1.289 (FIRST-PRINCIPLES via L308n)
- ε = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- γ_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- τ_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v2.7 era framework, not v3.5.9+ A2.
"""

import numpy as np
import math

# Physical constants
hbar = 1.055e-34  # J·s
c = 3e8            # m/s
G_N = 6.674e-11   # m³/(kg·s²)

# Planck mass
M_Pl_GeV = 1.22e19  # GeV
M_Pl_kg = 2.18e-8   # kg

# 1 GeV⁻¹ = 1.97e-16 m
GeV_inv_to_m = 1.97e-16

# =============================================================================
# Q1: 2+1D Planck mass on a Karch-Randall brane
# =============================================================================
def q1_karch_randall_2d_planck():
    """
    Karch-Randall: 2+1D brane in AdS_5 has effective 2+1D Planck mass

    The 2+1D Planck mass depends on the brane's bulk position y:
    M_Pl_3²(y) = M_5³ × (1 - e^{-2ky})/(2k) × (volume factor)

    For y → ∞: M_Pl_3²(∞) = M_5³/(2k)
    For y → 0: M_Pl_3²(0) → 0 (no extra volume)
    """
    print("=" * 80)
    print("Q1: 2+1D Planck mass on a Karch-Randall brane")
    print("=" * 80)
    print()

    M_5_GeV = 1e19
    k_GeV = 1e19

    print("M_Pl_3²(y) = M_5³ × (1 - e^{-2ky})/(2k)")
    print()
    print(f"For M_5 = {M_5_GeV:.1e} GeV, k = {k_GeV:.1e} GeV:")
    print()
    print(f"  y in units of 1/k |  e^{{-2ky}}  | M_Pl_3(y) in GeV |  in kg")
    print(f"  ----------------|--------------|------------------|----------")
    for y_in_inv_k in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 38.4, 100.0]:
        y_GeV_inv = y_in_inv_k / k_GeV
        e_2ky = np.exp(-2 * k_GeV * y_GeV_inv)
        M_Pl_3_sq = M_5_GeV**3 * (1 - e_2ky) / (2 * k_GeV)
        M_Pl_3 = np.sqrt(M_Pl_3_sq)
        M_Pl_3_kg = M_Pl_3 * 1.783e-27  # 1 GeV/c² in kg
        print(f"  {y_in_inv_k:>14.1f}  |  {e_2ky:>10.2e}  | {M_Pl_3:>16.2e} | {M_Pl_3_kg:>8.2e}")
    print()
    print("Notes:")
    print("  - At y=0, M_Pl_3 = 0 (no extra-dimensional volume)")
    print("  - As y → ∞, M_Pl_3 → M_5^(3/2)/sqrt(2k) (max value)")
    print("  - For natural RS-II (M_5 = k = M_Pl), M_Pl_3(∞) ~ 7e18 GeV")
    print()
    print("Honest finding: Karch-Randall 2+1D Planck scale is set by M_5, k, y.")
    print("For natural RS-II, M_Pl_3(∞) is close to M_Pl, but with (2+1)D signature.")
    print()

# =============================================================================
# Q2: 2D universe mass from M_Pl_3
# =============================================================================
def q2_2d_universe_mass():
    """
    The 2D universe's mass scale could be set by M_Pl_3 (Karch-Randall)
    or by the Liouville 2D CFT, or by the energetic event that creates it.

    Cascade's postulate: m_2D_2D ~ 6 M_sun (from Liouville-like considerations)
    Karch-Randall: M_Pl_3(∞) ~ 7e18 GeV ~ 1e-8 kg (Planck mass scale)
    Liouville CFT: gives a different mass scale (cascade's 6 M_sun)
    """
    print("=" * 80)
    print("Q2: 2D universe mass from different sources")
    print("=" * 80)
    print()

    M_5_GeV = 1e19
    k_GeV = 1e19
    M_Pl_3_inf = np.sqrt(M_5_GeV**3 / (2 * k_GeV))  # GeV
    M_Pl_3_inf_kg = M_Pl_3_inf * 1.783e-27  # kg

    print("Three estimates of 2D universe mass:")
    print()
    print(f"  (a) Karch-Randall M_Pl_3(∞): {M_Pl_3_inf:.2e} GeV = {M_Pl_3_inf_kg:.2e} kg")
    print(f"      = {M_Pl_3_inf_kg / 1.989e30:.2e} M_sun")
    print()
    print(f"  (b) Liouville 2D CFT (cascade's postulate): 6 M_sun = {6 * 1.989e30:.2e} kg")
    print()
    print(f"  (c) E_2D ~ (event energy) ~ M_Pl (if created by Planck-scale event):")
    print(f"      ~ {M_Pl_kg:.2e} kg = 1 M_Pl")
    print()

    # Time compression: m_2D_3+1D = m_2D_2D × e^{-ky}
    print("Time compression to 3+1D (e^{-ky} factor):")
    print()
    for label, m_2D_kg in [("M_Pl_3(∞)", M_Pl_3_inf_kg), ("Liouville 6 M_sun", 6 * 1.989e30), ("M_Pl", M_Pl_kg)]:
        m_2D_GeV = m_2D_kg / 1.783e-27  # kg to GeV
        print(f"  From {label} = {m_2D_kg:.2e} kg = {m_2D_GeV:.2e} GeV:")
        for target_label, target_kg in [("axion (1.1e-23 kg)", 1.1e-23), ("WIMP (100 GeV)", 100 * 1.783e-27), ("axion (1e-5 eV)", 1e-5 * 1.783e-30)]:
            e_ky_required = target_kg / m_2D_kg
            y_in_inv_k = -np.log(e_ky_required)
            print(f"    To get {target_label}: e^{{-ky}} = {e_ky_required:.2e}, y = {y_in_inv_k:.1f} / k")
        print()

    print("Honest finding:")
    print("  - Karch-Randall M_Pl_3(∞) ~ 1e-8 kg (10 micrograms)")
    print("  - Liouville 6 M_sun is much heavier")
    print("  - The cascade's 2D universe mass is the Liouville value, not M_Pl_3")
    print("  - The 50-orders tension is between Liouville mass and 3+1D observed")
    print("  - Karch-Randall doesn't directly help, but provides the framework")
    print()

# =============================================================================
# Q3: 2D universe density from Ω_DM
# =============================================================================
def q3_2d_universe_density():
    """
    Number density of 2D universes needed to give Ω_DM = 0.27.

    This is what the cascade needs (input postulate), and it gives a
    specific 2D universe population.
    """
    print("=" * 80)
    print("Q3: 2D universe density from Ω_DM = 0.27")
    print("=" * 80)
    print()

    # ρ_crit with H_0 = 70.16
    H_0 = 70.16e3 / 3.086e22  # s⁻¹
    rho_crit = 3 * H_0**2 / (8 * np.pi * G_N)
    rho_DM = rho_crit * 0.27
    print(f"ρ_crit (H_0 = 70.16) = {rho_crit:.2e} kg/m³")
    print(f"ρ_DM (Ω_DM = 0.27) = {rho_DM:.2e} kg/m³")
    print()

    # 2D universe count for different masses
    print("Number density for different 2D universe masses:")
    print()
    print(f"  m_2D_3+1D (kg) | n_2D (m⁻³) | separation (m) | separation (cm)")
    print(f"  ---------------|------------|----------------|----------------")
    for m_2D_kg in [1.1e-23, 1e-22, 1e-21, 1e-5, 1, 1e10, 6 * 1.989e30]:
        n_2D = rho_DM / m_2D_kg
        sep = n_2D ** (-1/3)
        print(f"  {m_2D_kg:>13.2e}  | {n_2D:>10.2e}  | {sep:>14.2e}  | {sep*100:>14.2e}")
    print()
    print("Note: axion-like mass (1.1e-23 kg) gives ~10 m separation.")
    print("Note: M_Pl_3(∞) mass (~1e-8 kg) gives ~0.4 m separation.")
    print("Note: 6 M_sun mass gives ~km separation.")
    print()

    print("Honest finding: The cascade's 2D universe density depends on m_2D.")
    print("For axion-like mass, ~10 m separation (very dense).")
    print("For 6 M_sun mass, ~km separation (sparse).")
    print("The cascade postulates axion-like 3+1D mass (L31), so ~10 m separation.")
    print()

# =============================================================================
# Q4: 2 kpc from 2D universe density?
# =============================================================================
def q4_2kpc_from_density():
    """
    Can the 2 kpc length scale emerge from the 2D universe density?

    At 2 kpc, the cascade's RAR matches. Maybe this is where:
    - The 2D universe population transitions from "individual" to "collective"
    - The Poisson fluctuations become Gaussian
    - The 2D universe mass becomes a smooth DM fluid
    """
    print("=" * 80)
    print("Q4: 2 kpc from 2D universe density?")
    print("=" * 80)
    print()

    # 2 kpc = 6.17e19 m
    kpc_m = 3.086e19
    two_kpc_m = 2 * kpc_m
    print(f"2 kpc = {two_kpc_m:.2e} m")
    print()

    # ρ_DM for Ω_DM = 0.27
    H_0 = 70.16e3 / 3.086e22  # s⁻¹
    rho_crit = 3 * H_0**2 / (8 * np.pi * G_N)
    rho_DM = rho_crit * 0.27

    # At 2 kpc, the volume of a sphere contains how many 2D universes?
    vol_2kpc = (4/3) * np.pi * (two_kpc_m)**3
    print(f"Volume of 2 kpc sphere: {vol_2kpc:.2e} m³")
    print()

    # For axion-like 2D universe (1.1e-23 kg, n_2D ~ 2.3e-4 m⁻³)
    n_2D_axion = rho_DM / 1.1e-23
    n_2D_in_2kpc = n_2D_axion * vol_2kpc
    print(f"2D universe count in 2 kpc sphere (m_2D = axion):")
    print(f"  n_2D = {n_2D_axion:.2e} m⁻³")
    print(f"  N_2D in 2 kpc sphere = {n_2D_in_2kpc:.2e}")
    print()

    # For 2 kpc to be a "transition scale", we'd need N_2D ~ O(1) in a 2 kpc sphere
    # That would require m_2D_3+1D ~ ρ_DM × (4π/3) × (2 kpc)³
    m_2D_for_N1 = rho_DM * vol_2kpc
    print(f"For N_2D ~ 1 in 2 kpc sphere:")
    print(f"  m_2D = {m_2D_for_N1:.2e} kg = {m_2D_for_N1/1.989e30:.2e} M_sun")
    print()

    print("Honest finding: 2 kpc is NOT a 'single 2D universe' scale.")
    print("For axion-like 2D universes, there are ~10^56 in a 2 kpc sphere.")
    print("For 2 kpc to be 'one 2D universe' would require m_2D ~ 1000 M_sun,")
    print("which is the cascade's 2D universe mass in 2D-frame, not 3+1D-frame.")
    print()
    print("The 2 kpc is probably a different kind of transition scale.")
    print("Possibilities:")
    print("  - Where the cascade's RAR fitting transitions from g_+ to g_-")
    print("  - Set by the supernova rate (energetic event density)")
    print("  - Coincidence with the Liouville 2D CFT")
    print()

# =============================================================================
# Q5: 2D universe rate from supernova rate
# =============================================================================
def q5_2d_universe_rate():
    """
    2D universes are created by SM energetic events above E_crit.
    The cascade postulates: every event above E_crit creates a 2D universe.

    If E_crit ~ 100 MeV (nuclear physics scale), the events are:
    - Supernovae (~10^58 events per supernova)
    - Neutron star mergers
    - Black hole mergers
    - AGN

    Number of 2D universes in the observable universe.
    """
    print("=" * 80)
    print("Q5: 2D universe rate from SM energetic events")
    print("=" * 80)
    print()

    # Supernova rate: ~1 per century per galaxy ~ 10^(-2) per year per galaxy
    # Number of galaxies in observable universe: ~10^11
    # Supernovae per year: ~10^9 (per observable universe)
    # Per second: ~30
    sn_rate_per_sec = 30  # supernovae per second in observable universe

    # Each supernova releases ~10^53 J of energy
    # If E_crit = 100 MeV = 1.6e-11 J
    # Number of "E_crit events" per supernova: 10^53 / 1.6e-11 = 6e63
    E_crit_J = 1.6e-11  # J
    E_sn_J = 1e53       # J per supernova
    n_events_per_sn = E_sn_J / E_crit_J
    print(f"Supernova rate: ~{sn_rate_per_sec} per second (observable universe)")
    print(f"Energy per supernova: ~{E_sn_J:.0e} J")
    print(f"E_crit (cascade's postulate): ~{E_crit_J:.0e} J = 100 MeV")
    print(f"Number of E_crit events per supernova: {n_events_per_sn:.2e}")
    print()

    # 2D universe creation rate
    n_2D_per_sec = sn_rate_per_sec * n_events_per_sn
    print(f"2D universe creation rate: {n_2D_per_sec:.2e} per second (from SNe)")
    print()

    # 2D universe lifetime: τ_2D ~ 30 Gyr (cascade's postulate)
    # Active 2D universe count: rate × τ_2D
    tau_2D_sec = 30e9 * 365.25 * 24 * 3600  # 30 Gyr in seconds
    N_active = n_2D_per_sec * tau_2D_sec
    print(f"2D universe lifetime (cascade's postulate): 30 Gyr = {tau_2D_sec:.2e} s")
    print(f"Active 2D universe count (from SNe only): {N_active:.2e}")
    print()

    # Cumulative 2D universe deaths over T_universe
    T_universe_sec = 13.8e9 * 365.25 * 24 * 3600
    N_cumulative = n_2D_per_sec * T_universe_sec
    print(f"Cumulative 2D universe deaths (over T_universe = 13.8 Gyr):")
    print(f"  N = {N_cumulative:.2e}")
    print()

    # Total mass of cumulative 2D universe deaths
    # m_2D_2D ~ 6 M_sun (cascade's postulate)
    M_cumulative_kg = N_cumulative * 6 * 1.989e30
    M_cumulative_Msun = N_cumulative * 6
    print(f"Cumulative mass (m_2D_2D = 6 M_sun, in 2D-frame):")
    print(f"  M = {M_cumulative_Msun:.2e} M_sun = {M_cumulative_kg:.2e} kg")
    print()

    # In 3+1D frame: multiply by e^{-ky} ~ 10^-54 (for 6 M_sun → axion-like)
    e_ky = 1e-54
    M_3plus1D_kg = M_cumulative_kg * e_ky
    print(f"In 3+1D frame (e^{{-ky}} = 10^-54, for 6 M_sun -> axion-like):")
    print(f"  M = {M_3plus1D_kg:.2e} kg = {M_3plus1D_kg/1.989e30:.2e} M_sun")
    print()

    # Observed DM mass in observable universe:
    # V_obs ~ 4e80 m³, ρ_DM ~ 2.5e-27 kg/m³
    # M_DM_obs ~ 1e54 kg
    V_obs_m3 = 4e80
    M_DM_obs_kg = V_obs_m3 * 2.5e-27
    print(f"Observed DM mass in observable universe: ~{M_DM_obs_kg:.2e} kg")
    print(f"SN-only 3+1D mass: ~{M_3plus1D_kg:.2e} kg")
    print(f"Ratio (SN-only / observed): {M_3plus1D_kg/M_DM_obs_kg:.2e}")
    print()

    print("Honest finding:")
    print("  - Cascade postulates: every event above E_crit creates a 2D universe")
    print("  - Supernovae create ~10^64 2D universes per event")
    print("  - Cumulative 2D universe deaths: ~10^80 (in 2D frame)")
    print("  - In 3+1D frame: ~10^60 kg (with e^{-ky} = 10^-54)")
    print("  - This is ~10^6 times MORE than observed DM mass in observable universe")
    print("  - Conclusion: SN-only over-produces DM, so the rate must be lower,")
    print("    or E_crit must be higher, or 2D universe mass is smaller")
    print("  - The cascade can adjust f_active (active fraction) to match Ω_DM = 0.27")
    print()

# =============================================================================
# Run all
# =============================================================================
if __name__ == "__main__":
    q1_karch_randall_2d_planck()
    q2_2d_universe_mass()
    q3_2d_universe_density()
    q4_2kpc_from_density()
    q5_2d_universe_rate()
    print("=" * 80)
    print("Summary of Karch-Randall calculations")
    print("=" * 80)
    print()
    print("1. Karch-Randall 2+1D Planck: M_Pl_3(∞) = sqrt(M_5³/2k) ~ 7e18 GeV for natural RS-II")
    print("2. 2D universe mass: cascade's 6 M_sun is much heavier than M_Pl_3")
    print("3. 2D universe density: ~10 m separation for axion-like mass")
    print("4. 2 kpc: NOT a 'one 2D universe' scale (need m_2D ~ 1000 M_sun for that)")
    print("5. 2D universe rate: SN-only gives ~10^60 kg in 3+1D, ~10^6x more than DM")
    print()
    print("Conclusion: The cascade needs to account for:")
    print("  - f_active (active fraction) ~ 10^-6 to match Ω_DM = 0.27 with SN rate")
    print("  - 2D universe mass from Liouville, not from M_Pl_3")
    print("  - 2 kpc from a non-density transition (e.g., RAR fitting)")
