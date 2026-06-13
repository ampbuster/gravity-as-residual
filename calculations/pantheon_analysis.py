#!/usr/bin/env python3
"""
Pantheon+ SNe analysis: cascade H_0(z) vs LCDM (vectorized, fast)

Uses Pantheon+ data to test cascade's H_0(z) prediction.
M is a free parameter (per cosmology fit), H_0 is fit in z bins.
"""

import math
import sys
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
        try:
            idx_zCMB = header.index("zCMB")
            idx_zCMBERR = header.index("zCMBERR")
            idx_mb = header.index("m_b_corr")
            idx_mb_err = header.index("m_b_corr_err_DIAG")
        except ValueError as e:
            print(f"Column not found: {e}")
            return []
        for line in f:
            parts = line.split()
            if len(parts) < len(header):
                continue
            try:
                zCMB = float(parts[idx_zCMB])
                mb = float(parts[idx_mb])
                mb_err = float(parts[idx_mb_err])
                if zCMB > 0 and mb > 0 and mb_err > 0:
                    data.append({
                        "zCMB": zCMB,
                        "m_b_corr": mb,
                        "m_b_corr_err": mb_err,
                    })
            except (ValueError, IndexError):
                continue
    return data


def MU_pred(z, H_0, Omega_m=0.315):
    """Predicted distance modulus (vectorized for arrays)."""
    c_kms = 299792.458
    if isinstance(z, np.ndarray):
        MU_ps = np.zeros_like(z)
        for i, zi in enumerate(z):
            if zi <= 0:
                MU_ps[i] = 0
                continue
            n_steps = 50
            dz = zi / n_steps
            integral = 0
            for j in range(n_steps):
                zp = (j + 0.5) * dz
                E = math.sqrt(Omega_m * (1 + zp)**3 + (1 - Omega_m))
                integral += dz / E
            dL = (1 + zi) * (c_kms / H_0) * integral
            MU_ps[i] = 5 * math.log10(dL / 1e-5)
        return MU_ps
    else:
        if z <= 0:
            return 0
        n_steps = 50
        dz = z / n_steps
        integral = 0
        for j in range(n_steps):
            zp = (j + 0.5) * dz
            E = math.sqrt(Omega_m * (1 + zp)**3 + (1 - Omega_m))
            integral += dz / E
        dL = (1 + z) * (c_kms / H_0) * integral
        return 5 * math.log10(dL / 1e-5)


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


def compute_chi2_M(z_arr, mb_arr, err_arr, MU_pred_arr):
    """Compute chi^2 with M analytically marginalized."""
    sig2 = err_arr**2
    M_num = np.sum((mb_arr - MU_pred_arr) / sig2)
    M_den = np.sum(1 / sig2)
    M = M_num / M_den
    chi2 = np.sum(((mb_arr - M - MU_pred_arr) / err_arr)**2)
    return M, chi2


def main():
    hr()
    print("PANTHEON+ ANALYSIS: CASCADE H_0(z) vs LCDM")
    hr()

    print(f"\n  Step 1: Load Pantheon+ data")
    print(f"  ----------------------------------------------------------------")
    filename = "supporting/data/PantheonSH0ES.dat"
    data = parse_pantheon(filename)
    print(f"  Loaded {len(data)} SNe")
    
    # Convert to arrays (use Hubble flow, z > 0.01)
    hubble_flow = [d for d in data if d["zCMB"] > 0.01]
    z_arr = np.array([d["zCMB"] for d in hubble_flow])
    mb_arr = np.array([d["m_b_corr"] for d in hubble_flow])
    err_arr = np.array([d["m_b_corr_err"] for d in hubble_flow])
    print(f"  Hubble flow SNe (z > 0.01): {len(hubble_flow)}")
    print(f"  z range: {z_arr.min():.4f} to {z_arr.max():.4f}")

    print(f"\n  Step 2: Fit H_0 and M jointly")
    print(f"  ----------------------------------------------------------------")
    Omega_m = 0.315
    
    # LCDM with various H_0 values
    print(f"  LCDM fits (M free, H_0 fixed):")
    for H0_test in [67.4, 70.0, 73.04, 75.0]:
        MU_p = np.array([MU_pred(z, H0_test) for z in z_arr])
        M, chi2 = compute_chi2_M(z_arr, mb_arr, err_arr, MU_p)
        print(f"    H_0 = {H0_test:.2f}: M = {M:.3f}, chi2 = {chi2:.0f}, reduced = {chi2/len(z_arr):.3f}")
    
    # Best-fit LCDM
    H0_grid = np.linspace(60, 80, 200)
    chi2_grid = []
    M_grid = []
    for H0 in H0_grid:
        MU_p = np.array([MU_pred(z, H0) for z in z_arr])
        M, chi2 = compute_chi2_M(z_arr, mb_arr, err_arr, MU_p)
        chi2_grid.append(chi2)
        M_grid.append(M)
    chi2_grid = np.array(chi2_grid)
    M_grid = np.array(M_grid)
    best_idx = np.argmin(chi2_grid)
    best_H0_LCDM = H0_grid[best_idx]
    best_M_LCDM = M_grid[best_idx]
    best_chi2_LCDM = chi2_grid[best_idx]
    print(f"\n  Best-fit LCDM: H_0 = {best_H0_LCDM:.2f}, M = {best_M_LCDM:.3f}, chi2 = {best_chi2_LCDM:.0f}")
    
    # Cascade fit (M free, H_0(z) from cascade)
    H0_cas_arr = H_0_cascade_arr(z_arr)
    MU_p_cas = np.array([MU_pred(z, H0_cas_arr[i]) for i, z in enumerate(z_arr)])
    M_cas, chi2_cas = compute_chi2_M(z_arr, mb_arr, err_arr, MU_p_cas)
    print(f"\n  Cascade fit: M = {M_cas:.3f}, chi2 = {chi2_cas:.0f}, reduced = {chi2_cas/len(z_arr):.3f}")
    
    print(f"\n\n  Step 3: Comparison")
    print(f"  ----------------------------------------------------------------")
    print(f"  Best-fit LCDM: chi2 = {best_chi2_LCDM:.0f}")
    print(f"  Cascade:       chi2 = {chi2_cas:.0f}")
    delta_chi2 = chi2_cas - best_chi2_LCDM
    if delta_chi2 < 0:
        print(f"  CASCADE WINS by {-delta_chi2:.0f}")
    else:
        print(f"  LCDM WINS by {delta_chi2:.0f}")
    
    if delta_chi2 < -25:
        print(f"  (>5 sigma)")
    elif delta_chi2 < -9:
        print(f"  (>3 sigma)")
    elif delta_chi2 < 0:
        print(f"  (not significant)")
    else:
        print(f"  (LCDM is better)")

    print(f"\n\n  Step 4: H_0 vs z trend")
    print(f"  ----------------------------------------------------------------")
    z_bins = [(0.01, 0.1), (0.1, 0.2), (0.2, 0.3), (0.3, 0.5), (0.5, 0.7), (0.7, 1.0), (1.0, 1.5)]
    print(f"  {'z range':>15} | {'N':>5} | {'H_0 fit':>10} | {'H_0 cas':>10} | {'delta':>8}")
    bin_results = []
    for z_lo, z_hi in z_bins:
        mask = (z_arr >= z_lo) & (z_arr < z_hi)
        if mask.sum() < 5:
            continue
        z_sub = z_arr[mask]
        mb_sub = mb_arr[mask]
        err_sub = err_arr[mask]
        # Best-fit H_0 in this bin
        chi2_sub = []
        for H0 in H0_grid:
            MU_p = np.array([MU_pred(z, H0) for z in z_sub])
            _, c2 = compute_chi2_M(z_sub, mb_sub, err_sub, MU_p)
            chi2_sub.append(c2)
        chi2_sub = np.array(chi2_sub)
        H0_fit = H0_grid[np.argmin(chi2_sub)]
        H0_cas_bin = H_0_cascade((z_lo + z_hi) / 2)
        delta = H0_fit - H0_cas_bin
        print(f"  {z_lo:.2f}-{z_hi:.2f}    | {mask.sum():>5} | {H0_fit:>10.2f} | {H0_cas_bin:>10.2f} | {delta:>+8.2f}")
        bin_results.append(((z_lo + z_hi) / 2, H0_fit, H0_cas_bin))
    
    if len(bin_results) >= 2:
        z_mids = np.array([r[0] for r in bin_results])
        H0_fits = np.array([r[1] for r in bin_results])
        slope = np.polyfit(z_mids, H0_fits, 1)[0]
        print(f"\n  Linear fit: H_0(z) slope = {slope:.2f}")
        if slope < -1:
            print(f"  H_0 decreases with z (CONSISTENT with cascade)")
        elif slope < 0:
            print(f"  Slight negative trend (weak support for cascade)")
        else:
            print(f"  H_0 does NOT decrease with z (NOT consistent with cascade)")

    print(f"\n\n  Step 5: H_0 at z=1 specifically (cascade's key prediction)")
    print(f"  ----------------------------------------------------------------")
    mask = (z_arr >= 0.8) & (z_arr <= 1.2)
    if mask.sum() > 0:
        z_sub = z_arr[mask]
        mb_sub = mb_arr[mask]
        err_sub = err_arr[mask]
        chi2_sub = []
        for H0 in H0_grid:
            MU_p = np.array([MU_pred(z, H0) for z in z_sub])
            _, c2 = compute_chi2_M(z_sub, mb_sub, err_sub, MU_p)
            chi2_sub.append(c2)
        chi2_sub = np.array(chi2_sub)
        H0_z1 = H0_grid[np.argmin(chi2_sub)]
        H0_cas_z1 = H_0_cascade(1.0)
        print(f"  SNe at z ~ 1 ({mask.sum()} SNe):")
        print(f"    Best-fit H_0 in LCDM: {H0_z1:.2f}")
        print(f"    Cascade prediction: H_0(z=1) = {H0_cas_z1:.2f}")
        print(f"    LCDM constant: H_0 = 67.4 (Planck)")
        print()
        d_lcdm = abs(H0_z1 - 67.4)
        d_cas = abs(H0_z1 - H0_cas_z1)
        print(f"    Distance from LCDM prediction: {d_lcdm:.2f}")
        print(f"    Distance from cascade prediction: {d_cas:.2f}")
        if d_cas < d_lcdm:
            print(f"  CASCADE PREDICTION IS CLOSER TO DATA (by {d_lcdm - d_cas:.2f})")
        else:
            print(f"  LCDM PREDICTION IS CLOSER TO DATA (by {d_cas - d_lcdm:.2f})")

    # Final summary
    hr()
    print("SUMMARY")
    hr()
    print(f"\n  Pantheon+ analysis ({len(hubble_flow)} Hubble flow SNe):")
    print(f"    Best-fit LCDM: H_0={best_H0_LCDM:.2f}, M={best_M_LCDM:.3f}, chi2={best_chi2_LCDM:.0f}")
    print(f"    Cascade: M={M_cas:.3f}, chi2={chi2_cas:.0f}")
    print(f"    Delta chi^2: {delta_chi2:.1f}")
    print()
    if delta_chi2 < -25:
        print(f"  CASCADE FITS SIGNIFICANTLY BETTER (~5 sigma)")
    elif delta_chi2 < -9:
        print(f"  CASCADE FITS BETTER (~3 sigma)")
    elif delta_chi2 < 0:
        print(f"  Cascade fits slightly better (not significant)")
    else:
        print(f"  LCDM FITS BETTER (cascade is not supported by Pantheon+)")
    print()
    if len(bin_results) >= 2:
        print(f"  H_0 vs z trend: slope = {slope:.2f}")
    print()
    print(f"  CAVEATS:")
    print(f"    1. Used diagonal errors only (full covariance would be better)")
    print(f"    2. No light-curve fit (SALT2 not applied)")
    print(f"    3. No bias corrections")
    print(f"    4. M is degenerate with H_0, so H_0 fit is loose")
    print(f"  For a definitive test, use sncosmo or CosmoSIS with full pipeline.")


if __name__ == "__main__":
    main()
