# v2.7 Calculations — RS-II + Liouville + Boltzmann + Event Spectrum

These calculations are from the v2.7 era of the cascade, focused on:
- Testing the cascade's 5D framework against standard RS-II physics
- Testing the 2D universe sector with Karch-Randall + Liouville
- Running CAMB with cascade modifications
- Computing the 2D universe population spectrum
- Deriving the cascade's likely parameters
- Deriving g_+ and CMB predictions

## Files

| File | Description |
|------|-------------|
| `v27_rs_ii_calculations.py` | 7 RS-II calculations (brane tension, Newton's law, hierarchy, 2 kpc, Karch-Randall, 2D universe population, 54-orders tension) |
| `v27_karch_randall_2d_universes.py` | 5 Karch-Randall calculations (2+1D Planck mass, 2D universe mass, density, 2 kpc, event rate) |
| `v27_cascade_camb_full.py` | 5 CAMB calculations (baseline ΛCDM, extra-DM, time compression, back-reaction, H_0 = 70.16) |
| `v27_rs_ii_liouville_boltzmann.py` | 6 combined analytical calculations (G_4, 2D universe mass, lifetime, warp factor, AdS/CFT, creation rate) |
| `v27_derive_cascade_parameters.py` | 7-questions parameter derivation (e^{-ky} for various m_2D, y, time dilation, n_2D, cumulative, grid search, simple set) |
| `v27_trial_and_error_2d_universe.py` | 7-questions trial-and-error on 2D universe mass and lifetime |
| `v27_2d_universe_population_spectrum.py` | 26 event types (SN, AGN, BH, NS, GRBs, X-ray bursts, etc.) with Ω_DM contribution |
| `v27_cascade_g_plus_derivation.py` | 5 approaches to derive g_+ from cascade (c × H_0/2π, galaxy properties, 2D universe population, 2D CFT, natural scales) |
| `v27_cascade_cmb_anisotropy.py` | 4 CMB questions (2D universe population at z=1100, acoustic peak, damping tail, specific predictions) |

## Key Findings

### From RS-II calculations
- 5D AdS_5 framework is STANDARD (no novelty)
- Graviton localization, brane tension, Newton's law, hierarchy all automatic
- Karch-Randall provides framework for 2+1D 2D universes
- 2 kpc is NOT a natural AdS_5 scale (k ~ 1e-19 GeV would be needed, unphysical)
- 2D universe mass is the Liouville value, not M_Pl_3
- 54-orders tension is partially mitigated by Karch-Randall (to ~15 orders)

### From Liouville + Karch-Randall
- G_4 is from RS-II; 2D universes add to M_eff, not G
- 2D universe mass from Liouville DOZZ is ~10^-8 kg, NOT 6 M_sun
- 2D universe lifetime from Liouville 1/√μ is way too fast, NOT 30 Gyr
- AdS/CFT gives qualitative interpretation (DM=IR modes, DE=UV vacuum)
- 2D universe creation rate = rate_SN × |C|²_Dozz × α

### From CAMB
- Standard ΛCDM reproduces Planck 2018 (ℓ_peak=220, age=13.8 Gyr)
- Cascade as extra-DM is INDISTINGUISHABLE from ΛCDM
- Time compression is a LABEL on 2D universe mass, no new H(z) effect
- 2D universe back-reaction on bulk is negligible
- H_0 = 70.16 with Planck-like densities gives intermediate CMB peak (ℓ=218)

### From 2D universe population spectrum
- The 2D universe population is a MIX of event types, not a single value
- Top contributors: star formation, X-ray bursts, Type Ia SN
- Required |C|² × α ~ 10^-7 to 10^-9 to match Ω_DM = 0.27
- f_active << 0.05 for all event types (free parameter confirmed)
- The cascade is QUALITATIVELY consistent with ΛCDM

### From g_+ derivation
- g_+ = c × H_0 / (2π) = 1.3e-10 m/s² (10% match, coincidence)
- g_+ from typical galaxy: ~1e-10 m/s² (matches, but fitting parameter)
- g_+ from 2D universe population: consistent check
- 2D CFT scale argument requires 2D CFT scale = H_0 (separate postulate)
- No natural length/time scale gives g_+ = 1.2e-10 m/s²
- HONEST: g_+ is EMPIRICAL, not derived from cascade first principles

### From CMB anisotropy
- 2D universe population at z=1100: Thomson-dominated (~10^48 J/Mpc³)
- Even with α << 1, Thomson dominates the 2D universe population
- Acoustic peak: ℓ_1 ~ 220 (consistent with ΛCDM)
- Damping tail: same as ΛCDM (no DM-photon coupling)
- Cascade does NOT predict: N_eff, H_0 at z=1100, τ_reion, f_NL
- HONEST: cascade is consistent with ΛCDM but adds no new CMB predictions

## What the cascade can claim

### Borrowed from RS-II + Liouville + Boltzmann:
- 5D AdS_5 framework
- G_4 on the brane
- Newton's law
- Hierarchy solution
- Karch-Randall 2+1D branes
- DOZZ 3-point function
- AdS/CFT correspondence
- CMB peak with H_0 = 70.16

### Cascade-specific (postulates):
- Cone-shape 3-level architecture
- Time compression mechanism
- Geometric mean property (H_0,4D = 70.16)
- 5/27/68 interpretation (qualitative)
- 4D event brane
- 2D universe creation by SM events

### NOT derived (honest unknowns):
- 2D universe mass (free parameter, was 6 M_sun)
- 2D universe lifetime (event-size-dependent)
- α (bulk-brane coupling)
- f_active (free parameter)
- g_+ (empirical, not derived)
- 5/27 inner split (dropped as postulate)
- Specific H_0 value (Mechanism M)

## Files originally in tempcalc/ (untracked)

These calculations were first created in `tempcalc/` (untracked) and then
copied to `calculations/` with v27_ prefix. The tempcalc/ versions are
preserved as research artifacts.

## Usage

```bash
python3 calculations/v27_rs_ii_calculations.py
python3 calculations/v27_karch_randall_2d_universes.py
python3 calculations/v27_cascade_camb_full.py
python3 calculations/v27_rs_ii_liouville_boltzmann.py
python3 calculations/v27_derive_cascade_parameters.py
python3 calculations/v27_trial_and_error_2d_universe.py
python3 calculations/v27_2d_universe_population_spectrum.py
python3 calculations/v27_cascade_g_plus_derivation.py
python3 calculations/v27_cascade_cmb_anisotropy.py
```

## Output

Each script prints its findings to stdout. The "HONEST" findings document
what the cascade can and cannot derive, what's empirical vs postulated,
and what would be needed to derive more from first principles.
