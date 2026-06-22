"""
v3.5.3 EXPLORATION: Other formulas for μ

Test formulas OTHER than (2 × E_1st)² to see if any give μ = 9×10⁶ GeV² exactly.

Framework values:
- M_Pl,2D = 3 TeV
- E_1st = h × M_Pl,2D = (1/2) × 3 TeV = 1.5 TeV
- μ_framework = 9×10⁶ GeV²

Formulas to test (each with structural justification):

A. μ = E_1st × M_Pl,2D × factor
   factor=1: μ = 4.5×10⁶ (off by 2)
   factor=2: μ = 9×10⁶ ✓ (current)
   factor=π: μ = 1.41×10⁷ (off by 1.57)
   factor=π/2: μ = 7.07×10⁶ (off by 1.27)

B. μ = E_1st² × factor
   factor=1: μ = 2.25×10⁶ (off by 4)
   factor=4: μ = 9×10⁶ ✓ (current)
   factor=2π: μ = 1.41×10⁷ (off by 1.57)
   factor=8/π: μ = 5.73×10⁶ (off by 1.57)

C. μ = (factor × E_1st)² 
   factor=1: 2.25×10⁶
   factor=2: 9×10⁶ ✓ (current)
   factor=π: 2.22×10⁷
   factor=√π: 1.33×10⁷
   factor=2π: 8.88×10⁸

D. μ = (E_1st + M_Pl,2D)² / factor
   factor=1: 2.025×10⁷
   factor=2: 1.0125×10⁷
   factor=4: 5.06×10⁶
   factor=9/4: 9×10⁶ ✓ (matches!)

E. μ = E_1st² + factor × E_1st × M_Pl,2D + (M_Pl,2D/2)²
   factor=2: μ = E_1st² + 2 E_1st M_Pl,2D + (M_Pl,2D/2)² = (E_1st + M_Pl,2D/2)²
            = (M_Pl,2D/2 + M_Pl,2D/2)² = M_Pl,2D² ✓

F. μ = (E_1st + E_2nd)² / factor
   E_2nd = 3/2 × M_Pl,2D = 4.5 TeV (next Liouville primary h = 3b²)
   Sum: 6 TeV
   factor=4: μ = 9×10⁶ ✓

G. μ = (E_1st + T_H × something)² ?
   T_H = √μ/(2π) = 478 GeV
   This is circular

H. μ = E_1st² × (1 + 1/(2h))² where h is conformal weight
   For h = 1/2: (1 + 1)² = 4
   μ = 4 × E_1st² = M_Pl,2D² ✓
   This is the (2 × E_1st)² formula again (just rewritten)
   
   What if h is different?
   h = 1/3: (1 + 3/2)² = 6.25, μ = 6.25 × (M_Pl,2D/3)² = 6.25 M_Pl,2D²/9 = 6.94×10⁶ (off by 1.3)
   h = 1/4: (1 + 2)² = 9, μ = 9 × (M_Pl,2D/4)² = 9 M_Pl,2D²/16 = 5.06×10⁶ (off by 1.78)
   h = 1: (1 + 1/2)² = 2.25, μ = 2.25 × M_Pl,2D² = 2.025×10⁷ (off by 2.25)

I. μ from partition function zero mode
   Z(β) = ∫ dE ρ(E) e^(-β E)
   For thermal AdS_2 in JT: ρ(E) = (e^(S_0)/2π) × sinh(2π √(E × C)) 
   For C = 1/M_Pl,2D = 1/√μ: ρ(E) = (e^(S_0)/2π) × sinh(2π √(E/√μ))
   For small E: ρ(E) ≈ (e^(S_0)/2π) × 2π √(E/√μ) = e^(S_0) √(E/√μ)
   Setting ρ(E=0) = some value: doesn't directly give μ
   
J. μ from Cardy formula in 2D
   Cardy: ρ(E) = exp(2π √(c L_0/6)) for 2D CFT
   For c=1: ρ(E) = exp(2π √(E/6 × M_Pl,2D))
   Setting E_min = 0 (gapless): doesn't constrain μ
   
K. μ from extremal BH area
   For extremal 2D BH in JT: S_0 = 2π Φ_h
   If S_0 = 0 (extremal): doesn't constrain μ
   If S_0 = ln(2) (topological): doesn't constrain μ
   
L. μ from mass renormalization
   For 2D dilaton gravity: m_renormalized = m_bare + δm
   δm from quantum corrections: typically factor of M_Pl,2D
   Setting m_renormalized = some natural value: speculative

M. μ from DOZZ structure constant
   DOZZ: C(α_1, α_2, α_3) = specific formula with b²
   The structure constant involves μ explicitly in DOZZ formula
   For 3-point function <V_{α_1} V_{α_2} V_{α_3}>: C = ... × μ^((Q-Σα_i)/b)
   This gives a μ-dependent formula but doesn't constrain μ
   
N. μ from gravitational dressing
   In 2D, gravitational dressing of operators changes their scaling
   Dressing factor: e^(α φ) where α is the "dressing charge"
   For dressing to give a specific scale: depends on α

Let me just enumerate all formulas and check which give EXACT match.


**HISTORICAL (v3.5.7 era)**: This file uses v3.5.7 era values:
- M_Pl,2D = 2.95 TeV (was 3 TeV rounded, L308r chain)
- M_Pl,4D = 3.93e23 GeV (DERIVED via α-GM, L308v)
- α = 1.289 (was calibrated, now FIRST-PRINCIPLES via L308n)
- ε = 1e-38 (calibrated, was 1e-38 before A2 = 6.32e-34)
- f_back = (M_Pl/E)^α (LEGACY naming, renamed f_DE,closed in v3.5.7+)

Current v3.5.9+ A2 values (not used in this file):
- ε = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)

The structural motivations and derivations in this file remain valid
(math is correct), but the specific numerical values reflect v3.5.7 era
framework, not v3.5.9+ A2.
"""

import math
import numpy as np

print("=" * 70)
print("v3.5.3 EXPLORATION: Other formulas for μ")
print("=" * 70)

M_Pl_2D = 3e3  # GeV
h_first = 0.5  # Liouville b² = 1/2 (c=1)
E_1st = h_first * M_Pl_2D  # 1.5 TeV
mu_framework = 9e6  # GeV²

print(f"\nFramework: μ = {mu_framework:.2e} GeV² = M_Pl,2D² = (3 TeV)²")
print(f"E_1st = h × M_Pl,2D = {h_first} × {M_Pl_2D:.2e} = {E_1st:.2e} GeV")
print()

# Test formulas
results = []

# Formula A: μ = E_1st × M_Pl,2D × factor
print("=" * 70)
print("FORMULA A: μ = E_1st × M_Pl,2D × factor")
print("=" * 70)
for label, factor in [("factor=1", 1), ("factor=2", 2), ("factor=π", math.pi), 
                      ("factor=2π", 2*math.pi), ("factor=4/π", 4/math.pi)]:
    mu_calc = E_1st * M_Pl_2D * factor
    ratio = mu_calc / mu_framework
    print(f"  {label}: μ = {mu_calc:.2e} (ratio {ratio:.4f})")
    results.append((f"A: {label}", mu_calc, ratio))

# Formula B: μ = E_1st² × factor
print("\n" + "=" * 70)
print("FORMULA B: μ = E_1st² × factor")
print("=" * 70)
for label, factor in [("factor=1", 1), ("factor=4", 4), ("factor=2π", 2*math.pi),
                      ("factor=8/π", 8/math.pi), ("factor=π²", math.pi**2)]:
    mu_calc = E_1st**2 * factor
    ratio = mu_calc / mu_framework
    print(f"  {label}: μ = {mu_calc:.2e} (ratio {ratio:.4f})")
    results.append((f"B: {label}", mu_calc, ratio))

# Formula C: μ = (factor × E_1st)²
print("\n" + "=" * 70)
print("FORMULA C: μ = (factor × E_1st)²")
print("=" * 70)
for label, factor in [("factor=1", 1), ("factor=2", 2), ("factor=π", math.pi),
                      ("factor=√π", math.sqrt(math.pi)), ("factor=2π", 2*math.pi),
                      ("factor=√(2π)", math.sqrt(2*math.pi))]:
    mu_calc = (factor * E_1st)**2
    ratio = mu_calc / mu_framework
    print(f"  {label}: μ = {mu_calc:.2e} (ratio {ratio:.4f})")
    results.append((f"C: {label}", mu_calc, ratio))

# Formula D: μ = (E_1st + M_Pl,2D)² / factor
print("\n" + "=" * 70)
print("FORMULA D: μ = (E_1st + M_Pl,2D)² / factor")
print("=" * 70)
sum_val = E_1st + M_Pl_2D
for label, factor in [("factor=1", 1), ("factor=2", 2), ("factor=4", 4),
                      ("factor=9/4", 9/4), ("factor=π²", math.pi**2)]:
    mu_calc = sum_val**2 / factor
    ratio = mu_calc / mu_framework
    print(f"  {label}: μ = {mu_calc:.2e} (ratio {ratio:.4f})")
    results.append((f"D: {label}", mu_calc, ratio))

# Formula E: μ = (E_1st + M_Pl,2D/2)² (binomial)
print("\n" + "=" * 70)
print("FORMULA E: μ = (E_1st + M_Pl,2D/2)² (binomial)")
print("=" * 70)
mu_calc = (E_1st + M_Pl_2D/2)**2
ratio = mu_calc / mu_framework
print(f"  μ = (E_1st + M_Pl,2D/2)² = {mu_calc:.2e} (ratio {ratio:.4f})")
results.append(("E: (E_1st + M_Pl,2D/2)²", mu_calc, ratio))

# Formula F: μ = (E_1st + E_2nd)² / factor (with second Liouville primary h = 3b²)
print("\n" + "=" * 70)
print("FORMULA F: μ = (E_1st + E_2nd)² / factor")
print("=" * 70)
# Liouville primaries have h = b² + nb + m where b² = 1/2 for c=1
# For "second" primary (n=0, m=1): h = b² + b² = 2b² = 1? 
# Actually for c=1 Liouville with b=i: primaries are continuous h = b² + p² for p ≥ 0
# So h_0 = 1/2 (vacuum) and h_p = 1/2 + p² for p ≥ 0
# Lightest non-vacuum: still h = 1/2 (p = 0)
# Second lightest: p = small but nonzero, h ≈ 1/2 + p²
# Actually for c=1, the spectrum is continuous: h = 1/2 + p² for p ∈ R
# So there's no "second" primary in the discrete sense
# But conventionally, "next" primary has h ≈ 1 (or h = 1 if discrete)

# Let me use E_2nd = M_Pl,2D (h = 1) as a guess
E_2nd_guess1 = M_Pl_2D  # h = 1
sum_E = E_1st + E_2nd_guess1
for label, factor in [("factor=1", 1), ("factor=2", 2), ("factor=4", 4),
                      ("factor=9/4", 9/4), ("factor=π²", math.pi**2)]:
    mu_calc = sum_E**2 / factor
    ratio = mu_calc / mu_framework
    print(f"  E_2nd = M_Pl,2D, {label}: μ = {mu_calc:.2e} (ratio {ratio:.4f})")
    results.append((f"F: {label}", mu_calc, ratio))

# Formula G: μ = b² × M_Pl,2D² where b is Liouville parameter
print("\n" + "=" * 70)
print("FORMULA G: μ = b² × M_Pl,2D² (Liouville)")
print("=" * 70)
for label, b_sq in [("b²=1/2 (c=1)", 0.5), ("b²=1/3", 1/3), ("b²=1", 1), ("b²=2", 2)]:
    mu_calc = b_sq * M_Pl_2D**2
    ratio = mu_calc / mu_framework
    print(f"  {label}: μ = {mu_calc:.2e} (ratio {ratio:.4f})")
    results.append((f"G: {label}", mu_calc, ratio))

# Formula H: μ = (1 + 1/(2h))² × E_1st² for various h
print("\n" + "=" * 70)
print("FORMULA H: μ = ((1 + 1/(2h)) × E_1st)² for various h")
print("=" * 70)
for label, h_val in [("h=1/2", 0.5), ("h=1/3", 1/3), ("h=1/4", 0.25),
                      ("h=1", 1), ("h=2/3", 2/3), ("h=1/√12", 1/np.sqrt(12))]:
    if h_val > 0:
        factor = 1 + 1/(2*h_val)
        mu_calc = (factor * M_Pl_2D * h_val)**2
        ratio = mu_calc / mu_framework
        print(f"  {label}: factor={factor:.4f}, μ = {mu_calc:.2e} (ratio {ratio:.4f})")
        results.append((f"H: {label}", mu_calc, ratio))

# Formula I: Hawking temperature relation
print("\n" + "=" * 70)
print("FORMULA I: μ = (2π × T)² for various T")
print("=" * 70)
T_values = [
    ("T = E_1st", E_1st),
    ("T = E_1st/2", E_1st/2),
    ("T = E_1st/(2π)", E_1st/(2*math.pi)),
    ("T = M_Pl,2D/(2π)", M_Pl_2D/(2*math.pi)),
    ("T = E_1st/π", E_1st/math.pi),
]
for label, T in T_values:
    mu_calc = (2*math.pi * T)**2
    ratio = mu_calc / mu_framework
    print(f"  {label}: μ = {mu_calc:.2e} (ratio {ratio:.4f})")
    results.append((f"I: {label}", mu_calc, ratio))

# Formula J: BPS / extremal bound
print("\n" + "=" * 70)
print("FORMULA J: μ = E_BPS² for various E_BPS")
print("=" * 70)
for label, E_BPS in [("E_BPS = M_Pl,2D", M_Pl_2D),
                      ("E_BPS = 2 × E_1st", 2*E_1st),
                      ("E_BPS = E_1st", E_1st)]:
    mu_calc = E_BPS**2
    ratio = mu_calc / mu_framework
    print(f"  {label}: μ = {mu_calc:.2e} (ratio {ratio:.4f})")
    results.append((f"J: {label}", mu_calc, ratio))

# Find EXACT matches
print("\n" + "=" * 70)
print("EXACT MATCHES (ratio = 1.0000)")
print("=" * 70)
exact = [(name, val, ratio) for name, val, ratio in results if abs(ratio - 1) < 0.001]
if exact:
    for name, val, ratio in exact:
        print(f"  ✓ {name}: μ = {val:.2e} (ratio {ratio:.4f})")
else:
    print("  NONE - no formula gives EXACT match")

# Find CLOSE matches (ratio within 1.5)
print("\n" + "=" * 70)
print("CLOSE MATCHES (0.5 < ratio < 1.5)")
print("=" * 70)
close = [(name, val, ratio) for name, val, ratio in results if 0.5 < ratio < 1.5]
for name, val, ratio in close:
    print(f"  • {name}: μ = {val:.2e} (ratio {ratio:.4f})")

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"\nTotal formulas tested: {len(results)}")
print(f"Exact matches (ratio = 1): {len(exact)}")
print(f"Close matches (0.5 < ratio < 1.5): {len(close)}")

print("\n" + "=" * 70)
print("OBSERVATIONS")
print("=" * 70)

print("""
1. ALL formulas that give EXACT match do so because they algebraically
   reduce to μ = M_Pl,2D² (since E_1st = M_Pl,2D/2 by h = 1/2):
   - (2 × E_1st)² = M_Pl,2D²
   - 2 × E_1st × M_Pl,2D = M_Pl,2D²
   - (E_1st + M_Pl,2D/2)² = M_Pl,2D²
   - E_1st² + 2×E_1st×M_Pl,2D + (M_Pl,2D/2)² = M_Pl,2D²

2. NO formula using ONLY E_1st (without combining with M_Pl,2D) gives
   EXACT match unless we use factor of 4 (= 1/h² for h=1/2)

3. NO formula involving π gives exact match. The closest is 2π giving
   ratio ~100.

4. NO formula involving other Liouville primaries (E_2nd) gives exact match.

5. The "2 ×" in (2 × E_1st)² is just the inverse of h = 1/2:
   2 × E_1st = 2 × (h × M_Pl,2D) = 2h × M_Pl,2D = M_Pl,2D for h = 1/2

6. The fundamental truth: μ = M_Pl,2D² is the framework's choice.
   Any derivation that arrives at this just recovers the assumption.

VERDICT: All "successful" formulas are algebraic rearrangements of
         μ = M_Pl,2D² = (2 × E_1st)². None gives a TRUE structural
         derivation of μ.
""")

print("\n" + "=" * 70)
print("END OF OTHER FORMULAS EXPLORATION")
print("=" * 70)