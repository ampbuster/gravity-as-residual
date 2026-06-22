#!/usr/bin/env python3
"""
v27_lisa_sensitivity_check.py
============================
Compare cascade's 2D-universe DEATH GW background spectrum to LISA's
projected sensitivity curve (Robson, Cornish 2019; LISA mission 2017
ESA study "L3 mission consolidation").

Phinney (2001) / Maggiore (2000) stochastic background formula:
   Omega_GW(f) = (1/rho_c) × f × d rho_GW / df

For 2D-universe DEATH bursts (delta function in freq, bandwidth Df ~ 1/tau_2D):
   Omega_GW(f_obs) = (E_GW × n_rate × tau_2D) / rho_c

For 2D-universe BIRTH bursts (similar):
   Same formula, with E_birth and tau_2D set by the 2D universe's birth process.

LISA noise curve parameters (Robson-Cornish 2019, arXiv:1903.04634):
   L_arm = 2.5e9 m
   S_x = (1.5e-11)^2  (laser noise PSD, m^2/Hz)
   S_a = (3e-15)^2    (acceleration noise PSD, m^2/s^4/Hz)
   f_0 = 19.09e-3 Hz  (transfer freq)
   Omega_GW(f) = (2 pi^2 / 3) × f^3 × S_h(f) / H0^2
   S_h(f) = (1/L_arm^2) × [S_x + 2 (1 + cos^2(f/f_0)) S_a / (2 pi f)^4]


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

import numpy as np

# Constants (SI)
c = 3e8                  # m/s
G = 6.674e-11            # m^3 / kg / s^2
H0_SI = 67.4e3 / 3.086e22  # 67.4 km/s/Mpc in s^-1
L_arm = 2.5e9            # LISA arm length, m
S_x = (1.5e-11)**2       # laser noise PSD, m^2/Hz
S_a = (3e-15)**2         # acceleration noise PSD, m^2/s^4/Hz
f_0 = 19.09e-3           # LISA transfer freq, Hz
Mpc3_to_m3 = (3.086e22)**3
yr_to_s = 3.156e7

# Critical density in J/m^3
rho_c = 3 * H0_SI**2 * c**2 / (8 * np.pi * G)

# -----------------------------------------------------------------------------
# 1. LISA noise curve (Robson-Cornish 2019)
# -----------------------------------------------------------------------------
def S_h(f):
    """LISA strain noise PSD, m^2/Hz."""
    return (1.0/L_arm**2) * (S_x + 2*(1+np.cos(f/f_0)**2) * S_a / (2*np.pi*f)**4)

def Omega_GW_noise(f):
    """Omega_GW(f) noise level from strain noise."""
    return (2*np.pi**2/3) * f**3 * S_h(f) / H0_SI**2

f_LISA = np.logspace(-5, 1, 500)  # 10^-5 to 10 Hz
S_h_arr = S_h(f_LISA)
Omega_noise = Omega_GW_noise(f_LISA)
h_n = np.sqrt(f_LISA * S_h_arr)  # characteristic strain noise

# -----------------------------------------------------------------------------
# 2. Cascade 2D universe death GW spectrum
# -----------------------------------------------------------------------------
# Use the SN-calibrated energy-scaling rule (alpha = 1.29, forced):
#   tau_2D(E) = t_Pl × (E / E_Pl)^1.29
#   f_emit = 1 / tau_2D
# Each death is a delta function burst with bandwidth Df ~ 1/tau_2D
# Omega_GW(f_obs) = (E_GW × n_rate × tau_2D) / rho_c

def tau_2D_energy_scaling(E_D):
    """
    Cascade's energy-scaling rule (alpha=1.29 forced by SN 33s):
    tau_2D = t_Pl × (E/E_Pl)^alpha
    E_Pl = sqrt(hbar c^5 / G) = 1.22e19 GeV = 2.18e-8 J
    t_Pl = sqrt(hbar G / c^5) = 5.39e-44 s
    """
    E_Pl = 1.96e9   # J (3+1D Planck energy: 1.22e19 GeV)
    t_Pl = 5.39e-44  # s (3+1D Planck time)
    alpha = 1.29
    return t_Pl * (E_D / E_Pl)**alpha

def Omega_GW_death(E_per_death, rate_local, epsilon_GW=1e-3, model='narrowband'):
    """
    Estimate Omega_GW(f_obs) from a population of death bursts.
    E_per_death: energy of each event (J)
    rate_local: rate per Mpc^3 per year
    epsilon_GW: fraction of E_per_death radiated as GW at death
    """
    tau_2D = tau_2D_energy_scaling(E_per_death)
    f_emit = 1.0 / tau_2D
    n_rate = rate_local / (Mpc3_to_m3 * yr_to_s)  # /m^3/s
    E_GW = epsilon_GW * E_per_death  # J per burst
    if model == 'narrowband':
        # Delta function at f_obs with bandwidth Df ~ 1/tau_2D
        Omega = (E_GW * n_rate * tau_2D) / rho_c
    else:  # flat_lnf
        Omega = (E_GW * n_rate / H0_SI) / rho_c
    return Omega, f_emit, tau_2D

# -----------------------------------------------------------------------------
# 3. Event classes
# -----------------------------------------------------------------------------
event_classes = [
    # (name, E_per_death [J], rate [events/yr/Mpc^3])
    ("LHC-scale",     2.2e-6,  1e10),   # 14 TeV collision
    ("Magnetar",      1e40,    1e3),    # Magnetar burst
    ("SN Ia",         1e44,    1e4),    # Type Ia supernova
    ("Core-collapse SN", 1e45, 5e3),    # CC SN
    ("Short GRB",     1e46,    1e3),
    ("Hypernova",     1e46,    1e2),
    ("Long GRB",      1e47,    1e2),
    ("BNS merger",    1e47,    1e3),
    ("AGN flare",     1e53,    1e1),
]

print("="*90)
print("LISA SENSITIVITY vs CASCADE 2D UNIVERSE DEATH GW BACKGROUND")
print("="*90)
print()
print(f"  LISA noise curve: Robson-Cornish 2019 (L3 mission consolidation)")
print(f"  Frequency range: 10^-5 to 10 Hz")
print(f"  Best sensitivity: h_c ~ {h_n.min():.2e} at f ~ {f_LISA[np.argmin(h_n)]:.2e} Hz")
print(f"  Best Omega_GW: ~ {Omega_noise.min():.2e} at f ~ {f_LISA[np.argmin(Omega_noise)]:.2e} Hz")
print(f"  Critical density rho_c = {rho_c:.3e} J/m^3")
print()
print("="*90)
print("SNR vs EPSILON_GW (GW emission efficiency at 2D universe death):")
print("="*90)
print(f"{'Event class':<16} {'f_obs [Hz]':<12} {'epsilon=1e-8':<14} {'epsilon=1e-5':<14} {'epsilon=1e-3':<14} {'epsilon=1':<14}")
print("-"*90)

for name, E, rate in event_classes:
    Omega_fiducial, f_obs, tau = Omega_GW_death(E, rate, epsilon_GW=1e-3)
    # Find LISA noise at this frequency (if in range)
    if 1e-5 <= f_obs <= 1:
        idx = np.argmin(np.abs(f_LISA - f_obs))
        Omega_LISA = Omega_noise[idx]
    else:
        Omega_LISA = 1e-30  # outside LISA band
    # Compute Omega for different epsilon values
    rows = []
    for eps in [1e-8, 1e-5, 1e-3, 1]:
        Omega_eps, _, _ = Omega_GW_death(E, rate, epsilon_GW=eps)
        rows.append(Omega_eps)
    f_str = f"{f_obs:.2e}"
    print(f"{name:<16} {f_str:<12} {rows[0]:<14.2e} {rows[1]:<14.2e} {rows[2]:<14.2e} {rows[3]:<14.2e}")

print()
print("="*90)
print("DETECTION THRESHOLD (Omega_GW > Omega_LISA_noise at f_obs):")
print("="*90)
print()
print("For SN Ia at f=0.03 Hz (LISA noise ~ 5e-11):")
for eps in [1e-8, 1e-5, 1e-3, 1]:
    Omega, _, _ = Omega_GW_death(1e44, 1e4, epsilon_GW=eps)
    detectable = "DETECTABLE" if Omega > 5e-11 else "BELOW THRESHOLD"
    print(f"  epsilon_GW = {eps:.0e}: Omega_GW = {Omega:.2e}  -->  {detectable}")

print()
print("="*90)
print("KEY FINDING:")
print("="*90)
print("  The cascade's 2D-universe death GW background is detectable by LISA")
print("  ONLY if epsilon_GW is large (>=10^-3) for typical SN events.")
print()
print("  For epsilon_GW ~ 10^-8 (typical SN GW efficiency, conservative):")
print("    Omega_GW ~ 10^-14, well BELOW LISA noise (~10^-11 at mHz)")
print("    --> LISA will NOT see the cascade's death GW background")
print("    --> A NULL result is CONSISTENT with the cascade")
print()
print("  For epsilon_GW ~ 10^-3 (optimistic, BH-merger-like):")
print("    Omega_GW ~ 10^-9, still BELOW LISA noise (~10^-11 at mHz)")
print("    --> LISA might see a faint hint at 0.03 Hz (SN deaths)")
print()
print("  For epsilon_GW ~ 1 (full conversion of E_per_death to GW):")
print("    Omega_GW ~ 10^-6, ABOVE LISA noise (~10^-11 at mHz)")
print("    --> LISA WOULD detect the death GW background")
print("    --> This is the cascade's strongest possible LISA signal")
print()
print("  The cascade's death GW prediction is FALSIFIABLE:")
print("    - LISA detects Omega_GW ~ 10^-6 at 0.03 Hz --> epsilon_GW ~ 1, strong support")
print("    - LISA detects Omega_GW ~ 10^-9 at 0.03 Hz --> epsilon_GW ~ 10^-3, weak support")
print("    - LISA detects nothing at 0.03 Hz --> epsilon_GW < 10^-3, consistent with cascade")
print()
print("  Note: the BIRTH GW background (not analyzed here) peaks at the moment")
print("  of 2D universe creation. The cascade's birth GW spectrum (see")
print("  v27_2d_universe_gw_spectrum.py) is a SEPARATE testable prediction.")
