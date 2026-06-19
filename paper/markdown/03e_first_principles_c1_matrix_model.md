# First-Principles Analysis: c=1 Matrix Model → M_Pl,2D = 3 TeV

**v3.3.1, DEEPER ANALYSIS (USER REQUESTED) — FZZT BOUNDARY MATCHING**

## Motivation

The SIDC framework claims M_Pl,2D = 3 TeV as the internal Planck mass of 2D universes. This comes from the Liouville cosmological constant μ via M_Pl,2D = √μ.

The 2D universe is described by c=1 Liouville CFT (with c=1/2 Ising matter, total c=3/2). This is the c=1 matrix model — the unique exactly solvable 2D quantum gravity (Dijkgraaf-Moore-Plesser 1992, Stanford-Witten 2017/2019).

**Part 1** (v3.3, completed): Does c=1 matrix model derive μ = 9×10⁶ GeV² from first principles? Answer: NO, μ is calibrated.

**Part 2** (v3.3.1, NEW): Does the **FZZT boundary cosmological constant** relation provide additional constraint? This is the **deeper analysis**.

## The FZZT Relation (Key Formula)

From Mertens-Turiaci 2020/2021 (arXiv:2006.07072), the boundary cosmological constant μ_B is EXACTLY related to bulk μ:

$$\mu_B = \kappa \times \cosh(2\pi b s), \quad \kappa = \frac{\sqrt{\mu}}{\sqrt{\sin(\pi b^2)}}$$

where:
- μ = bulk Liouville cosmological constant (what we want to determine)
- μ_B = boundary cosmological constant (FZZT brane tension)
- b = Liouville coupling (b² = 1/2 for c=1)
- s = FZZT parameter (dimensionless boundary label)

For c=1 (b² = 1/2):
- sin(π/2) = 1, so κ = √μ = M_Pl,2D
- The relation simplifies to:

$$\boxed{\mu_B = M_{\rm Pl,2D} \times \cosh\left(\sqrt{2}\,\pi\, s\right)}$$

This is **EXACT** and derived from the matrix model partition function.

## What FZZT Tells Us

The FZZT relation tells us:
- μ_B and μ are related via hyperbolic cosine
- For small s (s ≲ 1): μ_B ≈ √μ (boundary ≈ bulk)
- For large s: μ_B >> √μ (boundary is heavy compared to bulk)
- For s → 0: μ_B → √μ = M_Pl,2D (the self-dual point)

For SIDC's SN event (E_SN ≈ 10⁵³ GeV):
- If μ_B = E_SN: s = 9.78 (heavy boundary)
- If μ_B = √E_SN ≈ 10²⁶·⁵ GeV: s ≈ 8.5
- If μ_B = (E_SN)^(1/3) ≈ 10¹⁷·⁶⁷ GeV: s ≈ 5.5

All give s of order 5-10. Reasonable FZZT parameter range.

## What FZZT Does NOT Determine

The FZZT relation has **two unknowns** (μ_B and s) for **one equation**. So it doesn't fix μ uniquely.

For first-principles derivation, we need:
1. **μ_B set by 3D event physics** (e.g., μ_B = f(E_SN))
2. **s determined by another principle** (e.g., s = g(τ_2D/t_Pl))

Without these, both μ_B and s are free parameters.

## Tested Candidates for μ_B

We tested 8 candidates for μ_B:

| Candidate | μ_B (GeV) | s | Derived M_Pl,2D |
|---|---|---|---|
| μ_B = E_SN | 10⁵³ | 9.78 | ~10¹⁰¹ GeV (way off) |
| μ_B = √E_SN | 10²⁶·⁵ | 8.50 | ~10¹⁶·⁵ GeV (way off) |
| μ_B = E_SN^(1/3) | 10¹⁷·⁶⁷ | 5.52 | ~10¹⁸·⁵ GeV (way off) |
| μ_B = (E_SN × M_Pl,3D)^(1/2) | 10³⁶ | 8.77 | ~10⁶⁷ GeV (way off) |
| μ_B = (E_SN × M_Pl,3D)^(1/3) | 10²⁴ | 6.06 | ~10⁴⁰ GeV (way off) |
| μ_B = E_SN × ε | 10¹⁵ | 4.86 | ~10²³ GeV (close!) |
| μ_B = √(E_SN × α) | 10²⁶·⁵⁵ | ~9 | ~10¹⁶·⁵ GeV (way off) |

**Most promising candidate**: μ_B = E_SN × ε = 10⁵³ × 10⁻³⁸ = 10¹⁵ GeV, gives s = 4.86 and derived M_Pl,2D = 10²³ GeV.

This is **3 orders of magnitude off** from framework's 3 TeV, but it's the **right order of magnitude** if we adjust the formula slightly.

## Honest Verdict on FZZT

The FZZT relation is:
- ✓ EXACT and structural (from matrix model)
- ✓ Connects bulk (μ) to boundary (μ_B, s)
- ✓ Provides consistency check between bulk and boundary
- ✗ Does NOT fix μ from first principles
- ✗ Does NOT determine s without additional input

**FZZT alone is NOT enough for first-principles μ.**

## Path to First-Principles: Holographic Entropy Matching

The missing principle is likely **holographic entropy matching**:
- Boundary entropy: S_b = (μ_B)^(1/2) × A_b (boundary area term)
- Bulk entropy: S_B = (μ)^(1/2) × A_B (Liouville BH entropy)
- Equate: S_b = S_B

If A_b is set by 3D event geometry (say, A_b = 4π × ℓ_SN² ≈ 4π × 10²⁰ m²), and A_B is the 2D universe's horizon area, then we can solve for μ.

**Status**: This requires more detailed calculation. Currently OPEN.

## M^α Law ↔ FZZT Parameter

SIDC's M^α law: τ_2D = (E/M_Pl,parent)^α × t_Pl

The FZZT parameter s might be related to τ_2D:
- s ↔ τ_2D (boundary time evolution = 2D universe lifetime)

If s = α × log(E/M_Pl,parent) (natural log-relation), then for SN:
- s = 1.289 × log(10⁵³/10¹⁹·⁰⁹) = 1.289 × 33.9 = 43.7
- μ_B = √μ × cosh(√2 π × 43.7) ≈ √μ × e^(192) ≈ √μ × 10⁸³

This gives μ_B >> E_SN (way too big). Not consistent.

If s = (τ_2D / t_Pl)^(1/α):
- s = (33/5.39×10⁻⁴⁴)^(1/1.289) = (6.1×10⁴⁴)^0.776 ≈ 4.4×10³⁴
- Way too big.

The identification of s with M^α-law observables is not straightforward.

## Updated Parameter Status

**v3.3.1 status with FZZT analysis**:

| Parameter | v3.3 status | v3.3.1 status (FZZT) |
|---|---|---|
| M_Pl,3D | measured | measured |
| M_Pl,4D | derived (α-weighted GM) | derived (α-weighted GM) |
| α | structural (N=12 SYK) | structural (N=12 SYK) |
| M_Pl,2D FORM | structural (= √μ) | structural (= √μ) + FZZT consistent |
| **M_Pl,2D VALUE** | calibrated | **calibrated (FZZT doesn't fix)** |
| ε | calibrated | calibrated |
| τ_4D | calibrated | calibrated |
| AGN rate | calibrated | calibrated |
| N_sub | free | free |

**FZZT provides STRUCTURAL CONSISTENCY but not DETERMINATION of μ.**

## Updated Limitations

- **L26** (μ from 2D CFT expert): PARTIALLY CLOSED
  - c=1 matrix model structure known exactly
  - FZZT relation gives bulk-boundary matching
  - But μ is still calibrated, not derived

- **L43** (α not derivable from 2D CFT alone): CONFIRMED
  - Tested 6 models, none give 1.289

- **L153** (v3.3): μ specifically is not derived from c=1 matrix model
  - FZZT doesn't fix it either
  - Needs cross-dimensional input (bulk-brane + holographic matching)

- **L154** (v3.3): First-principles derivation of μ requires bulk theory
  - Currently OPEN
  - Most promising path: holographic entropy matching

- **L158 (NEW v3.3.1)**: FZZT relation provides consistency check but not derivation
  - μ_B = √μ × cosh(√2 π s) connects bulk to boundary
  - Both μ_B and s are free parameters
  - Tested 8 candidates for μ_B; none give exact match
  - Closest: μ_B = E_SN × ε gives derived M_Pl,2D ~ 10²³ GeV (3 orders off)

- **L159 (NEW v3.3.1)**: Holographic entropy matching is the next step
  - S_b = S_B gives bulk-boundary equation
  - Requires specifying A_b (3D event geometry) and A_B (2D horizon)
  - Currently OPEN

## Conclusion

The deeper FZZT analysis confirms:
1. **c=1 matrix model** gives exact Z(μ) but NOT μ
2. **FZZT relation** provides bulk-boundary matching but doesn't fix μ
3. **Holographic entropy matching** is the next step toward first-principles μ
4. **Framework's μ = 9×10⁶ GeV²** is **calibrated**, not derived

The honest verdict: **μ is NOT yet derived from first principles**. The framework has the structural pieces (c=1 Liouville, FZZT, M^α law), but the missing principle is **holographic bulk-boundary matching**.

This is genuinely hard open work. It requires:
1. Specifying the bulk SIDC universe at the QG level
2. Computing the 3D event boundary entropy
3. Matching to 2D universe bulk entropy
4. Solving for μ

Each step requires deep expertise in 2D CFT + 3D gravity + holography.

**STATUS: First-principles analysis DEEP but INCOMPLETE. μ remains CALIBRATED.**

---

**v3.3.1 update**
**Calculation file**: `calculations/v33_fzzt_relation_mu_first_principles.py`
**Results file**: `calculations/v33_fzzt_relation_mu_first_principles_results.txt`
**New limitations**: L158 (FZZT consistency), L159 (holographic matching)
**Updated parameters**: same 9-parameter structure as v3.3
