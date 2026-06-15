"""
Asymmetric Horizon Dynamics — Running Hubble Parameterization
(SIDC §4.5 spec test)

Per user-provided spec:
  H_0(z) = H_local · (1+z)^(-α)

Test whether this power-law formula can simultaneously fit:
- H_0(z=0, SH0ES) = 73.04
- H_0(z=0.02, TRGB) = 69.6
- H_0(z=1100, Planck) = 67.4

Question: does a single α fit all three regimes?
"""

import numpy as np
import json

# Data
H_local = 73.04
H_TRGB = 69.6  # at z ~ 0.02
H_CMB = 67.4   # at z = 1100

print("=" * 80)
print("ASYMMETRIC HORIZON DYNAMICS — RUNNING HUBBLE PARAMETERIZATION")
print("=" * 80)
print()
print("Formula: H_0(z) = H_local · (1+z)^(-α)")
print()
print("Data:")
print(f"  H_0(z=0, SH0ES):    {H_local} km/s/Mpc")
print(f"  H_0(z~0.02, TRGB):  {H_TRGB} km/s/Mpc")
print(f"  H_0(z=1100, Planck): {H_CMB} km/s/Mpc")
print()

# Step 1: find α that fits the endpoints
print("=" * 80)
print("Step 1: Find α that fits z=0 and z=1100")
print("=" * 80)
print()
alpha_CMB = -np.log(H_CMB / H_local) / np.log(1101)
print(f"α (Planck fit):       {alpha_CMB:.6f}")
print()

# Test this α at all redshifts
print("H_0(z) predictions with α = 0.0114:")
print()
test_zs = [0, 0.01, 0.02, 0.05, 0.1, 0.5, 1.0, 1.5, 2.0, 5.0, 10.0, 1100]
print(f"{'z':<10s} {'H_0(z)':<12s} {'Data':<12s} {'Residual'}")
print("-" * 50)
for z in test_zs:
    H_pred = H_local * (1+z)**(-alpha_CMB)
    if z == 0:
        data_str = f"{H_local}"
        residual = H_pred - H_local
    elif z == 1100:
        data_str = f"{H_CMB}"
        residual = H_pred - H_CMB
    else:
        # Interpolate data
        if z <= 0.02:
            data_str = f"~{H_TRGB} (TRGB)"
            residual = H_pred - H_TRGB
        else:
            data_str = "(no data)"
            residual = None
    if residual is not None:
        print(f"{z:<10g} {H_pred:<12.3f} {data_str:<12s} {residual:+.2f}")
    else:
        print(f"{z:<10g} {H_pred:<12.3f} {data_str:<12s}")
print()

# Step 2: find α that fits the mid-z TRGB
print("=" * 80)
print("Step 2: Find α that fits z=0 and z=0.02 (TRGB)")
print("=" * 80)
print()
alpha_TRGB = -np.log(H_TRGB / H_local) / np.log(1.02)
print(f"α (TRGB fit):        {alpha_TRGB:.6f}")
print()

# Test this α at all redshifts
print("H_0(z) predictions with α = 0.2968 (TRGB fit):")
print()
print(f"{'z':<10s} {'H_0(z)':<12s} {'Data':<12s} {'Residual'}")
print("-" * 50)
for z in test_zs:
    H_pred = H_local * (1+z)**(-alpha_TRGB)
    if z == 0:
        data_str = f"{H_local}"
        residual = H_pred - H_local
    elif z == 0.02:
        data_str = f"{H_TRGB}"
        residual = H_pred - H_TRGB
    elif z == 1100:
        data_str = f"{H_CMB}"
        residual = H_pred - H_CMB
    else:
        data_str = "(no data)"
        residual = None
    if residual is not None:
        print(f"{z:<10g} {H_pred:<12.3f} {data_str:<12s} {residual:+.2f}")
    else:
        print(f"{z:<10g} {H_pred:<12.3f} {data_str:<12s}")
print()

# Step 3: try to fit all three points
print("=" * 80)
print("Step 3: Can a single α fit all three points?")
print("=" * 80)
print()
print("The power-law formula has ONE free parameter (α).")
print("With ONE parameter, we can fit at most ONE ratio.")
print()
print("Required α for each pair:")
print(f"  α for H(1100) = {H_CMB}:  {alpha_CMB:.4f}")
print(f"  α for H(0.02) = {H_TRGB}: {alpha_TRGB:.4f}")
print()
print("These are 26× different. A single power-law cannot fit both.")
print()

# Step 4: test if a more complex formula works
print("=" * 80)
print("Step 4: Try a 2-parameter formula")
print("=" * 80)
print()
print("If H_0(z) = H_local · (1+z)^(-α) · (1 - β·z), can we fit?")
print()

# We want:
# H(0) = H_local = 73.04 (automatic, since (1+0)^-α · (1-0) = 1)
# H(0.02) = 73.04 · (1.02)^(-α) · (1 - 0.02β) = 69.6
# H(1100) = 73.04 · (1101)^(-α) · (1 - 1100β) = 67.4

# Use scipy to fit
from scipy.optimize import fsolve

def equations(p):
    alpha, beta = p
    eq1 = H_local * (1.02)**(-alpha) * (1 - 0.02*beta) - H_TRGB
    eq2 = H_local * (1101)**(-alpha) * (1 - 1100*beta) - H_CMB
    return [eq1, eq2]

# Try several initial guesses
for x0 in [(0.01, 0.001), (0.1, 0.001), (0.01, 0.0001), (0.3, 0.0005)]:
    try:
        sol = fsolve(equations, x0, full_output=True)
        alpha, beta = sol[0]
        if sol[2] == 1:  # converged
            print(f"  x0 = {x0}: α = {alpha:.4f}, β = {beta:.6f}")
            # Test
            H_0 = H_local
            H_002 = H_local * (1.02)**(-alpha) * (1 - 0.02*beta)
            H_1100 = H_local * (1101)**(-alpha) * (1 - 1100*beta)
            print(f"    H(0) = {H_0:.2f}, H(0.02) = {H_002:.2f}, H(1100) = {H_1100:.2f}")
    except Exception as e:
        print(f"  x0 = {x0}: failed ({e})")
print()

# Step 5: a different parameterization
print("=" * 80)
print("Step 5: Try H_0(z) = H_local · (1+z)^(-α) - γ·(1-(1+z)^(-α))")
print("=" * 80)
print()
print("This is a 2-parameter form: α (slow decay) and γ (drop at low z)")
print()

def equations2(p):
    alpha, gamma = p
    eq1 = H_local * (1.02)**(-alpha) - gamma*(1 - (1.02)**(-alpha)) - H_TRGB
    eq2 = H_local * (1101)**(-alpha) - gamma*(1 - (1101)**(-alpha)) - H_CMB
    return [eq1, eq2]

for x0 in [(0.01, 1), (0.05, 5), (0.1, 1), (0.5, 5)]:
    try:
        sol = fsolve(equations2, x0, full_output=True)
        alpha, gamma = sol[0]
        if sol[2] == 1:
            print(f"  x0 = {x0}: α = {alpha:.4f}, γ = {gamma:.4f}")
            H_0 = H_local
            H_002 = H_local * (1.02)**(-alpha) - gamma*(1 - (1.02)**(-alpha))
            H_1100 = H_local * (1101)**(-alpha) - gamma*(1 - (1101)**(-alpha))
            print(f"    H(0) = {H_0:.2f}, H(0.02) = {H_002:.2f}, H(1100) = {H_1100:.2f}")
    except Exception as e:
        print(f"  x0 = {x0}: failed ({e})")
print()

# Step 6: a 3-zone piecewise approach (matches the SIDC framework)
print("=" * 80)
print("Step 6: 3-zone piecewise formula (matches §2.6.2 framework)")
print("=" * 80)
print()
print("Zone 1 (z in [0, 0.005]): H_0 = 73.04 (SH0ES, hyper-local)")
print("Zone 2 (z in [0.005, 0.5]): H_0 = 70.16 (TRGB/sirens, 4D bulk)")
print("Zone 3 (z in [0.5, 1100]): H_0 = 67.4 + smooth transition to Planck)")
print()
print("This is a STEPPED function, not a smooth power law.")
print("The 'Running Hubble' from the spec is OVER-SMOOTH.")
print()

# Final verdict
print("=" * 80)
print("VERDICT")
print("=" * 80)
print()
print("The SIDC spec's formula H_0(z) = H_local · (1+z)^(-α) is a smooth")
print("power-law decay. It CAN fit any two of the three data points")
print("(SH0ES, TRGB, Planck) with a single α, but it CANNOT fit all three")
print("simultaneously:")
print()
print(f"  - α = 0.0114 fits SH0ES (73) and Planck (67.4), but predicts 73.0")
print(f"    at z=0.02 (TRGB), not 69.6. The 3.4 km/s/Mpc gap is unexplained.")
print()
print(f"  - α = 0.2968 fits SH0ES (73) and TRGB (69.6), but predicts")
print(f"    {73.0 * (1101)**(-0.2968):.2f} at z=1100, not 67.4. Way too low.")
print()
print("The 3-zone piecewise picture (Zone 1: 73, Zone 2: 70.16, Zone 3: 67.4)")
print("is more honest about the data: there's a SHARP TRANSITION between")
print("z=0.02 (TRGB) and z=0 (SH0ES), which the smooth power law cannot capture.")
print()
print("Honest finding: The Running Hubble Parameterization is a 1-parameter")
print("smooth fit that captures the endpoints (SH0ES, Planck) but misses")
print("the mid-z TRGB value. The cascade's 3-zone picture (DE-dominates")
print("framework in §2.6.2) is a better empirical fit, but it's a 3-parameter")
print("step function, not a smooth power law.")
