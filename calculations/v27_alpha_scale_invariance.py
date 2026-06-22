#!/usr/bin/env python3
"""
v27_alpha_scale_invariance.py
================================

Question: Is α = 1.29 truly scale-invariant, or does it change with energy?

The cascade's energy-scaling rule:
  τ_2D = (E/E_Pl)^α × t_Pl
with α = 1.29 (assumed universal, calibrated from SN).

Strong version: α = 1.29 for ALL E (scale-invariant)
Weak version: α depends on E (running α)
Weakest version: α is a local fit at SN scale

Test 1: What does constant α predict at different energies?
Test 2: What would running α look like?
Test 3: How would 2030s GW data distinguish?

Honest answer: the cascade ASSUMES α = constant. This is a phenomenological
choice, NOT derived from first principles. The 6 frameworks analyzed
(CGHS, Padmanabhan, HW, Jacobson, RT, KK) all give scale-dependent
predictions in some cases, so the constant-α assumption is actually
*stronger* than what those frameworks would naturally give.

In QFT, couplings "run" with energy. The cascade's α is a coupling-like
parameter. There is NO theoretical reason to expect α to be constant,
and good reasons (RG flow) to expect it to run.

The cascade's choice of constant α is the SIMPLEST possibility, but it
could be wrong.

Test: if α runs, what does it look like?

Simple model: α(E) = α_0 + β × log(E/E_SN)
- α_0 = 1.29 (SN value)
- β = "running rate" (free parameter)

For β = 0: constant α = 1.29 (cascade's assumption)
For β = 0.1: α changes by 10% per decade of energy
For β = -0.1: α decreases with energy

We don't know β. It's a hidden free parameter that the cascade has
collapsed to β = 0 (constant α).

Future GW observations of 2D universe death signals at different energies
(BNS, AGN) would constrain β.

Test: if β = 0 is correct, what do we predict?
- τ_2D(SN) = 33 s (calibration)
- τ_2D(BNS) = 33 × (10^46/10^44)^1.29 = 3.5 hours
- τ_2D(AGN) = 33 × (10^52/10^44)^1.29 = 1.6×10^8 yr

If β ≠ 0, these predictions would be different.


**HISTORICAL (v2.7 era, mid-2025)**: This file is from the v2.7.x era, predating:
- v3.0+ Lagrangian work (L102-L136)
- v3.1+ Multi-universe picture (L142-L150)
- v3.3 Bilateral cascade (E_4D = 5e79 J, M_Pl,4D = 3.93e23 GeV)
- v3.5.7+ Naming revolution (f_back → f_DE,f_DM,leak,f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N×v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via α-GM, L308v)
- α = 1.289 (FIRST-PRINCIPLES via L308n)
- ε = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- γ_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- τ_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v2.7 era framework, not v3.5.9+ A2.
"""
import numpy as np
import json

# Constants
c = 2.998e8
hbar = 1.055e-34
G = 6.674e-11
M_P = np.sqrt(hbar * c / G)
t_P = np.sqrt(hbar * G / c**5)
M_sun = 1.989e30
yr = 3.156e7

print("=" * 70)
print("IS α = 1.29 TRULY SCALE-INVARIANT?")
print("=" * 70)
print()
print("Cascade's assumption: α is UNIVERSAL (same value at all energies)")
print("Calibration: α = 1.29 from SN (E = 10^44 J)")
print()
print("=" * 70)
print("TEST 1: Constant α predictions across 14 orders of magnitude in E")
print("=" * 70)
print()
print(f"  {'Event':<20} {'E (J)':<12} {'τ_2D':<25} {'Status'}")
print("  " + "-"*85)

alpha = 1.29
E_SN = 1e44
tau_SN = 33.0

events = [
    ("LHC pp", 1e-9, "Unmeasurable (10^-67 s)"),
    ("Sun particle", 1e-19, "Unmeasurable (10^-95 s)"),
    ("SN", E_SN, "CALIBRATION (33 s)"),
    ("Hypernova", 1e46, "Prediction (3.5 hr)"),
    ("BNS merger", 1e53, "Prediction (4.3e5 yr)"),
    ("AGN outburst", 1e55, "Prediction (1.6e8 yr)"),
]

for name, E, status in events:
    E_Pl = E / (M_P * c**2)
    tau = t_P * E_Pl**alpha
    if tau < 1e-12:
        tau_str = f"{tau:.2e} s"
    elif tau < 3600:
        tau_str = f"{tau:.2e} s"
    elif tau < yr:
        tau_str = f"{tau/3600:.2e} hr"
    else:
        tau_str = f"{tau/yr:.2e} yr"
    print(f"  {name:<20} {E:<12.0e} {tau_str:<25} {status}")

print()
print("Verdict: With α = 1.29 (constant), predictions span 100 orders of magnitude")
print("in τ_2D, all from one SN calibration.")
print()

print("=" * 70)
print("TEST 2: What would running α look like?")
print("=" * 70)
print()
print("Hypothesis: α(E) = α_0 + β × log(E/E_SN)")
print()
print("Compare predictions for different β values:")
print()

print(f"  {'E (J)':<10} {'α(β=0)':<12} {'α(β=0.1)':<12} {'α(β=-0.1)':<12} {'τ(β=0.1)':<15} {'τ(β=-0.1)':<15}")
print("  " + "-"*85)

for name, E in [("LHC", 1e-9), ("SN", 1e44), ("BNS", 1e53), ("AGN", 1e55)]:
    log_ratio = np.log10(E / E_SN)
    alpha_0 = 1.29
    alpha_pos = 1.29 + 0.1 * log_ratio
    alpha_neg = 1.29 - 0.1 * log_ratio

    E_Pl = E / (M_P * c**2)
    tau_pos = t_P * E_Pl**alpha_pos
    tau_neg = t_P * E_Pl**alpha_neg

    print(f"  {E:<10.0e} {alpha_0:<12.3f} {alpha_pos:<12.3f} {alpha_neg:<12.3f} {tau_pos:<15.2e} {tau_neg:<15.2e}")

print()
print("Verdict: If α runs, the predicted τ_2D values at BNS, AGN could be")
print("DIFFERENT by orders of magnitude from constant-α predictions.")
print()
print("This is testable! Future BNS/AGN GW observations would distinguish:")
print("  - Constant α (β = 0): cascade's current assumption")
print("  - Running α (β ≠ 0): more complex dynamics, e.g., CGHS with energy-dependent back-reaction")
print()

print("=" * 70)
print("TEST 3: Why might α run? Theoretical motivation")
print("=" * 70)
print()
print("In QFT, couplings RUN with energy (renormalization group).")
print("The cascade's α is a coupling-like parameter (energy-scaling exponent).")
print()
print("Reasons α MIGHT run:")
print("  - 2D gravity back-reaction could be energy-dependent (CGHS variant)")
print("  - String theory moduli have energy-dependent VEVs")
print("  - The 'fundamental' scale (Planck scale?) might shift with E")
print("  - Multi-scale physics (e.g., 2D universe has internal scales)")
print()
print("Reasons α MIGHT be constant:")
print("  - 2D conformal invariance (CFT) gives scale-invariant physics")
print("  - Simple power-law is the lowest-order ansatz")
print("  - The cascade's framework is 'scale-invariant in the energy/size sense' (§2.1)")
print()
print("Honest answer: the cascade ASSUMES constant α for simplicity.")
print("There is no theoretical reason (from any of the 6 frameworks) to")
print("expect α to be constant. The constant-α assumption is a phenomenological")
print("choice, not a derivation.")
print()

print("=" * 70)
print("WHAT WOULD 2030s OBSERVATIONS TELL US?")
print("=" * 70)
print()
print("Cascade predicts 2D universe death GW at:")
print("  - BNS (E = 10^53 J): τ_2D = 4.3e5 yr → GW frequency ~ 7e-14 Hz (PTA band)")
print("  - AGN (E = 10^55 J): τ_2D = 1.6e8 yr → GW frequency ~ 2e-17 Hz (PTA band)")
print()
print("SKA-MPG PTAs in 2030s could detect these signals (or not).")
print()
print("If detected at cascade's predicted amplitudes and frequencies:")
print("  - α = 1.29 is consistent with constant-α hypothesis")
print("  - β = 0 is supported")
print()
print("If detected at DIFFERENT amplitudes/frequencies:")
print("  - α is NOT 1.29 at those energies")
print("  - α is running (β ≠ 0)")
print("  - Or α = 1.29 only at SN scale, not universal")
print()
print("If NOT detected:")
print("  - α = 1.29 is FALSIFIED")
print("  - The cascade's energy-scaling rule is wrong")
print()

print("=" * 70)
print("SUMMARY: Is α = 1.29 scale-invariant?")
print("=" * 70)
print()
print("The cascade ASSUMES α = 1.29 is universal (same at all energies).")
print()
print("This assumption is:")
print("  ✗ NOT derived from any framework (CGHS, Padmanabhan, HW, RT, KK all")
print("    allow for energy-dependent α)")
print("  ✗ NOT theoretically motivated (QFT couplings generally run)")
print("  △ Phenomenologically simplest (constant power-law)")
print("  ✓ TESTABLE in 2030s by BNS/AGN GW observations")
print()
print("If future GW observations match cascade's α = 1.29 predictions at")
print("BNS, AGN, GRB energies (spanning 10+ orders of magnitude), then")
print("the constant-α assumption is validated. If not, α is running.")
print()
print("The cascade is honest: it assumes constant α, but this is a")
print("phenomenological choice, not a derivation. The 2030s tests will")
print("show whether this assumption holds across 14+ orders of magnitude")

results = {
    "test": "Is α = 1.29 truly scale-invariant across energies?",
    "cascade_assumption": "α is constant (universal)",
    "cascade_calibration": "α = 1.29 from SN (E = 10^44 J)",
    "predictions_under_constant_alpha": {
        "LHC_pp_s": t_P * (1e-9 / (M_P * c**2))**1.29,
        "BNS_merger_yr": t_P * (1e53 / (M_P * c**2))**1.29 / yr,
        "AGN_outburst_yr": t_P * (1e55 / (M_P * c**2))**1.29 / yr,
    },
    "theoretical_motivation_for_running": [
        "QFT couplings generally run with energy (RG flow)",
        "CGHS back-reaction may be energy-dependent",
        "String moduli have energy-dependent VEVs",
        "Multi-scale physics in 2D universe creation",
    ],
    "verdict": {
        "constant_alpha_derived": False,
        "constant_alpha_motivated": "phenomenological only",
        "constant_alpha_testable": True,
        "testable_by": "BNS/AGN GW background in 2030s (SKA-MPG PTAs)",
        "if_validated": "α = 1.29 holds across 14+ orders of magnitude",
        "if_falsified": "α runs with energy, or α = 1.29 is local fit only",
    },
    "conclusion": "α = 1.29 is ASSUMED constant, not derived. The cascade's scale-invariance assumption is phenomenological, not theoretical. 2030s GW observations would distinguish constant-α from running-α scenarios."
}

with open('/workspace/github-repo/calculations/v27_alpha_scale_invariance_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print()
print("Results saved to calculations/v27_alpha_scale_invariance_results.json")
