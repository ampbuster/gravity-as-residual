# P(y) Problem — Explained

## What is P(y)?

P(y) is the cascade's bulk position distribution. It tells us WHERE
2D universes are located in the 5D AdS_5 bulk:
- y = 0: on our 3+1D brane (shallow)
- y > 0: deep in the bulk

The time compression factor depends on y:
- y = 0: e^{-ky} = 1 (no time compression)
- y > 0: e^{-ky} < 1 (time-compressed)

This determines the 2D universe's 3+1D-frame mass:
m_2D_3+1D = m_2D_2D × e^{-ky}

## The two requirements

The cascade needs P(y) to satisfy TWO conflicting requirements:

### Requirement 1: Axion-like mass
For m_2D_3+1D ~ 1.1e-23 kg (axion-like, matching observations):
- If m_2D_2D = 6 M_sun (cascade's postulate)
- Then e^{-ky} ~ 10^-48
- This means 2D universes must be DEEP in the bulk (y ~ 100 AdS_5 radii)

### Requirement 2: Local R_stellar boost
For the +2.88 km/s/Mpc at z=0 (SH0ES=73.04):
- Need 2D universes at SHALLOW bulk (y ~ 0)
- Where e^{-ky} ~ 1 (no time compression)
- Their full 2D-frame mass (6 M_sun) appears in 3+1D
- This gives a significant gravitational effect

## The conflict

These are CONTRADICTORY. If most 2D universes are deep in the bulk,
the local boost is too small. If most are shallow, the average mass
is too large (stellar-scale, not axion-like).

## The trial-and-error result

I tested a bimodal P(y) distribution (50% shallow, 50% deep) in
calculations/trial_and_error_v26.py:

| Population | e^{-ky} | m_2D_3+1D (kg) | Contribution |
|------------|---------|-----------------|--------------|
| Shallow (50%) | 1 | 6 M_sun = 1.2e31 | dominates |
| Deep (50%) | 10^-48 | 1.1e-23 | negligible |

Average m_2D_3+1D ~ 6e30 kg (3 M_sun, stellar-scale)

This is WAY too heavy. The cascade needs m_2D_3+1D ~ 1.1e-23 kg (axion-like).

For the average to be 1.1e-23 kg, the deep population must DOMINATE:
P(deep) / P(shallow) >> 1, like 10^48 : 1 ratio.

But then the shallow population (needed for local boost) is negligible.

## Why this is a real problem

The cascade's framework REQUIRES both:
1. 2D universe population that gives the right AVERAGE mass (Ω_DM = 0.27)
2. 2D universe population that gives the local R_stellar boost (Zone 1)

These come from DIFFERENT P(y) distributions:
- Requirement 1: P(y) heavily weighted toward deep bulk
- Requirement 2: P(y) has a non-negligible shallow-bulk population

You can't have both with a simple P(y).

## What this means

**The cascade's local R_stellar boost and axion-like mass are INCOMPATIBLE**
under the simple bimodal P(y) assumption.

This is a NEW inconsistency in the v2.6 architecture that wasn't
obvious before. It emerged from the trial-and-error analysis.

## Possible resolutions

### Option A: Different mechanisms for different effects
- The local R_stellar boost is NOT from 2D universe deaths
- It might be from a different cascade mechanism (e.g., 4D event's direct effect)
- The 2D universe population is entirely deep-bulk (axion-like)

### Option B: Non-bimodal P(y)
- P(y) is NOT 50/50 shallow/deep
- Maybe a specific functional form (e.g., exponential decay from shallow to deep)
- This would require a specific calculation from the cascade's 5D physics

### Option C: The local boost is over-interpreted
- The +2.88 km/s/Mpc at z=0 is NOT from 2D universes
- It's just noise in the data
- The 4-zone H(z) is over-interpreted

### Option D: The 2D universe mass is different
- The cascade's 6 M_sun postulate is wrong
- The actual 2D-frame mass is much smaller (e.g., 1e-23 kg)
- This would resolve the P(y) problem by making both shallow and deep
  populations contribute equally to the average

### Option E: P(y) is a delta function with a small tail
- P(y) is mostly at y ~ 100/k (deep bulk, axion-like)
- With a small tail extending to y ~ 0 (shallow bulk, for local boost)
- The tail is responsible for the local boost, but it's a small fraction

The required ratio P(deep) / P(shallow) ~ 10^48. This is a HUGE ratio,
but it's not impossible.

## What the cascade's P(y) should be

For the cascade to be self-consistent, P(y) needs to be:
- Mostly deep (e^{-ky} ~ 10^-48) for the axion-like mass
- With a small shallow component (e^{-ky} ~ 1) for the local boost
- The shallow component must be SMALL enough that the average mass
  is still axion-like

The P(y) could be a delta function at y ~ 100/k (pure deep bulk), with
a small tail extending to y ~ 0 (shallow bulk). The tail is responsible
for the local boost, but it's a small fraction of the total population.

## The honest assessment

The P(y) problem is a REAL inconsistency in the v2.6 architecture.
The cascade's two main claims about H(z):
- The axion-like mass (requires deep bulk)
- The local R_stellar boost (requires shallow bulk)

are not simultaneously achievable with a simple P(y) distribution.

This is a limitation that should be added to the cascade's list. It's
not a "fatal flaw" — the cascade can still work if P(y) is appropriately
structured — but it requires a specific calculation from the cascade's
5D physics that hasn't been done.

## What this means for v2.6

The P(y) problem is a NEW limitation that should be documented:
- L35 (NEW): Bulk position distribution P(y) is unknown; the cascade
  needs a specific P(y) to reconcile the axion-like mass with the
  local R_stellar boost. Without a specific 5D physics calculation,
  P(y) is postulated.

The cascade can say:
- "The bulk position distribution P(y) is a free parameter of the cascade"
- "Different choices of P(y) give different predictions for the
  local R_stellar boost vs axion-like mass"
- "A specific 5D physics calculation would constrain P(y)"

## File locations

- This memo: `tempcalc/py_problem_explained.md`
- Trial-and-error: `calculations/trial_and_error_v26.py` (Q4)
- Time compression: `tempcalc/time_compression_memo.md`
- 4-zone assessment: `tempcalc/4zone_data_fitting_assessment.md`
- Hubble tension: `tempcalc/hubble_tension_4zone_assessment.md`
- Architecture: `tempcalc/cascade_architecture_decision.md`

## Bottom line

The P(y) problem is a REAL inconsistency in the v2.6 architecture:
- The axion-like mass requires 2D universes deep in the bulk
- The local R_stellar boost requires 2D universes shallow in the bulk
- A simple bimodal P(y) doesn't work (shallow dominates the average)
- P(y) needs to be heavily weighted toward deep bulk with a small
  shallow tail

The cascade can work if P(y) is appropriately structured, but the
specific P(y) requires a 5D physics calculation that hasn't been done.
This is a NEW limitation for the v2.6 architecture.
