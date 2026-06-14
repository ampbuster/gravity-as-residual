#!/usr/bin/env python3
"""
Direct Detection Experiment Null Test (Test 3)

Cascade prediction: ZERO direct detection signal. DM is geometric gravity
(modification of 3+1D gravity from 2D universe back-projection), not a
particle. No coupling to Standard Model particles means no WIMP-nucleon
cross section, no scattering, no detection.

Standard WIMP prediction: A non-zero signal in the range σ_SI ~ 10^-44
to 10^-48 cm^2 depending on WIMP mass, expected from the thermal
relic abundance (the "WIMP miracle").

Test: Compare cascade prediction (zero signal) against published
experimental limits from LZ, XENONnT, PandaX-4T, etc. (as of 2024-2025).

Verdict: Multiple decades of WIMP searches with no detection. The cascade's
prediction of "no signal" is consistent with the cumulative null result.
"""

import numpy as np
import math

print("="*60)
print("Direct Detection Null Test")
print("Cascade prediction: ZERO signal at all cross sections")
print("="*60)

# Published limits (as of 2024-2025, all 90% CL, spin-independent WIMP-nucleon)
# Sources: LZ 2024, XENONnT 2023/2024, PandaX-4T 2024
limits = {
    'LZ (2024, 280 days)': {
        'min_sigma_SI': 9.2e-48,  # cm^2 at 36 GeV WIMP mass
        'mass_at_min': 36,  # GeV
        'exposure': 5.5,  # tonne-year
        'ref': 'J. Aalbers+ (LZ), PRL 131 (2023) 041002; updated 2024',
    },
    'XENONnT (2023, Science)': {
        'min_sigma_SI': 2.1e-47,  # cm^2
        'mass_at_min': 30,  # GeV
        'exposure': 1.16,  # tonne-year
        'ref': 'E. Aprile+ (XENONnT), PRL 131 (2023) 041004',
    },
    'PandaX-4T (2024)': {
        'min_sigma_SI': 3.3e-47,  # cm^2
        'mass_at_min': 40,  # GeV
        'exposure': 1.0,  # tonne-year
        'ref': 'Y. Meng+ (PandaX-4T), PRL 131 (2024) 191001',
    },
    'XENON1T (legacy, 2018)': {
        'min_sigma_SI': 1.0e-46,  # cm^2
        'mass_at_min': 30,  # GeV
        'exposure': 0.279,  # tonne-year
        'ref': 'E. Aprile+ (XENON1T), PRL 121 (2018) 111302',
    },
    'LUX (legacy, 2017)': {
        'min_sigma_SI': 1.1e-46,  # cm^2
        'mass_at_min': 50,  # GeV
        'exposure': 0.335,  # tonne-year
        'ref': 'D. Akerib+ (LUX), PRL 118 (2017) 021303',
    },
    'DEAP-3600 (Ar, 2022)': {
        'min_sigma_SI': 3.9e-45,  # cm^2 (less sensitive but different target)
        'mass_at_min': 100,  # GeV
        'exposure': 0.231,  # tonne-year
        'ref': 'R. Ajaj+ (DEAP), PRD 100 (2019) 022004',
    },
}

print("\n1. Published WIMP direct-detection limits (90% CL, spin-independent):\n")
for exp, data in limits.items():
    print(f"   {exp}:")
    print(f"      Best limit: σ_SI < {data['min_sigma_SI']:.2e} cm² at M_WIMP = {data['mass_at_min']} GeV")
    print(f"      Exposure: {data['exposure']} tonne-year")
    print(f"      Ref: {data['ref']}")

# Cumulative exposure
total_exposure = sum(d['exposure'] for d in limits.values())
print(f"\n   Total exposure across all experiments: ~{total_exposure:.1f} tonne-year")
print(f"   For comparison: 1 tonne-year ~ 10^27 proton-years")

# Standard WIMP "miracle" prediction
print(f"\n2. Standard WIMP 'miracle' prediction:")
print(f"   The thermal relic abundance gives σ_SI ~ 10^-26 cm^3/s annihilation cross section,")
print(f"   which for spin-independent WIMP-nucleon scattering gives σ_SI ~ 10^-44 to 10^-46 cm².")
print(f"   This is the WIMP 'natural' cross section range.")
print(f"   The minimal WIMP miracle prediction: σ_SI ~ 10^-44 cm²")

# Compare with limits
print(f"\n3. Status of WIMP detection:")
print(f"   Current best limit: σ_SI < 9.2e-48 cm² (LZ, June 2024)")
print(f"   This is ~10^4 below the 'natural' WIMP cross section 10^-44 cm²")
print(f"   WIMP parameter space at σ > 10^-46 cm² is essentially EXCLUDED for masses 10-1000 GeV")
print(f"   The WIMP miracle region (σ ~ 10^-44 cm²) has been RULED OUT by orders of magnitude")

# Cascade prediction
print(f"\n4. Cascade prediction:")
print(f"   DM is geometric gravity, not a particle")
print(f"   No WIMP-nucleon coupling exists (no Standard Model coupling to 2D universes)")
print(f"   Predicted signal: ZERO at all cross sections and all WIMP masses")
print(f"   This is a sharper prediction than 'natural' WIMP models")

# Comparison
print(f"\n5. Test verdict:")
print(f"   Cascade predicts: σ_SI = 0 (or effectively unmeasurably small)")
print(f"   Data: σ_SI < 9.2e-48 cm² (no signal observed)")
print(f"   Status: CONSISTENT (no detection = consistent with zero signal)")
print(f"")
print(f"   Caveat: 'Consistent with zero' is also consistent with sub-threshold WIMPs.")
print(f"   The cascade's sharper prediction is that ALL future direct-detection experiments")
print(f"   will also see nothing, even as exposures grow by orders of magnitude.")
print(f"   Sub-threshold WIMPs could eventually be detected; cascade DM cannot.")

# Future projections
print(f"\n6. Future projections:")
print(f"   - LZ-upgrade: ~10x more exposure, σ_SI < ~3e-49 cm²")
print(f"   - XLZD/G3 (next gen): ~100x more exposure, σ_SI < ~1e-50 cm²")
print(f"   - DarkSide-20k (Ar): complementary, similar sensitivity")
print(f"")
print(f"   The cascade's prediction: ALL of these will see zero signal.")
print(f"   If any future direct-detection experiment sees a WIMP-like signal,")
print(f"   the cascade is FALSIFIED.")

# Save results
output_path = "/workspace/github-repo/calculations/direct_detection_null_test_results.txt"
with open(output_path, 'w') as f:
    f.write("Direct Detection Null Test Results\n")
    f.write("==================================\n\n")
    f.write("Cascade prediction: ZERO direct-detection signal at all cross sections.\n")
    f.write("DM is geometric gravity (cascade back-projection), not a particle.\n")
    f.write("No WIMP-nucleon coupling exists; no Standard Model coupling to 2D universes.\n\n")
    
    f.write("Published experimental limits (90% CL, spin-independent WIMP-nucleon):\n")
    for exp, data in limits.items():
        f.write(f"  {exp}: σ_SI < {data['min_sigma_SI']:.2e} cm² at {data['mass_at_min']} GeV\n")
        f.write(f"    Exposure: {data['exposure']} tonne-year, Ref: {data['ref']}\n")
    
    f.write(f"\nTotal exposure: ~{total_exposure:.1f} tonne-year\n\n")
    f.write("Standard WIMP 'miracle' prediction: σ_SI ~ 10^-44 cm²\n")
    f.write("Current best limit: σ_SI < 9.2e-48 cm² (LZ)\n")
    f.write("WIMP 'miracle' parameter space: RULED OUT by ~10^4\n\n")
    f.write("Verdict: CONSISTENT with cascade (no detection observed)\n")
    f.write("Caveat: A future detection would falsify the cascade\n")

print(f"\nResults saved to {output_path}")
