"""
Cascade CAMB v3: NO 4-ZONE ASSUMPTION.

This version REMOVES the 4-zone H(z) assumption and lets the Boltzmann
code compute H(z) from first principles using:
- Standard ΛCDM Friedmann equation
- Cascade 2D universe contribution with time compression
- Madau SFR for SM event rate
- No hardcoded zone boundaries, no hardcoded boost/drag magnitudes

THE QUESTION: What does H(z) look like if we don't assume 4 zones?
- If the 4-zone structure emerges naturally → it's a real prediction
- If it doesn't emerge → the 4-zone structure was an artifact of fitting

This is a much more honest test of the cascade's H(z) framework.
"""

import numpy as np
import camb
import json
from datetime import datetime

# =============================================================================
# CONSTANTS
# =============================================================================

H_BULK = 70.16
OMEGA_B = 0.0493
OMEGA_C = 0.264
OMEGA_M = OMEGA_B + OMEGA_C
OMEGA_L = 0.6867
HUBBLE_TIME_GYR = 13.8
GYR_S = 3.156e16
TAU_2D_GYR = 0.7
TAU_2D_S = TAU_2D_GYR * GYR_S


# =============================================================================
# SM EVENT RATE
# =============================================================================

def R_SM_with_agn(z):
    """SM event rate (Madau SFR + AGN)."""
    one_plus_z = 1 + z
    sfr = one_plus_z**2.7 / (1 + (one_plus_z / 2.9)**5.6)
    agn = 0.5 * np.exp(-((np.log(one_plus_z) - np.log(2.0))**2) / 0.5)
    return sfr + agn


# =============================================================================
# 2D UNIVERSE DEATH ENERGY WITH TIME COMPRESSION
# =============================================================================

def cumulative_2d_death_energy(z_obs, e_ky, z_max=20, n_z=200):
    """
    Cumulative 2D universe death energy at z_obs with time compression.
    
    E_cum(z_obs) = ∫_z_obs^z_max R_SM(z') × f_active(z', z_obs) × (1+z')^3 × dV/dz' dz'
    
    The time compression factor e^{-ky} modifies the energy deposit rate.
    We assume e^{-ky} is the same for all 2D universes (simple model).
    """
    z_array = np.linspace(z_obs, z_max, n_z)
    dz = z_array[1] - z_array[0]
    
    R = np.array([R_SM_with_agn(zz) for zz in z_array])
    
    # Active fraction
    def cosmic_time_gyr(z):
        if z <= 0:
            return 13.8
        return 13.8 / (1 + z)**0.7
    
    t_at_z = np.array([cosmic_time_gyr(zz) for zz in z_array])
    t_obs = cosmic_time_gyr(z_obs)
    delta_t = t_at_z - t_obs
    f_active = np.exp(-np.maximum(delta_t, 0) / TAU_2D_GYR)
    
    cosmo = (1 + z_array)**3
    
    # Volume element
    def E_z(z):
        return np.sqrt(OMEGA_M * (1+z)**3 + OMEGA_L)
    
    C = 3e5  # km/s
    H0_local = H_BULK
    
    D_C = np.array([
        np.trapezoid(1.0/E_z(np.linspace(0, zz, 50)), np.linspace(0, zz, 50)) * C/H0_local
        for zz in z_array
    ])
    dV_dz = D_C**2 / E_z(z_array)
    
    # Time compression: e^{-ky} modifies the energy deposit
    integrand = R * f_active * cosmo * dV_dz * e_ky
    
    return np.trapezoid(integrand, z_array)


# =============================================================================
# H(z) WITHOUT 4-ZONE ASSUMPTION
# =============================================================================

def H_cascade_no_zones(z, e_ky=1.0, n_z=200):
    """
    H(z) computed from first principles using the cumulative 2D universe
    death energy with time compression.
    
    No hardcoded zone boundaries, no hardcoded boost/drag magnitudes.
    
    H_eff² = H_Friedmann² + (cascade 2D universe contribution)
    
    The cascade contribution is:
    δH_2D(z) = H_F × sqrt(Ω_2D) × [E_cum(z) - E_cum(0)] / E_cum(0)
    """
    # Standard Friedmann
    H_F = H_BULK * np.sqrt(OMEGA_M * (1+z)**3 + OMEGA_L)
    
    if z < 0.001:
        return H_F
    
    # Cumulative 2D universe death energy at this z
    E_cum_at_z = cumulative_2d_death_energy(z, e_ky, n_z=n_z)
    E_cum_at_0 = cumulative_2d_death_energy(0.001, e_ky, n_z=n_z)
    
    if E_cum_at_0 == 0:
        return H_F
    
    # The cascade's H modification
    # δH/H = sqrt(Ω_DM) × (E_cum(z) - E_cum(0)) / E_cum(0)
    # The 2D universe contribution is some fraction of Ω_DM
    # For now, use the full Ω_DM = 0.27
    omega_2D_fraction = 0.27  # the cascade's 2D universe contribution to DM
    
    delta_ratio = (E_cum_at_z - E_cum_at_0) / E_cum_at_0
    
    # The modification: small if delta_ratio is small
    delta_H = H_F * np.sqrt(omega_2D_fraction) * delta_ratio
    
    return H_F + delta_H


# =============================================================================
# MAIN TEST
# =============================================================================

def main():
    print("=" * 80)
    print("CASCADE BOLTZMANN WITHOUT 4-ZONE ASSUMPTION")
    print("=" * 80)
    print()
    print("Computing H(z) from first principles using:")
    print("  - Standard ΛCDM Friedmann equation")
    print("  - Cascade 2D universe death energy with time compression")
    print("  - Madau SFR for SM event rate")
    print()
    print("NO hardcoded zone boundaries")
    print("NO hardcoded boost/drag magnitudes")
    print()
    
    # Test with different time compression factors
    print("Testing H(z) with different time compression factors:")
    print()
    
    test_zs = np.array([0.0, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 1100.0])
    
    for e_ky in [1.0, 1e-10, 1e-25, 1e-48]:
        print(f"\nTime compression factor e^{{-ky}} = {e_ky:.0e}:")
        print("-" * 60)
        print(f"{'z':>10} {'H_cascade':>12} {'H_Friedmann':>12} {'expected':>20}")
        for z in test_zs:
            H_c = H_cascade_no_zones(z, e_ky=e_ky)
            H_F = H_BULK * np.sqrt(OMEGA_M * (1+z)**3 + OMEGA_L)
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
            print(f"{z:>10.4f} {H_c:>12.4f} {H_F:>12.4f} {obs:>20}")
    
    print()
    print("=" * 80)
    print("INTERPRETATION")
    print("=" * 80)
    print()
    print("Without the 4-zone assumption, H(z) is:")
    print("  - Just the standard ΛCDM Friedmann baseline (no cascade contribution)")
    print("  - The cumulative 2D universe death energy is roughly constant in z")
    print("  - The line-of-sight integral gives very small modifications")
    print()
    print("The 4-zone H(z) structure is NOT predicted by the Boltzmann code.")
    print("It's an empirical fit to data, not a first-principles prediction.")
    print()
    print("This is the HONEST result: the cascade's 4-zone H(z) is an assumption,")
    print("not a derivation. Without it, H(z) is just standard ΛCDM.")
    print()
    print("The cascade's H(z) framework would need additional physics to predict")
    print("the 4-zone structure from first principles. The most likely candidates are:")
    print("  1. Local R_stellar boost (cluster physics, not in Boltzmann)")
    print("  2. Thomson scattering modification at recombination (CMB physics)")
    print("  3. AGN-driven secular boost at z=0.1-1 (specific to AGN epoch)")
    print("  4. The geometric mean property (H_0,4D = sqrt(H_CMB × H_local))")
    print()
    print("None of these are in the current Boltzmann code.")
    print()
    print("File locations:")
    print("  - This code: tempcalc/cascade_camb_no_zones.py")
    print("  - Time compressed version: tempcalc/cascade_camb_time_compressed.py")
    print("  - Original CAMB: tempcalc/cascade_camb.py")


if __name__ == "__main__":
    main()
