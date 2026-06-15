#!/usr/bin/env python3
"""
v27_cascade_exotic_forms.py
=============================
Try more exotic forms for G(E, z) that might fit both data points.

The fundamental issue: cumulative particle energy at z=0 (4e14 J/m^3)
is dominated by z > 1100 contributions (3.7e14 = 93% of total).
The observed DM at z=0 is 4.5e8 smaller than at z=1100.

This means: G must be much LARGER for events at z=1100 than for events
at z just below 1100. Specifically, the ratio G(z=1100)/G(z<1100)
must be ~5e8 to match the data.

Forms to try:
  H. Sigmoid in z: G ∝ sigmoid(α(z-z_0))
  I. Power of (1+z) with very high n
  J. Hill function: G ∝ (1+z)^n / (1 + (z/z_0)^m)
  K. 1/(1 + (z/z_0)^(-n)) = 1 for z >> z_0, 0 for z << z_0 (hard step)
  L. Gaussian: G ∝ exp(-(z-z_0)^2 / (2σ^2))
  M. Sum of multiple factors
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
beta = 0.43
f_E = lambda E: (E / E_SN) ** beta


def H_z(z):
    return H_0 * np.sqrt(Omega_m * (1+z)**3 + Omega_Lambda)


def obs_DM(z):
    H = H_z(z)
    rho_crit_mass_z = 3 * H**2 / (8 * math.pi * G)
    return Omega_c * rho_crit_mass_z * c**2


def cumulative_pp(z_obs, weight_func, z_max=2000, n_samples=2000):
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


E_pp_0 = cumulative_pp(0, lambda z: 1)
E_pp_1100 = cumulative_pp(1100, lambda z: 1)
E_SN_0 = 7.5e-18
obs_0 = obs_DM(0)
obs_1100 = obs_DM(1100)

print(f"  E_pp(0)     = {E_pp_0:.3e} J/m^3")
print(f"  E_pp(1100)  = {E_pp_1100:.3e} J/m^3")
print(f"  obs(0)      = {obs_0:.3e} J/m^3")
print(f"  obs(1100)   = {obs_1100:.3e} J/m^3")
print(f"  obs(1100)/obs(0) = {obs_1100/obs_0:.3e}")
print(f"  E_pp(1100)/E_pp(0) = {E_pp_1100/E_pp_0:.3f}")
print()


# -----------------------------------------------------------------------------
# Form H: Hill function
# G(z) = (1+z)^n / (K + (1+z)^n) where K is the half-saturation
# For (1+z) << K^1/n: G ~ (1+z)^n / K (small)
# For (1+z) >> K^1/n: G ~ 1 (saturated)
# -----------------------------------------------------------------------------
def form_H(n, K):
    weight = lambda z: (1 + z) ** n / (K + (1 + z) ** n)
    E_pp_0_w = cumulative_pp(0, weight)
    E_pp_1100_w = cumulative_pp(1100, weight)
    g_sn_0 = G_max * f_E(E_SN) * 1 / (K + 1)  # at z=0
    g_pp_1100 = G_max * f_E(E_pp) * 1101 ** n / (K + 1101 ** n)
    pred_0 = f_attractive * g_sn_0 * E_SN_0 + f_attractive * G_max * f_E(E_pp) * E_pp_0_w
    pred_1100 = f_attractive * g_pp_1100 * E_pp_1100_w
    return pred_0, pred_1100


# -----------------------------------------------------------------------------
# Form I: Sigmoid in z
# G(z) = 1 / (1 + exp(-(z - z_0) / scale))
# -----------------------------------------------------------------------------
def form_I(z_0, scale):
    weight = lambda z: 1 / (1 + math.exp(-(z - z_0) / scale))
    E_pp_0_w = cumulative_pp(0, weight)
    E_pp_1100_w = cumulative_pp(1100, weight)
    g_sn_0 = G_max * f_E(E_SN) * 1 / (1 + math.exp(-(0 - z_0) / scale))
    g_pp_1100 = G_max * f_E(E_pp) * 1 / (1 + math.exp(-(1100 - z_0) / scale))
    pred_0 = f_attractive * g_sn_0 * E_SN_0 + f_attractive * G_max * f_E(E_pp) * E_pp_0_w
    pred_1100 = f_attractive * g_pp_1100 * E_pp_1100_w
    return pred_0, pred_1100


# -----------------------------------------------------------------------------
# Form J: Gaussian centered at z_0
# G(z) = exp(-(z - z_0)^2 / (2 sigma^2))
# -----------------------------------------------------------------------------
def form_J(z_0, sigma):
    weight = lambda z: math.exp(-(z - z_0)**2 / (2 * sigma**2))
    E_pp_0_w = cumulative_pp(0, weight)
    E_pp_1100_w = cumulative_pp(1100, weight)
    g_sn_0 = G_max * f_E(E_SN) * math.exp(-(0 - z_0)**2 / (2 * sigma**2))
    g_pp_1100 = G_max * f_E(E_pp) * math.exp(-(1100 - z_0)**2 / (2 * sigma**2))
    pred_0 = f_attractive * g_sn_0 * E_SN_0 + f_attractive * G_max * f_E(E_pp) * E_pp_0_w
    pred_1100 = f_attractive * g_pp_1100 * E_pp_1100_w
    return pred_0, pred_1100


# -----------------------------------------------------------------------------
# Form K: Power law with hard cutoff
# G(z) = (1+z)^n for z < z_cut, G = (1+z_cut)^n for z > z_cut
# -----------------------------------------------------------------------------
def form_K(n, z_cut):
    weight = lambda z: (1 + z) ** n if z < z_cut else (1 + z_cut) ** n
    E_pp_0_w = cumulative_pp(0, weight)
    E_pp_1100_w = cumulative_pp(1100, weight)
    g_sn_0 = G_max * f_E(E_SN) * (1 + 0) ** n
    g_pp_1100 = G_max * f_E(E_pp) * weight(1100)
    pred_0 = f_attractive * g_sn_0 * E_SN_0 + f_attractive * G_max * f_E(E_pp) * E_pp_0_w
    pred_1100 = f_attractive * g_pp_1100 * E_pp_1100_w
    return pred_0, pred_1100


def test_form(name, pred_0, pred_1100):
    r0 = pred_0 / obs_0
    r1100 = pred_1100 / obs_1100
    ok_0 = "✓" if 0.5 < r0 < 2 else "✗"
    ok_1100 = "✓" if 0.5 < r1100 < 2 else "✗"
    print(f"  {name:<40} z=0: {r0:>10.3e} {ok_0}  z=1100: {r1100:>10.3e} {ok_1100}")


def main():
    print("="*80)
    print("FORM H: Hill function G = (1+z)^n / (K + (1+z)^n)")
    print("="*80)
    for n in [1, 2, 3, 5, 8, 12]:
        for K in [1e3, 1e6, 1e9, 1e12]:
            p0, p11 = form_H(n, K)
            test_form(f"H: n={n}, K={K:.0e}", p0, p11)
    print()

    print("="*80)
    print("FORM I: Sigmoid G = 1/(1 + exp(-(z-z_0)/scale))")
    print("="*80)
    for z_0 in [500, 1000, 1100, 1200, 1500]:
        for scale in [10, 50, 100, 200]:
            p0, p11 = form_I(z_0, scale)
            test_form(f"I: z_0={z_0}, scale={scale}", p0, p11)
    print()

    print("="*80)
    print("FORM J: Gaussian G = exp(-(z-z_0)^2 / (2σ^2))")
    print("="*80)
    for z_0 in [1100, 1500, 2000]:
        for sigma in [50, 100, 200, 500]:
            p0, p11 = form_J(z_0, sigma)
            test_form(f"J: z_0={z_0}, σ={sigma}", p0, p11)
    print()

    print("="*80)
    print("FORM K: Power law with hard cutoff at z_cut")
    print("="*80)
    for n in [3, 5, 8, 12, 20]:
        for z_cut in [500, 1000, 1100, 1500]:
            p0, p11 = form_K(n, z_cut)
            test_form(f"K: n={n}, z_cut={z_cut}", p0, p11)
    print()

    print("="*80)
    print("LEGEND")
    print("="*80)
    print("  ✓ : predicted/observed ratio between 0.5 and 2 (good fit)")
    print("  ✗ : ratio outside 0.5-2 (bad fit)")


if __name__ == "__main__":
    main()
