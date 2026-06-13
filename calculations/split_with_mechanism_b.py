#!/usr/bin/env python3
"""
Task 10: 5/27/68 revisited with Mechanism B/F as motivation

The 5/27/68 split is currently a *fit* (empirical), not a *derivation*.
Per Monte Carlo test (commit 58): 0.5% match is NOT statistically significant.

But: maybe Mechanism B/F (4D event temporal structure) provides a motivation
for why the split is what it is.

Hypothesis: The 5/27/68 split corresponds to a *snapshot* of the 4D event's
dynamics. Specifically:
  - 5% ordinary matter: created during 4D event's *burst* phase
  - 27% dark matter: created during 4D event's *extended* phase
  - 68% dark energy: the 4D event's *current* antigravity output

If the 4D event is a "born + persistent" system, with a brief birth and
long persistence, the 5/27 split could be a "frozen" record of the 4D
event's history. The 68% is the *current* state, while 5/27 are historical.

This script explores whether Mechanism B/F gives the 5/27/68 split a
*motivating* derivation, even if the specific numbers can't be derived.
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
    print("TASK 10: 5/27/68 REVISITED WITH MECHANISM B/F AS MOTIVATION")
    hr()

    print(f"\n  Step 1: Recall 5/27/68 split current status")
    print(f"  ----------------------------------------------------------------")
    print(f"  The cascade's mass-energy budget (5/27/68):")
    print(f"    Omega_o = 0.05 (ordinary matter)")
    print(f"    Omega_DM = 0.27 (dark matter)")
    print(f"    Omega_DE = 0.68 (dark energy)")
    print(f"  Observed: 0.0493, 0.265, 0.686 (Planck 2018)")
    print()
    print(f"  Current best-fit formula (1/20, 3/11, residual):")
    print(f"    Omega_o = 1/(N*(N+1)) with N=4: 1/20 = 0.05")
    print(f"    Omega_DM = N_spatial/(2N+N_spatial) with N_spatial=3: 3/11 = 0.2727")
    print(f"    Omega_DE = 1 - Omega_o - Omega_DM = 0.6773")
    print()
    print(f"  Status: FIT (matches to 0.5%) but NOT statistically significant")
    print(f"          (Monte Carlo test, 1M random formulas: ~92% p-value)")

    print(f"\n\n  Step 2: Mechanism B/F (4D event temporal structure)")
    print(f"  ----------------------------------------------------------------")
    print(f"  4D event's antigravity output is not constant in 4D time.")
    print(f"  Currently ~8% above time-averaged (per local H_0 = 73 vs CMB 67.4).")
    print()
    print(f"  Implication: the 5/27/68 split is a *snapshot* in 4D time.")
    print(f"  As the 4D event evolves, the split could evolve.")

    # Try: 5/27/68 is a snapshot of a 4D event that has been evolving
    print(f"\n\n  Step 3: 5/27/68 as a snapshot of 4D event evolution")
    print(f"  ----------------------------------------------------------------")
    print(f"  Hypothesis: the 4D event has three phases:")
    print(f"    Phase 1 (early): high matter creation, low DM, no DE")
    print(f"      -> creates ordinary matter in our 3+1D universe")
    print(f"    Phase 2 (middle): peak DM creation, some matter, no DE")
    print(f"      -> creates dark matter in our 3+1D universe")
    print(f"    Phase 3 (current): low creation, dominant DE")
    print(f"      -> dark energy dominates the energy budget")
    print()
    print(f"  If the 4D event's 'energy budget' is divided as 5% Phase 1,")
    print(f"  27% Phase 2, 68% Phase 3 (currently), then:")
    print()
    print(f"  Phase 3 fraction (current 4D state) = Omega_DE = 68%")
    print(f"  Phase 2 fraction (history, fixed) = Omega_DM = 27%")
    print(f"  Phase 1 fraction (history, fixed) = Omega_o = 5%")
    print()
    print(f"  This means: as 4D time progresses, Omega_DE grows,")
    print(f"  while Omega_o and Omega_DM stay fixed (they were created in")
    print(f"  past phases and don't change).")

    # Calculate when 4D event was at different phases
    print(f"\n\n  Step 4: 4D event timeline based on 5/27/68")
    print(f"  ----------------------------------------------------------------")
    print(f"  Currently Omega_DE = 68% (peak, post Phase 3 transition)")
    print(f"  The 4D event is in late Phase 2 / early Phase 3")
    print()
    print(f"  Wait, that's backwards. Let me reconsider.")
    print()
    print(f"  Actually: the 5/27/68 split is the current state of the universe.")
    print(f"  It reflects:")
    print(f"    Omega_o = 5%: ordinary matter created over 13.8 Gyr")
    print(f"    Omega_DM = 27%: dark matter created over 13.8 Gyr")
    print(f"    Omega_DE = 68%: dark energy, the 4D event's current antigravity")
    print()
    print(f"  In Mechanism B/F: 4D event's antigravity is currently ~8% above")
    print(f"  average. If 'average' is the historical antigravity, then current")
    print(f"  DE density is 8% above historical.")
    print()
    print(f"  At earlier times, the 4D event's antigravity was lower, so DE")
    print(f"  was lower. The 5% matter and 27% DM were created in earlier times,")
    print(f"  so they're fixed (those matter particles don't change).")
    print()
    print(f"  But: the *proportions* change with time.")
    print(f"  In the early universe (high z), DE was lower fraction of total.")

    # The evolving 5/27/68
    print(f"\n\n  Step 5: Evolving 5/27/68 split")
    print(f"  ----------------------------------------------------------------")
    print(f"  Let t=0 be the 4D event's beginning. At t=t_now (now),")
    print(f"  Omega_o = 0.05, Omega_DM = 0.27, Omega_DE = 0.68.")
    print()
    print(f"  Matter and DM are *created* during cosmic history, so their")
    print(f"  *absolute* energy increases with t. But once created, they dilute")
    print(f"  as the universe expands (a^-3).")
    print()
    print(f"  DE is a *vacuum energy*, so its density stays constant.")
    print(f"  As the universe expands, DE becomes dominant.")
    print()
    print(f"  In the cascade, the *initial* 5/27/68 split might have been")
    print(f"  very different. For example:")
    print(f"    At t ~ 1 Gyr: Omega_o ~ 0.5, Omega_DM ~ 0.5, Omega_DE ~ 0")
    print(f"    At t ~ 5 Gyr: Omega_o ~ 0.2, Omega_DM ~ 0.5, Omega_DE ~ 0.3")
    print(f"    At t ~ 13.8 Gyr: Omega_o ~ 0.05, Omega_DM ~ 0.27, Omega_DE ~ 0.68")
    print()
    print(f"  The transition from matter-dominated to DE-dominated happened at")
    print(f"  z ~ 0.5 (about 5 Gyr ago).")

    # Where does the 5/27/68 number itself come from?
    print(f"\n\n  Step 6: Where does the *specific* 5/27/68 number come from?")
    print(f"  ----------------------------------------------------------------")
    print(f"  Currently: 5/27/68 is empirical, fit to observation.")
    print()
    print(f"  Mechanism B/F motivation:")
    print(f"    - 5/27 are *ratios* between matter and DM (1:5.4)")
    print(f"    - 68 is the *current* DE fraction")
    print(f"    - The 5/27 ratio might be a consequence of the 4D event's")
    print(f"      *birth phase* dynamics: how it created matter vs DM")
    print()
    print(f"  But: the 5/27 ratio depends on the SPECIFIC 4D event.")
    print(f"  A different 4D event could have created 4/30/66 or 6/25/69.")
    print(f"  The cascade doesn't uniquely predict 5/27.")
    print()
    print(f"  What we DO predict: a *frozen* history of matter/DM creation,")
    print(f"  with DE being a *current* dynamic state.")

    # Why might 5/27 ratio be what it is?
    print(f"\n\n  Step 7: Why 5:27 = 1:5.4 ratio?")
    print(f"  ----------------------------------------------------------------")
    print(f"  In the cascade: 5% ordinary matter vs 27% dark matter.")
    print(f"  Per dimensional inversion: ordinary matter is what the 4D event")
    print(f"  *contains*, while dark matter is what 2D universes *contribute*.")
    print()
    print(f"  If 2D universes are *children* of 3+1D events, then the ratio")
    print(f"  of matter-to-DM depends on the *efficiency* of 3+1D -> 2D")
    print(f"  conversion. This is a *physical* parameter of our universe.")
    print()
    print(f"  Hypothesis: the 5:27 ratio reflects the *energy partition* in")
    print(f"  the 4D event's birth:")
    print(f"    - 4D event creates 3+1D universe with 'X' ordinary matter")
    print(f"    - 3+1D universe's events create 2D universes with 'Y' back-projected")
    print(f"    - Y/X ~ 5.4 (gives 5/27 ratio)")
    print()
    print(f"  But: the specific value 5.4 depends on the 4D event's details.")
    print(f"  It's not a *derivation* of the cascade.")
    print()
    print(f"  So: 5:27 ratio is a *parameter* of the cascade, not a *prediction*.")

    # What about the 68% DE?
    print(f"\n\n  Step 8: Why 68% DE?")
    print(f"  ----------------------------------------------------------------")
    print(f"  In Mechanism B/F, DE is the 4D event's *current* antigravity output.")
    print(f"  The 68% reflects the *cumulative* antigravity that has built up")
    print(f"  over 13.8 Gyr.")
    print()
    print(f"  If the 4D event has been 'ramping up' its antigravity over time,")
    print(f"  then 68% is the *current* value, and it will be different at")
    print(f"  other times.")
    print()
    print(f"  Specifically:")
    print(f"    Omega_DE(t) grows as the 4D event's antigravity grows")
    print(f"    Omega_o(t) and Omega_DM(t) are fixed at their 13.8 Gyr values")
    print(f"      (but their *proportions* of the total change)")
    print()
    print(f"  In the future, Omega_DE will continue to grow (Mechanism B/F).")
    print(f"  Omega_o and Omega_DM will continue to dilute.")
    print()
    print(f"  Eventually, Omega_DE -> 1, Omega_o and Omega_DM -> 0.")
    print(f"  This is consistent with the 'big chill' / 'heat death' scenario.")

    # What can we say NEW about the 5/27/68 from Mechanism B/F?
    print(f"\n\n  Step 9: NEW: Mechanism B/F implications for 5/27/68")
    print(f"  ----------------------------------------------------------------")
    print(f"  Before Mechanism B/F:")
    print(f"    5/27/68 was just an empirical split, fit to observation")
    print()
    print(f"  After Mechanism B/F:")
    print(f"    - 5/27 is a *frozen* historical record (matter + DM created in")
    print(f"      past 4D event phases)")
    print(f"    - 68 is a *current* dynamic state (4D event's antigravity now)")
    print(f"    - The 5:27 ratio is a parameter of the 4D event's birth")
    print(f"    - The 68% will evolve (grow) over time as the 4D event")
    print(f"      continues to ramp up its antigravity")
    print(f"    - In the future, Omega_DE will exceed 68%")
    print(f"    - In the past (z>0.5), Omega_DE was less than 68%")
    print()
    print(f"  New testable prediction:")
    print(f"    - The Hubble tension (H_0_local > H_0_CMB) is a CONSEQUENCE")
    print(f"      of Mechanism B/F")
    print(f"    - H_0(z) is *not constant* in the cascade (decreasing with z)")
    print(f"    - This can be tested with SNe data at z=0.5-1.0")
    print()
    print(f"  Status: Mechanism B/F doesn't DERIVE 5/27/68, but it does")
    print(f"  explain its TIME-DEPENDENCE (5:27 frozen, 68 current).")

    # Summary
    hr()
    print("SUMMARY")
    hr()
    print(f"\n  Mechanism B/F (4D event temporal structure) gives the 5/27/68")
    print(f"  split a NEW interpretation:")
    print(f"    5/27: *frozen* historical record of matter + DM creation")
    print(f"    68: *current* dynamic state (4D event's antigravity)")
    print()
    print(f"  What it does NOT do:")
    print(f"    - It does NOT derive the specific 5:27 ratio (still a parameter)")
    print(f"    - It does NOT derive the 68% value from first principles")
    print(f"    - 5/27/68 remains a *fit* (empirical), not a *derivation*")
    print()
    print(f"  What it DOES do:")
    print(f"    - Explain why 5+27 = 32% is *fixed* (historical creation)")
    print(f"    - Explain why 68% is *evolving* (current 4D state)")
    print(f"    - Connect the 5/27/68 split to the Hubble tension")
    print(f"    - Predict that 68% will grow with time")
    print(f"    - Predict that 5/27 proportions will dilute with time")
    print()
    print(f"  New testable prediction:")
    print(f"    - Omega_DE(z) at z=1 should be LESS than 68%")
    print(f"    - Combined with the H_0(z) prediction, this gives 2")
    print(f"      testable effects of Mechanism B/F on cosmological data.")
    print()
    print(f"  Status: 5/27/68 is still a *fit*, but Mechanism B/F gives it")
    print(f"  a *theoretical motivation* (3+1 universe is a snapshot of an")
    print(f"  evolving 4D event). This is a more sophisticated interpretation")
    print(f"  than the pure empirical fit.")


if __name__ == "__main__":
    main()
