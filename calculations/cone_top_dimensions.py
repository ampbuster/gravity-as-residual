#!/usr/bin/env python3
"""
Why is 5D the top? Why not 6D, 7D, ...?

User's question: if 5D exists, why not 6D, 7D, etc.?

The cascade's cone-shape: 32/68 universal at every level.
Going UP the cone: each level has 3.125x more total energy than below.

If we extend up indefinitely, top has exponentially more energy.
This is a runaway. Where does it stop?

This script:
1. Simulates cones with different D_top (4, 5, 6, 7, ..., 11)
2. Computes energy at each level
3. Tries to find a derivation for D_top from cascade principles
4. Honest: D_top is a choice, not derivable

Possible derivations:
1. Energy bound: top's energy <= some limit (Planck? cosmological?)
2. Dimensional bound: D_top <= 11 (M-theory)
3. Observational: smallest D_top that explains observation = 4
4. Parsimony: D_top = 4 (Cone 1)
5. Self-consistency: D_top where 32/68 split breaks down
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


def simulate_top(top_dim, E_3plus1D=2.7e71):
    """
    Simulate a cone with top dimension = top_dim.
    
    Returns: dict of level -> (E_total, E_energetic, E_vacuum)
    """
    results = {}
    E_top = E_3plus1D * (1/0.32) ** (top_dim - 4)  # E at top_dim level
    results[f"{top_dim}D"] = E_top
    
    for d in range(top_dim - 1, 2, -1):
        # d-dimensional level has E = E_top * 0.32^(top_dim - d)
        E_d = E_top * (0.32) ** (top_dim - d)
        results[f"{d}D"] = E_d
    
    return results


def main():
    hr()
    print("WHY IS 5D THE TOP? WHY NOT 6D, 7D, ...?")
    hr()

    print(f"\n  Step 1: Recall cone-shape 32/68 universal")
    print(f"  ----------------------------------------------------------------")
    print(f"  At each level: 32% energetic, 68% vacuum.")
    print(f"  Going UP: each level has 3.125x more total energy than below.")
    print()
    print(f"  For 3+1D's E_3plus1D = 2.7e71 J (observed):")
    
    rho_c = 8.5e-27
    c = Constants.c
    R_observable = 4.4e26
    V_observable = (4/3) * math.pi * R_observable**3
    E_3plus1D = rho_c * c**2 * V_observable
    print(f"    E_3plus1D = {E_3plus1D:.3e} J")
    print()
    print(f"  Going UP the cone (each level is 3.125x more energy):")
    print(f"    4D: {E_3plus1D / 0.32:.3e} J")
    print(f"    5D: {E_3plus1D / 0.32**2:.3e} J")
    print(f"    6D: {E_3plus1D / 0.32**3:.3e} J")
    print(f"    7D: {E_3plus1D / 0.32**4:.3e} J")
    print(f"    8D: {E_3plus1D / 0.32**5:.3e} J")
    print(f"    9D: {E_3plus1D / 0.32**6:.3e} J")
    print(f"    10D: {E_3plus1D / 0.32**7:.3e} J")
    print(f"    11D: {E_3plus1D / 0.32**8:.3e} J")
    print()
    print(f"  Each level up multiplies energy by 3.125. Runaway!")

    print(f"\n\n  Step 2: What bounds D_top?")
    print(f"  ----------------------------------------------------------------")
    print(f"  Several possible bounds:")
    print()
    print(f"  Bound 1: Energy limit (Planck energy)")
    E_Pl = 1.96e9  # J (Planck energy)
    print(f"    Planck energy: E_Pl ~ {E_Pl:.2e} J")
    print(f"    For 3+1D's E = {E_3plus1D:.3e} J, top's E = E_3plus1D * 3.125^(D_top-4)")
    print(f"    For top's E to equal E_Pl: 3.125^(D_top-4) = E_Pl / E_3plus1D")
    ratio = E_Pl / E_3plus1D
    print(f"    = {ratio:.3e}")
    if ratio > 0:
        D_top_Planck = 4 + math.log(ratio) / math.log(3.125)
        print(f"    D_top = 4 + log({ratio:.2e}) / log(3.125) = {D_top_Planck:.2f}")
        print(f"    But D_top must be an integer! Planck bound is meaningless for integer dims.")
    print()
    print(f"  Bound 2: Cosmological energy limit (total energy in observable universe)")
    print(f"    E_cosmic ~ {E_3plus1D:.2e} J (this is the total!)")
    print(f"    Top can't exceed this, so D_top ~ 4 (no extension)")
    print()
    print(f"  Bound 3: Dimensional limit (M-theory: 11D max)")
    print(f"    M-theory: D <= 11 is well-defined; D > 11 is problematic")
    print(f"    So D_top could be anywhere from 4 to 11")
    print()
    print(f"  Bound 4: Just postulate (cascade's choice)")
    print(f"    The cascade chooses D_top = 4 (Cone 1)")
    print(f"    or D_top = 5 (Cone 2)")
    print(f"    These are choices, not derivations")

    print(f"\n\n  Step 3: Simulating different D_top values")
    print(f"  ----------------------------------------------------------------")
    print(f"  For each D_top, what is the cone's energy at the top?")
    print()
    print(f"  {'D_top':>6} | {'E_top (J)':>15} | {'Comment'}")
    print(f"  {'-'*6} | {'-'*15} | {'-'*50}")
    
    for D_top in [4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20]:
        E_top = E_3plus1D / 0.32 ** (D_top - 4)
        if D_top == 4:
            comment = "Cone 1 (cascade's choice, parsimonious)"
        elif D_top == 5:
            comment = "Cone 2 (5D above 4D, complete)"
        elif D_top <= 11:
            comment = f"Cone with {D_top}D at top (M-theory allowed)"
        else:
            comment = f"Cone with {D_top}D at top (M-theory violation?)"
        print(f"  {D_top:>6} | {E_top:>15.3e} | {comment}")

    print(f"\n  As D_top increases, E_top grows exponentially.")
    print(f"  At D_top = 11 (M-theory limit): E_top ~ {E_3plus1D / 0.32**7:.2e} J")
    print(f"  At D_top = 20: E_top ~ {E_3plus1D / 0.32**16:.2e} J")
    print(f"  At D_top -> infinity: E_top -> infinity")

    print(f"\n\n  Step 4: What determines D_top in the cascade?")
    print(f"  ----------------------------------------------------------------")
    print(f"  The cascade doesn't uniquely determine D_top. It's a CHOICE.")
    print()
    print(f"  Possible derivations:")
    print()
    print(f"  A) PARSIMONY: smallest D_top that explains observation = 4")
    print(f"     - Cone 1 (D_top = 4) is preferred")
    print()
    print(f"  B) COMPLETENESS: every level has a parent DE source")
    print(f"     - In Cone 1, 4D's DE has no parent source")
    print(f"     - In Cone 2 (D_top = 5), 4D's DE = 5D's antigravity (with source)")
    print(f"     - Symmetry argues for D_top >= 5 (so 4D has DE source)")
    print()
    print(f"  C) SYMMETRY: if 3+1D is sandwiched (has parent 4D and children 2D),")
    print(f"     maybe 4D should be sandwiched too (has parent 5D and children 3+1D)")
    print(f"     - D_top = 5 makes 4D sandwiched (like 3+1D)")
    print()
    print(f"  D) PARALLEL STRUCTURE: if 3+1D has both parent and children,")
    print(f"     maybe every level should have both. This requires INFINITE cone")
    print(f"     (every level has parent and children). But cone terminates.")
    print(f"     So D_top is just the top, but structure is asymmetric.")
    print()
    print(f"  E) JUST POSTULATE: the cascade chooses D_top = 4 (or 5) as a postulate")
    print(f"     - Not derivable, just chosen")

    print(f"\n\n  Step 5: Why might D_top = 4 (Cone 1) be preferred?")
    print(f"  ----------------------------------------------------------------")
    print(f"  Cone 1 advantages:")
    print(f"    1. PARSIMONY: 1 parameter (depth=2)")
    print(f"    2. SIMPLICITY: 4D event is the unique parent of our universe")
    print(f"    3. CMB INFLATION: 4D event is the 'Big Bang' of our universe")
    print(f"    4. NO ADDITIONAL STRUCTURE: just 3+1D, 2D, and 4D event")
    print()
    print(f"  Cone 1 disadvantages:")
    print(f"    1. 4D's DE has no source (just '4D's own vacuum')")
    print(f"    2. Asymmetric structure (only 3+1D has both parent and children)")
    print()
    print(f"  Cone 1 is preferred if:")
    print(f"    - The cascade is minimal (Occam's razor)")
    print(f"    - 4D event is a 'unique' event (not part of a higher-D hierarchy)")

    print(f"\n\n  Step 6: Why might D_top > 4 be preferred?")
    print(f"  ----------------------------------------------------------------")
    print(f"  Cone 2 (D_top = 5) advantages:")
    print(f"    1. COMPLETENESS: every level has a parent DE source")
    print(f"    2. SYMMETRY: 4D is sandwiched (parent 5D, children 3+1D) like 3+1D")
    print(f"    3. BETTER EXPLANATION: 4D's DE = 5D's antigravity (more concrete)")
    print()
    print(f"  Cone 2 disadvantages:")
    print(f"    1. LESS PARSIMONIOUS: 2 parameters (depth=3, 5D exists)")
    print(f"    2. 5D physics unspecified")
    print()
    print(f"  Higher D_top advantages (Cone X, X > 5):")
    print(f"    - Even more 'complete' (more levels have parent DE sources)")
    print(f"    - But: more parameters, more unspecified physics")
    print()
    print(f"  Higher D_top is preferred if:")
    print(f"    - 'Completeness' is valued over parsimony")
    print(f"    - The cascade is part of a higher-D hierarchy (e.g., string theory)")

    print(f"\n\n  Step 7: Could D_top be DETERMINED by some cascade principle?")
    print(f"  ----------------------------------------------------------------")
    print(f"  Let me try: D_top = some function of dimensional-analysis quantities")
    print()
    print(f"  In the cascade, the 32/68 split is universal. So D_top is not")
    print(f"  determined by the split itself (it's the same at every level).")
    print()
    print(f"  What if D_top is determined by the requirement that the top's")
    print(f"  'physics' is well-defined?")
    print()
    print(f"  In standard physics:")
    print(f"    - D = 4: GR is well-defined (our universe + time)")
    print(f"    - D = 5, 6, ..., 11: GR-like physics is well-defined (extra spatial dims)")
    print(f"    - D = 12+: physics is exotic (problems with gauge couplings, etc.)")
    print()
    print(f"  So D_top could be anywhere from 4 to 11.")
    print(f"  The cascade's choice of D_top = 4 is one possibility.")
    print(f"  D_top = 5, 6, ..., 11 are also possible.")
    print()
    print(f"  Status: D_top is a free parameter of the cascade (not derivable).")
    print(f"  Different choices give different (but observationally equivalent)")
    print(f"  predictions for our 3+1D universe.")

    print(f"\n\n  Step 8: What if D_top is 11 (M-theory)?")
    print(f"  ----------------------------------------------------------------")
    print(f"  M-theory: 11D spacetime, 10 spatial + 1 time")
    print(f"  M-theory is the leading candidate for 'theory of everything'")
    print(f"    - Unifies gravity + other forces")
    print(f"    - Has 11D as the natural limit")
    print()
    print(f"  If the cascade's D_top = 11, then:")
    print(f"    - 11D -> 10D -> 9D -> ... -> 4D -> 3+1D -> 2D (cone)")
    print(f"    - That's 10 levels (11D down to 2D)")
    print(f"    - Cone depth = 9 (10 - 1)")
    print()
    print(f"  M-theory has extra structure: branes, strings, etc.")
    print(f"  The cascade's cone would need to incorporate this.")
    print()
    print(f"  But: M-theory's 11D is not specifically the cascade's 'cone top'.")
    print(f"  M-theory is a candidate for the cascade's higher levels,")
    print(f"  but the cascade doesn't require it.")
    print()
    print(f"  Status: D_top = 11 (M-theory) is a possible extension, but")
    print(f"  the cascade doesn't uniquely select it.")

    print(f"\n\n  Step 9: Honest answer")
    print(f"  ----------------------------------------------------------------")
    print(f"  The cascade doesn't uniquely determine D_top. It's a CHOICE.")
    print()
    print(f"  Choices:")
    print(f"    D_top = 4: Cone 1 (parsimonious, current cascade)")
    print(f"    D_top = 5: Cone 2 (5D above 4D, complete)")
    print(f"    D_top = 6, 7, ..., 11: Cone X (M-theory allowed)")
    print(f"    D_top = infinity: fractal (NOT cone, contradicts cone-shape)")
    print()
    print(f"  The cascade's principled derivation (commit 76) prefers D_top = 4")
    print(f"  (parsimony). But the user's intuition (D_top = 5 or higher)")
    print(f"  has merit (completeness, symmetry).")
    print()
    print(f"  Status: D_top is a free parameter of the cascade.")
    print(f"  Different choices give observationally equivalent predictions.")
    print(f"  Choice is theoretical preference (parsimony vs completeness).")

    # Summary
    hr()
    print("SUMMARY")
    hr()
    print(f"\n  User's question: why is 5D the top? why not 6D, 7D, ...?")
    print()
    print(f"  Honest answer: 5D is NOT necessarily the top. The cascade")
    print(f"  doesn't uniquely determine D_top. It could be 4, 5, 6, ..., 11,")
    print(f"  or even higher.")
    print()
    print(f"  Each level up multiplies total energy by 3.125 (runaway).")
    print(f"  Without an energy bound, the cone could extend indefinitely.")
    print()
    print(f"  Possible bounds:")
    print(f"    - Energy limit: top's energy can't exceed some limit")
    print(f"    - Dimensional limit: M-theory caps at 11D")
    print(f"    - Parsimony: smallest D_top that explains observation = 4")
    print(f"    - Completeness: largest D_top that's consistent with physics")
    print()
    print(f"  The cascade's choice: D_top = 4 (Cone 1, parsimonious)")
    print(f"  But: D_top = 5, 6, ..., 11 are also valid (just less parsimonious)")
    print()
    print(f"  The choice is a theoretical preference, not derivable from")
    print(f"  the cascade alone. The cascade derives 32/68 at every level,")
    print(f"  but not where the cone terminates (D_top).")
    print()
    print(f"  Status: D_top is a free parameter. Different D_top values give")
    print(f"  observationally equivalent 3+1D predictions.")


if __name__ == "__main__":
    main()
