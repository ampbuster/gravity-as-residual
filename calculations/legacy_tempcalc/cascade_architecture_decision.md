# Cascade Architecture — Decision Memo

## Status: 3-level cascade (cone-shaped, NOT scale-invariant)

After discussion, the cascade's structure is:

```
4D parent (event) → 3+1D us (SM brane) → 2D children (terminal)
```

This is a **3-level cone-shaped structure** with:
- **4D ceiling**: the "Big Bang" event with antigravity
- **3+1D middle**: our SM brane
- **2D floor**: terminal child universes (no 1D, no 0D)

## Why NOT scale-invariant (the original default)

Earlier the paper said "default is scale-invariance / infinite cascade, regulated by ρ_crit at each level." This is **physically impossible** because:

1. **1D universes are nonsensical** — no stable orbits, no chemistry, no complex structure
2. **0D universes are just points** — not universes, just events
3. **The cascade MUST terminate at 2D** — going below 2D gives unphysical universes
4. **The ρ_crit regulator is unnecessary** — the 2D floor is a hard structural limit

The "scale-invariant / infinite cascade" option was always physically problematic. It assumed the cascade could go 4D → 3+1D → 2D → 1D → 0D → ... indefinitely, but this is impossible.

## Why 2D specifically (not 1D, not 0D)

2D is special in physics:
- **2D CFTs are exactly solvable** (infinite-dimensional symmetry, Virasoro algebra)
- **Liouville 2D gravity is rigorously defined** (Miller-Sheffield 2021 proved the metric exists)
- **2D is the highest dimension where quantum gravity is "easy"**
- **2D CFT correlation functions are exact** (DOZZ formula, BPZ conformal blocks)

If the cascade has a hard floor (which it must), 2D is the natural choice because:
- It's the lowest dimension where quantum gravity is well-defined
- Going below 2D gives nonsensical physics
- The 2D Liouville framework provides a rigorous mathematical structure

## Why 4D specifically (not 3D, not 5D+)

The cascade's "4D parent" is the "Big Bang" event. 4D is special because:
- **AdS_5/CFT_4** is the original and most well-studied AdS/CFT correspondence
- **4D spacetime** has the right structure for the Standard Model
- **One dimension above 3+1D** is the natural "parent" for a dimensional cascade

The cascade does NOT extend to 5D (or higher) for now. This is a **deliberate choice**, not a derivation:
- 5D extension is possible (would give 4-level cascade)
- But 5D doesn't have a strong physical motivation (unlike 2D, which is forced)
- Adding 5D adds complexity without clear benefit
- We keep 3-level for simplicity

## What this means for the paper

1. **Drop "scale-invariance / infinite cascade" as the default.** The cone-shape is forced, not an alternative.

2. **Drop "Scale-Invariant" from the model's name.** "Scale-Invariant Dimensional Cascade" (SIDC) is misleading. Better names:
   - "Dimensional Cascade" (DC)
   - "Cone-Shaped Dimensional Cascade" (CSDC)
   - "Three-Level Dimensional Cascade" (3LDC)

3. **Remove the ρ_crit regulator.** With cone-shape, the cascade terminates naturally at 2D. No infinite regress, no regulator needed.

4. **The 5/27/68 split is a 3-level structural feature:**
   - 4D parent contributes 68% (DE, projected to 3+1D)
   - 3+1D direct contributes 5% (SM, on the brane)
   - 2D sector contributes 27% (cumulative 2D universe death, back-projected to 3+1D)

5. **The 7/7 specific-case predictions are unchanged.** Cone-shape and scale-invariant both give the same predictions. The change is in framing, not physics.

## What this means for Limitation 26

Current Limitation 26: "Cascade specifies geometry, not Lagrangian. The action in §2.5.1 is a SKELETON with 5+ free parameters."

Updated Limitation 26: "Cascade specifies the 3-level cone-shaped structure (4D / 3+1D / 2D). The 2D floor is hard. The 2D universe's Lagrangian is hypothesized to be 2D Liouville CFT (closes the L_2D specification). The free parameters are: 2D action parameters (b, μ), bulk-brane coupling α, 2D universe lifetime τ_2D, and the 4D event's projection geometry. The 5/27/68 split is a structural feature but is not derived from the Lagrangian alone."

## What this means for §2.5.1 (Cascade Lagrangian)

The cascade's Lagrangian has:
- S_grav (5D bulk, but only the 4D level is relevant for our 3+1D physics)
- S_matter (SM on 3+1D brane)
- S_brane_2D (Liouville 2D CFT for the 2D universe sector)
- S_creation (vertex operator insertion for 2D universe creation)
- S_destruction (energy return to 3+1D as DM at 2D universe death)

The Liouville 2D CFT is the natural framework for the 2D universe sector. This is now a stronger claim (cone-shape forces 2D as the floor, so 2D CFT is the natural choice).

## What this means for §2.6 (Cone-shaped hierarchy)

The current §2.6 says cone-shape is "a viable alternative" to scale-invariance. This should be flipped: **cone-shape is the only physically consistent option**, scale-invariance is impossible.

## What this means for the broader principle

The cascade's "broader principle" (the 4D → 3+1D → 2D structure applying at each level) is now:
- **Not scale-invariant** (the 2D floor breaks scale invariance)
- **Self-similar in some regimes** (the RAR works across galaxy masses)
- **Threshold-based** (E > E_crit triggers 2D universe creation)
- **3-level** with hard bounds

The "broader principle" is more nuanced than "scale-invariant" — it's "the cascade has a specific 3-level structure with threshold-based 2D universe creation, and this structure is self-similar across galaxy scales (the RAR) but not scale-invariant at the cosmological level (the 4 zones of H(z) are epoch-dependent)."

## Summary

- **3-level cascade**: 4D parent → 3+1D us → 2D children (terminal)
- **2D is the hard floor** (forced by physics, 1D and 0D are nonsensical)
- **4D is the ceiling** (specific choice, not extended to 5D for now)
- **NOT scale-invariant** (the 2D floor breaks scale invariance)
- **Cone-shaped, terminal at 2D**
- **5/27/68 is a 3-level structural feature**
- **The 7/7 specific-case predictions are unchanged**
- **2D Liouville CFT is the natural framework for the 2D universe sector**
- **ρ_crit regulator is removed**
- **"Scale-Invariant" should be dropped from the model's name**

## Open questions

1. **What fixes the specific 2D floor?** The argument that 2D is the floor is physical (1D and 0D are nonsensical), but the SPECIFIC value (2D, not 2.5D or 1.5D) is a choice. The cascade's 2D is "1+1" (1 space + 1 time) or "2+1" (2 space + 1 time). The paper should specify this.

2. **What fixes the 4D ceiling?** The cascade currently picks 4D, but doesn't derive it. Possible motivations:
   - AdS_5/CFT_4 (the most well-studied AdS/CFT)
   - 4D spacetime is the natural "parent" of 3+1D
   - String theory's 10D/11D would give more levels, but we don't extend that far

3. **What about 5D as a possible extension?** Future work. For now, 3-level.

4. **The 5/27/68 split** is now a structural feature of the 3-level cascade. It might be derivable from the projection geometry at each level. This is a major calculation, not yet done.

5. **The 2D universe's specific Lagrangian** is hypothesized to be 2D Liouville CFT. This is a choice, not a derivation. The free parameters (b, μ) are still free.

## File locations

- This memo: `tempcalc/cascade_architecture_decision.md`
- v1 Liouville findings: `tempcalc/liouville_factive_findings.md`
- v3 Liouville findings: `tempcalc/liouville_v3_findings.md`
- Literature memo: `tempcalc/lagrangian_literature_memo.md`
- Liouville test code: `tempcalc/liouville_factive_test.py`
- More Liouville tests: `tempcalc/liouville_more_tests.py`
