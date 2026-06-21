#!/usr/bin/env python3
"""
Early-universe 2D universe creation: Does the existing scaling law close the CMB gap?

The framework's universal scaling law:
    tau_2D = t_Pl,3 * (E / E_Pl,3)^alpha  with alpha = 1.289

The framework's smooth creation function (v2.7.5+):
    C(E) = E^(1+alpha)

These apply to ALL energetic events, including early-universe ones.
Question: Do early-universe events naturally produce the observed 27% DM at z=1100?

User insight (June 21, 2026): "hot plasma during universe creation also produces 2D universes"
"""

import numpy as np

# Constants (SI units)
c = 2.998e8                  # m/s
h_planck = 1.055e-34         # J*s
k_B = 1.381e-23              # J/K
G_N = 6.674e-11              # m^3/kg/s^2

# Cosmological parameters (Planck 2018)
H_0 = 2.184e-18              # /s  (67.4 km/s/Mpc)
Omega_b = 0.0493
Omega_c = 0.265              # CDM (this is what we want to match)
Omega_m = Omega_b + Omega_c  # 0.3143
Omega_Lambda = 0.6857
Omega_r = 9.16e-5            # photons + neutrinos
rho_crit = 8.6e-27           # kg/m^3  (today)

# CMB epoch
z_CMB = 1100
t_CMB = 380_000 * 365.25 * 24 * 3600  # 380 kyr in seconds ~ 1.2e13 s
T_CMB = 2.725                 # K

# 3+1D Planck units
M_Pl_3D_GeV = 1.22e19        # GeV
M_Pl_3D_J = M_Pl_3D_GeV * 1.602e-10  # J = 1.954e9 J
E_Pl_3D = M_Pl_3D_J
t_Pl_3D = 5.391e-44          # s
l_Pl_3D = 1.616e-35          # m

# Framework's alpha (L308n)
alpha = 1.0 + 1.0/np.sqrt(12)  # = 1.2887

print("=" * 70)
print("FRAMEWORK CONSTANTS")
print("=" * 70)
print(f"alpha = 1 + 1/sqrt(12) = {alpha:.10f}")
print(f"M_Pl,3D = {M_Pl_3D_GeV:.3e} GeV = {E_Pl_3D:.3e} J")
print(f"t_Pl,3D = {t_Pl_3D:.3e} s")
print()
print(f"Planck 2018: Omega_b = {Omega_b}, Omega_c = {Omega_c}, Omega_L = {Omega_Lambda}")
print(f"z_CMB = {z_CMB}, t_CMB = {t_CMB:.3e} s, T_CMB = {T_CMB} K")

# ----------------------------------------------------------------------
# Function: 2D universe lifetime in our frame
# ----------------------------------------------------------------------
def tau_2D(E_J):
    """2D universe lifetime in our (3+1D) frame, given event energy E in J."""
    return t_Pl_3D * (E_J / E_Pl_3D)**alpha

def E_for_tau(tau_s):
    """Event energy needed to give a 2D universe lifetime tau in our frame."""
    return E_Pl_3D * (tau_s / t_Pl_3D)**(1.0/alpha)

# ----------------------------------------------------------------------
# 1. What E gives tau = t_CMB (dies at CMB)?
# ----------------------------------------------------------------------
print()
print("=" * 70)
print("1. REQUIRED ENERGY FOR tau_2D = t_CMB")
print("=" * 70)
E_die_at_CMB = E_for_tau(t_CMB)
print(f"For a 2D universe dying exactly at CMB (z=1100):")
print(f"  E_required = {E_die_at_CMB:.3e} J")
print(f"  Compare to:")
print(f"    SN kinetic energy      ~ 1e44 J  (too small)")
print(f"    Hypernova              ~ 1e46 J  (still too small)")
print(f"    BNS merger             ~ 1e53 J  (PERFECT MATCH!)")
print(f"    AGN outburst           ~ 1e55 J  (too big)")
print()

# ----------------------------------------------------------------------
# 2. Hubble parameters at different redshifts
# ----------------------------------------------------------------------
def H_z(z):
    """Hubble parameter at redshift z."""
    return H_0 * np.sqrt(Omega_r * (1+z)**4 + Omega_m * (1+z)**3 + Omega_Lambda)

def t_H(z):
    """Hubble time at redshift z (in seconds)."""
    return 1.0 / H_z(z)

def R_H(z):
    """Hubble radius at redshift z (in meters)."""
    return c * t_H(z)

def V_H(z):
    """Hubble volume at redshift z (in m^3)."""
    return (4.0 * np.pi / 3.0) * R_H(z)**3

def T_rad(z):
    """Radiation temperature at redshift z (in K)."""
    return T_CMB * (1+z)

def rho_rad(z):
    """Radiation energy density at redshift z (in J/m^3)."""
    # a*T^4 with a = 7.566e-16 J/m^3/K^4, factor of ~1.68 for relativistic particles
    a_rad = 7.566e-16
    return 1.68 * a_rad * T_rad(z)**4

# ----------------------------------------------------------------------
# 3. Hubble-volume-as-event at different redshifts
# ----------------------------------------------------------------------
print("=" * 70)
print("2. HUBBLE VOLUME AS 'EVENT' AT DIFFERENT REDSHIFTS")
print("=" * 70)
print(f"{'epoch':<20} {'z':>10} {'T [K]':>10} {'R_H [m]':>10} {'E_Hubble [J]':>15} {'tau_2D [s]':>15} {'dies before z=1100?':>20}")
print("-" * 110)

epochs = [
    ("Inflation end",    1e26, 1e28),
    ("Reheating",        1e15, 1e10),
    ("EW phase trans",   1e15, 1e2),
    ("QCD phase trans",  1e12, 2e8),
    ("BBN",              1e10, 1e6),
    ("Matter-radiation", 3400, 9400),
    ("Recombination",    1100, 3000),
    ("Reionization",     10,   30),
    ("Today",            0,    2.725),
]

for name, z, T in epochs:
    R = R_H(z)
    V = V_H(z)
    rho = rho_rad(z)
    E_H = rho * V
    tau = tau_2D(E_H)
    dies = "YES" if tau < t_CMB else "no (tau > t_CMB)"
    print(f"{name:<20} {z:>10.2e} {T:>10.2e} {R:>10.2e} {E_H:>15.3e} {tau:>15.3e} {dies:>20}")

# ----------------------------------------------------------------------
# 4. Energy per Hubble volume: when does it equal 1e53 J?
# ----------------------------------------------------------------------
print()
print("=" * 70)
print("3. WHEN DOES E_Hubble = 1e53 J (the value that gives tau = t_CMB)?")
print("=" * 70)
# In rad-dom era: rho ~ (1+z)^4, V_H ~ (1+z)^-6, so E_H ~ (1+z)^-2
# E_H(z=1e12) ~ 1e47 J, so E_H = 1e53 requires (1+z)^2 = 1e47/1e53 * (1e12)^2 = 1e18, 1+z = 1e9
z_target_E = 1e9
print(f"Target E_Hubble = 1e53 J occurs at z ~ {z_target_E:.2e}")
print(f"  This is BBN-era (T ~ {T_rad(z_target_E):.2e} K ~ {T_rad(z_target_E)/1.16e4:.2e} eV)")
print(f"  Hubble time: {t_H(z_target_E):.3e} s")
print(f"  Hubble radius: {R_H(z_target_E):.3e} m")
print(f"  Hubble volume: {V_H(z_target_E):.3e} m^3")
print(f"  E_Hubble: {rho_rad(z_target_E) * V_H(z_target_E):.3e} J")
print(f"  tau_2D: {tau_2D(rho_rad(z_target_E) * V_H(z_target_E)):.3e} s")
print(f"  Dies at cosmic time t_CMB = {t_CMB:.3e} s? {'YES' if abs(tau_2D(rho_rad(z_target_E)*V_H(z_target_E))-t_CMB)/t_CMB < 0.5 else 'NO'}")
print()

# ----------------------------------------------------------------------
# 5. Number of Hubble volumes in comoving V that becomes observable today
# ----------------------------------------------------------------------
print("=" * 70)
print("4. NUMBER OF HUBBLE VOLUMES IN COMOVING V THAT BECOMES OUR OBSERVABLE UNIVERSE")
print("=" * 70)
# Comoving V = Hubble V at z=1100 (roughly)
V_comoving = V_H(z_CMB)
print(f"Comoving volume (= Hubble V at z=1100): {V_comoving:.3e} m^3")
print()

for name, z, T in epochs:
    V_physical_at_z = V_comoving * ((1+z_CMB) / (1+z))**3
    V_H_at_z = V_H(z)
    N_events = V_physical_at_z / V_H_at_z
    print(f"At {name:<20} (z={z:.2e}): {N_events:.3e} Hubble volumes in comoving V")

# ----------------------------------------------------------------------
# 6. Total DM from "Hubble volume as event" treatment
# ----------------------------------------------------------------------
print()
print("=" * 70)
print("5. TOTAL DM IF 'EVENT = HUBBLE VOLUME' AT EACH EPOCH")
print("=" * 70)
print("(This assumes each Hubble volume is one discrete event that creates one 2D universe)")
print()

total_mass_DM = 0.0
print(f"{'epoch':<20} {'z':>10} {'E_H [J]':>15} {'tau_2D [s]':>15} {'N_events':>15} {'m per event [kg]':>20} {'M_DM [kg]':>15} {'contributes at z=1100?':>25}")
print("-" * 145)

for name, z, T in epochs:
    E_H = rho_rad(z) * V_H(z)
    tau = tau_2D(E_H)
    V_physical_at_z = V_comoving * ((1+z_CMB) / (1+z))**3
    N_events = V_physical_at_z / V_H(z)
    m_per_event = E_H / c**2

    # Did it die before z=1100?
    died = tau < t_CMB
    contributes = "YES (already dead)" if died else "no (still alive)"

    M_DM = N_events * m_per_event if died else 0
    total_mass_DM += M_DM

    print(f"{name:<20} {z:>10.2e} {E_H:>15.3e} {tau:>15.3e} {N_events:>15.3e} {m_per_event:>20.3e} {M_DM:>15.3e} {contributes:>25}")

# Required DM at z=1100 in our observable universe
M_DM_required = Omega_c * rho_crit * V_comoving
print()
print(f"Total DM mass from this treatment: {total_mass_DM:.3e} kg")
print(f"Required DM at z=1100:           {M_DM_required:.3e} kg")
print(f"Ratio (overproduction):           {total_mass_DM/M_DM_required:.3e}")

# ----------------------------------------------------------------------
# 7. Smooth creation function C(E) = E^(1+alpha)
# ----------------------------------------------------------------------
print()
print("=" * 70)
print("6. SMOOTH CREATION FUNCTION C(E) = E^(1+alpha)")
print("=" * 70)
print("Contribution from a single event of energy E:")
print(f"  C(E) = E^(1+alpha) = E^{1+alpha:.4f}")
print()
print("For each Hubble-volume-as-event:")
for name, z, T in epochs[:5]:
    E_H = rho_rad(z) * V_H(z)
    C = E_H ** (1 + alpha)
    print(f"  {name:<20}: C(E_H) = {C:.3e} J^{1+alpha:.2f}")

# ----------------------------------------------------------------------
# 8. CONCLUSION
# ----------------------------------------------------------------------
print()
print("=" * 70)
print("7. CONCLUSION")
print("=" * 70)
print()
print("HONEST FINDING: The smooth creation function C(E) = E^(1+alpha) applied")
print("to early-universe Hubble volumes OVERPRODUCES DM by ~30-35 orders of magnitude.")
print()
print("Why? In standard cosmology, the early universe is a CONTINUOUS thermodynamic")
print("process, not a collection of discrete events. The QCD phase transition is a")
print("crossover, not a first-order transition. There are no discrete bubbles to count.")
print()
print("To close the CMB gap, we need one of:")
print("  (a) BSM physics: first-order QCD/EW phase transitions (discrete bubbles)")
print("  (b) Discrete early-universe events: cosmic strings, PBHs, topological defects")
print("  (c) Framework modification: continuous-process formalism for C(E)")
print("  (d) Normalization: only a fraction of early-universe energy goes to DM")
print()
print("The scaling law ITSELF is universal and applies to early universe, but the")
print("APPLICATION to standard cosmology is non-trivial.")
print()
print(f"RECOMMENDATION: Open new section §4.x 'Early-universe 2D universe creation'")
print(f"and new limitation L308ab marking CMB gap as PARTIAL closure if any of (a)-(d) works.")
