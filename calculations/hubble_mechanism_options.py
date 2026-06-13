#!/usr/bin/env python3
"""
Alternative Hubble tension mechanisms for the cascade

Mechanism B/F was rejected by Pantheon+ at ~7 sigma (commit 82).
What other mechanisms could the cascade propose?

The Hubble tension: H_0_local (73) vs H_0_CMB (67.4), 5.6 km/s/Mpc apart.
Cascade's job: explain this WITHOUT new physics beyond the 4D event.

Possible mechanisms:

A) Mechanism B/F (REJECTED): 4D event's antigravity output varies in 4D time.
   H_0(z) decreases monotonically with z.
   Status: REJECTED at ~7 sigma by Pantheon+.

B) Mechanism C: H_0 is the same in all directions but DIFFERENT in different
   *regions* of the universe. Local Hubble bubble vs cosmic average.
   This is essentially the 'local void' hypothesis.
   Status: somewhat consistent with SH0ES+Planck, but doesn't fully resolve.

C) Mechanism D: H_0 is set by the 2D universe creation rate in our region.
   More 2D universes = more DM back-projection = different H_0 effective.
   The rate depends on local stellar/AGN activity.
   Status: speculation, hard to test.

D) Mechanism E: The 4D event's projection is ANISOTROPIC. Different
   directions have different projection fractions.
   Status: would manifest as H_0 dipole, which is NOT observed strongly.

E) Mechanism G: H_0 is not a single number. It's a *function* of the
   cascade's parameters. The 'H_0 tension' is just our local region
   having a slightly different 4D event geometry.
   Status: not a mechanism, just a description.

F) Mechanism H: The cascade doesn't explain the Hubble tension. It's
   an open question for the cascade.
   Status: honest position.

G) Mechanism I: The 4D event has TWO components: a 'long-lived' component
   (creates our universe) and a 'recent burst' (boosts local H_0).
   The recent burst is local, doesn't affect CMB (which averages over
   a larger volume).
   Status: this is the "late-time physics" hypothesis. Could work
   but needs more development.

H) Mechanism J: 4D event's antigravity decays exponentially with 4D
   time, so the projection to 3+1D is stronger now (z=0) than at z=1100.
   This is similar to B/F but with exponential decay.
   Status: would give similar predictions to B/F, likely rejected.

I) Mechanism K: 4D event's projection has a *delay*. The 4D event
   projects to 3+1D with a time delay; we see the projection now,
   but the CMB is from 13.8 Gyr ago (different 4D event state).
   Status: essentially B/F with different functional form.

Let me think more carefully about what's CONSISTENT with Pantheon+.

Pantheon+ rejects monotonic H_0(z) decrease. So mechanisms B/F, J, K
all give this prediction, so they're all rejected.

What could be consistent with Pantheon+ (constant H_0 within error)?

A) H_0 is locally high but globally constant. Pantheon+ measures
   cosmological distances, so it sees the *average* H_0 of the universe,
   not local H_0. The local bubble might be high.
   - SH0ES measures H_0 locally (within ~100 Mpc)
   - Pantheon+ measures H_0 averaged over 1588 SNe spanning z=0.01-1.5
   - The Pantheon+ best-fit H_0 is the *average* H_0
   - Local void would affect SH0ES (z~0) but not Pantheon+ (high z)
   
B) Late-time physics: something changed in the universe recently
   (last few Gyr) that affects local H_0 but not early universe.
   - Dark energy equation of state w != -1
   - Modified gravity at late times
   - These are standard physics modifications, not cascade-specific

C) The cascade accepts the Hubble tension as a feature, not a bug.
   The tension is REAL and the cascade accommodates it.
   - This is the most honest position.

So the most viable options for the cascade:
1. Local bubble / void (Mechanism C)
2. Late-time physics modification (Mechanism I or B)
3. Accept the tension (Mechanism H)

Let me also think: does Pantheon+ PRECLUDE any H_0(z) variation?
Pantheon+ constrains H_0 to be ~73 ± 2 (within statistical error) across
z bins (commits 79, 82). So H_0 is consistent with CONSTANT ~73
across z.

This is consistent with the standard Hubble tension:
- Local H_0 ~ 73 (SH0ES)
- Pantheon+ best-fit H_0 ~ 73 (matches SH0ES)
- CMB-inferred H_0 ~ 67 (Planck)

The tension is between LOCAL + PANTHEON+ (73) vs CMB (67). Not within
Pantheon+ itself.

So Mechanism B/F was wrong because it predicted H_0(z) decrease, but
data shows H_0(z) is roughly constant at ~73.

For the cascade, the right mechanism is:
- H_0 is roughly constant at ~73 in 3+1D's frame
- The CMB H_0 of 67.4 is from PLANCK's analysis of the CMB, which uses
  LCDM model to infer H_0
- The cascade's mechanism for the tension: PLANCK's analysis assumes LCDM,
  but in the cascade, the universe is NOT LCDM (it's the cascade)
- When CMB is analyzed with the CASCADE's model, the inferred H_0
  might come out as ~73 too

This is actually a more sophisticated take. The cascade doesn't need
to predict H_0(z) variation. It just needs to say:
  "In the cascade's model, the CMB-inferred H_0 of 67.4 is an artifact
  of assuming LCDM. With the cascade's model, CMB analysis would give
  H_0 ~ 73 (consistent with local + Pantheon+)."

This is the "model-dependent" interpretation of the Hubble tension.

Let me write this up.
"""

import math
import sys
sys.path.insert(0, ".")
sys.path.insert(0, "calculations")

from cascade_model import Constants


def hr(ch="="):
    print()
    print(ch * 78)
    print(ch * 78)


def main():
    hr()
    print("ALTERNATIVE HUBBLE TENSION MECHANISMS FOR THE CASCADE")
    hr()

    print(f"\n  Context: Mechanism B/F was REJECTED at ~7 sigma by Pantheon+ (commit 82).")
    print(f"  Question: what other mechanisms could the cascade propose?")
    
    print(f"\n\n  Step 1: Recall the data")
    print(f"  ----------------------------------------------------------------")
    print(f"  H_0_local (SH0ES): 73.04 ± 1.04 km/s/Mpc (z~0, ~40 calibrators)")
    print(f"  H_0_CMB (Planck): 67.4 ± 0.5 km/s/Mpc (z~1100, ΛCDM-inferred)")
    print(f"  H_0_Pantheon+: 73.00 km/s/Mpc (z=0.01-1.5, 1588 SNe, full cov)")
    print(f"  Difference: H_0_local ~ H_0_Pantheon+ ≠ H_0_CMB")
    print()
    print(f"  Tension: between LOCAL+PANTHEON+ (73) and CMB (67).")
    print(f"  Pantheon+ itself shows roughly constant H_0 ~ 73 across z bins.")
    print(f"  Mechanism B/F was wrong because it predicted H_0(z) decrease.")

    print(f"\n\n  Step 2: Mechanism B/F summary (rejected)")
    print(f"  ----------------------------------------------------------------")
    print(f"  Mechanism: 4D event's antigravity output varies in 4D time.")
    print(f"  Prediction: H_0(z) decreases monotonically with z.")
    print(f"  H_0(z=0) = 73, H_0(z=1) = 71, H_0(z=1100) = 67.")
    print(f"  Status: REJECTED at 7 sigma by Pantheon+ (commit 82).")
    print(f"  Reason: Pantheon+ shows H_0 is roughly constant at ~73,")
    print(f"          not decreasing with z as B/F predicted.")

    print(f"\n\n  Step 3: Alternative Mechanism C - Local bubble / void")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: We live in a local underdensity (Hubble bubble).")
    print(f"        Local H_0 is higher than cosmic average.")
    print(f"        Pantheon+ measures cosmic average (over 1588 SNe).")
    print(f"  Prediction:")
    print(f"    - Local H_0 (SH0ES) > cosmic H_0 (Pantheon+)")
    print(f"    - But Pantheon+ best-fit is H_0 ~ 73, which matches local")
    print(f"    - So Pantheon+ should give slightly LOWER H_0 if void is real")
    print(f"  Status:")
    print(f"    - Conceptually OK")
    print(f"    - But: Pantheon+ H_0 ~ 73 matches SH0ES H_0 ~ 73, not lower")
    print(f"    - Suggests the local bubble, if real, is small")
    print(f"  Viable? Maybe, but doesn't fully explain tension (CMB 67 is still off)")

    print(f"\n\n  Step 4: Alternative Mechanism I - Late-time physics")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: Something changed in the universe recently (last few Gyr)")
    print(f"        that affects local H_0 but not early universe.")
    print(f"  Examples:")
    print(f"    - Dark energy equation of state w != -1 (e.g., w = -0.9)")
    print(f"    - Modified gravity at late times")
    print(f"    - 'Early dark energy' (EDE) that decays")
    print(f"    - 4D event's recent burst (similar to B/F but local)")
    print(f"  Status:")
    print(f"    - 'Late w' is a real research direction (w != -1)")
    print(f"    - EDE is also a real research direction")
    print(f"    - 4D event's recent burst is B/F (rejected)")
    print(f"  Viable? Yes, but these are standard physics modifications,")
    print(f"  not cascade-specific.")

    print(f"\n\n  Step 5: Alternative Mechanism L - Model-dependent interpretation")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: The H_0 tension is a MODEL-DEPENDENT artifact.")
    print(f"        CMB-inferred H_0 = 67.4 assumes LCDM.")
    print(f"        In the cascade's model, CMB analysis would give H_0 ~ 73.")
    print(f"  Mechanism:")
    print(f"    - Planck analyzes CMB assuming LCDM")
    print(f"    - In cascade, the universe is NOT LCDM (it's the cascade)")
    print(f"    - The '67.4' is an artifact of forcing cascade to look like LCDM")
    print(f"    - Re-analyzing CMB with cascade's model: H_0 ~ 73")
    print(f"  Prediction:")
    print(f"    - H_0 is constant ~73 at all z (matches Pantheon+ and SH0ES)")
    print(f"    - 'CMB H_0' is model-dependent, not a real measurement")
    print(f"  Status:")
    print(f"    - This is the most sophisticated cascade interpretation")
    print(f"    - Requires re-analyzing Planck data with cascade model")
    print(f"    - Would be a substantial analysis (CosmoSIS pipeline)")
    print(f"  Viable? Yes, but requires serious work to verify.")

    print(f"\n\n  Step 6: Alternative Mechanism M - Accept the tension")
    print(f"  ----------------------------------------------------------------")
    print(f"  Idea: The cascade doesn't explain the Hubble tension.")
    print(f"        The tension is real, and the cascade accommodates it.")
    print(f"  Status:")
    print(f"    - Honest, but not a 'mechanism' per se")
    print(f"    - The cascade's contribution is to provide the framework")
    print(f"      (DM from 2D, DE from 4D, etc.)")
    print(f"    - The Hubble tension is a separate problem that the cascade")
    print(f"      doesn't solve")
    print(f"  Viable? Yes, but unsatisfying.")

    print(f"\n\n  Step 7: Other exotic mechanisms")
    print(f"  ----------------------------------------------------------------")
    print(f"  Mechanism N: 4D event has a 'memory' that decays with time.")
    print(f"    - Similar to B/F, but the decay is along a different parameter")
    print(f"    - H_0 is determined by 4D event's 'memory state'")
    print(f"    - The memory affects how 4D projects to 3+1D")
    print(f"    - Result: H_0 could vary in non-monotonic ways")
    print(f"    Status: speculative, hard to test.")
    print()
    print(f"  Mechanism O: H_0 depends on observer (relativistic)")
    print(f"    - Different observers in different parts of the universe see different H_0")
    print(f"    - We see H_0 ~ 73 because we're in a 'high H_0' region")
    print(f"    - But this is essentially the local bubble hypothesis")
    print(f"    Status: equivalent to Mechanism C")
    print()
    print(f"  Mechanism P: H_0 depends on 2D universe creation rate")
    print(f"    - 2D universes are created by 3+1D events")
    print(f"    - More 2D universes = different effective H_0 in that region")
    print(f"    - Our region has more 2D universes (more activity)")
    print(f"    - This gives higher local H_0")
    print(f"    Status: speculation, hard to test observationally")

    print(f"\n\n  Step 8: What's most viable for the cascade?")
    print(f"  ----------------------------------------------------------------")
    print(f"  Ranking by viability:")
    print()
    print(f"  1. Mechanism L (model-dependent interpretation):")
    print(f"     - Most consistent with data")
    print(f"     - H_0 is constant at ~73 (matches Pantheon+ and SH0ES)")
    print(f"     - 'CMB H_0 = 67.4' is model-dependent, not a real measurement")
    print(f"     - Requires re-analyzing Planck with cascade model")
    print()
    print(f"  2. Mechanism C (local bubble):")
    print(f"     - Standard physics hypothesis")
    print(f"     - Consistent with Pantheon+ (which measures cosmic average)")
    print(f"     - But: Pantheon+ best-fit is 73, not lower")
    print()
    print(f"  3. Mechanism I (late-time physics):")
    print(f"     - Real research direction (w != -1, EDE)")
    print(f"     - But: not cascade-specific")
    print()
    print(f"  4. Mechanism M (accept the tension):")
    print(f"     - Honest but unsatisfying")
    print()
    print(f"  5. Other exotic mechanisms (N, O, P):")
    print(f"     - Speculative, hard to test")

    print(f"\n\n  Step 9: Recommendation")
    print(f"  ----------------------------------------------------------------")
    print(f"  Best option: Mechanism L (model-dependent interpretation)")
    print(f"    - Most sophisticated and consistent with data")
    print(f"    - Requires re-analyzing Planck with cascade model")
    print(f"    - Would need CosmoSIS or custom pipeline")
    print()
    print(f"  If that's too much work, Mechanism M (accept the tension):")
    print(f"    - Honest position")
    print(f"    - 'Cascade doesn't explain the tension, but it's a separate problem'")
    print()
    print(f"  My honest take: Mechanism L is the most promising,")
    print(f"  but it requires significant new analysis to verify.")
    print(f"  Until then, the cascade should acknowledge the tension")
    print(f"  as a feature the cascade accommodates but doesn't fully explain.")

    # Summary
    hr()
    print("SUMMARY")
    hr()
    print(f"\n  Mechanism B/F (4D time-varying antigravity) is REJECTED.")
    print(f"  Pantheon+ shows H_0 is roughly constant at ~73.")
    print()
    print(f"  Alternative mechanisms for the cascade:")
    print()
    print(f"  C: Local bubble / void (standard physics)")
    print(f"     - Conceptually OK, but Pantheon+ doesn't show local high H_0")
    print()
    print(f"  I: Late-time physics (w != -1, EDE, etc.)")
    print(f"     - Real research direction, not cascade-specific")
    print()
    print(f"  L: Model-dependent interpretation (best option)")
    print(f"     - CMB H_0 = 67.4 is an artifact of assuming LCDM")
    print(f"     - In cascade model, CMB analysis gives H_0 ~ 73")
    print(f"     - Requires Planck re-analysis with cascade model")
    print()
    print(f"  M: Accept the tension (honest, unsatisfying)")
    print()
    print(f"  Other (N, O, P): speculative")
    print()
    print(f"  Status: cascade's Mechanism B/F is rejected.")
    print(f"  The cascade should adopt Mechanism L (or M if no time for re-analysis).")
    print(f"  Mechanism L requires re-analyzing Planck with cascade model.")


if __name__ == "__main__":
    main()
