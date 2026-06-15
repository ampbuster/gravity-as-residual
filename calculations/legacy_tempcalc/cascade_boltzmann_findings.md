# Cascade Boltzmann-lite — Findings

## What I built

A simplified line-of-sight integral approach for the cascade's H(z) modification.
The idea: integrate the cumulative 2D universe death energy along the line of sight
to get the 3+1D gravitational effect.

## Three versions

### v1: Basic framework
- Hardcoded boost/drag at zone boundaries
- Got the 4-zone structure right
- But the boost/drag were not derived from the integral

### v2: Physical SM event rate
- Used Madau & Dickinson SFR + AGN component
- Still had hardcoded zone boundaries (z=0.01, 1.0)
- Still had hardcoded boost/drag magnitudes (2.88, -2.76)
- The integral was computed but not used for the H modification

### v3: Derived from integral
- Computes the cumulative 2D universe death energy E_cum(z) from the line-of-sight integral
- Uses the integral to derive the H(z) modification
- Local R_stellar boost still hardcoded (separate effect from line-of-sight)
- CMB drag computed from the integral but with a small coupling

## What the integral actually gives

The cumulative 2D universe death energy E_cum(z) at different z:

| z | E_cum(z) | E_cum(z)/E_cum(0.01) |
|---|----------|----------------------|
| 0.01 | 3.83e+10 | 1.0000 |
| 0.10 | 3.83e+10 | 1.0000 |
| 0.50 | 3.82e+10 | 0.9999 |
| 1.00 | 3.82e+10 | 0.9982 |
| 2.00 | 3.71e+10 | 0.9693 |
| 5.00 | 2.74e+10 | 0.7175 |
| 10.00 | 1.46e+10 | 0.3811 |

**The integral gives a small effect.** E_cum(z) is roughly constant for z<1
(because the Madau SFR peaks at z~2 and the integration range doesn't change
much at low z), then drops by ~30% at z=5 and ~60% at z=10.

This is NOT the +2.84 secular boost or -2.76 CMB drag. The integral gives
much smaller effects (0.1% at z=0.5, 30% at z=10).

## Why the integral doesn't give the cascade's 4-zone H(z)

The cascade's 4-zone H(z) requires:
- +2.88 boost at z=0
- 0 boost at z=0.02
- +2.84 boost at z=0.1-1
- -2.76 drag at z>1

The line-of-sight integral gives:
- ~0 effect at z=0.01-0.5 (the SFR is roughly the same)
- 0.1% effect at z=1
- 30% effect at z=5
- 60% effect at z=10

The integral's effect is much smaller than the cascade's boost/drag. To get
the cascade's values, you would need to:
1. Use a much larger E_2D (the 2D universe death energy) — but this is
   the 50-orders-of-magnitude tension from Test A
2. Use a different SM event rate that peaks more strongly at z~0-1
3. Add the local R_stellar boost as a separate term (it's a 3D cluster
   effect, not a line-of-sight integral)

## What the Boltzmann-lite approach IS good for

1. **Framework validation**: The line-of-sight integral IS the right
   structure for connecting 2D universe physics to 3+1D observables
2. **SFR/AGN input**: Uses real cosmic star formation history
3. **Physical motivation**: The integral captures the cumulative effect
   of 2D universe deaths over cosmic time
4. **Test bed for the 5/27/68**: The integral can be extended to compute
   the cosmic DM density from 2D universe deaths

## What the Boltzmann-lite approach IS NOT good for

1. **Doesn't derive the 4-zone H(z)**: The integral gives much smaller
   effects than the cascade's empirical values
2. **Doesn't solve the 50-orders tension**: The E_2D is still unknown
3. **Doesn't derive the 5/27/68 split**: Need a full cosmological integration
4. **Doesn't include local R_stellar boost**: This is a separate cluster effect

## What a full Boltzmann code would add

A proper Boltzmann code (CAMB, CLASS, or custom) would:
1. Solve the full Einstein-Boltzmann equations with the 2D universe sector
2. Track the 2D universe population as a function of (x, p, t)
3. Compute the gravitational effect of the cumulative 2D universe deaths
4. Self-consistently compute H(z) and the matter power spectrum
5. Include the CMB anisotropies from 2D universe drag at recombination

This is a major project (weeks to months), not a quick test.

## Honest assessment

The Boltzmann-lite approach:
- ✓ Has the right structure (line-of-sight integral)
- ✓ Uses a physical SM event rate (Madau SFR + AGN)
- ✓ Can be extended to compute the 5/27/68 split
- ✗ Doesn't derive the 4-zone H(z) from the integral alone
- ✗ Doesn't solve the 50-orders tension
- ✗ Doesn't include local R_stellar boost

This is a **framework for future work**, not a complete calculation.
A full Boltzmann code with the cascade's 2D universe sector would be
the proper way to derive the cascade's H(z) from first principles.

## File locations

- v1 (basic): `tempcalc/cascade_boltzmann_lite.py`
- v2 (physical SFR): `tempcalc/cascade_boltzmann_v2.py`
- v3 (derived from integral): `tempcalc/cascade_boltzmann_v3.py`
- This memo: `tempcalc/cascade_boltzmann_findings.md`

## Next steps

1. **Add the 5/27/68 derivation**: Use the Boltzmann-lite to compute the
   cosmic DM density from 2D universe deaths over cosmic time
2. **Add proper E_2D calculation**: Use Liouville + 2D Planck mass to get E_2D
3. **Implement a real Boltzmann code**: Replace the line-of-sight integral
   with a proper Boltzmann code (CAMB extension or custom)
4. **Add the local R_stellar boost as a separate effect**: Cluster 2D universe
   population, not line-of-sight integral
5. **Compute the matter power spectrum**: P(k) with cascade modifications
6. **Compute the CMB anisotropies**: 2D universe drag at recombination
