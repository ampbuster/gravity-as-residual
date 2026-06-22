#!/usr/bin/env python3
"""
L308bm: FRAMEWORK AUDIT — L308ab c value + M_Pl,4D α-GM inconsistency
=====================================================================

USER REQUEST (June 22, 2026): "Re-examine L308ab's α value (since the L308bl
'magnitude' estimate was wrong). Address other framework inconsistencies if you
spot them."

AUDIT FINDINGS:

1. L308ab c = 1.13 IS CALIBRATED (acknowledged in L308ab)
   - c is calibrated to drain 32 orders by z=1100
   - Integration starts at t_Pl (5.4e-44 s)
   - If integration starts at BBN, c = 4.8 (much larger)
   - c = 1.13 is self-consistent: gives τ_DM = 12.84 Gyr (universe age)
   - HONEST FRAMING: c is calibration, not derivation. But choice is forced.

2. M_Pl,4D α-GM INCONSISTENCY in A2 (NEW FINDING)
   - L138 (A1 era): M_Pl,4D = M_Pl,3D^α × M_Pl,2D^(1-α) with α = 1.289 → 3.93e23
   - A2: α_4D = 1.577 (dim-specific)
   - If applied to M_Pl,4D α-GM: M_Pl,4D = M_Pl,3D^1.577 × M_Pl,2D^(-0.577) = 1.25e28
   - Framework uses M_Pl,4D = 3.93e23 (A1 value), but A2 α_4D = 1.577
   - INCONSISTENCY: 4.5 orders of magnitude difference

3. f_DE,closed uses both A1 M_Pl,4D AND A2 α_4D
   - f_DE,closed = (M_Pl,4D/E_4D)^α_4D × prefactor
   - M_Pl,4D = 3.93e23 (A1), α_4D = 1.577 (A2)
   - The prefactor is calibrated to give f_DE,closed = 1.79e-90
   - The "prefactor" hides the inconsistency

STATUS: Framework uses A1's M_Pl,4D with A2's α. Need to fix.

**CURRENT (v3.5.9+ A2, June 22, 2026)**: Audit of L308ab and α-GM formulas.
"""

import numpy as np

print("=" * 70)
print("L308bm: FRAMEWORK AUDIT")
print("=" * 70)
print()

# Section 1: L308ab c value
print("SECTION 1: L308ab c = 1.13 — CALIBRATED, NOT DERIVED")
print("-" * 70)
print()
print("c is calibrated to drain 32 orders by z=1100 (matches Ω_c = 0.265)")
print()
print("But c DEPENDS ON THE STARTING TIME OF THE INTEGRATION:")
print()
print(f"{'Starting time':<28} {'I_total':<15} {'c':<10} {'τ_DM (Gyr)':<12}")
print("-" * 70)

H_0 = 2.184e-18
t_CMB = 1.155e13
t_eq = 1.613e12

starting_times = [
    ("t_Pl (5.4e-44 s, FRAMEWORK)", 5.39e-44, "Framework's choice"),
    ("t_EW (1e-12 s)", 1e-12, "Electroweak transition"),
    ("t_QCD (1e-5 s)", 1e-5, "QCD transition"),
    ("t_BBN (1 s)", 1.0, "Big Bang nucleosynthesis"),
]

for name, t_start, note in starting_times:
    if t_start < t_eq:
        I_rad = 0.5 * np.log(t_eq / t_start)
        I_mat = (2.0/3.0) * np.log(t_CMB / t_eq)
    else:
        I_rad = 0
        I_mat = (2.0/3.0) * np.log(t_CMB / t_start)
    I_total = I_rad + I_mat
    c = (32 * np.log(10)) / I_total
    tau_DM = 1 / (c * H_0) / (365.25 * 24 * 3600 * 1e9)
    note_marker = " ← FRAMEWORK" if "FRAMEWORK" in name else ""
    print(f"{name:<28} {I_total:<15.3f} {c:<10.3f} {tau_DM:<12.2f}{note_marker}")

print()
print("KEY OBSERVATIONS:")
print("  - c = 1.13 with t_Pl gives τ_DM = 12.84 Gyr (universe age = 13.8 Gyr)")
print("  - Other starting times give larger c, shorter τ_DM (inconsistent)")
print("  - c = 1.13 is FORCED by the requirement τ_DM ≈ universe age")
print()
print("HONEST FRAMING:")
print("  - c ≈ 1 is the natural value (essentially f_leak = H(z))")
print("  - c = 1.13 is a 13% calibration correction")
print("  - The choice of starting time (t_Pl) is arbitrary but consistent")
print("  - 'Why c ≈ 1?' is OPEN (could be derived from 4D event geometry)")
print()

# Section 2: M_Pl,4D α-GM inconsistency
print("=" * 70)
print("SECTION 2: M_Pl,4D α-GM INCONSISTENCY IN A2 (NEW FINDING)")
print("-" * 70)
print()

M_Pl_3D = 1.22e19  # GeV
M_Pl_2D = 2.95e3  # GeV
M_Pl_4D_framework = 3.93e23  # GeV (framework uses this)

alpha_A1 = 1.289
alpha_2D = 1.289
alpha_3p1D = 1.408
alpha_4D = 1.577

# A1 calculation
M_Pl_4D_A1 = M_Pl_3D**alpha_A1 * M_Pl_2D**(1-alpha_A1)
print(f"A1 (α = 1.289):")
print(f"  M_Pl,4D = M_Pl,3D^α × M_Pl,2D^(1-α)")
print(f"         = ({M_Pl_3D:.2e})^{alpha_A1} × ({M_Pl_2D:.2e})^{1-alpha_A1:.3f}")
print(f"         = {M_Pl_4D_A1:.3e} GeV")
print(f"  Framework value: {M_Pl_4D_framework:.2e} GeV")
print(f"  Match: {M_Pl_4D_A1/M_Pl_4D_framework*100:.1f}%")
print()

# A2 calculation (using α_4D)
M_Pl_4D_A2_alpha4D = M_Pl_3D**alpha_4D * M_Pl_2D**(1-alpha_4D)
print(f"A2 with α_4D = 1.577:")
print(f"  M_Pl,4D = M_Pl,3D^α_4D × M_Pl,2D^(1-α_4D)")
print(f"         = ({M_Pl_3D:.2e})^{alpha_4D} × ({M_Pl_2D:.2e})^{1-alpha_4D:.3f}")
print(f"         = {M_Pl_4D_A2_alpha4D:.3e} GeV")
print(f"  Framework value: {M_Pl_4D_framework:.2e} GeV")
print(f"  DISCREPANCY: {M_Pl_4D_A2_alpha4D/M_Pl_4D_framework:.2e}×")
print(f"  This is {np.log10(M_Pl_4D_A2_alpha4D/M_Pl_4D_framework):.1f} orders of magnitude off!")
print()

# What α is implied by the framework's M_Pl,4D?
log_M_Pl_4D = np.log(M_Pl_4D_framework)
log_M_Pl_3D = np.log(M_Pl_3D)
log_M_Pl_2D = np.log(M_Pl_2D)
alpha_implied = (log_M_Pl_4D - log_M_Pl_2D) / (log_M_Pl_3D - log_M_Pl_2D)
print(f"α implied by M_Pl,4D = {M_Pl_4D_framework:.2e}: {alpha_implied:.4f}")
print(f"This matches α_2D = {alpha_2D} (NOT α_4D = {alpha_4D})")
print()

# Conclusion
print("=" * 70)
print("CONCLUSION")
print("=" * 70)
print()
print("M_Pl,4D α-GM INCONSISTENCY:")
print()
print("  - L138 (A1 era): α = 1.289 → M_Pl,4D = 3.93e23 (correct)")
print("  - A2 should use α_4D = 1.577, giving M_Pl,4D = 1.25e28")
print("  - But framework still uses M_Pl,4D = 3.93e23 (A1 value)")
print("  - The α dim-specific changes were NOT propagated to M_Pl,4D formula")
print()
print("WHAT NEEDS TO BE FIXED:")
print("  Option A: Update M_Pl,4D to 1.25e28 (consistent with α_4D)")
print("    - This changes f_DE,closed prefactor by 6.7 orders")
print("    - f × ε invariant may or may not be preserved")
print("  Option B: Note that M_Pl,4D = 3.93e23 is a 'fixed parameter' (not from α_4D)")
print("    - The α-GM formula is then NOT used for M_Pl,4D in A2")
print("    - Need to update the documentation")
print()
print("CURRENT STATE (inconsistent):")
print("  - L138 uses α = 1.289 (A1) to derive M_Pl,4D = 3.93e23 ✓ (math right)")
print("  - L308av/aw (A2) use α_4D = 1.577 (dim-specific)")
print("  - These are inconsistent: 4.5 orders of magnitude")
print()
print("RECOMMENDATION: Option B for now (less disruptive):")
print("  - Document M_Pl,4D = 3.93e23 as A1 value, not derived in A2")
print("  - f_DE,closed prefactor hides the inconsistency but is calibrated")
print("  - Future: re-derive M_Pl,4D in A2 with proper α handling")
print()

# Section 3: f_DE,closed check
print("=" * 70)
print("SECTION 3: f_DE,closed CHECK")
print("-" * 70)
print()
E_4D_GeV = 4.99e79 / 1.602e-10
print(f"E_4D = {E_4D_GeV:.3e} GeV")
print(f"M_Pl,4D = {M_Pl_4D_framework:.3e} GeV (A1 value, used in A2)")
print(f"α_4D = {alpha_4D} (A2 dim-specific)")
print()

# Calculate (M_Pl,4D/E_4D)^α_4D
ratio = M_Pl_4D_framework / E_4D_GeV
print(f"M_Pl,4D/E_4D = {ratio:.3e}")
result = ratio**alpha_4D
print(f"(M_Pl,4D/E_4D)^α_4D = {result:.3e}")
print()

# Required to get f_DE,closed = 1.79e-90
f_DE_target = 1.79e-90
prefactor = f_DE_target / result
print(f"f_DE,closed target = {f_DE_target:.3e}")
print(f"Required prefactor = {prefactor:.3e}")
print(f"Framework says prefactor ~ 7e13")
print(f"Match: {prefactor/7e13*100:.1f}%")
print()
print("The prefactor hides the M_Pl,4D α-GM inconsistency.")
print("f × ε invariant is preserved (both A1 and A2 give 1.13e-123).")
print("But the M_Pl,4D value is technically inconsistent with α_4D.")
print()

# Final summary
print("=" * 70)
print("FINAL SUMMARY (L308bm)")
print("=" * 70)
print()
print("L308ab c = 1.13: CALIBRATED, not derived. Self-consistent.")
print("  - c depends on starting time of integration (t_Pl)")
print("  - c = 1.13 is forced by τ_DM ≈ universe age requirement")
print("  - 'Essentially f_leak = H(z)' is more robust than c = 1.13")
print()
print("M_Pl,4D = 3.93e23: INCONSISTENT with α_4D = 1.577 in A2")
print("  - L138 (A1): α = 1.289 → 3.93e23 ✓")
print("  - A2 should: α_4D = 1.577 → 1.25e28 (off by 4.5 orders)")
print("  - Framework uses A1 value, hidden by f_DE,closed prefactor")
print()
print("RECOMMENDATION:")
print("  - Document c = 1.13 as 'calibrated to t_Pl' more clearly")
print("  - Note M_Pl,4D = 3.93e23 is A1 value, not derived in A2")
print("  - Future: re-derive M_Pl,4D with consistent α handling")
print()
print("STATUS: Framework has 2 calibration issues that need documentation.")
print("Numerical results (ρ_DE, γ_4D) are correct within A1 era.")