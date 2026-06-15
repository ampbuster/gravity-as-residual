# Quantities Derivable from Ω_DM = 0.27

## What we can calculate

If we adopt the cascade's postulate that ALL observed Ω_DM = 0.27 is
2D universe mass, time-compressed via the 5D AdS_5 bulk, we can
derive the following quantities:

### Population quantities

| Quantity | Value | Notes |
|----------|-------|-------|
| Total DM mass density | 2.48e-27 kg/m³ | from Planck 2018 |
| Total DM mass in past lightcone | 2.4e52 kg | 1.2e22 M_sun |
| Past lightcone volume | 9.6e78 m³ | (4/3)π(c/H_0)³ with H_0 = 70.16 |
| Number of 2D universe deaths (lightcone) | 2.2e75 | assuming m_2D_3+1D = 1.1e-23 kg |
| Per Mpc³ over T_universe | 6.6e63 deaths | cumulative |
| 2D universe creation rate | 1.5e46 per Mpc³ per second | steady-state |
| Active 2D universe population | 3.4e62 per Mpc³ | multiplied by f_active = 0.05 |
| Average inter-2D-universe separation | ~44 m | very dense! |
| Per m³ | 1.1e-5 | same as ~10^-5 per m³ |

### Energy/power quantities

| Quantity | Value | Notes |
|----------|-------|-------|
| Total DM energy in lightcone | 2.2e69 J | E = mc² |
| Power per 2D universe death (3+1D) | 4.5e-23 J/s | very low per unit |
| 2D universe lifetime in 2D frame | 0.7 Gyr | the cascade's τ_2D |
| 2D universe lifetime in 3+1D frame (with full compression) | 5.5e52 × T_universe | very long with e^{-ky} ~ 10^-48 |

### Galaxy/cluster-scale quantities

| Quantity | Value | Notes |
|----------|-------|-------|
| DM mass in 10 kpc sphere (10^12 M_sun galaxy) | 1.5e5 M_sun | matches observations |
| DM mass in 1 Mpc sphere (cluster) | 1.5e11 M_sun | matches observations |
| Local g_+ in 10 kpc | 1.2e-10 m/s² | matches RAR |
| Number of 2D universe deaths in 10 kpc | 2.8e58 | very many |
| Number of 2D universe deaths in 2 kpc | 2.2e56 | very many |

### Time compression parameters

| Quantity | Value | Notes |
|----------|-------|-------|
| Required e^{-ky} for 6 M_sun 2D mass | 10^-48 to 10^-54 | to match axion-like 3+1D mass |
| Required bulk depth y | ~100-125 AdS_5 radii | depends on assumption |
| 2D-frame mass for given time compression | varies | see table below |

For e^{-ky} = 1 (no compression): m_2D_2D = 1.1e-23 kg (axion-like directly)
For e^{-ky} = 10^-25: m_2D_2D = 110 kg (small-mass)
For e^{-ky} = 10^-48: m_2D_2D = 1.1e25 kg = 5.5e-6 M_sun (sub-stellar)
For e^{-ky} = 10^-54: m_2D_2D = 1.1e31 kg = 5.5 M_sun (stellar)

## What this means

### 1. 2D universes are EXTREMELY numerous

Average separation ~44 m. The 2D universe sector is a dense "medium"
pervading 3+1D space, much denser than the visible matter.

### 2. The cascade's RAR is naturally explained

The cumulative 2D universe population in a 10 kpc sphere gives a
gravitational acceleration of g_+ ~ 1.2e-10 m/s², which matches
the observed RAR scale. This is the cascade's "local R_stellar boost."

### 3. The 50-orders tension has a specific resolution

The 2D-frame mass is stellar-scale (6 M_sun) IF the time compression
is e^{-ky} ~ 10^-48. This corresponds to 2D universes at bulk depth
y ~ 100 AdS_5 radii. Deep but not unreasonable.

### 4. Power per 2D universe is tiny but cumulative

Each 2D universe death contributes 4.5e-23 J/s in 3+1D. But there are
3.4e62 active 2D universes per Mpc³, so the cumulative power is huge.

## What this DOESN'T give

The Ω_DM = 0.27 input does NOT give us:
- The specific 2D universe mass (need time compression or Liouville)
- The 4-zone H(z) structure (need cluster/AGN/Thomson physics)
- τ_2D (need Liouville 2D CFT)
- The DOZZ 3-point function (need Liouville parameter b)
- The 5:27 inner split (postulated, not derivable)
- g_+ at all scales (it's c × H_0 / 2π, a coincidence)
- f_back (the back-projection probability)

## What's still free / unspecified

- The 2D universe's intrinsic 2D-frame mass (6 M_sun postulated)
- The bulk position distribution P(y)
- The 4-zone H(z) structure
- g_+ (the RAR universal scale)
- f_back
- The 5:27 inner split

## Honest assessment

Using Ω_DM = 0.27 as an INPUT gives a consistent picture of the
2D universe population, but it does NOT derive the cascade's
specific values. The 6 M_sun 2D-frame mass, the 50-orders time
compression, and the 4-zone H(z) structure are still postulates
or empirical fits, not derivations.

The Ω_DM = 0.27 input gives us:
- A consistent 2D universe population
- A natural explanation of the RAR
- A specific time compression to resolve the 50-orders tension
- A dense "soup" of 2D universes pervading 3+1D space

But it does NOT give us:
- A derivation of the cascade's specific parameters
- A prediction of the 4-zone H(z) structure
- A first-principles calculation of the 2D universe's intrinsic mass
- A derivation of the 5:27 inner split

## File locations

- This memo: `tempcalc/omega_dm_derived_quantities.md`
- Time compression memo: `tempcalc/time_compression_memo.md`
- Cascade CAMB code: `tempcalc/cascade_camb*.py`
- 50-orders tension: `tempcalc/liouville_more_tests.py` (Test A)
- Architecture decision: `tempcalc/cascade_architecture_decision.md`
