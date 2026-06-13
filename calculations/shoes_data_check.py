#!/usr/bin/env python3
"""
Task 5: SH0ES/Pantheon+ data check — does H_0 correlate with host galaxy type?

Cascade prediction (from Task 2): H_0 should be HIGHER in star-forming hosts
(spirals) vs passive hosts (ellipticals), because active star formation
correlates with active 2D universe creation, which contributes to local
antigravity bias.

This script summarizes what the *published data* actually shows about
H_0 vs host galaxy type, and whether the cascade's prediction is supported
or refuted.

Key finding from literature review:
  - SH0ES sample is BIASED toward late-type (spiral) galaxies because
    Cepheids are young, massive stars that only exist in star-forming hosts.
  - This means SH0ES H_0 is measured *primarily on star-forming hosts*,
    where the cascade predicts the *highest* H_0.
  - The cascade would predict: H_0(SBF on early-types) < H_0(SH0ES on spirals).
  - The actual data: SBF H_0 (Blakeslee et al. 2021) = 73.3 ± 0.7 ± 2.4 km/s/Mpc
    (using Cepheid+TRGB calibration)
  - The SBF H_0 is *similar* to SH0ES H_0, NOT lower.
  - This is a PROBLEM for the cascade's specific prediction.

Status: Cascade's prediction (H_0 in ellipticals should be lower) is
NOT supported by the data. Both methods give H_0 ~ 73.
"""

import sys
sys.path.insert(0, ".")


def hr(ch="="):
    print()
    print(ch * 78)
    print(ch * 78)


def main():
    hr()
    print("TASK 5: SH0ES/PANTHEON+ DATA CHECK — HOST GALAXY TYPE vs H_0")
    hr()

    # Step 1: What is the cascade's prediction?
    print(f"\n  Step 1: Cascade prediction (from Task 2 hubble_sfr_correlation.py)")
    print(f"  ----------------------------------------------------------------")
    print(f"  Active fraction of DM in:")
    print(f"    Passive elliptical (no recent SF): f_active ~ 0.05")
    print(f"    Normal spiral (modest SF):        f_active ~ 0.20")
    print(f"    Local 50 Mpc (mixed):             f_active ~ 0.30")
    print(f"    Starburst galaxy (high SF):       f_active ~ 0.55")
    print(f"    Central starburst (extreme SF):   f_active ~ 0.80")
    print()
    print(f"  Predicted H_0:")
    print(f"    Passive:      67.85 km/s/Mpc")
    print(f"    Normal:       69.22 km/s/Mpc")
    print(f"    Local:        70.13 km/s/Mpc")
    print(f"    Starburst:    72.40 km/s/Mpc")
    print(f"    C. starburst: 74.68 km/s/Mpc")
    print()
    print(f"  Cascade predicts: dH_0 / dlog(SFR) ~ 1.5 km/s/Mpc per decade")
    print(f"  Cascade predicts: H_0(passive) < H_0(starburst) by ~5 km/s/Mpc")

    # Step 2: What the data actually shows
    print(f"\n\n  Step 2: What the published data shows")
    print(f"  ----------------------------------------------------------------")
    print(f"  Riess et al. 2022 (SH0ES, 42 Cepheid calibrators):")
    print(f"    H_0 = 73.04 ± 1.04 km/s/Mpc (with systematics)")
    print(f"    Sample: ALL 42 host galaxies are spiral/late-type")
    print(f"    (Quote from A&A 2021: 'SNe calibrated with Cepheids are all")
    print(f"    hosted in late-type galaxies')")
    print()
    print(f"  Blakeslee et al. 2021 (SBF, 63 early-type galaxies):")
    print(f"    H_0 = 73.3 ± 0.7 ± 2.4 km/s/Mpc")
    print(f"    Sample: 63 bright, MAINLY EARLY-TYPE galaxies")
    print(f"    Calibration: still uses Cepheid+TRGB in spiral hosts")
    print()
    print(f"  KEY OBSERVATION: Both methods give H_0 ~ 73 km/s/Mpc,")
    print(f"  regardless of host galaxy type!")

    # Step 3: Does the cascade's prediction match?
    print(f"\n\n  Step 3: Comparison with cascade prediction")
    print(f"  ----------------------------------------------------------------")
    print(f"  Cascade predicts H_0 in elliptical hosts:")
    print(f"    With f_active = 0.05 (passive elliptical): H_0 = 67.85")
    print(f"    With f_active = 0.30 (local mixed):        H_0 = 70.13")
    print(f"    With f_active = 0.55 (starburst):          H_0 = 72.40")
    print()
    print(f"  Observed:")
    print(f"    SH0ES (spiral hosts):  H_0 = 73.04 ± 1.04")
    print(f"    SBF (early-type hosts): H_0 = 73.3 ± 0.7 ± 2.4")
    print()
    print(f"  COMPARISON:")
    print(f"    Cascade predicts H_0(elliptical) < H_0(spiral) by ~5 km/s/Mpc")
    print(f"    Observed: H_0(elliptical) ~ H_0(spiral) (both ~ 73)")
    print()
    print(f"  -> The cascade's specific prediction (H_0 correlation with SFR)")
    print(f"     is NOT supported by the data.")
    print()
    print(f"  HONEST INTERPRETATION:")
    print(f"    The cascade predicted H_0 should depend on host type (spiral vs")
    print(f"    elliptical). The data shows H_0 is ~ 73 in both, which is")
    print(f"    INCONSISTENT with the cascade's specific quantitative prediction.")
    print()
    print(f"    This is a *falsification* of the cascade's Task 2 prediction,")
    print(f"    not a confirmation.")

    # Step 4: Why might the cascade be wrong?
    print(f"\n\n  Step 4: Possible reasons for the discrepancy")
    print(f"  ----------------------------------------------------------------")
    print(f"  Possibility A: Selection bias in SH0ES")
    print(f"    The SH0ES sample is *all* spirals. The cascade would predict")
    print(f"    spiral H_0 > CMB H_0, which is observed. But the *specific*")
    print(f"    prediction of dH_0/dlog(SFR) = 1.5 km/s/Mpc is not testable")
    print(f"    from the SH0ES data alone (no ellipticals in sample).")
    print()
    print(f"  Possibility B: SBF calibration chain still uses spirals")
    print(f"    Blakeslee et al. measure early-type galaxies with SBF, but")
    print(f"    the calibration chain (zero point) uses Cepheid+TRGB distances")
    print(f"    in spiral hosts. So the SBF H_0 inherits the same calibration")
    print(f"    bias as SH0ES. This is not a *clean* test of elliptical hosts.")
    print()
    print(f"  Possibility C: The cascade is wrong")
    print(f"    The 2D universe's contribution to local H_0 may be")
    print(f"    smaller than the cascade predicts. The H_0 tension has a")
    print(f"    different origin (e.g., early-universe physics, not late-time")
    print(f"    local effects).")
    print()
    print(f"  Possibility D: The cascade's mechanism is different from what")
    print(f"    Task 2 assumed. The 'active children boost antigravity' may")
    print(f"    not be the right physical picture. The Hubble tension may")
    print(f"    be due to a different cascade effect (e.g., mechanism B from")
    print(f"    hubble_tightened.py: 4D event temporal structure).")

    # Step 5: What this means for the cascade
    hr()
    print("WHAT THIS MEANS FOR THE CASCADE")
    hr()
    print(f"\n  The cascade's specific Task 2 prediction is:")
    print(f"    H_0 should correlate with local SFR (H_0 in starbursts > H_0 in")
    print(f"    passive ellipticals).")
    print()
    print(f"  The data does NOT support this specific prediction.")
    print()
    print(f"  HOWEVER:")
    print(f"    - The data is selection-biased (SH0ES = all spirals; SBF")
    print(f"      calibration still uses spirals)")
    print(f"    - A clean test of elliptical H_0 doesn't exist in the literature")
    print(f"    - The cascade's *qualitative* prediction (H_0_local > H_0_CMB)")
    print(f"      is correct (the data shows H_0 ~ 73 > CMB ~ 67)")
    print()
    print(f"  Status: PARTIAL FAILURE")
    print(f"    The cascade's qualitative direction is correct.")
    print(f"    The cascade's specific quantitative correlation is NOT")
    print(f"    supported by the data.")
    print()
    print(f"  This is a *falsifiable prediction* that didn't pan out.")
    print(f"  The cascade's mechanism (active children boost local H_0) may")
    print(f"  be the wrong picture, or the magnitude is overestimated.")
    print()
    print(f"  What this teaches us:")
    print(f"  1. The Hubble tension may have a non-local origin")
    print(f"     (e.g., early-universe physics, not local effects)")
    print(f"  2. The cascade's mechanism A (active children) may not be the")
    print(f"     right one; mechanism B (4D event temporal structure) or")
    print(f"     mechanism D (selection effects) may be more accurate.")
    print(f"  3. The cascade's Task 2 prediction was a 'falsifiable' claim")
    print(f"     that has been *falsified* by the data (within the caveats).")
    print()
    print(f"  This is honest: the cascade made a specific prediction, and the")
    print(f"  data doesn't support it. The cascade's qualitative claims are")
    print(f"  still consistent with the data, but the specific quantitative")
    print(f"  prediction of H_0 correlation with host type is NOT.")


if __name__ == "__main__":
    main()
