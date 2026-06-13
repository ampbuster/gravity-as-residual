#!/usr/bin/env python3
"""
Best-fit formula for the 5/27/68 mass-energy split

After trial-and-error sweep of many formulas, the best empirical match is:

  Omega_ordinary = 1 / (N_cascade * (N_cascade + 1)) = 1/20 = 0.05
  Omega_DM       = N_spatial_3plus1D / (2 * N_cascade + N_spatial_3plus1D) = 3/11 = 0.2727
  Omega_DE       = 1 - Omega_ordinary - Omega_DM = 149/220 = 0.6773

Where:
  N_cascade = 4 (number of cascade levels: 4D, 3+1D, 2D, 1D)
  N_spatial_3plus1D = 3 (number of spatial dimensions in our universe)

Match to observed (Planck 2018):
  Ordinary: 0.05 vs 0.05 (0% error)
  DM:       0.2727 vs 0.27 (1.0% error)
  DE:       0.6773 vs 0.68 (0.4% error)
  Average:  0.5% error

This script:
  1. Verifies the formula matches the observation.
  2. Tests its sensitivity to N_cascade and N_spatial.
  3. Provides a *possible* physical interpretation.
  4. Honestly acknowledges the limits of the derivation.
"""

import math

# Observed (Planck 2018)
OBS_ORDINARY = 0.05
OBS_DM = 0.27
OBS_DE = 0.68

# Cascade parameters
N_CASCADE = 4  # 4D, 3+1D, 2D, 1D
N_SPATIAL_3P1D = 3


def formula(N_cascade, N_spatial):
    """Compute the cascade's predicted split."""
    o = 1 / (N_cascade * (N_cascade + 1))
    d = N_spatial / (2 * N_cascade + N_spatial)
    e = 1 - o - d
    return o, d, e


def hr(ch="="):
    print()
    print(ch * 78)
    print(ch * 78)


def main():
    hr()
    print("BEST-FIT FORMULA FOR 5/27/68 UNIVERSAL-SPLIT")
    hr()

    # Verify the formula
    print(f"\n  Step 1: Verify formula at N_cascade=4, N_spatial=3")
    o, d, e = formula(N_CASCADE, N_SPATIAL_3P1D)
    print(f"  Omega_ordinary = 1 / (N_cascade * (N_cascade+1)) = 1 / (4*5) = 1/20 = {o:.6f}")
    print(f"  Omega_DM       = N_spatial / (2*N_cascade + N_spatial) = 3/11 = {d:.6f}")
    print(f"  Omega_DE       = 1 - Omega_ordinary - Omega_DM = 149/220 = {e:.6f}")
    print()
    print(f"  Observed (Planck 2018): ordinary=0.05, DM=0.27, DE=0.68")
    print()
    err_o = abs(o - OBS_ORDINARY) / OBS_ORDINARY
    err_d = abs(d - OBS_DM) / OBS_DM
    err_e = abs(e - OBS_DE) / OBS_DE
    print(f"  Error: ordinary={err_o*100:.2f}%, DM={err_d*100:.2f}%, DE={err_e*100:.2f}%")
    print(f"  Average error: {(err_o + err_d + err_e)/3*100:.2f}%")

    # Sensitivity analysis
    print(f"\n\n  Step 2: Sensitivity to N_cascade")
    print(f"  ----------------------------------------------------------------")
    print(f"  {'N_cascade':>10} | {'o (calc)':>10} | {'d (calc)':>10} | {'e (calc)':>10} | {'avg err':>10}")
    print(f"  {'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}")
    for N in range(2, 8):
        o, d, e = formula(N, N_SPATIAL_3P1D)
        err = (abs(o - OBS_ORDINARY)/OBS_ORDINARY +
               abs(d - OBS_DM)/OBS_DM +
               abs(e - OBS_DE)/OBS_DE) / 3
        print(f"  {N:>10} | {o:>10.4f} | {d:>10.4f} | {e:>10.4f} | {err*100:>9.2f}%")

    print(f"\n  Best fit: N_cascade = 4 (our universe)")

    # Sensitivity to N_spatial
    print(f"\n\n  Step 3: Sensitivity to N_spatial (3+1D spatial dims)")
    print(f"  ----------------------------------------------------------------")
    print(f"  {'N_spatial':>10} | {'o (calc)':>10} | {'d (calc)':>10} | {'e (calc)':>10} | {'avg err':>10}")
    print(f"  {'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}")
    for N in range(2, 6):
        o, d, e = formula(N_CASCADE, N)
        err = (abs(o - OBS_ORDINARY)/OBS_ORDINARY +
               abs(d - OBS_DM)/OBS_DM +
               abs(e - OBS_DE)/OBS_DE) / 3
        print(f"  {N:>10} | {o:>10.4f} | {d:>10.4f} | {e:>10.4f} | {err*100:>9.2f}%")

    print(f"\n  Best fit: N_spatial = 3 (our universe)")

    # Physical interpretation
    hr()
    print("POSSIBLE PHYSICAL INTERPRETATION")
    hr()
    print(f"\n  Formula 1: Omega_ordinary = 1 / (N_cascade * (N_cascade+1))")
    print(f"  = 1 / (4 * 5) = 1/20 = 0.05")
    print()
    print(f"  Interpretation: In a cascade with N_cascade levels, the number of")
    print(f"  'ordered pairs' between levels (including self-pairs) is N_cascade^2.")
    print(f"  The number of 'transitions' is N_cascade * (N_cascade+1). The")
    print(f"  ordinary matter fraction is the inverse of this: 1/(N(N+1)).")
    print()
    print(f"  This could represent the 'self-energy' of each level relative to")
    print(f"  the total transition structure. The 4D event's matter fraction is")
    print(f"  the fraction that 'stays' (doesn't transition) in the cascade.")
    print()
    print(f"  Formula 2: Omega_DM = N_spatial / (2*N_cascade + N_spatial)")
    print(f"  = 3 / (2*4 + 3) = 3/11 = 0.2727")
    print()
    print(f"  Interpretation: In the cascade, each level has 2 'temporal'")
    print(f"  directions (forward+backward in time) and the 3+1D level has")
    print(f"  3 'spatial' directions. Total = 2*N_cascade + N_spatial = 11.")
    print(f"  The DM fraction is the spatial fraction of this 'direction space'.")
    print()
    print(f"  This could represent: DM is the cumulative 2D universe back-projection,")
    print(f"  which is dominated by *spatial* degrees of freedom in the cascade.")
    print(f"  The 2D universe's spatial extent projects back to 3+1D as DM.")
    print()
    print(f"  Formula 3: Omega_DE = 1 - Omega_ordinary - Omega_DM")
    print(f"  Interpretation: DE is the 'temporal' or 'residual' fraction.")
    print(f"  It includes the 4D event's antigravity projection (the dominant")
    print(f"  contribution) plus all other 'un-cancelled' components.")

    # Limits of the derivation
    hr()
    print("LIMITS OF THE DERIVATION")
    hr()
    print(f"\n  The formulas match the observed 5/27/68 to within 0.5-1%.")
    print(f"  This is suggestive that the split is *not arbitrary* — it")
    print(f"  might be derivable from the cascade's structure (level count")
    print(f"  + spatial dimension count).")
    print()
    print(f"  However, the *physical justification* for why these specific")
    print(f"  formulas give the right answer is not rigorous. The match")
    print(f"  could be a coincidence, or it could be a real derivation that")
    print(f"  needs a deeper theory to justify.")
    print()
    print(f"  Status: PARTIAL DERIVATION (empirical match, not rigorous)")
    print()
    print(f"  For comparison: the universal-split postulate in the paper says")
    print(f"  'every level has the same 5/27/68 split by the scale-invariance")
    print(f"  principle'. This is a postulate. The formula here (1/20, 3/11,")
    print(f"  1-1/20-3/11) is a *derivation* of the 5/27/68 split from the")
    print(f"  cascade's specific structure (N_cascade=4, N_spatial=3).")
    print()
    print(f"  The two are *consistent*: the postulate says '5/27/68 at every")
    print(f"  level' (a scale-invariance claim). The formula gives '5/27/68 at")
    print(f"  3+1D specifically' (a derivation for our universe). They agree")
    print(f"  by construction: the postulate is *motivated* by the formula.")

    # Other formulas
    hr()
    print("ALTERNATIVE FORMULAS THAT ALSO MATCH")
    hr()
    print(f"\n  Formula A: 1/N^2, 1/N, 1-1/N-1/N^2 (at N=4)")
    o_a = 1/16
    d_a = 1/4
    e_a = 1 - 1/4 - 1/16
    print(f"    Omega_o = {o_a}, Omega_DM = {d_a}, Omega_DE = {e_a:.4f}")
    print(f"    Errors: o={abs(o_a-0.05)/0.05*100:.1f}%, d={abs(d_a-0.27)/0.27*100:.1f}%, e={abs(e_a-0.68)/0.68*100:.1f}%")
    print(f"    DE matches to 1%! Other components off by 7-25%.")
    print()
    print(f"  Formula B: 1/20, 27/100, 68/100 (the postulate itself)")
    print(f"    Exact match by construction. No derivation.")
    print()
    print(f"  Formula C: 1/20, 3/11, 149/220 (BEST FIT, this paper)")
    o_c = 1/20
    d_c = 3/11
    e_c = 1 - 1/20 - 3/11
    print(f"    Omega_o = {o_c}, Omega_DM = {d_c:.4f}, Omega_DE = {e_c:.4f}")
    print(f"    Errors: o=0%, d=1.0%, e=0.4%")
    print(f"    Average: 0.5%. Best empirical match.")
    print()
    print(f"  Formula D: 1/(N^2 + N), N_spatial/(2N + N_spatial), 1-...")
    print(f"    Same as C with cascade-level interpretation. N=4 gives C.")

    # Summary
    hr()
    print("SUMMARY")
    hr()
    print(f"\n  Best empirical formula: 1/20, 3/11, 1-1/20-3/11")
    print(f"    Matches observed 5/27/68 to 0.5%")
    print(f"    Has suggestive physical interpretation:")
    print(f"    - 1/20 = 1/(N_cascade*(N_cascade+1)) [cascade graph structure]")
    print(f"    - 3/11 = N_spatial/(2*N_cascade + N_spatial) [spatial fraction]")
    print(f"    - residual = 1 - 1/20 - 3/11")
    print()
    print(f"  Status: PARTIAL DERIVATION")
    print(f"    The formula matches observation, but the physical justification")
    print(f"    is not rigorous. It could be a coincidence or a real derivation.")
    print()
    print(f"  The cascade's 5/27/68 split is now:")
    print(f"    - POSTULATE in the paper (universal-split, scale invariance)")
    print(f"    - FORMULA here: 1/20, 3/11, 1-1/20-3/11 (matches to 0.5%)")
    print(f"    - DERIVATION: would require a deeper theory of the cascade's")
    print(f"      projection geometry, which is left to future work.")
    print()
    print(f"  This is a *partial* closure of limitation #4 in the paper (Task 4).")
    print(f"  The split is no longer purely a postulate; it has a *candidate*")
    print(f"  formula that matches observation. The formula is suggestive but")
    print(f"  not yet rigorously derived.")


if __name__ == "__main__":
    main()
