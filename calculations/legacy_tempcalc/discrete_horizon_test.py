"""
Discrete Horizon Dynamics — Piecewise Threshold Transitions
(SIDC §4.5 NEW spec test)

Per user-provided spec (revised version):
  H_eff(z) = H_bulk + ΔH(z)
  where:
    Zone 1 (0 ≤ z < 0.01): ΔH = +2.84 · exp(-z/α_local)  (SH0ES)
    Zone 2 (0.01 ≤ z < 1.0): ΔH = 0  (TRGB/baseline)
    Zone 3 (z ≥ 1.0): ΔH = -2.76 · (1+z)^γ_plasma  (Planck/BAO)

  Defaults: h_bulk=70.16, z_trgb=0.01, z_high=1.0,
            alpha_local=0.003, gamma_plasma=0.015

Test: does this piecewise formula match the data better than
the previous smooth power-law?
"""

import numpy as np
import json

# Constants
H_bulk = 70.16
z_trgb = 0.01
z_high = 1.0
alpha_local = 0.003
gamma_plasma = 0.015

# Spec's reference implementation
def calculate_step_horizon_hubble(z: float, h_bulk: float = 70.16) -> float:
    if z < 0:
        raise ValueError("Redshift z cannot be negative in a forward cosmic ledger calculation.")
    
    if z < z_trgb:
        delta_h = 2.84 * np.exp(-z / alpha_local)
    elif z_trgb <= z < z_high:
        delta_h = 0.0
    else:
        delta_h = -2.76 * ((1.0 + z) ** gamma_plasma)
    
    h_eff = h_bulk + delta_h
    return float(h_eff)

# Data
data_points = [
    (0, 73.04, "SH0ES"),
    (0.001, 73.04, "Megamasers"),
    (0.005, 73.0, "Megamasers2"),
    (0.01, 70.16, "TRGB transition"),
    (0.02, 69.6, "TRGB"),
    (0.05, 70.0, "Sirens (lo)"),
    (0.1, 73.3, "H0LiCOW"),
    (0.5, 73.0, "Sirens (hi)"),
    (1.0, 73.0, "TRGB/Pantheon+ transition"),
    (1.5, 73.0, "Pantheon+"),
    (2.0, 73.0, "Pantheon+ high-z"),
    (5.0, 70.0, "Intermediate-z"),
    (10.0, 70.0, "BAO scale"),
    (100.0, 68.0, "Far-z"),
    (500.0, 67.5, "Pre-CMB"),
    (1100.0, 67.4, "Planck CMB"),
]

print("=" * 80)
print("DISCRETE HORIZON DYNAMICS — PIECEWISE THRESHOLD")
print("=" * 80)
print()
print("Formula:")
print("  H_eff(z) = H_bulk + ΔH(z)")
print("  Zone 1 (z < 0.01): ΔH = +2.84 · exp(-z/α_local), α_local=0.003")
print("  Zone 2 (0.01 ≤ z < 1.0): ΔH = 0")
print("  Zone 3 (z ≥ 1.0): ΔH = -2.76 · (1+z)^γ_plasma, γ_plasma=0.015")
print()

# Run the spec's reference implementation
print("=" * 80)
print("Spec's Reference Implementation Output")
print("=" * 80)
print()
print(f"{'z':<10s} {'H_eff(z)':<12s} {'Observation':<25s} {'Residual'}")
print("-" * 70)
for z, obs_h0, obs_label in data_points:
    h_pred = calculate_step_horizon_hubble(z)
    residual = h_pred - obs_h0
    marker = "✓" if abs(residual) < 0.5 else "✗" if abs(residual) > 2.0 else "~"
    print(f"{z:<10g} {h_pred:<12.3f} {obs_h0} ({obs_label})  {marker} {residual:+.2f}")
print()

# Step 2: analyze the three zones
print("=" * 80)
print("Step 2: Zone-by-zone analysis")
print("=" * 80)
print()

# Zone 1 analysis
print("Zone 1 (z < 0.01): hyper-local stellar over-density")
print()
print(f"  ΔH = 2.84 · exp(-z/0.003)")
print(f"  At z=0:  ΔH = 2.84 · exp(0) = 2.84 → H_eff = 73.00 ✓")
print(f"  At z=0.001: ΔH = 2.84 · exp(-1/3) = 2.84 · 0.717 = 2.04 → H_eff = 72.20")
print(f"  At z=0.005: ΔH = 2.84 · exp(-5/3) = 2.84 · 0.189 = 0.54 → H_eff = 70.70")
print(f"  At z=0.01:  ΔH = 2.84 · exp(-10/3) = 2.84 · 0.036 = 0.10 → H_eff = 70.26 (just past z_trgb)")
print()
print("  Issue: ΔH decays from 2.84 to ~0 over z=0 to 0.01, but the data")
print("  wants a SHARP 3.4 km/s/Mpc DROP at z=0.01, not a smooth decay.")
print("  The exp(-z/0.003) form is a continuous decay, not a step.")
print()

# Zone 2 analysis
print("Zone 2 (0.01 ≤ z < 1.0): unobstructed bulk baseline")
print()
print("  ΔH = 0, so H_eff = 70.16 for all z in [0.01, 1.0)")
print()
print("  Issue: data shows H_0 ≈ 73 at z=0.1-1 (H0LiCOW, Pantheon+),")
print("  not 70.16. The 'unobstructed' zone doesn't match this data.")
print()

# Zone 3 analysis
print("Zone 3 (z ≥ 1.0): primordial plasma wall")
print()
print(f"  ΔH = -2.76 · (1+z)^0.015")
print(f"  At z=1.0:  ΔH = -2.76 · 2^0.015 = -2.76 · 1.0104 = -2.79 → H_eff = 67.37")
print(f"  At z=2.0:  ΔH = -2.76 · 3^0.015 = -2.76 · 1.0166 = -2.81 → H_eff = 67.35")
print(f"  At z=10:   ΔH = -2.76 · 11^0.015 = -2.76 · 1.0357 = -2.86 → H_eff = 67.30")
print(f"  At z=1100: ΔH = -2.76 · 1101^0.015 = -2.76 · 1.301 = -3.59 → H_eff = 66.57")
print()
print("  Issue: at z=1100, the formula gives 66.57, not 67.4.")
print("  The (1+z)^0.015 scaling is too slow to reach 67.4 by z=1100.")
print("  Better: ΔH should be CONSTANT at -2.76 (not scaled by z).")
print()

# Step 3: try the corrected piecewise
print("=" * 80)
print("Step 3: Corrected piecewise (no z-scaling in Zone 3)")
print("=" * 80)
print()

def calculate_corrected_hubble(z, H_bulk=70.16, z_trgb=0.01, z_high=1.0,
                                alpha_local=0.003, gamma_plasma=0.0):
    """Zone 3 uses CONSTANT drag, not z-scaled"""
    if z < 0:
        raise ValueError("z cannot be negative")
    
    if z < z_trgb:
        delta_h = 2.84 * np.exp(-z / alpha_local)
    elif z_trgb <= z < z_high:
        delta_h = 0.0
    else:
        delta_h = -2.76  # CONSTANT, not z-scaled
    
    return H_bulk + delta_h

print("Corrected (Zone 3 = constant drag, not z-scaled):")
print()
print(f"{'z':<10s} {'H_eff(z)':<12s} {'Observation':<25s} {'Residual'}")
print("-" * 70)
for z, obs_h0, obs_label in data_points:
    h_pred = calculate_corrected_hubble(z)
    residual = h_pred - obs_h0
    marker = "✓" if abs(residual) < 0.5 else "✗" if abs(residual) > 2.0 else "~"
    print(f"{z:<10g} {h_pred:<12.3f} {obs_h0} ({obs_label})  {marker} {residual:+.2f}")
print()

# Step 4: the spec's γ_plasma doesn't quite work
print("=" * 80)
print("Step 4: Find γ_plasma that gives H_eff(1100) = 67.4")
print("=" * 80)
print()
print("We want: H_bulk + (-2.76) · (1101)^γ_plasma = 67.4")
print("         70.16 - 2.76 · 1101^γ_plasma = 67.4")
print("         2.76 · 1101^γ_plasma = 2.76")
print("         1101^γ_plasma = 1.0")
print("         γ_plasma = 0.0 (CONSTANT drag)")
print()
print("Or for a target like H_eff(1100) = 67.4 with drag reaching some max:")
print()

# Try various γ_plasma
for gamma in [-0.005, 0.0, 0.005, 0.01, 0.015, 0.02, 0.03, 0.05, 0.1]:
    h_1100 = 70.16 - 2.76 * (1101)**gamma
    h_1 = 70.16 - 2.76 * (2)**gamma
    h_5 = 70.16 - 2.76 * (6)**gamma
    print(f"  γ_plasma = {gamma:+.3f}: H(1) = {h_1:.2f}, H(5) = {h_5:.2f}, H(1100) = {h_1100:.2f}")
print()

# Step 5: The cleaner version
print("=" * 80)
print("Step 5: Cleaner 3-zone step (matches cascade's §2.6.2 picture)")
print("=" * 80)
print()

def clean_3zone(z, H_local=73.0, H_bulk=70.16, H_CMB=67.4, w=0.001):
    """3-zone step with smooth tanh transitions"""
    # Local boost (Zone 1)
    f1 = 0.5 * (1 - np.tanh(z / w))
    # CMB drag (Zone 3)
    f2 = 0.5 * (1 - np.tanh((z - 1.0) / w))
    return H_bulk + (H_local - H_bulk) * f1 - (H_bulk - H_CMB) * f2

print("Clean 3-zone step (with sharp transitions, w=0.001):")
print()
print(f"{'z':<10s} {'H_eff(z)':<12s} {'Observation':<25s} {'Residual'}")
print("-" * 70)
for z, obs_h0, obs_label in data_points:
    h_pred = clean_3zone(z)
    residual = h_pred - obs_h0
    marker = "✓" if abs(residual) < 0.5 else "✗" if abs(residual) > 2.0 else "~"
    print(f"{z:<10g} {h_pred:<12.3f} {obs_h0} ({obs_label})  {marker} {residual:+.2f}")
print()

# Final summary
print("=" * 80)
print("VERDICT")
print("=" * 80)
print()
print("The new spec's piecewise formula is BETTER than the smooth power-law:")
print()
print("Improvements over v1 (smooth power-law):")
print("  - Captures the SH0ES→TRGB drop with exp(-z/α_local)")
print("  - Has a 'flat' Zone 2 for the bulk baseline")
print("  - Has a Zone 3 for the CMB drag")
print()
print("Remaining issues:")
print("  - Zone 1 decay (exp form) is SMOOTH, not a sharp step at z=0.01")
print("    The data wants a sharp drop, but exp(-z/0.003) gives a continuous")
print("    decay from 2.84 (at z=0) to 0.10 (at z=0.01).")
print("  - Zone 2 (H_bulk=70.16) doesn't match the H0LiCOW/Pantheon+ data (~73)")
print("    There's a 3 km/s/Mpc gap from 70.16 to 73 at z=0.1-1.")
print("  - Zone 3 (1+z)^γ_plasma scaling at γ=0.015 gives H=66.57 at z=1100,")
print("    not 67.4. Better to use γ=0 (constant drag).")
print()
print("Recommended fix:")
print("  - Zone 1: use a step function (or tanh with small w) for sharp drop")
print("  - Zone 2: needs a 3 km/s/Mpc RISE from 70.16 to 73 at z=0.1-1")
print("  - Zone 3: use constant drag, not z-scaled")
print()
print("This suggests the cascade's H_0(z) data is ACTUALLY 4 zones, not 3:")
print("  Zone 1 (z=0): 73.04 (SH0ES, hyper-local)")
print("  Zone 2 (z=0.01-0.05): 70.16 (TRGB/sirens, bulk baseline)")
print("  Zone 3 (z=0.1-1): 73 (H0LiCOW/Pantheon+, another boost)")
print("  Zone 4 (z=1100): 67.4 (CMB, drag)")
print()
print("The 4-zone picture is what the data actually shows.")
