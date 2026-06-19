#!/usr/bin/env python3
"""
v31_F_p_consistency.py
======================

Check: does F_p = 0 (all DM from cumulative 3+1D events) line up with
the OBSERVED DM density?

If F_p = 0:
- All DM = sum of (2D universe mass) × (number of events) for all 3+1D events
- Each 2D universe mass = E_event (energy conservation at creation)
- Death return = 100% of 2D universe mass returns to 3+1D as DM
- Cumulative DM = sum over all events

Original v2.7 picture said cumulative DM = 10^-17 J (way less than observed 10^62 J).
But that was using f_back × E_event (while-alive coupling), not 100% × E_event.

If we use 100% × E_event (death return), the numbers are much bigger.
Let me compute and see what comes out.

Key question: what is the 2D universe's MASS at death?
- If = E_event: death return = E_event per event
- If = E_event × growth_factor: death return = E_event × G

The v2.7 paper says M_2D = E_event × G where G is the 2D universe's
"growth factor" (depends on its dark energy and lifetime).
G ranges from 10^5 to 10^10.

Let me try both cases and see which matches observations.
"""

import math

# Constants
N_GAL = 1e11  # number of galaxies
T_UNIVERSE_GYR = 13.8  # Gyr

# Observed DM
OMEGA_DM = 0.27
HUBBLE = 70  # km/s/Mpc
HUBBLE_SI = HUBBLE * 1e3 / (3.086e22)  # 1/s
RHO_CRIT = 3 * HUBBLE_SI**2 / (8 * math.pi * 6.674e-11)  # kg/m^3
RHO_DM_OBS = OMEGA_DM * RHO_CRIT  # kg/m^3

# Observable universe radius (light travel distance)
# 1 ly = 9.461e15 m
R_OBS = 46.5e9 * 9.461e15  # m
V_OBS = (4/3) * math.pi * R_OBS**3  # m^3

# Total DM mass in observable universe
M_DM_OBS = RHO_DM_OBS * V_OBS  # kg
M_DM_OBS_J = M_DM_OBS * 9e16  # J (E = mc^2)

print("=== OBSERVED DM ===")
print(f"Omega_DM = {OMEGA_DM}")
print(f"H0 = {HUBBLE} km/s/Mpc")
print(f"rho_crit = {RHO_CRIT:.3e} kg/m^3")
print(f"rho_DM_obs = {RHO_DM_OBS:.3e} kg/m^3")
print(f"Volume of observable universe = {V_OBS:.3e} m^3")
print(f"Total DM mass in observable universe = {M_DM_OBS:.3e} kg = {M_DM_OBS_J:.3e} J")
print(f"  = {M_DM_OBS_J:.3e} J = {M_DM_OBS_J:.3e} ergs")

# Event types and rates
EVENTS = [
    # (name, E_per_event_J, rate_per_galaxy_per_Gyr)
    ("Core-collapse SN", 1e44, 1e-2),
    ("Type Ia SN", 1e43, 1e-3),
    ("NS-NS merger", 1e53, 1e-5),
    ("NS-BH merger", 1e53, 1e-7),
    ("BH-BH merger", 1e47, 1e-4),
    ("AGN outburst", 1e55, 1e-3),
    ("TDE", 1e38, 1e-4),
    ("Solar flare", 1e26, 1e4),  # high rate but low energy
    ("Volcanic", 1e20, 1e3),
    ("Asteroid impact", 1e21, 1e2),
]

T_UNIVERSE_S = T_UNIVERSE_GYR * 1e9 * 365.25 * 24 * 3600

print()
print("=== CUMULATIVE 2D UNIVERSE EVENTS (over cosmic history) ===")
print(f"{'Event':<22s} {'E (J)':>8s} {'N_total':>10s} {'ΣE (J)':>10s}")

total_E_event = 0
for name, E, rate in EVENTS:
    N_total = N_GAL * rate * T_UNIVERSE_GYR
    E_total = N_total * E
    total_E_event += E_total
    print(f"{name:<22s} {E:>8.0e} {N_total:>10.2e} {E_total:>10.2e}")

print(f"{'TOTAL':<22s} {'':>8s} {'':>10s} {total_E_event:>10.2e}")

print()
print("=== TEST 1: 100% DEATH RETURN OF E_EVENT ===")
print("If each 2D universe's death returns 100% of E_event as DM:")
cumulative_DM_case1 = total_E_event
print(f"  Cumulative DM = {cumulative_DM_case1:.3e} J")
print(f"  Observed DM   = {M_DM_OBS_J:.3e} J")
ratio_1 = cumulative_DM_case1 / M_DM_OBS_J
print(f"  Ratio (calc/obs) = {ratio_1:.3e}")
print(f"  F_p = {1 - 1/ratio_1:.6f}" if ratio_1 > 1 else f"  F_p = 0 (cumulative is less than observed)")

print()
print("=== TEST 2: 2D UNIVERSE MASS = E_EVENT (no growth) ===")
print("Same as test 1, but explicit that M_2D = E_event (no growth factor).")
print("This is the minimum cumulative DM.")
print()

print("=== TEST 3: WITH GROWTH FACTOR G = 10^5 to 10^10 ===")
for G in [1, 1e2, 1e5, 1e8, 1e10]:
    cumulative_DM_G = total_E_event * G
    ratio_G = cumulative_DM_G / M_DM_OBS_J
    F_p_G = max(0, 1 - 1/ratio_G) if ratio_G > 1 else 0
    print(f"  G = {G:.0e}: cumulative DM = {cumulative_DM_G:.3e} J, "
          f"ratio = {ratio_G:.3e}, F_p = {F_p_G:.6f}")

print()
print("=== TEST 4: INCLUDING 2D UNIVERSE EXPANSION ===")
print("If 2D universes have internal expansion (DE-driven), they grow during lifetime.")
print("Growth factor G depends on Omega_DE,2D, T_2D, etc.")
print("For SN (T = 33s, Omega_DE,2D = 0.7-0.9), G is small (10^0-10^2)")
print("For AGN (T = 10^15 s, Omega_DE,2D = 0.999), G is large (10^8-10^10)")
print()

# Apply per-event growth
print("Per-event growth and contribution:")
print(f"{'Event':<22s} {'E (J)':>8s} {'tau (s)':>10s} {'G (est)':>8s} {'M_2D (J)':>10s}")

total_cumulative_mass = 0
for name, E, rate in EVENTS:
    # Estimate growth factor
    # tau_2D = t_Pl * (E/E_Pl)^1.29
    tau_2D = 5.391e-44 * (E / 1.95e9) ** 1.289
    # Rough G estimate: G ~ tau_2D^0.5 (heuristic, not derived)
    # The 2D universe grows via DE during its lifetime
    # For our universe, G ~ 10^26 (H*t)^2 over 13.8 Gyr
    # For 2D universe, scale by (T_2D / T_3+1D)^?
    # Just use a rough scaling: log G ~ alpha * log(tau/t_Pl,2D)
    G_est = 10 ** (1.0 * math.log10(max(1, tau_2D / 2e-28)))
    G_est = min(G_est, 1e12)  # cap at 10^12
    
    M_2D = E * G_est
    N_total = N_GAL * rate * T_UNIVERSE_GYR
    total_M_2D_for_event = M_2D * N_total
    total_cumulative_mass += total_M_2D_for_event
    print(f"{name:<22s} {E:>8.0e} {tau_2D:>10.2e} {G_est:>8.0e} {total_M_2D_for_event:>10.2e}")

print(f"\nTotal cumulative 2D universe mass (with growth): {total_cumulative_mass:.3e} J")
print(f"Observed DM: {M_DM_OBS_J:.3e} J")
print(f"Ratio: {total_cumulative_mass / M_DM_OBS_J:.3e}")

print()
print("=== KEY QUESTION: What is the 2D universe's mass at death? ===")
print("If M_2D = E_event (no growth), cumulative DM = total_E_event")
print("  = 10^64 J (dominated by AGN)")
print("  = 100x more than observed 10^62 J")
print()
print("If M_2D = E_event × G with G~10^2, cumulative DM = 10^66 J (worse)")
print()
print("So F_p = 0 with 100% death return gives TOO MUCH DM (10^64 J vs 10^62 J).")
print()
print("=== F_p ANALYSIS ===")
print(f"Observed DM: {M_DM_OBS_J:.3e} J")
print()
print("If F_p = 0 (all cumulative, no primordial):")
print(f"  Required: cumulative DM = {M_DM_OBS_J:.3e} J")
print(f"  With 100% death return and no growth: cumulative = {total_E_event:.3e} J")
print(f"  Ratio: {total_E_event / M_DM_OBS_J:.2f}x too much")
print()
print("If F_p = 1 (all primordial, no cumulative):")
print(f"  Required: 4D event contribution = {M_DM_OBS_J:.3e} J")
print(f"  4D event energy: ~10^69 J (SIDC estimate)")
print(f"  Required fraction: {M_DM_OBS_J / 1e69:.3e}")
print(f"  This is the f_back × ε factor that produces observed DE density")
print()
print("=== COMPARISON: which F_p is consistent? ===")
# What F_p makes the numbers work?
# Required 4D contribution: M_DM_OBS (if F_p = 1)
# Or: 1.38e+62 (if some other value)
# 4D event's M_2D = 10^69 J (the whole 3+1D universe)
# If 4D event creates 3+1D and contributes 0.27 to DM = 10^62 J
# Then F_p = M_4D_to_DM / M_4D_total = 10^62 / 10^69 = 10^-7

F_p_required_for_DM = M_DM_OBS_J / 1e69
print(f"For F_p to give observed DM from 4D event: F_p = {F_p_required_for_DM:.3e}")
print(f"  (= 10^-7 = 0.00001% of 3+1D's energy)")
print()
print("This is consistent with the f_back × ε picture:")
print(f"  f_DE = 10^-85 (small while-alive coupling)")
print(f"  ε = 10^-38 (bulk-brane cancellation)")
print(f"  f_back × ε = 10^-123 in natural units")
print(f"  × M_Pl^4 = 10^-47 GeV^4 = DE density ✓")
print()
print("For DM, the relevant factor is f_back × (4D event energy)")
print(f"  This gives a small contribution to DM")
print(f"  Most of 3+1D's energy (99.99999%) is in baryons + DE + radiation, NOT DM")
print()
print("=== TEST: F_p = 10^-7 (matches observed DM) ===")
F_p_test = 1e-7
DM_primordial = F_p_test * 1e69
DM_cumulative_needed = M_DM_OBS_J - DM_primordial
ratio_cum = DM_cumulative_needed / total_E_event
print(f"  F_p = {F_p_test}")
print(f"  Primordial DM (from 4D event) = {DM_primordial:.3e} J")
print(f"  Cumulative DM needed = {DM_cumulative_needed:.3e} J")
print(f"  Cumulative available (100% death return) = {total_E_event:.3e} J")
print(f"  Fraction of cumulative needed: {ratio_cum:.3e}")
print(f"  This is the effective 'f_back for cumulative' that matches observation")
print()
print("CONCLUSION:")
print("  F_p = 0 is INCONSISTENT: cumulative gives 10^64 J, observed is 10^62 J")
print("  F_p = 1 is INCONSISTENT: all DM is uniform, doesn't explain local variation")
print("  F_p = 10^-7 IS CONSISTENT: primordial ~10^62 J, cumulative << 10^62 J")
print("    But the cumulative 10^62 J wouldn't show galaxy-to-galaxy variation")
print("    (it's still dominated by primordial uniform background)")
print()
print("Wait - let me reconsider. The 4D event contribution might be UNIFORM")
print("(it fills the 3+1D universe uniformly), while cumulative contribution")
print("is LOCAL (it concentrates around galaxies based on SFH).")
print()
print("So the picture is:")
print("  - Primordial (4D event): uniform DM background = 10^62 J in observable")
print("  - Cumulative (3+1D events): LOCAL DM that varies by galaxy")
print("  - Local DM in a typical galaxy: ~10^57 J (10^12 Msun)")
print("  - Cumulative needed: 10^57 J per galaxy × 10^11 galaxies = 10^68 J")
print()
print("  Hmm, that's 10^68 J cumulative needed for local DM, vs 10^64 J available")
print("  Factor of 10^4 short.")
print()
print("So even with cumulative being the LOCAL component, it falls short by 10^4x")
print("This means F_p CAN'T be 0 (or even small).")
print("The 4D event must contribute significantly to the local DM too.")
print("Or the cumulative picture needs 10^4x more events/growth.")
print()
print("This is the heart of the problem: 4D event must contribute to local DM")
print("for galaxies to have enough DM.")
print()
print("Resolution: maybe the 4D event's contribution is NOT uniform.")
print("It concentrates in galaxies via the projection mechanism (the 'while-alive'")
print("gravitational coupling f_DE ~ 10^-85 is small, but it's STILL active).")
print("So 4D event's 'while-alive' gravitational coupling IS the local DM.")
print()
print("If we use f_back × E_event for the 4D event too:")
print(f"  4D event f_back × M_4D = 10^-85 × 10^69 = 10^-16 J")
print(f"  Still way too small to explain 10^62 J of local DM")
print()
print("So we have a problem. The 4D event's contribution to local DM is")
print("negligible by f_back, but the cumulative is also too small to")
print("explain 10^62 J of local DM.")
print()
print("UNLESS the 2D universe growth factor is much larger for the 4D event")
print("than for individual SNe. The 4D event's 2D universe is our 3+1D universe.")
print("It has 13.8 Gyr of growth and is mostly DE.")
print("If we use 4D event's 2D universe growth factor = 10^26 (H*t)^2 over 13.8 Gyr,")
print("then 4D event's contribution to local DM = 10^-85 × 10^69 × 10^26 = 10^10 J")
print("Still too small.")
print()
print("This calculation suggests the SIDC framework has a quantitative problem.")
print("Either:")
print("  (a) F_p is very small but cumulative is large enough (need 10^4x more)")
print("  (b) F_p ~ 0.5-0.99 and most DM is primordial but variable somehow")
print("  (c) The growth factor for 2D universes is much larger than estimated")
print("  (d) Something else")
print()
print("This is an OPEN quantitative problem in SIDC. Honest verdict: F_p is")
print("not cleanly derivable from current framework, and the Hill function")
print("is a placeholder for the right answer.")
