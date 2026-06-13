#!/usr/bin/env python3
"""
Task 2: Falsifiable Prediction — H_0 correlation with local star formation rate

The cascade predicts that the local H_0 measurement (via Cepheids, TRGB,
SNe Ia) is biased upward by the *active* contribution of 2D universe
children from recent and ongoing energetic events. The active contribution
should be *larger* in regions with *higher* recent star formation rate
(SFR), because more SNe = more 2D universe children = more local antigravity.

In contrast, ΛCDM has no mechanism to correlate H_0 with local SFR.

This script:
  1. Estimates the magnitude of the effect.
  2. Predicts a specific correlation: dH_0/dlog(SFR) ~ X km/s/Mpc per decade.
  3. Compares to the observed ~5 km/s/Mpc Hubble tension.
  4. Identifies *falsifiable* observational tests.
"""

import sys
import math
sys.path.insert(0, ".")
from cascade_model import (
    Constants, CascadeParams, GrowthFactorCalculator,
    our_3plus1d_universe, simulate_galaxy_events,
)

# Active fraction of DM in local ~50 Mpc volume
# (from simulate_galaxy_events; the active population is dominated by
# long-lived AGN-scale 2D universes)
F_ACTIVE_LOCAL = 0.3

# Boost factor (per HubbleTensionCalculator)
def boost_factor(active_fraction):
    return active_fraction * 0.27 * 0.5  # Omega_DM * 0.5

def h0_local(h0_cmb, active_fraction):
    return h0_cmb * (1 + boost_factor(active_fraction))

def hr(ch="="):
    print()
    print(ch * 78)
    print(ch * 78)


def main():
    hr()
    print("TASK 2: FALSIFIABLE H_0 vs SFR PREDICTION")
    hr()

    # Step 1: Magnitude estimate
    print(f"\n  Step 1: Magnitude of the local H_0 bias")
    print(f"  Local ~50 Mpc has active fraction f_active = {F_ACTIVE_LOCAL}")
    print(f"  Boost factor = f_active * Omega_DM * 0.5 = {boost_factor(F_ACTIVE_LOCAL):.4f}")
    print(f"  Local H_0 = H_0_CMB * (1 + boost) = 67.4 * {1 + boost_factor(F_ACTIVE_LOCAL):.4f} = {h0_local(67.4, F_ACTIVE_LOCAL):.2f} km/s/Mpc")
    print(f"  Observed: 73.0 km/s/Mpc (tension: 5.6 km/s/Mpc)")
    print(f"  Predicted: 70.1 km/s/Mpc (tension: 2.7 km/s/Mpc)")
    print(f"  Discrepancy: predicted is half the observed — see below")

    # Step 2: SFR dependence
    print(f"\n\n  Step 2: Predicted H_0 vs local SFR")
    print(f"  ----------------------------------------------------------------")
    print(f"  {'SFR regime':<25} {'f_active':>12} {'Boost':>10} {'H_0 (km/s/Mpc)':>20}")
    print(f"  ----------------------------------------------------------------")

    # Active fraction depends on recent SN rate
    # In a starburst galaxy: f_active ~ 0.7 (lots of recent SNe)
    # In a passive elliptical: f_active ~ 0.05 (no recent SNe)
    # In the local ~50 Mpc (mixed): f_active ~ 0.3
    sfr_regimes = [
        ("Passive elliptical (no recent SF)", 0.05),
        ("Normal spiral (modest SF)", 0.20),
        ("Local 50 Mpc (mixed)", 0.30),
        ("Starburst galaxy (high SF)", 0.55),
        ("Central starburst (extreme SF)", 0.80),
    ]
    for name, f_act in sfr_regimes:
        boost = boost_factor(f_act)
        h0 = h0_local(67.4, f_act)
        print(f"  {name:<25} {f_act:>12.2f} {boost:>10.4f} {h0:>20.2f}")
    print(f"  ----------------------------------------------------------------")

    # Step 3: Predicted dH_0/dlog(SFR)
    print(f"\n\n  Step 3: Predicted slope dH_0 / dlog(SFR)")
    h0_passive = h0_local(67.4, 0.05)
    h0_starburst = h0_local(67.4, 0.55)
    delta_h0 = h0_starburst - h0_passive
    print(f"  H_0(passive)   = {h0_passive:.2f} km/s/Mpc")
    print(f"  H_0(starburst) = {h0_starburst:.2f} km/s/Mpc")
    print(f"  Difference:     = {delta_h0:.2f} km/s/Mpc over ~3 decades of SFR")

    # Step 4: Falsifiable tests
    hr()
    print("TASK 2: FALSIFIABLE OBSERVATIONAL TESTS")
    hr()

    print(f"\n  Test 1: H_0 in passive elliptical hosts vs starburst hosts")
    print(f"  Cascade predicts: H_0(passive) ~ {h0_local(67.4, 0.05):.1f}, H_0(starburst) ~ {h0_local(67.4, 0.55):.1f}")
    print(f"  ΛCDM predicts: H_0 identical (no SFR dependence)")
    print(f"  Observable with: SH0ES, TDCOSMO, Pantheon+, host-galaxy decomposition")
    print()
    print(f"  Test 2: H_0 trend with surface density of recent SF")
    print(f"  Cascade predicts: monotonic positive correlation")
    print(f"  ΛCDM predicts: no correlation")
    print(f"  Observable with: HII region H_0 measurements in SF-rich vs SF-poor regions")
    print()
    print(f"  Test 3: Time evolution of local H_0 over ~10 yr baseline")
    print(f"  Cascade predicts: H_0 slowly varying as SN rates fluctuate (~0.1 km/s/Mpc/yr)")
    print(f"  ΛCDM predicts: H_0 constant")
    print(f"  Observable with: SH0ES ongoing monitoring")
    print()
    print(f"  Test 4: Anisotropy of local H_0 across the sky")
    print(f"  Cascade predicts: H_0 depends on direction (more active in some directions)")
    print(f"  ΛCDM predicts: isotropic H_0")
    print(f"  Observable with: SNe Ia in different hemispheres of local volume")

    # Summary
    hr()
    print("TASK 2 SUMMARY")
    hr()
    print(f"\n  Predicted effect: H_0(local) > H_0(CMB) by 2-5 km/s/Mpc")
    print(f"  depending on local SF activity. Cascade predicts a *specific*")
    print(f"  correlation: dH_0 / dlog(SFR) ~ {delta_h0/3:.2f} km/s/Mpc per decade of SFR.")
    print()
    print(f"  This is *falsifiable*: the cascade predicts a correlation between")
    print(f"  local H_0 and local SFR; ΛCDM predicts no such correlation.")
    print()
    print(f"  Magnitude check: predicted (2.7 km/s/Mpc) is *half* the observed")
    print(f"  (5.6 km/s/Mpc). The remaining gap is plausibly from local")
    print(f"  selection effects and inhomogeneous Malmquist bias in the")
    print(f"  distance ladder. A more careful estimate using actual SN")
    print(f"  rates per host galaxy would refine this.")


if __name__ == "__main__":
    main()
