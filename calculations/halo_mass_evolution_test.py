#!/usr/bin/env python3
"""
Halo Mass vs M* Evolution with Redshift (Test 6) - Documentation

This test explores whether the cascade's M_halo/M_star prediction
at fixed M_star evolves with redshift, and how that compares to
observation. As analyzed, this is NOT a clean discriminative test
because both the cascade and ΛCDM have similar predictions.

Cascade prediction analysis:
The cascade's DM has two components:
- Active: from current high-energy activity (~5% of total)
- Cumulative: from past activity integrated over time (~95% of total)

For a galaxy at fixed M* observed at different z:
- Active contribution: depends on current SFR
  Cosmic SFR peaks at z~2 (Madau & Dickinson 2014), so at z~2,
  active is HIGHER than at z=0.
- Cumulative contribution: depends on integrated past activity
  For galaxies at z=4, less time has elapsed for integration.
  But galaxies at z=4 are typically YOUNGER (formed later in cosmic time)
  and may have different SFHs.

This makes the cascade's prediction at fixed M* COMPLEX:
- The "same M* galaxy" at different z may have different SFHs
- High-z galaxies are typically bursting → more cumulative at fixed time
- Low-z galaxies are typically quiescent → less cumulative at fixed time

Net prediction: M_halo/M_star at fixed M* is ~ CONSTANT in z (similar to ΛCDM)

Standard ΛCDM prediction: M_halo/M_star at fixed M* is ~ CONSTANT
(halo mass set at formation, with weak z evolution ~ 0.1 dex)

Published data:
- Leauthaud+ 2012 (z=0-1): M_halo/M_star ~ constant
- Behroozi+ 2013 (z=0-4): M_halo/M_star ~ constant to within 0.2 dex
  Mild "downsizing" (M_halo/M_star slightly HIGHER at high z)

Verdict: CONSISTENT with both cascade and ΛCDM

This is NOT a discriminative test:
- Both models predict ~constant M_halo/M_star at fixed M*
- The cascade's active vs cumulative contributions can adjust to match
- The 0.2 dex scatter is comparable to any second-order effect

To make this discriminative, would need:
- Better z-resolution data
- A precise cascade calculation that includes SFH as a function of z
- A prediction for the EXACT z-dependence (e.g., shape of M_halo/M_star vs z curve)

This test confirms that the cascade and ΛCDM both produce reasonable
predictions for the SHMR (stellar-to-halo mass relation) at different z.
The cascade is CONSISTENT with the data but not DISCRIMINATIVE.
"""

print("="*60)
print("Halo Mass vs M* Evolution with Redshift (Test 6)")
print("="*60)

print("\nCascade prediction analysis:")
print("  Cascade DM = active (current SFR) + cumulative (integrated past)")
print("  For galaxies at fixed M* observed at different z:")
print("    Active: depends on current SFR (peaks at z~2)")
print("    Cumulative: depends on integrated past activity")
print("    Galaxy SFHs differ at different z (bursting at high z)")
print("  Net: complex, but ~constant M_halo/M_star")
print()

print("ΛCDM prediction:")
print("  M_halo set at formation → M_halo/M_star ~ constant at fixed M*")
print()

print("Published data:")
print("  - Leauthaud+ 2012 (z=0-1): M_halo/M_star ~ constant")
print("  - Behroozi+ 2013 (z=0-4): M_halo/M_star ~ constant to within 0.2 dex")
print()

print("Verdict: CONSISTENT with both cascade and ΛCDM (NOT discriminative)")
print("  Both models predict ~constant M_halo/M_star at fixed M*")
print("  The cascade's two-component structure (active + cumulative)")
print("  can naturally accommodate the constancy")
print()

print("Why NOT a discriminative test:")
print("  - Both models predict the same outcome")
print("  - The cascade has more flexibility (active and cumulative adjust)")
print("  - The 0.2 dex scatter is comparable to any second-order effect")
print()

print("To make this discriminative, would need:")
print("  - Better z-resolution data (sub-redshift bins)")
print("  - A precise cascade calculation including SFH as a function of z")
print("  - A prediction for the EXACT z-dependence")
print("  - The discriminative test would be a specific z-dependence predicted")
print("    by the cascade (e.g., M_halo/M_star slightly HIGHER at z~2 where")
print("    cosmic SFR peaks)")

# Save
output_path = "/workspace/github-repo/calculations/halo_mass_evolution_test_results.txt"
with open(output_path, 'w') as f:
    f.write("Halo Mass vs M* Evolution Test Results (Documentation)\n")
    f.write("========================================================\n\n")
    f.write("Cascade prediction analysis:\n")
    f.write("  Cascade DM = active (current SFR) + cumulative (integrated past)\n")
    f.write("  Net: complex, but ~constant M_halo/M_star\n\n")
    f.write("ΛCDM prediction: M_halo/M_star ~ constant at fixed M*\n\n")
    f.write("Published data:\n")
    f.write("  Leauthaud+ 2012 (z=0-1): M_halo/M_star ~ constant\n")
    f.write("  Behroozi+ 2013 (z=0-4): M_halo/M_star ~ constant to within 0.2 dex\n\n")
    f.write("Verdict: CONSISTENT with both (NOT discriminative)\n")
    f.write("  Both models predict ~constant M_halo/M_star at fixed M*\n")
    f.write("  Cascade's two-component structure can accommodate this\n\n")
    f.write("To make discriminative:\n")
    f.write("  - Better z-resolution data\n")
    f.write("  - More sophisticated cascade calculation including SFH\n")
    f.write("  - Precise prediction for z-dependence\n")

print(f"Results saved to {output_path}")
