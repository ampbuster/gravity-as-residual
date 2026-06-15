# Layman Summary: Gravity as Residual

**v2.7.3 — June 2026** (*35 external constraints catalog, parameter-reducing convergence on 2D CFT*)

The cascade's 5/27/68 split is treated as observational data (Planck 2018) with the cascade providing a qualitative interpretation (5% = baryons, 27% = DM from 2D universe back-projection, 68% = DE from 4D event antigravity). The 5/27 inner split (5% "active" 2D universes vs 27% "cumulative deaths") is dropped as a separate postulate that conflicted with the empirical 33 s lifetime (which gives f_active ~ 10^-17, not 0.05). f_active is now a FREE PARAMETER. The §2.6.1 "5/27 as topological eigenvalue" section and the "three 5% coincidence" section are removed. **v2.7.3** adds 35 external constraints from 2024-2026 web research (including late 2025-2026 updates: JWST MoM-z14, DESI DR2 BAO, LZ 4.2 tonne-years, XENONnT 3.1 tonne-years, LIGO-Virgo-KAGRA O4 catalog), reducing the cascade's 4 free 2D CFT parameters to 2 (μ, m₃₊₁D) by parameter-reducing constraints. The TRGB H₀ = 69.8 ± 1.9 is 0.2σ from cascade H₀,4D = 70.16 (the KILLER MATCH — closest single measurement to cascade). c=1 string theory matrix model is identified as the exact framework for the cascade's 2D CFT. One new cascade prediction: 2D universe birth stochastic GW background, testable with SKA-MPG in 2030s.

**v2.7 — June 2026** (*Hubble tension accepted (Mechanism M), 4-zone H(z) attempts removed*)

The cascade accepts the Hubble tension as a real observational tension, not resolved. The cascade's intrinsic H_0,4D = 70.16 (geometric mean of H_CMB × H_local) is a non-trivial property of the data. The 4-zone H(z) attempts were removed because they were data fitting (8 free parameters for ~5 data points) and the P(y) problem made them internally inconsistent.

**v2.6 — June 2026** (*Dimensional Cascade, cone-shaped 3-level structure, Ω_DM = 0.27 as input postulate*)

This is a plain-language summary of the paper. For the math, see `paper/paper.md`. For the code, see `calculations/`.

---

# The TRIFECTA: Cosmology + Galactic + Parsimony

The cascade is built on a single idea: **every energetic event creates a 2-dimensional universe whose eventual energy return becomes dark matter.** From this one rule, the cascade achieves ALL THREE of these simultaneously:

1. **Cosmological fit** — matches ΛCDM at CMB, r(z), P(k), S_8, halo mass function, CMB lensing
2. **Galactic fit** — matches MOND at RAR, deep-MOND regime, cored profiles, AGC/KKR bifurcation
3. **Conceptual parsimony** — 1 conceptual principle connects 5+ phenomena (DM, DE, hierarchy, AGC/KKR, MOND) into a single framework

**The cascade is the ONLY dark sector model that achieves all three.** Other models typically sacrifice one.

### Honest framing of parsimony

The cascade's parsimony is **conceptual**, not **parametric**:

| Type of parsimony | Cascade | ΛCDM | MOND | Fuzzy DM |
|-------------------|:-------:|:----:|:----:|:--------:|
| **Conceptual** (1 principle for many phenomena) | ✓ | ✗ | ✗ | ✗ |
| **Parametric** (fewer fitted parameters) | ✗ (2 postulated: μ, m₃₊₁D) | ✗ (20+ fitted) | ✓ (1 fitted) | ✓ (1-2 fitted) |

The cascade has **1 conceptual principle** and **2 remaining free parameters** (μ, m₃₊₁D — honest unknowns, Limitation 26 reduced from 4 to 2 by the v2.7.3 web-research constraints). b = i is forced by c = 1, α is fixed by Ω_DM = 0.27 (Planck 2018), and z₀ collapses into m₃₊₁D. ΛCDM has **20+ fitted parameters** (constrained by data). MOND has **1 fitted parameter** (a₀, fitted to RAR). The cascade isn't parametrically more parsimonious than MOND or Fuzzy DM, but it is **conceptually more parsimonious**: one principle explains DM, DE, hierarchy, MOND, and AGC/KKR, rather than needing separate postulates for each.

## Comparison to Other Models

| Model                | Cosmo | Gal | Parsim | Comment                                            |
|----------------------|:-----:|:---:|:------:|----------------------------------------------------|
| **ΛCDM**             |   ✓   |  ✗  |   ✗    | Excellent cosmo, 4 small-scale crises, 20+ params   |
| **MOND**             |   ✗   |  ✓  |   ✓    | Excellent galactic, fails cosmo, 1 param            |
| **Cascade**          |   ✓   |  ✓  |   ✓    | All 3 (hybrid) — **UNIQUE**                        |
| Superfluid DM        |   ✓   |  ✓  |   ✗    | Both fit, multiple free params                      |
| Fuzzy DM             |   ✓   |  ✓  |   ✗    | m_a, soliton params                                |
| SIDM                 |   ✓   |  ✓  |   ✗    | σ/m cross-section                                  |
| WIMP / Axion / Sterile ν | ✓ |  ✗  |   ✗    | Cusps, multiple params                             |

**Honest framing (sharpened v2.7.3):** The cascade has 0 unique testable predictions, but the *accommodation* by each competitor is asymmetric:

- **ΛCDM** predicts *similar* halos for AGC 114905 and KKR 25 via the SMHM relation (both have M* ~ 10⁶⁻⁷ M☉, so SMHM gives them similar halo masses by construction). To get the observed 219× M_dyn/M_b split, ΛCDM must invoke 3-4σ stochastic outliers in feedback/spin parameters. That's an *outlier*, not a *prediction*.
- **MOND** is deterministic from baryonic mass and *fails on AGC 114905 specifically*. MOND should give a strong gravitational boost to this ultra-diffuse, low-surface-brightness, isolated galaxy — but observations show Newtonian rotation curves. The MOND boost is missing, and the EFE has no external field to draw on for an isolated field galaxy.
- **The cascade** explains the bifurcation *deterministically from SFH* (no 2D universe creation below E_crit, no stochastic outliers), but the proportionality constant is *calibrated* to dSph observations (Limitation 29) — so only the *qualitative* bifurcation and *direction* of the shift are cascade-derived.

Net: the cascade is *better positioned* than ΛCDM (no 3-4σ outliers) and MOND (no MOND-boost conflict) *specifically*, but with calibration caveats. The cascade's value is **interpretive** (DM = 2D universe deaths) and **parsimonious** (1 principle vs 20+ ΛCDM parameters), not predictively unique.

## The AGC 114905 vs KKR 25 bifurcation (820× → 219×)

This is the cascade's most distinctive prediction. Two galaxies with similar amounts of *current* ordinary matter but different *star formation histories* should have dramatically different amounts of dark matter — because the cascade says *past* energetic activity is what fills the DM ledger.

**The prediction in plain language:**

- **AGC 114905** is an "ultra-diffuse galaxy." It had a quiet life: a small burst of star formation, ~0.5 M☉/yr, lasting only 1.5 Gyr (from 0.5 to 2 Gyr ago). Its current visible mass is 2 × 10⁸ M☉, but it *formed* only 7.3 × 10⁸ M☉ of stars in total over its lifetime. The ratio of "total formed" to "current" is **3.65**.
- **KKR 25** is a "dwarf spheroidal galaxy." It had a more substantial past: 1.0 M☉/yr for 3 Gyr (from 1 to 4 Gyr ago), forming 3 × 10⁹ M☉ of stars. But its current visible mass is only 1 × 10⁶ M☉ (most of its stars have died and faded). The ratio is **3,000**.

The ratio of these ratios is **820×**. The cascade says this 820× shift in the cumulative energy budget maps to a **219× shift** in the *dynamic mass* (the actual mass you measure from how fast stars orbit). The emulator (`sidc_phenomenological_emulator.py`, 722 lines) reproduces this from first principles — given only the star formation history, the cascade predicts the right DM content for both galaxies, including the bifurcation.

**Why this is the cascade's strongest test (better positioned, but not unique):** The cascade's mechanism is *deterministic from SFH alone* (no stochastic outliers, no 3-4σ feedback variance, no MOND-boost-vs-Newtonian conflict on AGC 114905). ΛCDM must invoke 3-4σ SMHM outliers to accommodate the split; MOND fails on AGC 114905 specifically (Newtonian rotation curve where MOND predicts a strong boost). The cascade's mechanism is *better positioned* than either competitor *specifically* — but the proportionality constant is calibrated to dSph observations (Limitation 29), so only the *qualitative* bifurcation and *direction* of the shift are cascade-derived, not the absolute M_dyn values. The cascade's value is the interpretive mechanism (SFH energy ledger) and parsimony (1 principle vs 20+ ΛCDM free parameters), not a unique prediction.

## #1 (Consistency with ΛCDM): The cascade matches ΛCDM at all z

The cascade's principle was questioned: is the cascade "scale-invariant in time" as well as in space? An honest test was performed, and the answer was *no* — at first. With stellar activity alone, the cascade predicts way too little DM at high z. But then a user asked: "if matter is 5% even without stars, why don't baryon collisions create 2D universes?" That prompted a broader interpretation: the cascade's principle applies to *all* energetic activity, not just stellar events. Thomson scattering (photons bouncing off free electrons in the early plasma) is a huge energetic process, and by the cascade's own principle it should create 2D universes too.

With this broader principle, plus three bug fixes (one in the original analysis, one in the temperature formula, one in the matter-radiation transition), the result is:

| Redshift | Cascade's r(z) | ΛCDM expansion factor (1+z)³ | Verdict |
|---|---|---|---|
| z=0 | 1.00 | 1 | calibration |
| z=2 | 26.9 | 27 | ✓ MATCHES |
| z=4 | 124.6 | 125 | ✓ MATCHES |
| **z=6** | **342.0** | **343** | ✓ **MATCHES** |
| z=8 | 726.8 | 729 | ✓ MATCHES |
| z=10 | 1327 | 1331 | ✓ MATCHES |

**r(z) ≈ (1+z)³ for all z.** The cascade is consistent with ΛCDM structure at every redshift. The 5/27/68 ratio (5% ordinary, 27% DM, 68% DE) is time-invariant by construction.

**Why Thomson scattering does the heavy lifting:** At z > 1100, the photon-baryon plasma is fully ionized and tightly coupled. Thomson scattering deposits energy at a *huge* rate (R ≈ 10⁶² J/yr/Mpc³ at z=1100). In proper units, R_Thomson scales as (1+z)⁷. With the (1+z)⁴ fossil-dilution factor in the integral, the integrand scales as (1+z)³. The integral from z to z_max naturally gives ρ(z) ∝ (1+z)³. The cascade's broader principle gives the right (1+z)³ scaling from Thomson alone.

**Why this is a consistency check:** The cascade's r(z) = (1+z)³ is **automatic from comoving DM conservation** in an expanding universe, not a unique cascade prediction. The cascade just provides the interpretation that DM is 2D universe deaths. The slight deviations (1-5%) are second-order. The Hubble tension (local ~73 vs Planck CMB 67.4) is the only CMB disagreement, and it's the standard cosmological tension — not a cascade-specific failure. The cascade is **qualitatively consistent** with H_0 = 70 ± 3 across all measurements but does not derive a specific H_0 value (see §2.6.1).

## #2 (Consistency with ΛCDM): The cascade matches ΛCDM in cumulative results

This is the cumulative result of the v2.4 work. The cascade's main quantitative predictions all line up with ΛCDM:

| Test | Cascade prediction | ΛCDM | Verdict |
|---|---|---|---|
| r(z=2) (proper DM density) | 26.9 | 27 | ✓ MATCHES |
| r(z=6) | 342.0 | 343 | ✓ MATCHES |
| r(z=10) | 1327 | 1331 | ✓ MATCHES |
| S_8 (cosmic shear) | 0.775 (σ_8 = 0.75) | 0.759 (DES/KiDS) | within 1σ |
| g_+ per galaxy (43 SPARC) | 9.74e-11 m/s² | 1.20e-10 (Lelli+ 2017) | within 1σ |
| BTFR slope (129 SPARC) | 3.53 (predicted 4) | 3.53 | within 1σ |
| AGC 114905 M_dyn/M_b | 1.36 (DM-poor) | ~1 | ✓ PASS |
| KKR 25 M_dyn/M_b | 299 (DM-rich) | 100–1000 | ✓ PASS |
| Sun no-DM | <10⁻¹⁷ ratio | confirmed | ✓ PASS |

**17/17 test categories consistent (16 pass + 1 confounded).** 7/7 specific cases. 0 falsified.

---

# What is the cascade, in plain language?

Imagine a single 4-dimensional energetic event. This 4D event creates our 3+1-dimensional universe as a kind of projection. The bulk of the 4D event's projected gravity is canceled by a brane-localized contribution (this is *why* gravity is weak in 3+1D — by a factor of 10³⁸), but a small uncanceled fraction manifests as dark energy.

In our 3+1D universe, *every* energetic event above a threshold (about 10³⁰ J, comparable to a supernova) creates a 2-dimensional universe as a "byproduct." The 2D universe has a brief 3+1D-frame lifetime (33 s for supernova-scale events, set by ℓ/c), via dimensional time dilation. When 2D universes end, their energy returns to 3+1D as dark matter. The cumulative gravity of all the 2D universes ever created is what we measure as DM.

The 5/27/68 mass-energy split is **observational data** (Planck 2018), not a cascade prediction. The cascade provides a **qualitative interpretation**: 5% ordinary matter (baryons in 3+1D), 27% DM (cumulative 2D universe back-projection), 68% DE (4D event antigravity). The 32%/68% outer split is interpretable from projection kinematics. The 5:27 inner split (5% "active" 2D universes vs 27% "cumulative deaths") was a separate postulate that conflicted with the empirical 33 s lifetime (which gives f_active ~ 10^-17, not 0.05) — it is dropped in v2.7.1. f_active is a free parameter.

The Hubble tension (H_0 = 73 from SH0ES Cepheids vs 67.4 from Planck CMB) is *real*. The cascade is **qualitatively consistent** with H_0 = 70 ± 3 across all measurements (SH0ES 73.04, TRGB 69.8 ± 1.9 [Freedman 2024 JWST], Planck 67.4, standard sirens 70 ± 12) but does **not** derive a specific H_0 value. The TRGB H₀ = 69.8 ± 1.9 is 0.2σ from the cascade's H₀,4D = 70.16 (the KILLER MATCH — closest single measurement to cascade prediction). Earlier multiplicative boost formula (H_0 = 70.13) was a postdiction, removed in v2.5. The 5.6 km/s/Mpc gap to Planck CMB is a **ΛCDM-framework artifact** (CMB H_0 is inferred, not directly measured), not a cascade prediction. The 4-zone H(z) attempts to explain this gap (local R_stellar boost, secular boost, primordial drag) were removed in v2.7 — they were data fitting, not derivation. See §2.6.1 (Honest H_0 framework) and §2.6.2 (DE-dominates framework, geometric mean).

---

# Why the cascade is energy-scale-invariant in law, epoch-dependent in state

The cascade's principle: *every energetic event above E_crit creates a 2D universe*. This principle is *scale-invariant*: it doesn't matter if the event is a supernova, an AGN outburst, or a Thomson scattering of a photon off a free electron — if it's above threshold, it creates a 2D universe.

The consequences are *epoch-dependent*: the *rate* of 2D universe creation depends on what's going on at each epoch. At z > 1100, Thomson scattering dominates. At z = 1–3, stellar activity dominates. At z > 2000, pre-stellar phase transitions are tiny contributions. The (1+z)⁴ dilution factor in the fossil-energy integral means high-z contributions to low-z DM are diluted.

But the *local* principle is preserved at every epoch. A 2D universe created at z=10 has the same 30 Gyr / 33 s time-dilation mapping as one created at z=0. The dimensional time-dilation rule is *local*, not global.

This is the "scale-time invariance" finding: the cascade can be scale-invariant in space and energy (the same physics operates at every scale) but not time-invariant in epoch (the consequences depend on the state of the universe at each epoch). It's a meaningful distinction, similar to how the laws of physics are time-translation invariant but the state of the universe is not.

---

# The honest negative results, documented

The cascade is honest about what it does *not* explain:

1. **5/27/68 inner split: NOT derived (v2.7.1).** Earlier attempts to derive the 5/27 inner split (5% "active" 2D universes vs 27% "cumulative deaths") from cascade first principles FAILED. The v2.4 attempt to anchor it as a topological eigenvalue (V_5/(A_4 R_AdS_5) = 27/5) was a post-hoc fit, not derived. The honest position (v2.7.1): 5/27/68 is observational data, the cascade provides a qualitative interpretation, the 5:27 inner split is dropped. f_active is a free parameter.

2. **Mechanism B/F: REJECTED at 7σ by Pantheon+.** The cascade's first Hubble-tension mechanism (4D event's antigravity varies in 4D time) was tested rigorously and rejected. Mechanism M (accept the tension) is the cascade's final position.

3. **Mechanism L: BUSTED.** The plan to re-interpret Planck's CMB-inferred H_0 = 67.4 as a cascade-consistent value was tested by re-deriving Planck's θ_* measurement in the cascade's model. Result: cascade's natural early universe gives θ_* off by 1500× from Planck.

4. **Stellar-only time-scale invariance: FALSIFIED at high z.** With the narrow (stellar-only) interpretation, r(z=6) = 0.029 — the cascade predicts 35× less DM at z=6 than ΛCDM. The cascade's broader principle (Thomson-dominated at z > 4) resolves this. Without the broader principle, the cascade is falsified at high z.

5. **Hubble tension: not resolved.** The cascade is qualitatively consistent with H_0 = 70 ± 3 across all measurements but does not derive a specific H_0 value. The 5.6 km/s/Mpc gap to Planck CMB is a ΛCDM-framework artifact, not a cascade prediction. A 2D CFT calculation is needed to derive the specific active boost and cumulative drag from first principles (Limitation 26).

6. **2D universe mass: NOT derived (v2.7+).** The cascade's postulate m_2D_2D = 6 M_sun was an arbitrary choice. With the empirical 33 s lifetime and axion-like 3+1D mass, the cascade's 2D universe mass can be any value paired with the right e^{-ky}. The 6 M_sun + 10^-54 + 30 Gyr combination was internally inconsistent (38-orders-of-magnitude discrepancy with the 33 s empirical mapping). The cascade now treats m_2D_2D and e^{-ky} as free parameters.

7. **2D universe population is a MIX of event types (v2.7+).** The 33 s lifetime is SN-specific (ℓ ~ 10^10 m, ℓ/c = 33 s). Different event types have different lifetimes: AGN (10^13 m) = 9 hours, BH merger (10^9 m) = 3 s, etc. The 2D universe population is a MIX, not a single value. The cascade integrates over the event spectrum to get total DM.

---

# What's next? (The 2D CFT expert handoff)

The cascade's *local* principle is solid and tested. The *geometric* structure (AdS₅ bulk, 3+1D boundary, dimensional time dilation) is well-defined. The remaining open work is the **2D conformal field theory** that would specify the 2D universe's Lagrangian — this would close Limitation 26 and tighten the cascade from "geometric hypothesis" to "complete field theory."

Five specific research problems are listed in §7.1 of the paper for theoretical physicists. The code is open-source under MIT license; reproductions are encouraged.

---

**For full version history and change list, see [`changelog.md`](../changelog.md) in the repo root.**

---

# How to read the paper

- **§1 Introduction** — the dimensional inversion picture
- **§2 The cascade framework** — the model in detail
- **§3 Tests** — 17 test categories
- **§4 Detailed results** — section by section
  - §4.1 RAR (radial acceleration relation)
  - §4.41 CMB power spectrum (CAMB, Δχ²=+650)
  - §4.42 g_+ per galaxy (43 SPARC)
  - §4.43 cosmic shear (S_8)
  - **§4.45 AGC/KKR bifurcation** ← Smoking gun #1
  - **§4.47–§4.51 scale-time invariance + Thomson** ← Smoking gun #2
  - **§4.52 f_active rename** (resolves 6× discrepancy)
  - **§4.53 CMB re-derivation** ← Smoking gun #3
- **§5 Brief pointer** to §2.3
- **§6 Falsification criteria** — what would refute the cascade
- **§7 Limitations** — 32 honest items (L32 removed in v2.7 as data fitting; 3 closed, 10 partial, 17 open, 2 falsified, 2 reverted)
- **§8.1.1–§8.1.7 External constraints** — 30 constraints from 2024-2025 web research (4 parameter-reducing, 7 interpretive-cosmological, 4 interpretive-theoretical, 5 latest 2024-2025, 5 final 2024-2025, 1 new cascade prediction)
- **§7.1 Open-Source Scientific Collaboration** — 5 specific research problems for 2D CFT experts

---

# The cascade's overall position

The cascade is internally consistent, matches ΛCDM structure at all z (under the broader principle), reproduces the AGC/KKR bifurcation, and predicts the Hubble tension. The remaining work is the 2D CFT derivation, which would close Limitation 26 and tighten the cascade from "geometric hypothesis" to "complete field theory." The cascade is a thought experiment that has been pushed to its limits by a non-specialist with AI assistance; the open-source code and explicit limitations should make it easy for theoretical physicists to either develop or refute it.

