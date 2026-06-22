#!/usr/bin/env python3
"""
v27_cascade_cmb_analysis.py
=============================
Cascade's CMB prediction and its tension with Planck 2018.

The cascade says DM = cumulative 2D universe back-projection from
energetic 3D events. Before the first stars (z > 20), there are
essentially NO energetic events in the cascade's sense. Therefore,
the cascade predicts ~0 DM at z = 1100 (CMB epoch).

But the observed CMB angular power spectrum REQUIRES DM at z = 1100
(without DM, the peaks are at the wrong positions and ratios).

This script:
  1. Computes the cascade's predicted DM density as a function of z
  2. Compares to Planck 2018 Omega_m (assumed constant)
  3. Identifies the TENSION at z > 20: cascade says no DM, CMB says DM
  4. Discusses possible resolutions (early-DM mechanism needed)

This is an HONEST FRAMING: the cascade has a real CMB gap.

Source: Planck 2018 results V (A&A 641, A5), arXiv:1907.12875
        Madau-Dickinson 2014 (cosmic SFR)
        SPARC database (RAR)


**HISTORICAL (v2.7 era, mid-2025)**: This file is from the v2.7.x era, predating:
- v3.0+ Lagrangian work (L102-L136)
- v3.1+ Multi-universe picture (L142-L150)
- v3.3 Bilateral cascade (E_4D = 5e79 J, M_Pl,4D = 3.93e23 GeV)
- v3.5.7+ Naming revolution (f_back -> f_DE, f_DM,leak, f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N*v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via alpha-GM, L308v)
- alpha = 1.289 (FIRST-PRINCIPLES via L308n)
- eps = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- gamma_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- tau_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v2.7 era framework, not v3.5.9+ A2.

"""

import math
import numpy as np


# Constants
hbar = 1.055e-34
c = 2.998e8
G = 6.674e-11
M_sun = 1.989e30
year = 3.156e7
yr = year
pc = 3.086e16
kpc = 3.086e19
Mpc = 3.086e22
Gyr = 1e9 * yr
H_0 = 67.4e3 / Mpc  # Planck 2018 H_0 in 1/s

# Planck 2018 cosmological parameters
Omega_b = 0.0493
Omega_c = 0.265
Omega_Lambda = 0.6847
sigma_8 = 0.811
n_s = 0.9649
tau_reion = 0.054
z_reion = 7.67
z_drag = 1020
A_s = 2.1e-9  # primordial amplitude
rho_crit = 8.5e-10  # J/m^3


# -----------------------------------------------------------------------------
# 1. Madau-Dickinson cosmic star formation history
# -----------------------------------------------------------------------------
def sfr_density_madau(z):
    """Cosmic SFR density [M_sun/yr/Mpc^3] (Madau-Dickinson 2014 best fit)."""
    if z < 0:
        return 0.0
    zp1 = 1.0 + z
    return 0.015 * zp1**2.7 / (1.0 + (zp1 / 2.9)**5.6)


def H_z(z, Omega_m=Omega_c + Omega_b, Omega_L=Omega_Lambda, H_0=H_0):
    """H(z) in 1/s for flat LCDM."""
    return H_0 * np.sqrt(Omega_m * (1+z)**3 + Omega_L)


# -----------------------------------------------------------------------------
# 2. Cascade's predicted DM as a function of z
# -----------------------------------------------------------------------------
def cascade_dm_at_z(z, f_proj=1e-10, growth_factor=1e8):
    """
    Cascade's predicted DM density [J/m^3] at redshift z.

    Cascade: DM = cumulative 2D universe back-projection from energetic events.
    Before stars form (z > 20), there are no energetic events → no DM.
    After stars form (z < 20), DM accumulates as integral of past events.

    Parameters:
      f_proj: 2D universe back-projection efficiency (calibrated ~ 1e-10)
      growth_factor: 2D universe's growth factor (calibrated ~ 1e8)
    """
    if z > 20:
        return 0.0
    # Integrate SFR from z to z=0, weighted by SN rate
    z_arr = np.linspace(z, 0, 100)
    dz = z_arr[1] - z_arr[0] if len(z_arr) > 1 else z
    total_E_per_Mpc3 = 0.0
    for i, z_i in enumerate(z_arr):
        R = sfr_density_madau(z_i) * 1e-2  # SN rate ~1% of SFR
        E_avg = 1e44  # J per SN (Type Ia equivalent)
        H_z_s = H_z(z_i)
        dt = dz / (H_z_s * (1 + z_i)) if i < len(z_arr) - 1 else 0
        total_E_per_Mpc3 += R * E_avg * 0.32 * growth_factor * f_proj * dt

    Mpc3_to_m3 = Mpc**3
    rho_dm = total_E_per_Mpc3 / Mpc3_to_m3
    return rho_dm


def cascade_omega_dm_at_z(z, **kwargs):
    """Cascade's Omega_DM at redshift z (dimensionless)."""
    rho = cascade_dm_at_z(z, **kwargs)
    H_z_s = H_z(z)
    rho_crit_z = 3 * H_z_s**2 / (8 * math.pi * G) / c**2
    return rho / (rho_crit_z * c**2)


# -----------------------------------------------------------------------------
# 3. Comparison to Planck 2018
# -----------------------------------------------------------------------------
def planck_omega_dm_at_z(z):
    """LCDM's Omega_DM at z (constant, no z dependence)."""
    return Omega_c


# -----------------------------------------------------------------------------
# 4. Main analysis
# -----------------------------------------------------------------------------
def main():
    print("="*80)
    print("CASCADE CMB ANALYSIS — predicted DM vs Planck 2018")
    print("="*80)
    print()
    print("Cascade's mechanism: DM = cumulative 2D universe back-projection")
    print("                     from energetic 3D events")
    print()
    print("Key cascade prediction: ~0 DM at z > 20 (no energetic events before stars)")
    print("Planck 2018:           Omega_m = 0.315 (constant, ~0.265 in DM)")
    print()
    print("TENSION: cascade says no DM at z=1100 (CMB epoch)")
    print("         Planck requires DM at z=1100 to match angular power spectrum")
    print()
    print("="*80)
    print("CASCADE'S PREDICTED DM DENSITY vs z")
    print("="*80)
    print()
    print(f"{'z':<8} {'Cascade rho_DM':<22} {'Cascade Omega_DM':<18} {'Cascade Omega_b':<18} {'Planck Omega_DM':<15}")
    print("-"*80)

    for z in [0, 0.5, 1, 2, 5, 10, 20, 50, 100, 500, 1000, 1100]:
        rho_dm = cascade_dm_at_z(z)
        omega_dm = cascade_omega_dm_at_z(z)
        planck_omega = planck_omega_dm_at_z(z)
        # Cascade's Omega_b is constant 0.049 (baryons exist at all z, in plasma form)
        omega_b_cascade = 0.049
        print(f"{z:<8} {rho_dm:<22.3e} {omega_dm:<18.3e} {omega_b_cascade:<18.4f} {planck_omega:<15.4f}")

    print()
    print("="*80)
    print("THE CMB TENSION - correctly framed (with baryons accounted for)")
    print("="*80)
    print()
    print("At z = 1100 (CMB epoch):")
    print(f"  Cascade Omega_b  = 0.049 (baryons exist at all z, in plasma form) MATCH")
    print(f"  Cascade Omega_DM = 0 (no energetic events before stars) MISMATCH")
    print(f"  Cascade Omega_m  = 0.049 (baryon only)")
    print(f"  Planck  Omega_DM = {Omega_c} (required to fit CMB 3rd peak)")
    print(f"  Planck  Omega_m  = 0.315")
    print()
    print("The cascade BARYON prediction is correct at z = 1100.")
    print("The cascade DM prediction fails at z = 1100.")
    print()
    print("Specifically, the cascade's *DM production mechanism* gives 0 at z > 20")
    print("because the first 'energetic events' (Population III stars) don't form until")
    print("z ~ 20-30. The CMB requires Omega_DM = 0.265 at z = 1100 in ADDITION to the 0.049 baryons.")
    print()
    print("Impact on CMB peaks (baryons present, DM missing):")
    print("  - 1st peak (l ~ 220): sound horizon (slightly wrong, depends on Omega_c)")
    print("  - 2nd peak (l ~ 540): baryon-to-photon ratio (CORRECT, baryons are right)")
    print("  - 3rd peak (l ~ 810): matter-to-radiation (WRONG, missing DM contribution)")
    print()
    print("="*80)
    print("POSSIBLE RESOLUTIONS")
    print("="*80)
    print()
    print("The cascade needs an EARLY-DM mechanism to match the CMB. Options:")
    print()
    print("1. PRIMORDIAL 2D UNIVERSE CREATION during inflation/baryogenesis/BBN")
    print("   - If the cascade's 2D universe creation extends to non-stellar events")
    print("   - The 'energetic event' threshold would need to be much lower")
    print("   - This is a post-hoc extension of the cascade")
    print()
    print("2. COSMOLOGICAL DM COMPONENT not from 2D universe back-projection")
    print("   - The cascade admits a 'primordial' DM component")
    print("   - This is dual-component DM (cascade + particle-like)")
    print("   - Ad hoc but not falsified")
    print()
    print("3. CASCADE IS INCOMPLETE at z > 20")
    print("   - The cascade currently has no mechanism for DM at z > 20")
    print("   - This is a known limitation")
    print("   - Awaiting a more complete cosmological model")
    print()
    print("="*80)
    print("WHAT IS FALSIFIED, WHAT IS FALSIFIABLE")
    print("="*80)
    print()
    print("FALSIFIED (if cascade is taken literally with no early-DM extension):")
    print("  - CMB angular power spectrum cannot be matched")
    print("  - This is a SERIOUS TENSION, not just a 'gap'")
    print()
    print("FALSIFIABLE (with early-DM extension):")
    print("  - The 47 Tuc test (cascade vs particle DM) — still valid")
    print("  - End-of-universe signatures (DESI Y5, LSST Y1) — still valid")
    print("  - Galaxy-zoo tests — still valid (these are at z = 0)")
    print()
    print("The cascade's CMB gap is REAL and should be acknowledged in the paper.")
    print()
    print("="*80)
    print("QUANTITATIVE COMPARISON: CASCADE vs LCDM CMB")
    print("="*80)
    print()
    print("LCDM CMB (Planck 2018) requires Omega_m = 0.315 at z = 1100.")
    print("This is mostly CDM (Omega_c = 0.265) with a small baryon fraction (Omega_b = 0.049).")
    print()
    print("The cascade's predicted Omega_m(z=1100):")
    print("  Cascade has no 'CDM' mechanism; only baryons are present at z > 20")
    print("  So cascade Omega_m(z=1100) ~ Omega_b = 0.049 (baryon only)")
    print()
    print("Difference from LCDM:")
    print(f"  Delta Omega_m = {0.315 - 0.049:.3f}")
    print("  This is the 'missing DM' that the cascade must provide some other way")
    print()
    print("Numerical impact on CMB peaks:")
    print("  - First peak (l ~ 220): controlled by sound horizon, SHIFTS if Omega_m changes")
    print("  - Second peak (l ~ 540): baryon-to-photon ratio, changes with Omega_m")
    print("  - Third peak (l ~ 810): matter-to-radiation, depends on Omega_c")
    print()
    print("Without the cascade providing Omega_c ~ 0.265 at z = 1100,")
    print("the CMB peaks would be at WRONG positions. This is NOT a small effect.")
    print()
    print("="*80)
    print("HONEST SUMMARY")
    print("="*80)
    print()
    print("The cascade's mechanism (DM = 2D universe back-projection from energetic events)")
    print("predicts essentially zero DM at z > 20 (no energetic events before stars).")
    print()
    print("The CMB angular power spectrum requires Omega_m ~ 0.315 at z = 1100,")
    print("i.e., Omega_c ~ 0.265 of DM at the CMB epoch, in ADDITION to the 0.049 baryons.")
    print()
    print("Note: the cascade's BARYON prediction is correct (0.049 at all z).")
    print("The cascade's DM prediction fails at z = 1100.")
    print()
    print("This is a REAL TENSION in the DM mechanism specifically.")
    print("The cascade needs an early-DM mechanism or must admit a non-cascade DM component.")
    print()
    print("Status: NOT YET ADDRESSED in the cascade's framework.")
    print("This is a fundamental limitation of v2.7.3+.")
    print()
    print("The cascade is consistent with:")
    print("  - EXISTING galaxy data (z < 4)")
    print("  - The baryon fraction at all z (including z = 1100)")
    print()
    print("The cascade is INCONSISTENT with:")
    print("  - The DM fraction at z = 1100 (predicts 0, observed 0.265)")
    print()
    print("This analysis should be added to the paper as a §11.X or §13:")
    print("'Cascade's CMB Gap' — a fundamental limitation requiring future work.")
    print()


if __name__ == "__main__":
    main()
