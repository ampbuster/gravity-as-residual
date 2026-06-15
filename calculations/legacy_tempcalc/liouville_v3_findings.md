# Liouville Tests v3 — Final Honest Findings

## What I tried to do

Push beyond the v1 f_active test (which I realized was a tautology —
f_active = τ_2D/T_universe is just dimensional analysis). Test whether
Liouville 2D CFT actually derives any of the cascade's other empirical
values.

## What I found (UPDATED with proper analysis)

### Test A: 2D universe average mass at death — STILL A DISCREPANCY

**Approach 1** (count 2D universes from SM events):
- 0.3 SM events/s/Mpc³ × 5% above E_crit × T_universe = 6.5e15 ever
- Total DM mass: 7.7e40 kg/Mpc³
- Average per 2D universe: **1.2e25 kg = 6 M_sun**

**Approach 2** (2D Planck mass scaling):
- m_2D ~ α × M_Planck_4D
- For α ~ 1e-15: m_2D ~ 1e-23 kg (axion-like)

**Discrepancy: 50 orders of magnitude**

This is a **real tension** in the cascade. The cascade's SM event rate
is too high by 50 orders of magnitude if the 2D universe mass is
axion-like. Either:
- (a) The fraction of SM events above E_crit is 10^-50 (essentially zero)
- (b) The 2D universe mass is stellar-scale (which has other problems)
- (c) The cascade's "2D universe population" is a much smaller fraction of DM

**Liouville does NOT resolve this** — it's a separate question.

### Test B: DOZZ 3-point function — REAL NUMBERS

The DOZZ 3-point function <V_α0 V_α0 V_α0> for various (b, α0):

| b | α0 | |C|² |
|---|----|-----|
| 0.5 | 0.5 | 0.28 |
| 0.7 | 0.5 | 18 |
| 1.0 | 0.5 | 46 |
| 1.0 | 0.3 | 8.2 |
| 1.2 | 0.5 | 31 |

**This is a real Liouville prediction**: |C|² ~ 1-50 for natural (b, α0).
The PHYSICAL creation rate per SM event is α² × |C|², where α is the
bulk-brane coupling (free parameter).

### Test C: 2-point function at finite T — WRONG PHYSICS

The cluster boost (T_cluster/T_field)^{2-2Δ_α} is huge (10^7-10^14),
but this is the wrong physics. The cascade's "cluster boost" comes from
the event rate (more star formation, more supernovae), not from
Liouville 2-point function temperature dependence.

**Conclusion:** Don't conflate these mechanisms.

### Test D: f_back from Liouville — NOT DERIVABLE

The cascade's f_back ~ 10^-85 is a probability for the 2D universe's
death energy to return to 3+1D as DM. Liouville's reflection coefficient
ρ(α) is ~ 1 for natural α, not 10^-85.

**Conclusion:** f_back is a separate cascade concept (a probability for
energy to return vs escape), not a Liouville quantity. Remains a free
parameter.

### Test E: 5/27/68 split — REQUIRES FULL BOLTZMANN CODE

The 5/27 split depends on:
1. SM energy density evolution (BBN, recombination, structure formation)
2. 2D universe creation rate (DOZZ × SM event rate)
3. 2D universe lifetime distribution
4. Energy return at death
5. Integration over cosmic time

**NOT a back-of-envelope calculation.** Requires a full cosmological
Boltzmann code with Liouville. NOT done in v3.

### Test F: g_+ — NOT DERIVABLE

g_+ = c × H_0 / (2π) ~ 1.2e-10 m/s² is a fundamental constant
combination, set by the cosmic expansion rate and the speed of light.
Neither is derivable from Liouville.

**Conclusion:** g_+ remains a free parameter.

### Test G: 2D universe death energy — REQUIRES 2D PLANCK SCALE

Multiple attempts to compute E_death gave absurdly small numbers
(10^-66 to 10^-54 kg). The issue: Liouville natural units are
dimensionless, and the 2D Planck scale is unspecified.

**Conclusion:** E_death is hard to compute without specifying the
2D Planck mass. The cascade currently POSTULATES m_2D ~ axion mass,
not derived.

### NEW Test: Energy-weighted f_active — TAUTOLOGY

I tried to find a non-trivial Liouville prediction for energy-weighted
f_active. The result <Δ × τ> = 1 was a tautology:
- I assumed τ_2D(α) = 1/Δ_α
- Then <Δ × τ> = <Δ × 1/Δ> = 1 trivially

Different assumptions (τ = Δ, τ = 1/Δ², etc.) give different results.
**The τ(Δ) scaling is a separate question that Liouville does NOT
resolve.**

## Overall: HONEST ASSESSMENT (UPDATED)

| Test | v1 | v3 | Verdict |
|------|----|----|---------|
| f_active | "PASS" (was tautology) | tautology | trivially passes (no info) |
| 2D universe mass | not tested | 50-orders-off TENSION | free parameter |
| DOZZ amplitude | not computed | \|C\|² ~ 1-50 | real Liouville number |
| Cluster 2pt T-dep | not tested | wrong physics | not relevant |
| f_back | not tested | Liouville ≠ f_back | free parameter |
| 5/27/68 split | not tested | needs Boltzmann | unresolved |
| g_+ | not tested | c × H_0 / 2π | free parameter |
| 2D death energy | not tested | 2D Planck unknown | free parameter |
| Energy-weighted f_active | not tested | tautology | not informative |

## What Liouville ACTUALLY adds (revised)

1. **A specific 2D universe Lagrangian** (Liouville action with b, μ)
2. **The DOZZ 3-point function** giving 2D universe creation amplitude
   |C|² ~ 1-50 (Liouville natural units) — this is REAL
3. **A natural 2D universe lifetime** τ_2D ~ 1/√μ × (1/Δ_α scaling)
4. **A specific reflection coefficient** ρ(α) for 2D universe weights
5. **Mathematical rigor**: 2D CFT correlation functions are EXACT
6. **Holographic dual** to AdS_3 (Karch-Randall)

## What Liouville does NOT add

1. The cascade's empirical τ_2D = 0.7 Gyr (free parameter)
2. The cascade's g_+ ~ 1.2e-10 m/s² (it's c × H_0 / 2π)
3. The cascade's f_back ~ 10^-85 (a probability)
4. The cascade's 5/27/68 split (needs full Boltzmann)
5. The cascade's 2D universe mass (needs 2D Planck scale)
6. The cascade's f_active ~ 0.05 (trivially τ_2D/T_universe)
7. A non-trivial energy-weighted f_active (depends on τ(Δ) scaling)
8. Resolution of the 50-orders-of-magnitude mass tension

## What this means for the cascade

**The v1 test was MISLEADING.** I claimed "Liouville f_active passes"
but it was just dimensional analysis, not a derivation. The honest
claim is much weaker.

**The MAJOR WIN is smaller than I thought:**
- Liouville gives a specific 2D universe sector with a known Lagrangian
- The DOZZ 3-point function gives the creation amplitude |C|² ~ 1-50
- This is a real theoretical anchor (a known 2D CFT)

**The MAJOR LOSS is the honest realization that:**
- The cascade's specific empirical values (τ_2D, g_+, f_back, 5/27/68,
  m_2D) are NOT derivable from Liouville alone
- They require additional inputs (2D Planck scale, Boltzmann evolution,
  bulk-brane coupling α)
- The 50-orders-of-magnitude mass tension is a REAL problem in the
  cascade that Liouville does NOT solve

## Recommendation

Adopt the Liouville framework as the cascade's 2D universe Lagrangian
(closes Limitation 26's first phase: specify L_2D).

But be VERY HONEST in the paper that:
- The 2D universe's specific parameters (mass, lifetime) are still free
- The DOZZ 3-point function gives a creation AMPLITUDE, not a creation RATE
- The 5/27/68 split is NOT derived from Liouville (needs Boltzmann code)
- g_+ is NOT derived from Liouville (it's c × H_0 / 2π)
- The 50-orders-of-magnitude mass tension in Test A is a REAL problem
  that the cascade needs to address

**The honest claim should be:**
"The cascade's 2D universe sector is 2D Liouville quantum gravity.
The 2D universe's Lagrangian is now specified. The 2D universe's
creation amplitude (DOZZ 3-point function) is calculable. However,
the specific empirical values (τ_2D, g_+, f_back, 5/27/68, m_2D) are
free parameters of the model and are not derived from the Lagrangian
alone. A complete derivation would require: (a) specifying the 2D
Planck scale, (b) integrating the SM event rate over cosmic time,
(c) computing the energy return at 2D universe death, (d) full
Boltzmann code with Liouville sector. This is future work."

## File locations

- Test code: `tempcalc/liouville_more_tests.py`
- v3 results: `tempcalc/liouville_v3_results.json`
- This memo: `tempcalc/liouville_v3_findings.md`
- v1 (f_active test): `tempcalc/liouville_factive_test.py`
- v1 findings: `tempcalc/liouville_factive_findings.md` (needs honesty update)
- Literature memo: `tempcalc/lagrangian_literature_memo.md`
- DOZZ inline: see Test B output
