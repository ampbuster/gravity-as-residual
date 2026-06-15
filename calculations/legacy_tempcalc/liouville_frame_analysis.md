# Liouville Frame Analysis — 2D vs 3+1D

## Direct answer

**Liouville 2D CFT calculates in the 2D FRAME OF REFERENCE**, not the 3+1D frame.

The cascade has THREE frames:
- **4D frame** (parent, the "Big Bang" event)
- **3+1D frame** (us, the SM brane) — this is what we observe
- **2D frame** (children, the 2D universes) — this is what Liouville describes

## What Liouville calculates (2D frame)

Liouville 2D CFT gives the 2D universe's intrinsic 2D physics:
- **2D universe creation amplitude**: DOZZ 3-point function |C|² ~ 1-50
- **2D universe lifetime**: τ_2D ~ 1/√μ (Liouville potential)
- **2D universe conformal weights**: Δ_α = α(Q-α)
- **2D universe correlation functions**: 2-point, 3-point
- **2D universe reflection coefficient**: ρ(α) = λ(α)/λ(Q-α)

All of these are 2D-frame quantities. They describe the 2D universe's intrinsic 2D physics.

## What Liouville does NOT calculate (3+1D frame)

The 3+1D-frame observables require conversion from 2D to 3+1D:
- **2D universe mass in 3+1D kg**: m_2D_3+1D = (coupling α) × m_2D_2D
- **2D universe gravitational effect on 3+1D**: requires back-projection geometry
- **H(z) profile in 3+1D**: requires cosmological integral of 2D universe deaths
- **5/27/68 split**: requires Boltzmann evolution in 3+1D
- **g_+ (RAR universal scale)**: requires 2D-to-3+1D energy deposit calculation
- **f_back ~ 10^-85**: a probability, not a 2D CFT quantity

These are NOT in 2D units. They require conversion.

## The conversion problem

To go from 2D frame to 3+1D frame, you need:
1. **The 2D-3+1D coupling α** (a free parameter in the cascade)
2. **The projection geometry** (how 2D universe physics projects to 3+1D)
3. **The cosmological evolution** (how the 2D universe population evolves over cosmic time)
4. **The 2D Planck mass** (sets the scale of 2D physics)

None of these are derived from Liouville. They are separate inputs.

## The 50-orders tension explained

Test A in the v3 Liouville tests had a 50-orders-of-magnitude tension between two approaches to the 2D universe's mass:
- Approach 1 (count): m_2D ~ 6 M_sun (stellar-scale)
- Approach 2 (Planck): m_2D ~ 1e-23 kg (axion-like)

This is **the conversion problem**. The 2D-frame mass (in 2D natural units) is well-defined, but the 3+1D-frame mass depends on α. Without knowing α, we can't convert.

If α is very small (1e-30), the 3+1D mass is very small (axion-like).
If α is moderate (1e-5), the 3+1D mass is moderate (asteroid-like).
If α is order 1, the 3+1D mass is large (stellar-like).

The cascade doesn't derive α, so the 3+1D mass is undetermined within 50 orders of magnitude.

## What the cascade's 3-frame picture looks like

```
4D frame (parent event)
   |
   | dimensional projection (Big Bang)
   v
3+1D frame (us, SM) ← we observe this
   |
   | vertex operator insertion (SM events above E_crit)
   v
2D frame (children) ← Liouville describes this
   |
   | energy return at death
   v
3+1D frame again (DM) ← we observe this as DM
```

Each frame has its own physics:
- **4D frame**: 4D spacetime, parent event's antigravity
- **3+1D frame**: standard GR + SM, with cascade modifications (DE, DM, f_active, g_+)
- **2D frame**: 2D Liouville CFT, with creation amplitude, lifetime, conformal weights

The connections between frames are:
- **4D → 3+1D**: projection (the "Big Bang" creates our 3+1D brane)
- **3+1D → 2D**: vertex insertion (SM events create 2D universes)
- **2D → 3+1D**: energy return (2D universe deaths return energy as DM)

These connections are NOT given by Liouville. They require:
- Bulk-brane coupling α (for 3+1D ↔ 2D)
- Projection geometry (for 4D → 3+1D)
- Cosmological evolution (for time-dependent effects)

## Why this matters for the cascade

The cascade's specific empirical values (mass, f_back, g_+, 5/27/68, 4-zone H(z)) are all 3+1D-frame quantities. They depend on:
- 2D-frame physics (Liouville gives this)
- 2D-to-3+1D conversion (α, projection geometry, etc.)
- Cosmological evolution (Boltzmann code)

Liouville gives the FIRST piece (2D-frame physics). The SECOND and THIRD pieces are not derivable from Liouville alone. They require additional inputs.

This is why:
- The DOZZ |C|² ~ 1-50 is a real 2D-frame number, but doesn't give the 3+1D creation rate
- The 2D universe's intrinsic 2D mass is well-defined, but the 3+1D mass is undetermined
- The 2 kpc length scale is a 2D-frame coincidence, not a 3+1D prediction
- The 27% DM is a 3+1D observation that Liouville can interpret (2D universe content) but not derive (the 5% and 68% aren't from Liouville)

## What the paper should say

The honest framing of Liouville in the cascade:

> "The cascade's 2D universe sector is hypothesized to be 2D Liouville CFT. This provides a specific Lagrangian and exact correlation functions for the 2D universe's intrinsic 2D physics. However, Liouville 2D CFT is a 2D-frame theory, not a 3+1D-frame theory. To compare with 3+1D observations (H(z), DM density, RAR), the 2D-frame results must be converted to 3+1D-frame observables. This conversion depends on the bulk-brane coupling α (a free parameter), the projection geometry, and the cosmological evolution — none of which are derived from Liouville alone. This is why the cascade's specific empirical values (mass, f_back, g_+, 5/27/68) are NOT derived from Liouville alone, even though Liouville provides a real theoretical anchor for the 2D universe sector."

## File locations

- This memo: `tempcalc/liouville_frame_analysis.md`
- v1 Liouville findings: `tempcalc/liouville_factive_findings.md`
- v3 Liouville findings: `tempcalc/liouville_v3_findings.md`
- Pure Liouville H(z) test: `tempcalc/pure_liouville_hubble_test_results.md`
- Architecture decision: `tempcalc/cascade_architecture_decision.md`
