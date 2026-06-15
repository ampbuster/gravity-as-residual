# Trial-and-Error on 2D Universe Mass and Lifetime

## Summary

The cascade's two main unconstrained postulates are:
- 2D universe mass m_2D_2D (in 2D frame)
- 2D universe lifetime τ_2D (in 2D frame)

This memo summarizes a systematic trial-and-error to find values consistent
with the cascade's other constraints.

## The trial-and-error script

`tempcalc/trial_and_error_2d_universe.py` does 7 calculations:

### Q1: Required e^{-ky} for given m_2D_2D and target m_2D_3+1D

For target 3+1D mass m_2D_3+1D = 1.1e-23 kg (axion-like):

| m_2D_2D | e^{-ky} required | y (in 1/k) |
|---------|------------------|------------|
| 1.1e-23 kg (axion) | 1 (no compression) | 0 |
| 1e-15 kg | 10^-8 | 18 |
| 1e-8 kg (M_Pl) | 10^-15 | 34 |
| 1 kg | 10^-23 | 53 |
| 1e10 kg | 10^-33 | 76 |
| 1e20 kg | 10^-43 | 99 |
| 1e30 kg | 10^-53 | 122 |
| 1.2e31 kg (6 M_sun) | 10^-54 | 124 |

**Honest finding:** Many (m_2D_2D, e^{-ky}) pairs give the right 3+1D mass.
The cascade's choice (6 M_sun, e^{-ky}=10^-54) is ONE valid choice.

### Q2: Bulk position y from e^{-ky}

y = -log(e^{-ky}) / k

For natural RS-II (k = M_Pl, 1/k = 2e-35 m):
- e^{-ky} = 1: y = 0
- e^{-ky} = 10^-15: y = 34/k = 7e-34 m
- e^{-ky} = 10^-32: y = 74/k = 1.5e-33 m
- e^{-ky} = 10^-48: y = 110/k = 2.2e-33 m
- e^{-ky} = 10^-54: y = 124/k = 2.4e-33 m

**Honest finding:** y is a Planck-scale length, NOT 2 kpc.
2 kpc is WAY bigger than any natural AdS_5 length.

### Q3: Time dilation from 2D to 3+1D

dτ_2D = e^{-ky} dt_4D
τ_3+1D = τ_2D / e^{-ky}

For τ_2D = 0.7 Gyr (cascade postulate):
- e^{-ky} = 1: τ_3+1D = 0.7 Gyr
- e^{-ky} = 10^-15: τ_3+1D = 7e14 Gyr
- e^{-ky} = 10^-32: τ_3+1D = 7e31 Gyr
- e^{-ky} = 10^-54: τ_3+1D = 7e53 Gyr

**KEY ISSUE:** For e^{-ky} = 10^-54, τ_3+1D = 7e53 Gyr.
The universe is only 13.8 Gyr old, so 2D universes NEVER DIE in 3+1D.

### Q4: Active 2D universe population

n_2D = ρ_DM / m_2D_3+1D

| m_2D_3+1D (kg) | n_2D (m⁻³) | separation (m) |
|----------------|-----------|----------------|
| 1.1e-23 | 2.3e-4 | 16 |
| 1e-15 | 2.5e-12 | 7e3 |
| 1e-8 | 2.5e-19 | 1.6e6 |
| 1 | 2.5e-27 | 7e8 |
| 1e10 | 2.5e-37 | 1.6e12 |
| 1e20 | 2.5e-47 | 3.4e15 |
| 1e30 | 2.5e-57 | 7e18 |
| 1.2e31 (6 M_sun) | 2.1e-58 | 1.7e19 |

**Honest finding:** For axion-like 3+1D mass, ~10 m separation.
For 6 M_sun 3+1D mass, ~10^19 m = ~1 kpc separation (galaxy scale!).

### Q5: Cumulative 2D universe deaths over T_universe

Raw 2D rate: 1.9e65 s⁻¹ (SN rate × events/SN above E_crit)

For T_universe = 13.8 Gyr:

| \|C\|²_Dozz | N_cumulative | Ω_equiv (3+1D, with e^{-ky}=10^-54) |
|------------|--------------|--------------------------------------|
| 0.28 | 2.3e82 | ~10^21 too small |
| 1 | 8.2e82 | ~10^21 too small |
| 8.2 | 6.7e83 | ~10^22 too small |
| 18 | 1.5e84 | ~10^22 too small |
| 31 | 2.5e84 | ~10^22 too small |
| 46 | 3.8e84 | ~10^22 too small |

**Honest finding:** |C|² × raw rate gives ~10^82 over T_universe.
But in 3+1D, 2D universes never die (τ_3+1D >> T_universe).
So "cumulative deaths" is the same as "active population".

### Q6: Grid search for consistent (m_2D, τ_2D)

Many combinations work. The cascade's choice (6 M_sun, 0.7 Gyr) is
ONE valid choice, not unique.

### Q7: A simple consistent set of postulates

Tested 3 trials:
- m_2D_2D = M_Pl, τ_2D = 1s: τ_3+1D = 6e7 yr (too short)
- m_2D_2D = M_Pl, τ_2D = 10^15 s: τ_3+1D = 6e13 Gyr (too long)
- m_2D_2D = 6 M_sun, τ_2D = 0.7 Gyr: τ_3+1D = 7e53 Gyr (eternal in 3+1D)

## The KEY ISSUE: 2D universes never die in 3+1D

For the cascade's default values (m_2D_2D = 6 M_sun, e^{-ky} = 10^-54):
- τ_2D = 0.7 Gyr (2D frame)
- τ_3+1D = 0.7 Gyr / 10^-54 = 7e53 Gyr (3+1D frame)
- T_universe = 13.8 Gyr

**τ_3+1D >> T_universe, so 2D universes NEVER DIE in 3+1D.**

This creates a paradox:
- The cascade distinguishes "active" (5%) and "cumulative" (95%) 2D universes
- But if 2D universes never die, "cumulative" = "active" (f_active = 1.0)
- The cascade's f_active = 0.05 is INCONSISTENT with the time dilation

## Possible resolutions

### (a) Specify τ_2D as 3+1D-frame lifetime (not 2D-frame)
- If τ_2D = 0.7 Gyr is in 3+1D, then 2D-frame lifetime is 0.7 Gyr × e^{ky}
- This is consistent with most 2D universes being dead in 3+1D
- BUT contradicts the explicit "2D frame" label in the cascade

### (b) Accept f_active = 1.0
- "Cumulative deaths" = "active population"
- All 2D universes are still alive in 3+1D
- f_active = 1.0, not 0.05
- The cascade's distinction is removed

### (c) Add new physics to make 2D universes die in 3+1D
- Maybe 2D universe death is triggered by some 3+1D event
- Not from natural 2D lifetime, but from 3+1D interactions
- This is NEW PHYSICS, not currently in the cascade

## What this means for the cascade

The cascade needs to clarify:
- Is τ_2D = 0.7 Gyr in 2D frame or 3+1D frame?
- If 2D frame: f_active = 1.0, "cumulative = active"
- If 3+1D frame: 2D-frame lifetime is 0.7 Gyr × 10^54 (long, but not eternal)
- Either way, the cascade's f_active = 0.05 needs justification

This is a NEW limitation:
- L35 (NEW): 2D universe lifetime is ambiguous (2D vs 3+1D frame)
- L36 (NEW): f_active = 0.05 is INCONSISTENT with time dilation
- The cascade needs to resolve this ambiguity

## Honest conclusion

The cascade's main remaining postulates are:
- 2D universe mass m_2D_2D = 6 M_sun (still a postulate)
- 2D universe lifetime τ_2D = 0.7 Gyr (still a postulate, ambiguous frame)
- f_active = 0.05 (INCONSISTENT with time dilation)
- e^{-ky} = 10^-54 (corresponds to 2D mass + axion-like 3+1D mass)

These are honestly documented in the paper. The cascade can still work
with these postulates, but the time dilation issue needs to be addressed.

## File locations

- This memo: `tempcalc/trial_and_error_2d_universe_findings.md`
- Trial-and-error script: `tempcalc/trial_and_error_2d_universe.py`
- 2D universe mass and lifetime memo: `tempcalc/omega_dm_derived_quantities.md`
- Time compression memo: `tempcalc/time_compression_memo.md`
- Karch-Randall: `tempcalc/karch_randall_2d_universes.py`
- RS-II calculations: `tempcalc/rs_ii_calculations.py`

## Bottom line

The cascade's 2D universe mass (6 M_sun) and lifetime (0.7 Gyr) are
postulates. The time dilation τ_3+1D = τ_2D / e^{-ky} = 7e53 Gyr means
2D universes never die in 3+1D. This is INCONSISTENT with the cascade's
f_active = 0.05 (active vs cumulative). The cascade needs to clarify
or revise its f_active framework.
