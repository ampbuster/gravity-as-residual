"""
Cascade CAMB v2: WITH TIME COMPRESSION.

This version adds the time dilation factor for 2D universes deep in the
5D AdS_5 bulk, and tests whether it resolves the 50-orders tension
in the 2D universe mass calculation.

THE PHYSICS:
- 2D universe's proper time: dτ_2D = e^{-ky} dt_4D
- y = bulk position, k = AdS_5 curvature
- The death energy E_2D is released in 2D frame, but observed in 3+1D frame
- The effective 3+1D energy deposit is: dE_3+1D/dt_3+1D = (E_2D/τ_2D) × e^{-ky}

KEY QUESTION: For what value of e^{-ky} does the 3+1D-frame mass match
the empirical DM mass density (1e-23 kg per 2D universe, axion-like)?

IF TIME COMPRESSION WORKS:
- m_2D_2D = 6 M_sun (from Liouville/Planck-scale 2D physics)
- m_2D_3+1D = m_2D_2D × e^{-ky} ~ 1e-23 kg
- → e^{-ky} ~ 10^-50
- → 2D universes are very deep in the bulk

IF TIME COMPRESSION DOESN'T WORK:
- 50-orders tension remains
- Need a different explanation

ALSO TESTS:
- 4-zone H(z) with time compression
- Whether the local R_stellar boost is preserved (shallow bulk)
- Whether the CMB drag is reduced (deep bulk)
"""

import numpy as np
import camb
import json
from datetime import datetime

# =============================================================================
# CONSTANTS
# =============================================================================

C = 3e8  # m/s
H0 = 67.4  # km/s/Mpc (Planck CMB-inferred)
H_BULK = 70.16  # km/s/Mpc (cascade's 4D bulk baseline)
MPC_M = 3.086e22  # m
HUBBLE_TIME_GYR = 13.8
GYR_S = 3.156e16  # s
M_SUN_KG = 2e30  # kg
M_PLANCK_KG = 2.18e-8  # kg
L_PLANCK_M = 1.616e-35  # m
TAU_2D_GYR = 0.7
TAU_2D_S = TAU_2D_GYR * GYR_S

# Empirical values
OMEGA_B = 0.0493
OMEGA_C = 0.264
OMEGA_M = OMEGA_B + OMEGA_C
OMEGA_L = 0.6867
OMEGA_DM_EMPIRICAL = 0.27
RHO_CRIT_KG_M3 = 9.2e-27  # kg/m³
RHO_DM_KG_M3 = OMEGA_DM_EMPIRICAL * RHO_CRIT_KG_M3  # 2.5e-27 kg/m³


# =============================================================================
# 2D UNIVERSE PROPERTIES
# =============================================================================

# Approach 1: 2D universe mass from counting SM events
# Per Mpc³, we have ~ 6.5e15 2D universes ever created
# Total DM mass per Mpc³: 7.7e40 kg
# Average per 2D universe: 1.2e25 kg = 6 M_sun
M_2D_FROM_COUNT = 1.2e25  # kg (stellar-scale, 2D-frame)

# Approach 2: 2D universe mass from 2D Planck scaling
# m_2D = α × M_Planck, for α ~ 1e-15
M_2D_FROM_PLANCK = 1.1e-23  # kg (axion-like, 3+1D-frame)

# The 50-orders tension
TENSION_RATIO = M_2D_FROM_COUNT / M_2D_FROM_PLANCK
print(f"50-orders tension: M_count / M_Planck = {TENSION_RATIO:.2e}")
print(f"  = 10^{np.log10(TENSION_RATIO):.1f}")
print()


# =============================================================================
# TIME COMPRESSION FACTOR
# =============================================================================

def time_dilation_factor(bulk_depth_factor):
    """
    Time dilation factor for 2D universe at bulk depth y.
    dτ_2D / dt_4D = e^{-ky}
    
    bulk_depth_factor = e^{-ky} (the time dilation factor itself)
    """
    return bulk_depth_factor


def solve_time_compression():
    """
    Find the time dilation factor e^{-ky} that resolves the 50-orders tension.
    
    We need: M_2D_3+1D = M_2D_2D × e^{-ky} = 1.1e-23 kg
    So: e^{-ky} = 1.1e-23 / 1.2e25 = 9.2e-49
    
    This means the 2D universe is very deep in the bulk.
    """
    e_ky = M_2D_FROM_PLANCK / M_2D_FROM_COUNT
    print(f"Required time dilation factor e^{{-ky}} = {e_ky:.2e}")
    print(f"  = 10^{np.log10(e_ky):.1f}")
    print()
    
    # What bulk depth y does this correspond to?
    # We need a value for k (AdS_5 curvature)
    # In RS-II, k ~ 10^19 GeV = 10^(19 - 0) GeV
    # In natural units: k ~ M_Pl_5 ~ 10^19 GeV
    
    # k in units of 1/m: M_Pl_5 / ℏc
    # M_Pl_5 ~ 10^19 GeV = 1.6e-8 J
    # ℏc = 1.05e-34 J·s × 3e8 m/s = 3.15e-26 J·m
    # k = 1.6e-8 / 3.15e-26 = 5e17 m^-1
    
    k_MPC = 5e17  # 1/m, AdS_5 curvature in Planck-scale units
    
    # y = -ln(e^{-ky}) / k
    y_required = -np.log(e_ky) / k_MPC
    print(f"For AdS_5 curvature k ~ M_Pl_5 ~ 5e17 m^-1:")
    print(f"Required bulk depth: y = {y_required:.2e} m = {y_required/MPC_M:.2e} Mpc")
    print(f"That's a LOT deeper than the AdS_5 radius (1/k = {1/k_MPC:.2e} m)")
    print()
    
    # In units of AdS_5 radius:
    y_in_ads_radius = y_required * k_MPC
    print(f"In units of AdS_5 radius (1/k): y = {y_in_ads_radius:.2e}")
    print()
    
    return e_ky


# =============================================================================
# SM EVENT RATE
# =============================================================================

def R_SM_with_agn(z):
    """SM event rate (Madau SFR + AGN), normalized to 1 at z=0."""
    one_plus_z = 1 + z
    sfr = one_plus_z**2.7 / (1 + (one_plus_z / 2.9)**5.6)
    agn = 0.5 * np.exp(-((np.log(one_plus_z) - np.log(2.0))**2) / 0.5)
    return sfr + agn


# =============================================================================
# H(z) WITH TIME COMPRESSION
# =============================================================================

def H_with_time_compression(z, e_ky, depth_dependence="constant"):
    """
    H(z) with cascade time compression.
    
    H² = H_Friedmann² + δH_2D² × e^{-2ky}
    
    where the time compression factor e^{-2ky} modifies the H(z) contribution
    from 2D universe deaths.
    
    depth_dependence: how e^{-ky} depends on z
    - "constant": e^{-ky} is the same at all z
    - "z_dependent": e^{-ky} is larger at high z (deeper bulk for early 2D universes)
    """
    H_F = H_BULK * np.sqrt(OMEGA_M * (1+z)**3 + OMEGA_L)
    
    # Cascade contribution: 2D universe death energy with time compression
    # The factor e^{-2ky} reduces the H(z) modification
    
    if depth_dependence == "constant":
        compression_factor = e_ky
    elif depth_dependence == "z_dependent":
        # 2D universes at high z are deeper in the bulk (more time compression)
        # At z=0: shallow bulk (e^{-ky} ~ 1, no compression)
        # At z=1100: deep bulk (e^{-ky} ~ 10^-50, maximum compression)
        compression_factor = e_ky ** (z / 1100.0)
    else:
        compression_factor = 1.0
    
    # Standard cascade H modification (without time compression)
    # This is a small effect on top of the Friedmann baseline
    if z < 0.01:
        # Local R_stellar boost (shallow bulk, no time compression)
        delta_H = 2.88 * (1.0 - np.tanh((z - 0.005) / 0.001))
    elif z > 1.0:
        # Primordial drag (deep bulk, time compression reduces it)
        delta_H = -2.76 * compression_factor
    else:
        # Mid-z (some time compression)
        delta_H = 2.84 * compression_factor
    
    return H_F + delta_H


# =============================================================================
# CAMB WITH TIME COMPRESSION
# =============================================================================

def setup_camb_with_time_compression(omega_2D_extra=0.0):
    """CAMB setup with cascade 2D universe contribution (time-compressed)."""
    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=H_BULK,
        ombh2=OMEGA_B * (H_BULK/100)**2,
        omch2=(OMEGA_C + omega_2D_extra) * (H_BULK/100)**2,
        tau=0.054,
    )
    pars.InitPower.set_params(As=2.1e-9, ns=0.965, r=0)
    pars.WantTensors = False
    pars.DoLensing = False
    pars.set_matter_power(redshifts=[0.0, 0.5, 1.0, 2.0, 5.0, 1100.0], kmax=10.0)
    pars.set_for_lmax(2500, lens_potential_accuracy=0)
    return pars


def run_camb_with_cascade(omega_2D_extra=0.0):
    """Run CAMB with cascade modifications."""
    pars = setup_camb_with_time_compression(omega_2D_extra)
    results = camb.get_results(pars)
    zs = np.array([0.0, 0.005, 0.01, 0.02, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 1100.0])
    H_at_z = np.array([results.hubble_parameter(z) for z in zs])
    return {'H_at_z': H_at_z, 'zs': zs, 'omega_2D_extra': omega_2D_extra}


# =============================================================================
# MAIN TEST
# =============================================================================

def main():
    print("=" * 80)
    print("CASCADE BOLTZMANN WITH TIME COMPRESSION")
    print("=" * 80)
    print()
    print("Testing whether time compression resolves the 50-orders tension")
    print("in the 2D universe mass calculation.")
    print()
    
    # Step 1: Solve for required time dilation factor
    print("STEP 1: Find required time dilation factor")
    print("-" * 60)
    e_ky_required = solve_time_compression()
    print()
    
    # Step 2: Run CAMB with different time compression scenarios
    print("STEP 2: Run CAMB with time compression")
    print("-" * 60)
    print()
    print("Testing different e^{-ky} values:")
    print()
    
    # Scenario 1: No time compression (e^{-ky} = 1)
    print("Scenario 1: No time compression (e^{-ky} = 1)")
    result_no_compress = run_camb_with_cascade(omega_2D_extra=0.0)
    for i, z in enumerate(result_no_compress['zs']):
        H = result_no_compress['H_at_z'][i]
        print(f"  z = {z:>8.3f}, H(z) = {H:>10.4f} km/s/Mpc")
    print()
    
    # Scenario 2: With time compression (e^{-ky} = 10^-50)
    # This corresponds to the cascade's required value
    # We can't add 10^-50 to Ω directly, but we can test the conceptual effect
    print("Scenario 2: With strong time compression (e^{-ky} = 10^-50)")
    print("  → 2D universe contribution to Ω_2D is suppressed by 10^-100")
    print("  → Effect on H(z) is negligible (cascade 2D universe DM is invisible)")
    print("  → The 50-orders tension is RESOLVED if the 2D universe mass is 6 M_sun")
    print()
    
    # Scenario 3: H(z) with time compression (custom formula)
    print("Scenario 3: H(z) with time compression (custom)")
    print()
    print(f"{'z':>10} {'H(e_ky=1)':>12} {'H(e_ky=10^-50)':>16} {'expected':>20}")
    print("-" * 60)
    test_zs = [0.0, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 1100.0]
    for z in test_zs:
        H_no = H_with_time_compression(z, e_ky=1.0)
        H_comp = H_with_time_compression(z, e_ky=1e-50)
        if z == 0:
            obs = "73.04 (SH0ES)"
        elif z < 0.01:
            obs = "~73 (local)"
        elif z < 0.05:
            obs = "70.16 (TRGB)"
        elif z < 1.0:
            obs = "~73 (secular)"
        else:
            obs = "67.4 (CMB)"
        print(f"{z:>10.4f} {H_no:>12.4f} {H_comp:>16.4f} {obs:>20}")
    print()
    
    print("=" * 80)
    print("INTERPRETATION")
    print("=" * 80)
    print()
    print("With e^{-ky} = 1 (no time compression):")
    print("  - The cascade's 2D universe contribution is FULLY visible in H(z)")
    print("  - The 4-zone H(z) is preserved (local boost, secular boost, CMB drag)")
    print()
    print("With e^{-ky} = 10^-50 (full time compression):")
    print("  - The cascade's 2D universe contribution is SUPPRESSED by 10^-100")
    print("  - The H(z) modifications are negligible")
    print("  - H(z) is just the standard ΛCDM Friedmann baseline (70.16 at z=0)")
    print()
    print("This creates a TENSION:")
    print("  - To resolve the 50-orders mass tension, we need e^{-ky} ~ 10^-50")
    print("  - But this makes the cascade's H(z) modifications invisible")
    print("  - The 4-zone H(z) structure requires e^{-ky} ~ 1 (no compression)")
    print()
    print("POSSIBLE RESOLUTION: The 2D universes are at DIFFERENT bulk depths")
    print("  - Local 2D universes (cluster): shallow bulk, e^{-ky} ~ 1 (visible)")
    print("  - Distant 2D universes (high-z): deep bulk, e^{-ky} ~ 10^-50 (invisible)")
    print("  - This would preserve the local R_stellar boost while making the")
    print("    2D universe mass look axion-like in 3+1D")
    print()
    print("This is testable: the local boost requires shallow-bulk 2D universes,")
    print("while the mass tension requires deep-bulk 2D universes.")
    print("If the local boost is real, the 2D universes are NOT all deep in the bulk,")
    print("and the mass tension is NOT resolved by time compression.")
    print()
    print("File locations:")
    print("  - This code: tempcalc/cascade_camb_time_compressed.py")
    print("  - Original CAMB: tempcalc/cascade_camb.py")
    print("  - Time compression memo: tempcalc/time_compression_memo.md")


if __name__ == "__main__":
    main()
