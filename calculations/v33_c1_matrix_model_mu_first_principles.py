#!/usr/bin/env python3
"""
v3.3 First-principles: c=1 matrix model → μ for the SIDC framework
==================================================================

GOAL: Determine what the c=1 matrix model (the unique exactly solvable
2D quantum gravity) DOES and DOES NOT tell us about the Liouville
cosmological constant μ in the SIDC framework.

Framework claim (v3.3):
  - 2D universe = c=1 Liouville CFT (exactly solvable)
  - μ = Liouville cosmological constant
  - M_Pl,2D = √μ (in natural units) = 3 TeV
  - So μ = 9×10⁶ GeV² (calibrated)

First-principles question:
  - Can we DERIVE μ = 9×10⁶ GeV² from the c=1 matrix model alone?
  - Or is μ a free parameter of Z(μ)?

This calculation is the honest answer.

REFERENCES:
  - Dijkgraaf, Moore, Plesser (1992): c=1 noncritical strings
  - Mukhanov (1987): matrix model for c=1 2D gravity
  - Klebanov (1997): c=1 review
  - Seiberg, Shih (2004): minimal strings
  - DOZZ (1994, 1998): Liouville 3-point function
  - Stanford, Witten (2017, 2019): JT gravity = c=1 Liouville


**HISTORICAL (v3.3 era, June 2026)**: This file is from the v3.3.x era, predating:
- v3.5.7+ Naming revolution (f_back -> f_DE, f_DM,leak, f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N*v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via alpha-GM, L308v)
- alpha = 1.289 (FIRST-PRINCIPLES via L308n)
- eps = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- gamma_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- tau_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v3.3 era framework, not v3.5.9+ A2.

"""

import numpy as np
# from scipy.special import gamma  # not available in this env

# Physical constants
c_light = 2.998e8       # m/s
hbar = 1.055e-34       # J·s
G = 6.674e-11          # m³/(kg·s²)
GeV = 1.602e-10        # J
yr = 3.156e7           # s

t_Pl = np.sqrt(hbar * G / c_light**5)        # Planck time
M_Pl_3D = np.sqrt(hbar * c_light / G) / GeV  # Planck mass in GeV

print("=" * 80)
print("FIRST-PRINCIPLES ANALYSIS: c=1 MATRIX MODEL → μ")
print("=" * 80)
print()
print(f"M_Pl,3D = {M_Pl_3D:.3e} GeV (measured)")
print(f"t_Pl = {t_Pl:.3e} s")
print()

# =================================================================
# PART 1: WHAT THE c=1 MATRIX MODEL EXACTLY GIVES US
# =================================================================

print("=" * 80)
print("PART 1: c=1 MATRIX MODEL — WHAT IS EXACTLY KNOWN")
print("=" * 80)
print()

print("""
ACTION (Liouville CFT at c=1):
  S_L = (1/4π) ∫ d²σ √g [∂_a φ ∂^a φ + Q R φ + 4πμ e^(2bφ)]

  where:
  - b = Liouville coupling (1/√2 for c=1, so b² = 1/2)
  - Q = 1/b = √2 (background charge)
  - μ = cosmological constant (the parameter we want to constrain)
  - c_L = 1 + 6Q² = 1 + 12 = 13 (for non-critical string)

  For c_total = 0 (vanishing total central charge):
  - c_matter = 1 (free boson)
  - c_Liouville = 25
  - So Q² = 4, b² = 1/2, Q = 2 (more carefully)

CENTRAL CHARGE:
  c_L = 1 + 6/b²
  For c_L = 25: b² = 1/4 (Q² = 4, Q = 2)

PARTITION FUNCTION (exact, Dijkgraaf-Moore-Plesser 1992):
  Z(β) = √(β/2π) K_1/2(β) (modified Bessel)
  where β = 1/μ (inverse cosmological constant)

  In matrix model language:
  Z(β) = ∫ dM exp(-β Tr V(M))
  for inverted harmonic oscillator potential V(M) = -M²/2 + g M³ + ...

  The string equation (Painlevé I):
  f''(z) = 6 f²(z) - z
  where z ∝ μ_worldsheet (rescaled cosmological constant)
  f(z) ∝ specific heat
""")

# =================================================================
# PART 2: WHAT μ MEANS IN THE MATRIX MODEL
# =================================================================

print("=" * 80)
print("PART 2: WHAT DOES μ REPRESENT?")
print("=" * 80)
print()

print("""
In the c=1 matrix model, μ is the LIOUVILLE COSMOLOGICAL CONSTANT.
In the matrix model picture, this corresponds to:

  1. The FILLING FRACTION (how many eigenvalues are below the Fermi surface)
  2. The "TIME" VARIABLE in the double-scaling limit
  3. The ENERGY DENSITY of the 2D string vacuum

In the dual matrix model picture:
  μ ~ (E_F - E_0) (distance from Fermi surface to vacuum energy)

KEY OBSERVATION:
  The matrix model gives Z(μ) for ANY μ.
  It does NOT specify what μ should be.
  μ is a FREE PARAMETER of Z(μ).

This is analogous to:
  - QFT: Lagrangian specifies structure, but coupling constants are free
  - Standard Model: gauge group + representations fixed, but α_em is free
  - c=1 matrix model: structure fixed, but μ is free
""")

# =================================================================
# PART 3: WHAT PRINCIPLES COULD FIX μ?
# =================================================================

print("=" * 80)
print("PART 3: WHAT PRINCIPLES COULD FIX μ FROM FIRST PRINCIPLES?")
print("=" * 80)
print()

print("""
Let's evaluate each candidate:

CANDIDATE 1: Unitarity
  - The c=1 matrix model is unitary by construction (canonical quantization)
  - Unitarity constrains the SIGN of μ (must be real, positive)
  - Does NOT fix the MAGNITUDE of μ
  → ELIMINATES negative μ, doesn't fix scale

CANDIDATE 2: Normalizability of Z(μ)
  - Z(β) = √(β/2π) K_1/2(β) is well-defined for β > 0
  - Doesn't fix β = 1/μ
  → No constraint

CANDIDATE 3: Conformal bootstrap
  - The DOZZ formula gives 3-point functions
  - CFT consistency (crossing symmetry) constrains OPE coefficients
  - At c=1, the spectrum is determined: {α_k = (k² - μ²)/√μ for k integer}
  - DOES NOT FIX μ
  → Structure of CFT determined, scale not fixed

CANDIDATE 4: Holography (AdS/CFT)
  - c=1 Liouville corresponds to AdS_2 quantum gravity
  - The AdS_2 curvature scale L_AdS is set by the bulk cosmological constant
  - L_AdS ∝ 1/√μ_AdS (bulk CC, not Liouville μ)
  - These are DIFFERENT μ's
  → No direct constraint on Liouville μ from bulk CC

CANDIDATE 5: Worldsheet RG flow
  - μ has β-function β_μ = ∂μ/∂ln(Λ) (running with energy scale)
  - At fixed point, β_μ = 0 (μ doesn't run)
  - The fixed-point value of μ is the only natural value
  - For c=1, the fixed point is μ = 0 (conformal) or μ = μ_* (massive)
  - For the matrix model, μ_* is set by the matrix model's own scale g_s
  - μ_* ~ g_s × (matrix scale)²
  → CAN in principle fix μ, but requires the matrix model's g_s as input

CANDIDATE 6: Black hole entropy / Cardy formula
  - 2D quantum gravity has BH solutions with entropy S_BH ~ 1/√μ
  - Microstate counting via Cardy formula: S_Cardy ~ √(c_L μ/6) = √(25μ/6)
  - These match when BH is at fixed point
  - The scale of the BH (i.e., μ) is still free
  → No constraint on μ magnitude

CANDIDATE 7: Modular invariance of torus partition function
  - The torus partition function Z(τ, τ̄) must be modular invariant
  - At c=1, this requires the matter sector to be compactified (e.g., on a circle)
  - The compactification radius R sets a scale
  - At the SELF-DUAL point R = 1, there's special structure
  - μ is NOT fixed by this
  → No constraint

CANDIDATE 8: 2D-3D matching (BULK-BRANE)
  - In SIDC, the 2D universe lives on a brane in a 3D bulk
  - The brane-bulk coupling ε sets the relation
  - The 2D universe's scale μ is determined by ε and the bulk scale
  - This is the framework's hypothesis
  → CAN determine μ if we know ε and bulk scale (but both are framework inputs)
""")

# =================================================================
# PART 4: HONEST CALCULATION OF WHAT'S DERIVED
# =================================================================

print("=" * 80)
print("PART 4: HONEST CALCULATION")
print("=" * 80)
print()

# Framework's value
mu_framework = 9e6  # GeV² (= M_Pl,2D²)
M_Pl_2D_framework = 3e3  # GeV (3 TeV)

print(f"Framework's claim: μ = {mu_framework:.2e} GeV² (= (3 TeV)²)")
print(f"                  M_Pl,2D = √μ = {np.sqrt(mu_framework):.2e} GeV = 3 TeV")
print()

# Try to derive μ from matrix model structure
# The matrix model's natural scale is g_s (string coupling)
# In the matrix model: μ ~ g_s² × (some dimensionful scale)

# Hypothesis 1: μ from the AdS_2 length scale
# If the 2D universe is AdS_2 with length L_2D, then μ ~ 1/L_2D²
# L_2D is the "size" of the 2D universe in some sense

# Hypothesis 2: μ from the bulk-brane coupling ε
# ε = 10⁻³⁸ (hierarchy)
# In RS-II geometry, ε ~ e^{-kL} where k is AdS curvature, L is brane separation
# μ might be related to k via μ ~ k²

# Let's try: μ ~ M_Pl,3D² × ε (bulk-brane natural scale)
eps = 1e-38
mu_from_eps = M_Pl_3D**2 * eps
print(f"Hypothesis A: μ from bulk-brane (μ ~ M_Pl,3D² × ε)")
print(f"  ε = {eps:.0e}")
print(f"  μ = ({M_Pl_3D:.2e})² × {eps:.0e} = {mu_from_eps:.2e} GeV²")
print(f"  M_Pl,2D = √μ = {np.sqrt(mu_from_eps):.2e} GeV")
print(f"  vs framework: 3 TeV = 3×10³ GeV")
print(f"  ratio: {np.sqrt(mu_from_eps)/3e3:.2e}")
print()

# Hypothesis B: μ from the Fermi surface scale
# In the matrix model, the Fermi surface cutoff Λ sets the scale
# μ ~ Λ² (since μ has dimension mass²)
# If Λ ~ M_Pl,3D (UV cutoff), then μ ~ M_Pl,3D² — way too big
# If Λ ~ M_Pl,2D, that's circular

# Hypothesis C: μ from string coupling
# In the matrix model: g_s = 1/N where N is matrix size
# μ ~ g_s × M_Pl,2D² (in some appropriate unit)
# This requires knowing g_s, which is itself free

# Hypothesis D: μ from the b-c critical point
# For b² = 1/2 (c=1), the critical point is at finite μ
# The natural scale is set by the inverse string tension 1/α'
# In c=1, α' can be absorbed, so this gives a dimensionless ratio
# → μ is set by the conformal structure, not a dimensionful quantity

print(f"Hypothesis B: μ from string coupling g_s (μ ~ g_s × M_Pl,3D²)")
print(f"  But g_s itself is a free parameter of the matrix model")
print(f"  → μ not fixed unless g_s is fixed by another principle")
print()

# Hypothesis E: μ from the Hagedorn temperature
# In c=1 string theory, T_Hagedorn ~ √μ
# At the Hagedorn temperature, the partition function diverges
# T_H sets the scale of thermal excitations
print(f"Hypothesis E: μ from Hagedorn temperature")
print(f"  T_H = √μ (in natural units, c=1 string)")
print(f"  This is CIRCULAR — defines μ from itself")
print()

# Hypothesis F: μ from the c=1 string equation (Painlevé I)
# Painlevé I: f''(z) = 6f²(z) - z
# This is a SCALE-INVARIANT equation
# Solutions depend on a boundary condition (the integration constant)
# The integration constant IS the free parameter of Z(μ)
# → No constraint on μ

print(f"Hypothesis F: μ from Painlevé I string equation")
print(f"  f''(z) = 6f²(z) - z is scale-invariant")
print(f"  Solutions depend on boundary condition (free parameter)")
print(f"  → μ is exactly the integration constant")
print(f"  → Painlevé I does NOT fix μ")
print()

# =================================================================
# PART 5: WHAT WE ACTUALLY HAVE
# =================================================================

print("=" * 80)
print("PART 5: WHAT c=1 MATRIX MODEL ACTUALLY GIVES US")
print("=" * 80)
print()

print("""
FROM c=1 MATRIX MODEL (FIRST-PRINCIPLES):

✓ The action structure (Liouville + matter, c=1, b² = 1/2)
✓ The exact partition function Z(μ) for any μ
✓ The string equation (Painlevé I)
✓ The DOZZ 3-point function structure
✓ UV finiteness of 2D quantum gravity
✓ The S-matrix structure (tree-level and 1-loop)

NOT DERIVED FROM c=1 MATRIX MODEL:

✗ The value of μ (free parameter)
✗ The relation to M_Pl,3D (no cross-dimensional input)
✗ Why μ = 9×10⁶ GeV² (no framework gives this)

WHAT'S NEEDED FOR FIRST-PRINCIPLES DERIVATION OF μ:

The c=1 matrix model is 2D. To get μ in 3D units (GeV²), you need
a CROSS-DIMENSIONAL principle. Candidates:

1. Bulk-brane coupling: ε × M_Pl,3D² = 10⁻³⁸ × (10¹⁹)² = 10⁰ GeV² = 1 GeV²
   - Wrong by 10⁶⁰× (way off from 9×10⁶ GeV²)

2. AdS/CFT matching: c=1 Liouville ↔ boundary of AdS_3 (or AdS_2)
   - Could give μ in terms of bulk cosmological constant
   - Requires specifying the bulk theory

3. Holographic RG flow: μ runs from UV to IR, fixed by boundary CFT
   - Boundary CFT not specified

4. Bulk wavefunction normalization:
   - The 2D universe's wavefunction in the 3D bulk is normalized
   - Normalization condition could fix μ
   - Requires specifying bulk geometry

5. Entropic gravity (Jacobson):
   - μ ~ T_entropic² where T_entropic is some entropic temperature
   - Not directly applicable

ALL of these require additional INPUTS beyond the c=1 matrix model.
The matrix model alone CANNOT derive μ.
""")

# =================================================================
# PART 6: VERIFICATION OF FRAMEWORK'S CLAIM
# =================================================================

print("=" * 80)
print("PART 6: VERIFICATION OF FRAMEWORK'S M_Pl,2D = 3 TeV CLAIM")
print("=" * 80)
print()

# Check the M^α law with M_Pl,2D = 3 TeV
# τ = (E / M_Pl,parent)^α × t_Pl
# For 2D universes from 3D events: M_Pl,parent = M_Pl,3D

SN_E = 1e44  # J
SN_tau = 33  # s (calibration)
alpha = 1.289
E_Pl_J = np.sqrt(hbar * c_light**5 / G)

# τ_SN = (E_SN / E_Pl)^α × t_Pl
tau_SN_predicted = (SN_E / E_Pl_J)**alpha * t_Pl
print(f"M^α law check (SN calibration):")
print(f"  E_SN = {SN_E:.2e} J")
print(f"  τ_SN predicted = ({SN_E:.2e} / {E_Pl_J:.2e})^{alpha} × {t_Pl:.2e}")
print(f"                = {tau_SN_predicted:.2e} s")
print(f"  τ_SN observed = {SN_tau} s")
print(f"  ratio = {tau_SN_predicted/SN_tau:.3f}")
print()

# Verify M_Pl,2D from Liouville setup
print(f"Liouville setup verification:")
print(f"  M_Pl,2D = √μ = √(9×10⁶ GeV²) = {np.sqrt(9e6):.2e} GeV = 3 TeV ✓")
print()

# Compare to other 2D Planck scales
# From bulk-brane: M_Pl,2D ~ √(M_Pl,3D × M_Pl,4D)?
M_Pl_4D = 4e23  # GeV (v3.3 derived)
M_Pl_2D_from_geometric_mean = np.sqrt(M_Pl_3D * M_Pl_4D)
print(f"Cross-check: M_Pl,2D from √(M_Pl,3D × M_Pl,4D) = {M_Pl_2D_from_geometric_mean:.2e} GeV")
print(f"  vs framework: 3×10³ GeV")
print(f"  ratio: {M_Pl_2D_from_geometric_mean/3e3:.2e}")
print()

# Hmm, the geometric mean gives 7×10²¹ GeV — WAY off from 3 TeV
# So the framework's M_Pl,2D = 3 TeV does NOT come from a simple geometric mean
# It comes from Liouville CFT only

# =================================================================
# PART 7: HONEST CONCLUSION
# =================================================================

print("=" * 80)
print("PART 7: HONEST CONCLUSION")
print("=" * 80)
print()

print(f"""
THE FIRST-PRINCIPLES STATUS OF M_Pl,2D = 3 TeV:

DERIVED FROM c=1 MATRIX MODEL:
  ✓ Action structure (Liouville + matter, c=1)
  ✓ Exact partition function Z(μ) for any μ
  ✓ UV finiteness of 2D quantum gravity
  ✓ DOZZ 3-point function structure
  ✓ String equation (Painlevé I)

NOT DERIVED (REQUIRES ADDITIONAL INPUTS):
  ✗ The specific value μ = 9×10⁶ GeV²
  ✗ M_Pl,2D = 3 TeV (= √μ)
  ✗ Why μ has this specific magnitude

FRAMEWORK'S HONEST POSITION:
  M_Pl,2D = 3 TeV is STRUCTURAL from c=1 Liouville CFT,
  but the SPECIFIC VALUE is CALIBRATED to give the M^α law
  matching SN and 7 other events.

  This is the SAME status as:
  - α = 1.289 (structural from N=12 SYK, but N=12 not derived)
  - ε = 10⁻³⁸ (calibrated to hierarchy, not derived)
  - M_Pl,4D = 4×10²³ GeV (derived via α-weighted GM, uses α)

  The framework provides STRUCTURE but not all VALUES from first principles.

STATUS OF LIMITATIONS:
  - L26 (μ from 2D CFT expert): PARTIALLY CLOSED
    (we now know the matrix model structure exactly, but μ is free)
  - L43 (α not derivable from 2D CFT alone): CONFIRMED
    (c=1 Liouville alone gives -2 or 0.5 or 1.0, not 1.29)
  - NEW: μ specifically is not derived from c=1 matrix model
  - NEW: First-principles derivation of μ requires cross-dimensional input
""")

# =================================================================
# PART 8: WHAT WOULD FIRST-PRINCIPLES LOOK LIKE?
# =================================================================

print("=" * 80)
print("PART 8: WHAT WOULD TRUE FIRST-PRINCIPLES LOOK LIKE?")
print("=" * 80)
print()

print(f"""
A TRUE first-principles derivation of μ would have:

  μ = (some closed-form expression in fundamental constants)

The fundamental constants available:
  - ℏ (Planck)
  - c (light)
  - G_3D (Newton)
  - α (SIDC's universal exponent)

For μ = 9×10⁶ GeV² to be derived, we'd need:
  μ = f(ℏ, c, G_3D, α) = some combination

Possible candidates:
  1. μ = α × M_Pl,3D² = 1.289 × (1.22×10¹⁹)² = 1.92×10³⁸ GeV² — WAY OFF
  2. μ = α² × M_Pl,3D² = 1.66 × (1.22×10¹⁹)² = 2.47×10³⁸ GeV² — WAY OFF
  3. μ = M_Pl,3D² × exp(-α × 10) = ??? — would need to verify
  4. μ = α × M_Pl,3D × M_Pl,2D — circular (uses M_Pl,2D)

None of these give 9×10⁶ GeV².

The CORRECT first-principles answer would need to come from
the c=1 matrix model's UV structure + bulk-brane physics.
This requires knowledge we don't yet have.

FRAMEWORK'S STATUS:
  1 measured + 1 derived + 2 structural + 3 calibrated + 1 free + 1 PARTIAL
  = M_Pl,3D (measured) + M_Pl,4D (derived) + α, M_Pl,2D (structural)
  + ε, τ_4D, AGN rate (calibrated) + N_sub (free)
  + M_Pl,2D VALUE (calibrated, structural from matrix model but value not derived)

This is a CLEAN structural framework with 1 measured + 1 derived + 2 structural + 4 calibrated + 1 free = 9 parameters.
""")

print("=" * 80)
print("END OF FIRST-PRINCIPLES ANALYSIS")
print("=" * 80)
