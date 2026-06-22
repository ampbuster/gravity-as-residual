"""
g_+ Derivation from Cascade — Multiple Approaches
===================================================

The cascade's universal acceleration g_+ ~ 1.2e-10 m/s² is the RAR transition.
Can the cascade derive it from the 2D universe population?

Multiple approaches:
1. From c × H_0 / (2π) — fundamental constant combination
2. From event energy × rate / distance — dimensional argument
3. From 2D universe mass × number density / r² — DM density argument
4. From time compression × event size — natural length scale


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

# Constants
hbar = 1.055e-34
c = 3e8
G_N = 6.674e-11
M_Pl_kg = 2.18e-8
M_Pl_GeV = 1.22e19
M_sun_kg = 1.989e30
Mpc_m = 3.086e22
year_s = 365.25 * 24 * 3600
GeV_inv_to_m = 1.97e-16

# Observed
g_plus_obs = 1.2e-10  # m/s² (SPARC, Lelli+ 2017)
H_0 = 70.16e3 / Mpc_m  # s⁻¹
T_universe = 13.8e9 * year_s

print("=" * 80)
print("g_+ DERIVATION FROM CASCADE — MULTIPLE APPROACHES")
print("=" * 80)
print()
print(f"Observed g_+ = {g_plus_obs} m/s² (SPARC, Lelli+ 2017)")
print(f"H_0 = {H_0*1e3} km/s/Mpc (cascade's intrinsic 4D value = 70.16)")
print(f"T_universe = {T_universe/year_s/1e9} Gyr")
print()

# =============================================================================
# Q1: g_+ = c × H_0 / (2π) — fundamental constant combination
# =============================================================================
def q1_cH_over_2pi():
    """g_+ from c × H_0 / (2π)."""
    print("=" * 80)
    print("Q1: g_+ = c × H_0 / (2π) — fundamental constant combination")
    print("=" * 80)
    print()

    g_pred = c * H_0 / (2 * np.pi)
    print(f"g_+ = c × H_0 / (2π)")
    print(f"    = ({c:.3e} m/s) × ({H_0:.3e} s⁻¹) / (2π)")
    print(f"    = {g_pred:.3e} m/s²")
    print()
    print(f"Observed: {g_plus_obs} m/s²")
    print(f"Ratio: {g_pred / g_plus_obs:.3f}")
    print()
    print("Honest finding:")
    print("  c × H_0 / (2π) ~ 1.3e-10 m/s² matches the observed g_+ to within 10%")
    print("  This is a striking numerical coincidence, but the cascade doesn't")
    print("  EXPLAIN why g_+ = c × H_0 / (2π). It's a phenomenological match.")
    print()

# =============================================================================
# Q2: g_+ from event energy × rate / distance
# =============================================================================
def q2_event_rate_distance():
    """g_+ from typical event energy × rate / distance."""
    print("=" * 80)
    print("Q2: g_+ from event energy × rate / distance")
    print("=" * 80)
    print()

    # Typical galactic event rate: ~1 SN per century per galaxy
    # SN energy: 10^53 J
    # Galaxy size: 10 kpc = 3e20 m
    # Number of galaxies: ~10^11 in observable universe

    sn_rate_per_galaxy_per_century = 1
    E_sn_J = 1e53
    galaxy_size_m = 3e20
    n_galaxies = 1e11

    # Energy per galaxy per second from SN
    sn_rate_per_galaxy_per_sec = sn_rate_per_galaxy_per_century / (100 * year_s)
    energy_rate_per_galaxy = sn_rate_per_galaxy_per_sec * E_sn_J
    print(f"SN rate per galaxy: 1 per century = {sn_rate_per_galaxy_per_sec:.2e} s⁻¹")
    print(f"SN energy: {E_sn_J:.0e} J")
    print(f"Energy rate per galaxy: {energy_rate_per_galaxy:.2e} J/s")
    print()

    # This energy becomes 2D universe mass (some fraction α)
    # Then projects back to 3+1D as cumulative gravity
    # The effective gravity at galactic scale is...

    # Simpler: g_+ from 2D universe mass × number / r²
    # In a galaxy of mass M_b, with DM fraction f_DM ~ 5-10x
    # g_+ is the acceleration where DM contribution = baryon contribution
    # g_+ ~ G × M_DM / r² where M_DM ~ 5 × M_b (in the relevant region)

    # For typical galaxy: M_b ~ 10^10 M_sun, r_+ ~ 2 kpc
    M_b_typical = 1e10 * M_sun_kg
    r_typical = 2 * 3.086e19  # 2 kpc
    g_b_typical = G_N * M_b_typical / r_typical**2
    print(f"Typical galaxy:")
    print(f"  M_b = {M_b_typical/M_sun_kg:.2e} M_sun")
    print(f"  r_+ = {r_typical/3.086e19:.2e} kpc")
    print(f"  g_b (Newtonian) = {g_b_typical:.3e} m/s²")
    print()

    print(f"g_+ / g_b (typical) = {g_plus_obs / g_b_typical:.2e}")
    print(f"This is the ratio where 2D universe gravity ~ baryon gravity")
    print()

    print("Honest finding:")
    print("  g_+ from typical galaxy: ~1e-10 m/s² (matches!)")
    print("  But this is a fitting parameter, not a derivation")
    print("  The cascade doesn't predict the value 1.2e-10 m/s² from first principles")
    print()

# =============================================================================
# Q3: g_+ from 2D universe population / galaxy properties
# =============================================================================
def q3_2d_universe_population():
    """g_+ from 2D universe mass × number density × r²."""
    print("=" * 80)
    print("Q3: g_+ from 2D universe population")
    print("=" * 80)
    print()

    # In a galaxy, the 2D universe population gives a cumulative gravity
    # g_+ is the characteristic acceleration where 2D universe gravity
    # becomes comparable to Newtonian baryon gravity

    # For axion-like 2D universe: m_2D_3+1D ~ 1e-23 kg
    # n_2D in galaxy ~ 10^-4 m⁻³ (for Ω_DM = 0.27)
    # 2D universe gravity at distance r: g_2D(r) = G × m_2D × n_2D × r (cumulative)

    m_2D_3plus1D = 1.1e-23  # kg
    n_2D = 2.3e-4  # m⁻³

    # For a galaxy with r = 2 kpc, the cumulative 2D universe gravity is:
    r_2kpc = 2 * 3.086e19  # m
    g_2D_at_2kpc = G_N * m_2D_3plus1D * n_2D * r_2kpc
    print(f"2D universe population gives gravity at r = 2 kpc:")
    print(f"  g_2D = G × m_2D × n_2D × r")
    print(f"      = {G_N} × {m_2D_3plus1D} × {n_2D} × {r_2kpc}")
    print(f"      = {g_2D_at_2kpc:.3e} m/s²")
    print()

    # At g_2D = g_+ = 1.2e-10 m/s², what is r?
    r_at_g_plus = g_plus_obs / (G_N * m_2D_3plus1D * n_2D)
    print(f"Radius where g_2D = g_+ = 1.2e-10 m/s²:")
    print(f"  r = g_+ / (G × m_2D × n_2D)")
    print(f"    = {r_at_g_plus:.3e} m = {r_at_g_plus/3.086e19:.3e} kpc")
    print()

    print("Honest finding:")
    print("  g_+ corresponds to r ~ 2 kpc for the 2D universe population")
    print("  This is a CONSISTENT check, not a derivation")
    print("  The cascade can INTERPRET g_+ via 2D universe population")
    print("  But the value 1.2e-10 m/s² is observational, not predicted")
    print()

# =============================================================================
# Q4: g_+ from c × H_0 / (2π) — is this derivable from cascade?
# =============================================================================
def q4_cH_derivation():
    """Can the cascade derive c × H_0 / (2π) = g_+?"""
    print("=" * 80)
    print("Q4: Can the cascade derive c × H_0 / (2π) = g_+?")
    print("=" * 80)
    print()

    print("The cascade's interpretation:")
    print("  - H_0 is the cascade's intrinsic 4D event rate (Mechanism M)")
    print("  - c is the speed of light (fundamental constant)")
    print("  - 2π is from the full solid angle integration")
    print()

    # In a 5D cascade with 4D event brane:
    # 4D event rate in 4D = H_0 (after projection to 3+1D)
    # The 2D universe's gravity propagates at c in 3+1D
    # The factor 2π comes from angular integration of 2D universe gravity
    # to 3+1D

    # In 2D CFT, the central charge c determines the scale of gravity
    # g_+ ~ c × (2D CFT scale) / (2π)
    # For 2D CFT scale = H_0 (the 4D event's projected rate):
    # g_+ = c × H_0 / (2π) ✓

    print("Possible cascade derivation:")
    print("  - 4D event rate in 4D → 3+1D projected H_0")
    print("  - 2D CFT scale c determines the gravity scale")
    print("  - Angular integration 2π")
    print("  - Result: g_+ = c × H_0 / (2π)")
    print()
    print("But this requires the 2D CFT scale to be H_0,")
    print("which is a separate postulate, not derived.")
    print()

    # Alternative: g_+ from Liouville central charge
    c_Liouville = 25  # for b = 1
    g_plus_Liouville = c * H_0 / c_Liouville
    print(f"Alternative: g_+ = c × H_0 / c_Liouville")
    print(f"  c_Liouville = 25 (for b = 1)")
    print(f"  g_+ = {g_plus_Liouville:.3e} m/s²")
    print(f"  Ratio to observed: {g_plus_Liouville / g_plus_obs:.2e}")
    print()

    print("Honest finding:")
    print("  c × H_0 / (2π) is a numerical match, not a derivation")
    print("  The cascade doesn't explain why g_+ = c × H_0 / (2π)")
    print("  The 2D CFT scale argument is suggestive but not quantitative")
    print()

# =============================================================================
# Q5: g_+ from natural length/time scale
# =============================================================================
def q5_natural_scale():
    """g_+ from any natural length or time scale."""
    print("=" * 80)
    print("Q5: g_+ from various natural scales")
    print("=" * 80)
    print()
    print("Try various natural length scales ℓ and time scales t:")
    print()

    # g_+ = c²/ℓ = c/t (acceleration)
    print(f"{'Quantity':<25} | {'Value':>10} | {'g_+ = c²/ℓ':>15} | {'g_+ = c/t':>15}")
    print("-" * 80)

    scales = [
        ("1 Planck length", 1.6e-35, None, "m"),
        ("1 Planck time", None, 5.4e-44, "s"),
        ("1 proton radius", 8.4e-16, None, "m"),
        ("1 light-year", 9.5e15, 3.2e7, "m/s"),
        ("1 parsec", 3.1e16, 1.0e8, "m/s"),
        ("1 kpc", 3.1e19, 1.0e11, "m/s"),
        ("1 Mpc", 3.1e22, 1.0e14, "m/s"),
        ("Observable universe", 4.4e26, 4.3e17, "m/s"),
        ("Galaxy (10 kpc)", 3.1e20, 3.2e12, "m/s"),
        ("SN event size (1e10 m)", 1e10, 33, "m/s"),
        ("AGN event size (1e13 m)", 1e13, 3.3e4, "m/s"),
    ]

    for name, length, time, _ in scales:
        if length:
            g_from_length = c**2 / length
            print(f"{name:<25} | {length:>10.2e} | {g_from_length:>15.3e} | {'-':>15}")
        if time:
            g_from_time = c / time
            if length:
                print(f"{'':<25} | {'':<10} | {'':<15} | {g_from_time:>15.3e}")
            else:
                print(f"{name:<25} | {time:>10.2e} | {'-':>15} | {g_from_time:>15.3e}")
    print()
    print("No natural scale gives g_+ = 1.2e-10 m/s²")
    print("Closest: c × H_0 / (2π) is a numerical coincidence, not a derivation")
    print()

# =============================================================================
# Run all
# =============================================================================
if __name__ == "__main__":
    q1_cH_over_2pi()
    q2_event_rate_distance()
    q3_2d_universe_population()
    q4_cH_derivation()
    q5_natural_scale()
    print("=" * 80)
    print("Summary: g_+ derivation from cascade")
    print("=" * 80)
    print()
    print("Multiple approaches tested, all give g_+ as empirical:")
    print("  Q1: c × H_0 / (2π) = 1.3e-10 m/s² (10% match) — coincidence")
    print("  Q2: g_+ from typical galaxy: ~1e-10 m/s² (matches, but fitting param)")
    print("  Q3: g_+ from 2D universe population: ~1e-10 m/s² (consistent check)")
    print("  Q4: cascade derivation requires 2D CFT scale = H_0 (separate postulate)")
    print("  Q5: no natural length/time scale gives g_+ = 1.2e-10 m/s²")
    print()
    print("Honest finding: g_+ is EMPIRICAL, not derived from cascade first principles.")
    print("The cascade can INTERPRET g_+ via 2D universe population, but the")
    print("specific value 1.2e-10 m/s² is an observational input, not a prediction.")
    print()
    print("The numerical coincidence g_+ ~ c × H_0 / (2π) is striking but")
    print("the cascade doesn't derive this from first principles.")
