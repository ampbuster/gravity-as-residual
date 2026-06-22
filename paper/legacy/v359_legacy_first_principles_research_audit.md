# v3.5.9+ A2 — Web Research Audit for First-Principles Derivations (2026-06-22)

**Context**: User requested a follow-up web research sweep targeting the open
first-principles gaps: L43 (α from 2D CFT), L138 (M_Pl,4D closed derivation),
L144 (N_sub first-principles), L142a (4π geometric origin).

**Goal**: Determine whether any 2024-2026 literature offers a CLOSED
first-principles derivation of these quantities that would let us promote
them from STRUCTURAL/CALIBRATED → FIRST-PRINCIPLES.

**Verdict (TL;DR)**: **No closed first-principles derivations found.**
All four gaps remain at their current v3.5.9+ A2 status. The closest
literature results are *consistent with* the cascade's values but do not
*derive* them. Several promising candidates were re-examined and found
to be (a) require framework-specific ICFT calculations not yet done, (b)
involve free parameters in the literature, or (c) only verify the formula
shape, not the numeric values.

This is an **honest negative result**, not a research failure. It documents
that we did the search, what we found, and why each candidate falls short
of closing its target limitation.

---

## L43 — α from 2D CFT: Already at "1st-principles via Schwarzian SYK N=12"

**Current v3.5.9+ A2 status**: PARTIAL CLOSURE via L308n
(α = 1 + 1/√12 = 1.2886751346, matches framework 1.289 within 0.025%)

**Research sweep**:
- HKS bound (Hartman-Keller-Stoica 2024, arXiv:1405.5137) — proven
  universal inequality on 2D CFT partition function. Constrains F(βL)
  in large-c limit, but does NOT predict α = 1.289. Provides
  *consistency check* that SIDC's c = 3/2 ICFT structure is admissible
  (SIDC is non-unitary Liouville + SYK, so Hellerman bound c ≤ 1 is
  not violated despite the framework's value).
- HKS conjecture proves a 1-parameter family of universal inequalities;
  not specific to Schwarzian SYK N=12.
- JT gravity on finite geometry (Frank Ferrari, BICMR Dec 2025 talk) —
  gives a "new type of boundary condition" with fluctuating boundary,
  but does not produce α directly. It would give a new combinatorial
  problem for α extraction.
- Schwarzian QM / JT gravity derivations (Callebaut-Verlinde, Maxfield-
  Turiaci, etc.) all confirm Schwarzian structure of near-extremal
  black holes, but α in SIDC's sense is the *gravitational power-law
  exponent* (E_2D/E_3D) = (E_3D/M_Pl,3D)^α, NOT the Schwarzian
  coefficient c_s = 1/√N. The Schwarzian coefficient gives
  α = 1 + 1/√N (L308n derivation). This is a NEW result that
  combines SYK + Schwarzian. No off-the-shelf literature gives
  α from N=12 directly — this is a framework-specific derivation.

**Verdict**: L43 already has the strongest available first-principles
derivation (L308n). No 2024-2026 literature improves on this. The
remaining "5/27 derivation attempts" all failed in v3.0-v3.0.22 and
the conclusion holds: α needs framework-specific input (cross-couplings,
observable identification) that no off-the-shelf CFT provides.

---

## L138 — M_Pl,4D closed derivation: α-GM is the best available

**Current v3.5.9+ A2 status**: PARTIAL CLOSURE via L308v (α-GM with
all first-principles inputs, 1.2% match to framework value 3.93×10²³ GeV)

**Research sweep**:
- Kuntz-Trautner 2023/2025 (arXiv:2312.09853, "Extra Dimensions Beyond
  the Horizon"): extra-dimensional braneworld with hyperbolic warp
  factor. 4D Planck AND 4D cosmological constant determined by two
  bulk scales: extra-dim radius R and visible-brane-to-horizon distance
  R₀. This is CLOSE to the cascade's spirit — both scales appear in
  their 4D Planck derivation. But: it requires specifying a 5D
  geometry (circle compactification) and the relationship between
  R, R₀, and the visible-brane 4D effective theory is a FREE choice
  in their framework. Doesn't give M_Pl,4D as a closed function of
  known quantities.
- Standard Model scales from warped extra dimensions (arXiv:0809.0111):
  "Scales on successive branes in the extra dimension descend from
  Planck scale in a geometric sequence of common ratio 1/π." This is
  similar to SIDC's α-GM self-similar structure, but the common
  ratio 1/π doesn't match α = 1.289. Could be modified but isn't a
  derivation in SIDC's sense.
- New warped extra dimension models (PhysRevD.98.085022, 2018):
  parallel approach to hierarchy problem; doesn't give a specific
  M_Pl,4D formula derivable from SIDC's M_Pl,3D, M_Pl,2D, α inputs.
- No-scale Brans-Dicke (arXiv:2503.18648, Mar 2025): treats M_Pl as
  emergent from no-scale SUSY, gives a massless scalar. Doesn't
  produce M_Pl,4D as a specific value.
- Riley 2008 formula (referenced in framework): n=9.07, close to
  integer 9 but not exact. The "1.6% off" pattern from α-GM also
  appears in Riley's independent approach. This is an interesting
  cross-check but not a derivation.

**Verdict**: L138 is already at PARTIAL CLOSURE (α-GM closed loop).
The α-GM formula IS a structural relation (weighted geometric mean)
encoding the cascade's self-similarity. No 2024-2026 literature gives
a CLOSED first-principles derivation independent of SIDC's structure.

**Honest framing**: The α-GM is not derived from a deeper principle —
it IS the principle. The cascade's self-similar structure is encoded
in α. If you want a derivation of α-GM, you'd need to derive the
self-similar structure, which is what L43 already does (via Schwarzian
SYK N=12).

---

## L144 — N_sub first-principles: N_12 × (M_Pl,4D/M_Pl,3D)^(1/3) is the best available

**Current v3.5.9+ A2 status**: PARTIAL CLOSURE via L308ad
(N_sub ≈ N_12 × (M_Pl,4D/M_Pl,3D)^(1/3) = 381.8, framework 386,
1.6% match)

**Research sweep**:
- Holographic principle: N_sub = A_3D / l_Pl,4D² gives 10^185
  (way too many). This was already tried in L308ad and confirmed
  not to work. The cascade's N_sub is NOT a holographic bound —
  it's a generation-counting rule (12 fermion DOFs × geometric
  cube-root factor).
- Bousso holographic bound reviews (2002): entropy bound is
  S ≤ A/(4 l_Pl²), not a particle/event count. Doesn't apply.
- 3D flat cosmological horizons (PRL 110.141302, 2013): first
  derivation of Bekenstein-Hawking entropy for 3D horizons via
  2D CFT dual. Confirms holographic structure of cosmological
  horizons. Could potentially give N_sub via 2D CFT state count
  for horizon microstates, but: (a) the framework's 2D CFT is
  c = 3/2 non-unitary, not the standard c ≫ 1 limit, (b) the
  calculation is event-specific (would need to be done for each
  4D event), (c) no closed formula emerges in the literature.
- Cosmic holography (Bak & Rey, 2000): bounds particle entropy
  within cosmological apparent horizon. Not a count of sub-universes.
- MDPI Holographic Bound in Newtonian Cosmology: total entropy
  bounded at 10^123 k_B, not N_sub.
- Cribiori-Tonioni 2025 (arXiv:2507.02738, Jul 2025): UV/IR mixing
  bounds scalar field range in inflationary scenarios, gives
  relation between extra dimensions and tensor-to-scalar ratio.
  Doesn't give N_sub.
- No 2024-2026 paper derives "number of sub-universes per 4D event"
  in a cascade/multiverse model. N_sub is a SIDC-specific quantity
  (specific to the framework's "sub-universe" definition, which
  is 4D events that undergo 2D→3D→4D cascade with γ_4D time
  dilation).

**Verdict**: L144 is at PARTIAL CLOSURE (L308ad). The cube-root
formula N_sub ≈ N_12 × (M_Pl,4D/M_Pl,3D)^(1/3) makes dimensional
sense (3 spatial dimensions of 3+1D → cube root, ×12 fermion
channels) and matches 1.6%. No literature result offers a better
derivation.

**Honest framing**: N_sub is the "sub-universe count" in a model
where each 4D event creates sub-universes. This is a SIDC-specific
construction; it's not a standard cosmological quantity in the
literature. The cube-root formula is a SIDC structural insight,
not a literature derivation.

---

## L142a — 4π geometric origin: S² boundary hypothesis is the best available

**Current v3.5.9+ A2 status**: PARTIAL CLOSURE via §7.4.8
(4π = surface area of S² = boundary of 3-ball, structural pattern
from cascade progression)

**Research sweep**:
- Surface area of unit sphere in n dimensions: S^{n-1} has area
  2π^{n/2}/Γ(n/2). For S² (n=3): 4π. For S¹ (n=2): 2π. This is
  the geometric fact underlying the framework's 2π → 4π progression.
- Gauss law and divergence theorem: 4π appears naturally in 3D
  Gauss's law for inverse-square forces (gravity, EM). This is
  the framework's "DM is 3+1D inverse-square" claim.
- Brane boundary geometry: arXiv:2411.16033 (Rak-Kyeong Seong,
  Apr 2025) on generative AI for brane configurations — uses
  coamoeba projection of mirror curves, not directly relevant
  to 4π origin.
- "Warped geometry of brane worlds" (NASA ADS 2002CQGra..19.2983F):
  2D phase portrait for flat branes, doesn't give 4π specifically.
- Pure geometric f(R) branes (CERN 2025, PLB 139718): f(R)
  cosmology on 5D branes, doesn't produce 4π.
- A Dynamical Hypothesis in (3,2)-Dimensional Spacetime
  (arXiv:2606.12457): single extra spatial dimension ruled out
  as superluminal mediator. Doesn't give 4π.
- Holographic entropy bound from quantum geometry (PRD 63.044019,
  2001): Chern-Simons boundary description, doesn't produce 4π
  in SIDC's sense.
- Holography of 3D flat cosmological horizons (PRL 110.141302):
  CFT state counting for 3D horizons. Could potentially give
  4π in some thermodynamic limit, but not derived.

**Verdict**: L142a is at PARTIAL CLOSURE (S² boundary hypothesis).
The 4π factor has multiple geometric origins (sphere area, Gauss
law, divergence theorem), all consistent with the framework's
"3+1D is inverse-square" claim. No literature offers a unique
DERIVATION (only multiple consistent INTERPRETATIONS).

**Honest framing**: 4π appears naturally in 3+1D physics. The
framework's contribution is recognizing that the 2π → 4π progression
is geometrically motivated (each cascade level's transition factor
= surface measure of parent's boundary sphere). This is structural
pattern-matching, not a derivation from first principles.

---

## Cross-Cutting Observations

1. **All four gaps are at PARTIAL CLOSURE in v3.5.9+ A2.** The
   framework already has the strongest available derivations
   (L308n for α, L308v for M_Pl,4D, L308ad for N_sub, §7.4.8
   for 4π). No literature sweep improves on these.

2. **The "free parameters" problem is structural, not a research gap.**
   The framework has 4 truly free parameters (M_Pl,3D measured, ρ_DE,
   AGN rate, N_sub). Of these, M_Pl,3D is MEASURED, and the other
   three are at structural/calibrated status. Promotion to FIRST-
   PRINCIPPLES would require framework-specific calculations that
   the current literature doesn't provide.

3. **The cascade is not a "mainstream" model.** Searches for
   "sub-universe count from holographic bound" or "α = 1 + 1/√N
   from Schwarzian" don't return SIDC-like results because the
   framework is original. The first-principles derivations we have
   (L308n for α, L308ad for N_sub) are framework-specific insights,
   not literature imports.

4. **The 1.6% / 1.2% / 0.025% matches are at the framework's
   intrinsic precision.** α-GM at 1.2%, cube-root formula at 1.6%,
   Schwarzian at 0.025% — all are within framework rounding. These
   are NOT exact matches, and we should not pretend they are. They
   are CONSISTENT with first-principles inputs, not DERIVED from
   them.

5. **Future research directions** (none of which are doable in a
   web search):
   - Compute the full combined Z = Z_Liouville × Z_Schwarzian × Z_SYK
     path integral (L43 strengthening)
   - Derive α-GM from a specific 6D compactification (L138
     strengthening, Riley 2008 n=9.07 → n=9 closure)
   - Compute N_sub for a specific 4D-bulk dynamics (L144 closure)
   - Derive 4π from S² boundary dynamics in a specific bulk
     Lagrangian (L142a closure)
   These require framework-specific theoretical physics work,
   not literature imports.

---

## Files Updated by This Research

- This file (paper/legacy/v359_legacy_first_principles_research_audit.md)
  documents the audit and its negative result.

## Files NOT Updated

- 06_limitations.md: status of L43/L138/L144/L142a already reflects
  the best available first-principles derivations (L308n, L308v,
  L308ad, §7.4.8). No literature sweep improves on these.
- paper.md: no changes needed.
- All other docs: no changes needed.

## Recommendation

Keep the current v3.5.9+ A2 status:
- **L43**: PARTIAL (α first-principles via Schwarzian SYK N=12)
- **L138**: PARTIAL CLOSURE (α-GM closed loop, 1.2%)
- **L144**: PARTIAL CLOSURE (N_12 × (M_Pl,4D/M_Pl,3D)^(1/3), 1.6%)
- **L142a**: PARTIAL (S² boundary hypothesis, structural)

These are honest statements of what we know. The web sweep confirmed
that no off-the-shelf literature closes these gaps. Future closure
requires framework-specific theoretical work, not literature imports.

---

**Date**: 2026-06-22
**Author**: Mavis (with user direction)
**Context**: v3.5.9+ A2, 479 pages (was 478 pre-consistency-sweep), 144 master table limitations
**References**: Searches covered 2023-2026 literature on:
holographic bounds, JT gravity, Schwarzian derivatives, brane
cosmology, multi-universe models, entropy bounds, and Planck scale
derivations in extra-dim models. Total: ~30 search queries, ~150
results examined. No closed first-principles derivations found.
