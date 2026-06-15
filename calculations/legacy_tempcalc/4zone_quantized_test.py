"""
4-Zone Quantized Step Engine Test (cleaned up)
"""

import numpy as np

def calculate_4zone_quantized_hubble(z: float, h_bulk: float = 70.16) -> float:
    if z < 0:
        raise ValueError("Redshift z cannot be negative")
    z_trgb = 0.01
    z_rise = 0.05
    z_fall = 1.0
    w_local = 0.001
    
    delta_h_local = 1.44 * (1.0 - np.tanh((z - z_trgb) / w_local))
    
    if z_rise <= z < z_fall:
        delta_h_secular = 2.84
    else:
        delta_h_secular = 0.0
    
    if z >= z_fall:
        delta_h_primordial = -2.76
    else:
        delta_h_primordial = 0.0
    
    h_eff = h_bulk + delta_h_local + delta_h_secular + delta_h_primordial
    return float(h_eff)

data_points = [
    (0, 73.04, "SH0ES"),
    (0.001, 73.04, "Megamasers"),
    (0.005, 73.0, "Megamasers2"),
    (0.01, 70.16, "TRGB transition"),
    (0.02, 69.6, "TRGB"),
    (0.05, 70.0, "TRGB/Sirens boundary"),
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
print("4-ZONE QUANTIZED STEP ENGINE TEST (NEW spec)")
print("=" * 80)
print()
print("Reference implementation:")
print("  Zone 1: H_bulk + 1.44 * (1 - tanh((z - 0.01)/0.001))  [local boost, sharp drop]")
print("  Zone 2: H_bulk                                            [bulk baseline]")
print("  Zone 3: H_bulk + 2.84                                    [secular boost, z in (0.05, 1.0)]")
print("  Zone 4: H_bulk - 2.76                                    [primordial drag, z >= 1.0]")
print()

# Run the spec's reference implementation
print("=" * 80)
print("Spec Reference Implementation Output")
print("=" * 80)
print()
print(f"{'z':<10s} {'H_eff(z)':<12s} {'Observation':<25s} {'Residual'}")
print("-" * 70)
for z, obs_h0, obs_label in data_points:
    h_pred = calculate_4zone_quantized_hubble(z)
    residual = h_pred - obs_h0
    marker = "✓" if abs(residual) < 0.5 else "✗" if abs(residual) > 2.0 else "~"
    print(f"{z:<10g} {h_pred:<12.3f} {obs_h0} ({obs_label})  {marker} {residual:+.2f}")
print()

print("=" * 80)
print("VERIFICATION: Zone 4 is correct!")
print("=" * 80)
print()
print("At z=1100, the spec gives:")
print("  delta_h_local = 0 (way past 0.01)")
print("  delta_h_secular = 0 (since 1100 >= 1.0, NOT in (0.05, 1.0))")
print("  delta_h_primordial = -2.76 (since 1100 >= 1.0)")
print("  H_eff = 70.16 + 0 + 0 + -2.76 = 67.40 ✓")
print()
print("I was WRONG above to think Zone 4 stacks the secular boost. The")
print("conditions are:")
print("  if z_rise <= z < z_fall: secular = 2.84")
print("  if z >= z_fall: primordial = -2.76")
print("These are MUTUALLY EXCLUSIVE. At z=1.0, secular is OFF, primordial is ON.")
