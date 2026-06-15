# Deriving the Cascade's Likely Parameters

## Strategy

1. **Drop the 30 Gyr assumption** (it was a guess)
2. **Use 33 s in 3+1D as the empirical constraint** (from ℓ/c rule)
3. **Treat m_2D_2D and e^{-ky} as free parameters**
4. **Find CONSISTENT values** that satisfy all cascade constraints

## Constraints (FIXED)

| Quantity | Value | Source |
|----------|-------|--------|
| τ_3+1D | 33 s | Empirical ℓ/c mapping |
| m_2D_3+1D | 1.1×10^-23 kg | Axion-like target |
| Ω_DM | 0.27 | Planck 2018 |
| ρ_DM | 2.5×10^-27 kg/m³ | Derived from H_0 = 70.16 |
| k | ~10^19 GeV | RS-II natural |
| Raw 2D rate | 1.9×10^65 s^-1 | SN+AGN events |

## Free parameters (POSTULATES)

| Quantity | Recommended | Status |
|----------|-------------|--------|
| m_2D_2D | M_Pl ~ 2×10^-8 kg | Free (postulate) |
| e^{-ky} | 5.5×10^-16 | Free (Karch-Randall natural) |
| α × \|C\|² | ~10^-7 | Free (bulk-brane coupling) |

## Derived quantities

| Quantity | Value | Status |
|----------|-------|--------|
| m_2D_3+1D | 1.1×10^-23 kg | ✓ Axion-like (by construction) |
| τ_2D | 1.9 Gyr | Derived (33 s / e^{-ky}) |
| n_2D | 2.3×10^-4 m^-3 | Derived (10 m separation) |
| Total 2D in obs universe | 10^75 | Derived |
| Bulk position y | 34.7/k = 6.8×10^-34 m | Derived |
| α × \|C\|² | ~10^-7 | Free (matches Ω_DM) |

## The f_active discovery

**The cascade's f_active = 0.05 is WRONG.**

For τ_3+1D = 33 s and T_universe = 13.8 Gyr:
- f_active = τ_3+1D / T_universe = 33 s / (13.8 Gyr)
- f_active = 7.6×10^-17 (NOT 0.05!)

The cascade's f_active = 0.05 was based on the assumption that 2D universes
live for 30 Gyr in 2D (which would give a 2D-frame lifetime long enough
to have 5% active). But with 33 s empirical lifetime, the 2D universe
DIE almost immediately, and the active fraction is essentially zero.

**Wait, this doesn't quite work.** Let me think again.

f_active is the fraction of 2D universes that are STILL ALIVE in 3+1D.

If τ_3+1D = 33 s:
- A 2D universe is created and lives for 33 s in 3+1D
- After 33 s, it dies
- So at any given moment, only the most recent 33 s of creations are alive
- f_active = (number alive) / (number ever created) = 33 s / T_universe

This gives f_active ~ 10^-17, NOT 0.05.

## The 5/27/68 reinterpretation

With the corrected f_active ~ 10^-17:
- "Active" 2D universes contribute 10^-17 × total
- "Cumulative deaths" contribute (1 - 10^-17) × total

The cascade's claim that 5% of DM is from "active" 2D universes and 95% is
from "cumulative deaths" was based on the 30 Gyr assumption.

With 33 s empirical lifetime, the split is:
- 5% active + 95% cumulative (cascade default, 30 Gyr)
- 10^-17 active + ~1 cumulative (33 s empirical)

The 5/27/68 split in the paper needs to be re-examined.

## What the cascade should do

The cascade has two options:

### Option 1: Keep 33 s empirical mapping
- f_active ~ 10^-17 (negligible active)
- All DM is "cumulative deaths"
- The 5% / 95% active/cumulative split goes away
- The 5/27/68 split needs revision

### Option 2: Keep f_active = 0.05 (5% active, 95% cumulative)
- Then τ_3+1D is not 33 s
- τ_3+1D = 0.05 × T_universe = 0.05 × 13.8 Gyr = 0.69 Gyr
- This contradicts the 33 s empirical mapping
- 0.69 Gyr is much longer than 33 s

These are inconsistent. The cascade must choose:
- The 33 s empirical mapping (ℓ/c rule) — strong
- The 5%/95% active/cumulative split — based on 30 Gyr postulate

The 33 s is more empirical, so it should win.

## Recommended framework (final)

| Quantity | Value | Status |
|----------|-------|--------|
| τ_3+1D | 33 s | Empirical (KEEP) |
| m_2D_2D | M_Pl | Postulate (free) |
| e^{-ky} | 5.5×10^-16 | Postulate (free) |
| m_2D_3+1D | 1.1×10^-23 kg | Derived (axion-like) |
| τ_2D | 1.9 Gyr | Derived (33 s / e^{-ky}) |
| n_2D | 2.3×10^-4 m^-3 | Derived |
| f_active | ~10^-17 | Derived (33 s / T_universe) |
| α × \|C\|² | ~10^-7 | Postulate (free) |

**The 5/27/68 split needs revision.** The cascade should be honest:
- 5% ordinary matter (postulated)
- 27% dark matter (input from Planck)
- 68% dark energy (input from Planck)

The "5% from active 2D universes" is NOT supported by the empirical 33 s lifetime.

## The 6 M_sun mistake

The cascade's earlier postulates (m_2D_2D = 6 M_sun, τ_2D = 30 Gyr, e^{-ky} = 10^-54)
were a CHOICE, not derived. They are ONE POSSIBLE parameter set, but:
- They conflict with the 33 s empirical mapping
- They require 2D universes to be eternal in 3+1D (τ_3+1D = 7×10^53 Gyr)
- They make f_active = 1.0, not 0.05
- They require m_2D_2D to be 6 M_sun, which has no derivation

The recommended parameter set is simpler and more consistent:
- m_2D_2D = M_Pl (Planck mass, natural in 2D CFT)
- e^{-ky} = 5.5×10^-16 (Karch-Randall natural scale)
- τ_2D = 1.9 Gyr (reasonable 2D lifetime)
- τ_3+1D = 33 s (empirical)
- f_active ~ 10^-17 (negligible)

## Files

- This memo: `tempcalc/derive_cascade_parameters_findings.md`
- Derivation script: `tempcalc/derive_cascade_parameters.py`
- Trial-and-error v1: `tempcalc/trial_and_error_2d_universe.py`
- Trial-and-error v2: `tempcalc/trial_and_error_2d_v2.py`

## Bottom line

**The cascade's earlier 6 M_sun + 30 Gyr + 10^-54 combination was an arbitrary choice**, not derived. The 30 Gyr postulate conflicted with the 33 s empirical mapping by 38 orders of magnitude.

**A simpler, more consistent parameter set exists:**
- m_2D_2D = M_Pl
- e^{-ky} = 5.5×10^-16
- τ_2D = 1.9 Gyr
- τ_3+1D = 33 s
- f_active ~ 10^-17 (negligible)

**The 5/27/68 split in the paper needs revision.** The 5% "active" contribution is NOT supported by the 33 s empirical lifetime.
