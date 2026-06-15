# Why 5% Active? — Honest Analysis

## The user's question

"Why 5% active in the first place? Isn't that just a postulate as well?"

**Yes, the 5% active (f_active = 0.05) is a POSTULATE, not a derivation.**

## Where did 5% come from?

The 5% active came from the **RAR (Radial Acceleration Relation) MCMC fit**:

> "MCMC posterior: f_active = 0.0513 +0.0070/-0.0073 (1σ), the fraction of
> cumulative 2D universe back-projection that is 'active' at any moment."

So f_active = 0.05 was a **fit to data**, not a first-principles derivation.

The paper then tried to "derive" it:
> "DERIVABLE (conditional): f_active = τ_2D / T_universe = 0.7/13.8 = 0.051
> with τ_2D ~ 0.7 Gyr (gas consumption timescale)."

But the caveat is:
> "τ_2D ~ 0.7 Gyr is identified by physical analogy, not from first principles."

So:
- f_active = 0.05 is a FIT to RAR data
- τ_2D = 0.7 Gyr is a SEPARATE POSTULATE (gas consumption timescale)
- The two are CONSISTENT (0.7/13.8 = 0.05), but neither is derived

## The chain of postulates

The 5% active depends on:
1. **f_active = 0.05** ← FIT to RAR data (not derived)
2. **τ_2D = 0.7 Gyr** ← Physical analogy (not derived)
3. **5/27/68 split** ← Universal energy budget postulate (not derived)
4. **5% is "active"** ← Same as f_active (postulate)
5. **2D universe mass = 6 M_sun** ← Separate postulate
6. **2D universe lifetime = 30 Gyr in 2D** ← Separate postulate (now dropped)
7. **e^{-ky} = 10^-54** ← Set by m_2D_2D and target m_2D_3+1D

Each of these is a separate postulate, none derived from first principles.

## What 5% active actually represents

In the cascade's framework:
- "Active" 2D universes: currently-alive 2D universes contributing to DM
- "Cumulative" 2D universe deaths: past 2D universes whose death energy projects to DM
- f_active = (active contribution) / (total DM)

The 5% means 5% of DM is from currently-alive 2D universes, 95% from cumulative deaths.

But:
- The 30 Gyr 2D lifetime is now DROPPED (was a guess, not derived)
- The 33 s in 3+1D gives f_active = 7.6×10^-17 (essentially zero)
- For ANY single event type, f_active is much less than 0.05

So the 5% active is INCONSISTENT with the empirical 33 s lifetime.

## The honest answer

**Yes, 5% active is a postulate, not a derivation.** It was:
- A phenomenological fit to the RAR
- Post-hoc justified by the gas consumption timescale
- Inconsistent with the empirical 33 s lifetime
- Inconsistent with the actual time dilation of the cascade

The cascade should drop f_active = 0.05 and acknowledge it's a phenomenological parameter, not a derived quantity.

## What should replace 5% active?

The cascade's honest position is:
- DM = cumulative gravitational effect of 2D universe deaths (qualitative)
- The 5% active vs 95% cumulative split is NOT derived
- The 2D universe population is a MIX of event types, each with its own parameters
- f_active depends on the event-type mix and time dilation
- The actual f_active is likely much less than 0.05 (maybe ~10^-17)

The 5/27/68 split should be treated as:
- 5% ordinary matter: observational (Planck)
- 27% dark matter: observational (Planck), interpreted as 2D universe deaths
- 68% dark energy: observational (Planck), interpreted as 4D event antigravity
- The 5%/27% inner split: NOT derived (assumed universal energy budget)

## What to do in the paper

The paper should:
1. Acknowledge f_active = 0.05 is a phenomenological fit, not a derivation
2. Drop the 30 Gyr 2D lifetime (was a guess)
3. Drop the 5% active in 5/27/68 (the active contribution is essentially zero)
4. Treat the 2D universe population as a MIX of event types
5. Document f_active as a free parameter, not a derived quantity

This is more honest and consistent with the analysis we've done.

## Files

- This memo: `tempcalc/why_5pct_active.md`
- RAR MCMC fit: see paper/paper.md §4.7
- 30 Gyr discussion: `tempcalc/trial_and_error_2d_v2.py`
- Event-size dependence: `tempcalc/derive_cascade_parameters_v2.py`

## Bottom line

**The 5% active was a phenomenological fit to RAR data, not a derivation.** It was post-hoc justified by the gas consumption timescale (τ_2D = 0.7 Gyr), but the 0.7 Gyr is a separate postulate. The 5% active is INCONSISTENT with the empirical 33 s lifetime (which gives f_active ~ 10^-17). The cascade should drop 5% active and acknowledge it's a postulate.
