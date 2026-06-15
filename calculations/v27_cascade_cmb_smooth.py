#!/usr/bin/env python3
"""
v27_cascade_cmb_smooth.py
==========================
Smooth F(z) curves vs 2-zone (§4.48 step function) for the CMB gap.

Current state (§4.48):
  F_p = 0.7 (constant primordial)
  F_s = 0.3 × SFR(z)/SFR(0) (Madau-SFR, stellar, → 0 at high z)
  At z=0: F_total = 0.7 + 0.3 = 1.0 ✓
  At z=1100: F_total = 0.7 + 0 = 0.7 (gap: rho_DM(1100)/rho_DM(0) is 3.18, not 0.7)

User's question: can a SMOOTH F(z) fit the CMB data better than the 2-zone step?

The smooth F(z) idea: the primordial component itself could have a z-dependence,
either because:
  (a) R_p(z) is z-dependent (4D event's activity profile has structure)
  (b) τ_2D(z) depends on cosmic state (E_primordial varies with epoch)
  (c) some other smooth enhancement of the early-DM contribution

This script tests several smooth F(z) parameterizations and finds the best
fit to BOTH z=0 and z=1100 anchor points.

KEY INSIGHT: the cumulative 2D universe energy ratio is z-independent
(within a few percent) for a wide class of G(E) forms. So the gap is set
by the FRACTION F(z) that is "primordial" vs "stellar", not by the
underlying energy budget.
"""
import math
import numpy as np

# =============================================================================
# Cosmology (Planck 2018)
# =============================================================================
H_0 = 67.4  # km/s/Mpc
Omega_DM_0 = 0.265
Omega_b_0 = 0.0493
Omega_Lambda = 0.685
Omega_m_0 = Omega_DM_0 + Omega_b_0

# z=0 and z=1100 anchor points
# OBSERVED Omega_DM is approximately 0.265 at both z=0 and z=1100 (Planck).
# CASCADE PREDICTS F_total(z), which is NORMALIZED so F_total(0) = 1.0.
# So we test: does F_total(z=1100) = 1.0?
Z_ANC = [0.0, 1100.0]
F_TOTAL_OBS = [1.0, 1.0]  # Both anchors should give F_total = 1.0 (calibration + Planck)

# Test z values for the curve shape
Z_TEST = [0, 1, 2, 4, 6, 8, 10, 20, 50, 100, 200, 500, 1100]

# =============================================================================
# Madau-SFR (stellar) profile (Cole+ 2001, Madau & Dickinson 2014)
# =============================================================================
def sfr_madau(z):
    """Normalized Madau SFR: peaks at z~2, drops at z=0 and z=10+"""
    return (1 + z)**2.7 / (1 + ((1 + z)/2.9)**5.6)

def sfr_normalized(z):
    """Normalize so that SFR(0) = 1"""
    return sfr_madau(z) / sfr_madau(0.0)

# Cumulative stellar contribution at z (relative to z=0)
# F_s(z) = F_s(0) × ∫_z^z_max R_s(z') dz' / ∫_0^z_max R_s(z') dz'
# (mass already created, not future mass)
# Note: this is the *cumulative* stellar mass at z, normalized to z=0

def F_s_cumulative(z, z_max=20.0, n_int=1000):
    """Fraction of total stellar 2D universe mass that has been created by z"""
    if z > z_max:
        return 0.0
    z_arr = np.linspace(z, z_max, n_int)
    integrand = sfr_madau(z_arr)
    return np.trapezoid(integrand, z_arr) / np.trapezoid(sfr_madau(np.linspace(0, z_max, n_int)),
                                                  np.linspace(0, z_max, n_int))

# =============================================================================
# Smooth F(z) functions
# =============================================================================
def F_p_const(z, **kwargs):
    """§4.48 constant: F_p = 0.7"""
    return 0.7

def F_p_step(z, **kwargs):
    """§4.48 step: F_p = 0.7 (low z) + 0.3 (high z, after z=4)"""
    return 0.7 + 0.3 * (1.0 if z > 4 else 0.0)

def F_p_sigmoid(z, z_scale=4.0, **kwargs):
    """Smooth sigmoid: F_p grows from 0.7 to 1.0 around z=z_scale"""
    return 0.7 + 0.3 / (1 + np.exp(-(z - z_scale) / (z_scale / 4)))

def F_p_exponential(z, z_scale=2.0, **kwargs):
    """Exponential: F_p = 1 - 0.3 × exp(-z/z_scale)"""
    return 1 - 0.3 * np.exp(-z / z_scale)

def F_p_hill(z, n=2.0, z_half=3.0, **kwargs):
    """Hill: F_p = 0.7 + 0.3 × z^n / (z_half^n + z^n)"""
    return 0.7 + 0.3 * z**n / (z_half**n + z**n) if z > 0 else 0.7

def F_p_tanh(z, z_scale=2.0, **kwargs):
    """tanh: smooth step"""
    return 0.7 + 0.3 * (np.tanh(z / z_scale) + 1) / 2  # goes from 0.7 to 1.0

# =============================================================================
# Total F(z) and predicted Omega_DM(z)
# =============================================================================
def Omega_DM_cascade(z, F_p_func, F_p_kwargs={}, F_s_0=0.3):
    """Predicted Omega_DM(z) given the cascade F(z) decomposition"""
    F_p = F_p_func(z, **F_p_kwargs)
    F_s = F_s_0 * F_s_cumulative(z)
    return F_p + F_s

# =============================================================================
# Cost function: fit both anchor points
# =============================================================================
def cost(F_p_func, F_p_kwargs={}, F_s_0=0.3):
    """Sum of squared log-ratios at z=0 and z=1100"""
    cost_val = 0
    for z, target in zip(Z_ANC, F_TOTAL_OBS):
        pred = Omega_DM_cascade(z, F_p_func, F_p_kwargs, F_s_0)
        if pred <= 0:
            return 1e10
        cost_val += (math.log(pred / target))**2
    return cost_val

# =============================================================================
# Run comparison
# =============================================================================
def main():
    print("=" * 80)
    print("SMOOTH F(z) vs 2-ZONE F(z): CMB GAP ANALYSIS")
    print("=" * 80)
    print()
    print("§4.48 current model:")
    print("  F_p = 0.7 (constant primordial)")
    print("  F_s = 0.3 × SFR(z)/SFR(0) (Madau-SFR stellar, → 0 at high z)")
    print()
    print("Cascade predicts: Omega_DM(z=1100) = 0.7 × Omega_DM(0)")
    print("Observed (Planck): Omega_DM(z=1100) ≈ Omega_DM(0) = 0.265")
    print("=> Gap: 30% under-prediction at z=1100")
    print()
    
    print("-" * 80)
    print("MODEL COMPARISON")
    print("-" * 80)
    print()
    print(f"{'Model':<35} {'z=0':<10} {'z=1100':<12} {'Gap@1100':<12} {'Cost'}")
    print("-" * 80)
    
    models = [
        ("§4.48 constant F_p=0.7", F_p_const, {}),
        ("§4.48 step F_p(z>4)=1.0", F_p_step, {}),
        ("Sigmoid z_scale=4", F_p_sigmoid, {"z_scale": 4.0}),
        ("Sigmoid z_scale=2", F_p_sigmoid, {"z_scale": 2.0}),
        ("Sigmoid z_scale=1", F_p_sigmoid, {"z_scale": 1.0}),
        ("Sigmoid z_scale=0.5", F_p_sigmoid, {"z_scale": 0.5}),
        ("Exponential z_scale=2", F_p_exponential, {"z_scale": 2.0}),
        ("Exponential z_scale=4", F_p_exponential, {"z_scale": 4.0}),
        ("Exponential z_scale=10", F_p_exponential, {"z_scale": 10.0}),
        ("Hill n=2 z_half=3", F_p_hill, {"n": 2.0, "z_half": 3.0}),
        ("Hill n=4 z_half=6", F_p_hill, {"n": 4.0, "z_half": 6.0}),
        ("tanh z_scale=2", F_p_tanh, {"z_scale": 2.0}),
        ("tanh z_scale=4", F_p_tanh, {"z_scale": 4.0}),
    ]
    
    for name, func, kwargs in models:
        o0 = Omega_DM_cascade(0, func, kwargs)
        o1100 = Omega_DM_cascade(1100, func, kwargs)
        # Gap = how far F_total(1100) is from 1.0 (calibration target)
        gap = (o1100 - 1.0) / 1.0 * 100
        c = cost(func, kwargs)
        print(f"{name:<35} {o0:<10.4f} {o1100:<12.4f} {gap:>+8.1f}%     {c:.4f}")
    
    print()
    print("-" * 80)
    print("FULL F(z) CURVES (best models)")
    print("-" * 80)
    print()
    print(f"{'z':<8} {'F_s(z)':<10} {'F_p_const':<12} {'F_p_sigmoid':<14} {'F_p_exp':<12} {'F_p_hill':<12} {'Obs':<10}")
    print("-" * 80)
    
    for z in Z_TEST:
        F_s = 0.3 * F_s_cumulative(z)
        Fp_const = F_p_const(z)
        Fp_sig = F_p_sigmoid(z, z_scale=4.0)
        Fp_exp = F_p_exponential(z, z_scale=2.0)
        Fp_hill = F_p_hill(z, n=2.0, z_half=3.0)
        # Observed F_total(z) — should be 1.0 at all z (Planck + calibration)
        obs = 1.0
        print(f"{z:<8} {F_s:<10.4f} {0.7+F_s:<12.4f} {Fp_sig+F_s:<14.4f} {Fp_exp+F_s:<12.4f} {Fp_hill+F_s:<12.4f} {obs:<10.4f}")
    
    print()
    print("=" * 80)
    print("CONCLUSIONS")
    print("=" * 80)
    print()
    print("1. CONSTANT F_p = 0.7 (§4.48 current) under-predicts Omega_DM(1100) by ~30%")
    print("2. STEP FUNCTION (F_p jumps to 1.0 at z=4) gives a clean match at both anchors")
    print("3. SMOOTH CURVES (sigmoid, exp, hill) can match both anchors if z_scale is right")
    print("4. The 'gap' at z=1100 is bridged by ANY function that grows F_p from 0.7 to ~1.0")
    print()
    print("PHYSICAL INTERPRETATION:")
    print("  - F_p = 0.7 means 70% of DM came from the 4D event's steady activity")
    print("  - F_p → 1.0 at high z means early DM was PRIMARILY primordial (no stellar)")
    print("  - This is consistent with: 4D event's activity was higher in the past,")
    print("    OR early 2D universes were more massive / longer-lived (different E)")
    print()
    print("Smooth F(z) is more honest than step because:")
    print("  - The 4D event's R_p(z) is unlikely to be a step function")
    print("  - Stellar activity drops smoothly with z (Madau-SFR)")
    print("  - The transition between F_p-dominated and F_s-dominated is gradual")
    print()
    print("RECOMMENDATION: replace F_p = const with F_p(z) = 0.7 + 0.3 × (1 - exp(-z/z_scale))")
    print("  with z_scale ~ 2-4 (transition over z = 0 to z = 8).")
    print()
    print("This is a 1-parameter family (z_scale) that fits both anchors and provides")
    print("a smooth, physically motivated transition.")

if __name__ == "__main__":
    main()
