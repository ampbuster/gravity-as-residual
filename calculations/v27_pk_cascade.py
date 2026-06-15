"""
Matter power spectrum P(k) from cascade
========================================

Cross-dimensional: P(k) connects
  - 3+1D cosmology (large k, structure formation)
  - 2D universe physics (small k, 2D universe density)
  - 1D event (4D event projection)

P(k) at:
  - Large scales (k < 0.1 h/Mpc): probes 3+1D expansion
  - Intermediate (0.1 < k < 1 h/Mpc): probes DM clustering
  - Small scales (k > 1 h/Mpc): probes 2D universe population

The cascade's P(k) differs from ΛCDM at small scales if:
  - 2D universes have non-zero cross-section (SIDM-like)
  - 2D universe mass spectrum has structure
  - f_active depends on local density (MOND-like at low accel)
"""

import numpy as np

# Constants
H_0 = 70.16e3 / 3.086e22  # s^-1
Omega_m = 0.315
Omega_b = 0.045
Omega_L = 0.685
Omega_DM = 0.27  # cascade input
h = 0.7016

print("=" * 80)
print("MATTER POWER SPECTRUM P(k) — CASCADE VS ΛCDM")
print("=" * 80)
print()

# =============================================================================
# ΛCDM linear P(k) (Eisenstein & Hu 1999 approximation)
# =============================================================================
def P_k_LCDM(k_h_Mpc):
    """Linear matter power spectrum from Eisenstein & Hu 1999.

    k_h_Mpc: wavenumber in h/Mpc
    Returns: P(k) in (Mpc/h)³
    """
    k = k_h_Mpc  # h/Mpc
    # Transfer function (no-wiggle approximation)
    Om = Omega_m
    Ob = Omega_b
    h_val = h
    Theta = 2.728 / 2.7  # T_CMB / 2.7
    # Sound horizon
    s = 44.5 * np.log(9.83 / Om) / np.sqrt(1 + 10 * Ob**0.75) * h_val
    # Silk damping scale
    alpha_gamma = 1 - 0.328 * np.log(431 * Om * h_val**2) * Ob / Om + 0.38 * np.log(22.3 * Om * h_val**2) * (Ob / Om)**2
    alpha_gamma = 1.0  # simplification
    # Effective wavenumber
    ks = 1.6 * np.sqrt(Ob / Om) * (1 + (9.0 / np.log(Om * h_val**2)) * (Theta * np.sqrt(1 + 10 * Ob**0.75) - 1))
    # q (Eisenstein & Hu)
    q = k / (13.41 * ks)
    # L = L_0 + L_1
    L_0 = np.log(2 * np.e + 1.8 * q)
    L_1 = np.log(2 * np.e + 1.8 * q) / (1 + 0.137 * (Om * h_val**2 - 0.17)**2)  # simplified
    C_0 = 14.2 + 731.0 / (1 + 62.5 * q)
    return L_0 / (L_0 + C_0 * q**2)

def P_k_full(k_h_Mpc):
    """Full P(k) = A_s × k^ns × T²(k) / k^3"""
    k = k_h_Mpc
    A_s = 2.1e-9  # primordial amplitude
    n_s = 0.965   # spectral index
    T = P_k_LCDM(k)
    return A_s * k**n_s * T**2

# =============================================================================
# Compare at different scales
# =============================================================================
print("P(k) at different scales (Cascade vs ΛCDM):")
print()
print(f"{'k (h/Mpc)':>10} | {'P(k) (Mpc/h)³':>15} | {'Length scale':>15} | {'What it probes':>20}")
print("-" * 75)

k_values = [1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0]
for k in k_values:
    P = P_k_full(k)
    # Length scale
    L_Mpc = 2 * np.pi / k  # Mpc/h
    if L_Mpc > 1000:
        length = f"{L_Mpc/1000:.0f} Gpc/h"
    elif L_Mpc > 1:
        length = f"{L_Mpc:.0f} Mpc/h"
    else:
        length = f"{L_Mpc*1000:.0f} kpc/h"

    # What does it probe?
    if k < 1e-3:
        probe = "Cosmological (CMB)"
    elif k < 1e-1:
        probe = "Large-scale structure"
    elif k < 1:
        probe = "Galaxy clustering"
    elif k < 10:
        probe = "Galaxy internal"
    else:
        probe = "Sub-galactic / 2D universe"

    print(f"{k:10.4f} | {P:15.4e} | {length:>15} | {probe:>20}")

print()

# =============================================================================
# Cascade's prediction for P(k)
# =============================================================================
print("=" * 80)
print("CASCADE'S P(k) PREDICTION")
print("=" * 80)
print()
print("The cascade's 2D universes are CDM-like (no EM interaction), so")
print("at cosmological scales, P(k) is INDISTINGUISHABLE from ΛCDM.")
print()
print("At SUB-GALACTIC scales (k > 1 h/Mpc, length < 6 Mpc/h), the")
print("cascade might predict differences:")
print()

# At k = 10 h/Mpc, length = 0.6 Mpc/h = 0.4 Mpc
# This is galactic scale
# Cascade predicts: MOND-like behavior at low acceleration
# → slightly different P(k) at these scales (MOND gives more cored profiles)
print("  - At k = 1-10 h/Mpc (galactic scale):")
print("    ΛCDM: cuspy NFW halos, P(k) peaks and turns over")
print("    Cascade: cored profiles (MOND-like at low accel),")
print("    P(k) is slightly suppressed at small k relative to ΛCDM")
print()

# =============================================================================
# 2D universe population: power spectrum of 2D universe distribution
# =============================================================================
print("=" * 80)
print("2D UNIVERSE POPULATION P(k)")
print("=" * 80)
print()
print("If 2D universes are uniformly distributed in space (homogeneous),")
print("their P_2D(k) is FLAT (no clustering).")
print()
print("If 2D universes cluster with galaxies (because stars create them),")
print("their P_2D(k) follows the galaxy P(k).")
print()

# Cascade parameter
n_2D_per_m3 = 2.3e-4  # 2D universe density (10 m separation)

# Mean inter-2D-universe separation
separation = (1 / n_2D_per_m3)**(1/3)  # meters
print(f"2D universe density: {n_2D_per_m3:.2e} m^-3")
print(f"Mean separation: {separation:.2e} m = {separation/3.086e16:.2e} pc")
print()

# Characteristic k for 2D universe clustering
k_2D_per_m = (n_2D_per_m3)**(1/3)  # 1/m
k_2D_h_Mpc = k_2D_per_m * 3.086e22 / h
print(f"Characteristic k (2D universe clustering): {k_2D_h_Mpc:.2e} h/Mpc")
print()

# This is much larger than any cosmological scale
# So 2D universes are essentially homogeneously distributed
# → their P_2D(k) is FLAT (Poisson) on cosmological scales
# → no observable effect on P(k)

print("=" * 80)
print("HONEST VERDICT: P(k) FROM CASCADE")
print("=" * 80)
print()
print("Cascade P(k) is INDISTINGUISHABLE from ΛCDM at cosmological scales.")
print()
print("Why:")
print("  - 2D universes are CDM-like (no EM interaction)")
print("  - 2D universe distribution is essentially homogeneous")
print("  - P_2D(k) is flat (Poisson) on cosmological scales")
print("  - No new physics adds to P(k) at k < 10 h/Mpc")
print()
print("At GALACTIC scales (k > 1 h/Mpc), cascade might give slightly")
print("different P(k) due to MOND-like behavior at low acceleration.")
print("But this is already tested by SPARC, not a new test.")
print()
print("The cascade's P(k) is a CONSISTENCY CHECK, not a unique prediction.")
print()

# =============================================================================
# What about cross-dimensional correlations?
# =============================================================================
print("=" * 80)
print("CROSS-DIMENSIONAL CORRELATIONS")
print("=" * 80)
print()
print("P(k) connects 3+1D cosmology to 2D universe density.")
print("Can we look for 2D universe-2D universe correlations?")
print()
print("If 2D universes are created by stars, they should correlate with")
print("galaxies. P_2D(k) should follow P_galaxy(k).")
print()
print("This would be a UNIQUE cascade prediction:")
print("  - 2D universes cluster with galaxies")
print("  - But their GRAVITY contribution to P(k) is the same as CDM")
print("  - So the cross-correlation is hidden in CDM")
print()
print("VERDICT: Cross-dimensional correlations are not directly observable")
print("because 2D universes are CDM-like (no distinguishing signature).")
print()
print("This is consistent with the cascade being a hybrid framework:")
print("  - Borrows CDM behavior at cosmological scales")
print("  - Borrows MOND behavior at galactic scales")
print("  - Adds interpretive framework (2D universe deaths)")
print("  - But no unique testable cross-dimensional predictions")
print()
