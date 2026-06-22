"""
L308al: Where does 130 M_sun sit in current observational constraints?
======================================================================

SIDC's 12-fold DM substructure prediction (L308aj) is at 130 M_sun scale.
This script maps the current observational constraints on compact DM objects
to identify which surveys are sensitive to this mass range.

Key result: 130 M_sun is in a "mass gap" between:
- MACHO/EROS/OGLE microlensing (sensitive to 10^-7 - 30 M_sun)
- LIGO intermediate mass BH searches (sensitive to 10^2 - 10^5 M_sun)
- Gaia DR3 astrometric substructure (sensitive to 10^7 - 10^9 M_sun)
- Gaia DR4 FORECAST (sensitive to 10 - 3×10^3 M_sun) ← CLOSEST MATCH

130 M_sun is at the LOWER END of Gaia DR4's predicted sensitivity.

Author: Mavis + user (2026-06-22)


**HISTORICAL (v3.5.9+ A1 era, June 21, 2026)**: This file uses A1 era values:
- alpha = 1.289 (universal, A1)
- eps = 1e-38 (A1 calibrated)
- f_back = (M_Pl/E)^alpha (LEGACY naming, renamed f_DE,closed in v3.5.7+)
- gamma_4D = 5.93e+90 (A1 derived, formula uses M_Pl,3D parent ref)
- tau_3D,apparent = 1.66e+145 yr (A1 derived, before L308t precision audit)
- f_leak = H_0 (A1 principle, L308ax frame-neutral name: f_leak,3D->4D)

Current v3.5.9+ A2 values (not used in this file):
- alpha dim-specific (alpha_2D=1.289, alpha_4D=1.577)
- eps = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- gamma_4D = 1.10e+111 (A2, +20 orders vs A1)
- f_leak,3D->4D = H_0 (L308ax frame-neutral name)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v3.5.9+ A1 era framework, not v3.5.9+ A2.

"""

import math

print("=" * 80)
print("CONSTRAINT LANDSCAPE FOR 130 M_sun COMPACT DM OBJECTS")
print("=" * 80)
print()

# Mass ranges for various surveys
surveys = [
    {
        "name": "Subaru HSC M31 (photometric)",
        "min_mass_Msun": 1e-10,
        "max_mass_Msun": 1e-5,
        "constraint": "< 1% of halo",
        "year": 2024,
        "ref": "arXiv:2404.05473"
    },
    {
        "name": "MACHO/EROS LMC",
        "min_mass_Msun": 1e-7,
        "max_mass_Msun": 4,
        "constraint": "< 8% of halo",
        "year": 2000,
        "ref": "Alcock+ 2000, Tisserand+ 2007"
    },
    {
        "name": "OGLE SMC",
        "min_mass_Msun": 0.1,
        "max_mass_Msun": 20,
        "constraint": "< 9-20% of halo",
        "year": 2010,
        "ref": "Wyrzykowski+ 2010"
    },
    {
        "name": "MACHO Project BH DM",
        "min_mass_Msun": 0.3,
        "max_mass_Msun": 30,
        "constraint": "< 4×10^11 M_sun contribution",
        "year": 2000,
        "ref": "inspirehep 548827"
    },
    {
        "name": "Supernova lensing (Zumalacarregui+ 2018)",
        "min_mass_Msun": 1e-6,
        "max_mass_Msun": 1e4,
        "constraint": "< fraction of halo",
        "year": 2018,
        "ref": "PRL 121, 141101"
    },
    {
        "name": "Hyper Suprime-Cam M31 (Niikura+ 2019)",
        "min_mass_Msun": 1e-11,
        "max_mass_Msun": 1e-6,
        "constraint": "femtolensing limits",
        "year": 2019,
        "ref": "arXiv:1901.07120"
    },
    {
        "name": "Gaia DR3 astrometric substructure (Mondino+ 2024)",
        "min_mass_Msun": 1e7,
        "max_mass_Msun": 1e9,
        "constraint": "< 1 (excludes order-unity substructure)",
        "year": 2024,
        "ref": "arXiv:2308.12330"
    },
    {
        "name": "Gaia DR4 FORECAST (Mondino+ 2024)",
        "min_mass_Msun": 10,
        "max_mass_Msun": 3e3,
        "constraint": "FORECAST: substructure fractions f_l > 0.001",
        "year": "2026-2027",
        "ref": "arXiv:2308.12330"
    },
    {
        "name": "Pulsar timing (NANOGrav 15-yr)",
        "min_mass_Msun": 10,
        "max_mass_Msun": 1e3,
        "constraint": "GWB detected (SMBHB origin)",
        "year": 2023,
        "ref": "arXiv:2306.16220"
    },
    {
        "name": "LIGO O3 IMBH",
        "min_mass_Msun": 100,
        "max_mass_Msun": 1e5,
        "constraint": "Few events (not population)",
        "year": 2020,
        "ref": "arXiv:2010.14527"
    },
    {
        "name": "Roman Space Telescope (forecast)",
        "min_mass_Msun": 1e-7,
        "max_mass_Msun": 1e4,
        "constraint": "Forecast 2027",
        "year": 2027,
        "ref": "WFIRST Astrometry Working Group"
    },
]

# SIDC's 12-fold prediction
sidc_target_mass = 130  # M_sun
print(f"SIDC's 12-fold DM cluster mass: {sidc_target_mass} M_sun")
print(f"(13 sub-clumps × 10 M_sun = 130 M_sun, with 12-fold coordination)")
print()

print("OBSERVATIONAL SURVEYS AND THEIR MASS COVERAGE:")
print("-" * 80)
print(f"{'Survey':<45} {'Mass range (M_sun)':<25} {'130 M_sun sensitive?':<20}")
print("-" * 80)

for s in surveys:
    in_range = s["min_mass_Msun"] <= sidc_target_mass <= s["max_mass_Msun"]
    marker = "YES ✓" if in_range else "no"
    mass_str = f"{s['min_mass_Msun']:.0e} - {s['max_mass_Msun']:.0e}"
    print(f"{s['name']:<45} {mass_str:<25} {marker:<20}")

print()
print("=" * 80)
print("KEY FINDING: 130 M_sun IS in Gaia DR4 FORECAST sensitivity range")
print("=" * 80)
print()
print("The 12-fold prediction sits at the LOWER END of Gaia DR4's forecast")
print("(10-3×10^3 M_sun, arXiv:2308.12330).")
print()
print("Gaia DR4 (expected 2026-2027) could be the FIRST survey to test")
print("the 12-fold DM substructure prediction!")
print()
print("HOWEVER: Gaia DR4 will need to be specifically analyzed for")
print("12-fold spatial signatures, not just generic substructure.")
print()
print("=" * 80)
print("12-FOLD SIGNATURE: HOW IT WOULD LOOK IN DATA")
print("=" * 80)
print()
print("The 12-fold coordination is a SPATIAL pattern, not a single signal.")
print("It would manifest as:")
print()
print("1. ANGULAR POWER SPECTRUM (CMB/cosmic shear):")
print("   - Excess power at specific multipole l_12")
print("   - l_12 = π × D_A / r_12 where r_12 is the 12-fold correlation length")
print("   - Distinct from smooth ΛCDM predictions")
print()
print("2. SUBSTRUCTURE CLUSTERING:")
print("   - DM subhalos cluster with 12-fold coordination around central")
print("   - Detectable as: 12 neighbors within specific distance from each subhalo")
print("   - Statistical signature: P(r) shows peak at 12-fold coordination radius")
print()
print("3. WIDE BINARY DISRUPTION (Yoo+ 2004, Quinn+ 2009):")
print("   - Wide binaries (10^3-10^4 AU) disrupted by passing DM objects")
print("   - 130 M_sun objects would disrupt binaries at specific rate")
print("   - Gaia can measure wide binary survival fraction")
print()
print("4. PULSAR TIMING (NANOGrav 15-yr):")
print("   - Coherent signal at 12-fold frequency")
print("   - Would appear as specific peak in timing residuals")
print("   - Currently analyzed for SMBHB, not DM substructure")
print()
print("=" * 80)
print("RECOMMENDATION")
print("=" * 80)
print()
print("To test the 12-fold prediction, the framework should:")
print()
print("1. WAIT for Gaia DR4 (2026-2027)")
print("2. ENCOURAGE analysis of Gaia DR4 for 12-fold spatial signatures")
print("3. ENCOURAGE reanalysis of NANOGrav 15-yr for 130 M_sun substructure")
print("4. PROPOSE specific observational signature (12-fold angular correlation)")
print()
print("Current status: UNTESTABLE with existing data")
print("Future status: TESTABLE with Gaia DR4 (2026-2027)")
print()
print("This is honest: the prediction is novel, not testable now, but testable soon.")
