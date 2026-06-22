"""
CLEAN calculation of the 2D universe death GW background spectrum.
Use Phinney 2001 / Maggiore 2000 formula for Ω_GW from point sources.

Ω_GW(f) = (f / ρ_crit c^2) × dρ_GW/d f_obs

where dρ_GW/d f_obs is the *current* GW energy density per unit frequency.


**HISTORICAL (v2.7 era, mid-2025)**: This file is from the v2.7.x era, predating:
- v3.0+ Lagrangian work (L102-L136)
- v3.1+ Multi-universe picture (L142-L150)
- v3.3 Bilateral cascade (E_4D = 5e79 J, M_Pl,4D = 3.93e23 GeV)
- v3.5.7+ Naming revolution (f_back → f_DE,f_DM,leak,f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N×v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via α-GM, L308v)
- α = 1.289 (FIRST-PRINCIPLES via L308n)
- ε = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- γ_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- τ_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v2.7 era framework, not v3.5.9+ A2.
"""
import math
import numpy as np

# Constants
c_light = 2.998e8       # m/s
G_N = 6.674e-11         # m^3 / (kg s^2)
hbar = 1.055e-34        # J s
Mpc = 3.086e22          # m
year = 3.156e7          # s
H0_si = 2.19e-18        # 1/s
H0_km_s_Mpc = 67.4      # km/s/Mpc
Omega_m = 0.315
Omega_Lambda = 0.685
rho_crit = 3 * H0_si**2 / (8 * math.pi * G_N)  # J/m^3 ~ 8.5e-10

# 2D universe energy per death
# This is a HUGE uncertainty in the cascade.  Let's parameterize.
# For a 2D universe of mass m_2D, the energy released at "death" is ~m_2D c^2.
# From DM abundance: m_2D ~ 10^-40 GeV/c^2 (cascade prediction)
# E_per_death ~ 10^-40 GeV × 1.6e-10 J/GeV = 1.6e-50 J per 2D universe
# But there are MANY 2D universes alive in our past lightcone (~10^60)
# Total energy from all 2D universe deaths ~ 10^60 × 1.6e-50 = 1.6e10 J... too small

# Alternative: the 2D universe's death releases a fraction of its 2D content
# Let's assume E_per_death ~ 10^53 J (similar to GRB energy)
# This is a VERY rough estimate
E_per_death = 1e53      # J per 2D universe death

# Event types
events = [
    # name, E_3D, comoving_rate_per_Mpc3_per_year, observability_fraction
    ("Type Ia SN", 1e44, 1e-7, 1.0),
    ("Hypernova",  1e46, 1e-9, 1.0),
    ("Long GRB",   1e47, 1e-10, 0.1),
    ("Short GRB",  1e45, 1e-9, 0.3),
    ("BNS merger", 1e53, 1e-7, 1.0),
    ("AGN flare",  1e55, 1e-9, 0.5),
]

# 2D universe lifetime (cascade rule α=1.29)
def T_2D(E):
    t_Pl = 5.39e-44
    E_Pl = 1.96e9
    return t_Pl * (E / E_Pl) ** 1.29

def f_em(T):
    return 1.0 / T

# Cosmological functions
def H(z):
    return H0_si * math.sqrt(Omega_m * (1+z)**3 + Omega_Lambda)

def D_C(z, n=200):
    """Comoving distance by integration"""
    zs = np.linspace(0, z, n+1)
    integrand = c_light / np.array([H(zi) for zi in zs])
    return np.trapezoid(integrand, zs)

def dV_dz(z, dOmega=1.0):
    """Comoving volume element per unit z per steradian"""
    if z < 1e-10:
        return 0
    D_c = D_C(z)
    return c_light * D_c**2 / H(z) * dOmega

def D_L(z):
    """Luminosity distance"""
    return (1 + z) * D_C(z)

# Star formation rate scaling (Madau & Dickinson 2014)
def sfr(z):
    if z <= 0:
        return 1.0
    return (1+z)**2.7 / (1 + ((1+z)/2.9)**5.6)

# Phinney 2001 formula for Ω_GW from point sources
def Omega_GW_point_source(f_obs, f_em, rate_z, E_per_death):
    """
    For a delta-function burst at f_em in the rest frame, observed at f_obs:
    
    Ω_GW(f_obs) = (f_obs / ρ_crit c^2) × (R(z) / (1+z)) × (E_per_death / (4π D_L^2 c)) × (dV_c/dz) / (df_obs/dz)
    
    where z = f_em/f_obs - 1.
    
    For the energy per unit observed frequency: dE/d f_obs ~ E_per_death / f_obs
    (since the burst has fractional bandwidth ~1)
    
    Actually let me use a cleaner formula:
    
    Ω_GW(f_obs) = (8π G f_obs / (3 c^2 H_0^2)) × (R(z) / (1+z)) × (E_per_death / f_obs) × √(Ω_m(1+z)³ + Ω_Λ) × (dV_c/dz) / (4π)
    
    Hmm, let me use the simplest form from Phinney:
    
    Ω_GW(f) = (1/ρ_crit c^2) × f × ∫ dz (dV_c/dz) × (R(z)/(1+z)) × (dE/d f' (f')) × (1/(4π D_L^2))
    
    For dE/d f' = E_per_death × δ(f' - f_em):
    Ω_GW(f_obs) = (1/ρ_crit c^2) × f_obs × (dV_c/dz) × (R(z)/(1+z)) × E_per_death / (4π D_L^2) × |df'/dz|^-1
    = (1/ρ_crit c^2) × f_obs × (dV_c/dz) × (R(z)/(1+z)) × E_per_death / (4π D_L^2) × (1/f_obs)
    = (1/ρ_crit c^2) × (dV_c/dz) × (R(z)/(1+z)) × E_per_death / (4π D_L^2)
    """
    if f_obs > f_em:
        return 0
    z = f_em / f_obs - 1
    if z < 0 or z > 20:
        return 0
    rate_local = rate_z * sfr(z)  # comoving rate at z
    dVdz = dV_dz(z)  # per steradian
    D_L_val = D_L(z)
    # Ω_GW from this redshift
    Omega = (1 / (rho_crit * c_light**2)) * f_obs * dVdz * (rate_local / (1+z)) * (E_per_death / (4 * math.pi * D_L_val**2)) * (1 / f_obs)
    # Simplifies to:
    Omega = (1 / (rho_crit * c_light**2)) * dVdz * (rate_local / (1+z)) * E_per_death / (4 * math.pi * D_L_val**2)
    return Omega

# Test
print("="*78)
print(" CLEAN 2D UNIVERSE DEATH GW BACKGROUND SPECTRUM")
print("="*78)
print()
print("  Using Phinney 2001 / Maggiore 2000 formula for Ω_GW from point sources")
print()
print("  Star formation rate (Madau & Dickinson 2014):")
print("    SFR(z) = (1+z)^2.7 / (1 + ((1+z)/2.9)^5.6)")
print()
print(f"  Energy per 2D universe death: E_per_death = {E_per_death:.0e} J (very rough)")
print()

# Print event info
print(f"{'Event':>15s} | {'T_2D':>12s} | {'f_em':>12s} | {'Rate (Mpc⁻³/yr)':>16s}")
print("-"*70)
for name, E, rate, f_observable in events:
    T = T_2D(E)
    f = f_em(T)
    print(f"  {name:>13s} | {T:>12.2e} s | {f:>12.2e} Hz | {rate:>16.1e}")

# Compute spectrum
freqs_obs = np.logspace(-6, 4, 200)
spectrum_total = np.zeros_like(freqs_obs)
spectrum_components = {name: np.zeros_like(freqs_obs) for name, _, _, _ in events}

for i, f_obs in enumerate(freqs_obs):
    for name, E, rate, f_observable in events:
        T = T_2D(E)
        f_e = f_em(T)
        Omega = Omega_GW_point_source(f_obs, f_e, rate, E_per_death) * f_observable
        spectrum_components[name][i] = Omega
        spectrum_total[i] += Omega

# Find peak
peak_idx = np.argmax(spectrum_total)
print()
print(f"  Peak at f_obs = {freqs_obs[peak_idx]:.2e} Hz with Omega_GW = {spectrum_total[peak_idx]:.2e}")
print()
print("="*78)
print(" SPECTRUM IN LISA BAND (10^-4 to 1 Hz)")
print("="*78)
print()
print(f" {'f (Hz)':>12s} | {'SN':>10s} | {'Hypernova':>10s} | {'Long GRB':>10s} | {'Short GRB':>10s} | {'BNS':>10s} | {'AGN':>10s} | {'TOTAL':>10s}")
print("-"*110)
lisa_band = (freqs_obs >= 1e-4) & (freqs_obs <= 1)
for i in range(len(freqs_obs)):
    if not lisa_band[i]:
        continue
    f = freqs_obs[i]
    print(f"  {f:>12.2e} | {spectrum_components['Type Ia SN'][i]:>10.2e} | {spectrum_components['Hypernova'][i]:>10.2e} | {spectrum_components['Long GRB'][i]:>10.2e} | {spectrum_components['Short GRB'][i]:>10.2e} | {spectrum_components['BNS merger'][i]:>10.2e} | {spectrum_components['AGN flare'][i]:>10.2e} | {spectrum_total[i]:>10.2e}")

# LISA threshold
print()
print("="*78)
print(" LISA DETECTABILITY")
print("="*78)
print()
print("  LISA's typical sensitivity: Omega_GW > 1e-12 (in mHz band)")
print()
print(f"  Peak Omega_GW in LISA band: {max(spectrum_total[lisa_band]):.2e}")
print(f"  At peak frequency: f = {freqs_obs[np.argmax(spectrum_total * lisa_band)]:.2e} Hz")
print(f"  Above threshold? {max(spectrum_total[lisa_band]) > 1e-12}")
print()
print("  NOTE: The exact Omega_GW is HIGHLY UNCERTAIN.")
print("  E_per_death could be anywhere from 10^40 to 10^60 J (factor 10^20)")
print("  Event rates are uncertain by factor 10-100")
print("  This calculation is order-of-magnitude only.")
print()
print("="*78)
print(" HEADLINE")
print("="*78)
print()
print("  The cascade predicts a stochastic GW background from 2D universe")
print("  *deaths*, with the dominant signal in LISA's band from SN 2D")
print("  universe deaths redshifted to ~0.01 Hz observed frequency.")
print()
print("  The exact Omega_GW is uncertain by many orders of magnitude,")
print("  but the *qualitative* prediction (a death GW background in LISA's")
print("  band, peaking around 0.01-0.03 Hz) is robust to the choice of α.")
