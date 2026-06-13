#!/usr/bin/env python3
"""
Task 3 (from todos): 1D universe predictions

The cascade applies at every level. We've analyzed 3+1D extensively
and developed some 2D universe predictions. But the cascade continues
to 1D universes, created by energetic events in 2D universes.

This script:
  1. Establishes the 1D universe's properties
  2. Computes 1D universe lifetimes, energies, and effects
  3. Asks: what are the *observable* consequences in our 3+1D world?
  4. Identifies what's a *novel prediction* (not derivable from 3+1D alone)

Key insight: 1D universes are CREATED by 2D energetic events. They are
CASCADE-LEVEL-GRANDCHILDREN of our universe (2D child of 3+1D has a
1D grandchild when it has an energetic event). But the 1D universe's
own dynamics could in principle be observable.
"""

import math
import sys
sys.path.insert(0, ".")
sys.path.insert(0, "calculations")

from cascade_model import (
    Constants, CascadeParams, GrowthFactorCalculator,
    our_3plus1d_universe, simulate_galaxy_events,
    supernova_universe, lhc_collision_universe,
)


def hr(ch="="):
    print()
    print(ch * 78)
    print(ch * 78)


def main():
    hr()
    print("TASK 3: 1D UNIVERSE PREDICTIONS")
    hr()

    print(f"\n  Step 1: Establishing 1D universe properties")
    print(f"  ----------------------------------------------------------------")
    print(f"  Per cascade: every energetic event creates a child universe")
    print(f"  at the next cascade level. So:")
    print(f"    3+1D event -> 2D universe (already analyzed)")
    print(f"    2D event   -> 1D universe (this analysis)")
    print(f"    1D event   -> 0D universe (probably negligible)")
    print()
    print(f"  The 1D universe's 'spatial' extent is set by the 2D event's")
    print(f"  spatial extent. For a SN in 2D (~ 1e10 m photosphere):")
    print(f"    1D universe extent in 2D's frame: 1e10 m")
    print(f"    1D universe lifetime in 2D's frame: 1e10 / c = 33 s")
    print(f"    1D universe lifetime in OUR frame: ? (need cascade time-dilation)")
    print()
    print(f"  Per dimensional time-dilation (per cascade §2.2):")
    print(f"    tau_1D_in_2D_frame = l_event / c")
    print(f"    tau_1D_in_3plus1D_frame = ?")

    # Calculate 1D universe lifetimes
    print(f"\n\n  Step 2: 1D universe lifetimes")
    print(f"  ----------------------------------------------------------------")
    print(f"  Per dimensional time-dilation, tau_N+1_in_N_frame = l_event / c.")
    print(f"  But what's the relationship between tau_1D_in_2D and tau_1D_in_3plus1D?")
    print()
    print(f"  If 2D's frame is itself in 3+1D, and the 2D universe's 'time' axis")
    print(f"  projects back to 3+1D as... spatial? temporal? it's not specified.")
    print()
    print(f"  Let me assume the simplest: tau_1D_in_3plus1D = tau_1D_in_2D (no extra dilation)")
    print(f"  This means 1D universes are very short-lived in our frame too.")
    print()
    print(f"  {'2D event':<25} {'l_2D_event (m)':>15} {'tau_1D in 2D':>15} {'tau_1D in 3+1D':>15}")
    print(f"  {'-'*25} {'-'*15} {'-'*15} {'-'*15}")

    events_2D = [
        ("LHC 2D collision", 1e-15),
        ("Cosmic ray 2D", 10),
        ("BNS 2D merger", 3e4),
        ("SN 2D (Type II)", 1e10),
        ("AGN 2D outburst", 1.2e10),
    ]
    for name, l in events_2D:
        tau_2D = l / Constants.c
        # Assume no extra dilation: tau_3plus1D = tau_2D
        print(f"  {name:<25} {l:>15.3e} {tau_2D:>15.3e} {tau_2D:>15.3e}")

    # 1D universe creation rate
    print(f"\n\n  Step 3: 1D universe creation rate in our universe")
    print(f"  ----------------------------------------------------------------")
    print(f"  A 1D universe is created when a 2D universe has an energetic event.")
    print(f"  In our 3+1D universe, the 2D universes are created by OUR events.")
    print(f"  So a 1D universe is created by an event in a 2D universe,")
    print(f"  which is itself created by an event in our 3+1D universe.")
    print()
    print(f"  Cascade: 3+1D event -> 2D universe -> (2D event) -> 1D universe")
    print(f"  This is a 2-step cascade.")
    print()
    print(f"  Rate: For each 2D universe with E_2D event energy, the 2D")
    print(f"  universe has its own energetic events (per 2D physics), and")
    print(f"  each of those creates a 1D universe.")
    print()
    print(f"  But: 2D physics is *abstract* (per cascade_model.py).")
    print(f"  We don't have a 2D SM. So 1D universe rate is *unspecified*.")

    # 1D universe mass-energy
    print(f"\n\n  Step 4: 1D universe mass-energy")
    print(f"  ----------------------------------------------------------------")
    print(f"  A 1D universe is created by a 2D energetic event with E_2D energy.")
    print(f"  Per cascade universal-split: M_1D_peak = 20 * G_1D * M_2D_event")
    print(f"  where G_1D is the 1D universe's growth factor (analogous to G=1e8 for 2D).")
    print()
    print(f"  If G_1D ~ G_2D ~ 1e8 (similar physical mechanism):")
    print(f"    M_1D_peak = 20 * 1e8 * M_2D_event = 2e9 * M_2D_event")
    print()
    print(f"  But: 1D universes are *children* of 2D universes. They don't project")
    print(f"  back to 3+1D directly (the cascade only goes 1 level up).")
    print(f"  They are *internal* to 2D universes.")
    print()
    print(f"  So 1D universes are OBSERVABLE only insofar as they affect 2D physics.")
    print(f"  But 2D physics is also abstract (per cascade_model.py).")
    print(f"  So 1D universes are *doubly abstract* in our 3+1D frame.")

    # What's observable in our 3+1D frame
    print(f"\n\n  Step 5: What's observable in our 3+1D frame?")
    print(f"  ----------------------------------------------------------------")
    print(f"  1D universes are INTERNAL to 2D universes.")
    print(f"  2D universes are CHILDREN of our 3+1D universe (per §2.3).")
    print(f"  2D universes' back-projection to 3+1D is our dark matter (per §2.5).")
    print()
    print(f"  The 1D universes DON'T directly project back to 3+1D.")
    print(f"  They contribute to 2D universe's *internal* dark energy (per cascade).")
    print(f"  That 2D DE is INTERNAL to 2D (doesn't project back to 3+1D).")
    print()
    print(f"  So 1D universes have NO direct observable consequence in 3+1D!")
    print(f"  They're a feature of the 2D universe's internal dynamics.")

    # 1D universes as a *novel prediction* of the cascade
    print(f"\n\n  Step 6: 1D universes as a *novel prediction* of the cascade")
    print(f"  ----------------------------------------------------------------")
    print(f"  In the cascade framework, the existence of 1D universes is")
    print(f"  a *consequence* of the cascade's scale-invariance principle.")
    print(f"  If the cascade extends to lower levels (which it must, per the")
    print(f"  scale-invariance postulate), then 1D universes exist.")
    print()
    print(f"  This is a *novel* prediction, but it's not directly *testable*")
    print(f"  in our 3+1D frame (since 1D universes don't project back to 3+1D).")
    print()
    print(f"  Could 1D universes be testable?")
    print(f"  - If 1D universes affect 2D universe dynamics (e.g., dark energy,")
    print(f"    matter, or expansion), and 2D universes' BACK-PROJECTION to 3+1D")
    print(f"    depends on their internal state, then 1D universes could")
    print(f"    indirectly affect the 3+1D dark matter density.")
    print()
    print(f"  But: this is a 2nd-order effect, very small.")
    print(f"  1D universe energy / 2D universe energy ~ 1e-9 (per growth factor)")
    print(f"  So 1D -> 2D contribution to 3+1D dark matter ~ 1e-9 * 1e-9 ~ 1e-18")
    print(f"  This is well below detection threshold.")

    # What about other levels?
    print(f"\n\n  Step 7: What about even lower levels (0D, -1D, ...)?")
    print(f"  ----------------------------------------------------------------")
    print(f"  The cascade extends to:")
    print(f"    3+1D (us) -> 2D (children) -> 1D (grandchildren) -> 0D (-1D, etc.)")
    print(f"  Per the cascade, each level has its own:")
    print(f"    - Energetic events (creating child universes)")
    print(f"    - Dark matter (back-projection of child universes)")
    print(f"    - Dark energy (parent's antigravity projection)")
    print()
    print(f"  The cascade is *fractal* in this sense.")
    print(f"  Each level has a 5/27/68 split (per the universal-split postulate).")
    print()
    print(f"  But: at the lower levels, the energy scales are tiny.")
    print(f"  0D universes (created by 1D events) are at most ~1e-9 of 1D universe")
    print(f"  energy, or 1e-18 of 2D universe energy, or 1e-27 of 3+1D energy.")
    print(f"  These are unobservably small.")

    # What's the cascade's *observable* signature of the lower levels?
    print(f"\n\n  Step 8: Observable signature of the cascade's lower levels")
    print(f"  ----------------------------------------------------------------")
    print(f"  The cascade's lower levels (1D, 0D, ...) are not directly observable.")
    print(f"  But they contribute INDIRECTLY to our 3+1D observations:")
    print()
    print(f"  1. 1D universes affect 2D universe's internal DE.")
    print(f"     This changes the 2D universe's '32% attractive' back-projection,")
    print(f"     which is our dark matter.")
    print(f"     Effect: ~1e-18 fractional change in our DM density.")
    print(f"     Observable: NO (well below detection).")
    print()
    print(f"  2. 0D universes affect 1D universe's internal DE.")
    print(f"     This affects 1D -> 2D -> 3+1D chain.")
    print(f"     Effect: even smaller (~1e-36 fractional change).")
    print(f"     Observable: NO.")
    print()
    print(f"  3. The cascade as a *whole* is a self-consistent framework.")
    print(f"     Its predictions (DM density, DE density, hierarchy, RAR)")
    print(f"     are derivable from the cascade's structure.")
    print(f"     This is the *main* observable consequence.")
    print()
    print(f"  4. NEW: 1D universes might be detectable through their")
    print(f"     contribution to the cascade's *vacuum energy* (DE).")
    print(f"     The cascade's DE is the cumulative antigravity from the")
    print(f"     4D event. 1D universes don't contribute directly, but their")
    print(f"     existence is *consistent* with the cascade's structure.")
    print(f"     Observable: NO direct signature.")

    # Summary
    hr()
    print("SUMMARY")
    hr()
    print(f"\n  1D universe properties (per cascade):")
    print(f"    - Created by energetic events in 2D universes")
    print(f"    - Lifetime: 33 s for SN-scale 2D events (in 2D's frame)")
    print(f"    - Mass-energy: 2e9 * M_2D_event at peak")
    print(f"    - Spatial: 1D (one spatial + one time dimension)")
    print()
    print(f"  Observable consequences in 3+1D:")
    print(f"    - 1D universes are INTERNAL to 2D universes")
    print(f"    - They don't project back to 3+1D directly")
    print(f"    - Their effect on 2D universe dynamics is ~1e-18 level")
    print(f"    - NOT directly observable in 3+1D")
    print()
    print(f"  Status: 1D universes are a *theoretical consequence* of the cascade,")
    print(f"  not a *testable prediction*. They are part of the cascade's")
    print(f"  structure but not directly observable in our 3+1D frame.")
    print()
    print(f"  What this means for the paper:")
    print(f"  The cascade's 5/27/68 split and other predictions are robust to")
    print(f"  the existence (or non-existence) of 1D universes, since 1D")
    print(f"  universes don't directly project back to 3+1D.")
    print()
    print(f"  The *consistency* of the cascade (1D universes fit the framework)")
    print(f"  is a *theoretical* asset, not an *observational* one.")
    print()
    print(f"  This is honest: the cascade's lower levels (1D, 0D, etc.) are")
    print(f"  part of its internal consistency, not testable predictions.")
    print(f"  We acknowledge this in the paper.")

    # Check 1D universe creation rate from our 3+1D perspective
    print(f"\n\n  Step 9: 1D universe creation rate in our 3+1D frame")
    print(f"  ----------------------------------------------------------------")
    galaxy = our_3plus1d_universe()
    result = simulate_galaxy_events(galaxy, sn_count=1e8, stellar_events=1e30, lhc_count=1e15)
    print(f"  In a typical galaxy over 13.8 Gyr:")
    print(f"    SN: {result['sn_count']:.0e}")
    print(f"    Stellar events: {result['stellar_events']:.0e}")
    print(f"    LHC-scale collisions: {result['lhc_count']:.0e}")
    print(f"    SN total energy: {result['sn_total_E']:.3e} J")
    print(f"    Stellar total energy: {result['stellar_total_E']:.3e} J")
    print(f"    LHC total energy: {result['lhc_total_E']:.3e} J")
    print(f"    DM back-projected to 3+1D: {result['total_cumulative_E_3plus1D']:.3e} J")
    print()
    print(f"  1D universes per galaxy (cascade down):")
    print(f"    Each 2D universe has its own energetic events,")
    print(f"    each creating a 1D universe.")
    print(f"    Number of 1D universes ~ 2D events in 2D ~ ???")
    print(f"    (requires specifying 2D physics, which is abstract)")
    print()
    print(f"  Even if 2D events are ~equivalent to 3+1D events:")
    print(f"    1D universes per galaxy ~ 1e8 SNe * (2D events per 2D SN universe)")
    print(f"    ~ 1e8 * 1e8 = 1e16 1D universes per galaxy")
    print()
    print(f"  But these are all INTERNAL to 2D universes, not observable in 3+1D.")


if __name__ == "__main__":
    main()
