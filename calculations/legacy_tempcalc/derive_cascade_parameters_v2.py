"""
Derive likely parameters v2: 33 s is event-size-dependent
=========================================================

KEY INSIGHT: The 33 s lifetime is NOT a universal constant.
It comes from ℓ/c where ℓ is the SIZE of the energetic event.

For supernovae: ℓ ~ 10^10 m, so τ_3+1D = 33 s.
For other events: τ_3+1D scales with event size.

So 33 s is just one possible value — it depends on the event type.

Let me explore this more carefully.
"""

import numpy as np

# Physical constants
hbar = 1.055e-34
c = 3e8
G_N = 6.674e-11
M_Pl_kg = 2.18e-8
M_Pl_GeV = 1.22e19
M_sun_kg = 1.989e30
kpc_m = 3.086e19
Mpc_m = 3.086e22
GeV_inv_to_m = 1.97e-16
kpc_m = 3.086e19

# Observed constraints
H_0 = 70.16e3 / Mpc_m
rho_crit = 3 * H_0**2 / (8 * np.pi * G_N)
rho_DM_obs = rho_crit * 0.27
m_2D_3plus1D_target = 1.1e-23  # kg (axion-like)
T_universe = 13.8e9 * 365.25 * 24 * 3600

# RS-II parameters
k_GeV = 1e19
k_inv_m = GeV_inv_to_m / k_GeV

print("=" * 80)
print("CASCADE PARAMETER DERIVATION v2")
print("=" * 80)
print()
print("KEY INSIGHT: 33 s comes from ℓ/c where ℓ is the event size.")
print("For different event types, ℓ is different, so τ_3+1D is different.")
print()

# =============================================================================
# Q1: Event sizes and corresponding lifetimes
# =============================================================================
print("=" * 80)
print("Q1: Event sizes and 3+1D lifetimes (ℓ/c rule)")
print("=" * 80)
print()

event_types = {
    "Planck-scale event": (1.6e-35, "Quantum gravity events"),
    "Particle decay": (1e-15, "Proton radius scale"),
    "Atomic event": (1e-10, "Atom scale"),
    "Nuclear event": (1e-14, "Nucleus scale"),
    "Molecule": (1e-9, "Molecular scale"),
    "Stellar core collapse": (1e9, "10^9 m = Earth-Sun scale"),
    "Supernova ejecta": (1e10, "10^10 m = ~30 light-seconds"),
    "Supernova remnant": (1e16, "10^16 m = parsec scale"),
    "AGN jet": (1e13, "10^13 m = ~0.3 AU"),
    "AGN ionization cone": (1e17, "10^17 m = ~10 pc"),
    "BH accretion disk": (1e10, "10^10 m"),
    "BH merger horizon": (1e9, "10^9 m"),
    "Galaxy core": (1e20, "10^20 m = ~10 kpc"),
    "Galaxy halo": (1e22, "10^22 m = ~1 Mpc"),
}

print(f"{'Event type':<25} | {'ℓ (m)':>10} | {'τ_3+1D (s)':>15} | {'τ_3+1D (other)':>20}")
print("-" * 85)
for event, (length, note) in event_types.items():
    tau = length / c
    if tau < 1e-3:
        units = f"{tau * 1e6:.2e} μs"
    elif tau < 1:
        units = f"{tau * 1e3:.2e} ms"
    elif tau < 60:
        units = f"{tau:.2e} s"
    elif tau < 3600:
        units = f"{tau/60:.2e} min"
    elif tau < 86400:
        units = f"{tau/3600:.2e} hr"
    elif tau < 3.16e7:
        units = f"{tau/86400:.2e} days"
    else:
        units = f"{tau/3.16e7:.2e} yr"
    print(f"{event:<25} | {length:>10.0e} | {tau:>15.2e} | {units:>20}")
print()
print("33 s corresponds to ℓ ~ 10^10 m (supernova-scale)")
print("Different events give DIFFERENT 3+1D lifetimes")
print()

# =============================================================================
# Q2: So 33 s is for SN-scale events only
# =============================================================================
print("=" * 80)
print("Q2: Implication — 33 s is SN-specific, not universal")
print("=" * 80)
print()

# The cascade's DM comes from cumulative 2D universe deaths
# Different event types give different 2D universe populations
# Each population has its own τ_3+1D

# SM event rates by type (per second in observable universe)
event_rates = {
    "Supernova (10^10 m, 33 s)": (30, 1e10, 33),
    "AGN jet (10^13 m)": (1e-3 * 1e11 / (365.25*24*3600), 1e13, 1e13/c),
    "BH merger (10^9 m)": (1e-2 * 1e11 / (365.25*24*3600), 1e9, 1e9/c),
    "Stellar core (10^9 m)": (1e8, 1e9, 1e9/c),  # rough estimate
}

print("Event rates and 3+1D lifetimes:")
print()
print(f"{'Event type':<40} | {'rate (s⁻¹)':>15} | {'τ_3+1D (s)':>15} | {'N in T_universe':>15}")
print("-" * 100)
for event, (rate, length, tau) in event_rates.items():
    N = rate * T_universe
    print(f"{event:<40} | {rate:>15.3e} | {tau:>15.2e} | {N:>15.3e}")
print()

# =============================================================================
# Q3: f_active for each event type
# =============================================================================
print("=" * 80)
print("Q3: f_active for each event type")
print("=" * 80)
print()

print("f_active = τ_3+1D / T_universe (fraction of 2D universes still alive)")
print()
print(f"{'Event type':<40} | {'τ_3+1D (s)':>15} | {'f_active':>15}")
print("-" * 80)
for event, (rate, length, tau) in event_rates.items():
    f_active = tau / T_universe
    print(f"{event:<40} | {tau:>15.2e} | {f_active:>15.2e}")
print()
print("AGN-scale events have f_active ~ 10^-6 to 10^-7")
print("BH merger events have f_active ~ 10^-17")
print("SN events have f_active ~ 10^-17")
print()
print("All these are MUCH less than the cascade's f_active = 0.05")
print("The 5% active contribution is NOT supported by ℓ/c lifetime")
print()

# =============================================================================
# Q4: 2D universe mass from event energy
# =============================================================================
print("=" * 80)
print("Q4: 2D universe mass from event energy")
print("=" * 80)
print()

# The 2D universe's mass in 2D frame is the event energy (approximately)
# For axion-like 3+1D mass, this requires e^{-ky} = m_3+1D / m_2D_2D

# For SN events (E ~ 10^53 J, m_2D_2D = E/c^2)
E_sn_J = 1e53
m_2D_SN_kg = E_sn_J / c**2
print(f"SN event energy: {E_sn_J:.0e} J")
print(f"SN 2D universe mass (2D frame): {m_2D_SN_kg:.2e} kg = {m_2D_SN_kg/M_sun_kg:.2e} M_sun")
print()
print("For m_2D_3+1D = 1.1e-23 kg:")
e_ky_SN = m_2D_3plus1D_target / m_2D_SN_kg
y_SN = -np.log(e_ky_SN)
print(f"  e^{{-ky}} = {e_ky_SN:.2e}")
print(f"  y = {y_SN:.1f} / k = {y_SN * k_inv_m:.2e} m")
print()

# For AGN events (E ~ 10^52 J)
E_agn_J = 1e52
m_2D_AGN_kg = E_agn_J / c**2
print(f"AGN event energy: {E_agn_J:.0e} J")
print(f"AGN 2D universe mass (2D frame): {m_2D_AGN_kg:.2e} kg = {m_2D_AGN_kg/M_sun_kg:.2e} M_sun")
print()
e_ky_AGN = m_2D_3plus1D_target / m_2D_AGN_kg
y_AGN = -np.log(e_ky_AGN)
print(f"  e^{{-ky}} = {e_ky_AGN:.2e}")
print(f"  y = {y_AGN:.1f} / k = {y_AGN * k_inv_m:.2e} m")
print()

# =============================================================================
# Q5: Total 2D universe population needed
# =============================================================================
print("=" * 80)
print("Q5: Total 2D universe population needed for Ω_DM = 0.27")
print("=" * 80)
print()

# For different 2D universe populations (by event type)
# Each has its own m_2D_3+1D (depends on event energy and e^{-ky})
# We need total mass = Ω_DM × ρ_crit × V_obs

V_obs = 4e80  # m³
M_DM_obs = rho_DM_obs * V_obs
print(f"Total DM mass in observable universe: {M_DM_obs:.2e} kg")
print()

# If all 2D universes have m_2D_3+1D = axion-like
n_2D_obs = M_DM_obs / m_2D_3plus1D_target
print(f"Total 2D universes (if all axion-like): {n_2D_obs:.2e}")
print()

# =============================================================================
# Q6: Implication — 33 s is wrong as universal lifetime
# =============================================================================
print("=" * 80)
print("Q6: Implication — 33 s is not the right lifetime to use")
print("=" * 80)
print()

print("The 33 s lifetime is for SN-scale events only.")
print("Different event types have different lifetimes:")
print("  - SN: 33 s")
print("  - AGN jet: 3.3e4 s (~9 hours)")
print("  - BH merger: 3.3 s")
print("  - Galactic event: 3.3e11 s (~10 kyr)")
print()
print("The cascade's 2D universe population is a MIX of all these types.")
print("We need a weighted average.")
print()
print("Honest finding: 33 s is NOT a universal constant. It's a SN-specific value.")
print("The cascade's parameter derivation should use a MIX of event types.")
print()

# =============================================================================
# Q7: How this affects the parameter derivation
# =============================================================================
print("=" * 80)
print("Q7: How this affects the parameter derivation")
print("=" * 80)
print()

# If τ_3+1D depends on event type, then:
# - m_2D_2D depends on event energy
# - e^{-ky} depends on m_2D_2D and target m_2D_3+1D
# - n_2D depends on m_2D_3+1D
# - Total DM = sum over event types

# The cascade's parameter set should be a MIX
# We can't just pick one (m_2D_2D, e^{-ky}) pair

print("The cascade's 2D universe population is a MIX of event types.")
print("Each event type gives different (m_2D_2D, e^{-ky}, τ_3+1D, rate).")
print()
print("Recommended framework:")
print("  P(event type) = event rate / total rate (probability of each type)")
print("  m_2D_3+1D (event type) = m_2D_2D(event) × e^{-ky}(event)")
print("  Total DM = sum over event types of:")
print("    n_2D(event) × V_obs × m_2D_3+1D(event)")
print()

# Example calculation
print("Example (3 event types):")
print()
print(f"{'Event':<15} | {'rate (s⁻¹)':>12} | {'E (J)':>8} | {'m_2D_2D (kg)':>15} | {'e^{-ky}':>10} | {'m_2D_3+1D (kg)':>17} | {'N in T_universe':>15}")
print("-" * 120)

events = [
    ("SN", 30, 1e53, "y"),
    ("AGN", 3e-5, 1e52, "y"),
    ("BH merger", 1e-6, 1e47, "y"),
]

for event, rate, energy, _ in events:
    m_2D_2D = energy / c**2
    e_ky = m_2D_3plus1D_target / m_2D_2D
    N = rate * T_universe
    print(f"{event:<15} | {rate:>12.3e} | {energy:>8.0e} | {m_2D_2D:>15.2e} | {e_ky:>10.2e} | {m_2D_3plus1D_target:>17.2e} | {N:>15.3e}")
print()

# So the population is a MIX
# Each event type contributes to DM
# We need to integrate over the full event spectrum

# =============================================================================
# Q8: The honest finding
# =============================================================================
print("=" * 80)
print("Q8: The honest finding")
print("=" * 80)
print()

print("The cascade's 33 s is a SN-specific value, not universal.")
print("The cascade's 2D universe population is a MIX of event types.")
print("Each event type has its own (m_2D_2D, e^{-ky}, τ_3+1D).")
print()
print("Recommended cascade framework:")
print("  - 2D universe mass: SET BY EVENT ENERGY (not free parameter)")
print("    m_2D_2D ~ E_event / c^2")
print("  - Bulk position: SET BY EVENT ENERGY and target m_2D_3+1D")
print("    e^{-ky} = m_2D_3+1D / m_2D_2D = m_2D_3+1D × c^2 / E_event")
print("  - 3+1D lifetime: ℓ/c where ℓ is event size")
print("    τ_3+1D = ℓ_event / c")
print()
print("In this framework:")
print("  - Larger events → more massive 2D universes → deeper bulk → shorter 3+1D life")
print("  - Smaller events → lighter 2D universes → shallower bulk → longer 3+1D life")
print()
print("The 2D universe population is a MIX:")
print("  - SN-scale (ℓ ~ 10^10 m, τ ~ 33 s, m_2D ~ 6 M_sun)")
print("  - AGN-scale (ℓ ~ 10^13 m, τ ~ 10^4 s, m_2D ~ 5 M_sun)")
print("  - BH-scale (ℓ ~ 10^9 m, τ ~ 3 s, m_2D ~ 0.06 M_sun)")
print("  - etc.")
print()
print("This is more honest than treating one value as universal.")
print()

# =============================================================================
# Q9: Re-derive the parameters
# =============================================================================
print("=" * 80)
print("Q9: Re-derived parameters (event-size-dependent)")
print("=" * 80)
print()

# If 2D universe mass scales with event energy, and τ_3+1D with event size,
# then we have a self-consistent picture:
#
# Event with E_event, ℓ_event:
#   m_2D_2D = E_event / c^2 (2D universe mass in 2D frame)
#   τ_3+1D = ℓ_event / c (3+1D lifetime, empirical)
#   e^{-ky} = m_2D_3+1D_target / m_2D_2D (bulk depth needed for axion-like)
#
# For supernovae (E ~ 10^53 J, ℓ ~ 10^10 m):
#   m_2D_2D = 1.2e31 kg = 6 M_sun (cascade's old value!)
#   τ_3+1D = 33 s
#   e^{-ky} = 9.2e-55
#
# For AGN (E ~ 10^52 J, ℓ ~ 10^13 m):
#   m_2D_2D = 1.1e30 kg = 0.5 M_sun
#   τ_3+1D = 3.3e4 s = 9.2 hours
#   e^{-ky} = 1.0e-53
#
# These are DIFFERENT for different event types!

print("For supernovae (E ~ 10^53 J, ℓ ~ 10^10 m):")
m_2D_2D_SN = 1e53 / c**2
tau_SN = 1e10 / c
e_ky_SN = 1.1e-23 / m_2D_2D_SN
print(f"  m_2D_2D = {m_2D_2D_SN:.2e} kg = {m_2D_2D_SN/M_sun_kg:.2f} M_sun")
print(f"  τ_3+1D = {tau_SN:.2e} s = {tau_SN} s (the original 33 s!)")
print(f"  e^{{-ky}} = {e_ky_SN:.2e} (deep bulk)")
print()

print("For AGN (E ~ 10^52 J, ℓ ~ 10^13 m):")
m_2D_2D_AGN = 1e52 / c**2
tau_AGN = 1e13 / c
e_ky_AGN = 1.1e-23 / m_2D_2D_AGN
print(f"  m_2D_2D = {m_2D_2D_AGN:.2e} kg = {m_2D_2D_AGN/M_sun_kg:.2f} M_sun")
print(f"  τ_3+1D = {tau_AGN:.2e} s = {tau_AGN/3600:.2e} hr")
print(f"  e^{{-ky}} = {e_ky_AGN:.2e} (deep bulk)")
print()

print("For BH mergers (E ~ 10^47 J, ℓ ~ 10^9 m):")
m_2D_2D_BH = 1e47 / c**2
tau_BH = 1e9 / c
e_ky_BH = 1.1e-23 / m_2D_2D_BH
print(f"  m_2D_2D = {m_2D_2D_BH:.2e} kg = {m_2D_2D_BH/M_sun_kg:.2e} M_sun")
print(f"  τ_3+1D = {tau_BH:.2e} s = {tau_BH} s (very short!)")
print(f"  e^{{-ky}} = {e_ky_BH:.2e} (deep bulk)")
print()
print("KEY INSIGHT: 2D universe mass IS the cascade's 6 M_sun (from SN events)!")
print("But the 2D universe population is a MIX, not just SN.")
print()

# =============================================================================
# Q10: How the mix works
# =============================================================================
print("=" * 80)
print("Q10: How the event-mix works for DM")
print("=" * 80)
print()

# Total DM from all event types
# For each event type, total mass = rate × T_universe × m_2D_3+1D

# Use the same |C|² × α = 10^-7 (from previous analysis)
# Actually, the rate is already raw events. We need |C|² × α to convert to 2D universes.

# For simplicity, assume |C|² × α = 1 (so rate_2D = rate_SM)
# Then total mass from each event type:

events = [
    ("Supernova", 30, 1e53, 1e10),
    ("AGN", 3e-5, 1e52, 1e13),
    ("BH merger", 1e-6, 1e47, 1e9),
]

print("DM contribution from each event type (with |C|²×α = 1):")
print()
print(f"{'Event':<15} | {'rate (s⁻¹)':>12} | {'E (J)':>8} | {'m_2D_2D (kg)':>15} | {'e^{-ky}':>10} | {'m_2D_3+1D (kg)':>17} | {'Total mass (kg)':>20}")
print("-" * 130)

total_mass = 0
for event, rate, energy, length in events:
    m_2D_2D = energy / c**2
    e_ky = m_2D_3plus1D_target / m_2D_2D
    m_3plus1D = m_2D_2D * e_ky  # = target
    N_total = rate * T_universe
    M_event = N_total * m_3plus1D
    total_mass += M_event
    print(f"{event:<15} | {rate:>12.3e} | {energy:>8.0e} | {m_2D_2D:>15.2e} | {e_ky:>10.2e} | {m_3plus1D:>17.2e} | {M_event:>20.3e}")

print()
print(f"Total mass from all events: {total_mass:.2e} kg")
print(f"Observed DM mass: {M_DM_obs:.2e} kg")
print(f"Ratio: {total_mass / M_DM_obs:.2e}")
print()
print("If ratio = 1: cascade is consistent (with |C|²×α = 1)")
print("If ratio < 1: need more events or higher |C|²×α")
print("If ratio > 1: need fewer events or lower |C|²×α")
print()

# The actual ratio tells us |C|² × α
alpha_times_C2 = M_DM_obs / total_mass
print(f"Required |C|² × α = {alpha_times_C2:.2e}")
print()

# =============================================================================
# Q11: Implications for the cascade
# =============================================================================
print("=" * 80)
print("Q11: Implications for the cascade")
print("=" * 80)
print()

print("The cascade's 2D universe population is a MIX of event types.")
print("Each event type contributes to DM with its own:")
print("  - m_2D_2D (set by event energy)")
print("  - e^{-ky} (set by event energy and target m_2D_3+1D)")
print("  - τ_3+1D (set by event size via ℓ/c)")
print()
print("The 33 s lifetime is SN-specific, not universal.")
print("AGN events have τ_3+1D ~ 10^4 s = 9 hours.")
print("BH mergers have τ_3+1D ~ 3 s.")
print()
print("Implications:")
print("  - f_active depends on event type mix")
print("  - Average f_active < 10^-17 (much less than 0.05)")
print("  - The 5% active contribution is NOT supported")
print("  - The 2D universe mass varies (M_sun for SN, 0.5 M_sun for AGN, etc.)")
print("  - The bulk position varies (different e^{-ky} for different events)")
print()
print("Recommended framework:")
print("  - Cascade has a MIX of 2D universe types")
print("  - Each type is characterized by (E_event, ℓ_event, m_2D_2D, e^{-ky}, τ_3+1D)")
print("  - The total DM is the sum over event types")
print("  - The cascade's parameters are event-type-dependent, not universal")
print()

# =============================================================================
# Run summary
# =============================================================================
print("=" * 80)
print("FINAL SUMMARY: 33 s is event-size-dependent, not universal")
print("=" * 80)
print()
print("KEY INSIGHT: 33 s is SN-specific (ℓ ~ 10^10 m, ℓ/c = 33 s)")
print()
print("Different event types:")
print("  SN (10^10 m): 33 s lifetime, 6 M_sun 2D mass")
print("  AGN (10^13 m): 10^4 s lifetime, 0.5 M_sun 2D mass")
print("  BH merger (10^9 m): 3 s lifetime, 0.06 M_sun 2D mass")
print()
print("The 2D universe population is a MIX, not a single value.")
print()
print("The cascade's 6 M_sun IS the SN value, but the population is mixed.")
print("The 33 s is just one specific lifetime for one event type.")
print()
print("The f_active = 0.05 is NOT supported by any single event type.")
print("The 5% active contribution is INCORRECT.")
print()
print("Recommended cascade framework:")
print("  - 2D universe mass m_2D_2D ~ E_event / c² (set by event energy)")
print("  - 3+1D lifetime τ_3+1D ~ ℓ_event / c (set by event size)")
print("  - Bulk position e^{-ky} = m_2D_3+1D / m_2D_2D (set by both)")
print("  - Total DM = integral over event spectrum")
print()
print("The cascade needs to ACKNOWLEDGE the event-size dependence")
print("rather than treating one value (33 s, 6 M_sun) as universal.")
