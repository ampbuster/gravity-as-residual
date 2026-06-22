#!/usr/bin/env python3
"""
v27_cascade_all_forms.py
==========================
Try ALL possible forms for G(E, environment) and see which fits the data.

The cascade's CMB gap requires a mechanism that:
  - At z=0: predicted DM ≈ 2.0e-10 J/m^3
  - At z=1100: predicted DM ≈ 0.085 J/m^3

Forms to try:
  A. G(E) only (baseline)
  B. G(E) × (1+z)^n
  C. G(E) × (1+z)^n (negative exponent)
  D. G(E) × |P(z)|^n
  E. G(E) × (H(z)/H_0)^n
  F. G(E) × |dP/dt|^n
  G. G(E) × (1+z)^n × |P(z)|^m
  H. G(E) × (1+z)^n × sigmoid(α × P)
  I. G(E) × exp(-z/z_scale)
  J. G(E) × exp(+z/z_scale)

For each form, fit free parameters and report fit quality.


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
a_rad = 7.5657e-16
T_0 = 2.725
f_attractive = 0.32
G_max = 9.7e7
E_SN = 1e44
E_pp = m_p_c2
beta = 0.43  # slope of G(E) interpolation
f_E = lambda E: (E / E_SN) ** beta


def pressure_total(z):
    T = T_0 * (1 + z)
    P_rad = a_rad * T**4 / 3
    rho_DE = Omega_Lambda * rho_crit_mass_0 * c**2
    return P_rad - rho_DE


def H_z(z):
    return H_0 * np.sqrt(Omega_m * (1+z)**3 + Omega_Lambda)


def dP_dt(z):
    """Time derivative of pressure."""
    dz = 0.001
    return (pressure_total(z + dz) - pressure_total(z - dz)) / (2 * dz / H_z(z))


# -----------------------------------------------------------------------------
# Cumulative energies
# -----------------------------------------------------------------------------
def cumulative_pp(z_obs, z_max=2000, n_samples=2000):
    z_arr = np.linspace(z_obs, z_max, n_samples)
    cumulative_E = 0.0
    cumulative_weighted = 0.0  # for forms with z-dependent weight
    for i, z_i in enumerate(z_arr):
        if i == 0:
            continue
        n_b = Omega_b * rho_crit_mass_0 * (1+z_i)**3 / m_p
        n_gamma = 4.1e8 * (1+z_i)**3
        rate = n_b * n_gamma * sigma_T * c
        H = H_z(z_i)
        if H > 0 and (1 + z_i) > 0:
            dt = (z_arr[i] - z_arr[i-1]) / (H * (1 + z_i))
            dE = rate * m_p_c2 * dt
            cumulative_E += dE
    return cumulative_E


def cumulative_pp_weighted(z_obs, weight_func, z_max=2000, n_samples=2000):
    """Cumulative pp energy weighted by some function of z."""
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
            w = weight_func(z_i)
            dE = rate * m_p_c2 * dt * w
            cumulative_E += dE
    return cumulative_E


def obs_DM(z):
    H = H_z(z)
    rho_crit_mass_z = 3 * H**2 / (8 * math.pi * G)
    return Omega_c * rho_crit_mass_z * c**2


# -----------------------------------------------------------------------------
# Pre-compute cumulative energies
# -----------------------------------------------------------------------------
E_pp_0 = cumulative_pp(0)
E_pp_1100 = cumulative_pp(1100)
E_SN_0 = 7.5e-18  # J/m^3 from paper

obs_0 = obs_DM(0)
obs_1100 = obs_DM(1100)

print("="*80)
print("DATA POINTS")
print("="*80)
print(f"  E_pp(0)     = {E_pp_0:.3e} J/m^3")
print(f"  E_pp(1100)  = {E_pp_1100:.3e} J/m^3")
print(f"  E_SN(0)     = {E_SN_0:.3e} J/m^3")
print(f"  obs(0)      = {obs_0:.3e} J/m^3")
print(f"  obs(1100)   = {obs_1100:.3e} J/m^3")
print()


# -----------------------------------------------------------------------------
# Form A: G(E) only (baseline, no z-dependence)
# -----------------------------------------------------------------------------
def form_A():
    # G = G_max × f(E)  (no z-dependence)
    # We need: 0.32 × G_max × f(E_pp) × E_pp_total = obs
    # 2 equations, but no free parameter (G_max, f(E) are calibrated)
    # 1 equation for SN, 1 for pp
    # SN at z=0: 0.32 × 9.7e7 × 1 × 7.5e-18 = 2.3e-10 (matches obs 2.0e-10)
    # pp at z=0:  0.32 × 9.7e7 × 7.3e-26 × 4e14 = 9.1e-5 (overshoots by 4e5)
    # pp at z=1100: 0.32 × 9.7e7 × 7.3e-26 × 3.7e14 = 8.5e-5 (overshoots by 1)
    pred_0 = f_attractive * G_max * f_E(E_pp) * E_pp_0 + f_attractive * G_max * f_E(E_SN) * E_SN_0
    pred_1100 = f_attractive * G_max * f_E(E_pp) * E_pp_1100
    return pred_0, obs_0, pred_1100, obs_1100


# -----------------------------------------------------------------------------
# Form B: G(E) × (1+z)^n
# -----------------------------------------------------------------------------
def form_B(n):
    weight = lambda z: (1 + z) ** n
    E_pp_0_w = cumulative_pp_weighted(0, weight)
    E_pp_1100_w = cumulative_pp_weighted(1100, weight)
    # SN at z=0: G evaluated at z=0
    g_sn_0 = G_max * f_E(E_SN) * (1 + 0) ** n
    g_pp_1100 = G_max * f_E(E_pp) * (1 + 1100) ** n
    pred_0 = f_attractive * g_sn_0 * E_SN_0 + f_attractive * G_max * f_E(E_pp) * E_pp_0_w
    pred_1100 = f_attractive * g_pp_1100 * E_pp_1100
    return pred_0, obs_0, pred_1100, obs_1100


# -----------------------------------------------------------------------------
# Form C: G(E) × |P(z)|^n
# -----------------------------------------------------------------------------
def form_C(n):
    weight = lambda z: abs(pressure_total(z)) ** n if pressure_total(z) != 0 else 0
    E_pp_0_w = cumulative_pp_weighted(0, weight)
    E_pp_1100_w = cumulative_pp_weighted(1100, weight)
    g_sn_0 = G_max * f_E(E_SN) * abs(pressure_total(0)) ** n
    g_pp_1100 = G_max * f_E(E_pp) * abs(pressure_total(1100)) ** n
    pred_0 = f_attractive * g_sn_0 * E_SN_0 + f_attractive * G_max * f_E(E_pp) * E_pp_0_w
    pred_1100 = f_attractive * g_pp_1100 * E_pp_1100
    return pred_0, obs_0, pred_1100, obs_1100


# -----------------------------------------------------------------------------
# Form D: G(E) × (H(z)/H_0)^n
# -----------------------------------------------------------------------------
def form_D(n):
    weight = lambda z: (H_z(z) / H_0) ** n
    E_pp_0_w = cumulative_pp_weighted(0, weight)
    E_pp_1100_w = cumulative_pp_weighted(1100, weight)
    g_sn_0 = G_max * f_E(E_SN) * 1 ** n  # at z=0
    g_pp_1100 = G_max * f_E(E_pp) * (H_z(1100) / H_0) ** n
    pred_0 = f_attractive * g_sn_0 * E_SN_0 + f_attractive * G_max * f_E(E_pp) * E_pp_0_w
    pred_1100 = f_attractive * g_pp_1100 * E_pp_1100
    return pred_0, obs_0, pred_1100, obs_1100


# -----------------------------------------------------------------------------
# Form E: G(E) × |dP/dt|^n
# -----------------------------------------------------------------------------
def form_E(n):
    weight = lambda z: abs(dP_dt(z)) ** n if abs(dP_dt(z)) > 0 else 0
    E_pp_0_w = cumulative_pp_weighted(0, weight)
    E_pp_1100_w = cumulative_pp_weighted(1100, weight)
    g_sn_0 = G_max * f_E(E_SN) * abs(dP_dt(0)) ** n
    g_pp_1100 = G_max * f_E(E_pp) * abs(dP_dt(1100)) ** n
    pred_0 = f_attractive * g_sn_0 * E_SN_0 + f_attractive * G_max * f_E(E_pp) * E_pp_0_w
    pred_1100 = f_attractive * g_pp_1100 * E_pp_1100
    return pred_0, obs_0, pred_1100, obs_1100


# -----------------------------------------------------------------------------
# Form F: G(E) × exp(-z/z_scale)
# -----------------------------------------------------------------------------
def form_F(z_scale):
    weight = lambda z: math.exp(-z / z_scale)
    E_pp_0_w = cumulative_pp_weighted(0, weight)
    E_pp_1100_w = cumulative_pp_weighted(1100, weight)
    g_sn_0 = G_max * f_E(E_SN) * 1  # exp(0) = 1
    g_pp_1100 = G_max * f_E(E_pp) * math.exp(-1100 / z_scale)
    pred_0 = f_attractive * g_sn_0 * E_SN_0 + f_attractive * G_max * f_E(E_pp) * E_pp_0_w
    pred_1100 = f_attractive * g_pp_1100 * E_pp_1100
    return pred_0, obs_0, pred_1100, obs_1100


# -----------------------------------------------------------------------------
# Form G: G(E) × (1+z)^n × |P(z)|^m
# -----------------------------------------------------------------------------
def form_G(n, m):
    weight = lambda z: ((1 + z) ** n) * (abs(pressure_total(z)) ** m if pressure_total(z) != 0 else 0)
    E_pp_0_w = cumulative_pp_weighted(0, weight)
    E_pp_1100_w = cumulative_pp_weighted(1100, weight)
    g_sn_0 = G_max * f_E(E_SN) * (1 + 0) ** n * abs(pressure_total(0)) ** m
    g_pp_1100 = G_max * f_E(E_pp) * (1 + 1100) ** n * abs(pressure_total(1100)) ** m
    pred_0 = f_attractive * g_sn_0 * E_SN_0 + f_attractive * G_max * f_E(E_pp) * E_pp_0_w
    pred_1100 = f_attractive * g_pp_1100 * E_pp_1100
    return pred_0, obs_0, pred_1100, obs_1100


# -----------------------------------------------------------------------------
# Run all forms
# -----------------------------------------------------------------------------
def test_form(name, pred_0, obs_0, pred_1100, obs_1100):
    r0 = pred_0 / obs_0 if obs_0 > 0 else float('inf')
    r1100 = pred_1100 / obs_1100 if obs_1100 > 0 else float('inf')
    ok_0 = "✓" if 0.5 < r0 < 2 else "✗"
    ok_1100 = "✓" if 0.5 < r1100 < 2 else "✗"
    print(f"  {name:<30} z=0: {r0:>8.3e} {ok_0}  z=1100: {r1100:>8.3e} {ok_1100}")
    return r0, r1100


def main():
    print("="*80)
    print("FORM A: G(E) only (baseline)")
    print("="*80)
    p0, o0, p11, o11 = form_A()
    test_form("A: G(E) only", p0, o0, p11, o11)
    print()

    print("="*80)
    print("FORM B: G(E) × (1+z)^n")
    print("="*80)
    for n in [-3, -1, 0, 1, 3, 5, 7, 10]:
        p0, o0, p11, o11 = form_B(n)
        test_form(f"B: (1+z)^{n}", p0, o0, p11, o11)
    print()

    print("="*80)
    print("FORM C: G(E) × |P(z)|^n")
    print("="*80)
    for n in [0, 0.5, 1, 2, 3, 5]:
        p0, o0, p11, o11 = form_C(n)
        test_form(f"C: |P|^{n}", p0, o0, p11, o11)
    print()

    print("="*80)
    print("FORM D: G(E) × (H/H_0)^n")
    print("="*80)
    for n in [0, 1, 2, 3, 5, 7, 10]:
        p0, o0, p11, o11 = form_D(n)
        test_form(f"D: (H/H_0)^{n}", p0, o0, p11, o11)
    print()

    print("="*80)
    print("FORM E: G(E) × |dP/dt|^n")
    print("="*80)
    for n in [0, 0.5, 1, 2, 3]:
        p0, o0, p11, o11 = form_E(n)
        test_form(f"E: |dP/dt|^{n}", p0, o0, p11, o11)
    print()

    print("="*80)
    print("FORM F: G(E) × exp(-z/z_scale)")
    print("="*80)
    for z_scale in [10, 50, 100, 200, 500, 1000]:
        p0, o0, p11, o11 = form_F(z_scale)
        test_form(f"F: z_scale={z_scale}", p0, o0, p11, o11)
    print()

    print("="*80)
    print("FORM G: G(E) × (1+z)^n × |P(z)|^m")
    print("="*80)
    for n, m in [(0, 1), (1, 1), (-1, 1), (1, 0), (0, 2), (-1, 0.5), (0.5, 0.5)]:
        p0, o0, p11, o11 = form_G(n, m)
        test_form(f"G: (1+z)^{n} * |P|^{m}", p0, o0, p11, o11)
    print()

    print("="*80)
    print("LEGEND")
    print("="*80)
    print("  ✓ : predicted/observed ratio between 0.5 and 2 (good fit)")
    print("  ✗ : ratio outside 0.5-2 (bad fit)")
    print()
    print("  A: baseline (G only depends on E) — should fail")
    print("  B: G scales with (1+z)^n")
    print("  C: G scales with |P|^n (pressure)")
    print("  D: G scales with (H/H_0)^n (expansion rate)")
    print("  E: G scales with |dP/dt|^n (pressure change rate)")
    print("  F: G scales with exp(-z/z_scale) (epoch decay)")
    print("  G: combined (1+z) and |P| dependence")


if __name__ == "__main__":
    main()
