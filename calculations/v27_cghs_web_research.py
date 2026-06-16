"""
v27_cghs_web_research.py
=========================

Web research result on CGHS-with-back-reaction and α = 1.29.

The cascade's §3.19 / §3.24 claimed that α = 1.29 falls within the
CGHS-with-back-reaction range [1, 3]. This script documents what
the web literature ACTUALLY says about CGHS-with-back-reaction scaling,
and concludes that the cascade's claim is OVERSTATED.

KEY FINDINGS FROM WEB RESEARCH (June 2026):

1. CGHS 2D black hole has Hawking temperature:
   T_H ~ (M_BH / λ_0)^{1/2} (square root, not linear)

2. 2D black hole lifetime: τ_BH ~ 4M (LINEAR scaling)
   - This is from the Frolov-Zelnikov / Strominger-Thorlacius analyses
   - NOT a power law with non-trivial exponent
   - This is a LINEAR scaling, τ ∝ M

3. RST model with back-reaction (Russo-Susskind-Thorlacius 1992):
   - Has a critical mass M_c
   - For M > M_c, BH forms and evaporates
   - For M < M_c, no BH forms (matter disperses)
   - The lifetime formula is τ ~ M (linear)

4. Various extensions (Bardeen-like, regular, etc.):
   - Modify the inner structure
   - Generally still τ ~ M
   - Power-law scaling τ ~ M^p is NOT a natural CGHS prediction

5. Search for "1.29" or "α = 1.29" in CGHS context:
   - No specific paper derives this value
   - The exponent depends on the model variant and regularization scheme
   - The "range [1, 3]" is a phenomenological observation, not a CGHS prediction

CONCLUSION:
The cascade's claim that α = 1.29 is "in the CGHS back-reaction range" is
OVERSTATED. The CGHS family of models gives LINEAR scaling τ ~ M (in 2D frame),
which is p = 1.0, not p = 1.29.

The cascade's democratic cosmology (§3.17) requires:
  τ_2D_proper = t_Pl,3 (CONSTANT in 2D frame, independent of E)

This is NOT a CGHS-with-back-reaction prediction. CGHS gives τ ∝ M,
which means τ_2D_proper depends on M_BH and hence on E.

The cascade's α = 1.29 emerges from:
  τ_2D_3+1D = γ × τ_2D_proper
  γ = (E/E_Pl,3)^1.29
  So τ_2D_3+1D = (E/E_Pl,3)^1.29 × t_Pl,3

But this requires a SPECIFIC projection-geometry relationship γ = (E/E_Pl)^1.29
which is NOT in the CGHS framework.

HONEST STATUS (v2.7.31+):
- α = 1.29 is a PHENOMENOLOGICAL fit to the SN lifetime calibration
- It is NOT derived from CGHS-with-back-reaction
- It is NOT derived from any established 2D dilaton gravity calculation
- A specific calculation yielding γ = (E/E_Pl)^1.29 is needed to close L9
- This is a research challenge, not a derivation
"""

import math
import json

# CGHS 2D black hole lifetime scaling
def cghs_lifetime(M_BH):
    """
    CGHS 2D black hole lifetime in 2D frame.
    Standard result: τ_BH ~ 4M (linear scaling, in Planck units).
    """
    return 4 * M_BH

# RST critical mass
def rst_critical_mass(eta_0):
    """
    RST model critical mass M_c above which BH forms.
    M_c = eta_0 / lambda_0 (in some normalization)
    """
    return eta_0  # simplified

# Print findings
print("=== §3.25: Web research on CGHS-with-back-reaction and α = 1.29 ===\n")

print("1. CGHS 2D black hole lifetime formula:")
print("   τ_BH ~ 4M_BH (LINEAR scaling, 2D frame)")
print("   This is the standard Frolov-Zelnikov result.")
print()

print("2. RST model with back-reaction:")
print("   Critical mass M_c above which BH forms")
print("   τ_BH ~ M_BH (linear) for M_BH > M_c")
print()

print("3. The cascade's claim:")
print("   α = 1.29 is in CGHS back-reaction range [1, 3]")
print()

print("4. Web research search for α = 1.29 in CGHS context:")
print("   No specific paper derives this value")
print("   The exponent depends on the model variant")
print()

print("5. Honest verdict:")
print("   The CGHS family gives p = 1.0 (linear), not p = 1.29")
print("   α = 1.29 is a phenomenological fit, not a CGHS prediction")
print("   L37 is now: 'α = 1.29 is phenomenological, not derived'")
print()

print("=== What the web research can NOT do ===\n")
print("Web research can:")
print("- Confirm what CGHS/RST does and doesn't predict")
print("- Find related 2D gravity models")
print("- Identify open research questions")
print()
print("Web research CANNOT:")
print("- Derive a new physical formula")
print("- Calculate γ_2D = (E/E_Pl)^1.29 from first principles")
print("- Solve the CGHS-with-back-reaction equations")
print()

print("=== Future work: what is needed to close L9 ===\n")
print("1. A specific 2D gravity model with:")
print("   - Back-reaction between matter and geometry")
print("   - A scaling relation τ_BH ~ M_BH^p with p ≈ 1.29")
print()
print("2. A geometric argument for:")
print("   - γ_2D = (E/E_Pl,3)^1.29")
print("   - This requires a specific projection-geometry relationship")
print()
print("3. A theoretical framework connecting:")
print("   - The cascade's 4D event → 3+1D brane → 2D universe projection")
print("   - The CGHS 2D dilaton gravity dynamics")
print()

print("=== Conclusion ===\n")
print("Web research CONFIRMS that α = 1.29 is NOT a natural CGHS prediction.")
print("The cascade is honest: α is a phenomenological fit to the SN calibration,")
print("and the derivation from first principles is an open research problem.")
print()
print("Status: L37 remains OPEN. The cascade's claim in §3.19 was OVERSTATED.")
print("The honest version (§3.25): α is phenomenological, not first-principles.")

results = {
    'web_research_finding': 'No CGHS-with-back-reaction paper gives α = 1.29',
    'cghs_lifetime_scaling': 'τ_BH ~ 4M (LINEAR, p = 1.0)',
    'cascade_claim_status': 'OVERSTATED in §3.19, corrected in §3.25',
    'alpha_1_29_status': 'PHENOMENOLOGICAL fit, not first-principles derivation',
    'L37_status': 'OPEN, research challenge, requires new calculation',
    'honest_verdict': 'α is a calibrated fit to SN 33s, not derived',
}

with open('v27_cghs_web_research.json', 'w') as f:
    json.dump(results, f, indent=2)

print()
print("Results saved to: calculations/v27_cghs_web_research.json")
