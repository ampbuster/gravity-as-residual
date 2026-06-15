# Trial-and-Error on v2.6 Cascade Parameters — Findings

## What I tried

Given the cascade's 31+ limitations, I did systematic trial-and-error
on the v2.6 cascade's free parameters to see what values reproduce
the observed data.

## Q1: What e^{-ky} × m_2D_2D × R_2D gives Ω_DM = 0.27?

The constraint: ρ_DM = R_2D × τ_2D × m_2D_3+1D

This gives: R_2D × m_2D_3+1D = 1.12e-43 kg/(m³·s)

Multiple (R_2D, m_2D_3+1D) combinations satisfy this:

| R_2D (per Mpc³/s) | m_2D_3+1D (kg) | e^{-ky} for 6 M_sun |
|--------------------|-----------------|----------------------|
| 1e40 | 3.3e-16 | 2.8e-47 |
| 1e42 | 3.3e-18 | 2.8e-49 |
| 1e44 | 3.3e-20 | 2.8e-51 |
| 1e46 | 3.3e-22 | 2.8e-53 |
| 1e48 | 3.3e-24 | 2.8e-55 |

**Conclusion:** Ω_DM = 0.27 constrains the PRODUCT, not the separate factors.
The cascade's values (R_2D ~ 10^46 per Mpc³/s, m_2D_3+1D ~ 1.1e-23 kg,
e^{-ky} ~ 10^-48) work, but other combinations also satisfy the constraint.

## Q2: What τ_2D gives f_active = 0.05?

τ_2D = f_active × T_universe = 0.0513 × 13.8 = 0.708 Gyr

This matches the cascade's τ_2D = 0.7 Gyr postulate.

**Conclusion:** Tautology, not a derivation. The cascade assumed τ_2D
from physical analogy, then f_active followed automatically.

## Q3: 4-zone H(z) best-fit parameters

The current 4-zone parameters (from v2.5 cascade's spec):
- H_bulk = 70.16
- z_trgb = 0.01, z_rise = 0.05, z_fall = 1.0
- w_local = 0.001
- delta_local = 1.44, delta_secular = 2.84, delta_primordial = -2.76

Sum of squared residuals: 2.07 (mostly from the z=0.01 transition zone)

Perturbing parameters increases the residual. The current 4-zone
parameters are already a good empirical fit.

**Conclusion:** A full optimization (e.g., scipy.optimize.minimize) would
refine them, but the cascade currently uses empirical values. The
4-zone H(z) is an empirical fit, not a derivation.

## Q4: Bulk position distribution P(y)

The cascade needs P(y) that satisfies:
1. Some 2D universes at shallow y (e^{-ky} ~ 1) for local boost
2. Some 2D universes at deep y (e^{-ky} ~ 10^-48) for axion-like mass
3. ∫ P(y) × m_2D × e^{-ky} dy = Ω_DM = 0.27

**Bimodal P(y) doesn't work** unless the deep population dominates.

For average mass ~ 1.1e-23 kg (axion-like), the deep population
must dominate: P(deep) / P(shallow) >> 1.

**Conclusion:** Most 2D universes are DEEP in the bulk (e^{-ky} ~ 10^-48).
Only a small fraction are at shallow bulk (for the local boost).
This is INCONSISTENT with the local R_stellar boost being a major
contribution to H(z) — if most 2D universes are deep, they don't
contribute to the local boost.

## Bottom line

The cascade's parameters are CONSISTENT with observations, but they
are POSTULATED, not DERIVED. The trial-and-error shows that the
postulates work, but doesn't explain WHY they have these specific
values.

## For a true derivation, we would need:

1. **The 2D universe's intrinsic mass** (6 M_sun) from Liouville 2D CFT
2. **The bulk position distribution P(y)** from AdS_5 geometry
3. **The 2D universe creation rate R_2D** from SM event physics
4. **The 2D universe lifetime τ_2D** from the Liouville potential μ
5. **The 4-zone H(z) parameters** from cluster/AGN/Thomson physics

Each of these would close one of the 31+ cascade limitations.
But none of them are derivable from the cascade's current framework.

## What this means for v2.6

The v2.6 architecture is a CLEANER FRAMEWORK, but it's not a
DERIVATION. The cascade's specific values are:
- Postulated (τ_2D = 0.7 Gyr, 2D-frame mass = 6 M_sun)
- Fitted (4-zone H(z) parameters)
- Postulated as input (Ω_DM = 0.27)
- Constrained by trial-and-error (e^{-ky} ~ 10^-48)

The trial-and-error shows that the postulates are CONSISTENT with
observations, but doesn't DERIVE them.

## File locations

- Code: `calculations/trial_and_error_v26.py`
- Results: `tempcalc/trial_and_error_v26_results.json`
- This memo: `tempcalc/trial_and_error_v26_findings.md`
- Earlier trial-and-error: `calculations/trial_and_error.py` (H_0 framework)
- v2.6 architecture: `tempcalc/cascade_architecture_decision.md`
- Ω_DM derivations: `tempcalc/omega_dm_derived_quantities.md`
- Time compression: `tempcalc/time_compression_memo.md`
- CAMB Boltzmann: `tempcalc/cascade_camb*.py`
