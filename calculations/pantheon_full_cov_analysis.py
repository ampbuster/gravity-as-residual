#!/usr/bin/env python3
"""
Pantheon+ SNe analysis with FULL COVARIANCE MATRIX (rigorous)

Uses full Pantheon+ statistical+systematic covariance matrix
(1701x1701) to compute chi^2 with proper SNe correlations.

This is the rigorous version, replacing the simplified diagonal-errors
analysis in pantheon_analysis.py.
"""

import math
import sys
import time
import numpy as np
sys.path.insert(0, ".")
sys.path.insert(0, "calculations")

from cascade_model import Constants


def hr(ch="="):
    print()
    print(ch * 78)
    print(ch * 78)


def parse_pantheon(filename):
    """Parse Pantheon+ data file."""
    data = []
    with open(filename) as f:
        header = f.readline().split()
        for line in f:
            parts = line.split()
            if len(parts) < len(header):
                continue
            try:
                zCMB = float(parts[header.index("zCMB")])
                mb = float(parts[header.index("m_b_corr")])
                if zCMB > 0 and mb > 0:
                    data.append({"zCMB": zCMB, "m_b_corr": mb})
            except (ValueError, IndexError, KeyError):
                continue
    return data


def load_covariance(filename):
    """Load full Pantheon+ covariance matrix."""
    print(f"  Loading {filename}...")
    t0 = time.time()
    with open(filename) as f:
        n = int(f.readline().strip())
        # Read as flat array, then reshape
        data = np.loadtxt(f)
    cov = data.reshape((n, n))
    t1 = time.time()
    print(f"  Loaded {n}x{n} matrix in {t1-t0:.1f}s")
    return cov


# Pre-compute E(z) for fast integration
Omega_m_default = 0.315
Omega_L_default = 1 - Omega_m_default
c_kms = 299792.458

_z_grid = np.linspace(0, 2.5, 5000)
_E_grid = np.sqrt(Omega_m_default * (1 + _z_grid)**3 + Omega_L_default)


def d_L_fast(z, H_0, Omega_m=0.315):
    """Fast d_L using pre-computed E(z) grid."""
    if z <= 0:
        return 0
    if z > _z_grid[-1]:
        z = _z_grid[-1]
    n_steps = 50
    dz = z / n_steps
    integral = 0
    for j in range(n_steps):
        zp = (j + 0.5) * dz
        if Omega_m != Omega_m_default:
            E = np.sqrt(Omega_m * (1 + zp)**3 + (1 - Omega_m))
        else:
            E = np.interp(zp, _z_grid, _E_grid)
        integral += dz / E
    return (1 + z) * (c_kms / H_0) * integral


def MU_pred(z, H_0, Omega_m=0.315):
    """Predicted distance modulus."""
    dL = d_L_fast(z, H_0, Omega_m)
    return 5 * math.log10(dL / 1e-5)


def MU_pred_arr(z_arr, H_0_arr, Omega_m=0.315):
    """Vectorized MU prediction."""
    MU_ps = np.zeros_like(z_arr)
    for i, (z, H0) in enumerate(zip(z_arr, H_0_arr)):
        MU_ps[i] = MU_pred(z, H0, Omega_m)
    return MU_ps


def H_0_cascade(z, H_0_local=73.04, H_0_CMB=67.4, q=2/3):
    """Cascade H_0(z) prediction."""
    f_z = 1 / (1 + z) ** q
    H_0_sq = H_0_CMB**2 + (H_0_local**2 - H_0_CMB**2) * f_z
    return math.sqrt(H_0_sq)


def H_0_cascade_arr(z_arr, H_0_local=73.04, H_0_CMB=67.4, q=2/3):
    """Vectorized cascade H_0(z)."""
    f_z = 1 / (1 + z_arr) ** q
    H_0_sq = H_0_CMB**2 + (H_0_local**2 - H_0_CMB**2) * f_z
    return np.sqrt(H_0_sq)


def fit_M_with_cov(mb_arr, MU_arr, cov):
    """Fit M analytically (marginalized) with full covariance."""
    cov_inv = np.linalg.inv(cov)
    delta = mb_arr - MU_arr
    ones = np.ones_like(delta)
    M = (ones @ cov_inv @ delta) / (ones @ cov_inv @ ones)
    return M


def chi2_with_cov(residuals, cov):
    """Compute chi^2 = r^T C^-1 r with full covariance."""
    cov_inv = np.linalg.inv(cov)
    return residuals @ cov_inv @ residuals


def main():
    hr()
    print("PANTHEON+ ANALYSIS: CASCADE H_0(z) vs LCDM (FULL COVARIANCE)")
    hr()

    print(f"\n  Step 1: Load data and full covariance matrix")
    print(f"  ----------------------------------------------------------------")
    data = parse_pantheon("supporting/data/PantheonSH0ES.dat")
    print(f"  Loaded {len(data)} SNe")
    
    cov = load_covariance("supporting/data/PantheonSH0ES_STAT+SYS.cov")
    print(f"  Covariance shape: {cov.shape}")
    print(f"  Covariance is symmetric: {np.allclose(cov, cov.T)}")
    print(f"  Min eigenvalue: {np.linalg.eigvalsh(cov).min():.3e} (should be > 0)")
    
    z_arr = np.array([d["zCMB"] for d in data])
    mb_arr = np.array([d["m_b_corr"] for d in data])
    
    print(f"\n\n  Step 2: Compute MU predictions (vectorized, fast)")
    print(f"  ----------------------------------------------------------------")
    
    # LCDM with H_0 = 67.4
    t0 = time.time()
    MU_67 = MU_pred_arr(z_arr, np.full_like(z_arr, 67.4))
    print(f"  LCDM (H_0=67.4) MU: {time.time()-t0:.1f}s")
    
    # LCDM with H_0 = 73.04
    t0 = time.time()
    MU_73 = MU_pred_arr(z_arr, np.full_like(z_arr, 73.04))
    print(f"  LCDM (H_0=73.04) MU: {time.time()-t0:.1f}s")
    
    # Cascade (H_0 varies with z)
    t0 = time.time()
    H0_cas_arr = H_0_cascade_arr(z_arr)
    MU_cas = MU_pred_arr(z_arr, H0_cas_arr)
    print(f"  Cascade MU: {time.time()-t0:.1f}s")
    
    print(f"\n\n  Step 3: Compute chi^2 with FULL COVARIANCE (M marginalized)")
    print(f"  ----------------------------------------------------------------")
    
    # LCDM with H_0 = 67.4
    M_67 = fit_M_with_cov(mb_arr, MU_67, cov)
    r_67 = mb_arr - M_67 - MU_67
    chi2_67 = chi2_with_cov(r_67, cov)
    print(f"  LCDM (H_0=67.4): M = {M_67:.3f}, chi^2 = {chi2_67:.1f}, reduced = {chi2_67/len(data):.2f}")
    
    # LCDM with H_0 = 73.04
    M_73 = fit_M_with_cov(mb_arr, MU_73, cov)
    r_73 = mb_arr - M_73 - MU_73
    chi2_73 = chi2_with_cov(r_73, cov)
    print(f"  LCDM (H_0=73.04): M = {M_73:.3f}, chi^2 = {chi2_73:.1f}, reduced = {chi2_73/len(data):.2f}")
    
    # Cascade
    M_cas = fit_M_with_cov(mb_arr, MU_cas, cov)
    r_cas = mb_arr - M_cas - MU_cas
    chi2_cas = chi2_with_cov(r_cas, cov)
    print(f"  Cascade (H_0(z)): M = {M_cas:.3f}, chi^2 = {chi2_cas:.1f}, reduced = {chi2_cas/len(data):.2f}")
    
    print(f"\n  LCDM (H_0=67.4): chi2 = {chi2_67:.1f}")
    print(f"  LCDM (H_0=73.04): chi2 = {chi2_73:.1f}")
    print(f"  Cascade: chi2 = {chi2_cas:.1f}")
    
    print(f"\n\n  Step 4: Best-fit H_0 in LCDM (M free)")
    print(f"  ----------------------------------------------------------------")
    H_0_grid = np.linspace(60, 80, 100)
    chi2_grid = []
    for H0 in H_0_grid:
        MU_p = MU_pred_arr(z_arr, np.full_like(z_arr, H0))
        M = fit_M_with_cov(mb_arr, MU_p, cov)
        r = mb_arr - M - MU_p
        chi2 = chi2_with_cov(r, cov)
        chi2_grid.append(chi2)
    chi2_grid = np.array(chi2_grid)
    best_idx = np.argmin(chi2_grid)
    best_H0_LCDM = H_0_grid[best_idx]
    best_chi2_LCDM = chi2_grid[best_idx]
    print(f"  Best-fit LCDM: H_0 = {best_H0_LCDM:.2f}, chi^2 = {best_chi2_LCDM:.1f}")
    
    # Compare
    print()
    delta_chi2 = chi2_cas - best_chi2_LCDM
    print(f"  Delta chi^2 (cascade - best LCDM) = {delta_chi2:.1f}")
    if delta_chi2 < 0:
        print(f"  CASCADE WINS by {-delta_chi2:.1f}")
    else:
        print(f"  LCDM WINS by {delta_chi2:.1f}")
    
    if abs(delta_chi2) > 25:
        sig = "~5 sigma"
    elif abs(delta_chi2) > 9:
        sig = "~3 sigma"
    elif abs(delta_chi2) > 4:
        sig = "~2 sigma"
    else:
        sig = "not significant"
    print(f"  Significance: {sig}")
    
    print(f"\n\n  Step 5: H_0 at z=1 specifically (cascade's key prediction)")
    print(f"  ----------------------------------------------------------------")
    mask_z1 = (z_arr >= 0.8) & (z_arr <= 1.2)
    z_z1 = z_arr[mask_z1]
    mb_z1 = mb_arr[mask_z1]
    cov_z1 = cov[np.ix_(mask_z1, mask_z1)]
    
    print(f"  SNe at z ~ 1: {mask_z1.sum()}")
    
    chi2_z1_grid = []
    for H0 in H_0_grid:
        MU_p = MU_pred_arr(z_z1, np.full_like(z_z1, H0))
        M = fit_M_with_cov(mb_z1, MU_p, cov_z1)
        r = mb_z1 - M - MU_p
        chi2 = chi2_with_cov(r, cov_z1)
        chi2_z1_grid.append(chi2)
    chi2_z1_grid = np.array(chi2_z1_grid)
    best_H0_z1 = H_0_grid[np.argmin(chi2_z1_grid)]
    H0_cascade_z1 = H_0_cascade(1.0)
    print(f"  Best-fit H_0 at z~1: {best_H0_z1:.2f}")
    print(f"  Cascade prediction at z=1: {H0_cascade_z1:.2f}")
    print(f"  LCDM constant: 67.4 (Planck)")
    print()
    d_lcdm = abs(best_H0_z1 - 67.4)
    d_cas = abs(best_H0_z1 - H0_cascade_z1)
    print(f"  Distance from LCDM: {d_lcdm:.2f}")
    print(f"  Distance from cascade: {d_cas:.2f}")
    if d_cas < d_lcdm:
        print(f"  CASCADE PREDICTION IS CLOSER TO DATA (by {d_lcdm - d_cas:.2f})")
    else:
        print(f"  LCDM PREDICTION IS CLOSER TO DATA (by {d_cas - d_lcdm:.2f})")
    
    print(f"\n\n  Step 6: H_0 vs z trend with full covariance")
    print(f"  ----------------------------------------------------------------")
    z_bins = [(0.01, 0.1), (0.1, 0.2), (0.2, 0.3), (0.3, 0.5), (0.5, 0.7), (0.7, 1.0), (1.0, 1.5)]
    bin_results = []
    for z_lo, z_hi in z_bins:
        mask = (z_arr >= z_lo) & (z_arr < z_hi)
        if mask.sum() < 10:
            continue
        z_sub = z_arr[mask]
        mb_sub = mb_arr[mask]
        cov_sub = cov[np.ix_(mask, mask)]
        
        chi2_sub = []
        for H0 in H_0_grid:
            MU_p = MU_pred_arr(z_sub, np.full_like(z_sub, H0))
            M = fit_M_with_cov(mb_sub, MU_p, cov_sub)
            r = mb_sub - M - MU_p
            chi2 = chi2_with_cov(r, cov_sub)
            chi2_sub.append(chi2)
        chi2_sub = np.array(chi2_sub)
        H0_fit = H_0_grid[np.argmin(chi2_sub)]
        H0_cas_bin = H_0_cascade((z_lo + z_hi) / 2)
        delta = H0_fit - H0_cas_bin
        print(f"  z={z_lo:.2f}-{z_hi:.2f} (N={mask.sum()}): H_0 fit = {H0_fit:.2f}, H_0 cas = {H0_cas_bin:.2f}, delta = {delta:+.2f}")
        bin_results.append(((z_lo + z_hi) / 2, H0_fit, H0_cas_bin))
    
    if len(bin_results) >= 2:
        z_mids = np.array([r[0] for r in bin_results])
        H0_fits = np.array([r[1] for r in bin_results])
        slope = np.polyfit(z_mids, H0_fits, 1)[0]
        print(f"\n  Linear fit: H_0(z) slope = {slope:.2f}")
        if slope < -1:
            print(f"  H_0 DECREASES with z (CONSISTENT with cascade)")
        elif slope < 0:
            print(f"  Slight negative trend (weak support for cascade)")
        else:
            print(f"  H_0 does NOT decrease with z (NOT consistent with cascade)")

    # Final summary
    hr()
    print("SUMMARY (with FULL COVARIANCE)")
    hr()
    print(f"\n  Pantheon+ analysis ({len(data)} SNe, FULL covariance):")
    print(f"    Best-fit LCDM: H_0 = {best_H0_LCDM:.2f}, chi^2 = {best_chi2_LCDM:.1f}")
    print(f"    Cascade: chi^2 = {chi2_cas:.1f}")
    print(f"    Delta chi^2 = {delta_chi2:.1f}")
    print()
    if delta_chi2 < -25:
        print(f"  CASCADE FITS SIGNIFICANTLY BETTER (~5 sigma)")
    elif delta_chi2 < -9:
        print(f"  CASCADE FITS BETTER (~3 sigma)")
    elif delta_chi2 < 0:
        print(f"  Cascade slightly better (not significant)")
    else:
        print(f"  LCDM FITS BETTER (cascade is NOT supported)")
    print()
    if len(bin_results) >= 2:
        print(f"  H_0 vs z trend: slope = {slope:.2f}")
    print()
    print(f"  This is the rigorous version with full covariance.")
    print(f"  Compare to simplified version (commit 79):")
    print(f"    - Simplified: LCDM 733, Cascade 759 (delta 26)")
    print(f"    - Full cov:   LCDM {best_chi2_LCDM:.0f}, Cascade {chi2_cas:.0f} (delta {delta_chi2:.0f})")
    print()
    print(f"  The full covariance includes SNe correlations and systematics.")
    print(f"  This is the appropriate way to test cosmological models.")


if __name__ == "__main__":
    main()
