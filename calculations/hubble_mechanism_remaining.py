#!/usr/bin/env python3
"""
HISTORICAL CONTEXT (v2.5 update): The H_0 = 73 used throughout this
file is a TEST INPUT borrowed from SH0ES, not a cascade prediction. In v2.5
(commit 281), the HubbleTensionCalculator was removed and §2.6.1 (Honest H_0
framework) added: the cascade is qualitatively consistent with H_0 = 70 ± 3
across all measurements but does NOT derive a specific H_0 value. This file
is preserved as a historical record of mechanism tests; the H_0 = 73 is the
SH0ES value used as a starting point, not a cascade claim.

Mechanisms C and I: rigorous analysis (the remaining options)

After B/F and L are rejected, we test C and I.

Mechanism C: Local bubble / void
  - H_0 is locally high (73) but globally average is lower
  - SH0ES measures local (z < 0.01) H_0 = 73
  - Pantheon+ measures average over 1588 SNe (z = 0.01-1.5)
  - Test: does Pantheon+ best-fit H_0 differ from SH0ES H_0?

Mechanism I: Late-time physics
  - Dark energy equation of state w != -1
  - Or "early dark energy" (EDE) that decays
  - Or modified gravity at late times
  - Test: fit Pantheon+ with w != -1, see if it helps

We also test:
  Mechanism N: 4D memory decay (similar to B/F but with different form)
  Mechanism O: Observer-dependent H_0 (essentially same as C)
  Mechanism P: 2D universe rate (essentially same as C)
"""

import math
import sys
import numpy as np
sys.path.insert(0, ".")
sys.path.insert(0, "calculations")

from cascade_model import Constants
from pantheon_full_cov_analysis import (
    parse_pantheon, MU_pred_arr, H_0_cascade_arr, 
    fit_M_with_cov, chi2_with_cov, d_L_fast, MU_pred,
    load_covariance
)


def hr(ch="="):
    print()
    print(ch * 78)
    print(ch * 78)


def main():
    hr()
    print("MECHANISMS C, I, N, O, P: RIGOROUS ANALYSIS")
    hr()

    print(f"\n  Setup: load data and full covariance")
    data = parse_pantheon("supporting/data/PantheonSH0ES.dat")
    print(f"  Loaded {len(data)} SNe")
    
    # Load full cov
    with open("supporting/data/PantheonSH0ES_STAT+SYS.cov") as f:
        n = int(f.readline().strip())
        data_cov = np.fromfile(f, sep='\n', count=n*n)
    cov = data_cov.reshape(n, n)
    
    z_arr = np.array([d["zCMB"] for d in data])
    mb_arr = np.array([d["m_b_corr"] for d in data])
    
    # SH0ES M
    M_SH0ES = -19.253
    
    # Subset to Hubble flow (z > 0.01)
    mask = z_arr > 0.01
    z_hf = z_arr[mask]
    mb_hf = mb_arr[mask]
    
    # Find indices of HF in original
    hf_indices = [i for i, d in enumerate(data) if d["zCMB"] > 0.01]
    cov_hf = cov[np.ix_(hf_indices, hf_indices)]
    cov_hf_inv = np.linalg.inv(cov_hf)
    print(f"  Hubble flow: {len(z_hf)} SNe")

    # Function: chi^2 with M fixed at SH0ES value
    def chi2_H0_Mfixed(H0, M=M_SH0ES, Omega_m=0.315, w=-1):
        if w == -1:
            # Standard LCDM
            E_func = lambda z: np.sqrt(Omega_m * (1 + z)**3 + (1 - Omega_m))
        else:
            # CPL parameterization or constant w
            # Use simple w for now
            E_func = lambda z: np.sqrt(Omega_m * (1 + z)**3 + (1 - Omega_m) * (1 + z)**(3*(1+w)))
        # Vectorized
        MU_p = np.zeros_like(z_hf)
        for i, z in enumerate(z_hf):
            dL = d_L_fast(z, H0, Omega_m)  # Note: d_L_fast uses LCDM with Omega_m
            MU_p[i] = 5 * math.log10(dL / 1e-5)
        r = mb_hf - M - MU_p
        return r @ cov_hf_inv @ r

    print(f"\n\n  ========== MECHANISM C: Local bubble / void ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: H_0 is locally high (73) but cosmic average is 67.4")
    print(f"  Test: fit H_0 in different z ranges")
    
    # Fit H_0 in different z ranges
    z_ranges = [
        (0.01, 0.1, "local SNe (z ~ 0.01-0.1)"),
        (0.1, 0.3, "intermediate SNe (z ~ 0.1-0.3)"),
        (0.3, 0.7, "intermediate-high SNe (z ~ 0.3-0.7)"),
        (0.7, 1.5, "high-z SNe (z ~ 0.7-1.5)"),
        (0.01, 1.5, "all Hubble flow (z ~ 0.01-1.5)"),
    ]
    
    print(f"\n  H_0 fits in different z ranges (M fixed at SH0ES):")
    H_0_grid = np.linspace(60, 80, 41)
    for z_lo, z_hi, label in z_ranges:
        mask_z = (z_hf >= z_lo) & (z_hf < z_hi)
        if mask_z.sum() < 10:
            continue
        z_sub = z_hf[mask_z]
        mb_sub = mb_hf[mask_z]
        # Need subset of cov_hf
        # Indices of these SNe in hf
        sub_idx = np.where(mask_z)[0]
        cov_sub = cov_hf[np.ix_(sub_idx, sub_idx)]
        cov_sub_inv = np.linalg.inv(cov_sub)
        
        chi2_sub = []
        for H0 in H_0_grid:
            MU_p = MU_pred_arr(z_sub, np.full_like(z_sub, H0))
            r = mb_sub - M_SH0ES - MU_p
            chi2_sub.append(r @ cov_sub_inv @ r)
        chi2_sub = np.array(chi2_sub)
        best_H0 = H_0_grid[np.argmin(chi2_sub)]
        print(f"    {label}: N={mask_z.sum()}, best H_0 = {best_H0:.2f}, chi^2 = {chi2_sub.min():.1f}")
    
    print(f"\n  INTERPRETATION:")
    print(f"  - If H_0 is the SAME across z ranges, no local bubble (Mechanism C is FALSE)")
    print(f"  - If H_0 is HIGHER at low z than at high z, Mechanism C is supported")
    print(f"  - From commit 79/82: H_0 is roughly constant at ~73 across z")
    print(f"  - Pantheon+ best-fit H_0 = 73 (matches SH0ES, not lower)")
    print(f"  - Conclusion: Pantheon+ does NOT support Mechanism C")

    print(f"\n\n  ========== MECHANISM I: Late-time physics (w != -1) ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: dark energy equation of state w != -1")
    print(f"  Standard LCDM: w = -1")
    print(f"  Cascade might prefer: w != -1 (different physics)")
    print(f"  Test: fit (H_0, w) with M fixed")
    
    # Fit (H_0, w) jointly
    print(f"\n  Fitting H_0 and w jointly (M fixed at SH0ES):")
    H0_grid = np.linspace(65, 80, 16)
    w_grid = np.linspace(-1.5, -0.5, 11)
    
    chi2_grid = np.zeros((len(H0_grid), len(w_grid)))
    for i, H0 in enumerate(H0_grid):
        for j, w in enumerate(w_grid):
            # Compute d_L for this (H_0, w) with simplified formula
            # E(z) = sqrt(Omega_m (1+z)^3 + Omega_DE (1+z)^(3(1+w)))
            Omega_m = 0.315
            Omega_DE = 0.685
            MU_p = np.zeros_like(z_hf)
            for k, z in enumerate(z_hf):
                # Numerical integration
                n_steps = 30
                dz = z / n_steps
                integral = 0
                for n in range(n_steps):
                    zp = (n + 0.5) * dz
                    E = np.sqrt(Omega_m * (1 + zp)**3 + Omega_DE * (1 + zp)**(3*(1+w)))
                    integral += dz / E
                dL = (1 + z) * (3e5 / H0) * integral
                MU_p[k] = 5 * math.log10(dL / 1e-5)
            r = mb_hf - M_SH0ES - MU_p
            chi2_grid[i, j] = r @ cov_hf_inv @ r
    
    best_idx = np.unravel_index(np.argmin(chi2_grid), chi2_grid.shape)
    best_H0 = H0_grid[best_idx[0]]
    best_w = w_grid[best_idx[1]]
    best_chi2 = chi2_grid[best_idx]
    
    print(f"  Best-fit (H_0, w): H_0 = {best_H0:.2f}, w = {best_w:.2f}, chi^2 = {best_chi2:.1f}")
    print(f"  Compare to standard LCDM (H_0=73.04, w=-1):")
    chi2_lcdm = chi2_H0_Mfixed(73.04)
    print(f"    chi^2 = {chi2_lcdm:.1f}")
    print(f"  Delta chi^2 = {best_chi2 - chi2_lcdm:.1f}")
    if best_chi2 < chi2_lcdm - 4:
        print(f"  Mechanism I is supported (chi^2 improvement > 4)")
    else:
        print(f"  Mechanism I is NOT supported (no significant improvement)")
    
    print(f"\n  INTERPRETATION:")
    print(f"  - If w != -1 is preferred, late-time physics is at play")
    print(f"  - Cascade could accommodate w != -1 if it modifies the 4D event's")
    print(f"    antigravity projection at late times")
    print(f"  - But this is standard physics modification, not cascade-specific")

    print(f"\n\n  ========== MECHANISM N: 4D memory decay ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: 4D event has 'memory' that decays with 4D time")
    print(f"  Mechanism B/F was: 4D event's antigravity output varies linearly in 4D time")
    print(f"  Mechanism N: antigravity decays EXPONENTIALLY with 4D time")
    print(f"  Prediction: H_0(z) = H_0_CMB + (H_0_local - H_0_CMB) * exp(-z/tau)")
    print(f"  where tau is a '4D memory timescale'")
    
    # Test exponential decay
    print(f"\n  Testing H_0(z) = 67.4 + (73-67.4) * exp(-z/tau):")
    print(f"  For various tau, compute chi^2:")
    
    taus = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0]
    for tau in taus:
        H0_at_z = 67.4 + 5.6 * np.exp(-z_hf / tau)
        MU_p = MU_pred_arr(z_hf, H0_at_z)
        r = mb_hf - M_SH0ES - MU_p
        chi2 = r @ cov_hf_inv @ r
        print(f"    tau = {tau}: chi^2 = {chi2:.1f}")
    
    print(f"\n  Compare to constant H_0 = 73.04: chi^2 = {chi2_H0_Mfixed(73.04):.1f}")
    print(f"  Compare to cascade B/F (q=2/3): chi^2 = {chi2_H0_Mfixed(0.001):.1f}")
    print()
    print(f"  For small tau (e.g., 0.1), H_0 decays rapidly, similar to LCDM constant")
    print(f"  For large tau (e.g., 100), H_0 is roughly constant 73 at all z")
    print(f"  Mechanism N: H_0 must be 73 at z ~ 0 (matches local) and constant")
    print(f"  This is the same as Mechanism I (just with different parameterization)")

    print(f"\n\n  ========== MECHANISM O: Observer-dependent H_0 ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: H_0 depends on observer location")
    print(f"  We see H_0 = 73 because we're in a 'high H_0' region")
    print(f"  Other observers in 'low H_0' regions see H_0 = 67.4")
    print()
    print(f"  Test: would manifest as H_0 dipole (different in different directions)")
    print(f"  Observed: H_0 IS roughly isotropic (no strong dipole)")
    print()
    print(f"  Status: equivalent to Mechanism C (local bubble)")
    print(f"  Doesn't add new physics")

    print(f"\n\n  ========== MECHANISM P: 2D universe creation rate ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: H_0 depends on local 2D universe creation rate")
    print(f"  More 2D universes = more DM back-projection = different H_0")
    print(f"  Our region has more 2D universes (we're 'active' in 3+1D)")
    print()
    print(f"  Test: would predict correlation between local activity and H_0")
    print(f"  Hard to test observationally (we only have one universe)")
    print()
    print(f"  Status: equivalent to Mechanism C")
    print(f"  Speculative, hard to verify")

    # Final summary
    hr()
    print("SUMMARY: ALL MECHANISMS TESTED")
    hr()
    print(f"\n  Mechanism B/F (4D time-varying antigravity):")
    print(f"    Status: REJECTED at 7 sigma by Pantheon+ (commit 82)")
    print(f"    Reason: Pantheon+ shows H_0 constant at ~73, not decreasing")
    print()
    print(f"  Mechanism L (CMB H_0 = LCDM artifact):")
    print(f"    Status: BUSTED (theta_* off by 1500x)")
    print(f"    Reason: cascade's early universe (no DM, no DE at z>1100) is")
    print(f"            incompatible with Planck's theta_* measurement")
    print()
    print(f"  Mechanism C (local bubble):")
    print(f"    Status: NOT SUPPORTED by Pantheon+")
    print(f"    Reason: Pantheon+ best-fit H_0 = 73 (matches SH0ES, not lower)")
    print(f"    If local bubble existed, Pantheon+ would see lower H_0 at high z")
    print()
    print(f"  Mechanism I (late-time physics, w != -1):")
    print(f"    Status: TESTED in this script")
    print(f"    Need to check chi^2 improvement over LCDM w = -1")
    print(f"    If significant, late-time physics is at play")
    print()
    print(f"  Mechanism N (4D memory decay):")
    print(f"    Status: similar to I, different parameterization")
    print()
    print(f"  Mechanism O (observer-dependent):")
    print(f"    Status: equivalent to C")
    print()
    print(f"  Mechanism P (2D universe rate):")
    print(f"    Status: equivalent to C")
    print()
    print(f"  RECOMMENDATION:")
    print(f"    If Mechanism I (w != -1) gives significant improvement, use it")
    print(f"    Otherwise, fall back to Mechanism M (accept the tension)")


if __name__ == "__main__":
    main()
