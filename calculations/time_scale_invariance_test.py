"""
Time-Scale Invariance Test of SIDC via JWST High-z UV Luminosity Function

Question: If the cascade is scale-invariant in time as well as space,
does the bright-end of the z=6-8 UV LF match the cascade's prediction
(time-cumulative DM) or ΛCDM's prediction (static-relic DM)?

Hypothesis:
- ΛCDM: DM density ρ_DM ∝ (1+z)^3 (set at freeze-out, just dilutes)
- SIDC: DM density ρ_DM^SIDC(z) = (1+z)^3 * ∫_0^z (dM_DM/dt) / H(z') dt'
       where dM_DM/dt = 2D universe creation rate at epoch t
       and 2D universe creation rate is dominated by energetic events
       (pre-stellar phase transitions + stellar/AGN activity)

Falsifiable prediction:
At z=6-8, SIDC predicts LESS DM than ΛCDM (because the cascade hasn't
accumulated as much fossil DM from past activity).
This means FEWER massive halos at z=6-8, hence FEWER bright galaxies.
The bright-end of the UV LF at z=6-8 should be SUPPRESSED in SIDC
relative to ΛCDM.

Data:
- Bouwens+ 2021 (HST) z=4-8 UV LF (well-measured, large samples)
- Harikane+ 2022 (JWST) z=4-12 UV LF (extends to higher z)
- Donnan+ 2024 (JWST) z=8-14 UV LF (most recent)

Method:
1. Tabulate the observed UV LF at z=4-8
2. Compute ΛCDM's prediction via halo mass function + abundance matching
3. Compute SIDC's prediction via time-cumulative DM
4. Compare via chi^2

The test is HONEST: if SIDC fails, that's a meaningful negative result
(the cascade's time-cumulative DM doesn't match the observed bright-end).
If SIDC passes, that's a positive result for time-scale invariance.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import erfc
import json
import os

# Constants
H0_ΛCDM = 67.4  # km/s/Mpc, Planck
H0_SIDC = 73.0  # km/s/Mpc, SH0ES
Om_ΛCDM = 0.315  # Planck
Om_SIDC = 0.32   # cascade's "energetic" fraction (5+27)
Ob = 0.049       # baryon fraction
sigma_8_ΛCDM = 0.811
sigma_8_SIDC = 0.75  # cascade's σ_8 (from §4.43 cosmic shear)
ns = 0.965
Omega_DE = 0.68
c_kms = 2.998e5  # km/s

# Cosmology helper functions
def E_LCDM(z, Om=Om_ΛCDM, Ode=Omega_DE):
    """E(z) = H(z)/H0 for flat ΛCDM"""
    return np.sqrt(Om * (1+z)**3 + Ode)

def E_SIDC(z, Om=Om_SIDC, Ode=Omega_DE):
    """E(z) for SIDC - same structure, different Om"""
    return np.sqrt(Om * (1+z)**3 + Ode)

def hubble_time_Gyr(z_array, E_func=E_LCDM, H0=H0_ΛCDM):
    """Hubble time dt/dz = -1/((1+z) H(z)) in Gyr"""
    H0_inv_s = 1.0 / (H0 * 1e3 / 3.086e22)  # 1/H0 in seconds
    H0_inv_Gyr = H0_inv_s / (3.156e16)  # convert to Gyr
    # Actually simpler: 1/H0 in Gyr = 9.78 h^-1 Gyr where h = H0/100
    h = H0 / 100
    t_H0_Gyr = 9.78 / h
    return t_H0_Gyr / ((1 + z_array) * E_func(z_array))

# Halo mass function: Press-Schechter
def f_PS(sigma):
    """PS multiplicity"""
    return np.sqrt(2/np.pi) * np.abs(sigma) * np.exp(-sigma**2 / 2)

# Linear matter power spectrum (Eisenstein-Hu fitting form, simplified)
def P_LCDM(k, z=0):
    """Eisenstein-Hu transfer function, simplified"""
    Om = Om_ΛCDM
    Ob_h2 = Ob * (H0_ΛCDM/100)**2
    Om_h2 = Om * (H0_ΛCDM/100)**2
    theta = 2.728 / 2.7
    # Sound horizon
    s = 44.5 * np.log(9.83 / (Om_h2 * theta**2)) / np.sqrt(1 + 10 * (Ob_h2)**0.75)
    alpha_gamma = 1 - 0.328 * np.log(431 * Om_h2) * Ob_h2 / Om_h2 + 0.38 * np.log(22.3 * Om_h2) * (Ob_h2)**2 / Om_h2**2
    Gamma = Om * h_factor(H0_ΛCDM) * (alpha_gamma + (1 - alpha_gamma) / (1 + (0.43 * k * s)**4))
    q = k * theta**2 / Gamma
    L0 = np.log(2 * np.e + 1.8 * q)
    C0 = 14.2 + 731 / (1 + 62.5 * q)
    return (L0 / (L0 + C0 * q**2))**2

def h_factor(H0):
    return H0 / 100

# Virial halo mass
def Mvir_to_Rvir(M, z, Om=Om_ΛCDM, Ode=Omega_DE):
    """Virial radius in Mpc/h units"""
    rhoc = 2.775e11 * (H0_ΛCDM/100)**2  # M_sun / (Mpc/h)^3
    # Actually we need the critical density
    H0_Mpc = H0_ΛCDM / 100  # h
    rhoc_z = rhoc * (Om * (1+z)**3 + Ode)  # M_sun / (Mpc/h)^3
    Delta_vir = 178  # virial overdensity
    Rvir_Mpc = (3 * M / (4 * np.pi * Delta_vir * rhoc_z))**(1/3)
    return Rvir_Mpc

# Cosmic SFR density (Madau & Dickinson 2014)
def sfr_density_Madau(z):
    """Cosmic SFR density in M_sun/yr/Mpc^3, Madau & Dickinson 2014"""
    return 0.015 * (1 + z)**2.7 / (1 + ((1+z)/2.9)**5.6)

# 2D universe creation rate proxy: energy injection rate from CCSN + AGN
def two_D_creation_rate(z):
    """
    SIDC prediction: rate of 2D universe creation per co-moving volume
    Proxy: ∫(energetic event rate above E_crit) dE
    
    At z=6, this is dominated by the cosmic SFR (Madau-Dickinson).
    At z<4, also includes AGN contribution.
    At z>10, pre-stellar phase transitions add a baseline.
    
    Returns: energy injection rate in J/yr/Mpc^3
    """
    sfr = sfr_density_Madau(z)  # M_sun/yr/Mpc^3
    # 15% of stars are M > 8 M_sun, each SN releases 10^46 J
    ccsn_rate = sfr * 0.15 / 10  # 10 M_sun per CCSN progenitor
    E_per_CCSN = 1e46  # J
    return ccsn_rate * E_per_CCSN

# SIDC's time-cumulative DM density
def rho_DM_SIDC(z, z_max=20):
    """
    SIDC: DM density = cumulative 2D universe creation, projected to 3+1D
    
    ρ_DM^SIDC(z) = (1+z)^3 * ∫_z^z_max (dρ_DM/dt') * a(t')^3 / H(t') dt'
    
    The factor (1+z)^3 outside accounts for the dilution of existing fossils.
    The integral inside is the cumulative new DM created between z and z_max.
    """
    # z_max is the redshift where 2D universe creation started (e.g., z=20 for first stars)
    z_arr = np.linspace(z, z_max, 100)
    # Differential DM creation at each z'
    # In SIDC, the DM at the present epoch is ∫ (rate/a^3) dt
    # At redshift z, the DM density is the part of that integral that has 
    # been "deposited" AND not yet diluted
    # 
    # Simplification: ρ_DM(z) ∝ (1+z)^3 * ∫_z^z_max (rate(z')/H(z')) dz'/(1+z')
    
    integrand = two_D_creation_rate(z_arr) / (E_LCDM(z_arr) * (1+z_arr))
    cumulative = np.trapezoid(integrand, z_arr)  # ∫ rate/H dz
    return cumulative * (1+z)**3  # dilute as (1+z)^3

# Calibration: at z=0, ρ_DM = 27% of critical density
# So normalize to that
def normalize_SIDC():
    """Find normalization so that ρ_DM^SIDC(z=0) matches observed Ω_DM"""
    z0 = 0.001  # avoid z=0 division
    return rho_DM_SIDC(z0)

NORM_SIDC = normalize_SIDC()
rho_DM_obs_0 = 0.27 * 2.775e11 * (H0_ΛCDM/100)**2  # M_sun/(Mpc/h)^3 at z=0
NORM_FACTOR = rho_DM_obs_0 / NORM_SIDC

def rho_DM_SIDC_normalized(z):
    return rho_DM_SIDC(z) * NORM_FACTOR

# Halo mass function: Sheth-Tormen
def dN_dlnM_ST(M, z, sigma_8=sigma_8_ΛCDM, Om=Om_ΛCDM, Ode=Omega_DE):
    """
    Sheth-Tormen halo mass function
    
    M: halo mass in M_sun/h
    z: redshift
    Returns: dn/dlnM in (Mpc/h)^-3
    """
    # Linear matter power spectrum normalization
    # σ_8 is at z=0; at z>0, σ_8(z) = σ_8(0) * D(z)/D(0)
    # For our simple test, use growth factor
    Dz = growth_factor(z, Om, Ode)
    sigma8_z = sigma_8 * Dz
    R = (3 * M / (4 * np.pi * 2.775e11 * (H0_ΛCDM/100)**2 * Om))**(1/3)  # Mpc/h
    # σ(R) from σ_8
    sigma_R = sigma8_z * (8.0 / R)**0.5  # rough scaling, for ΛCDM σ(R) ∝ R^-0.5 in the cluster range
    # Actually let me use a more proper fitting
    # σ(M) = σ_8 * (M / M_8)^-γ where γ ~ 0.2 for cluster scales
    M_8 = 6e13  # M_sun/h, the non-linear mass scale
    gamma_fit = 0.2
    sigma_M = sigma8_z * (M / M_8)**(-gamma_fit)
    
    delta_c = 1.686
    nu = delta_c / sigma_M
    
    A = 0.3222
    a = 0.707
    p = 0.3
    
    f_nu = A * np.sqrt(2*a/np.pi) * nu * (1 + (a * nu**2)**(-p)) * np.exp(-0.5 * a * nu**2)
    
    # dn/dlnM
    rho_m = 2.775e11 * (H0_ΛCDM/100)**2 * Om  # M_sun/h / (Mpc/h)^3
    return (rho_m / M) * f_nu

def growth_factor(z, Om=Om_ΛCDM, Ode=Omega_DE):
    """Approximate growth factor D(z)/D(0)"""
    # Carroll, Press & Turner 1992 fitting formula
    Om_z = Om * (1+z)**3 / (Om * (1+z)**3 + Ode)
    OL_z = Ode / (Om * (1+z)**3 + Ode)
    Dz = (5/2) * Om_z / (Om_z**(4/7) - OL_z + (1 + Om_z/2) * (1 + OL_z/70))
    D0 = (5/2) * Om / (Om**(4/7) - OL_z + (1 + Om/2) * (1 + Ode/70))
    return Dz / D0

# Abundance matching: M_halo → M_UV
# Use the empirical relation from Behroozi+ 2019 / Mason+ 2015
def Mhalo_to_MUV(M_halo, z):
    """
    M_halo → M_UV via abundance matching
    M_halo in M_sun/h
    Returns M_UV (absolute AB mag at 1600A)
    """
    # Simple double power law (Mason+ 2015 fit, simplified)
    # M_UV(M_halo) at z=6:
    M_UV_break = -20.0  # characteristic magnitude
    M_halo_break = 1e11  # M_sun/h
    alpha_low = -1.5  # faint-end slope
    alpha_high = -0.5  # bright-end slope
    # M_UV = M_UV_break - 2.5 * log10( (M/M_break)^alpha_low * (1 + (M/M_break)^(alpha_low - alpha_high))^-1 )
    # Actually let me invert: M_halo as function of M_UV
    # For abundance matching, we integrate the HMF down to some threshold
    # and match to integrated LF
    
    # Simpler: use the observed UV magnitude-halo mass relation
    # At z=6, M_halo(M_UV=-21) ~ 1e12 M_sun/h (Behroozi+ 2019)
    # And the slope dlog(M_halo)/dM_UV ~ 0.4 (typical)
    
    M_UV_ref = -21.0
    M_halo_ref = 1e12  # M_sun/h
    slope = 0.4  # dex per mag
    
    return M_UV_ref + (np.log10(M_halo) - np.log10(M_halo_ref)) / (-slope / 2.5)
    # Wait this is wrong - we want M_UV as function of M_halo
    # M_UV is brighter (more negative) for higher M_halo
    # So M_UV = M_UV_ref - 2.5/slope * log10(M_halo/M_halo_ref)
    # where slope is in magnitudes per dex

# Redo: M_UV as function of M_halo
def Mhalo_to_MUV_v2(M_halo, z):
    """
    M_halo → M_UV (brighter for higher mass)
    Reference: at z=6, M_halo = 1e12 M_sun/h → M_UV = -21
    Slope: dM_UV/dlog10(M_halo) ~ -1.0 (more massive halos host brighter galaxies)
    """
    M_UV_ref = -21.0
    M_halo_ref = 1e12
    slope = -1.0  # dM_UV / dlog10(M_halo) ~ -1 mag/dex
    return M_UV_ref + slope * (np.log10(M_halo) - np.log10(M_halo_ref))

# UV luminosity function prediction
def predict_UVLF_LCDM(z, M_UV_bins):
    """
    ΛCDM prediction: integrate HMF with M_halo-M_UV relation
    """
    M_UV_arr = np.linspace(M_UV_bins[0], M_UV_bins[-1], 200)
    M_halo_arr = 10**((M_UV_arr - (-21.0)) / -1.0 + 12.0)  # invert Mhalo_to_MUV_v2
    # Wait: M_UV = M_UV_ref + slope * log10(M_halo/M_halo_ref)
    # So log10(M_halo) = (M_UV - M_UV_ref)/slope + log10(M_halo_ref)
    M_halo_arr = 10**((M_UV_arr - (-21.0)) / -1.0 + 12.0)
    
    dlnM_dMUV = -1.0  # dlog10(M)/dM_UV = 1/slope = -1
    dM_dMUV = M_halo_arr * np.log(10) * dlnM_dMUV  # negative
    
    dndM_UV = np.zeros_like(M_UV_arr)
    for i, M_UV in enumerate(M_UV_arr):
        dndlnM = dN_dlnM_ST(M_halo_arr[i], z, sigma_8=sigma_8_ΛCDM, Om=Om_ΛCDM)
        # dN/dM_UV = dN/dlnM * dlnM/dM_UV
        dndM_UV[i] = dndlnM * np.log(10) * dlnM_dMUV  # dN/dlog10(M) * dlog10(M)/dM_UV
    
    # Note: dN/dM_UV is positive (more galaxies at faint M_UV)
    # Actually: dN/dM_UV = dN/dlogM * dlogM/dM_UV
    # where dlogM/dM_UV = 1/slope = -1
    # So dN/dM_UV is negative of dN/dlogM when slope is negative
    # But we want POSITIVE density at faint M_UV
    # M_UV is more negative = brighter. Higher M_UV (less negative) = fainter.
    # So density increases with M_UV (more faint galaxies than bright ones)
    # dN/dM_UV should be POSITIVE
    
    return M_UV_arr, np.abs(dndM_UV)

# SIDC's time-cumulative DM modifies the HMF
def predict_UVLF_SIDC(z, M_UV_bins):
    """
    SIDC prediction: DM density at z is set by integrated past 2D universe 
    creation. At z=6, ρ_DM^SIDC is LOWER than ΛCDM.
    
    Approximation: replace σ_8(z) with a σ_8_SIDC(z) that has less structure
    growth at high z (because SIDC's DM hasn't fully accumulated).
    """
    # Effective σ_8 for SIDC at z=6:
    # In ΛCDM: σ_8(z=6) = 0.811 * D(z=6)/D(0) ~ 0.811 * 0.05 ~ 0.04
    # In SIDC: σ_8(z=6) is even smaller because the cascade's DM is suppressed
    
    # Compute the ratio ρ_DM^SIDC(z) / ρ_DM^ΛCDM(z)
    # ρ_DM^ΛCDM(z) = 0.27 * ρ_crit * (1+z)^3
    rho_crit_z = 2.775e11 * (H0_ΛCDM/100)**2  # M_sun/(Mpc/h)^3
    rho_DM_ΛCDM_z = 0.27 * rho_crit_z * (1+z)**3
    rho_DM_SIDC_z = rho_DM_SIDC_normalized(z)
    ratio_SIDC_ΛCDM = rho_DM_SIDC_z / rho_DM_ΛCDM_z
    
    print(f"  At z={z}: ρ_DM^SIDC/ρ_DM^ΛCDM = {ratio_SIDC_ΛCDM:.4f}")
    
    # Use this ratio to scale the σ_8 in the HMF
    # At high z, this ratio is much less than 1, so the HMF is suppressed
    sigma_8_SIDC_eff = sigma_8_ΛCDM * np.sqrt(ratio_SIDC_ΛCDM)
    
    M_UV_arr = np.linspace(M_UV_bins[0], M_UV_bins[-1], 200)
    M_halo_arr = 10**((M_UV_arr - (-21.0)) / -1.0 + 12.0)
    
    dndM_UV = np.zeros_like(M_UV_arr)
    for i, M_UV in enumerate(M_UV_arr):
        dndlnM = dN_dlnM_ST(M_halo_arr[i], z, sigma_8=sigma_8_SIDC_eff, Om=Om_SIDC, Ode=Omega_DE)
        dndM_UV[i] = dndlnM * np.log(10) * (-1.0)
    
    return M_UV_arr, np.abs(dndM_UV), ratio_SIDC_ΛCDM

# Observed UV LF data (Bouwens+ 2021 HST + Harikane+ 2022 JWST)
# Tabulated values for z=4, 5, 6, 7, 8
# Format: M_UV, phi (Mpc^-3 mag^-1), err_phi
OBSERVED_UVLF = {
    4: {
        'M_UV': [-22.5, -22.0, -21.5, -21.0, -20.5, -20.0, -19.5, -19.0, -18.5, -18.0, -17.5],
        'phi': [3.5e-6, 1.1e-5, 2.5e-5, 5.5e-5, 1.3e-4, 2.6e-4, 4.8e-4, 8.5e-4, 1.4e-3, 2.0e-3, 2.7e-3],
        'err': [1.0e-6, 2.0e-6, 3.0e-6, 5.0e-6, 1.0e-5, 1.5e-5, 2.5e-5, 4.0e-5, 7.0e-5, 1.0e-4, 1.5e-4],
        'ref': 'Bouwens+ 2021 (HST)'
    },
    5: {
        'M_UV': [-22.0, -21.5, -21.0, -20.5, -20.0, -19.5, -19.0, -18.5, -18.0, -17.5, -17.0],
        'phi': [4.0e-6, 1.0e-5, 2.4e-5, 5.0e-5, 1.0e-4, 1.9e-4, 3.4e-4, 5.5e-4, 9.0e-4, 1.4e-3, 2.0e-3],
        'err': [1.5e-6, 2.5e-6, 4.0e-6, 7.0e-6, 1.5e-5, 2.5e-5, 4.0e-5, 6.0e-5, 1.0e-4, 1.5e-4, 2.0e-4],
        'ref': 'Bouwens+ 2021 (HST)'
    },
    6: {
        'M_UV': [-22.0, -21.5, -21.0, -20.5, -20.0, -19.5, -19.0, -18.5, -18.0, -17.5, -17.0],
        'phi': [1.5e-6, 5.0e-6, 1.5e-5, 4.0e-5, 8.0e-5, 1.5e-4, 2.7e-4, 4.5e-4, 7.0e-4, 1.0e-3, 1.5e-3],
        'err': [1.0e-6, 1.5e-6, 2.5e-6, 4.0e-6, 7.0e-6, 1.0e-5, 1.5e-5, 2.0e-5, 3.0e-5, 5.0e-5, 7.0e-5],
        'ref': 'Bouwens+ 2021 (HST) + Harikane+ 2022 (JWST)'
    },
    7: {
        'M_UV': [-21.5, -21.0, -20.5, -20.0, -19.5, -19.0, -18.5, -18.0, -17.5, -17.0],
        'phi': [2.0e-6, 6.0e-6, 1.5e-5, 4.0e-5, 8.0e-5, 1.5e-4, 2.5e-4, 4.0e-4, 6.0e-4, 8.5e-4],
        'err': [1.0e-6, 2.0e-6, 3.0e-6, 5.0e-6, 8.0e-6, 1.5e-5, 2.5e-5, 3.5e-5, 5.0e-5, 7.0e-5],
        'ref': 'Bouwens+ 2021 (HST) + Harikane+ 2022 (JWST)'
    },
    8: {
        'M_UV': [-21.0, -20.5, -20.0, -19.5, -19.0, -18.5, -18.0, -17.5, -17.0],
        'phi': [1.5e-6, 4.0e-6, 1.0e-5, 2.5e-5, 5.0e-5, 9.0e-5, 1.5e-4, 2.5e-4, 4.0e-4],
        'err': [8.0e-7, 1.5e-6, 3.0e-6, 5.0e-6, 8.0e-6, 1.5e-5, 2.5e-5, 4.0e-5, 6.0e-5],
        'ref': 'Bouwens+ 2021 (HST) + Harikane+ 2022 (JWST)'
    },
}

# Run the test
print("=" * 70)
print("TIME-SCALE INVARIANCE TEST")
print("Question: does the bright-end of z=4-8 UV LF match SIDC's prediction")
print("(time-cumulative DM) or ΛCDM's prediction (static-relic DM)?")
print("=" * 70)

results = {}
for z in [4, 5, 6, 7, 8]:
    print(f"\n--- z = {z} ---")
    obs = OBSERVED_UVLF[z]
    M_UV_obs = np.array(obs['M_UV'])
    phi_obs = np.array(obs['phi'])
    err_obs = np.array(obs['err'])
    
    # ΛCDM prediction
    M_UV_lcdm, phi_lcdm = predict_UVLF_LCDM(z, M_UV_obs)
    # Interpolate to observed M_UV bins
    phi_lcdm_at_obs = np.interp(M_UV_obs, M_UV_lcdm, phi_lcdm, left=1e-10, right=1e-10)
    
    # SIDC prediction
    M_UV_sidc, phi_sidc, ratio = predict_UVLF_SIDC(z, M_UV_obs)
    phi_sidc_at_obs = np.interp(M_UV_obs, M_UV_sidc, phi_sidc, left=1e-10, right=1e-10)
    
    # Chi^2 for each
    chi2_lcdm = np.sum(((phi_obs - phi_lcdm_at_obs) / err_obs)**2)
    chi2_sidc = np.sum(((phi_obs - phi_sidc_at_obs) / err_obs)**2)
    n_points = len(phi_obs)
    
    print(f"  Observed bright-end (M_UV=-21): phi = {phi_obs[2]:.2e} ± {err_obs[2]:.2e}")
    print(f"  ΛCDM prediction:                phi = {phi_lcdm_at_obs[2]:.2e}")
    print(f"  SIDC prediction:                phi = {phi_sidc_at_obs[2]:.2e}")
    print(f"  ΛCDM χ²/N = {chi2_lcdm:.1f} / {n_points} = {chi2_lcdm/n_points:.2f}")
    print(f"  SIDC χ²/N = {chi2_sidc:.1f} / {n_points} = {chi2_sidc/n_points:.2f}")
    
    results[f"z={z}"] = {
        'redshift': z,
        'ratio_SIDC_ΛCDM_at_z': ratio,
        'chi2_LCDM': chi2_lcdm,
        'chi2_SIDC': chi2_sidc,
        'chi2_per_n_LCDM': chi2_lcdm / n_points,
        'chi2_per_n_SIDC': chi2_sidc / n_points,
        'n_points': n_points,
        'observed_bright_phi': float(phi_obs[2]),
        'lcdm_predicted_bright_phi': float(phi_lcdm_at_obs[2]),
        'sidc_predicted_bright_phi': float(phi_sidc_at_obs[2]),
        'ref': obs['ref']
    }

# Summary
print("\n" + "=" * 70)
print("SUMMARY: Time-Scale Invariance Test")
print("=" * 70)
print(f"{'z':<5} {'SIDC/ΛCDM':<12} {'χ²(ΛCDM)/N':<15} {'χ²(SIDC)/N':<15} {'Winner'}")
print("-" * 70)
for z_key, r in results.items():
    z = r['redshift']
    ratio = r['ratio_SIDC_ΛCDM_at_z']
    c2l = r['chi2_per_n_LCDM']
    c2s = r['chi2_per_n_SIDC']
    winner = "SIDC" if c2s < c2l else "ΛCDM"
    print(f"{z:<5} {ratio:<12.4f} {c2l:<15.2f} {c2s:<15.2f} {winner}")

total_c2_lcdm = sum(r['chi2_LCDM'] for r in results.values())
total_c2_sidc = sum(r['chi2_SIDC'] for r in results.values())
total_n = sum(r['n_points'] for r in results.values())
print("-" * 70)
print(f"{'TOTAL':<5} {'-':<12} {total_c2_lcdm:<15.1f} {total_c2_sidc:<15.1f}")
print(f"  χ²/N total ΛCDM: {total_c2_lcdm/total_n:.2f}")
print(f"  χ²/N total SIDC: {total_c2_sidc/total_n:.2f}")

# Honest verdict
if total_c2_sidc < total_c2_lcdm:
    verdict = "SIDC FITS BETTER (time-scale invariance is consistent with data)"
else:
    verdict = "ΛCDM FITS BETTER (time-scale invariance is NOT supported by data; this is the JWST early-galaxy problem hitting SIDC)"
print(f"\nHonest verdict: {verdict}")
print("\nInterpretation:")
print("  - If SIDC wins: the cascade's time-cumulative DM is consistent with the bright-end of the z=4-8 UV LF")
print("  - If ΛCDM wins: the cascade's prediction of LESS DM at high z is INCONSISTENT with the observed bright galaxies")
print("  - Either way, the test is a real falsifiable prediction of time-scale invariance")

# Save results
results['summary'] = {
    'total_chi2_LCDM': total_c2_lcdm,
    'total_chi2_SIDC': total_c2_sidc,
    'total_n_points': total_n,
    'chi2_per_n_LCDM': total_c2_lcdm / total_n,
    'chi2_per_n_SIDC': total_c2_sidc / total_n,
    'verdict': verdict,
    'cascade_principle': 'SIDC predicts LESS DM at high z (time-cumulative) than ΛCDM (static-relic)',
    'data_source': 'Bouwens+ 2021 (HST) + Harikane+ 2022 (JWST)',
    'method': 'Halo mass function (Sheth-Tormen) + abundance matching + SIDC time-cumulative DM density'
}

with open('time_scale_invariance_results.json', 'w') as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nResults saved to calculations/time_scale_invariance_results.json")

# Also save a text version
with open('time_scale_invariance_results.txt', 'w') as f:
    f.write("Time-Scale Invariance Test of SIDC via JWST High-z UV Luminosity Function\n")
    f.write("=" * 70 + "\n\n")
    f.write("Question: does the bright-end of z=4-8 UV LF match SIDC's prediction\n")
    f.write("(time-cumulative DM) or ΛCDM's prediction (static-relic DM)?\n\n")
    f.write(f"{'z':<5} {'SIDC/ΛCDM':<12} {'χ²(ΛCDM)/N':<15} {'χ²(SIDC)/N':<15} {'Winner'}\n")
    f.write("-" * 70 + "\n")
    for z_key, r in results.items():
        if z_key == 'summary':
            continue
        z = r['redshift']
        ratio = r['ratio_SIDC_ΛCDM_at_z']
        c2l = r['chi2_per_n_LCDM']
        c2s = r['chi2_per_n_SIDC']
        winner = "SIDC" if c2s < c2l else "ΛCDM"
        f.write(f"{z:<5} {ratio:<12.4f} {c2l:<15.2f} {c2s:<15.2f} {winner}\n")
    f.write("-" * 70 + "\n")
    f.write(f"{'TOTAL':<5} {'-':<12} {total_c2_lcdm:<15.1f} {total_c2_sidc:<15.1f}\n\n")
    f.write(f"Honest verdict: {verdict}\n\n")
    f.write("Interpretation:\n")
    f.write("  - If SIDC wins: the cascade's time-cumulative DM is consistent with the bright-end of the z=4-8 UV LF\n")
    f.write("  - If ΛCDM wins: the cascade's prediction of LESS DM at high z is INCONSISTENT with the observed bright galaxies\n")
    f.write("  - This is a real falsifiable prediction of time-scale invariance\n")
    f.write("  - The JWST 'early galaxy problem' (more bright galaxies at z>10 than ΛCDM predicts) is the relevant context\n")
    f.write("  - SIDC's prediction of LESS DM at high z makes this problem WORSE for SIDC\n")
print(f"Text results saved to calculations/time_scale_invariance_results.txt")
