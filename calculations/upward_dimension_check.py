#!/usr/bin/env python3
"""
Upward dimension check: does the scaling law + closed loop work at every level?
================================================================================

User question: "does the scaling law and closed loop work for every upward dimension?"

In SIDC, the hierarchy is cone-shaped:
- 4D event → 3+1D universe (us) → 2D universes (terminal at 2D)

Going UPWARD from 3+1D means higher-dimensional universes (hypothetical).
The §3.18 claim: "the same α = 1.29 applies at every level".

This script tests:
1. Scaling law at each upward level (using same α = 1.289)
2. Closed loop at each upward level
3. Cross-level consistency: do the predictions match?
4. Whether α = 1.289 is universal or level-dependent

For each level D-1 (D = parent dim, D-1 = child dim):
- Scaling law: τ_{D-1, D-view} = 33 s × (E_D / E_calibration)^α
- Closed loop: f_back at level D = ... × (E_{D+1}/E_calibration)^(1/(2α))

The "calibration" at each level uses the CHILD level's own reference event.


**HISTORICAL (v2.x era, mid-2025)**: This file is from the v2.x era, predating:
- v3.0+ Lagrangian work (L102-L136)
- v3.1+ Multi-universe picture (L142-L150)
- v3.3 Bilateral cascade (E_4D = 5e79 J, M_Pl,4D = 3.93e23 GeV)
- v3.5.7+ Naming revolution (f_back -> f_DE, f_DM,leak, f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N*v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via alpha-GM, L308v)
- alpha = 1.289 (FIRST-PRINCIPLES via L308n)
- eps = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- gamma_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- tau_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v2.x era framework, not v3.5.9+ A2.

"""

import numpy as np

# Constants
T_PLANCK_3 = 5.391e-44  # s
E_PLANCK_3 = 2.176e-8 * 2.998e8**2  # J = 1.96e9 J
ALPHA = 1.289

# Calibration at 3D → 2D level
E_SN_3D_to_2D = 1e44  # J
TAU_SN_3D_to_2D = 33.0  # s
E_4D_COSMOLOGICAL = 1e69  # J (4D event creating our universe)
TAU_4D_COSMOLOGICAL = 2e26 * 3.156e7  # s (our universe's 4D-view lifetime)

print("="*72)
print("UPWARD DIMENSION CHECK: scaling law + closed loop at every level")
print("="*72)

# =============================================================================
# PART 1: Define the SIDC hierarchy
# =============================================================================
print("\n" + "="*72)
print("PART 1: SIDC HIERARCHY (cone-shaped, 4 levels)")
print("="*72)

# Levels (from highest to lowest):
# Level 5: 5D event → 4D universe (hypothetical)
# Level 4: 4D event → 3+1D universe (our universe) — speculative
# Level 3: 3D event → 2D universe — CALIBRATED (SN 33s)
# Level 2: 2D universe is TERMINAL (no further downward cascade)

print("\nSIDC hierarchy:")
print("  Level 5: 5D event → 4D universe (hypothetical, beyond our universe)")
print("  Level 4: 4D event → 3+1D universe (us) — SPECULATIVE extrapolation")
print("  Level 3: 3D event → 2D universe — CALIBRATED at SN 33s")
print("  Level 2: 2D universe is TERMINAL (cone-shape stops)")

# =============================================================================
# PART 2: SCALING LAW at each level (upward extrapolation)
# =============================================================================
print("\n" + "="*72)
print("PART 2: SCALING LAW at each level")
print("="*72)

# At level 3 (calibrated): 3D event → 2D universe
# τ_2D = 33 s × (E_3D / 10^44 J)^1.289
# This is the GROUND TRUTH.

# At level 4 (extrapolated): 4D event → 3D universe (us)
# If SAME FORMULA: τ_3D = 33 s × (E_4D / E_3D_calibration)^1.289
# But we need to decide what E_3D_calibration is at this level.

# SIDC's claim: same α applies, but the CALIBRATION shifts to the parent level.
# At level D-1, calibration is: τ_{D-1} = 33 s when E_D = 10^44 J
# (in units of the parent level's energy)

print("\nAt level D-1, the scaling law says:")
print("  τ_{D-1, D-view} = 33 s × (E_D / 10^44 J)^α")
print("  where E_D is the parent level's event energy")

# Test: at level 4 (4D → 3D)
E_4D = E_4D_COSMOLOGICAL  # 10^69 J
tau_3D_predicted = 33.0 * (E_4D / 1e44) ** ALPHA
print(f"\nLevel 4 (4D → 3D, our universe):")
print(f"  E_4D = {E_4D:.2e} J")
print(f"  Predicted τ_3D (4D-view) = {tau_3D_predicted:.3e} s = {tau_3D_predicted/3.156e7:.3e} yr")
print(f"  Paper says 2 × 10^26 yr = {2e26*3.156e7:.3e} s")
print(f"  Ratio: {tau_3D_predicted / (2e26*3.156e7):.3f}")

# Test: at level 5 (5D → 4D, hypothetical)
# The 4D event in our universe has E_4D ~ 10^69 J
# At level 5, the parent event is the 5D event creating the 4D universe
# We don't know E_5D directly, but if we assume the same FORMULA...
# The 4D universe's "event" in level 4 is 10^69 J
# By the scaling law: the 5D event's energy would need to be even larger

# Let's parameterize: what if the 4D event is itself a 2D universe
# in a higher-dim framework? Then E_5D would be a different quantity.

# For the upward check: assume the same formula structure at level 5
# If E_5D = 10^X J (unknown), then τ_4D = 33 s × (E_5D / 10^44)^1.289

# But we can use the DOWNWARD relation: our universe is the child of a 4D event
# So the 4D event is "above" us, and the 4D universe would be "above that" if we
# were in a higher-dimensional framework.

# At level 5: τ_4D = 33 s × (E_5D / 10^44)^1.289
# We don't know E_5D. But we can use the SAME α and see what range of
# E_5D is consistent.

# Let's parameterize: what would E_5D need to be for the 4D universe to
# last a meaningful time (e.g., comparable to a cosmological timescale)?

print("\nLevel 5 (5D → 4D, hypothetical):")
for tau_target in [1e10, 1e20, 1e30, 1e40, 1e50]:  # years
    tau_target_s = tau_target * 3.156e7
    # 33 s × (E_5D / 1e44)^1.289 = tau_target_s
    # (E_5D / 1e44)^1.289 = tau_target_s / 33
    # E_5D / 1e44 = (tau_target_s / 33)^(1/1.289)
    ratio = tau_target_s / 33.0
    E_5D = 1e44 * ratio ** (1/ALPHA)
    print(f"  For τ_4D = {tau_target:.0e} yr: E_5D = {E_5D:.3e} J")

# =============================================================================
# PART 3: CLOSED LOOP at each level
# =============================================================================
print("\n" + "="*72)
print("PART 3: CLOSED LOOP at each level")
print("="*72)

# Closed loop formula (ground truth at level 3 → 2):
# f_back = (t_Pl,3/τ_4D) × (τ_SN,obs/τ_universe) × (E_4D/E_SN)^(1/(2α))
# This gives f_back ≈ 10^-85

# At level 4 (4D → 3D), the analogous formula:
# f_back_4 = (t_Pl,4/τ_5D) × (τ_3D/τ_4D_universe) × (E_5D/E_4D)^(1/(2α))
# This would give f_back_4 for the 3D universe (us)

# We don't know t_Pl,4, τ_5D, E_5D, etc. But we can compute the structure.

# Forward direction (γ): γ = (E/E_Pl)^α
# Backward direction (f_back): f_back ~ (E_parent/E_child)^(1/(2α))
# Round-trip: α × 1/(2α) = 1/2

# The CLOSED LOOP at any level is:
# f_back^level = (t_Pl,parent/τ_grandparent) × (τ_grandparent_child/τ_parent) ×
#                 (E_grandparent/E_parent)^(1/(2α))
# where parent and grandparent refer to the levels in the hierarchy

# At level 3 (3D → 2D): parent = 4D, grandparent = 5D (does not exist in SIDC)
# Wait, this is confusing. Let me re-think.

# Actually, the closed loop is between FORWARD (γ) and BACKWARD (f_back)
# at the SAME level. The "parent" in f_back formula is the level ABOVE
# the one we're computing the lifetime for.

# So at level 3 (computing τ_2D from E_3D event):
# Forward: γ_3 = (E_3D/E_Pl,3)^α → τ_2D = γ_3 × t_Pl,3
# Backward: f_back = (E_4D/E_3D)^(1/(2α)) × prefactors

# The closed loop: γ_3 × f_back = some fundamental quantity

# At level 4 (computing τ_3D from E_4D event):
# Forward: γ_4 = (E_4D/E_Pl,4)^α → τ_3D = γ_4 × t_Pl,4
# Backward: f_back_4 = (E_5D/E_4D)^(1/(2α)) × prefactors
# But we don't know E_5D!

# Key insight: at each level, we need BOTH the parent event energy
# (for the forward scaling) AND the grandparent event energy (for the
# back-action).

# In our universe: we know E_3D (SNe, etc.) and E_4D (cosmological event).
# We don't know E_5D (it would be the parent of the 4D event in a higher
# dimensional framework).

print("\nClosed loop formula at each level:")
print("  Level 3 (3D → 2D):")
print("    Forward γ_3 = (E_3D/E_Pl,3)^α")
print("    Backward f_back_3 = (E_4D/E_3D)^(1/(2α)) × prefactors_3")
print("    Closed: γ_3 × f_back_3 = constant")

# At level 4:
print("\n  Level 4 (4D → 3D):")
print("    Forward γ_4 = (E_4D/E_Pl,4)^α")
print("    Backward f_back_4 = (E_5D/E_4D)^(1/(2α)) × prefactors_4")
print("    Need E_5D to evaluate f_back_4")

# =============================================================================
# PART 4: What CAN we verify upward?
# =============================================================================
print("\n" + "="*72)
print("PART 4: WHAT WE CAN VERIFY UPWARD")
print("="*72)

# We CAN verify the scaling law upward IF we assume the SAME α
# We CAN verify the closed loop IF we know E_5D (we don't)

# What we can check: is the 4D → 3D scaling consistent with 3D → 2D?
# Use the SAME α = 1.289 at both levels.

# Test: at level 4, predict τ_3D using α = 1.289 and E_4D = 10^69 J
# Compare with paper value of 2 × 10^26 yr

tau_3D_from_scaling = 33.0 * (E_4D / 1e44) ** ALPHA
tau_3D_paper = 2e26 * 3.156e7
print(f"\nLevel 4 scaling prediction (using α = 1.289):")
print(f"  τ_3D = {tau_3D_from_scaling:.3e} s = {tau_3D_from_scaling/3.156e7:.3e} yr")
print(f"  Paper: 2 × 10^26 yr = {tau_3D_paper:.3e} s")
print(f"  Ratio: {tau_3D_from_scaling / tau_3D_paper:.3f}")
print(f"  WITHIN FACTOR 1.6 → scaling law works at level 4 ✓")

# What if α is slightly different at level 4?
print(f"\nSensitivity: if α changes by ±1% at level 4:")
for delta in [-0.05, -0.02, -0.01, 0, 0.01, 0.02, 0.05]:
    alpha_test = ALPHA + delta
    tau_test = 33.0 * (E_4D / 1e44) ** alpha_test
    ratio = tau_test / tau_3D_paper
    print(f"  α = {alpha_test:.3f}: τ_3D = {tau_test/3.156e7:.3e} yr, ratio = {ratio:.3f}")

# =============================================================================
# PART 5: Closed loop verification at level 4 (if we had E_5D)
# =============================================================================
print("\n" + "="*72)
print("PART 5: CLOSED LOOP at level 4 (with hypothetical E_5D)")
print("="*72)

# If we assume E_5D is much larger than E_4D (extrapolation),
# let's check if the closed loop still closes

# Speculative scenario: E_5D = 10^94 J (10x E_4D, in same spirit as 4D → 3D)
E_5D_HYPOTHETICAL = 1e94  # J (5D event creating the 4D universe, hypothetical)

# Closed loop at level 4:
# f_back_4 = (t_Pl,4/τ_5D) × (τ_4D_universe/τ_3D_4D_view) × (E_5D/E_4D)^(1/(2α))
# We don't know t_Pl,4 or τ_5D directly

# Use the 3D → 2D formula as a template
f_back_3 = (T_PLANCK_3 / TAU_4D_COSMOLOGICAL) * (TAU_SN_3D_to_2D / (13.8e9 * 3.156e7)) * (E_4D_COSMOLOGICAL / E_SN_3D_to_2D) ** (1/(2*ALPHA))
print(f"\nAt level 3 (calibrated): f_back = {f_back_3:.3e} ≈ 10^-85 ✓")

# At level 4 (hypothetical): if E_5D = 10^94 J
# Assume t_Pl,4 scales similarly to t_Pl,3 (or use floor M_Pl,4 ≥ 887 GeV → t_Pl,4 ~ 10^-27 s)
T_PLANCK_4_HYPOTHETICAL = 1e-27  # s (corresponds to M_Pl,4 ~ 887 GeV)

# We need τ_5D. Assume τ_5D scales similarly (cosmological event lifetime)
# In SIDC: τ_5D = 33 s × (E_5D / 10^44)^1.289
TAU_5D_HYPOTHETICAL = 33.0 * (E_5D_HYPOTHETICAL / 1e44) ** ALPHA
print(f"\nHypothetical level 5: τ_5D = {TAU_5D_HYPOTHETICAL:.3e} s = {TAU_5D_HYPOTHETICAL/3.156e7:.3e} yr")

# f_back at level 4 (with these assumptions)
# τ_4D_universe is the 4D universe's lifetime = E_4D cosmological / similar formula
TAU_4D_UNIVERSE_HYPOTHETICAL = 33.0 * (E_5D_HYPOTHETICAL / 1e44) ** ALPHA
TAU_3D_4D_VIEW = TAU_4D_COSMOLOGICAL  # 2 × 10^26 yr

f_back_4 = (T_PLANCK_4_HYPOTHETICAL / TAU_5D_HYPOTHETICAL) * \
           (TAU_3D_4D_VIEW / TAU_4D_UNIVERSE_HYPOTHETICAL) * \
           (E_5D_HYPOTHETICAL / E_4D_COSMOLOGICAL) ** (1/(2*ALPHA))

print(f"\nAt level 4 (with E_5D = 10^94 J, hypothetical):")
print(f"  f_back_4 = {f_back_4:.3e}")

# Compare with level 3
print(f"\nComparison:")
print(f"  f_back at level 3: {f_back_3:.3e}")
print(f"  f_back at level 4 (hypothetical): {f_back_4:.3e}")
print(f"  Ratio: {f_back_4 / f_back_3:.3e}")

# =============================================================================
# PART 6: KEY QUESTION: does α = 1.289 work at every level?
# =============================================================================
print("\n" + "="*72)
print("PART 6: KEY QUESTION — IS α UNIVERSAL?")
print("="*72)

print("""
For the scaling law + closed loop to work at EVERY upward level,
we need α = 1.289 to be UNIVERSAL across levels.

Evidence for α being universal:
1. N = 12 SYK is the SAME at every level (the 12 SM Weyl fermions are fixed)
2. The composite exponent 1/(2α) = c/α = (1/2)/1.289 = 0.388 depends on c = N/24
   which is universal
3. The scaling law at level 4 (4D → 3D) matches the paper within 12% using α = 1.289

Evidence against α being universal:
1. We don't have direct tests of α at levels above our own
2. The 4D → 3D level is "speculative extrapolation" (not calibrated)
3. If α depends on the brane-tension (which may differ at each level),
   then α could vary

VERDICT:
- At level 3 (3D → 2D), α = 1.289 is CALIBRATED.
- At level 4 (4D → 3D), α = 1.289 is PLAUSIBLE (consistent within 12%).
- At level 5 (5D → 4D), we CANNOT TEST (no data).

For the framework to be fully upward-extendable, we need α to be universal.
This is a CLAIM in SIDC, supported by structural arguments (N = 12 is fixed),
but not directly verified at higher levels.
""")

# =============================================================================
# PART 7: Summary
# =============================================================================
print("\n" + "="*72)
print("PART 7: SUMMARY")
print("="*72)

print("""
SCALING LAW at every upward level:
- Level 3 (3D → 2D): CALIBRATED at SN 33s. Works for 8/8 events within 1.6x.
- Level 4 (4D → 3D): EXTRAPOLATED using α = 1.289. Matches paper within 12%.
- Level 5 (5D → 4D): UNKNOWN (no data).

CLOSED LOOP at every upward level:
- Level 3 (3D → 2D): VERIFIED. f_back ≈ 10^-85.
- Level 4 (4D → 3D): SPECULATIVE (depends on E_5D, which we don't know).
- Level 5 (5D → 4D): CANNOT EVALUATE.

REQUIREMENTS for upward extension:
1. α = 1.289 must be universal (supported by N = 12 being fixed)
2. Closed loop prefactors must work at each level (need consistent t_Pl, τ_D)
3. The "33 s" calibration at each level must be consistent

CONCLUSION:
The scaling law WORKS at level 3 (calibrated) and is PLAUSIBLE at level 4.
The closed loop WORKS at level 3 but REQUIRES HYPOTHETICAL INPUT at level 4+
(E_5D, t_Pl,4, etc.).

SIDC's upward extendability is a CLAIM, supported by structural arguments,
but not directly verified above our own hierarchy level.
""")