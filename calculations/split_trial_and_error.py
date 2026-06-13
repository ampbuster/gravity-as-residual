#!/usr/bin/env python3
"""
Trial-and-error derivation of the 5/27/68 mass-energy split.

Observed (Planck 2018):
  Omega_ordinary ~ 0.05
  Omega_DM       ~ 0.27
  Omega_DE       ~ 0.68

Try various dimensional/geometric formulas and see which matches.
"""

import math

# Observed
TARGET_ORDINARY = 0.05
TARGET_DM = 0.27
TARGET_DE = 0.68

# Other key numbers from the cascade
EPSILON = 5.9e-39  # bulk-brane coupling
F_BACK = 2.27e-85  # staying fraction
G = 1e8  # growth factor (from 2D FRW dynamics)
N_LEVELS = 4  # 4D, 3+1D, 2D, 1D (cascade has 4 levels in our universe)
N_SPATIAL_4D = 3  # 4D has 3 spatial dimensions
N_SPATIAL_3P1D = 2  # 3+1D has 2 spatial "in-halo" dimensions relevant for back-projection
N_SPATIAL_2D = 1  # 2D has 1 spatial dimension
PI = math.pi

def try_formula(name, formula_ord, formula_dm, formula_de, normalize=True):
    """Try a formula and report the match."""
    o = formula_ord
    d = formula_dm
    e = formula_de
    if normalize:
        total = o + d + e
        o, d, e = o/total, d/total, e/total
    err_ord = abs(o - TARGET_ORDINARY) / TARGET_ORDINARY
    err_dm = abs(d - TARGET_DM) / TARGET_DM
    err_de = abs(e - TARGET_DE) / TARGET_DE
    avg_err = (err_ord + err_dm + err_de) / 3
    print(f"  {name:<50}: o={o:.4f} d={d:.4f} e={e:.4f} | err: o={err_ord:.2e} d={err_dm:.2e} e={err_de:.2e} | avg={avg_err:.2e}")
    return avg_err

def header(s):
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


def main():
    header("TRIAL-AND-ERROR: 5/27/68 MASS-ENERGY SPLIT")

    print(f"\n  Target: ordinary=0.05, DM=0.27, DE=0.68 (Planck 2018)")

    # Try various formulas
    print(f"\n\n  --- Category 1: Simple ratios ---")
    try_formula("o=1/20, d=27/100, e=68/100",
                1/20, 27/100, 68/100)
    try_formula("o=1/20, d=0.27, e=0.68",
                1/20, 0.27, 0.68)
    try_formula("o=5/100, d=27/100, e=68/100",
                5/100, 27/100, 68/100)
    try_formula("o=5/100, d=27/100, e=4*(17/100)",
                5/100, 27/100, 4*17/100)

    print(f"\n\n  --- Category 2: Powers of small numbers ---")
    for k in range(1, 5):
        try_formula(f"o=1/{k**4}, d=1/{k**2}, e=1-1/{k**2}-1/{k**4}",
                    1/k**4, 1/k**2, 1-1/k**2-1/k**4)
    for k in range(1, 5):
        try_formula(f"o=(1/{k})**4, d=(1/{k})**2, e=1-...",
                    (1/k)**4, (1/k)**2, 1-(1/k)**4-(1/k)**2)

    print(f"\n\n  --- Category 3: 4D->3+1D projection fractions ---")
    # 4D has 4 modes. 3+1D picks 3 spatial.
    # Maybe: ordinary = (1/4)^2 = 1/16, DM = something
    try_formula("o=(1/4)^2=1/16, d=?, e=?",
                1/16, 0.27, 0.68, normalize=False)
    # Maybe: o = 1/N^2, d = 1/N, e = 1 - 1/N - 1/N^2
    for N in [3, 4, 5, 6, 8, 10, 16, 20]:
        try_formula(f"N={N}: o=1/N^2, d=1/N, e=1-1/N-1/N^2",
                    1/N**2, 1/N, 1-1/N-1/N**2)

    print(f"\n\n  --- Category 4: 5/27/68 from powers ---")
    # 5 = 5
    # 27 = 3^3
    # 68 = 4^3 + 4 = 64 + 4? Or 68 = ?
    # 5 + 27 + 68 = 100
    # Or 5 = 5, 27 = 3^3, 68 = ?
    # Maybe 68 = 4*17, but 17 has no obvious meaning
    # Maybe 68 = 2^6 + 4 = 64 + 4
    # Maybe 68 = 2 * 34, 34 = 2 * 17
    # Or 68 = 2 * 4^2 + 4 = 32 + 4? No
    # Or 68 = (4+1)^2 + 7 = 32? No
    # Or 68 = 4^3 + 4 = 64 + 4? 4 = number of cascade levels
    try_formula("o=5, d=3^3=27, e=4^3+4=68",
                5, 27, 68)
    try_formula("o=5, d=3^3, e=4*(17)",
                5, 27, 4*17)
    try_formula("o=5, d=27, e=64+4",
                5, 27, 68)
    # 5, 27, 68 as a sequence: 5 = 2^2+1, 27 = 3^3, 68 = 2^6+4
    # 27/5 = 5.4, 68/27 = 2.52
    # 68/5 = 13.6
    # 5 * 13.6 = 68
    # 5 + 27 = 32, 32 + 36 = 68. 36 = 6^2

    print(f"\n\n  --- Category 5: 1/20 cascade ---")
    # The cascade has 4 levels. 4 * 5 = 20. So 1/20 = 5%.
    # The DM fraction might be: (3/4)^3 * 1 = 27/64 ~ 0.42 (matter in 2D projected to 3+1D)
    # The DE fraction might be: 1 - 1/20 - (3/4)^3 = 1 - 0.05 - 0.42 = 0.53 (no)
    # Or: DM = 27/100 from 3D projection of 2D (3^3=27, normalized to 100)
    # Or: DE = 1 - o - d = 0.68 from 100 - 5 - 27
    try_formula("o=1/20, d=(3/4)^3 * (1-1/20), e=1-...",
                1/20, (3/4)**3 * (1 - 1/20), 1 - 1/20 - (3/4)**3 * (1 - 1/20))

    print(f"\n\n  --- Category 6: 2D universe as source ---")
    # 2D universe has 2 spatial dimensions. Of these, 1 is the 'time' (per cascade)
    # 1 of 2 spatial dims survives projection
    # Or 1 of 3 (counting time)
    # 1/3 = 0.333 (no)
    # (1/3)^2 = 0.111 (no)
    # 1/(3*4) = 0.083 (close to 5%)
    try_formula("o=1/12, d=?, e=?",
                1/12, 0.27, 0.68, normalize=False)
    # 1/12 = 0.083 (close but not 0.05)
    # 1/20 = 0.05 (exact)
    # Why 20? 20 = 4*5 (4 levels, 5 ordinary particles?), or 20 = 4+16

    print(f"\n\n  --- Category 7: Hierarchy / DE coupling ---")
    # rho_DE = epsilon * f_back * rho_Pl
    # rho_Pl_3+1D = 4.6e113 J/m^3
    # rho_crit = 3 H^2 / (8 pi G) ~ 8.5e-10 J/m^3
    # rho_DE / rho_crit = 0.68
    # So: epsilon * f_back * rho_Pl / rho_crit = 0.68
    # (5.9e-39) * (2.27e-85) * (4.6e113) / 8.5e-10 = 0.68 ✓
    # This is what gives DE = 0.68
    # Ordinary: 1 - DE - DM = 0.05
    # DM: derived from G

    print(f"\n\n  --- Category 8: From cascade's growth factor G ---")
    # G = 1e8, derived from 2D FRW
    # Total DM per galaxy = 6.4 * G * M_event * N = 1.0e58 J
    # Critical density of universe in our galaxy: rho_crit * V_galaxy
    # V_galaxy ~ (10 kpc)^3 = 1.2e60 m^3
    # rho_crit = 8.5e-10 J/m^3
    # Mass_crit in galaxy = 8.5e-10 * 1.2e60 * c^2 = ?
    # Actually: Omega_DM = rho_DM / rho_crit = 0.27
    # rho_DM = 0.27 * rho_crit = 0.27 * 8.5e-10 = 2.3e-10 J/m^3
    # In galaxy volume 1.2e60 m^3: 2.3e-10 * 1.2e60 = 2.8e50 J
    # Per galaxy? That's WAY less than 1e58. Hmm.
    # Actually 1e58 J / c^2 = 1e58 / 9e16 = 1e41 kg = 5e10 M_sun. Yes!
    # So the per-galaxy DM energy matches. But what's Omega?
    # If 5e10 M_sun per galaxy, 1e10 galaxies in 30 Mpc volume = 5e20 M_sun total
    # In 30 Mpc^3 = (30 * 3e22 m)^3 = 8.1e67 m^3
    # rho_DM = 5e20 * 2e30 * 9e16 / 8.1e67 = 1.1e-9 J/m^3
    # rho_crit = 8.5e-10 J/m^3
    # Omega_DM = 1.3 (close to 0.27? Hmm, depends on galaxy density)
    # OK, the math is sensitive to galaxy density. But the rough picture is:
    # 27% DM = 6.4 * G * M_SN * N_SN / rho_crit
    # With G=1e8, M_SN ~ 1e44 J, N_SN ~ 1e8, this gives 0.27 if galaxies are dense enough

    # Try:
    for n_galaxies_per_Mpc3 in [1e-2, 1e-1, 1]:
        for galaxy_mass_factor in [3e10, 5e10, 1e11]:
            # Total DM mass in 30 Mpc volume
            n_gal = n_galaxies_per_Mpc3 * 30**3  # galaxies in 30 Mpc
            M_dm_per_gal = galaxy_mass_factor * 2e30  # kg
            V = (30 * 3.086e22) ** 3  # m^3
            rho_dm = n_gal * M_dm_per_gal * 9e16 / V
            rho_crit = 8.5e-10
            Omega = rho_dm / rho_crit
            if 0.2 < Omega < 0.35:
                print(f"  n_gal/Mpc^3={n_galaxies_per_Mpc3:.0e}, M_DM/gal={galaxy_mass_factor:.1e}: Omega_DM = {Omega:.3f}  *** CLOSE TO 0.27 ***")

    print(f"\n\n  --- Category 9: Specific cascade-level formulas ---")
    # Try: o = 1/(2N_cascade * 2) where N_cascade = 4
    for N in range(2, 10):
        try_formula(f"N_cascade={N}: o=1/(2N), d=N^2/100, e=1-...",
                    1/(2*N), N**2/100, 1 - 1/(2*N) - N**2/100)
    # 5/27/68 might be: 5 = 2.5^2/1.25, 27 = 3^3, 68 = 4*17
    # Or: from the hierarchy 10^-38
    # o = 10^-1.3 = 0.05
    # d = 10^-0.57 = 0.27
    # e = 10^-0.17 = 0.68
    # 1.3, 0.57, 0.17 have no obvious geometric meaning

    print(f"\n\n  --- Category 10: e_N inflation factor ---")
    # Inflation factor e^60 ~ 10^26
    # 1/e^60 ~ 10^-26 (too small)
    # (1/e^60)^(1/3) ~ 10^-9 (too small)
    # 60 e-folds of inflation
    # 1/60 ~ 0.017 (close to 1.7%, not 5%)
    # 1/20 ~ 5% (matches!)

    print(f"\n\n  --- Category 11: N_cascade * 2D universe lifetime ---")
    # 2D universe's age in 2D's frame ~ 30 Gyr
    # Our universe's age ~ 13.8 Gyr
    # Ratio = 30/13.8 = 2.17 (not obvious)
    # 1/2.17 = 0.46 (no)
    # log_10(30/13.8) = 0.34 (no)

    print(f"\n\n  --- Category 12: Hierarchy-inverse relationships ---")
    # Hierarchy = 10^38
    # 1/10^38 = 10^-38 (epsilon)
    # Maybe: o ~ epsilon^(1/77) = 10^-38/77 = 10^-0.49 = 0.32 (no)
    # o ~ epsilon^(1/76) = 10^-0.5 = 0.32 (no)
    # o ~ 10^-1.3 = 0.05. 1.3 ~ 38/30 ~ 1.27. Hmm, close to 1.3!
    # 38/29.2 = 1.30. What is 29.2?
    # 29.2 = 13.8 * 2.12? No.
    # 29.2 = (G-1)/log(G) = (1e8-1)/log(1e8) = 1.25e6. No.
    # 29.2 = 4 * 7.3? 7.3 = ?
    # 29.2 = 30 - 0.8? No obvious meaning
    # Maybe 1.3 is not from hierarchy directly

    print(f"\n\n  --- Category 13: From cascade's growth factor G = 1e8 ---")
    # G = 1e8 = 10^8
    # log10(G) = 8
    # 1/G = 1e-8 (no)
    # 8/100 = 0.08 (close to 5%)
    # 8/160 = 0.05 (matches! Why 160?)
    # 160 = 16*10 = (2*spatial_dims_in_4D=3+1)^2 * 10? No, 4^2 = 16, 16*10=160
    # Or 160 = 8 * 20 (cascade_levels * 5)
    # 8/200 = 0.04 (close to 5%)
    # 8/160 = 0.05 (exact match)

    # 5% = 8/160 = 8/(8*20) = 1/20
    # DM = 27%: log10(G) / (something) = 27
    # 8 * (27/8) = 27, trivial
    # Maybe: 27 = log10(G) + 19? 19 has no meaning
    # 27 = 3^3 = number of independent spatial directions cubed
    # 27/100 = (3/4)^3 * (4/3) = 0.42 * 1.33 = 0.56? No

    # Try: 5% = 1/20, 27% = 27/100, 68% = 1 - 0.05 - 0.27
    try_formula("o=1/20, d=27/100, e=1-0.05-0.27",
                1/20, 27/100, 1-0.05-0.27)

    # Maybe: 5/27/68 from the cascade's 4 levels
    # 4 levels: 4D, 3+1D, 2D, 1D
    # Level 0 (4D): 4 spatial dims
    # Level 1 (3+1D): 3 spatial dims
    # Level 2 (2D): 2 spatial dims
    # Level 3 (1D): 1 spatial dim
    # Total dims = 4+3+2+1 = 10
    # Per level: 4/10=0.4, 3/10=0.3, 2/10=0.2, 1/10=0.1
    # Doesn't give 5/27/68
    try_formula("o=1/20, d=3/11=0.273, e=8/11.76=0.68",
                1/20, 3/11, 1-1/20-3/11)
    # 3/11 = 0.2727, very close to 0.27!
    # 1 - 1/20 - 3/11 = 0.677, very close to 0.68!
    print("  !!! 3/11 = 0.2727, very close to 0.27 !!!")
    print("  !!! 1 - 1/20 - 3/11 = 0.677, very close to 0.68 !!!")

    print(f"\n\n  --- Category 14: 1/20 from cascade structure ---")
    # 20 = 4! / 1.2? No, 4! = 24
    # 20 = 4 + 4*4 = 4 + 16
    # 20 = 4 * 5 (4 cascade levels, 5 ordinary particles in SM?)
    # 20 = 4 * 5: 4 cascade levels + 5 (?)
    # 20 = 5! / 6 = 120/6
    # 20 = 16 + 4 = 4^2 + 4
    # 20 = (4+1) * 4 = 5*4
    # Why 20? Post hoc: matches 5% exactly.
    # But where does 20 come from physically?

    print(f"\n  1/20 = 0.05 exactly. 20 = ?")
    print(f"  20 = 4 * 5: 4 cascade levels, 5 (?)")
    print(f"  20 = 4 + 16 = 4 + 4^2")
    print(f"  20 = 5 * 4: 5 ordinary, 4 levels")
    print(f"  20 = 16 + 4: 4^2 + 4")
    print(f"  20 = 4! - 4 = 24 - 4")
    print(f"  All numerology. None physically motivated.")

    print(f"\n\n  --- Category 15: 3/11 = 0.2727 (very close to 0.27) ---")
    print(f"  11 = 4 + 4 + 3 (cascade levels + spatial dims?)")
    print(f"  11 = N_cascade * 2 + N_spatial_3plus1D = 4*2 + 3 = 11")
    print(f"  11 = 2 + 3 + 4 + 2 (1D, 2D, 3+1D, 4D cascade dims summed)")
    print(f"  11 = 4 + 7: 4 cascade levels, 7 (??)")
    print(f"  Again, all numerology.")

    print(f"\n\n  --- Category 16: Best matches found ---")
    print(f"  ----------------------------------------------------------------")
    print(f"  {'Formula':<50} {'err_avg':>10}")
    print(f"  ----------------------------------------------------------------")
    matches = []
    matches.append(("o=1/20, d=27/100, e=68/100", try_formula("o=1/20, d=27/100, e=68/100", 1/20, 27/100, 68/100)))
    matches.append(("o=1/20, d=3/11, e=1-1/20-3/11", try_formula("o=1/20, d=3/11, e=1-1/20-3/11", 1/20, 3/11, 1-1/20-3/11)))
    matches.append(("o=1/20, d=(3/4)^3*(1-1/20), e=1-...", try_formula("o=1/20, d=(3/4)^3*(1-1/20), e=1-...",
                    1/20, (3/4)**3 * (1-1/20), 1-1/20-(3/4)**3*(1-1/20))))
    matches.sort(key=lambda x: x[1])
    for name, err in matches:
        print(f"  {name:<50} {err:>10.2e}")

    print()
    print(f"  Best match: o=1/20, d=27/100, e=68/100 (the postulate itself)")
    print(f"  But this is a POSTULATE, not a derivation.")
    print(f"  No first-principles formula tried produces 5/27/68 exactly.")


if __name__ == "__main__":
    main()
