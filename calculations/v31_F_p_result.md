# v3.1 F_p = 0 Consistency Check — Result

**Date**: 2026-06-18
**Question**: If F_p = 0 (all DM is from cumulative 3+1D event 2D universe deaths), does the math line up with observed DM?

## Bottom line: **F_p = 0 is INCONSISTENT with observations.**

There's a 10^7 shortfall that the current framework can't explain.

## Numbers

**Observed DM in observable universe:**
- ρ_crit = 9.21 × 10⁻²⁷ kg/m³
- V_obs = 3.6 × 10⁸⁰ m³
- M_DM = 0.27 × ρ_crit × V_obs = 8.9 × 10⁵³ kg = **10⁷¹ J**

**4D event contribution** (if F_p = 1, 4D event creates all DM as part of 3+1D):
- M_4D = 10⁶⁹ J (SIDC estimate)
- DM_primordial = 0.27 × 10⁶⁹ = 2.7 × 10⁶⁸ J
- That's only **0.3%** of observed DM

**Cumulative contribution** (if F_p = 0, all DM from 3+1D event 2D universe deaths, 100% death return):
- Sum of E_event for 14 event types: 1.38 × 10⁶⁴ J
- That's only **0.001%** of observed DM

## The 10⁷ Shortfall

Neither pure F_p = 0 nor F_p = 1 works:
| Picture | DM contribution | % of observed |
|---|---|---|
| F_p = 1 (all 4D event) | 2.7 × 10⁶⁸ J | 0.3% |
| F_p = 0 (all cumulative) | 1.38 × 10⁶⁴ J | 0.001% |
| F_p = 0.003 (mixed) | 10⁷¹ J | 100% — but most is cumulative, contradicting "F_p = 0" |

## What could close the gap

The 10⁷ factor must come from one of:
1. **2D universe growth factor G ~ 10⁷**: each 2D universe's mass at death = E_event × G
2. **10⁷× more events** than current event rate estimates
3. **4D event contribution is much larger than 10⁶⁹ J** (revisit M_4D estimate)
4. **Some combination of primordial + cumulative + growth**

## The user's insight, restated

The user's "F_p = 0 might be wrong" intuition is correct.
The user said: "originally it's framed as DM is cumulative, and most of it is created by big bang"

This is the v2.7 framing: **F_p is high** (most DM is from the 4D event), not zero.

The "death return = 100% × E_event" picture (user's clarification) gives F_p = 0 only if 2D universes have no growth and the 4D event creates no DM. Both assumptions fail quantitatively.

## What this means for the paper

1. **L100 (F_p derivation) STAYS OPEN** — neither F_p = 0 nor F_p = 1 works; the math is unfinished
2. **L35 (z_half) STAYS OPEN** — depends on F_p, which is undetermined
3. **The Hill function with F_p ~ 0.7-0.99 is a phenomenological placeholder**, not a derivation
4. **The user's clarification of f_back** (alive vs death return) is correct, but doesn't resolve F_p
5. **The 4D event MUST contribute to DM** (most of it, by the v2.7 framing)
6. **The cumulative picture is necessary** for local DM variation, but the absolute scale is too small by 10⁷

## What's needed to close the gap

A proper derivation must explain:
- Why F_p is high (most DM is from 4D event / 3+1D creation)
- Why local DM varies by galaxy (cumulative component)
- What sets the 2D universe growth factor (if any)
- How the 10⁷ factor is distributed between F_p and growth

The Hill function was an attempt to bridge this gap. It correctly identified that F_p is variable (high overall, but with local variation), but didn't derive the absolute value or the growth factor.

## Honest verdict

The SIDC framework, as currently formulated, has a **quantitative problem** with DM:
- Cannot derive F_p from first principles
- Cannot derive the 2D universe growth factor
- The Hill function is a phenomenological fit, not a derivation
- F_p = 0 is now demonstrably wrong (calculation in v31_F_p_consistency.py)
- F_p = 1 is also wrong (4D event doesn't have enough energy)
- The truth is somewhere in between, but the framework can't yet pin it down

This is **L100, L35, and a new "L138: 2D universe growth factor not derived"** territory.
