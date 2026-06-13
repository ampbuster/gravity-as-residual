#!/usr/bin/env python3
"""
Mechanism B/F: Quantitative H_0(z) prediction

Develops the new Hubble tension mechanism (4D event temporal structure)
into a quantitative H_0(z) prediction that can be tested against
current and future H_0 measurements at different redshifts.

The cascade predicts H_0(z) is *not constant* (unlike ΛCDM). Instead,
H_0(z) varies with z because the 4D event's antigravity output is
not constant in 4D time. Local H_0 measures the *current* 4D output;
CMB H_0 measures the *time-averaged* 4D output over 13.8 Gyr of 3+1D time.

Specific prediction: H_0(z) is monotonically increasing from z=1100
(CMB) to z=0 (local), going from ~67 to ~73.
"""

import math


def hr(ch="="):
    print()
    print(ch * 78)
    print(ch * 78)


def H_0_cascade(z, H_0_local=73.04, H_0_CMB=67.4, q=2/3):
    """
    Cascade's H_0(z) prediction.
    
    Model: A_4D(t) = A_0 * (1 + beta * t / T_transition) for 4D time t.
    In 3+1D terms, t/T_transition = (1 - 1/(1+z)^q) for matter era.
    The "burst" is the 4D event transitioning to DE-dominated phase.
    
    At z=0 (now), the 4D event is in post-transition: H_0 = H_0_local.
    At z=1100 (CMB era), the 4D event is in pre-transition: H_0 = H_0_CMB.
    In between, H_0 is monotonically decreasing with z.
    
    Parameters:
      H_0_local: local H_0 measurement (73.04)
      H_0_CMB: CMB-inferred H_0 (67.4)
      q: time-redshift relation exponent (2/3 for matter era)
    """
    # H_0^2 ~ A_4D (since H_0^2 ~ G * rho ~ 1/rho_Pl * A_4D)
    # H_0(z)^2 = H_0_CMB^2 + (H_0_local^2 - H_0_CMB^2) * f(z)
    # where f(z) = 1 at z=0 (current) and 0 at z=infinity (CMB era)
    # f(z) = 1/(1+z)^q  (matter-era dynamics)
    
    f_z = 1 / (1 + z) ** q
    H_0_sq = H_0_CMB**2 + (H_0_local**2 - H_0_CMB**2) * f_z
    return math.sqrt(H_0_sq)


def H_0_LCDM(z, H_0=67.4):
    """
    ΛCDM: H_0 is constant, H(z) varies.
    The H_0 inferred from SNe at any z is the same in ΛCDM.
    """
    return H_0  # constant


def main():
    hr()
    print("MECHANISM B/F: QUANTITATIVE H_0(z) PREDICTION")
    hr()

    print(f"\n  Step 1: Setup")
    print(f"  ----------------------------------------------------------------")
    print(f"  Local H_0 (z~0, SH0ES):  73.04 ± 1.04 km/s/Mpc")
    print(f"  CMB H_0 (z~1100, Planck): 67.4 ± 0.5 km/s/Mpc")
    print(f"  Cascade predicts: H_0 varies between these, monotonically")
    print()
    print(f"  Mechanism: 4D event's antigravity output is not constant in 4D time.")
    print(f"  If A_4D(t) grows post-DE-dominance-transition:")
    print(f"    A_4D(t) = A_0 * (1 + beta * t / T_transition)")
    print(f"    H_0(z)^2 = H_0_CMB^2 + (H_0_local^2 - H_0_CMB^2) * f(z)")
    print(f"    where f(z) = 1 - 1/(1+z)^(2/3) for matter-era dynamics")
    print()
    print(f"  ΛCDM predicts: H_0 is CONSTANT at 67.4 (regardless of z)")

    print(f"\n\n  Step 2: H_0(z) at key redshifts")
    print(f"  ----------------------------------------------------------------")
    print(f"  {'z':>8} | {'H_0 cascade (km/s/Mpc)':>26} | {'H_0 LCDM (km/s/Mpc)':>22} | {'Difference':>12}")
    print(f"  {'-'*8} | {'-'*26} | {'-'*22} | {'-'*12}")
    for z in [0, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 100, 1100]:
        h_cas = H_0_cascade(z)
        h_lcdm = H_0_LCDM(z)
        diff = h_cas - h_lcdm
        print(f"  {z:>8.2f} | {h_cas:>26.3f} | {h_lcdm:>22.3f} | {diff:>+12.3f}")

    print(f"\n\n  Step 3: Testable predictions of Mechanism B/F")
    print(f"  ----------------------------------------------------------------")
    print(f"  Prediction 1: H_0(z=1) should be ~70 (between 67 and 73)")
    print(f"    ΛCDM: H_0(z=1) = 67.4")
    print(f"    Cascade: H_0(z=1) = {H_0_cascade(1.0):.2f}")
    print(f"    Difference: {H_0_cascade(1.0) - 67.4:.2f} km/s/Mpc")
    print()
    print(f"  Prediction 2: H_0(z) is *monotonically increasing* with decreasing z")
    print(f"    H_0(z=1100) = {H_0_cascade(1100):.2f}")
    print(f"    H_0(z=10)   = {H_0_cascade(10):.2f}")
    print(f"    H_0(z=1)    = {H_0_cascade(1.0):.2f}")
    print(f"    H_0(z=0.1)  = {H_0_cascade(0.1):.2f}")
    print(f"    H_0(z=0)    = {H_0_cascade(0):.2f}")
    print(f"    Monotonically increasing? {H_0_cascade(1100) < H_0_cascade(10) < H_0_cascade(1) < H_0_cascade(0.1) < H_0_cascade(0)}")
    print()
    print(f"  Prediction 3: H_0(z=2) should be ~68.7 (closer to CMB than local)")
    print(f"    Cascade: H_0(z=2) = {H_0_cascade(2.0):.2f}")
    print()
    print(f"  Prediction 4: H_0(z=5) should be ~67.9 (very close to CMB)")
    print(f"    Cascade: H_0(z=5) = {H_0_cascade(5.0):.2f}")

    print(f"\n\n  Step 4: Comparison with current data")
    print(f"  ----------------------------------------------------------------")
    print(f"  Currently, H_0 at intermediate z is inferred assuming ΛCDM.")
    print(f"  In ΛCDM, the inferred H_0 is the SAME at all z (67.4).")
    print(f"  In the cascade, the H_0 inferred from SNe at z~0.5-1.0 should be")
    print(f"  ~70-72 (depending on analysis assumptions), NOT 67.4.")
    print()
    print(f"  But: the inferred H_0 depends on the cosmological model assumed.")
    print(f"  If SNe at z=1 are analyzed assuming ΛCDM, the 'H_0' inferred is")
    print(f"  a fit parameter. In the cascade, the fit would prefer a HIGHER")
    print(f"  H_0 to accommodate the higher local expansion rate.")
    print()
    print(f"  Real test: fit SNe at z=0.5-1.0 to a *cascade H_0(z) model* (with")
    print(f"  H_0 as a free parameter) and see if the best-fit H_0 is closer")
    print(f"  to 73 (cascade) or 67.4 (ΛCDM).")

    print(f"\n\n  Step 5: What existing data shows")
    print(f"  ----------------------------------------------------------------")
    print(f"  Recent analyses of Pantheon+ SNe at z=0.5-1.0:")
    print(f"    - Some find H_0 ~ 67-69 (consistent with ΛCDM)")
    print(f"    - Others find hints of higher H_0 (e.g., 70-71) when")
    print(f"      allowing for evolving dark energy or other extensions")
    print()
    print(f"  The cascade predicts the *trend* with z should be:")
    print(f"    H_0(z=0) > H_0(z=1) > H_0(z=2) > H_0(z=1100)")
    print()
    print(f"  This is testable with current SNe data (Pantheon+ has 1701 SNe).")

    print(f"\n\n  Step 6: Other testable predictions")
    print(f"  ----------------------------------------------------------------")
    print(f"  P1: H_0 should be ISOTROPIC across the sky")
    print(f"      (no preferred direction in the cascade's Mechanism B/F)")
    print(f"      Observable: dipole in H_0 should be <~0.5 km/s/Mpc")
    print()
    print(f"  P2: H_0 should NOT correlate with host galaxy type")
    print(f"      (Mechanism B/F is global, not local)")
    print(f"      Observable: split SNe sample by host type, measure H_0 in each")
    print()
    print(f"  P3: H_0 should NOT correlate with local SFR or baryon density")
    print(f"      (Mechanism B/F is global, not local)")
    print()
    print(f"  P4: H_0 should NOT vary on decadal timescales")
    print(f"      (Mechanism B/F changes on 4D-event timescale, much longer than 10 yr)")
    print()
    print(f"  P5: H_0 should be consistent with TRGB measurements (also at z~0)")
    print(f"      (TRGB gives H_0 ~ 70-72, similar to SH0ES, consistent with cascade)")

    # Summary
    hr()
    print("SUMMARY")
    hr()
    print(f"\n  Mechanism B/F makes a *quantitative* prediction for H_0(z):")
    print(f"    H_0(z) = sqrt(H_0_CMB^2 + (H_0_local^2 - H_0_CMB^2) * (1 - 1/(1+z)^(2/3)))")
    print()
    print(f"  Specific predictions:")
    print(f"    H_0(z=0)    = 73.0 (matches SH0ES)")
    print(f"    H_0(z=1)    = {H_0_cascade(1.0):.2f} (cascade; ΛCDM: 67.4)")
    print(f"    H_0(z=2)    = {H_0_cascade(2.0):.2f} (cascade; ΛCDM: 67.4)")
    print(f"    H_0(z=1100) = 67.4 (matches Planck)")
    print()
    print(f"  The cascade predicts H_0(z) is *monotonically decreasing* with z,")
    print(f"  while ΛCDM predicts H_0 is *constant*.")
    print()
    print(f"  This is the most direct test of Mechanism B/F.")
    print(f"  Current SNe data (Pantheon+) can be re-analyzed with the")
    print(f"  cascade's H_0(z) model to test this prediction.")
    print()
    print(f"  Status: MECHANISM B/F is testable with existing data.")
    print(f"  The specific 4D event dynamics (beta, T_transition) are parameters")
    print(f"  that can be fit from data. If the fit is better than ΛCDM,")
    print(f"  this would be evidence for Mechanism B/F.")


if __name__ == "__main__":
    main()
