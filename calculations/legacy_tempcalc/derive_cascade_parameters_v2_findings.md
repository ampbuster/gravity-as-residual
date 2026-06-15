# Derive Cascade Parameters v2: 33 s is Event-Size-Dependent

## User's key insight

**33 s is only for SN-scale 2D universes** (where ℓ ~ 10^10 m and ℓ/c = 33 s). It's NOT a universal constant.

For other event types:
- AGN (ℓ ~ 10^13 m): τ_3+1D = 3.3×10^4 s = 9.2 hours
- BH merger (ℓ ~ 10^9 m): τ_3+1D = 3.3 s
- Galactic event (ℓ ~ 10^20 m): τ_3+1D = 3.3×10^11 s = 10 kyr
- Planck-scale (ℓ ~ 10^-35 m): τ_3+1D = 10^-43 s

**The 33 s is a free parameter too** — it depends on the event size.

## What this means for the cascade

The cascade's 2D universe population is a MIX of event types, not a single value. Each event type has:
- Its own E_event (energy)
- Its own ℓ_event (size)
- Its own m_2D_2D = E_event / c² (2D-frame mass)
- Its own τ_3+1D = ℓ_event / c (3+1D-frame lifetime)
- Its own e^{-ky} (set by m_2D_2D and target m_2D_3+1D)

## The 6 M_sun problem

The cascade's 6 M_sun was a SEPARATE postulate, not derived from any event.

If we set m_2D_2D = E_event / c²:
- SN (10^53 J): m_2D_2D = 1.1×10^36 kg = 5.6×10^5 M_sun
- AGN (10^52 J): m_2D_2D = 1.1×10^35 kg = 5.6×10^4 M_sun
- BH merger (10^47 J): m_2D_2D = 1.1×10^30 kg = 0.5 M_sun

The 6 M_sun is much LESS than the SN/AGN event energy converted to mass. So either:
- The 2D universe doesn't capture the full event energy (only a fraction α)
- The 2D universe has additional mass from somewhere else
- The 6 M_sun is wrong

## The recommended framework

The cascade's framework should be:

**Per event type:**
- E_event = event energy (SN ~ 10^53 J, AGN ~ 10^52 J, etc.)
- ℓ_event = event size (SN ~ 10^10 m, AGN ~ 10^13 m, etc.)
- m_2D_2D = α × E_event / c² (only fraction α of energy becomes 2D universe)
- τ_3+1D = ℓ_event / c (3+1D lifetime)
- e^{-ky} = m_2D_3+1D_target / m_2D_2D (bulk depth for axion-like 3+1D mass)

**Total DM:**
- Integrate over event spectrum (SN, AGN, BH, stellar, etc.)
- Each event type contributes to DM based on its rate and parameters

**f_active:**
- f_active = τ_3+1D / T_universe (depends on event type)
- For SN-scale: f_active ~ 10^-17
- For AGN-scale: f_active ~ 10^-13
- For BH merger: f_active ~ 10^-17
- All MUCH less than the cascade's 0.05

## The 5/27/68 split

With the corrected f_active ~ 10^-13 to 10^-17 (depending on event type):
- "Active" 2D universes contribute essentially 0% of DM
- "Cumulative deaths" contribute essentially 100% of DM

The cascade's 5% active contribution is NOT supported by the empirical ℓ/c lifetime for any event type.

The 5/27/68 split should be re-examined:
- 5% ordinary matter (postulated)
- 27% dark matter (input from Planck)
- 68% dark energy (input from Planck)
- The 5%/27% inner split is NOT derived from the 2D universe population

## What the cascade should do

The cascade should:
1. **Drop the 33 s as universal lifetime** — it's SN-specific
2. **Drop the 6 M_sun as universal mass** — it's an arbitrary postulate
3. **Drop the 0.05 f_active** — it's not supported by any event type
4. **Drop the 5% active in 5/27/68** — the active contribution is negligible
5. **Acknowledge that 2D universe parameters depend on event type**
6. **Integrate over the event spectrum** to get total DM

This is more honest and more consistent.

## The honest cascade position

After dropping these postulates, the cascade's only DM-related claims are:
- DM is the cumulative gravitational effect of 2D universe deaths (qualitative)
- The 2D universe population comes from SM energetic events (qualitative)
- The 3+1D-frame mass is m_2D_2D × e^{-ky} (qualitative)

The QUANTITATIVE claims (specific masses, lifetimes, f_active) were based on unjustified postulates and need to be revised.

## Files

- This memo: `tempcalc/derive_cascade_parameters_v2_findings.md`
- Derivation script: `tempcalc/derive_cascade_parameters_v2.py`
- Previous: `tempcalc/derive_cascade_parameters.py`, `tempcalc/derive_cascade_parameters_findings.md`
- Trial-and-error v1/v2: `tempcalc/trial_and_error_2d_universe.py`, `tempcalc/trial_and_error_2d_v2.py`

## Bottom line

**The 33 s lifetime is event-size-dependent, not universal.** The cascade's 2D universe population is a MIX of event types (SN, AGN, BH, etc.), each with its own ℓ and E. The 6 M_sun and 0.05 f_active were arbitrary postulates that conflict with the empirical ℓ/c lifetime for any event type.

The cascade's framework should be:
- DM = sum over event types of (rate × T_universe × m_2D_3+1D(event))
- m_2D_2D(event) = α × E_event / c²
- τ_3+1D(event) = ℓ_event / c
- e^{-ky}(event) = m_2D_3+1D_target / m_2D_2D(event)

This is more honest, more consistent, and removes several arbitrary postulates.
