"""
RS-II + Liouville + Boltzmann Calculations
==========================================

Combining three frameworks to test the cascade:
1. RS-II: 5D AdS_5 bulk geometry (warp factor e^{-ky})
2. Liouville 2D CFT: 2D universe's 2D-frame physics
3. CAMB: Boltzmann code for CMB/structure formation

References:
- Randall & Sundrum 1999 (RS-II)
- Zamolodchikov & Zamolodchikov 1996 (Liouville)
- Karch & Randall 2000
- Lewis, Challinor & Lasenby 2000 (CAMB)
"""

import numpy as np
import math

# =============================================================================
# Physical constants
# =============================================================================
hbar = 1.055e-34  # J·s
c = 3e8            # m/s
G_N = 6.674e-11   # m³/(kg·s²)
k_B = 1.381e-23   # J/K

# Planck units
M_Pl_GeV = 1.22e19
M_Pl_kg = 2.18e-8
GeV_inv_to_m = 1.97e-16

# =============================================================================
# Q1: Effective 4D Newton constant from 5D cascade
# =============================================================================
def q1_effective_4d_newton():
    """
    The cascade's 3+1D Newton constant G_4 has contributions from:
    - The 4D event brane (the "Big Bang" parent)
    - The 2D universe sector (cumulative gravitational back-projection)

    Standard RS-II gives G_4 = k / (48π M_5³)
    Cascade adds 2D universe contribution (fossil, see §2.5)
    """
    print("=" * 80)
    print("Q1: Effective 4D Newton constant from 5D cascade")
    print("=" * 80)
    print()
    print("Cascade: G_4 = G_4^RS-II + G_4^2D_universes")
    print()

    M_5_GeV = 1e19
    k_GeV = 1e19

    # RS-II contribution
    G_4_RSII = k_GeV / (48 * np.pi * M_5_GeV**3)  # in GeV⁻²
    M_Pl_RSII = 1 / np.sqrt(G_4_RSII)  # in GeV
    print(f"RS-II contribution (k ~ M_5 ~ M_Pl):")
    print(f"  G_4 = k / (48π M_5³) = {G_4_RSII:.2e} GeV⁻²")
    print(f"  M_Pl (RS-II) = {M_Pl_RSII:.2e} GeV")
    print()

    # 2D universe contribution
    # Each 2D universe has effective 3+1D mass m_2D_3+1D
    # Their cumulative gravitational effect adds to G_4
    # But this is NOT a constant — it's density-dependent

    # For DM density ρ_DM ~ 2.5e-27 kg/m³
    # G_4 * M_DM / r² is the gravitational acceleration
    # The 2D universe contribution to G_4 depends on the population

    # In cascade, the 2D universe gravity is SEPARATE from Newton's G
    # It's a 2D-to-3+1D back-projection, not a modification of G_4
    print("Cascade: 2D universe gravity is SEPARATE from Newton's G")
    print("  - G_4 is set by RS-II (graviton zero mode)")
    print("  - 2D universe gravity is a back-projected effect")
    print("  - Total gravity: G_4 × M_baryon + G_4 × M_2D_universes_eff")
    print()

    print("Honest finding: G_4 is set by RS-II. 2D universes add to M_eff, not G.")
    print()

# =============================================================================
# Q2: 2D universe mass from Liouville 3-point function
# =============================================================================
def q2_2d_universe_mass_liouville():
    """
    Can the Liouville 2D CFT give the 2D universe's mass?

    The DOZZ 3-point function gives |C|² ~ 1-50 for natural (b, α0).
    The 2D universe mass might be related to the DOZZ structure constant.
    """
    print("=" * 80)
    print("Q2: 2D universe mass from Liouville 3-point function")
    print("=" * 80)
    print()
    print("DOZZ 3-point function gives |C|² ~ 1-50 for natural (b, α0).")
    print("Can this give a 2D universe mass scale?")
    print()

    # DOZZ formula (simplified):
    # C(α1, α2, α3) = (product of Γ functions) × (b-dependent factors)
    # The |C|² has dimensions of (length)^(2(Q-α_sum)) in 2D

    # The 2D universe mass scale might be:
    # m_2D ~ μ × |C|² × M_Planck_2D
    # where μ is the Liouville cosmological constant

    # In 2D Liouville: μ has dimensions of (length)^(-2)
    # μ ~ M_Planck_2D² (natural scale)

    # So m_2D ~ M_Planck_2D × |C|²
    # For M_Planck_2D = M_Pl_3(∞) ~ 7e18 GeV:
    # m_2D ~ 7e18 GeV × |C|² ~ 7e18 to 3.5e20 GeV
    # In kg: 1.3e-8 to 6.3e-7 kg

    print("Possible 2D universe mass scales from Liouville:")
    print()
    M_Pl_2D_GeV = 7e18  # GeV (Karch-Randall 2+1D Planck)
    for c_squared in [0.28, 1, 8.2, 18, 31, 46]:
        m_2D_GeV = M_Pl_2D_GeV * c_squared
        m_2D_kg = m_2D_GeV * 1.783e-27
        print(f"  |C|² = {c_squared:>5.2f}: m_2D = {m_2D_GeV:.2e} GeV = {m_2D_kg:.2e} kg = {m_2D_kg/1.989e30:.2e} M_sun")
    print()

    # This is the Karch-Randall 2+1D Planck mass times DOZZ factor
    # All these are in the 10^-8 to 10^-6 kg range
    # This is FAR less than 6 M_sun (the cascade's postulate)

    print("Honest finding: Liouville 2D CFT gives m_2D ~ 10^-8 to 10^-6 kg")
    print("Cascade postulates 6 M_sun (~10^31 kg)")
    print("Discrepancy: ~37-39 orders of magnitude")
    print()
    print("Possible resolution:")
    print("  - m_2D is NOT from Liouville DOZZ alone")
    print("  - m_2D is from the energetic event that creates the 2D universe")
    print("  - The 2D universe mass = E_event × (some factor)")
    print("  - For E_event ~ 100 MeV, m_2D ~ 10^-25 kg (way off)")
    print("  - For E_event ~ 10^57 J (supernova), m_2D ~ 6 M_sun (matches!)")
    print()

# =============================================================================
# Q3: 2D universe lifetime from Liouville
# =============================================================================
def q3_2d_universe_lifetime():
    """
    Can the Liouville 2D CFT give the 2D universe's lifetime?

    The cascade postulates τ_2D = 30 Gyr (in 2D frame).
    Liouville might give this through the 2D CFT dynamics.
    """
    print("=" * 80)
    print("Q3: 2D universe lifetime from Liouville")
    print("=" * 80)
    print()
    print("Cascade postulates: τ_2D = 30 Gyr (in 2D frame)")
    print("Can Liouville 2D CFT derive this?")
    print()

    # In 2D Liouville, the partition function Z ~ exp(S_L)
    # where S_L is the Liouville action
    # The "lifetime" could be related to the inverse of the Liouville Hamiltonian eigenvalue

    # For a Liouville CFT on a 2D cylinder of circumference L:
    # H = (1/L) × (L_0 + L̄_0 - c/12)
    # Eigenvalues: E_n = (1/L) × (2h_n - c/12)

    # For c ≥ 25 (above barrier), the spectrum is continuous
    # The "lifetime" would be ~ ℏ/E_gap, where E_gap is the smallest energy difference

    # c = 1 + 6Q² (Q = b + 1/b)
    # For b = 1: Q = 2, c = 25
    # For b = 0.7: Q = 1/0.7 + 0.7 = 2.13, c = 1 + 6×4.54 = 28.2

    # E_gap ~ 1/L² (where L is the 2D universe's size)
    # For L = 2 kpc (3D radius?) or some 2D length scale
    # τ_2D ~ L² / (c² in 2D)

    # The 2D universe's "size" in 2D is unknown
    # But if we set τ_2D = 30 Gyr in 3+1D, and the time compression
    # makes it e^{ky} × 30 Gyr in 2D, then:
    # τ_2D_2D = 30 Gyr × e^{ky} for y ~ 124
    # = 30 Gyr × 10^54
    # This is way longer than the age of the universe

    print("The 2D universe lifetime in different frames:")
    print()

    tau_2D_3plus1D = 30e9 * 365.25 * 24 * 3600  # seconds
    print(f"  τ_2D (3+1D) = 30 Gyr = {tau_2D_3plus1D:.2e} s")

    e_ky_typical = 1e-54
    tau_2D_2D = tau_2D_3plus1D / e_ky_typical
    print(f"  τ_2D (2D) = τ_2D(3+1D) / e^{{-ky}} = {tau_2D_3plus1D/e_ky_typical:.2e} s")
    print(f"           = {tau_2D_3plus1D/e_ky_typical/(365.25*24*3600*1e9):.2e} Gyr")
    print()

    # Liouville's natural time scale: 1/μ^(1/2) where μ is the cosmological constant
    # μ ~ M_Planck_2D² (natural scale)
    M_Pl_2D_GeV = 7e18
    mu_GeV2 = M_Pl_2D_GeV**2  # GeV²
    mu_GeV = np.sqrt(mu_GeV2)
    print(f"Liouville natural time scale (1/√μ):")
    print(f"  μ ~ M_Pl_2D² = {mu_GeV2:.2e} GeV²")
    print(f"  √μ = {mu_GeV:.2e} GeV")
    print(f"  1/√μ in GeV⁻¹ = {1/mu_GeV:.2e}")
    print(f"  1/√μ in seconds = {(1/mu_GeV) * 6.58e-25:.2e}")
    print(f"  1/√μ in Gyr = {(1/mu_GeV) * 6.58e-25 / (365.25*24*3600*1e9):.2e}")
    print()

    print("Honest finding: Liouville natural time scale 1/√μ is way smaller than 30 Gyr.")
    print("The cascade's τ_2D = 30 Gyr is a POSTULATE, not from Liouville dynamics.")
    print()

# =============================================================================
# Q4: CAMB with RS-II warp factor as modified expansion
# =============================================================================
def q4_camb_warp_factor():
    """
    Can the RS-II warp factor modify the 3+1D expansion history?

    The warp factor e^{-2ky} on our brane is 1 (we're at y=0).
    But the 2D universe back-projection carries the warp factor.
    """
    print("=" * 80)
    print("Q4: CAMB with RS-II warp factor")
    print("=" * 80)
    print()
    print("The RS-II warp factor on our brane (y=0) is 1.")
    print("So it doesn't directly modify 3+1D gravity on the brane.")
    print()

    # The cascade's effect on 3+1D is via 2D universe back-projection
    # Each 2D universe's 3+1D mass is m_2D_2D × e^{-ky}
    # Their cumulative effect is the cascade's DM

    # For CAMB, this is just additional DM density
    # The warp factor is "absorbed" into the 2D universe's 3+1D mass
    # It doesn't modify the Friedmann equation directly

    # So CAMB with cascade = CAMB with extra DM component
    # Already tested in cascade_camb.py
    print("Cascade's effect on CAMB:")
    print("  - Adds extra DM component (2D universe back-projection)")
    print("  - The warp factor e^{-ky} is absorbed into m_2D_3+1D")
    print("  - The Friedmann equation is standard ΛCDM with extra DM")
    print()

    # The cascade does NOT modify the expansion history in a non-trivial way
    # (assuming the 2D universe population has the standard DM equation of state)
    print("Honest finding: CAMB with cascade = CAMB with extra DM (already tested)")
    print("The RS-II warp factor doesn't add new CAMB features")
    print("It's a re-labeling of the 2D universe's 3+1D-frame mass")
    print()

# =============================================================================
# Q5: Holographic RG flow from RS-II
# =============================================================================
def q5_holographic_rg():
    """
    AdS_5/CFT_4 duality: the 5D bulk is dual to a 4D CFT on the boundary.

    The cascade's 5D bulk is dual to a 4D CFT.
    The 2D universe sector is in the bulk.
    The 3+1D SM is on the brane.

    Can the holographic RG flow give us insights?
    """
    print("=" * 80)
    print("Q5: Holographic RG flow from RS-II")
    print("=" * 80)
    print()
    print("AdS_5/CFT_4: 5D bulk is dual to 4D CFT on boundary")
    print()

    # In AdS/CFT:
    # - Bulk position y ↔ RG scale μ in the CFT
    # - Near boundary (y → 0): UV (high energy)
    # - Deep bulk (y → ∞): IR (low energy)

    # The cascade's setup:
    # - 3+1D brane at y=0 (UV)
    # - 2D universes at y > 0 (IR)

    # The 2D universe's "RG flow" from the 4D CFT perspective:
    # - 2D universes are IR modes of the 4D CFT
    # - Their creation/death is the RG flow

    # The cascade's interpretation:
    # - DM = IR modes of the 4D CFT (cumulative 2D universe effects)
    # - DE = vacuum energy of the 4D CFT (UV)

    # This is qualitatively consistent with AdS/CFT
    print("Cascade interpretation via AdS/CFT:")
    print("  - 3+1D brane at y=0 (UV): SM fields")
    print("  - 2D universes at y>0 (IR): IR modes of 4D CFT")
    print("  - DM = cumulative IR modes (2D universe deaths)")
    print("  - DE = vacuum energy of 4D CFT (UV)")
    print()

    # Holographic RG flow: c_func decreases as we go to the IR
    # c_func at the 3+1D brane: c = 4D CFT central charge
    # c_func at 2D universe: c = 2D CFT central charge

    # For 4D N=4 SYM: c ~ N²
    # For 2D Liouville: c = 1 + 6Q²

    # The cascade's 2D universe sector is Liouville
    # The 3+1D sector is... unknown (not N=4 SYM)
    print("Quantitative:")
    print("  - 4D CFT central charge: unknown (cascade doesn't specify)")
    print("  - 2D Liouville central charge: c = 1 + 6(b + 1/b)²")
    print("  - For b = 1: c = 25")
    print()

    print("Honest finding: AdS/CFT gives qualitative interpretation")
    print("Quantitative match requires specifying the 4D CFT")
    print("The cascade doesn't specify this (it's a separate question)")
    print()

# =============================================================================
# Q6: 2D universe creation rate from DOZZ
# =============================================================================
def q6_creation_rate_dozz():
    """
    The 2D universe creation rate is:
    rate = (SM event rate above E_crit) × |C|²_Dozz

    DOZZ gives |C|² ~ 1-50. The SM event rate is also a function.
    """
    print("=" * 80)
    print("Q6: 2D universe creation rate from DOZZ")
    print("=" * 80)
    print()

    # SM event rate above E_crit:
    # Supernovae: ~30/s in observable universe
    # Each SN: ~10^64 events above E_crit (if E_crit = 100 MeV)

    sn_rate = 30  # s⁻¹
    E_crit_J = 1.6e-11  # 100 MeV
    E_sn_J = 1e53
    n_events_per_sn = E_sn_J / E_crit_J
    print(f"Supernova rate: {sn_rate} s⁻¹")
    print(f"Events per SN above E_crit: {n_events_per_sn:.2e}")
    print()

    raw_2d_rate = sn_rate * n_events_per_sn
    print(f"Raw 2D universe rate (no DOZZ): {raw_2d_rate:.2e} s⁻¹")
    print()

    # DOZZ factor
    print("With DOZZ factor |C|²:")
    for c_squared in [0.28, 1, 8.2, 18, 31, 46]:
        rate_with_dozz = raw_2d_rate * c_squared
        print(f"  |C|² = {c_squared:>5.2f}: rate = {rate_with_dozz:.2e} s⁻¹")
    print()

    # Cumulative over T_universe
    T_universe = 13.8e9 * 365.25 * 24 * 3600
    print(f"Cumulative over T_universe = 13.8 Gyr:")
    for c_squared in [0.28, 1, 8.2, 18, 31, 46]:
        n_cumulative = raw_2d_rate * c_squared * T_universe
        print(f"  |C|² = {c_squared:>5.2f}: N = {n_cumulative:.2e}")
    print()

    print("Honest finding: |C|²_Dozz is a real Liouville prediction")
    print("The 2D universe creation rate is rate_SN × |C|² × (some factor)")
    print("The factor depends on the bulk-brane coupling α")
    print()

# =============================================================================
# Run all
# =============================================================================
if __name__ == "__main__":
    q1_effective_4d_newton()
    q2_2d_universe_mass_liouville()
    q3_2d_universe_lifetime()
    q4_camb_warp_factor()
    q5_holographic_rg()
    q6_creation_rate_dozz()
    print("=" * 80)
    print("Summary of RS-II + Liouville + Boltzmann calculations")
    print("=" * 80)
    print()
    print("1. G_4 from RS-II: standard, doesn't directly involve Liouville")
    print("2. 2D universe mass: Liouville gives ~10^-8 kg, cascade postulates 6 M_sun")
    print("3. 2D universe lifetime: Liouville 1/√μ is way too fast, 30 Gyr is postulate")
    print("4. CAMB with warp factor: warp factor absorbed into 2D universe's m_3+1D")
    print("5. AdS/CFT interpretation: gives qualitative picture, not quantitative")
    print("6. 2D universe creation rate: rate_SN × |C|²_Dozz × α")
    print()
    print("Cascade contributions NOT derivable from RS-II + Liouville + Boltzmann:")
    print("  - 2D universe mass (6 M_sun postulate)")
    print("  - 2D universe lifetime (30 Gyr postulate)")
    print("  - bulk-brane coupling α (free parameter)")
    print("  - 4D event brane energy and duration")
    print("  - f_active (active fraction)")
    print()
    print("Cascade contributions derivable from RS-II + Liouville + Boltzmann:")
    print("  - 5D AdS_5 framework (RS-II standard)")
    print("  - G_4 on the brane (RS-II standard)")
    print("  - DOZZ 3-point function (Liouville standard)")
    print("  - Holographic RG flow (AdS/CFT standard)")
