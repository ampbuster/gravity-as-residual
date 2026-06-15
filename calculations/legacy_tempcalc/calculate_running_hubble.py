"""
Reference Implementation Test (SIDC §4.5 spec)
Test the proposed code from the spec to see what it actually computes.
"""

import numpy as np

def calculate_running_hubble(z: float, h_local: float = 73.0, alpha: float = 0.012) -> float:
    """
    Evaluates the effective inferred Hubble constant under an asymmetric
    SIDC model where global 4D bulk acceleration dominates matter drag.

    Parameters:
    -----------
    z : float
        The target redshift representing look-back time.
    h_local : float
        The unhindered local expansion velocity baseline (km/s/Mpc).
    alpha : float
        The evolutionary index tracking the power-law decay of the ledger.
        Empirically optimized to fit modern DESI/Planck running constraints.

    Returns:
    --------
    float
        The effective inferred Hubble parameter H_0(z).
    """
    if z < 0:
        raise ValueError("Redshift z cannot be negative in a forward cosmic ledger calculation.")

    # Natively maps the scale-time invariant power-law decay
    h_eff = h_local * ((1.0 + z) ** (-alpha))
    return float(h_eff)

# Test the spec's reference implementation
print("=" * 80)
print("REFERENCE IMPLEMENTATION TEST (SIDC §4.5 spec)")
print("=" * 80)
print()
print("Function: H_0(z) = h_local · (1+z)^(-alpha)")
print("Defaults: h_local=73.0, alpha=0.012")
print()

# Test at the three key redshifts
test_cases = [
    (0, "z=0 (SH0ES hyper-local)"),
    (0.02, "z~0.02 (TRGB mid-z)"),
    (0.1, "z=0.1 (H0LiCOW)"),
    (1.0, "z=1 (Pantheon+ high-z)"),
    (1100, "z=1100 (Planck CMB)"),
]

print(f"{'Redshift':<10s} {'H_0(z)':<12s} {'Observation':<25s} {'Match'}")
print("-" * 70)
for z, label in test_cases:
    h_eff = calculate_running_hubble(z)
    if z == 0:
        obs = "73.04 (SH0ES)"
        match = "EXACT" if abs(h_eff - 73.04) < 0.01 else f"off by {h_eff - 73.04:.2f}"
    elif z == 0.02:
        obs = "69.6 (TRGB)"
        match = "EXACT" if abs(h_eff - 69.6) < 0.01 else f"off by {h_eff - 69.6:.2f}"
    elif z == 0.1:
        obs = "73.3 (H0LiCOW)"
        match = "EXACT" if abs(h_eff - 73.3) < 0.01 else f"off by {h_eff - 73.3:.2f}"
    elif z == 1.0:
        obs = "~73 (Pantheon+)"
        match = f"off by {h_eff - 73:.2f}"
    elif z == 1100:
        obs = "67.4 (Planck)"
        match = "EXACT" if abs(h_eff - 67.4) < 0.01 else f"off by {h_eff - 67.4:.2f}"
    print(f"{z:<10g} {h_eff:<12.3f} {obs:<25s} {match}")
print()

# Step 2: scan alpha to find best fits
print("=" * 80)
print("Step 2: Scan alpha to find best fit for each observation")
print("=" * 80)
print()
print("α scan at z=1100 (target = 67.4):")
for alpha in [0.005, 0.010, 0.011, 0.0114, 0.012, 0.013, 0.015]:
    h = calculate_running_hubble(1100, alpha=alpha)
    print(f"  α = {alpha:.4f}: H_0(1100) = {h:.3f}")
print()

print("α scan at z=0.02 (target = 69.6):")
for alpha in [0.1, 0.2, 0.3, 0.2968, 0.4, 0.5]:
    h = calculate_running_hubble(0.02, alpha=alpha)
    print(f"  α = {alpha:.4f}: H_0(0.02) = {h:.3f}")
print()

# Step 3: visualize the power-law vs data
print("=" * 80)
print("Step 3: Power-law vs data")
print("=" * 80)
print()
print("Using α = 0.0114 (best Planck fit):")
print()
print(f"{'z':<10s} {'H_0(z)':<12s} {'Observation':<25s} {'Residual'}")
print("-" * 70)
data_points = [
    (0, 73.04, "SH0ES"),
    (0.001, 73.04, "Megamasers"),
    (0.02, 69.6, "TRGB"),
    (0.05, 70.0, "Sirens (lo)"),
    (0.5, 73.0, "Sirens (hi)"),
    (1.0, 73.0, "Pantheon+"),
    (1100, 67.4, "Planck"),
]
for z, obs_h0, obs_label in data_points:
    h_pred = calculate_running_hubble(z, alpha=0.0114)
    residual = h_pred - obs_h0
    marker = "✓" if abs(residual) < 0.5 else "✗" if abs(residual) > 2.0 else "~"
    print(f"{z:<10g} {h_pred:<12.3f} {obs_h0} ({obs_label})  {marker} {residual:+.2f}")
print()

# Step 4: a better fit - 2-parameter formula
print("=" * 80)
print("Step 4: 2-parameter fit H_0(z) = H_local · (1+z)^(-α) - γ·log(1+z)")
print("=" * 80)
print()
print("Try to fit SH0ES, TRGB, Planck simultaneously")
print()

from scipy.optimize import minimize

def loss(p, z_data, h_data):
    alpha, gamma = p
    pred = np.array([73.0 * (1+z)**(-alpha) - gamma * np.log(1+z) for z in z_data])
    return np.sum((pred - h_data)**2)

z_data = np.array([0, 0.02, 1100])
h_data = np.array([73.04, 69.6, 67.4])

best = None
for x0 in [(0.01, 1), (0.05, 5), (0.1, 0.5), (0.5, 1)]:
    res = minimize(loss, x0, args=(z_data, h_data), method='Nelder-Mead')
    if best is None or res.fun < best.fun:
        best = res

alpha, gamma = best.x
print(f"Best fit: α = {alpha:.6f}, γ = {gamma:.6f}, loss = {best.fun:.2f}")
print()
print("Predictions:")
for z, h_obs in zip(z_data, h_data):
    h_pred = 73.0 * (1+z)**(-alpha) - gamma * np.log(1+z)
    residual = h_pred - h_obs
    print(f"  z = {z}: H_pred = {h_pred:.3f}, H_obs = {h_obs}, residual = {residual:+.2f}")
print()

# Step 5: the cascade's 3-zone picture
print("=" * 80)
print("Step 5: Cascade's 3-zone picture (DE-dominates §2.6.2)")
print("=" * 80)
print()
print("Zone 1 (z in [0, 0.005]): H_0 = 73.04 (SH0ES, hyper-local R_stellar)")
print("Zone 2 (z in [0.005, 0.5]): H_0 = 70.16 (TRGB/sirens, 4D bulk)")
print("Zone 3 (z in [0.5, 1100]): H_0 = 67.4 + transition to Planck)")
print()
print("This 3-zone picture is the cascade's framework.")
print("It matches the data, but is a STEP FUNCTION, not a smooth power law.")
print()

# Step 6: a smooth version with a transition
print("=" * 80)
print("Step 6: Smooth 2-zone picture with a smooth transition")
print("=" * 80)
print()
print("H_0(z) = H_local if z < z_local")
print("H_0(z) = H_bulk if z_local <= z < z_CMB")
print("H_0(z) = H_CMB if z >= z_CMB")
print()
print("Or smoother: H_0(z) = H_bulk + 0.5*(H_local - H_bulk) * (1 - tanh((z-z_local)/w))")
print("                            - 0.5*(H_bulk - H_CMB) * (1 - tanh((z-z_CMB)/w))")
print()
print("where w is the transition width and z_local, z_CMB are the boundaries")
print()

# Test
def smooth_hubble(z, H_local=73.04, H_bulk=70.16, H_CMB=67.4, 
                  z_local=0.01, z_CMB=500, w=0.1):
    boost = 0.5 * (H_local - H_bulk) * (1 - np.tanh((z - z_local) / w))
    drag = 0.5 * (H_bulk - H_CMB) * (1 - np.tanh((z - z_CMB) / w))
    return H_bulk + boost - drag

print("Smooth 2-zone picture test:")
for z, obs_h0, obs_label in data_points:
    h_pred = smooth_hubble(z)
    residual = h_pred - obs_h0
    marker = "✓" if abs(residual) < 0.5 else "✗" if abs(residual) > 2.0 else "~"
    print(f"  z = {z}: H_pred = {h_pred:.3f}, H_obs = {obs_h0} ({obs_label})  {marker} {residual:+.2f}")
print()

# Step 7: summary
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print()
print("The SIDC spec's formula H_0(z) = H_local · (1+z)^(-α) is a smooth")
print("power-law. It fits SH0ES+Planck with α = 0.0114 but misses TRGB")
print("by 3.4 km/s/Mpc. It fits SH0ES+TRGB with α = 0.30 but misses Planck")
print("by 60 km/s/Mpc.")
print()
print("The cascade's 3-zone picture (§2.6.2) is a 3-parameter step function")
print("that matches the data but is not a smooth power law.")
print()
print("A smooth fit requires at LEAST 2 parameters (α and a transition")
print("function), and even then, the data has a SHARP transition between")
print("z=0 (SH0ES, 73) and z=0.02 (TRGB, 69.6) that any smooth function")
print("will struggle to capture.")
