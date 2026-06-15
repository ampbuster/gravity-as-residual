"""
Cross-dimensional calc #4: HI 21cm Power Spectrum at z = 6-20
=============================================================

The 21cm signal probes:
- High-z HI distribution (z = 6-20)
- Reionization era (z = 6-15)
- Cosmic dawn (z = 15-25)
- Lyα coupling and X-ray heating

Cascade prediction:
- 2D universes are CDM-like (no direct 21cm effect)
- Indirect effect: 2D universe deaths at high z add to matter density
- But the 21cm signal is dominated by HI physics (gas, stars, X-rays)
- Cascade adds a small contribution to total matter density

Tests:
- 21cm power spectrum amplitude
- Reionization timing
- Cosmic dawn timing
"""

import numpy as np

# Constants
H_0 = 70.16e3 / 3.086e22
Omega_m = 0.315
Omega_b = 0.045
Omega_DM = 0.27
H_0_Hz = H_0 / (3.086e22)  # dimensionless

print("=" * 80)
print("HI 21cm POWER SPECTRUM — CASCADE PREDICTION")
print("=" * 80)
print()

# =============================================================================
# 21cm signal basics
# =============================================================================
# Frequency: 1420 MHz (rest frame) at z = 6-20
# ν_obs = 1420 / (1+z) MHz

z_test = [6, 8, 10, 12, 15, 18, 20]
print(f"{'z':>5} | {'ν_obs (MHz)':>12} | {'T_21 expected (mK)':>20}")
print("-" * 50)
for z in z_test:
    nu = 1420 / (1 + z)
    # T_21 in mK (rough estimate)
    # -100 mK at z ~ 8 (absorption against CMB)
    # +30 mK at z ~ 6-10 (after reionization, emission)
    if z < 7:
        T_21 = 30  # emission
    elif z < 12:
        T_21 = -100  # absorption
    else:
        T_21 = -50  # cosmic dawn absorption
    print(f"{z:5.1f} | {nu:12.1f} | {T_21:20.1f}")

print()

# =============================================================================
# Cascade's contribution to 21cm signal
# =============================================================================
print("=" * 80)
print("CASCADE'S CONTRIBUTION TO 21cm SIGNAL")
print("=" * 80)
print()
print("Cascade's 2D universes are CDM-like (no direct 21cm effect).")
print("But they contribute to total matter density:")
print()
print("  2D universe density at z: ρ_2D(z) = ρ_DM × (1+z)^3 / (1+z_now)^3")
print()
print("This is the same as ΛCDM's CDM density at z.")
print("So the 21cm signal from 2D universes is INDISTINGUISHABLE from CDM.")
print()

# =============================================================================
# 21cm power spectrum
# =============================================================================
print("=" * 80)
print("21cm POWER SPECTRUM P_21(k)")
print("=" * 80)
print()
print("The 21cm power spectrum amplitude is set by:")
print("  - HI density (∝ Ω_b)")
print("  - Brightness temperature T_21")
print("  - Bias from galaxies (Lyα sources, X-ray sources)")
print()
print("Cascade prediction:")
print("  - Ω_b is the same as ΛCDM (input)")
print("  - T_21 is the same as ΛCDM (gas physics)")
print("  - Galaxy bias is the same as ΛCDM (star formation)")
print("  - 2D universes add to matter, not to HI or T_21")
print()
print("VERDICT: 21cm power spectrum is INDISTINGUISHABLE from ΛCDM")
print()

# =============================================================================
# Reionization history
# =============================================================================
print("=" * 80)
print("REIONIZATION HISTORY")
print("=" * 80)
print()
print("Reionization at z = 6-15 is from first stars and quasars.")
print("Cascade's 2D universe deaths at z = 6-15:")
print("  - Are CDM-like (no EM interaction)")
print("  - Don't ionize the IGM")
print("  - Don't change reionization history")
print()
print("Cascade reionization is the SAME as ΛCDM (Planck τ_reion = 0.054)")
print()

# =============================================================================
# Honest verdict
# =============================================================================
print("=" * 80)
print("HONEST VERDICT: 21cm POWER SPECTRUM")
print("=" * 80)
print()
print("The 21cm signal is INDISTINGUISHABLE from ΛCDM at all z.")
print()
print("Cascade's 2D universes don't affect 21cm because:")
print("  - They're CDM-like (no EM interaction)")
print("  - They don't ionize the IGM")
print("  - They don't couple to HI directly")
print()
print("Reionization history is the same as ΛCDM.")
print()
print("VERDICT: 21cm is a CONSISTENCY CHECK, not a unique cascade prediction.")
print()
