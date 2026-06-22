#!/usr/bin/env python3
"""
v3.5.7+ CASCADE EXTENDS TO 0 AND NEGATIVE DIMENSIONS
=======================================================

USER QUESTION (2026-06-20): "what happens if we extend it all the 
way till it reaches 0 or negative?"

EXPLORATION: What does the geometric factor formula do as n → -∞?

Formula: A_n = 2π^((n+1)/2) / Γ((n+1)/2)

KEY FINDINGS:
- Peak at n=6 (factor 33.07, S^6)
- Factors decrease past peak
- A_n crosses 1 at n ≈ 17
- A_n → 0 as n → ∞
- At n = -1: A_n = 0 (gamma pole)
- At n = -2: A_n = -1/π ≈ -0.318 (NEGATIVE!)
- At n = -3: A_n = 0 (gamma pole)
- At n = -4: A_n = +0.152 (POSITIVE)

Negative areas are mathematical curiosities that appear in:
- Zeta function regularization
- Divergent series
- String theory formalisms

PHYSICAL INTERPRETATION:
- The cone has a NATURAL RANGE from n=1 to n ≈ 17
- Past n ≈ 17, cone structure WEAKENS (factors < 1)
- At n → ∞, cone DISSOLVES (factors → 0)
- At n = 0, A_n = 2 (mathematically OK, physically nonsense)
- At n < 0, geometry becomes ill-defined (negative areas)


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
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def sphere_area(n):
    """Surface area of unit n-sphere."""
    try:
        result = 2 * math.pi**((n+1)/2) / math.gamma((n+1)/2)
        if math.isnan(result) or math.isinf(result):
            return None
        return result
    except (ValueError, OverflowError, ZeroDivisionError):
        return None


# Compute for all reasonable n
print("=" * 70)
print("EXTENDING CASCADE TO ALL n (INCLUDING NEGATIVE)")
print("=" * 70)
print()

print(f"{'n':<6} {'Transition':<14} {'A_n':<15} {'Behavior':<30}")
print("-" * 70)

for n in range(-4, 30):
    A_n = sphere_area(n)
    trans = f"{n}D → {n+1}D"
    
    if A_n is None:
        A_n_str = "undefined"
        behavior = "(gamma pole)"
    elif A_n < 0:
        A_n_str = f"{A_n:.4f}"
        behavior = "NEGATIVE area!"
    elif n == 0:
        A_n_str = f"{A_n:.4f}"
        behavior = "point (0D)"
    elif n < 6:
        A_n_str = f"{A_n:.4f}"
        behavior = "INCREASING"
    elif n == 6:
        A_n_str = f"{A_n:.4f}"
        behavior = "PEAK (33.07)"
    elif n <= 17:
        A_n_str = f"{A_n:.4f}"
        behavior = "DECREASING"
    elif n <= 22:
        A_n_str = f"{A_n:.4f}"
        behavior = "FADING (< 1)"
    else:
        A_n_str = f"{A_n:.4e}"
        behavior = "≈ 0 (dissolving)"
    
    print(f"{n:<6} {trans:<14} {A_n_str:<15} {behavior:<30}")

print()
print("=" * 70)
print("KEY OBSERVATIONS")
print("=" * 70)
print()

# Specific values
print("Specific values of interest:")
print(f"  A_0 = 2 (mathematically valid, physically nonsense)")
print(f"  A_6 = {sphere_area(6):.4f} (PEAK)")
print(f"  A_-2 = {sphere_area(-2):.4f} (NEGATIVE area)")
print(f"  A_-1 = undefined (gamma pole)")
print(f"  A_-3 = undefined (gamma pole)")
print(f"  A_-4 = {sphere_area(-4):.4f} (positive, small)")
print()

# Find where A_n crosses various thresholds
print("Where A_n crosses various thresholds:")
for threshold in [10, 1, 0.5, 0.1, 0.01]:
    for n in range(0, 40):
        A_n = sphere_area(n)
        if A_n is not None and A_n < threshold:
            print(f"  A_n = {threshold} at n = {n} (A_{n} = {A_n:.4f})")
            break

print()
print("=" * 70)
print("CONE LIFESPAN")
print("=" * 70)
print()
print("The cone has a NATURAL RANGE:")
print("  n = 1 to n ≈ 17: cone structure meaningful (factors > 1)")
print("  n > 17: cone structure WEAKENS (factors < 1)")
print("  n → ∞: cone DISSOLVES (factors → 0)")
print()
print("Framework's choice of 4D (n=2 → n=3) is well within the natural range.")
print("Cone COULD extend to n=17 before fading.")
print("Past n=17, the cone becomes 'flat' (no geometric distinction).")
print()
print("=" * 70)
print("WHAT HAPPENS AT 0 OR NEGATIVE")
print("=" * 70)
print()
print("AT n = 0:")
print("  A_0 = 2 (factor at 0D → 1D)")
print("  0D is a point — no spatial extent")
print("  Framework EXCLUDES 0D/1D (cone terminates at 2D)")
print()
print("AT n < 0 (negative dimensions):")
print("  n = -1: A_n = 0 (gamma pole)")
print("  n = -2: A_n = -1/π ≈ -0.318 (NEGATIVE area!)")
print("  n = -3: A_n = 0 (gamma pole)")
print("  n = -4: A_n = 3/(2π²) ≈ 0.152 (small positive)")
print()
print("Negative dimensions are MATHEMATICAL CURIOSITIES:")
print("  - Zeta function regularization")
print("  - Divergent series summation")
print("  - String theory formalisms")
print("  - Not physical dimensions")
print()
print("Interpretation: The cone has a 'boundary' at 2D (framework's choice).")
print("Below 2D: 1D, 0D, negative-d are MATHEMATICALLY DEFINED but PHYSICALLY NONSENSICAL.")
print("Above 4D: cone COULD extend to n=17 before fading.")

# Plot the full extension
fig, ax = plt.subplots(figsize=(14, 6))

# Sample n values
n_values = np.arange(-4, 30, 0.1)
A_values = []
for n in n_values:
    A = sphere_area(n)
    if A is None:
        A_values.append(np.nan)
    else:
        A_values.append(A)

ax.semilogy(n_values, np.abs(A_values), 'b-', linewidth=2, label='|A_n| (log scale)')

# Highlight key points
key_n = [-2, 0, 2, 6, 17]
for n in key_n:
    A = sphere_area(n)
    if A is not None:
        ax.plot(n, abs(A), 'ro', markersize=10)
        label = f"n={n}: A={A:.3f}" if A > 0 else f"n={n}: A={A:.3f} (NEG)"
        ax.annotate(label, (n, abs(A)), textcoords="offset points",
                    xytext=(10, 10), fontsize=10)

# Highlight peak
peak_n = 6
peak_A = sphere_area(peak_n)
ax.axvline(x=peak_n, color='red', linestyle='--', alpha=0.5,
           label=f'Peak at n=6 (A={peak_A:.2f})')

# Highlight where A=1
ax.axhline(y=1, color='green', linestyle=':', alpha=0.5, label='A_n = 1')

ax.set_xlabel('Cascade transition: nD → (n+1)D', fontsize=12)
ax.set_ylabel('|Geometric factor A_n| (log scale)', fontsize=12)
ax.set_title('Geometric Factor A_n for Cascade Transitions\n(extends from negative-n to n=∞)',
             fontsize=14)
ax.grid(True, alpha=0.3, which='both')
ax.legend(loc='upper right')
ax.set_xlim(-4, 30)
ax.set_ylim(0.001, 100)

# Mark the framework's 4D choice
ax.axvspan(1, 3, alpha=0.2, color='blue', label='Framework range (2D→4D)')

plt.tight_layout()
plt.savefig('/workspace/github-repo/calculations/plots/cone_extends_to_zero.png',
            dpi=120, bbox_inches='tight')
print()
print("Saved plot: calculations/plots/cone_extends_to_zero.png")
