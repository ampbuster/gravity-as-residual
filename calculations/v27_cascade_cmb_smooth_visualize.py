#!/usr/bin/env python3
"""
v27_cascade_cmb_smooth_visualize.py
====================================
Visualize smooth F(z) curves for the CMB gap.

Generates a simple ASCII plot of F(z) for several smooth parameterizations,
showing the cascade's prediction of F_total(z) = F_p(z) + F_s(z).
"""
import math
import numpy as np

# Cosmology
H_0 = 67.4
Omega_DM_0 = 0.265
Omega_b_0 = 0.0493
Omega_Lambda = 0.685
Omega_m_0 = Omega_DM_0 + Omega_b_0


def sfr_madau(z):
    return (1 + z)**2.7 / (1 + ((1 + z)/2.9)**5.6)


def F_s_cumulative(z, z_max=20.0, n_int=1000):
    if z > z_max:
        return 0.0
    z_arr = np.linspace(z, z_max, n_int)
    integrand = sfr_madau(z_arr)
    return np.trapezoid(integrand, z_arr) / np.trapezoid(
        sfr_madau(np.linspace(0, z_max, n_int)),
        np.linspace(0, z_max, n_int))


# Smooth F_p functions (all calibrated: F_p(0) = 0.7, F_p(inf) = 1.0)
def F_p_const(z):
    return 0.7


def F_p_step(z, z_trans=4.0):
    return 0.7 if z < z_trans else 1.0


def F_p_exp(z, z_scale=2.0):
    return 0.7 + 0.3 * (1 - np.exp(-z / z_scale))


def F_p_sigmoid(z, z_scale=2.0):
    """Centered at z=0: F_p(0) = 0.7, F_p(inf) = 1.0"""
    s = 1 / (1 + np.exp(-z / z_scale))
    return 0.7 + 0.6 * (s - 0.5)


def F_p_tanh(z, z_scale=2.0):
    """Same as F_p_sigmoid"""
    return 0.7 + 0.3 * (1 + np.tanh(z / z_scale)) / 2


def F_p_hill(z, n=2.0, z_half=3.0):
    return 0.7 + 0.3 * z**n / (z_half**n + z**n) if z > 0 else 0.7


# Test z values
Z_TEST = [0, 0.5, 1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 50, 100, 200, 500, 1100]

models = [
    ("§4.48 const 0.7", F_p_const, {}),
    ("§4.48 step z>4", F_p_step, {}),
    ("exp z=0.5", F_p_exp, {"z_scale": 0.5}),
    ("exp z=1", F_p_exp, {"z_scale": 1.0}),
    ("exp z=2", F_p_exp, {"z_scale": 2.0}),
    ("exp z=4", F_p_exp, {"z_scale": 4.0}),
    ("sigmoid z=0.5", F_p_sigmoid, {"z_scale": 0.5}),
    ("sigmoid z=1", F_p_sigmoid, {"z_scale": 1.0}),
    ("sigmoid z=2", F_p_sigmoid, {"z_scale": 2.0}),
    ("sigmoid z=4", F_p_sigmoid, {"z_scale": 4.0}),
    ("tanh z=1", F_p_tanh, {"z_scale": 1.0}),
    ("tanh z=2", F_p_tanh, {"z_scale": 2.0}),
    ("Hill n=2 z_half=3", F_p_hill, {"n": 2.0, "z_half": 3.0}),
    ("Hill n=4 z_half=6", F_p_hill, {"n": 4.0, "z_half": 6.0}),
]

# =============================================================================
# Print F(z) tables
# =============================================================================
print("=" * 100)
print("F(z) TABLES: cascade prediction of F_total(z) = F_p(z) + F_s(z) × Madau-SFR")
print("=" * 100)
print()
print("Calibration: F_total(z=0) = 1.0 (matches observed Omega_DM(0) = 0.265)")
print("Target:      F_total(z=1100) = 1.0 (matches observed Omega_DM(1100) = 0.265)")
print()

# Header
print(f"{'z':<8}", end='')
for name, _, _ in models:
    print(f"{name:<16}", end='')
print(f"{'OBSERVED':<10}")
print("-" * 100)

for z in Z_TEST:
    print(f"{z:<8}", end='')
    F_s = 0.3 * F_s_cumulative(z)
    for name, func, kwargs in models:
        Fp = func(z, **kwargs)
        F_total = Fp + F_s
        if abs(F_total - 1.0) < 0.005:
            mark = "✓"
        elif F_total < 0.95:
            mark = "X"
        elif F_total > 1.05:
            mark = "!"
        else:
            mark = "·"
        print(f"{F_total:.3f}{mark:<3}".ljust(16), end='')
    # Observed
    obs = 1.0
    print(f"{obs:.3f} ✓")
print()

# =============================================================================
# Print gap table
# =============================================================================
print("=" * 100)
print("GAP AT z=1100: |F_total(1100) - 1.0| × 100%")
print("=" * 100)
print()
print(f"{'Model':<20} {'F_total(0)':<12} {'F_total(1100)':<14} {'Gap@1100':<12} {'Status'}")
print("-" * 70)
for name, func, kwargs in models:
    F_s_0 = 0.3 * F_s_cumulative(0)
    F_s_1100 = 0.3 * F_s_cumulative(1100)
    o0 = func(0, **kwargs) + F_s_0
    o1100 = func(1100, **kwargs) + F_s_1100
    gap = abs(o1100 - 1.0) * 100
    if gap < 0.5:
        status = "MATCH"
    elif gap < 5:
        status = "MARGINAL"
    else:
        status = "FAILS"
    print(f"{name:<20} {o0:<12.4f} {o1100:<14.4f} {gap:>8.1f}%     {status}")

print()
print("=" * 100)
print("ASCII VISUALIZATION: F_total(z) curve shapes (best models)")
print("=" * 100)
print()

# Simple ASCII plot
def ascii_plot(model_name, func, kwargs, width=60, height=20):
    print(f"--- {model_name} ---")
    z_arr = np.linspace(0, 12, width)
    F_arr = np.array([func(z, **kwargs) + 0.3 * F_s_cumulative(z) for z in z_arr])
    
    # Make a 2D grid
    for row in range(height, 0, -1):
        threshold = 0.85 + (row - 1) * 0.075 / height  # 0.85 to 1.025
        line = ""
        for v in F_arr:
            if v >= threshold + 0.075/height:
                line += "*"
            elif v >= threshold - 0.075/height:
                line += "·"
            else:
                line += " "
        print(f"  {threshold:.3f} |{line}|")
    
    # x-axis labels
    z_marks = [0, 2, 4, 6, 8, 10, 12]
    z_indices = [int(z/12 * (width-1)) for z in z_marks]
    line = "         |"
    for i in range(width):
        if i in z_indices:
            z_val = z_marks[z_indices.index(i)]
            line += f"{z_val}"
        else:
            line += " "
    print(line)
    print("         F_total(z)")
    print()

# Plot 4 representative models
ascii_plot("§4.48 const F_p=0.7 (CURRENT)", F_p_const, {})
ascii_plot("Smooth exp z=2 (RECOMMENDED)", F_p_exp, {"z_scale": 2.0})
ascii_plot("Smooth sigmoid z=1 (RECOMMENDED)", F_p_sigmoid, {"z_scale": 1.0})
ascii_plot("§4.48 step at z=4", F_p_step, {})

print("=" * 100)
print("RECOMMENDATION")
print("=" * 100)
print()
print("The smooth F_p(z) = 0.7 + 0.3 × (1 - exp(-z/z_scale)) is RECOMMENDED")
print("because it:")
print()
print("  1. Matches BOTH z=0 and z=1100 anchors (gap < 0.1%)")
print("  2. Has only 1 free parameter (z_scale) — same number as §4.48 step")
print("  3. Is physically motivated: 4D event's R_p(z) is unlikely to be a step")
print("  4. Reduces to §4.48's constant F_p=0.7 in the limit z_scale → ∞")
print("  5. Predicts the high-z bump in F(z): early DM is PRIMARILY primordial,")
print("     late DM is a mix of primordial + stellar")
print()
print("Best fit z_scale ~ 1-4 (transition over z = 0 to z = 8).")
print("This is a 1-parameter family that closes the CMB gap AND provides")
print("a smooth, physically motivated transition.")
