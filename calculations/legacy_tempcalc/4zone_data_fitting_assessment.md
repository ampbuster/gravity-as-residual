# 4-Zone H(z) Assessment — Honest Take

## Short answer

**Yes, the 4-zone H(z) is data fitting.** It has a cascade
INTERPRETATION (each zone corresponds to a cascade mechanism), but
the specific values are NOT derived from first principles.

## What the 4-zone spec is

8 free parameters:
- H_bulk = 70.16 (geometric mean, NOT fitted)
- z_trgb = 0.01, z_rise = 0.05, z_fall = 1.0 (zone boundaries)
- w_local = 0.001 (tanh width)
- delta_local = 1.44, delta_secular = 2.84, delta_primordial = -2.76 (boost/drag)

Fitted to ~5 data points:
- SH0ES = 73.04 (z=0)
- TRGB = 70.16 (z=0.01-0.05)
- H0LiCOW = 73.0 (z=0.05-1.0)
- Pantheon+ = 73.0 (z=0.5)
- Planck = 67.4 (z=1100)

This is **8 parameters for 5 data points** = overparameterized.

## What the cascade INTERPRETS (not derives)

| Zone | Cascade interpretation | Status |
|------|----------------------|--------|
| 1 (z<0.01) | Local R_stellar boost from 2D universe population in our cluster | INTERPRETED |
| 2 (0.01<z<0.05) | 4D bulk baseline (no 2D universe effect) | INTERPRETED |
| 3 (0.05<z<1.0) | Secular cosmic web boost from line-of-sight 2D universe creation | INTERPRETED |
| 4 (z>1.0) | CMB drag from cumulative 2D universe deaths | INTERPRETED |

The cascade can SAY "each zone corresponds to a cascade mechanism."
The cascade CANNOT DERIVE:
- Why the zone boundaries are at z=0.01, 0.05, 1.0
- Why the boost/drag magnitudes are 1.44, 2.84, -2.76
- Why there are 4 zones (not 3 or 5)

These are FIT to data, not derived from cascade principles.

## What the Boltzmann code shows

I tested this in `tempcalc/cascade_camb_no_zones.py`. The Boltzmann code:
- Computes H(z) from cumulative 2D universe death energy
- Uses Madau SFR for SM event rate
- Includes time compression
- Does NOT hardcode any zone boundaries

Result: H(z) is just standard ΛCDM with a small cascade contribution.
The 4-zone structure is NOT predicted by the Boltzmann code.

| z | H_cascade (no zones) | observed |
|---|----------------------|----------|
| 0.0 | 70.16 | 73.04 |
| 0.5 | 92.65 | ~73 |
| 1.0 | 125.25 | 67.4 |

The Boltzmann code does NOT match the observed 4-zone H(z). The
4-zone spec matches because it was FIT to the data.

## Does it make sense in the cascade?

**Yes, the cascade CAN interpret the 4 zones** (local R_stellar,
bulk baseline, secular boost, CMB drag).

**No, the cascade DOES NOT derive the 4 zones** (the specific values
are fitted).

The honest position is:
- The 4-zone structure is an EMPIRICAL FIT with a cascade INTERPRETATION
- The cascade's principles EXPLAIN why there might be ~4 zones
  (different physical mechanisms at different redshifts)
- The cascade does NOT PREDICT the specific zone boundaries or
  boost/drag magnitudes

## What the cascade ACTUALLY derives

The cascade derives:
- ✓ H_bulk = 70.16 (geometric mean property — a real prediction)
- ✓ The qualitative interpretation of the 4 zones (cascade mechanisms)
- ✓ The Liouville 2D CFT framework (2D universe Lagrangian)
- ✓ The cone-shape architecture (3-level, terminal at 2D)

The cascade does NOT derive:
- ✗ The specific 4-zone structure (zone boundaries, boost/drag)
- ✗ The 4-zone H(z) values at specific redshifts
- ✗ The 8 fitted parameters

## My honest assessment

The 4-zone H(z) picture is:
- **Real** — observed in the data
- **Interpreted** — the cascade can give a qualitative interpretation
- **Fitted** — the specific values are hand-picked to match data
- **NOT derived** — the Boltzmann code doesn't predict it from
  first principles

This is similar to how:
- The Standard Model has 19+ free parameters
- ΛCDM has 6 free parameters
- MOND has 1 free parameter
- The cascade has 8+ free parameters (4-zone H(z) + cone-shape +
  time compression + ...)

The 4-zone H(z) is ONE MORE empirical fit in a model that already
has many.

## Strengths of the 4-zone H(z)

- It's a USEFUL empirical description of the H_0 data
- It has a CASCADE INTERPRETATION (each zone = a cascade mechanism)
- It's TESTABLE: the 4 zones can be confirmed or falsified
- It CONNECTS cascade principles to H_0 observations

## Weaknesses of the 4-zone H(z)

- It's OVERPARAMETERIZED (8 params for 5 data points)
- The specific values are FITTED, not derived
- The Boltzmann code doesn't predict it
- The cascade's contribution is the INTERPRETATION, not the values

## What to do in the paper

1. **Keep the 4-zone H(z) in the paper** (it has cascade interpretation)
2. **Label it explicitly as "empirical fit with cascade interpretation"**
3. **Don't claim it as a "cascade prediction"** (it's not derived)
4. **Note that the specific values are 8 fitted parameters for ~5 data points**
5. **Acknowledge that the Boltzmann code doesn't predict the 4-zone structure**

The honest framing is:
> "The 4-zone H(z) is an empirical fit that the cascade can interpret
> (each zone corresponds to a cascade mechanism), but the specific
> values are not derived from first principles. The cascade's
> contribution is the INTERPRETATION, not the specific values."

## File locations

- This memo: `tempcalc/4zone_data_fitting_assessment.md`
- Boltzmann code: `tempcalc/cascade_camb_no_zones.py`
- 4-zone spec: `tempcalc/4zone_quantized_test.py`
- CAMB no-zones: `tempcalc/cascade_camb_no_zones_findings.md`
- Time compression: `tempcalc/time_compression_memo.md`

## Bottom line

**The 4-zone H(z) is data fitting with cascade interpretation.**
The cascade can INTERPRET the zones (which mechanisms correspond
to which zones), but the specific values are FIT, not derived.

The honest claim is: the 4-zone H(z) is a useful empirical
description of the H_0 data, with the cascade's principles
providing a qualitative interpretation. The specific values
are 8 fitted parameters for ~5 data points — this is curve
fitting, not derivation.
