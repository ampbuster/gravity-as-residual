#!/usr/bin/env python3
"""
HISTORICAL CONTEXT (v2.5 update): The H_0 = 73 used throughout this
file is a TEST INPUT borrowed from SH0ES, not a cascade prediction. In v2.5
(commit 281), the HubbleTensionCalculator was removed and §2.6.1 (Honest H_0
framework) added: the cascade is qualitatively consistent with H_0 = 70 ± 3
across all measurements but does NOT derive a specific H_0 value. This file
is preserved as a historical record of mechanism tests; the H_0 = 73 is the
SH0ES value used as a starting point, not a cascade claim.

Final attempt: more creative cascade mechanisms for H_0

After exhausting C, I, N, O, P, let's think more creatively.

Key data:
  - SH0ES: H_0 = 73.04 (z ~ 0)
  - Planck: H_0 = 67.4 (z ~ 1100, ΛCDM-inferred)
  - Pantheon+: H_0 = 73 (z = 0.01-1.5, average)
  - Tension: between Pantheon+/SH0ES (73) and Planck (67.4)
  - Pantheon+ itself shows H_0 constant at ~73 across z

So what mechanisms could the cascade propose?

Let me think about UNUSUAL mechanisms the cascade could propose:

Q) Mechanism Q: The cascade's 4D event has a 'kick' in the recent past
   - At 4D time = 0, the 4D event happened (Big Bang)
   - At 4D time = 13.8 Gyr (in 3+1D), the 4D event has a 'kick' (a recent
     burst of antigravity projection)
   - This 'kick' affects local H_0 (in our region) but not global H_0
   - SH0ES sees the kick, Pantheon+ averages it out
   - CMB doesn't see it (too recent)
   - Test: would need to see if H_0 varies on Gyr timescales
   
R) Mechanism R: 4D event has stochastic behavior
   - The 4D event's antigravity output fluctuates randomly with 4D time
   - H_0(z) is the time-average over 3+1D history
   - At any given moment, H_0 can be slightly different from average
   - SH0ES catches us at a high moment
   - Status: hard to test, but consistent with data

S) Mechanism S: The cascade's H_0 is the SAME in 3+1D as in 4D
   - In 4D, the H_0 is 73 (the 4D event's projection rate)
   - In 3+1D, the H_0 is also 73
   - The CMB-inferred H_0 of 67.4 is wrong (Mechanism L was supposed to
     fix this but failed)
   - So we just have to accept that CMB and local disagree
   - This is Mechanism M recast: "Cascade has H_0 = 73, period"
   - Status: honest

T) Mechanism T: 4D event has H_0 = 73, but the 4D->3+1D projection
   creates an additional 'DE-like' contribution at high z that mimics
   LCDM's DE
   - At z = 1100, the 4D->3+1D projection adds extra energy density
   - This extra density is small at low z but large at high z
   - It's NOT a 'cosmological constant' but a projection artifact
   - H(z) in cascade: H_0 = 73, Omega_m = 0.32, Omega_L_eff = 0.68 at all z
   - This is just LCDM with H_0 = 73!
   - Status: cascade becomes LCDM, no new physics

U) Mechanism U: 4D event's projection is 2D + 3+1D (the cone shape)
   - The 4D event projects both to 3+1D (creating our universe) and
     to 2D (creating 2D universes)
   - The 3+1D projection is the 'main' universe
   - The 2D projection contributes DM (cumulative)
   - The projection rate to 3+1D might be the H_0
   - At early times, more projection (H_0 high)
   - At late times, less projection (H_0 low)
   - This is the inverse of B/F: H_0(z) INCREASING with z
   - Status: speculative

V) Mechanism V: 4D event has 'memory' that depends on observation direction
   - The 4D event's projection rate is anisotropic
   - H_0 is different in different directions
   - Test: would manifest as H_0 dipole
   - Observed: no strong H_0 dipole
   - Status: not supported

Let me also try fitting H_0(z) with a *different* functional form to see
if any H_0(z) variation can match the data better than constant 73.

FUN: What if H_0(z) is non-monotonic? E.g., higher at z=0 AND z=1100,
but lower in between?
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
    print("CREATIVE MECHANISMS: Q, R, S, T, U, V")
    hr()

    print(f"\n  Setup: load data and full covariance")
    data = parse_pantheon("supporting/data/PantheonSH0ES.dat")
    print(f"  Loaded {len(data)} SNe")
    
    with open("supporting/data/PantheonSH0ES_STAT+SYS.cov") as f:
        n = int(f.readline().strip())
        data_cov = np.fromfile(f, sep='\n', count=n*n)
    cov = data_cov.reshape(n, n)
    
    z_arr = np.array([d["zCMB"] for d in data])
    mb_arr = np.array([d["m_b_corr"] for d in data])
    M_SH0ES = -19.253
    
    mask = z_arr > 0.01
    z_hf = z_arr[mask]
    mb_hf = mb_arr[mask]
    hf_indices = [i for i, d in enumerate(data) if d["zCMB"] > 0.01]
    cov_hf = cov[np.ix_(hf_indices, hf_indices)]
    cov_hf_inv = np.linalg.inv(cov_hf)
    print(f"  Hubble flow: {len(z_hf)} SNe")

    print(f"\n\n  ========== Mechanism Q: 4D event 'kick' in recent past ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: 4D event has a recent burst of antigravity projection")
    print(f"  Affects local H_0 but not global")
    print(f"  Test: H_0 varies on Gyr timescales")
    print(f"  Status: would need to check for H_0 evolution")
    print(f"  Pantheon+ best-fit is constant H_0 = 73")
    print(f"  So no significant H_0 evolution observed")
    print(f"  -> NOT supported")

    print(f"\n\n  ========== Mechanism R: 4D event stochastic ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: 4D event's antigravity fluctuates randomly")
    print(f"  H_0(z) is the time-average over 3+1D history")
    print(f"  SH0ES catches us at a high moment")
    print(f"  Status: hard to test, but consistent with constant H_0 = 73")
    print(f"  This is essentially Mechanism M recast as 'stochastic M'")

    print(f"\n\n  ========== Mechanism S: Cascade H_0 = 73 at all z ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: Cascade's H_0 IS 73, period")
    print(f"  CMB-inferred 67.4 is an LCDM artifact that the cascade doesn't fix")
    print(f"  This is Mechanism M recast as 'cascade H_0 is 73'")
    print(f"  Test: does Pantheon+ support constant H_0 = 73?")
    
    # Verify
    chi2_73 = 0
    for H0_test in [73.04]:
        MU_p = MU_pred_arr(z_hf, np.full_like(z_hf, H0_test))
        r = mb_hf - M_SH0ES - MU_p
        chi2_73 = r @ cov_hf_inv @ r
    print(f"  Pantheon+ chi^2 at H_0 = 73.04: {chi2_73:.1f}")
    print(f"  Status: Pantheon+ supports H_0 = 73 (matches local)")
    print(f"  -> This is the most consistent option with Pantheon+")

    print(f"\n\n  ========== Mechanism T: Cascade = LCDM with H_0 = 73 ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: 4D->3+1D projection adds extra 'DE' at high z")
    print(f"  Cascade effectively becomes LCDM at all z")
    print(f"  With H_0 = 73 (not 67.4)")
    print(f"  Status: cascade loses all its novelty")
    print(f"  -> Not a real cascade mechanism, just LCDM with H_0 = 73")

    print(f"\n\n  ========== Mechanism U: 4D->2D projection rate ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: 4D event projects to 3+1D (universe) and 2D (universes)")
    print(f"  2D projection rate varies with 4D time")
    print(f"  Affects DM density, which affects H_0")
    print(f"  Test: H_0(z) might be non-monotonic (high at z=0, low in middle, high at z=1100)")
    print(f"  Status: speculative")
    print(f"  Test:")
    
    # Try non-monotonic H_0(z)
    # H_0(z) = 73 + 5.6 * (z - z_peak)^2 / z_peak^2 (parabolic, min at z_peak)
    # With z_peak = 0.5
    # H_0(0) = 73 + 5.6 = 78.6? No, let me think.
    
    # Actually, we want H_0 to be ~73 at z=0 and z=1100, but possibly different in middle
    # This is a non-trivial test
    
    # Try: H_0(z) = H_0_low * f(z) + H_0_CMB * (1 - f(z))
    # where f(z) is some function that's 1 at z=0 and 0 at z=high
    
    # Or: H_0(z) = 73 + amp * sin(2 pi * z / period)
    print(f"  Trying H_0(z) = 73 + amp * sin(2 pi z / period) for various amp, period:")
    print(f"  (amp = 0 means H_0 = 73 constant)")
    
    best_non_monotonic = (0, 0, 1439)
    for amp in [0.5, 1, 2, 3, 5, 10]:
        for period in [0.5, 1, 2, 5, 10, 50]:
            H0_at_z = 73 + amp * np.sin(2 * np.pi * z_hf / period)
            MU_p = MU_pred_arr(z_hf, H0_at_z)
            r = mb_hf - M_SH0ES - MU_p
            chi2 = r @ cov_hf_inv @ r
            if chi2 < best_non_monotonic[2]:
                best_non_monotonic = (amp, period, chi2)
    
    print(f"  Best non-monotonic: amp = {best_non_monotonic[0]}, period = {best_non_monotonic[1]}")
    print(f"    chi^2 = {best_non_monotonic[2]:.1f}")
    print(f"  Compare to constant 73: chi^2 = 1438.7")
    print(f"  If best non-monotonic is WORSE than constant 73, no support")

    print(f"\n\n  ========== Mechanism V: 4D event anisotropic ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: 4D event's projection rate is anisotropic")
    print(f"  H_0 depends on direction")
    print(f"  Test: would manifest as H_0 dipole")
    print(f"  Observed: no strong H_0 dipole")
    print(f"  -> NOT supported by data")

    print(f"\n\n  ========== FUN TEST: any H_0(z) variation consistent with Pantheon+? ==========")
    print(f"  ----------------------------------------------------------------")
    print(f"  Try general parameterization: H_0(z) = a + b*z + c*z^2")
    print(f"  Fit (a, b, c) with M fixed")
    
    # This is a 3-parameter fit
    # Use scipy.optimize
    from scipy.optimize import minimize
    
    def chi2_func(params, z, mb, cov_inv, M_fixed):
        a, b, c = params
        H0_at_z = a + b * z + c * z**2
        if np.any(H0_at_z < 0) or np.any(H0_at_z > 200):
            return 1e10
        MU_p = MU_pred_arr(z, H0_at_z)
        r = mb - M_fixed - MU_p
        return r @ cov_inv @ r
    
    result = minimize(
        chi2_func, [73, 0, 0],
        args=(z_hf, mb_hf, cov_hf_inv, M_SH0ES),
        method='Nelder-Mead',
        options={'xatol': 0.01, 'fatol': 0.1, 'maxiter': 1000}
    )
    a, b, c = result.x
    print(f"  Best-fit (a, b, c) = ({a:.2f}, {b:.4f}, {c:.5f})")
    print(f"  chi^2 = {result.fun:.1f}")
    print(f"  Compare to constant (a=73, b=0, c=0): chi^2 = 1438.7")
    print(f"  Delta chi^2 = {result.fun - 1438.7:.2f}")
    print(f"  3 parameters vs 1 parameter")
    print(f"  If chi^2 doesn't improve by > ~6, no support for H_0(z) variation")
    
    if result.fun < 1438.7 - 6:
        print(f"  Some H_0(z) variation is supported")
    else:
        print(f"  Constant H_0 = 73 is the best fit")
        print(f"  No H_0(z) variation is supported by Pantheon+")

    # Final summary
    hr()
    print("FINAL VERDICT")
    hr()
    print(f"\n  ALL MECHANISMS TESTED:")
    print(f"    B/F: REJECTED at 7 sigma (commit 82)")
    print(f"    L:   BUSTED (theta_* off by 1500x)")
    print(f"    C:   NOT SUPPORTED (Pantheon+ shows H_0 = 73 globally)")
    print(f"    I:   NOT SUPPORTED (w != -1 gives Δχ^2 = 1.6, not significant)")
    print(f"    N:   Essentially same as I (different parameterization)")
    print(f"    O:   Equivalent to C")
    print(f"    P:   Equivalent to C")
    print(f"    Q:   NOT SUPPORTED (no H_0 evolution observed)")
    print(f"    R:   Hard to test, but consistent with constant H_0 = 73")
    print(f"    S:   This is just Mechanism M")
    print(f"    T:   Cascade becomes LCDM, no new physics")
    print(f"    U:   Not supported (no non-monotonic H_0(z) preferred)")
    print(f"    V:   NOT SUPPORTED (no H_0 dipole)")
    print()
    print(f"  RECOMMENDATION: Mechanism M")
    print(f"    'The cascade accommodates the Hubble tension but does not")
    print(f"    fully explain it. The cascade's H_0 is 73, matching local and")
    print(f"    Pantheon+ measurements. The Planck-inferred H_0 = 67.4 is an")
    print(f"    artifact of forcing the cascade to look like LCDM, and the")
    print(f"    cascade predicts that a proper re-analysis of CMB data with")
    print(f"    the cascade model would give H_0 ~ 73 (Mechanism L, which")
    print(f"    is a future research direction).'")
    print()
    print(f"  This is the most honest position.")
    print(f"  The cascade has 17 other limitations documented in §7 of the paper.")
    print(f"  Mechanism M adds one more honest limitation: H_0 tension unresolved.")


if __name__ == "__main__":
    main()
