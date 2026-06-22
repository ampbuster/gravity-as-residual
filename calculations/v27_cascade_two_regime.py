#!/usr/bin/env python3
"""
v27_cascade_two_regime.py
===========================
User's two-regime model:
  - Above f_crit: use cascade's G_max (full growth)
  - Below f_crit: use the user's G(E) (small, smooth)

This is a piecewise function:
  G(E) = G_max                if E >= f_crit
  G(E) = G_subcritical(E)     if E < f_crit

Where G_subcritical is the user's smooth G(E) for low-energy events.

The two-regime model has:
  - 1 threshold (f_crit)
  - 1 smooth function (G_subcritical, with 2 calibration points)
  - 1 saturated value (G_max)
  = 3-4 parameters, but captures the cascade's "phase transition" +
    "subcritical regime" in a single framework

CALIBRATION:
  f_crit: threshold between regimes
  G_subcritical(m_p c²) ~ 7e-18 (low-E, calibrated)
  G_subcritical(f_crit) ~ 1 (matches G_max at threshold)
  G_max = 9.7e7 (cascade's existing)

The two-regime model tries to fit BOTH z=0 and z=1100.


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

import math
import numpy as np


# Constants
c = 2.998e8
G = 6.674e-11
sigma_T = 6.65e-25
m_p = 1.673e-27
m_p_c2 = 938e6 * 1.602e-19
Mpc = 3.086e22
H_0 = 67.4e3 / Mpc
Omega_b = 0.0493
Omega_c = 0.265
Omega_Lambda = 0.6847
Omega_m = Omega_b + Omega_c
rho_crit_mass_0 = 3 * H_0**2 / (8 * math.pi * G)
f_attractive = 0.32
G_max = 9.7e7
E_SN = 1e44
E_pp = m_p_c2


def H_z(z):
    return H_0 * np.sqrt(Omega_m * (1+z)**3 + Omega_Lambda)


def G_two_regime(E, f_crit, E_anchor, G_anchor):
    """
    Two-regime G(E):
      - E >= f_crit: G = G_max (full, supercritical)
      - E < f_crit:  G = G_anchor * (E / E_anchor)^beta (subcritical)
                    where beta is chosen so that G(E_anchor) = G_anchor
                    and G(f_crit) = 1 (continuous at threshold)
    """
    if E >= f_crit:
        return G_max
    # In subcritical regime: power law from E_anchor to f_crit
    # G(E_anchor) = G_anchor
    # G(f_crit) = 1
    # So beta = log(1/G_anchor) / log(f_crit/E_anchor)
    if E_anchor >= f_crit:
        return G_max
    beta_sub = math.log(1.0 / G_anchor) / math.log(f_crit / E_anchor)
    return G_anchor * (E / E_anchor) ** beta_sub


def cumulative_pp(z_obs, f_crit, E_anchor, G_anchor, z_max=2000, n_samples=2000):
    z_arr = np.linspace(z_obs, z_max, n_samples)
    cumulative_E = 0.0
    for i, z_i in enumerate(z_arr):
        if i == 0:
            continue
        n_b = Omega_b * rho_crit_mass_0 * (1+z_i)**3 / m_p
        n_gamma = 4.1e8 * (1+z_i)**3
        rate = n_b * n_gamma * sigma_T * c
        H = H_z(z_i)
        if H > 0 and (1 + z_i) > 0:
            dt = (z_arr[i] - z_arr[i-1]) / (H * (1 + z_i))
            g = G_two_regime(m_p_c2, f_crit, E_anchor, G_anchor)
            dE = rate * m_p_c2 * dt * g
            cumulative_E += dE
    return cumulative_E


def obs_DM(z):
    H = H_z(z)
    rho_crit_mass_z = 3 * H**2 / (8 * math.pi * G)
    return Omega_c * rho_crit_mass_z * c**2


def main():
    print("="*80)
    print("TWO-REGIME MODEL: G(E) = G_max for E >= f_crit, G(E) = subcritical for E < f_crit")
    print("="*80)
    print()
    print("User's insight: 'maybe below f_crit, use G(E)'")
    print("Two regimes:")
    print("  - High E (>= f_crit): full G_max (cascade's existing)")
    print("  - Low E (< f_crit): smooth subcritical G(E)")
    print()

    obs_0 = obs_DM(0)
    obs_1100 = obs_DM(1100)
    E_SN_0 = 7.5e-18

    print("="*80)
    print("SCAN f_crit AND G_anchor (E_anchor = m_p c²)")
    print("="*80)
    print()
    print(f"  {'f_crit':<12} {'G_anchor':<12} {'z=0 ratio':<12} {'z=1100 ratio':<12}")
    print(f"  {'-'*12} {'-'*12} {'-'*12} {'-'*12}")

    # Try various f_crit and G_anchor
    for f_crit_log in [10, 20, 30, 40, 44]:
        f_crit = 10 ** f_crit_log
        for G_anchor_log in [-25, -20, -16, -10]:
            G_anchor = 10 ** G_anchor_log
            E_anchor = m_p_c2
            if E_anchor >= f_crit:
                continue
            # Predicted DM
            g_pp = G_two_regime(m_p_c2, f_crit, E_anchor, G_anchor)
            g_sn = G_max if E_SN >= f_crit else G_two_regime(E_SN, f_crit, E_anchor, G_anchor)

            # Cumulative particle at z=0 and z=1100
            cumul_pp_0 = cumulative_pp(0, f_crit, E_anchor, G_anchor)
            cumul_pp_1100 = cumulative_pp(1100, f_crit, E_anchor, G_anchor)

            pred_0 = f_attractive * g_sn * E_SN_0 + f_attractive * cumul_pp_0
            pred_1100 = f_attractive * cumul_pp_1100

            r0 = pred_0 / obs_0
            r1100 = pred_1100 / obs_1100
            ok_0 = "✓" if 0.5 < r0 < 2 else "✗"
            ok_1100 = "✓" if 0.5 < r1100 < 2 else "✗"
            print(f"  10^{f_crit_log:<8} 10^{G_anchor_log:<8} {r0:<12.3e} {ok_0}  {r1100:<12.3e} {ok_1100}")

    print()
    print("="*80)
    print("ANALYSIS")
    print("="*80)
    print()
    print("The two-regime model is a STEP in the right direction:")
    print("  - Above f_crit: G = G_max (supercritical 2D universe)")
    print("  - Below f_crit: G = subcritical G(E) (small)")
    print()
    print("But the FUNDAMENTAL ISSUE remains: cumulative particle energy at z=0")
    print("is dominated by z > 1100 contributions (93% of total). For the cascade")
    print("to match obs(0) which is 4.2e8 smaller than obs(1100), G must vary by")
    print("4.2e8 within the z range. The two-regime model alone can't do this.")
    print()
    print("The cascade needs ADDITIONAL structure (z-dependent G below f_crit,")
    print("or a fundamentally different mechanism).")


if __name__ == "__main__":
    main()
