"""
Trial and Error: 2D Universe Mass and Lifetime (v2)
====================================================

KEY INSIGHT FROM USER: The 30 Gyr in 2D is an ASSUMPTION.
The 33 s in 3+1D is the empirical mapping (from ℓ/c dimensional time rule).

So the cascade's actual constraint is:
- 2D universe lives 33 s in 3+1D (this is the empirical mapping)
- This determines e^{-ky} (the time compression)
- Then m_2D_3+1D = m_2D_2D × e^{-ky} is fixed once we know m_2D_2D

Let me work this through carefully.

The dimensional time-dilation rule: ℓ/c, where ℓ is some natural length.
For 33 s: ℓ = 33 × c = 33 × 3e8 = 1e10 m = 10 billion meters
That's about 0.07 AU (between Earth and Sun).

If e^{-ky} ~ 1 (no compression), then 2D lifetime = 3+1D lifetime = 33 s
If e^{-ky} = 1e-17, then 2D lifetime = 33 s × 1e-17 = very short

Wait, let me think again. The 33 s is the 3+1D-frame lifetime.
The 2D-frame lifetime is 33 s × e^{ky} for e^{-ky} << 1.

Hmm, this is getting confusing. Let me use the cascade's explicit formula:
dτ_2D = e^{-ky} dt_4D

If a 2D universe's 3+1D lifetime is τ_3+1D = 33 s, and 2D lifetime is τ_2D:
τ_2D = e^{-ky} × τ_3+1D = 33 s × e^{-ky}

Wait, that's only true if both lifetimes are computed the same way.

Actually: dτ_2D = e^{-ky} dt_4D means proper time on 2D = warp × coordinate time.
If a 2D universe "lives" for τ_2D in its own proper time, and the 3+1D
observer sees it live for τ_3+1D in 3+1D time:

The relationship: τ_2D = e^{-ky} × τ_3+1D

This is because during τ_3+1D seconds of 3+1D time, the 2D universe's
proper time advances by e^{-ky} × τ_3+1D seconds (in 2D's time).

For τ_3+1D = 33 s and τ_2D = 30 Gyr:
30 Gyr = e^{-ky} × 33 s
e^{-ky} = 30 Gyr / 33 s = 9.46e17 s / 33 s = 2.87e16

But e^{-ky} should be ≤ 1, so 2.87e16 is impossible.

OR maybe I have the formula direction wrong:
dτ_2D = e^{-ky} dt_4D → τ_2D = e^{-ky} × τ_3+1D (this is what I had)
dτ_2D = e^{ky} dt_4D → τ_2D = e^{ky} × τ_3+1D (the other way)

If dτ_2D = e^{ky} dt_4D, then 1s in 3+1D = e^{ky} s in 2D (long 2D time).
For τ_2D = 30 Gyr = 9.46e17 s and τ_3+1D = 33 s:
e^{ky} = 9.46e17 / 33 = 2.87e16
e^{-ky} = 1/e^{ky} = 3.49e-17

This gives e^{-ky} = 3.5e-17. For m_2D_2D = 6 M_sun:
m_2D_3+1D = 6 M_sun × 3.5e-17 = 4.2e14 kg = 2e-16 M_sun

That's NOT axion-like (10^-23 kg). It's 10^37 times too big.

So the cascade CANNOT have both:
- 30 Gyr in 2D = 33 s in 3+1D (ℓ/c mapping)
- m_2D_3+1D ~ 10^-23 kg (axion-like)

These are physically inconsistent. The 30 Gyr assumption is the problem.
"""

import numpy as np

# Physical constants
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
H_0 = 70.16e3 / Mpc_m
rho_crit = 3 * H_0**2 / (8 * np.pi * G_N)
rho_DM_obs = rho_crit * 0.27
print(f"ρ_DM (Ω_DM=0.27, H_0=70.16) = {rho_DM_obs:.3e} kg/m³")
print()

# RS-II parameters
k_GeV = 1e19
k_inv_m = GeV_inv_to_m / k_GeV
print(f"k (RS-II natural) = {k_GeV:.1e} GeV, 1/k = {k_inv_m:.2e} m")
print()

# Empirical mapping: τ_3+1D = 33 s (from ℓ/c rule)
tau_3plus1D = 33  # seconds
print(f"τ_3+1D (empirical, from ℓ/c) = {tau_3plus1D} s")
print(f"ℓ = c × τ_3+1D = {c * tau_3plus1D:.2e} m = {c * tau_3plus1D / 1.5e11:.2e} AU")
print()

# =============================================================================
# Q1: What is m_2D_3+1D given various 2D universe masses?
# =============================================================================
def q1_m2d_3plus1D():
    """For various 2D universe masses, what is m_2D_3+1D given e^{-ky}?"""
    print("=" * 80)
    print("Q1: m_2D_3+1D given m_2D_2D and the 33 s constraint")
    print("=" * 80)
    print()

    print("The 33 s constraint gives e^{-ky} if we know τ_2D (assumption).")
    print("Or vice versa: if we know e^{-ky}, we know τ_2D = 33 s × e^{-ky}.")
    print()

    m_2D_2D_list = [1.1e-23, 1e-15, 1e-8, 1.0, 1e10, 1e20, 1e30, 6 * M_sun_kg]
    e_ky_list = {
        "1 (no compression)": 1,
        "1e-17 (ℓ/c)": 1e-17,
        "1e-32 (deep)": 1e-32,
        "1e-48 (very deep)": 1e-48,
        "1e-54 (cascade default)": 1e-54,
    }

    print(f"{'m_2D_2D (kg)':>15} | ", end="")
    for label in e_ky_list:
        print(f"m_2D_3+1D for {label[:12]:<12} | ", end="")
    print()
    print("-" * 130)

    for m_2D_2D in m_2D_2D_list:
        print(f"{m_2D_2D:>15.2e} | ", end="")
        for label, e_ky in e_ky_list.items():
            m_3plus1D = m_2D_2D * e_ky
            if m_3plus1D > 1e40:
                print(f"{'too big':>30} | ", end="")
            else:
                print(f"{m_3plus1D:>30.2e} | ", end="")
        print()
    print()
    print("Honest finding: For the 33 s in 3+1D constraint to give axion-like")
    print("3+1D mass, we need m_2D_2D ~ 1.1e-23 / 1e-17 = 1.1e-6 kg (milligram)")
    print("This is NOT 6 M_sun. The 6 M_sun postulate is INCOMPATIBLE with the")
    print("33 s in 3+1D constraint AND the axion-like 3+1D mass constraint.")
    print()

# =============================================================================
# Q2: Find m_2D_2D that's CONSISTENT with all three constraints
# =============================================================================
def q2_consistent_m2D():
    """Find m_2D_2D consistent with: 33 s, axion-like 3+1D mass, and Ω_DM."""
    print("=" * 80)
    print("Q2: Find consistent m_2D_2D for 33 s and axion-like 3+1D mass")
    print("=" * 80)
    print()

    # Constraint 1: τ_3+1D = 33 s
    # This gives τ_2D = 33 s × e^{-ky} (or e^{ky}, depending on formula)
    # Let's use dτ_2D = e^{-ky} dt_4D → τ_2D = e^{-ky} × τ_3+1D
    # For deep bulk: τ_2D is short (since 2D clock runs slow)
    # Wait, that's wrong. Let me think again.
    #
    # dτ_2D = e^{-ky} dt_4D
    # If e^{-ky} is small (deep bulk), then dτ_2D << dt_4D
    # 1 second in 3+1D = e^{-ky} seconds in 2D
    # 1 second in 2D = 1/e^{-ky} = e^{ky} seconds in 3+1D
    #
    # So if 2D universe's 2D-frame lifetime is τ_2D,
    # the 3+1D-frame lifetime is τ_3+1D = τ_2D × e^{ky}
    #
    # For τ_3+1D = 33 s and various e^{-ky}:
    # τ_2D = 33 s × e^{-ky}

    print("With dτ_2D = e^{-ky} dt_4D:")
    print("  τ_3+1D = τ_2D × e^{ky}")
    print("  τ_2D = τ_3+1D × e^{-ky}")
    print()
    print("For τ_3+1D = 33 s (constraint 1):")
    print()

    e_ky_list = [1, 1e-10, 1e-17, 1e-32, 1e-48, 1e-54]
    for e_ky in e_ky_list:
        tau_2D = tau_3plus1D * e_ky
        tau_2D_Gyr = tau_2D / (365.25 * 24 * 3600 * 1e9)
        # m_2D_3+1D = m_2D_2D × e^{-ky} (this is the time compression for mass too)
        # For m_2D_3+1D = 1.1e-23 kg (constraint 2), m_2D_2D = 1.1e-23 / e^{-ky}
        m_2D_2D_needed = 1.1e-23 / e_ky
        print(f"  e^{{-ky}} = {e_ky:>10.0e}: τ_2D = {tau_2D:>10.1e} s ({tau_2D_Gyr:>8.2e} Gyr), m_2D_2D = {m_2D_2D_needed:>10.2e} kg")
    print()

    # For the cascade to have both 33 s AND axion-like 3+1D mass:
    # Need e^{-ky} = 1e-17 (from 30 Gyr in 2D)
    # m_2D_2D = 1.1e-23 / 1e-17 = 1.1e-6 kg (milligram)
    # τ_2D = 33 s × 1e-17 = 3.3e-16 s (way shorter than universe age)

    print("Consistent solution:")
    print("  e^{-ky} = 1e-17, τ_2D = 3.3e-16 s, m_2D_2D = 1.1e-6 kg")
    print("  This is the ONLY self-consistent set")
    print("  Note: 6 M_sun postulate is INCOMPATIBLE with this")
    print()

# =============================================================================
# Q3: Implied 2D universe density for various scenarios
# =============================================================================
def q3_density_scenarios():
    """For consistent (m_2D_2D, e^{-ky}) pairs, what's the 2D universe density?"""
    print("=" * 80)
    print("Q3: 2D universe density for various scenarios")
    print("=" * 80)
    print()

    print("For Ω_DM = 0.27:")
    print()

    scenarios = [
        ("6 M_sun, e^{-ky}=10^-54 (cascade default)", 6 * M_sun_kg, 1e-54),
        ("6 M_sun, e^{-ky}=10^-17 (33 s constraint)", 6 * M_sun_kg, 1e-17),
        ("1.1e-6 kg, e^{-ky}=10^-17 (consistent)", 1.1e-6, 1e-17),
        ("1.1e-23 kg, e^{-ky}=1 (no compression)", 1.1e-23, 1),
        ("M_Pl, e^{-ky}=10^-15 (Karch-Randall)", M_Pl_kg, 1e-15),
    ]

    for label, m_2D, e_ky in scenarios:
        m_3plus1D = m_2D * e_ky
        n_2D = rho_DM_obs / m_3plus1D
        sep_m = n_2D ** (-1/3)
        sep_kpc = sep_m / kpc_m
        tau_2D = tau_3plus1D * e_ky
        print(f"  {label}:")
        print(f"    m_2D_3+1D = {m_3plus1D:.2e} kg, n_2D = {n_2D:.2e} m⁻³, sep = {sep_m:.2e} m = {sep_kpc:.2e} kpc")
        print(f"    τ_2D (2D-frame lifetime) = {tau_2D:.2e} s = {tau_2D/(365.25*24*3600*1e9):.2e} Gyr")
        print()

# =============================================================================
# Q4: Cumulative 2D universe deaths over T_universe
# =============================================================================
def q4_cumulative_deaths():
    """Total 2D universe deaths in T_universe."""
    print("=" * 80)
    print("Q4: Cumulative 2D universe deaths over T_universe")
    print("=" * 80)
    print()

    sn_rate = 30
    E_crit_J = 1.6e-11
    E_sn_J = 1e53
    n_events_per_sn = E_sn_J / E_crit_J
    raw_2d_rate = sn_rate * n_events_per_sn
    T_universe = 13.8e9 * 365.25 * 24 * 3600

    print(f"Raw 2D rate: {raw_2d_rate:.2e} s⁻¹")
    print()

    scenarios = [
        ("33 s, |C|²=1 (consistent)", 33, 1),
        ("33 s, |C|²=46 (max DOZZ)", 33, 46),
        ("30 Gyr, |C|²=1 (cascade default, but inconsistent)", 30e9*365.25*24*3600, 1),
    ]

    for label, tau, c_sq in scenarios:
        # n_deaths during T_universe (in 3+1D)
        n_deaths = raw_2d_rate * c_sq * T_universe
        # total mass
        # Each 2D universe, when it dies, contributes m_2D_3+1D to DM
        m_2D_3plus1D = 1.1e-23  # axion-like
        M_total_kg = n_deaths * m_2D_3plus1D
        # Volume of observable universe
        V_obs = 4e80
        rho_DM_cumulative = M_total_kg / V_obs
        Omega_cumulative = rho_DM_cumulative / rho_crit
        print(f"  {label}:")
        print(f"    N_deaths = {n_deaths:.2e}")
        print(f"    M_total (3+1D) = {M_total_kg:.2e} kg")
        print(f"    ρ_DM (cumulative) = {rho_DM_cumulative:.2e} kg/m³")
        print(f"    Ω_DM (cumulative) = {Omega_cumulative:.2e}")
        print(f"    f_active = 1 (τ_2D >> T_universe, all 2D universes are dead)")
        print()

# =============================================================================
# Q5: How to make cascade consistent
# =============================================================================
def q5_consistency_check():
    """How to make the cascade fully consistent."""
    print("=" * 80)
    print("Q5: How to make the cascade fully consistent")
    print("=" * 80)
    print()

    # The constraints:
    # 1. τ_3+1D = 33 s (empirical ℓ/c mapping)
    # 2. m_2D_3+1D = 1.1e-23 kg (axion-like)
    # 3. Ω_DM = 0.27 (Planck 2018)
    # 4. 5D AdS_5 (RS-II framework, k ~ M_Pl)

    # From (1) and the formula τ_2D = τ_3+1D × e^{-ky}:
    # The 2D-frame lifetime depends on e^{-ky}
    # We can choose e^{-ky} freely, then τ_2D is determined

    # From (2) and the formula m_2D_3+1D = m_2D_2D × e^{-ky}:
    # m_2D_2D is determined by e^{-ky} and m_2D_3+1D

    # The free parameter is e^{-ky} (or equivalently, y in units of 1/k)

    print("Free parameter: e^{-ky} (or y/k)")
    print("Determined quantities:")
    print("  τ_2D = 33 s × e^{-ky}")
    print("  m_2D_2D = 1.1e-23 kg / e^{-ky}")
    print()

    print("For various e^{-ky} choices:")
    print()
    print(f"{'e^(-ky)':>10} | {'y/k':>6} | {'τ_2D':>15} | {'m_2D_2D':>15} | consistent?")
    print("-" * 70)

    for e_ky in [1, 1e-10, 1e-17, 1e-32, 1e-48, 1e-54]:
        y_over_inv_k = -np.log(e_ky)
        tau_2D = tau_3plus1D * e_ky
        m_2D_2D = 1.1e-23 / e_ky

        ok = ""
        if e_ky == 1:
            ok = "no compression, m_2D_2D = axion, τ_2D = 33 s"
        elif 1e-20 < e_ky < 1e-10:
            ok = "ℓ/c scale, OK"
        elif e_ky < 1e-30:
            ok = "deep bulk, but m_2D_2D too big (stellar+)"
        print(f"{e_ky:>10.0e} | {y_over_inv_k:>6.1f} | {tau_2D:>15.2e} | {m_2D_2D:>15.2e} | {ok}")
    print()
    print("Honest finding: The cascade is consistent for ANY e^{-ky}, as long as")
    print("we don't fix m_2D_2D = 6 M_sun. The 6 M_sun is a SEPARATE postulate.")
    print()

# =============================================================================
# Q6: The 30 Gyr vs 33 s contradiction
# =============================================================================
def q6_30gyr_33s_contradiction():
    """The 30 Gyr vs 33 s contradiction."""
    print("=" * 80)
    print("Q6: 30 Gyr (2D) vs 33 s (3+1D) contradiction")
    print("=" * 80)
    print()

    # 30 Gyr = 9.46e17 s
    # 33 s
    # Ratio: 9.46e17 / 33 = 2.87e16

    # The contradiction:
    # - The cascade says τ_2D = 30 Gyr (in 2D frame)
    # - The cascade says τ_3+1D = 33 s (in 3+1D frame, from ℓ/c)
    # - These give e^{-ky} = 9.46e17/33 = 2.87e16 (impossible, > 1)
    # OR if formula is reversed: e^{-ky} = 33/9.46e17 = 3.5e-17

    # Let me check both interpretations
    print("Interpretation 1: dτ_2D = e^{-ky} dt_4D (slow 2D clock)")
    print("  τ_2D = e^{-ky} × τ_3+1D")
    print("  30 Gyr = e^{-ky} × 33 s")
    print("  e^{-ky} = 30 Gyr / 33 s = 2.87e16  (impossible, > 1)")
    print()

    print("Interpretation 2: dt_4D = e^{-ky} dτ_2D (slow 3+1D clock from 2D view)")
    print("  τ_3+1D = e^{-ky} × τ_2D")
    print("  33 s = e^{-ky} × 30 Gyr")
    print("  e^{-ky} = 33 / 9.46e17 = 3.5e-17  (this is what cascade probably intends)")
    print()

    print("With e^{-ky} = 3.5e-17:")
    print("  m_2D_3+1D = m_2D_2D × 3.5e-17")
    print("  For m_2D_2D = 6 M_sun: m_2D_3+1D = 4.2e14 kg = 2e-16 M_sun")
    print("  This is NOT axion-like (10^-23 kg)")
    print()

    print("Honest finding: The 30 Gyr in 2D and 33 s in 3+1D give e^{-ky} = 3.5e-17")
    print("This is INCOMPATIBLE with the cascade's axion-like 3+1D mass postulate.")
    print()

    print("To make the cascade consistent, choose ONE:")
    print()
    print("Option A: Keep 30 Gyr = 33 s mapping (ℓ/c empirical)")
    print("  → e^{-ky} = 3.5e-17")
    print("  → m_2D_2D = 1.1e-23 / 3.5e-17 = 3.1e-7 kg (milligram)")
    print("  → 2D universe is MILLIGRAM-SCALE, not stellar")
    print()
    print("Option B: Keep 6 M_sun 2D universe mass")
    print("  → m_2D_2D = 6 M_sun")
    print("  → For axion-like 3+1D: e^{-ky} = 9.2e-55")
    print("  → τ_3+1D = 30 Gyr × 9.2e-55 = 2.8e-45 s (way shorter than 33 s!)")
    print("  → 2D universe lives 10^-45 s in 3+1D, not 33 s")
    print()
    print("Option C: Drop the 30 Gyr assumption (it's a free parameter)")
    print("  → Use 33 s as the empirical lifetime (ℓ/c mapping)")
    print("  → e^{-ky} is determined by m_2D_2D (which is also free)")
    print("  → Many (m_2D_2D, e^{-ky}) pairs are consistent")
    print()

# =============================================================================
# Run all
# =============================================================================
if __name__ == "__main__":
    q1_m2d_3plus1D()
    q2_consistent_m2D()
    q3_density_scenarios()
    q4_cumulative_deaths()
    q5_consistency_check()
    q6_30gyr_33s_contradiction()
    print("=" * 80)
    print("Summary: 2D universe mass and lifetime (v2)")
    print("=" * 80)
    print()
    print("KEY INSIGHT: 30 Gyr was an assumption, 33 s is empirical.")
    print("Using 33 s as primary constraint:")
    print("  - 30 Gyr in 2D + 33 s in 3+1D → e^{-ky} = 3.5e-17")
    print("  - This is INCOMPATIBLE with axion-like 3+1D mass (needs e^{-ky} = 9.2e-55)")
    print("  - 38 orders of magnitude discrepancy")
    print()
    print("Resolution options:")
    print("  A) Keep 33 s, give up 6 M_sun postulate → m_2D_2D ~ milligram")
    print("  B) Keep 6 M_sun, give up 33 s → τ_3+1D = 10^-45 s (not 33 s)")
    print("  C) Drop 30 Gyr assumption → many (m_2D, e^{-ky}) pairs work")
    print()
    print("The cascade CANNOT have all three:")
    print("  1) 30 Gyr 2D lifetime")
    print("  2) 33 s 3+1D lifetime")
    print("  3) 6 M_sun 2D mass with axion-like 3+1D mass")
    print()
    print("The 30 Gyr was the weakest link — it's a postulate, not derived.")
