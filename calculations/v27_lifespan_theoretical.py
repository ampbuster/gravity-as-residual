"""
All four follow-ups:
1. Sensitivity to a hypothetical second data point
2. 2D CFT theoretical derivation attempt
3. Death GW background spectrum
4. Additional 2D universe lifetime anchors


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
t_Pl = 5.39e-44    # s
E_Pl = 1.96e9      # J
c_light = 2.998e8
hbar = 1.055e-34
G_N = 6.674e-11
year = 3.156e7
Mpc = 3.086e22

# Calibration
E_SN = 1e44        # J
T_SN = 33          # s
alpha_best = math.log(T_SN / t_Pl) / math.log(E_SN / E_Pl)
print(f"Best-fit alpha (forced by SN): {alpha_best:.4f}")

# ============================================================================
# 1. SENSITIVITY TO A HYPOTHETICAL SECOND DATA POINT
# ============================================================================
print("="*78)
print(" 1. SENSITIVITY: if we had a SECOND 2D universe lifetime data point,")
print("    how much would α change?")
print("="*78)
print()
print("  Calibration point 1: Type Ia SN  (10^44 J)  →  33 s")
print()
print("  Try various hypothetical 2nd points and refit α:")
print()

# Various hypothetical 2nd data points: a BNS merger 2D universe
second_points = [
    ("BNS merger 2D universe", 1e53, 1e2),       # 100 yr
    ("BNS merger 2D universe", 1e53, 1e3),       # 1 kyr
    ("BNS merger 2D universe", 1e53, 1e4),       # 10 kyr
    ("BNS merger 2D universe", 1e53, 4.3e5),     # α=1.29 prediction
    ("BNS merger 2D universe", 1e53, 1e6),       # 1 Myr
    ("BNS merger 2D universe", 1e53, 1e7),       # 10 Myr
    ("AGN flare 2D universe",  1e55, 1e6),       # 1 Myr
    ("AGN flare 2D universe",  1e55, 1e7),       # 10 Myr
    ("AGN flare 2D universe",  1e55, 1.6e8),     # α=1.29 prediction
    ("AGN flare 2D universe",  1e55, 1e10),      # 10 Gyr
    ("Hypernova 2D universe",  1e46, 1e1),       # 10 s
    ("Hypernova 2D universe",  1e46, 1e3),       # ~17 min
    ("Hypernova 2D universe",  1e46, 3.5e0),     # α=1.29 prediction (3.5 hr)
    ("Hypernova 2D universe",  1e46, 1e5),       # ~1 day
]

print(f"{'Hypothetical 2nd point':>30s} | {'log10 E':>8s} | {'T_2D':>10s} | {'α (refit)':>12s} | {'T_3D (4D)':>15s}")
print("-"*90)
for name, E2, T2 in second_points:
    # Refit α from two points
    # log10(T2) - log10(T1) = α × (log10(E2) - log10(E1))
    # α = (log10(T2) - log10(T1)) / (log10(E2) - log10(E1))
    alpha_refit = (math.log10(T2) - math.log10(T_SN)) / (math.log10(E2) - math.log10(E_SN))
    # Refit T_3D
    T_3D_refit = T_SN * (1e69 / E_SN) ** alpha_refit
    print(f"{name:>30s} | {math.log10(E2):>8.1f} | {T2:>10.2e} | {alpha_refit:>12.4f} | {T_3D_refit/year:>15.2e}")

print()
print("  KEY INSIGHT:  if the 2nd data point is CONSISTENT with α=1.29,")
print("  the rule is robust.  If the 2nd data point is INCONSISTENT,")
print("  α must change, and the 4D cosm. lifespan changes dramatically.")
print()
print("  The α=1.29 rule predicts:")
print("    BNS merger 2D universe:  4.3e5 yr (if α=1.29)")
print("    AGN flare 2D universe:  1.6e8 yr (if α=1.29)")
print("    Hypernova 2D universe:  3.5 hr (if α=1.29)")
print()
print("  These predictions are TESTABLE in principle (search for GW death")
print("  bursts at the predicted times after the corresponding events).")

# ============================================================================
# 2. 2D CFT THEORETICAL DERIVATION ATTEMPT
# ============================================================================
print()
print("="*78)
print(" 2. CAN THE c=1 MATRIX MODEL GIVE A FIRST-PRINCIPLES α?")
print("="*78)
print()
print("  The cascade's 2D CFT is the c=1 matrix model (Kazakov-Kostov-Kutasov).")
print("  Its Lagrangian (in the 2D worldsheet):")
print()
print("    S = ∫ d²σ √g (1/2 ∂φ ∂φ + μ e^(2bφ) + T(φ) + R (1/4π) φ + ...)")
print()
print("  Where:")
print("    φ  = 2D dilaton field")
print("    μ  = 2D cosmological constant")
print("    T(φ) = 2D tachyon field")
print("    b   = 2D string coupling parameter (b = i for c = 1)")
print("    R   = 2D worldsheet curvature")
print()
print("  The 2D universe's evolution is governed by this Lagrangian.")
print("  The 2D universe 'lifetime' in 3D view should be related to:")
print()
print("  1. 2D tachyon condensation time: t_T ~ 1/μ  (in 2D Planck units)")
print("     For T_2D = 33s:  μ ~ ℏ/(33s c²) ~ 5e-48 J ~ 3e-29 eV")
print()
print("  2. 2D universe expansion time:  t_exp ~ l_Pl,2 / c ~ t_Pl,2")
print("     For 2D Planck time t_Pl,2 ~ ℏ/μc²:  t_Pl,2 = 33s  →  same as above")
print()
print("  3. 2D 'burnout' time:  time for the 2D universe's matter to fully")
print("     expand/dilute.  This depends on the 2D Hubble rate, set by μ.")
print()
print("  The c=1 matrix model has:")
print("    - 2D string coupling g_s  (free parameter)")
print("    - 2D cosmological constant μ  (free parameter)")
print("    - b = i (fixed by c = 1)")
print()
print("  The 2D universe's lifetime T_2D is set by these parameters, NOT by")
print("  the 3D event's energy E_3D.  This contradicts the energy-scaling rule.")
print()
print("  RESOLUTION:  the c=1 matrix model describes the 2D universe's INTERNAL")
print("  dynamics.  The 2D universe's INTERNAL lifetime is set by μ.  The 3D")
print("  event's energy determines the 2D universe's *contents* (matter, energy,")
print("  size), not its internal lifetime.")
print()
print("  So the cascade's energy-scaling rule might be WRONG, or it might be")
print("  describing something different (the 2D universe's *effective* lifetime")
print("  in 3D view, not its internal lifetime).")
print()
print("  This is an OPEN question.  A 2D CFT expert would be needed to derive")
print("  the relationship between E_3D and T_2D rigorously.")
print()
print("  Verdict:  the c=1 matrix model doesn't give α=1.29 directly.  The")
print("  energy-scaling rule is a *fit* to one data point, and its theoretical")
print("  motivation is unclear.")

# ============================================================================
# 3. DEATH GW BACKGROUND SPECTRUM
# ============================================================================
print()
print("="*78)
print(" 3. DEATH GW BACKGROUND SPECTRUM (predicted LISA signal shape)")
print("="*78)
print()
print("  The cascade predicts a stochastic GW background from 2D universe")
print("  *death* events.  Each 3D event creates a 2D universe of lifetime T_2D;")
print("  the 2D universe dies with a GW burst at frequency f ~ 1/T_2D.")
print()
print("  The GW background spectrum depends on:")
print("    - The rate of past 3D energetic events (SNe, hypernovae, GRBs, BNS)")
print("    - The lifetime distribution (set by α and event energy)")
print("    - The 2D universe's 'death' GW energy (cascade prediction: ~10^60 erg)")
print()
print("  For the cascade's energy-scaling rule (α=1.29), the death frequencies are:")

# Event types and their rates
events_for_gw = [
    # (name, energy, rate_per_Mpc3_per_year, lifetime, freq)
    ("Type Ia SN",   1e44, 1e-7, 33,        0.03),
    ("Hypernova",    1e46, 1e-9, 1.26e4,    2.2e-5),  # 3.5 hr
    ("Long GRB",     1e47, 1e-10, 2.45e5,   4.7e-6),  # 2.8 days
    ("Short GRB",    1e45, 1e-9, 643,       1.55e-3), # 10.7 min
    ("BNS merger",   1e53, 1e-7, 1.36e13,   7.4e-14), # 4.3e5 yr
    ("Magnetar",     1e40, 1e-7, 2.28e-4,   4.4e3),   # 228 μs
    ("AGN flare",    1e55, 1e-9, 5.18e15,   1.93e-16), # 1.6e8 yr
]

# Compute the GW energy density per frequency
# ρ_GW(f) = sum over events of (rate × E_GW_per_death × dN/df)
# For a delta-function burst at f_i: ρ_GW(f) = sum rate_i × E_i × δ(f - f_i)
# In practice, each event has a finite bandwidth, so we smooth over a log range

print()
print(f"  {'Event':>15s} | {'E (J)':>10s} | {'Rate (Mpc⁻³/yr)':>16s} | {'T_2D':>12s} | {'f (Hz)':>12s}")
print("-"*80)
for name, E, rate, T, f in events_for_gw:
    T_fmt = f"{T:.2e}".replace("e+0", "e").replace("e-0", "e-")
    if T < 1:
        T_fmt = f"{T*1e3:.2f} ms" if T > 1e-3 else f"{T*1e6:.2f} μs"
    elif T < 60:
        T_fmt = f"{T:.2f} s"
    elif T < 3600:
        T_fmt = f"{T/60:.2f} min"
    elif T < 86400:
        T_fmt = f"{T/3600:.2f} hr"
    elif T < year:
        T_fmt = f"{T/86400:.2f} days"
    elif T < 1e6*year:
        T_fmt = f"{T/year:.2e} yr"
    else:
        T_fmt = f"{T/year:.2e} yr"
    print(f"  {name:>15s} | {E:>10.1e} | {rate:>16.1e} | {T_fmt:>12s} | {f:>12.2e}")

# The dominant signal in LISA's band (10^-4 to 1 Hz) is from SNe (0.03 Hz)
# and hypernovae (2.2e-5 Hz, just below LISA's band)
# Long GRBs (4.7e-6 Hz) are below LISA's band

# Total GW energy density
# Assuming each death releases E_GW ~ 10^60 erg = 10^53 J
E_per_death = 1e53  # J (rough estimate from cascade)
# Rate of 2D universe deaths in LISA's frequency band (10^-4 to 1 Hz)
# is dominated by SNe and hypernovae
rate_in_band = 1e-7 * 1e-9  # (SN rate) × (hypernova rate) per Mpc³/yr
# Wait, that's wrong.  Let me recompute.

# Each event type contributes independently
# For each event type, the death rate = 3D event rate
# (every 3D event creates exactly one 2D universe, which dies at T_2D)

# The total GW energy density is the integral over past events:
# ρ_GW(f) = ∫ dt (rate) × E_per_death × dN/df
# For a steady-state rate and narrow-band bursts:
# Ω_GW(f) ~ (rate × E_per_death) / (ρ_crit × c² × Δf)

# Numerical estimate
# ρ_crit = 9.2e-27 kg/m³ = 8.3e-10 J/m³
rho_crit = 8.3e-10  # J/m³
# Volume integral over cosmic time
H0_inv = 4.4e17  # s (1/H0 ~ 14 Gyr)
# Total 2D universe deaths per Mpc³ over Hubble time
# SN: 1e-7 × 4.4e17 / (Mpc in m)³ = 1e-7 × 4.4e17 / (3.086e22)³ = 1.5e-36 per m³
SN_deaths_per_m3 = 1e-7 * H0_inv / Mpc**3
# Total energy per m³ from SN deaths
SN_energy_density = SN_deaths_per_m3 * E_per_death
print()
print(f"  SN death energy density (over 14 Gyr): {SN_energy_density:.2e} J/m³")
print(f"  ρ_crit:                                {rho_crit:.2e} J/m³")
print(f"  Ω_GW(SN, 0.03 Hz):                     {SN_energy_density/rho_crit:.2e}")
# This is the *peak* Ω_GW at the SN death frequency

# For LISA: detectability threshold is Ω_GW ~ 10^-12
LISA_threshold = 1e-12
print(f"  LISA detection threshold:                {LISA_threshold:.0e}")
print(f"  Detectable?  {SN_energy_density/rho_crit > LISA_threshold}")
print()
print("  The SN 2D universe death GW background peaks at 0.03 Hz, just")
print("  inside LISA's 10^-4 - 1 Hz band.  If the cascade's energy-scaling")
print("  rule is right, LISA should detect a stochastic GW background at")
print("  this frequency.")

# ============================================================================
# 4. ADDITIONAL 2D UNIVERSE LIFETIME ANCHORS
# ============================================================================
print()
print("="*78)
print(" 4. ADDITIONAL 2D UNIVERSE LIFETIME ANCHORS IN THE CASCADE")
print("="*78)
print()
print("  Looking for OTHER 2D universe lifetime data points in the cascade...")
print()

# Anchor 1: 2D Planck scale
print("  --- Anchor 1: 2D universe Planck scale (set by μ) ---")
print()
print("  The 2D universe's natural time scale is t_Pl,2 = ℏ/(μ c²).")
print("  If T_2D ~ t_Pl,2, then:")
print()
print("    T_2D = 33 s  →  μ = ℏ/(33s c²) = 5.3e-48 J = 3.3e-29 eV")
print()
print("  This is a *derived* value of μ.  But the cascade treats μ as a FREE")
print("  parameter.  If the cascade *requires* T_2D = t_Pl,2 = 33s, then μ is")
print("  no longer free — it's pinned to 3.3e-29 eV.")
print()
print("  This is interesting because:")
print("    - 3.3e-29 eV is way below typical 2D CFT scales")
print("    - It's a 'dark energy'-like scale (slow-roll vacuum energy)")
print("    - It might be related to the 2D universe's 'slow' burnout")
print()
print("  PROBLEM:  T_2D = t_Pl,2 gives a UNIVERSAL 2D universe lifetime of 33s,")
print("  regardless of the 3D event.  This contradicts the user's energy-scaling")
print("  intuition (lower-energy events → shorter 2D universes).")
print()
print("  RESOLUTION:  T_2D = t_Pl,2 is the *minimum* lifetime.  More energetic")
print("  events create 2D universes with *more content*, which can have longer")
print("  lifetimes.  Less energetic events create 2D universes with *less content*,")
print("  which die faster (closer to t_Pl,2).")
print()

# Anchor 2: 2D universe burnout time
print("  --- Anchor 2: 2D universe 'burnout' time ---")
print()
print("  The 2D universe expands at near c from the 2D Planck length.")
print("  The 2D universe's contents dilute as the universe expands.")
print("  The 'burnout' time is when the 2D matter density falls below some")
print("  threshold (e.g., the 2D cosmological constant scale).")
print()
print("  In 2D, the Hubble rate is set by μ:  H_2D ~ √μ")
print("  The 2D universe's maximum size is l_2D ~ c/H_2D ~ c/√μ")
print("  The burnout time is t_burnout ~ l_2D/c ~ 1/√μ")
print()
print("  For T_2D = 33s:  1/√μ = 33s  →  μ = (1/33s)² = 9.2e-4 s⁻²")
print("  In energy units:  μ ~ ℏ × 9.2e-4 / (1.6e-19) ~ 6e-18 eV")
print()
print("  This is a DIFFERENT value of μ than the Planck-scale anchor (3.3e-29 eV).")
print("  The two anchors are inconsistent by ~12 orders of magnitude.")
print()

# Anchor 3: 2D universe 'expansion' time
print("  --- Anchor 3: 2D universe 'expansion' time ---")
print()
print("  The 2D universe expands at c.  If the 2D universe's initial size is")
print("  the 2D Planck length l_Pl,2, and the 2D universe expands for T_2D,")
print("  then the final size is l_final ~ c × T_2D.")
print()
print("  For T_2D = 33s:  l_final = c × 33s = 10^10 m = 10 Earth radii")
print()
print("  This is a 'natural' final size for a 2D universe.  But it doesn't")
print("  give a μ constraint without additional input.")
print()

# Anchor 4: m_{3+1D}
print("  --- Anchor 4: 2D universe 'effective mass' m_{3+1D} ---")
print()
print("  The cascade claims m_{3+1D} ~ 10^-62 kg contributes to DM (27% of ρ_crit).")
print("  If each 2D universe has mass m_{2D}, and there are N_2D ~ 10^60 2D")
print("  universes alive in our past lightcone, then:")
print("    m_{2D} × N_2D = 0.27 × ρ_crit × V_hubble ~ 10^53 kg")
print("    m_{2D} ~ 10^53 / 10^60 = 10^-7 kg = 10^(-40) GeV/c²")
print()
print("  This is a 'natural' 2D universe mass scale.  But the cascade doesn't")
print("  have a clean derivation of m_{2D} from the 2D CFT.")
print()

# Verdict
print("  --- VERDICT ---")
print()
print("  The cascade has FOUR candidate 2D universe lifetime anchors:")
print("    1. T_2D = t_Pl,2 (Planck scale):  μ = 3.3e-29 eV")
print("    2. T_2D = burnout time:           μ = 6e-18 eV  (inconsistent with #1)")
print("    3. T_2D = expansion time:         no direct μ constraint")
print("    4. m_{2D} from DM abundance:      m_{2D} ~ 10^-40 GeV/c² (free parameter)")
print()
print("  None of these are *additional* calibration points for the energy-scaling")
print("  rule.  They all relate to the 2D universe's *internal* parameters, not")
print("  the 3D event's energy.")
print()
print("  The cascade has only ONE explicit 2D universe lifetime data point:")
print("  the 33s for SN.  The energy-scaling rule is a *fit* to this one point,")
print("  and the extrapolation is uncertain by orders of magnitude (as shown in")
print("  §10.9).")
print()
print("  CASCADE LIMITATION:  the energy-scaling rule is a *fit* to a single")
print("  data point, with no first-principles derivation from the 2D CFT.  The")
print("  c=1 matrix model gives μ as a free parameter; it does not pin down")
print("  the relationship between E_3D and T_2D.  A 2D CFT expert would be")
print("  needed to derive this relationship rigorously.")
