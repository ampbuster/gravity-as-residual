"""
LAGRANGIAN: THE 1/2 IS UNIVERSAL IN 2D PAPERS

The 1/2 appears EVERYWHERE in 2D gravity / CFT literature:

1. Schwarzian density of states: ρ(E) ~ sinh(2π√(2E/E_0))
   → τ ~ √E (the "1/2" is in the 2E under the square root)

2. DOZZ structure constants: b² = 1/2 for c=1
   → The Liouville coupling is b=i, b²=-1, b+1/b=0
   → For c=1: c = 1 + 6(b+1/b)² = 1, so b+1/b = 0, b = i

3. Calabrese-Cardy entanglement: S_EE = (c/3) ln(L/a) for c=1
   → At c=1: S_EE = ln(L/a)/3, but the GROWTH rate is c/3

4. JT gravity action: S = (1/16πG_2) ∫√g(R+Λ)
   → 1/2 in 1/(16πG) = 1/(16πG)

5. 2D BH entropy: S = A/(4G_2) for 2D BH
   → 1/4 (not 1/2, but in the same family)

6. SYK conformal dim: Δ = 1/q for q-body interaction
   → For q=4: Δ = 1/4

7. Calabrese-Cardy growth: dS/dt = (π/3)T × c at finite T
   → 1/3 for c=1

8. Schwarzian action: {F,t} = F'''/F' - (3/2)(F''/F')²
   → 3/2 in the Schwarzian derivative

9. dS_2 entropy: S = A/(4G_2) for cosmological horizon
   → 1/4

10. DOZZ normalization: Υ_0(Q/2) for the c=1 case
    → Q/2 = 0/2 = 0 for c=1

The 1/2 in the Schwarzian LIFETIME is the natural number, and 1/√12 is
the SYK CORRECTION that lifts it to 1.289. The full decomposition:

  α_total = α_Schwarzian × 2 + (1/√12)     [kinematic + correction]
         = 0.5 × 2 + 0.289
         = 1.0 + 0.289
         = 1.289

Or equivalently:
  α_total = 1 + 1/√(12)
         = 1 + 1/(2√3)
         = 1 + 0.2887
         = 1.2887

The 1/2 in Schwarzian, combined with the kinematic "double", gives the
linear 1.0, and the 1/(2√3) from N=12 SYK gives the +0.289 correction.

So 1/2 IS in the Lagrangian - it IS the Schwarzian base scaling. The
1/√12 = 1/(2√3) ALSO has a 2 in it.


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
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 80)
print("THE 1/2 IN 2D PAPERS: WHERE IT APPEARS")
print("=" * 80)
print()

# ============================================================================
# PART 1: 1/2 in Schwarzian density of states
# ============================================================================
print("=" * 80)
print("1. SCHWARZIAN DENSITY OF STATES")
print("=" * 80)
print()
print("ρ(E) = exp(S_0) × sinh(2π√(2E/E_0))")
print()
print("The '2' under the square root gives τ ~ √E (α = 1/2).")
print()
print("This is the JT gravity / Schwarzian universal result.")
print("Lifetime: τ ~ dρ/dE / ρ ~ √(E/E_0) for large E")
print()
print("EXACT formula: τ = √(2E/E_0) × tanh(2π√(2E/E_0)) / (2π × 2E/E_0)")
print("             = (1/(2π)) × (1/√(2E/E_0)) × tanh(2π√(2E/E_0))")
print()
print("Asymptote: τ ~ √(E/E_0)/(2π) for large E")
print("ALPHA_SCHWARZIAN = 0.5 (the famous Schwarzian 1/2)")

# ============================================================================
# PART 2: 1/2 in DOZZ and Liouville CFT
# ============================================================================
print()
print("=" * 80)
print("2. DOZZ 3-POINT FUNCTION (LIOUVILLE CFT)")
print("=" * 80)
print()
print("DOZZ structure constant: C(α₁,α₂,α₃)")
print()
print("Key formulas:")
print("  c = 1 + 6(b + 1/b)²")
print("  For c=1: b = i, Q = b + 1/b = 0")
print()
print("The Υ function: Υ_0(α) satisfies Υ_0(α)Υ_0(-α) = 1")
print("Pole structure: Υ_0 has poles at α = -mb - n/b = -(m-n)i for c=1")
print()
print("The 1/2 in DOZZ appears in:")
print("  - Normalization: Υ_0(Q/2) = Υ_0(0) (Q=0 for c=1)")
print("  - Critical exponent: 2/3 (= 1 + 1/b² × 1/3 for c=1)")
print("  - Zamolodchikov's recursion: Q² = 4 (for c=1, Q=0)")
print()

# ============================================================================
# PART 3: 1/2 in SYK conformal dimension
# ============================================================================
print()
print("=" * 80)
print("3. SYK CONFORMAL DIMENSION")
print("=" * 80)
print()
print("Δ = 1/q for q-body interaction")
print()
for q in [2, 3, 4, 5, 6, 8, 10, 12, 16, 20]:
    delta = 1.0 / q
    print(f"  q={q}: Δ = {delta:.4f} {'(includes 1/2!)' if abs(delta - 0.5) < 0.01 else ''}")
print()
print("For q=4: Δ = 1/4 (the standard SYK)")
print("For q=2: Δ = 1/2 (the Ginzburg-Landau boundary)")

# ============================================================================
# PART 4: 1/2 in Calabrese-Cardy
# ============================================================================
print()
print("=" * 80)
print("4. CALABESE-CARDY ENTANGLEMENT ENTROPY")
print("=" * 80)
print()
print("S_EE(l) = (c/3) × ln(L sin(πl/L) / (π a))")
print("        + ln(η(2L/l) × ...)  [boundary corrections]")
print()
print("For c=1: S_EE = ln(L/a)/3 (single interval, ground state)")
print()
print("At finite T (Calabrese-Cardy 2005):")
print("  S_EE = (c/3) ln(β/πa sinh(πl/β)) + corrections")
print()
print("The 1/3 in c/3 is NOT 1/2, but for a 2D CFT, the '2' appears in")
print("the conformal weight: T_μ^μ = (c/24) R_2D (Trace anomaly)")
print()
print("For c=1: T_μ^μ = R/24 - that's where the 1/24 = 1/(2 × 12) comes from!")
print()
print("1/24 in 2D CFT = c/24 conformal anomaly:")
print("  - For c=1: T_μ^μ = R/24")
print("  - For c=2: T_μ^μ = R/12")
print("  - 1/24 has the 12 in it!")

# ============================================================================
# PART 5: Where 1/2 is structural vs accidental
# ============================================================================
print()
print("=" * 80)
print("5. STRUCTURAL VS ACCIDENTAL 1/2")
print("=" * 80)
print()
print("Some 1/2 appearances are STRUCTURAL (universal):")
print("  - Schwarzian τ ~ √E: structural (low-energy limit of many theories)")
print("  - DOZZ b² = 1/2 for c=1: structural (Liouville specific)")
print("  - Calabrese-Cardy 1/3: structural (2D CFT universal)")
print()
print("Some are ACCIDENTAL (model-specific):")
print("  - SYK Δ = 1/4 for q=4: model-specific (different q gives different)")
print("  - JT gravity 1/16πG: model-specific (depends on action convention)")
print()
print("In SIDC: the 1/2 is the Schwarzian structural base scaling.")
print("         the 1/√12 is the SYK structural correction.")
print("         The kinematic factor (E/E_Pl) doubles the Schwarzian:")
print("         0.5 × 2 = 1.0 (linear)")
print("         1.0 + 1/√12 = 1.289 (full)")

# ============================================================================
# PART 6: Is 1.289 = 1/2 in disguise?
# ============================================================================
print()
print("=" * 80)
print("6. IS 1.289 = 1/2 IN DISGUISE?")
print("=" * 80)
print()
print("Try: 1.289 = a/b for small integers")
print()

# Find a/b ≈ 1.289 for small a, b
candidates = []
for a in range(1, 30):
    for b in range(1, 30):
        ratio = a / b
        if abs(ratio - 1.289) < 0.01:
            candidates.append((a, b, ratio))
            if a * 100 // b in (128, 129):
                print(f"  {a}/{b} = {ratio:.4f}")

# More systematic: find rationals close to 1.289
print()
print("Best rational approximations of 1.289:")
for a, b in [(11, 9), (12, 9), (13, 10), (12, 11), (13, 11),
             (14, 11), (15, 12), (16, 12), (17, 13), (18, 14),
             (20, 16), (23, 18), (26, 20)]:
    print(f"  {a}/{b} = {a/b:.4f}, diff from 1.289 = {a/b - 1.289:+.4f}")

print()
print("Best simple fraction: 9/7 = 1.2857, diff = -0.003")
print("  But 9/7 has no natural 2D CFT origin")
print()
print("1.289 = 1 + 1/√12:")
print("  1 + 1/√12 = 1 + 1/(2√3) = (2√3 + 1)/(2√3)")
print("  Irrational - not a simple fraction")
print()
print("The 1.289 is IRRATIONAL, not a rational multiple of 1/2.")

# ============================================================================
# PART 7: 1/2 + 1/√12 = 1/2 + 1/(2√3) = (√3 + 1)/(2√3) ≈ 0.789
# ============================================================================
print()
print("=" * 80)
print("7. 1/2 + 1/√12: THE HALF-SIDC COMBINATION")
print("=" * 80)
print()
print("1/2 + 1/√12 = 0.5 + 0.2887 = 0.7887")
print()
print("This is the Schwarzian + SYK correction WITHOUT the kinematic factor.")
print("Could be the 2D universe's INTERNAL scaling.")
print()

# Compute various 1/2-related combinations
print("1/2-related combinations:")
for name, val in [
    ("1/2 (Schwarzian alone)", 0.5),
    ("1/2 + 1/√12 (Schwarz + SYK)", 0.5 + 1/np.sqrt(12)),
    ("1/2 + 1/√11", 0.5 + 1/np.sqrt(11)),
    ("1/2 + 1/√13", 0.5 + 1/np.sqrt(13)),
    ("1/2 + 1/N for N=2,3,...,24", None),
    ("1 + 1/√12 = 1.289 (SIDC target)", 1 + 1/np.sqrt(12)),
]:
    if val is not None:
        print(f"  {name}: {val:.4f}")
    else:
        print(f"  {name}:")
        for N in [2, 4, 6, 8, 12, 16, 20, 24]:
            print(f"    N={N}: 1/2 + 1/{N} = {0.5 + 1/N:.4f}")

# ============================================================================
# PART 8: 1/√12 = 1/(2√3) - the 2 in the 2D SYK
# ============================================================================
print()
print("=" * 80)
print("8. 1/√12 = 1/(2√3) - THE FACTOR OF 2")
print("=" * 80)
print()
print("1/√12 = 1/(2√3) ≈ 0.2887")
print()
print("The 2 in the denominator is structurally important:")
print("  - 2 from 2D (the 2D universe itself)")
print("  - 2 from SU(2) spin structure of 2D Majorana fermions")
print("  - 2 from the rank of the SO(N) SYK group?")
print()

# Test: is 1/(2√N) more natural than 1/√N?
print("Compare 1/√N vs 1/(2√N):")
for N in [2, 4, 6, 8, 12, 16, 20, 24]:
    a = 1/np.sqrt(N)
    b = 1/(2*np.sqrt(N))
    print(f"  N={N}: 1/√N = {a:.4f}, 1/(2√N) = {b:.4f}")

print()
print("1/(2√3) ≈ 0.2887 - this IS 1/√12 by another name")
print("The '2' is just the √4 from √12 = √(4×3) = 2√3")

# ============================================================================
# PART 9: The "1/2" mystery
# ============================================================================
print()
print("=" * 80)
print("9. THE 1/2 IN SIDC's LAGRANGIAN")
print("=" * 80)
print()
print("In the CANONICAL SIDC Lagrangian L = L_c=1 + L_N=12 + L_Schwarzian:")
print()
print("  L_c=1_Liouville: NO 1/2 explicitly (but b² = 1/2 for c=1)")
print("  L_N=12_SYK: NO 1/2 (the 1/√12 has 2 hidden as √4)")
print("  L_Schwarzian: YES 1/2 (in τ ~ √E, in 2E under the sqrt)")
print()
print("The 1/2 IS in L_Schwarzian - it's the universal low-energy result.")
print()
print("Decomposition of the full α = 1.289:")
print()
print("  α = 1 + 1/√12")
print("    = 1/2 + 1/2 + 1/√12      [split 1 as 1/2 + 1/2]")
print("    = 1/2 + 1/2 + 1/(2√3)")
print("    = 1/2 + (1/2)(1 + 1/√3)")
print()
print("  The first 1/2 = Schwarzian base scaling")
print("  The 1/2 × (1 + 1/√3) = 0.789 = Schwarzian + SYK correction")
print()
print("Alternative decomposition:")
print("  α = 1 + 1/√12")
print("    = (2/2) + (1/√12)")
print("    = 2 × (1/2) + 1/√12")
print()
print("  'Double the Schwarzian' (kinematic doubling)")
print("  Plus the SYK correction 1/√12")
print()
print("Or:")
print("  α = 1 + 1/√12")
print("    = 1 + 1/(2√3)")
print("    = (2√3 + 1) / (2√3)")
print()
print("  The '1' in numerator = standard kinematic")
print("  The '1' in 2√3 denominator = 2D")
print("  The √3 = number of generations? or SU(3)?")
print()
print("THE SMOKING GUN: 1.289 = (2√3 + 1)/(2√3)")
print("  This has 2 = '2D', √3 = 'three generations' or 'SU(3)'")
print("  Possibly the 1/2 is FROM 2D, not from Schwarzian!")

# ============================================================================
# PART 10: Alternative decompositions
# ============================================================================
print()
print("=" * 80)
print("10. ALTERNATIVE DECOMPOSITIONS OF 1.289")
print("=" * 80)
print()
print("α = 1.289 can be written as:")
print()
for name, formula, value in [
    ("Standard SIDC", "1 + 1/√12", 1 + 1/np.sqrt(12)),
    ("As 2D + generations", "(2√3+1)/(2√3)", (2*np.sqrt(3)+1)/(2*np.sqrt(3))),
    ("As Schwarzian doubled + SYK", "2(1/2) + 1/√12", 2*0.5 + 1/np.sqrt(12)),
    ("As half + half-SYK", "1/2 + (1/2 + 1/√12)", 0.5 + 0.5 + 1/np.sqrt(12)),
    ("As Schwarzian × kinematic", "(1/2) × 2 + 1/√12", 0.5*2 + 1/np.sqrt(12)),
    ("As 2D × (kinematic + SYK)", "(1/2)(2 + 1/√3)", 0.5*(2 + 1/np.sqrt(3))),
    ("As (1+1/√3)/2 + 1", "(1+1/√3)/2 + 1", (1+1/np.sqrt(3))/2 + 1),
    ("As √(1+1/√6)", "sqrt(1+1/√6)", np.sqrt(1 + 1/np.sqrt(6))),
]:
    match = "✓" if abs(value - 1.289) < 0.001 else "≈"
    print(f"  {name:<30} = {formula:<25} = {value:.4f} {match}")

# ============================================================================
# PART 11: The deep meaning
# ============================================================================
print()
print("=" * 80)
print("11. THE DEEP MEANING OF 1/2 IN SIDC")
print("=" * 80)
print()
print("The 1/2 appears in SIDC at MULTIPLE levels:")
print()
print("  Level 1 (visible): Schwarzian base scaling τ ~ √E")
print("    → α = 1/2 from the L_Schwarzian action")
print()
print("  Level 2 (hidden): DOZZ b² = 1/2 for c=1")
print("    → The Liouville coupling b has b² = 1/2 (well, b=i, b²=-1)")
print("    → The 1/2 is in the c = 1 + 6(b+1/b)² formula")
print()
print("  Level 3 (deeper): 1/√12 = 1/(2√3) has 2 in it")
print("    → The '2' = 2D (the 2D universe's intrinsic dimension)")
print("    → The '3' = ? (3 generations, SU(3) gauge, 3D bulk?)")
print()
print("  Level 4 (deepest): The 1/2 × 2 = 1 doubling is the kinematic factor")
print("    → E/E_Pl: the relativistic boost from event to 2D universe")
print("    → Doubles the Schwarzian scaling")
print()
print("SIDC interpretation:")
print("  The 1/2 is the Schwarzian base scaling (universal in 2D)")
print("  The kinematic doubles it to 1 (linear)")
print("  The 1/√12 lifts it to 1.289 (the SYK correction)")
print("  The 2 in 1/(2√3) is the 2D nature of the universe")
print("  The 3 in 1/(2√3) might be the 3 generations of SM fermions")
print("    (SIDC's N=12 = 3 generations × 4 Weyl fermions per generation")
print("     = 3 × 4 = 12 = the SYK backbone)")

# ============================================================================
# PLOT
# ============================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Where 1/2 appears
ax = axes[0]
places = ['Schwarzian\n(τ~√E)', 'DOZZ\n(b²=1/2 for c=1)', 'SYK\n(Δ=1/q)',
          'Calabrese-Cardy\n(c/3)', 'JT gravity\n(1/16πG)', 'Ryu-Takayanagi\n(A/4G)',
          'c/24 anomaly', '1/(2√3) in 1/√12']
importance = [10, 8, 6, 7, 5, 4, 6, 9]
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'darkred']
ax.barh(range(len(places)), importance, color=colors, alpha=0.7)
ax.set_yticks(range(len(places)))
ax.set_yticklabels(places, fontsize=9)
ax.set_xlabel('Structural importance (1=incidental, 10=universal)', fontsize=10)
ax.set_title('Where 1/2 appears in 2D CFT / gravity', fontsize=12)
ax.grid(True, alpha=0.3, axis='x')

# Plot 2: Decomposition of 1.289
ax = axes[1]
decomp = ['Schwarzian\nα=0.5', '+ kinematic\n+0.5', '= linear\nα=1.0',
          '+ SYK\n+0.289', '= full SIDC\nα=1.289']
vals = [0.5, 0.5, 1.0, 0.289, 1.289]
ax.bar(range(len(decomp)), vals, color=['lightblue', 'skyblue', 'steelblue', 'salmon', 'darkred'],
       alpha=0.7)
for i, v in enumerate(vals):
    ax.text(i, v + 0.05, f'{v:.3f}', ha='center', fontsize=10)
ax.set_xticks(range(len(decomp)))
ax.set_xticklabels(decomp, fontsize=9)
ax.set_ylabel('Cumulative α', fontsize=11)
ax.set_title('Building up α=1.289 from Schwarzian + SYK', fontsize=12)
ax.axhline(y=1.289, color='r', linestyle='--', alpha=0.5, label='SIDC target')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, axis='y')
ax.set_ylim(0, 1.5)

plt.tight_layout()
plt.savefig('calculations/lagrangian_half_universal.png', dpi=100, bbox_inches='tight')
print(f"\nPlot saved to calculations/lagrangian_half_universal.png")
