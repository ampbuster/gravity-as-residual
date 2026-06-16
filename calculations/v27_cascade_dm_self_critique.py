"""
v27_cascade_dm_self_critique.py
================================

Honest re-examination of §3.13: DM as decaying sterile neutrino.

User correction: "does the neutrino decay make sense? are there areas with DM and no neutrinos?"

Issues identified:
1. Pauli blocking mechanism doesn't work for typical DM masses
   - Fermi momentum in DM halos: p_F ~ 10^-22 GeV (way too small)
   - Decay product energy: E_γ = E_ν = m_s/2 ~ 0.5 GeV
   - Ratio: 10^21 (decay products WAY above Fermi sea)
   - Pauli blocking is INEFFECTIVE

2. Active neutrino flux prediction is too high
   - If all DM is sterile neutrino (m_s = 1 GeV) and decays
   - n_ν ~ 1.4e-6 /cm³
   - Flux at Earth: ~3e3 cm^-2 s^-1 sr^-1
   - Current Super-K limit at 500 MeV: ~10^-4 cm^-2 s^-1 sr^-1
   - TENSION: cascade overpredicts by factor 10^7

3. Sterile neutrino with m_s ~ 1 GeV is not viable
   - For Γ ~ 2.3e-18 /s, need sin²(2θ) ~ 10^-4 (large mixing)
   - Inconsistent with current bounds

The cascade's "DM = sterile neutrino with Pauli-blocked decay" hypothesis has issues.
"""

import math
import json

# Re-derive all the issues

# === Issue 1: Pauli blocking doesn't work ===
print("=== Issue 1: Pauli blocking is INEFFECTIVE ===\n")
rho_halo = 0.3  # GeV/cm³ (typical DM halo)
m_s = 1.0  # GeV (sterile neutrino mass)
n_DM = rho_halo / m_s  # per cm³
print(f"DM number density in halo: {n_DM:.2e} /cm³")

# Fermi momentum
hbar = 1.055e-34  # J s
n_SI = n_DM * 1e6  # m^-3
p_F = (3 * math.pi**2 * n_SI)**(1/3) * hbar  # J s/m
p_F_eV = p_F * 1e9 / 1.602e-19 / 3e8  # eV
print(f"Fermi momentum p_F: {p_F_eV:.2e} eV = {p_F_eV*1e-9:.2e} GeV")
print(f"Decay product energy (m_s/2 = 0.5 GeV): {m_s/2} GeV = {m_s/2*1e9} eV")
print(f"Ratio E_decay/p_F: {(m_s/2*1e9)/p_F_eV:.2e}")
print()
print("VERDICT: Decay product energy is 10^21 times larger than Fermi momentum.")
print("  Pauli blocking is completely INEFFECTIVE for typical DM masses.")
print("  The §3.13 'more clustered = slower decay via Pauli blocking' is WRONG.")
print()

# === Issue 2: Neutrino flux too high ===
print("=== Issue 2: Active neutrino flux prediction ===\n")
rho_crit = 9.2e-27  # kg/m³
Omega_DM = 0.27
rho_DM = Omega_DM * rho_crit  # kg/m³
m_s_kg = m_s * 1.783e-27  # kg (1 GeV)

n_nu = rho_DM / m_s_kg  # per m³
n_nu_cm3 = n_nu * 1e-6  # per cm³
print(f"DM density: {rho_DM:.2e} kg/m³")
print(f"Number density of active ν (if all DM decayed): {n_nu_cm3:.2e} /cm³")
print()

flux = n_nu_cm3 * 3e10 / (4 * math.pi)  # cm^-2 s^-1 sr^-1
print(f"Active ν flux at Earth: {flux:.2e} cm^-2 s^-1 sr^-1")
print(f"Super-K limit at ~500 MeV: ~10^-4 cm^-2 s^-1 sr^-1")
print(f"TENSION: cascade overpredicts by {flux/1e-4:.2e}x")
print()

# === Issue 3: Sterile neutrino constraints ===
print("=== Issue 3: Sterile neutrino with m_s ~ 1 GeV is not viable ===\n")
# Decay rate formula
G_F = 1.166e-5  # GeV^-2 (Fermi constant)
sin2_2theta_required = 2.3e-18 * 192 * math.pi**3 / (G_F**2 * m_s**5)
print(f"For Γ = 2.3e-18 /s and m_s = 1 GeV:")
print(f"  Required sin²(2θ) = {sin2_2theta_required:.2e}")
print(f"  This is large, but not necessarily ruled out")
print()
print("However, sterile neutrinos with m_s = 1 GeV face strong constraints:")
print("  - Beam dump experiments (CHARM, NA62)")
print("  - BBN (N_eff)")
print("  - Direct production at colliders (LHC)")
print("  - Inferred from meson decays")
print()
print("Conclusion: m_s ~ 1 GeV sterile neutrino is heavily constrained.")
print()

# === Alternative mechanisms ===
print("=== Alternative mechanisms for 'more clustered = slower decay' ===\n")
print("1. STABLE WIMP (no decay):")
print("   - DM is a stable particle, never decays")
print("   - 'Cumulative' because added, not because decaying slowly")
print("   - 'DM and no neutrinos' because no decay")
print("   - Consistent with observation (no anomalous neutrino flux)")
print()
print("2. AXION or AXION-LIKE PARTICLE (no decay):")
print("   - Stable, ultralight, no decay")
print("   - 'DM and no neutrinos' by construction")
print()
print("3. PRIMORDIAL BLACK HOLE DM (no decay):")
print("   - Stable on cosmological timescales (for M > 10^15 g)")
print("   - 'DM and no neutrinos' by construction")
print()
print("4. GEOMETRIC DM (no particle at all):")
print("   - The cascade's framework is geometric, not particle-physics")
print("   - 'DM' is the cumulative gravitational effect of 2D universe deaths")
print("   - No particle, no decay, no neutrino")
print("   - 'More clustered = slower decay' is not needed")
print("   - The cascade is HONEST about this being an option")
print()

# === Save results ===
results = {
    'pauli_blocking_ineffective': {
        'p_F_eV': p_F_eV,
        'E_decay_eV': m_s/2*1e9,
        'ratio': (m_s/2*1e9)/p_F_eV
    },
    'neutrino_flux_too_high': {
        'cascade_prediction': flux,
        'super_k_limit': 1e-4,
        'tension_factor': flux/1e-4
    },
    'sterile_neutrino_constraints': {
        'm_s_assumed_GeV': m_s,
        'sin2_2theta_required': sin2_2theta_required,
        'verdict': 'm_s ~ 1 GeV sterile neutrino is heavily constrained'
    },
    'alternative_mechanisms': [
        'stable WIMP (no decay)',
        'axion-like particle (no decay)',
        'primordial black hole DM (no decay)',
        'geometric DM (no particle, no decay)'
    ],
    'cascade_honest_claim': 'The cascade DM is geometric (cumulative effect of 2D universe deaths), not committed to a specific particle. The user hypothesis (sterile neutrino decay) is one option, but the Pauli blocking mechanism does not work as described.'
}

with open('v27_cascade_dm_self_critique.json', 'w') as f:
    json.dump(results, f, indent=2)

print()
print("Results saved to: calculations/v27_cascade_dm_self_critique.json")
print()
print("Cascade's HONEST acknowledgment:")
print("  §3.13 mechanism (sterile neutrino + Pauli blocking) DOES NOT WORK.")
print("  The user's insight is conceptually interesting but the specific")
print("  mechanism needs revision.")
print()
print("The cascade's framework allows for multiple DM hypotheses:")
print("  (a) Stable particle (no decay): WIMP, axion, etc.")
print("  (b) Unstable particle with non-Pauli mechanism for clustering-dependence")
print("  (c) Geometric DM (no particle, the cascade's geometric framework)")
print()
print("The cascade is committed to (c) as the framework, but (a) and (b)")
print("  are also consistent with observations.")
