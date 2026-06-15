"""
Cross-dimensional calc #3: CMB Lensing Reconstruction
======================================================

CMB lensing probes:
- 3+1D structure growth (large-scale potential)
- DM clustering (intermediate scales)
- 2D universe distribution (small scales)

Cascade prediction:
- Same as ΛCDM at large scales (2D universes are CDM-like)
- Slightly different at small scales (MOND-like at low accel)
- σ_8 and S_8 constraints

The cascade is consistent with current S_8 measurements from
cosmic shear (DES, KiDS).
"""

import numpy as np

# Constants
H_0 = 70.16e3 / 3.086e22
Omega_m = 0.315
Omega_DM = 0.27
Omega_b = 0.045
Omega_L = 0.685
h = 0.7016
sigma_8 = 0.75  # Planck-like

print("=" * 80)
print("CMB LENSING — CASCADE VS ΛCDM")
print("=" * 80)
print()

# =============================================================================
# S_8 = σ_8 × sqrt(Ω_m / 0.3)
# =============================================================================
S_8_cascade = sigma_8 * np.sqrt(Omega_m / 0.3)
S_8_DES = 0.759  # DES Year 3
S_8_KiDS = 0.766  # KiDS-1000

print("S_8 measurement (σ_8 × sqrt(Ω_m / 0.3)):")
print(f"  Cascade (input): {S_8_cascade:.3f}")
print(f"  DES Year 3:      {S_8_DES:.3f}")
print(f"  KiDS-1000:       {S_8_KiDS:.3f}")
print(f"  Difference: {abs(S_8_cascade - S_8_DES):.3f}")
print()

# =============================================================================
# CMB lensing potential
# =============================================================================
print("=" * 80)
print("CMB LENSING POTENTIAL φ(ℓ)")
print("=" * 80)
print()
print("C_l^φφ(ℓ) is the CMB lensing power spectrum")
print()
print("Standard ΛCDM: peaks at ℓ ~ 50-100, falls off at high ℓ")
print("Cascade prediction: SAME as ΛCDM at all ℓ")
print("  - 2D universes are CDM-like")
print("  - Their gravity is the same as CDM")
print("  - No new lensing signature")
print()
print("Exception: If cascade has a different σ_8, then C_l^φφ scales as σ_8^2")
print(f"  Cascade σ_8 = {sigma_8} (input)")
print(f"  C_l^φφ cascade / C_l^φφ ΛCDM = (σ_8_cascade / σ_8_ΛCDM)^2")
print()

# =============================================================================
# Cross-correlations
# =============================================================================
print("=" * 80)
print("CROSS-CORRELATIONS (CMB × galaxy lensing)")
print("=" * 80)
print()
print("The cross-correlation between CMB lensing and galaxy weak lensing")
print("probes the 2D universe-2D universe correlation.")
print()
print("Cascade predicts:")
print("  - 2D universes cluster with galaxies (since stars create them)")
print("  - This gives a POSITIVE cross-correlation")
print("  - But same as ΛCDM + galaxy bias")
print("  - Not unique to cascade")
print()

# =============================================================================
# Honest verdict
# =============================================================================
print("=" * 80)
print("HONEST VERDICT: CMB LENSING")
print("=" * 80)
print()
print(f"S_8 = {S_8_cascade:.3f} (cascade) matches S_8 measurements to 0.02")
print("CMB lensing potential C_l^φφ is INDISTINGUISHABLE from ΛCDM")
print("Cross-correlations with galaxy lensing are same as ΛCDM + bias")
print()
print("VERDICT: CMB lensing is a CONSISTENCY CHECK.")
print("The cascade's σ_8 = 0.75 (input) matches observations,")
print("but this is INPUT, not derived.")
print()
