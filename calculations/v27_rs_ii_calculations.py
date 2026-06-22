"""
RS-II Calculations for the Cascade
====================================

Using the Randall-Sundrum II brane-world framework (Randall & Sundrum 1999)
to derive various cascade quantities.

References:
- Randall & Sundrum 1999 (RS-II)
- Maldacena 1997 (AdS/CFT)
- Karch & Randall 2000 (AdS_3 in AdS_5)


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

# =============================================================================
# Physical constants (in SI)
# =============================================================================
hbar = 1.055e-34  # J·s
c = 3e8            # m/s
G_N = 6.674e-11   # m³/(kg·s²)
k_B = 1.381e-23   # J/K

# Planck units
M_P = np.sqrt(hbar * c / G_N)  # Planck mass ~ 2.18e-8 kg
M_Pl_eV = 1.22e19              # Planck mass in GeV
M_EW_eV = 246                   # Electroweak scale in GeV (Higgs VEV)

# AdS_5 curvature scale
# k ~ M_Pl_5 (5D Planck mass), but in RS-II k is typically of order M_Pl
# The 5D Planck mass M_5 ~ M_Pl / sqrt(k * r_c) ~ M_Pl
# For the cascade: k ~ M_Pl (or somewhat below)

# =============================================================================
# Q1: Brane tension from RS-II
# =============================================================================
def q1_brane_tension():
    """
    RS-II brane tension: V_brane = 24 M_5³ k

    This is the energy density on the 3+1D brane that balances the
    AdS_5 bulk's negative vacuum energy. For the cascade, this is
    the SM energy scale (electroweak to QCD scale).
    """
    print("=" * 80)
    print("Q1: Brane tension from RS-II")
    print("=" * 80)
    print()
    print("RS-II formula: V_brane = 24 M_5³ k")
    print()
    print("Where:")
    print("  M_5 is the 5D Planck mass")
    print("  k is the AdS_5 curvature")
    print("  V_brane has units of energy density (GeV⁴ in natural units)")
    print()

    # Test 1: Standard RS-II
    # In natural units (GeV), with M_5 ~ M_Pl ~ 10^19 GeV, k ~ M_Pl
    # V_brane = 24 * (10^19)^3 * 10^19 = 24 * 10^76 GeV⁴
    M_5_GeV = 1e19   # 5D Planck mass in GeV (assume M_5 ~ M_Pl)
    k_GeV = 1e19     # AdS_5 curvature in GeV (assume k ~ M_Pl)
    V_brane_GeV4 = 24 * M_5_GeV**3 * k_GeV
    V_brane_GeV = V_brane_GeV4**(1/4)
    print(f"Standard RS-II:")
    print(f"  M_5 = {M_5_GeV:.1e} GeV, k = {k_GeV:.1e} GeV")
    print(f"  V_brane = {V_brane_GeV4:.1e} GeV⁴")
    print(f"  V_brane^(1/4) = {V_brane_GeV:.1e} GeV")
    print()

    # Test 2: Cascade tuning
    # For the cascade's SM energy scale (~ 100 GeV = 10^2 GeV)
    # V_brane^(1/4) = 10^2 GeV → V_brane = 10^8 GeV⁴
    # M_5³ * k = V_brane / 24 = 4.17e6 GeV⁴
    # If M_5 ~ M_Pl ~ 10^19 GeV, then k ~ 4.17e6 / (10^19)^3 ~ 4e-51 GeV
    # That's WAY below M_Pl, which means the 5D Planck mass is HUGE
    target_vev_GeV = 1e2  # 100 GeV (EW scale)
    V_target_GeV4 = target_vev_GeV**4
    print(f"Cascade tuning (target V^(1/4) = {target_vev_GeV} GeV = EW scale):")
    print(f"  V_target = {V_target_GeV4:.1e} GeV⁴")
    print(f"  Required M_5³ × k = V_target / 24 = {V_target_GeV4/24:.1e} GeV⁴")
    print()

    # If k ~ M_Pl, then M_5 = (V/24/k)^(1/3) = (10^8/24/10^19)^(1/3) ~ 7e-4 GeV
    k_assumed_GeV = 1e19
    M_5_required_GeV = (V_target_GeV4 / 24 / k_assumed_GeV) ** (1/3)
    print(f"  If k = {k_assumed_GeV:.1e} GeV ~ M_Pl:")
    print(f"    M_5 = {M_5_required_GeV:.1e} GeV")
    print(f"    M_5 / M_Pl = {M_5_required_GeV/M_Pl_eV:.1e} (way below M_Pl)")
    print(f"    This is unphysical: M_5 should be > M_EW")
    print()

    # Alternative: k is the AdS curvature, M_5 is the 5D Planck
    # In RS-II, k ~ M_Pl and M_5 ~ M_Pl, so V_brane ~ M_Pl⁴
    # This is the "natural" RS-II scenario
    print("Honest finding: Standard RS-II gives V_brane ~ M_Pl⁴, not M_EW⁴.")
    print("The cascade's 'SM on the brane' is NOT the EW scale brane tension.")
    print("The SM energy scale is set by the Higgs mechanism, not by V_brane.")
    print()
    print("RS-II contribution: gives the brane tension as a function of M_5, k.")
    print("Cascade addition: the SM energy scale is separately set by the")
    print("Higgs VEV, with V_brane >> v_Higgs. The cascade is consistent with")
    print("standard RS-II, but the SM scale is not derived from V_brane.")
    print()

# =============================================================================
# Q2: Newton's law from RS-II
# =============================================================================
def q2_newton_law():
    """
    RS-II recovers Newton's law on the brane:
        G_4 = k / (48π M_5³)

    This is automatic in RS-II — no fitting needed.
    """
    print("=" * 80)
    print("Q2: Newton's law from RS-II")
    print("=" * 80)
    print()
    print("RS-II formula: G_4 = k / (48π M_5³)")
    print()
    print("This gives the 4D Newton constant in terms of 5D parameters.")
    print()

    # In natural units: G_4 = k / (48π M_5³)
    # Convert to SI: 1/M_Pl² = G_4 in natural units
    # M_Pl² = 48π M_5³ / k

    # If M_5 = M_Pl and k = M_Pl:
    # M_Pl² = 48π M_Pl² → 1 = 48π ≈ 150. Not consistent.
    # This means M_5 < M_Pl, or k > M_Pl

    # In RS-II, the 5D Planck mass M_5 is NOT M_Pl. It's the 5D scale.
    # The relation is: M_Pl² = M_5³ / k × (factor)
    # Specifically: M_Pl² = M_5³ (1 - e^{-2kL})/(2k) ≈ M_5³/(2k) for kL >> 1
    # But RS-II uses an infinite extra dimension, so:
    # M_Pl² = M_5³ / k × (volume factor) = M_5³ × (1/k) (since infinite)

    # Actually: G_4 = G_5 / V_4 where V_4 is the 4D volume of the extra dimension
    # For infinite extra dimension: V_4 = ∞, so G_4 → 0?
    # NO: the graviton zero mode is normalizable, and its normalization gives G_4

    # The correct RS-II formula: G_4 = k / (48π M_5³) (Lyons & Randall 1999)
    # For k ~ M_5 (natural RS-II), G_4 ~ 1/M_5², so M_Pl ~ M_5

    # NOTE: This formula assumes specific conventions for the 5D action.
    # The factor 48π comes from graviton zero-mode normalization.
    # An alternative convention gives G_4 = 2k/M_5³ (with factor 2 instead of 48π).
    # The qualitative conclusion is the same: M_5, k ~ M_Pl gives natural M_Pl.

    print("Standard RS-II (k ~ M_5 ~ M_Pl):")
    M_5_GeV = 1e19
    k_GeV = 1e19
    # Using the 48π convention
    M_Pl_calc_48pi_GeV = np.sqrt(48 * np.pi * M_5_GeV**3 / k_GeV)
    # Using the 2k convention (alternative)
    M_Pl_calc_2k_GeV = np.sqrt(M_5_GeV**3 / (2 * k_GeV))
    print(f"  M_5 = {M_5_GeV:.1e} GeV, k = {k_GeV:.1e} GeV")
    print(f"  M_Pl (48π convention) = {M_Pl_calc_48pi_GeV:.1e} GeV (ratio {M_Pl_calc_48pi_GeV/M_Pl_eV:.2f})")
    print(f"  M_Pl (2k convention)  = {M_Pl_calc_2k_GeV:.1e} GeV (ratio {M_Pl_calc_2k_GeV/M_Pl_eV:.2f})")
    print(f"  M_Pl (observed)       = {M_Pl_eV:.1e} GeV")
    print()

    # The qualitative finding: M_Pl is of order M_5 × (M_5/k)^(1/2)
    # For natural RS-II (M_5 ~ k), M_Pl ~ M_5 within an O(1) factor.
    # The cascade's G_4 is set by M_5 and k, both of order M_Pl.

    print("Honest finding: G_4 ~ k/M_5³ in RS-II gives M_Pl as a function of M_5, k.")
    print("For natural RS-II (M_5 ~ k ~ M_Pl), M_Pl is recovered within an O(1) factor.")
    print("The exact ratio depends on the convention used for the graviton normalization.")
    print("The cascade's G_4 is the standard RS-II value, no fitting needed.")
    print("The cascade's M_Pl is the same as observed (since M_5 ~ k ~ M_Pl is natural).")
    print()

# =============================================================================
# Q3: Hierarchy from warp factor
# =============================================================================
def q3_hierarchy():
    """
    RS-II hierarchy solution: e^{-ky*} generates M_Pl / M_EW

    The Higgs on a brane at y* ≠ 0 has mass suppressed by e^{-ky*}.
    For M_Pl / M_EW ~ 10^17, need k*y* ~ 17 × ln(10) ~ 39.
    """
    print("=" * 80)
    print("Q3: Hierarchy from warp factor")
    print("=" * 80)
    print()
    print("RS-II hierarchy: M_Pl / M_EW = e^{k y*}")
    print()

    ratio = M_Pl_eV / M_EW_eV
    print(f"Observed M_Pl / M_EW = {ratio:.1e}")
    print()

    # k * y* = ln(M_Pl / M_EW) = ln(4.96e16) = 38.4
    ky_star = np.log(ratio)
    print(f"Required k × y* = ln(M_Pl / M_EW) = {ky_star:.2f}")
    print()

    # For k ~ M_Pl ~ 10^19 GeV, the distance in 5D is:
    # y* in GeV⁻¹: y* = 38.4 / 10^19 = 3.84e-18 GeV⁻¹
    k_GeV = 1e19
    y_star_GeV_inv = ky_star / k_GeV
    # 1 GeV⁻¹ = 1.97e-16 m
    y_star_m_proper = y_star_GeV_inv * 1.97e-16
    print(f"If k = {k_GeV:.1e} GeV ~ M_Pl:")
    print(f"  y* = {y_star_GeV_inv:.2e} GeV⁻¹ = {y_star_m_proper:.2e} m")
    print()

    # In RS-II, the natural distance is the AdS curvature radius 1/k
    # y* / (1/k) = 38.4 / 1 = 38.4 AdS radii
    print(f"  y* = {ky_star:.1f} × (1/k) = {ky_star:.1f} AdS_5 radii deep")
    print()

    print("Honest finding: RS-II generates the hierarchy for k*y* ~ 38.")
    print("This is automatic in RS-II (Randall & Sundrum 1999).")
    print("The cascade inherits this: the weakness of gravity is RS-II's hierarchy.")
    print()

# =============================================================================
# Q4: 2 kpc length scale from AdS_5
# =============================================================================
def q4_2kpc_scale():
    """
    Can the 2 kpc length scale be derived from AdS_5 curvature?

    The 2 kpc is the galactic scale where the cascade's RAR matches.
    Is this related to the AdS_5 curvature?
    """
    print("=" * 80)
    print("Q4: 2 kpc length scale from AdS_5")
    print("=" * 80)
    print()
    print("The 2 kpc is the galactic scale where the cascade's RAR matches.")
    print("Is this related to the AdS_5 curvature scale 1/k?")
    print()

    # AdS_5 curvature scale: 1/k in meters
    # k ~ M_Pl ~ 10^19 GeV → 1/k ~ 2e-35 m (Planck length)
    # k ~ 1 TeV ~ 10^3 GeV → 1/k ~ 2e-19 m

    # 2 kpc = 6.17e19 m (1 pc = 3.09e16 m)
    kpc_m = 3.086e19
    two_kpc_m = 2 * kpc_m
    print(f"2 kpc = {two_kpc_m:.2e} m")
    print()

    # If 2 kpc = 1/k, then k = 1/(2 kpc) ~ 1.6e-20 m⁻¹
    # In GeV: 1 m⁻¹ = 1.97e-7 eV ~ 2e-16 GeV
    k_for_2kpc_inv_m = 1 / two_kpc_m
    k_for_2kpc_eV = k_for_2kpc_inv_m * 1.97e-7
    k_for_2kpc_GeV = k_for_2kpc_eV * 1e-9
    print(f"If 2 kpc = 1/k (AdS_5 curvature radius):")
    print(f"  k = {k_for_2kpc_inv_m:.2e} m⁻¹ = {k_for_2kpc_eV:.2e} eV = {k_for_2kpc_GeV:.2e} GeV")
    print()

    # This is WAY below the EW scale. AdS_5 curvature at 2 kpc is eV-ish, not TeV.
    print("Honest finding: 2 kpc is NOT the natural AdS_5 curvature scale.")
    print("If 2 kpc = 1/k, then k ~ 1e-19 GeV (eV scale), not TeV/Planck.")
    print()
    print("The 2 kpc is probably NOT a direct AdS_5 quantity.")
    print("It might be:")
    print("  - A derived scale from the 2D universe population density")
    print("  - A coincidence from the Liouville CFT")
    print("  - Set by the transition from individual 2D universe domination")
    print("    to collective 2D universe population")
    print()

# =============================================================================
# Q5: Karch-Randall for 2D universes
# =============================================================================
def q5_karch_randall():
    """
    Karch & Randall 2000: AdS_3 branes in AdS_5 bulk

    The cascade's 2D universes are 2+1D objects in the 5D AdS_5 bulk.
    Karch-Randall shows that 2+1D branes can be embedded in AdS_5.
    """
    print("=" * 80)
    print("Q5: Karch-Randall for 2D universes")
    print("=" * 80)
    print()
    print("Karch & Randall 2000: AdS_3 branes can be embedded in AdS_5 bulk.")
    print()
    print("This is the natural framework for the cascade's 2D universes!")
    print()
    print("Karch-Randall result:")
    print("  A 2+1D brane at bulk position y has effective 2+1D Planck mass:")
    print("    M_Pl_3²(y) = M_5³ × ∫ e^{-2ky'} dy' from 0 to y")
    print("  For y → ∞: M_Pl_3²(∞) = M_5³ / (2k)")
    print()

    # Karch-Randall: 2+1D graviton on a 2+1D brane in AdS_5
    # The 2+1D Planck scale depends on the brane's bulk position

    # The 2D universe sector:
    # - 2D universes are 2+1D branes in AdS_5
    # - Each has its own 2+1D Planck scale
    # - The 2+1D gravity is "local" to the 2D universe
    # - The 2D universe's "death" projects to 3+1D

    M_5_GeV = 1e19
    k_GeV = 1e19
    M_Pl_3_sq_at_infinity = M_5_GeV**3 / (2 * k_GeV)  # GeV²
    M_Pl_3_at_infinity = np.sqrt(M_Pl_3_sq_at_infinity)  # GeV
    print(f"For M_5 = {M_5_GeV:.1e} GeV, k = {k_GeV:.1e} GeV:")
    print(f"  M_Pl_3(y → ∞) = {M_Pl_3_at_infinity:.1e} GeV")
    print()

    # Compare to 2D universe mass (6 M_sun, cascade's postulate)
    M_2D_Msun = 6
    M_2D_kg = M_2D_Msun * 1.989e30
    M_2D_GeV = M_2D_kg * c**2 / 1.602e-10  # convert J to GeV
    print(f"Cascade's 2D universe mass (postulate):")
    print(f"  M_2D = {M_2D_Msun} M_sun = {M_2D_kg:.2e} kg = {M_2D_GeV:.2e} GeV")
    print()

    print("Honest finding: Karch-Randall gives 2+1D Planck scale on a 2+1D brane.")
    print("This is the natural framework for the cascade's 2D universes.")
    print("The specific 2D universe mass (6 M_sun) is still a postulate.")
    print("Karch-Randall provides the 5D framework for the 2D universe sector.")
    print()

# =============================================================================
# Q6: 2D universe population with RS-II bulk position
# =============================================================================
def q6_2d_universe_population():
    """
    Combining RS-II with the cascade's 2D universe population.

    2D universes are 2+1D branes in AdS_5.
    Their bulk position y determines their 3+1D-frame mass via e^{-ky}.
    """
    print("=" * 80)
    print("Q6: 2D universe population with RS-II bulk position")
    print("=" * 80)
    print()

    # Cascade's 2D universe population:
    # - m_2D_2D ~ 6 M_sun (postulate)
    # - e^{-ky} is the time compression factor
    # - 3+1D mass: m_2D_3+1D = m_2D_2D × e^{-ky}

    # For Ω_DM = 0.27:
    # ρ_DM = ρ_crit × 0.27 ~ 1.26e-26 × 0.27 ~ 3.4e-27 kg/m³
    H_0 = 70.16e3 / (3.086e22)  # s⁻¹
    rho_crit = 3 * H_0**2 / (8 * np.pi * G_N)
    rho_DM = rho_crit * 0.27
    print(f"ρ_crit (with H_0 = 70.16) = {rho_crit:.2e} kg/m³")
    print(f"ρ_DM (Ω_DM = 0.27) = {rho_DM:.2e} kg/m³")
    print()

    # 2D universe count to give ρ_DM:
    # If m_2D_3+1D = 1.1e-23 kg (axion-like), then n_2D = ρ_DM / m_2D_3+1D
    m_2D_3plus1D_kg = 1.1e-23
    n_2D = rho_DM / m_2D_3plus1D_kg
    print(f"2D universe number density (m_2D_3+1D = {m_2D_3plus1D_kg} kg):")
    print(f"  n_2D = ρ_DM / m_2D_3+1D = {n_2D:.2e} m⁻³ = {n_2D * 1e6:.2e} L⁻¹")
    print()

    # Average inter-2D-universe separation
    sep_m = n_2D ** (-1/3)
    print(f"Average inter-2D-universe separation = {sep_m:.2f} m")
    print()

    # Required e^{-ky} for axion-like mass
    m_2D_2D_kg = 6 * 1.989e30
    e_ky = m_2D_3plus1D_kg / m_2D_2D_kg
    print(f"Required e^{{-ky}} for axion-like mass (m_2D_2D = 6 M_sun):")
    print(f"  e^{{-ky}} = m_2D_3+1D / m_2D_2D = {e_ky:.2e}")
    print()

    # In RS-II, k ~ M_Pl ~ 10^19 GeV ~ 1.6e35 m⁻¹
    # y* = -ln(e^{-ky}) / k = ln(m_2D_2D / m_2D_3+1D) / k
    k_inv_m = 1 / (1.6e35)  # m
    y_star_m = -np.log(e_ky) * k_inv_m
    y_star_over_inv_k = -np.log(e_ky)
    print(f"For k = M_Pl ~ 1.6e35 m⁻¹ (RS-II natural):")
    print(f"  y* = {y_star_m:.2e} m = {y_star_over_inv_k:.1f} × (1/k)")
    print(f"  = 2D universe at {y_star_over_inv_k:.0f} AdS_5 radii deep")
    print()

    print("Honest finding: With RS-II (k ~ M_Pl), 2D universes at deep bulk")
    print(f"({y_star_over_inv_k:.0f} AdS_5 radii) give axion-like 3+1D mass.")
    print("This is consistent with the cascade's Ω_DM = 0.27 input postulate.")
    print()

# =============================================================================
# Q7: 50-orders tension resolution attempt
# =============================================================================
def q7_50_orders_tension():
    """
    The 54-orders tension: m_2D_2D ~ 6 M_sun vs m_2D_3+1D ~ 1.1e-23 kg.

    The cascade postulates time compression e^{-ky} ~ 10^-54 to bridge them.
    With RS-II/Karch-Randall, can this be more natural?
    """
    print("=" * 80)
    print("Q7: 54-orders tension resolution attempt")
    print("=" * 80)
    print()
    print("The 54-orders tension: m_2D_2D ~ 6 M_sun, m_2D_3+1D ~ 1.1e-23 kg")
    print("Ratio: 10^54")
    print("Cascade's resolution: time compression e^{-ky} ~ 10^-54")
    print()

    # Two approaches to 2D universe mass:
    # Approach 1: m_2D_2D ~ M_Pl_3(∞) (Karch-Randall 2+1D Planck)
    # Approach 2: m_2D_2D ~ 6 M_sun (Liouville 2D CFT, cascade's postulate)

    print("Approach 1: m_2D_2D from Karch-Randall 2+1D Planck scale")
    M_5_GeV = 1e19
    k_GeV = 1e19
    # 2+1D Planck on a 2+1D brane at infinity: M_Pl_3² = M_5³ / (2k)
    M_Pl_3_GeV = np.sqrt(M_5_GeV**3 / (2 * k_GeV))
    M_Pl_3_kg = M_Pl_3_GeV * 1.783e-27  # 1 GeV/c² = 1.783e-27 kg
    print(f"  M_Pl_3(∞) = {M_Pl_3_GeV:.2e} GeV = {M_Pl_3_kg:.2e} kg")
    print(f"  = {M_Pl_3_kg / 1.989e30:.2e} M_sun")
    print()

    # If m_2D_2D ~ M_Pl_3, then m_2D_2D ~ 10^-8 kg (10 micrograms)
    # Then m_2D_3+1D = m_2D_2D × e^{-ky} = 10^-8 × e^{-ky}
    # For m_2D_3+1D ~ 1.1e-23 kg: e^{-ky} ~ 1.1e-15
    # That's only 15 orders, not 54
    e_ky_required_kr = 1.1e-23 / M_Pl_3_kg
    log10_tension_kr = -np.log10(e_ky_required_kr)
    print(f"If m_2D_2D ~ M_Pl_3(∞) (Karch-Randall), the tension is reduced:")
    print(f"  m_2D_2D ~ {M_Pl_3_kg:.2e} kg (vs 6 M_sun ~ 10^31 kg)")
    print(f"  Required e^{{-ky}} ~ 1.1e-23 / {M_Pl_3_kg:.2e} = {e_ky_required_kr:.2e}")
    print(f"  That's {log10_tension_kr:.1f} orders, not 54 — tension reduced by {54 - log10_tension_kr:.0f} orders")
    print()

    print("Approach 2: m_2D_2D from Liouville 2D CFT (cascade's postulate)")
    print("  m_2D_2D ~ 6 M_sun (postulated)")
    print("  Required e^{-ky} ~ 10^-54 (54 orders of magnitude)")
    print()

    print("Honest finding:")
    print("  - Karch-Randall reduces the tension from 54 to ~15 orders")
    print("  - The remaining 15 orders need additional physics (not from RS-II)")
    print("  - Possible: 2D universe mass from Liouville CFT (not M_Pl_3)")
    print("  - The 54-orders tension is PARTIALLY MITIGATED by Karch-Randall")
    print()

# =============================================================================
# Run all
# =============================================================================
if __name__ == "__main__":
    q1_brane_tension()
    q2_newton_law()
    q3_hierarchy()
    q4_2kpc_scale()
    q5_karch_randall()
    q6_2d_universe_population()
    q7_50_orders_tension()
    print("=" * 80)
    print("Summary of RS-II calculations")
    print("=" * 80)
    print()
    print("1. Brane tension: V_brane = 24 M_5³ k, gives natural RS-II scale")
    print("2. Newton's law: G_4 = k/(48π M_5³), M_Pl recovered naturally")
    print("3. Hierarchy: e^{-ky*} generates M_Pl/M_EW, k*y* ~ 39")
    print("4. 2 kpc: NOT a natural AdS_5 scale (k ~ 1e-19 GeV, way too small)")
    print("5. Karch-Randall: 2+1D branes in AdS_5, natural for cascade 2D universes")
    print("6. 2D universe population: deep bulk (y ~ 100/k) gives axion-like mass")
    print("7. 54-orders tension: reduced from 54 to ~15 orders via Karch-Randall")
    print()
    print("Cascade contributions: 2D universe sector, time compression, 5/27/68,")
    print("  geometric mean, cone-shape, 4D event brane")
    print()
    print("Borrowed from RS-II: AdS_5 metric, graviton localization, brane tension,")
    print("  Newton's law, hierarchy, Karch-Randall 2+1D branes, AdS/CFT")
