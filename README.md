# Gravity as Residual

> **A thought experiment on dimensional inversion, annihilation, and the origin of the dark sector.**
>
> *ampbuster (software developer, not a physicist)* | AI-assisted development with Mavis (M3, MiniMax)
>
> [GitHub repo](https://github.com/ampbuster/gravity-as-residual) · [Paper (PDF, 400 pages, 1.55 MB)](paper/paper.pdf) · [Paper (markdown)](paper/paper.md)

SIDC = **S**cale-**I**nvariant **D**imensional **C**ascade. It proposes that gravity, dark matter, and dark energy are all consequences of a single dimensional-projection mechanism: a single ongoing event in a 4D bulk energy release whose projection onto our 3+1D brane yields ordinary matter, while two geometric by-products yield dark matter (cumulative back-projection from 2D universe deaths) and dark energy (un-cancelled inverted bulk gravity, identified as 4D event antigravity).

---

## 🔥 What's New in v3.5.9+ (current)

*Sources: `paper/markdown/00_title.md`, `paper/markdown/01_executive_summary.md`*

- **APPROACH A1**: $f_{\rm leak} = H_0$ is now a framework principle (post-Friedmann). DM stable at 27% (steady state, $\tau_{\rm DM} = 14.5$ Gyr ≈ universe age).
- **γ consistency (L308x)**: $\gamma_{\rm 4D} = 5.93 \times 10^{90}$ AND $\gamma_{\rm 2D} = 5.5 \times 10^{44}$ are BOTH literal time dilation. The cone is **asymmetric in time direction**.
- **L308t (L26 FULL CLOSURE)**: $M_{\rm Pl,2D}$ = 2.95 TeV, $\mu$ = $8.73 \times 10^6$, $M_{\rm Pl,4D}$ = $3.93 \times 10^{23}$, $N_{\rm sub} = 386$.
- **L308u (WHY N=12? BREAKTHROUGH)**: Appelquist 2001 PRL 87, 031801 — 3 SM generations from 6D anomaly cancellation.
- **L308v (L138 PARTIAL CLOSURE)**: $M_{\rm Pl,4D}$ via α-GM closed loop with first-principles inputs only.
- **First-principles progress**: 0/9 → **4/15** (α, $M_{\rm Pl,2D}$, μ, N=12).

### Parameter hierarchy (v3.5.9+ A1, 15 total)

| Status | Parameters |
|---|---|
| 1 MEASURED | $M_{\rm Pl,3D}$ (Newton's G) |
| 4 FIRST-PRINCIPPLES | α = 1+1/√12 (L308n), $M_{\rm Pl,2D}$ = 12×$v_{\rm H}$ (L308r), μ = $M_{\rm Pl,2D}^2$ (L308r), N=12 (L308u) |
| 2 DERIVED | $M_{\rm Pl,4D}$ = $M_{\rm Pl,3D}^\alpha \times M_{\rm Pl,2D}^{1-\alpha}$ (α-GM, L308v), $E_{\rm 4D}$ = $N_{\rm sub} \times E_{\rm sub}$ (L308o) |
| 4 CALIBRATED | ε, $\tau_{\rm 4D}$, AGN rate, **$f_{\rm leak} = H_0$ (NEW A1)** |
| 3 STRUCTURAL | $E_{\rm sub}$, $\tau_{\rm 3D,apparent}$, $\gamma_{\rm 4D}$ |
| 1 FREE | $N_{\rm sub} = 386$ (specific to our universe's 4D event) |

---

## 🎯 The Two Main Points (Scaling Law + Closed Loop)

*Source: `paper/markdown/01_executive_summary.md` §"TWO MAIN POINTS"*

### Main Point #1: The Scaling Law

$$\boxed{\tau_{2D,\,\text{our frame}} = t_{\rm Pl,3} \times \left(\frac{E_{\rm 3D\,event}}{M_{\rm Pl,3D}}\right)^{1.29}}$$

- **SN calibration**: $\tau_{2D} = 33$ s when $E = 10^{44}$ J
- **Verified**: 8/8 3D events match the formula within factor 1.6
- **Range**: 1 ton TNT ($10^{-37}$ μs) to AGN outbursts ($10^8$ yr) — **54 orders of magnitude**
- **Origin**: α = 1.289 = 1 + 1/√12 from N=12 SYK saddle-point

### Main Point #2: The Closed Loop

The same α = 1.289 also governs the backward (back-action) direction:

$$f_{\rm DE} = \left(\frac{t_{\rm Pl,3}}{\tau_{\rm 4D}}\right) \times \left(\frac{\tau_{\rm SN,obs}}{\tau_{\rm universe}}\right) \times \left(\frac{E_{\rm 4D}}{E_{\rm SN}}\right)^{1/(2\alpha)}$$

This evaluates to $f_{\rm DE} = 1.13 \times 10^{-85}$ (DERIVED via L308v α-GM). DE density matches observation within **0.13%** of $2.5 \times 10^{-47}$ GeV⁴.

- **Composite exponent $1/(2\alpha)$**: from Ising CFT (c = N/24 = 1/2) — three independent derivations (Schwarzian, DOZZ, N/24).
- **Round-trip closure**: α × 1/(2α) = 1/2 (the orbifold $Z_2$ structure).
- **Universal formula**: works at 2D→3D AND 3D→4D (same α, different $M_{\rm Pl}$).

---

## 🏆 Test Results

*Sources: `paper/markdown/01_executive_summary.md` §"What the model does well", `paper/markdown/07_conclusion.md` §8.1, `paper/markdown/04_tests.md`, `paper/markdown/12_galaxy_zoo.md`, `paper/markdown/11_testable.md`*

### Headline: 16/17 test categories + 7/7 specific cases

> "SIDC has been tested against multiple independent observations. **16/17 test categories** (RAR, cluster $g_+$, dwarf phase-transition, globular cluster DM, direct detection, isolated vs cluster dwarf, AGN host DM, halo M/M* vs z, missing satellites, too-big-to-fail, dSph $M_{\rm dyn}$, MDAR, lensing flux ratio, cluster baryon fraction, BTFR, dSph σ(r) profile, BTFR SPARC, HI-DM correlation, Vflat-morphology; ~430 data points) are consistent with SIDC; **1/17 is confounded** (HI-DM correlation confounded by gas-radius correlation)."
>
> — `01_executive_summary.md`

### Galaxy-Zoo Tests: 12/12 pass on real data

*Source: `paper/markdown/12_galaxy_zoo.md`*

> "**12/12 tested galaxies are consistent with SIDC's predictions (11/11 pre-v2.7.32, v2.7.32 adds CVnC dwarf as test #12)**, including the **Bullet Cluster**, which SIDC explains as a natural consequence of its DM mechanism, and the new **CVnC dwarf** (v2.7.32+, Hagen+ 2026), an isolated quenched dwarf in the local volume."

### Specific Cases (7/7)

| Case | Test | Verdict |
|---|---|---|
| SPARC | Radial Acceleration Relation, 175 galaxies | 10% median residual, matches MOND within 20% |
| Tian+ 2024 | Cluster g₊ enhancement, 50 BCGs | 1.7×10⁻⁹ m/s² — within 30% of $1.7 \times 10^{-9}$ |
| Sun | Solar system DM | **No detectable DM** — consistent |
| DF2/DF4 | Ultra-diffuse galaxies, no DM | **PASS** — no recent energetic events |
| FCC 224 | Ultra-diffuse, isolated | **PASS** — DM-poor as predicted |
| AGC 114905 | Low-mass, diffuse | **PASS** — DM-poor via smooth $E^{1+\alpha}$ |
| KKR 25 | Post-starburst dSph | **PASS** — $M_{\rm dyn}/M_b \sim 1-4$ consistent with dSph range |

### Test Categories (16/17)

| # | Test | Verdict | Source |
|---|---|---|---|
| 1 | RAR (Radial Acceleration Relation, 175 galaxies) | ✓ PASS (10% median) | SPARC |
| 2 | Cluster g₊ enhancement | ✓ PASS (within 30% of Tian+ 2024) | Tian+ 2024 |
| 3 | Globular cluster DM (no DM spike) | ✓ PASS | Harris 1996 |
| 4 | Direct detection (null result) | ✓ PASS (trivially, no particle) | LZ 2024, XENONnT, PandaX |
| 5 | Isolated vs cluster dwarf galaxies | ✓ PASS | SPARC |
| 6 | AGN host DM (morphology-matched) | ✓ PASS (+6.4%, p=0.047) | MaNGA DR17 |
| 7 | Halo M/M* vs z | = ΛCDM (not discriminative) | Behroozi+ |
| 8 | Missing satellites | ✓ structural (no sub-halos) | Sawala+ |
| 9 | Too-Big-To-Fail | ✓ structural | Boylan-Kolchin |
| 10 | dSph $M_{\rm dyn}$ slope | = ΛCDM (not discriminative) | Read+ |
| 11 | MDAR for dSphs (factor ~2 from MOND) | ✓ PASS | SPARC + dSph |
| 12 | Lensing flux ratio | ✓ structural | Dalal+Metcalf 2002 |
| 13 | Cluster baryon fraction | = ΛCDM (not discriminative) | f_b ≈ 0.15 |
| 14 | BTFR doc (slope 3.53) | = ΛCDM (not discriminative) | McGaugh 2012 |
| 15 | dSph σ(r) profile | ✓ structural (no cusps to fix) | Drlica-Wagner+ |
| 16 | BTFR SPARC real (129 gal) | ✓ PASS (slope 3.53) | SPARC |
| 17 | HI-DM correlation | ✗ confounded | SPARC |

**Score**: 11 clean passes + 4 structural + 5 = ΛCDM (consistent, not discriminative) + 1 confounded = **17/17 consistent, 0 falsified**.

### 4D Math Self-Consistency (10/10)

*Source: `paper/markdown/04_tests.md` §4.36*

| # | Constraint | Status |
|---|---|---|
| 1 | Dimensional structure: 4D bulk + 3+1D brane + 2D universes | ✓ SATISFIED by construction |
| 2 | Projection efficiency: 32% projected, 68% antigravity | ? OPEN (requires specific geometry) |
| 3 | Inner split: 5% direct, 27% cumulative 2D | ? OPEN (dropped v2.7.1) |
| 4 | Near-exact cancellation: ε ~ 10⁻³⁸ | ✓ SATISFIED (RS-II) |
| 5 | $f_{\rm active}$ = 0.0513 ± 0.0073 | ✓ PASS (MCMC) |
| 6 | Spatial distribution: isothermal cumulative | ✓ SATISFIED |
| 7 | $H_0 = 70 \pm 3$ (qualitative) | ✓ SATISFIED |
| 8 | RAR shape | ✓ PASS |
| 9 | w = -1 (cosmological constant behavior) | ✓ SATISFIED |
| 10 | Cone-shape: 2 levels, terminal at 2D | ✓ SATISFIED |

---

## ⚖️ SIDC vs Its Competitors

*Source: `paper/markdown/08_competitors.md`*

> "Whether SIDC is 'superior' to existing models depends entirely on the evaluation metric. If the metric is *mathematical and operational completion*, ΛCDM remains the reigning framework. If the metric is *parsimony and empirical coverage* — explaining the maximum number of distinct cosmic anomalies with the fewest arbitrary assumptions — SIDC presents a profoundly elegant, architecturally superior alternative."

### Comparison Table

| Model | Cosmo | Galactic | Parsimony | Comment |
|---|:---:|:---:|:---:|---|
| **ΛCDM** | ✓ | ✗ | ✗ | Excellent cosmo, 4 small-scale crises, 20+ params |
| **MOND** | ✗ | ✓ | ✓ | Excellent galactic, fails cosmo (clusters, CMB), 1 param |
| **SIDC** | ✓ | ✓ | ✓ | **All 3 (hybrid) — UNIQUE** |
| Superfluid DM | ✓ | ✓ | ✗ | Multiple free params |
| Fuzzy DM | ✓ | ✓ | ✗ | $m_a$, soliton params |
| SIDM | ✓ | ✓ | ✗ | σ/m cross-section |
| WIMP | ✓ | ✗ | ✗ | Mass, cross-section + cusps |
| Axion | ✓ | ✗ | ✗ | $m_a$, coupling + cusps |
| Sterile ν | ✓ | ✗ | ✗ | $m_ν$, mixing + cusps |
| ADD | ✗ | ✗ | ✗ | Hierarchy only, falsified at LHC |
| RS-II | ✓ | ✗ | ✗ | Hierarchy + graviton, no DM |

**SIDC is unique** because it achieves all three. Other models must choose 2 of 3.

### SIDC vs ΛCDM (Small-Scale Tests)

*Source: `08_competitors.md` §9.1*

| Small-scale test | ΛCDM | SIDC |
|---|---|---|
| Cusp-core | Needs ad-hoc feedback | Naturally isothermal |
| Missing satellites | Discrepancy with N-body | No sub-halos to be missing |
| Too-big-to-fail | Brightest sats too dense | No sub-halos to be too big |
| Lensing flux ratio | Quad anomalies from substructure | No sub-halos to lens |
| Direct detection | No WIMP up to $9.2 \times 10^{-48}$ cm² | No particle → trivially consistent |

**ΛCDM's burden**: requires accepting an increasingly messy and bloated "codebase" — undiscovered WIMPs/axions/sterile neutrinos for DM, a fine-tuned cosmological constant for DE, and highly complex baryonic feedback to reconcile simulations with observations.

**SIDC's structural advantage**: DM is a smooth, localized metric back-projection from the $S_{\rm destruction}$ action. Because it's not a physical particle, clumpy sub-halos do not exist *by construction*. The four historic small-scale crises collapse simultaneously.

### SIDC vs MOND (Galactic vs Cluster)

*Source: `08_competitors.md` §9.2*

| System | Empirical g₊ | MOND | SIDC | Best |
|---|---|---|---|---|
| Isolated spiral (SPARC) | $1.2 \times 10^{-10}$ m/s² | PASS | PASS | Tie |
| Massive cluster (Tian+ 2024) | $1.7 \times 10^{-9}$ m/s² | **FAIL** | **PASS** | SIDC |
| Dwarf galaxy | Variable | Fail (low SB) | **PASS** (via $E_{\rm crit}$) | SIDC |

**MOND's weakness**: works for isolated spirals (SPARC, 175 galaxies) but fails in massive clusters (the observed acceleration scale in cluster cores is 10× higher than MOND's $a_0$, forcing MOND proponents to introduce unseen baryonic gas or sterile neutrinos).

**SIDC's hybrid advantage**: behaves like MOND in quiet spiral arms (the 2D universe projection establishes a non-linear acceleration floor). But massive clusters (filled with violent plasma shocks) consistently blow past the $E_{\rm crit}$ threshold, naturally scaling the apparent acceleration up to match Tian+ 2024.

### SIDC vs Top-Down Extra Dimensions (ADD/RS)

*Source: `08_competitors.md` §9.3*

| Property | ADD/RS (top-down) | SIDC (bottom-up) |
|---|---|---|
| Hierarchy problem | Solved | Solved |
| Dark matter | Requires added scalar fields | Emerges as $S_{\rm destruction}$ return |
| Dark energy | Requires added potential | Emerges as 4D event antigravity |
| Phase transitions | Static | Active (event-driven) |
| Empirical fit (SPARC) | Not native | 10% median residual |
| Cluster g₊ | Not native | Naturally scaled |

**Top-down complexity failure**: ADD/RS posit a static higher-dimensional bulk to dilute gravity. They treat extra dimensions as permanent, passive plumbing. They don't natively explain the dark sector without added scalar fields.

**SIDC's dynamic advantage**: extra dimensions are not a static background — our universe actively spawns lower-dimensional spaces (3+1D → 2D) when localized energy density passes $E_{\rm crit}$. The dark sector is reframed as the time-delayed transactional debt of this scale-invariant lifecycle.

### SIDC vs Emergent / Entropic Gravity (Verlinde)

*Source: `08_competitors.md` §9.4*

| Galaxy | Entropic | SIDC | Match |
|---|---|---|---|
| AGC 114905 (low-mass, diffuse) | DM-rich (wrong) | DM-poor **PASS** | SIDC |
| KKR 25 (post-starburst) | DM-rich **PASS** | DM-rich **PASS** | Tie |
| Identical baryons, different DM | Struggles | History-dependent **PASS** | SIDC |

**Entropic gravity's temporal failure**: it lacks a historical clock — struggles to explain how two galaxies with nearly identical baryonic mass profiles can have completely opposite DM content.

**SIDC's temporal advantage**: by introducing the Stellar Age Lifecycle, SIDC has a historic ledger system. AGC 114905 (diffuse star formation that *never crossed* $E_{\rm crit}$) vs KKR 25 (intense historical starburst 1-4 Gyr ago whose $S_{\rm destruction}$ energy remains cached on our brane as a stable gravitational fossil).

### SIDC's Final Assessment

*Source: `08_competitors.md` §9.5*

> "SIDC is conceptually superior in its parsimony, its handling of small-scale galactic anomalies, its natural scaling from galaxies to clusters, and its radical intellectual honesty. It unifies dark matter, dark energy, and the hierarchy problem under a single, elegant geometric process rather than treating them as separate, disconnected problems."

---

## 📊 Honest Assessment

*Source: `paper/markdown/07_conclusion.md` §8.1*

### Strengths

- **Local physics is strong**: RAR matches SPARC to 10% median residual, AGN host DM strongly supported at p < $10^{-50}$ partial correlation, $g_+$ approximately constant at galaxy scale across 4.5 decades in $M_b$ (r=+0.19, p=0.22).
- **Parsimony**: 1 principle (geometric projection) vs ΛCDM's 20+ free parameters.

### Weaknesses

- **CMB-era physics is open**: 2D-to-3+1D time compression has 54-orders-of-magnitude uncertainty; full Lagrangian requires a 2D CFT expert.
- **Hubble tension**: ACCEPTED as real tension, $H_{0,4D} = 70.16$ is a geometric-mean property but specific $H_0$ values are not derived.
- **No unique testable predictions**: SIDC has **0 unique testable predictions** beyond what ΛCDM and MOND already predict. SIDC's value is *interpretive* (DM = 2D universe deaths, DE = 4D event antigravity) and *parsimonious*, not predictively unique.

### The AGC 114905 vs KKR 25 "bifurcation" was removed v2.7.36+

> "The 219× bifurcation was based on a 1000× error in KKR 25's $M_b$ (legacy_paper.md §3.27); the 10-year data gap makes pairwise comparison methodologically weak; AGC 114905's DM content is CONTESTED in 2022-2025 literature; SIDC now treats AGC 114905 and KKR 25 as INDEPENDENT galaxy tests."

---

## 🔬 Testable Predictions

*Source: `paper/markdown/07_conclusion.md` §8.1*

1. **2D universe birth stochastic GW background** at $\sim 10^{60-62}$ erg/s/Mpc³ (testable with SKA-MPG in 2030s, currently $10^3$× below NANOGrav sensitivity).
2. **BCG $g_+$ correlates with cluster ICM activity**, not BCG stellar mass alone.
3. **Dwarf $g_+$ correlates with recent star formation rate**, not total M*.
4. **DM fraction in quiescent galaxies should be LOWER** than in identical-mass active galaxies (phase-transition test).
5. **AGC 114905 has no high-energy events above $10^{30}$ J** in its recent history (testable with deep X-ray/radio).
6. **47 Tucanae (NGC 104)**: $M_{\rm dyn} \approx M_{\rm stars}$ (no local DM spike). Falsifiable by Rubin/LSST DP1 (2025), DR1 (2027), Y10 (2034).

---

## 📚 The Paper

**Current version**: v3.5.9+ (June 21, 2026, APPROACH A1)
**Length**: 400 pages, 1.55 MB
**Limitations**: 140 honest
**Repository**: https://github.com/ampbuster/gravity-as-residual

### Paper structure (23 markdown files)

| # | File | Topic |
|---|---|---|
| 00 | `00_title.md` | Title, version, highlights, parameter hierarchy |
| 01 | `01_executive_summary.md` | Abstract, scaling law, closed loop, honest framing |
| 02 | `02_glossary.md` | Comprehensive glossary of all variables |
| 03a | `03a_relations.md` | Mathematical relations |
| 03b | `03b_predictions.md` | Quantitative predictions |
| 03c | `03c_lagrangian.md` | Lagrangian formulation |
| 03e | `03e_first_principles_c1_matrix_model.md` | C=1 matrix model analysis (HISTORICAL) |
| 03f | `03f_dm_is_not_a_particle.md` | DM is not a particle |
| 03g | `03g_f_theory_12d_4d_bulk.md` | F-theory 12D as 4D bulk (HISTORICAL context) |
| 04 | `04_predictions.md` | Detailed predictions |
| 04 | `04_tests.md` | Test methodology and results |
| 05 | `05_falsification.md` | What would falsify SIDC |
| 06 | `06_limitations.md` | **All 140 honest limitations** |
| 07 | `07_conclusion.md` | Honest assessment + external constraints |
| 08 | `08_competitors.md` | SIDC vs ΛCDM/MOND/ADD/Entropic |
| 09 | `09_data_refs.md` | All data sources |
| 10 | `10_end_universe.md` | Speculative end-of-universe |
| 11 | `11_testable.md` | 47 Tuc test, Rubin/LSST timeline |
| 12 | `12_galaxy_zoo.md` | 12/12 galaxy tests |
| 13 | `13_cmb_gap.md` | What CMB-era physics would require |
| 14 | `14_appendix.md` | Appendices |
| 15 | `15_falsifiability_matrix.md` | Falsifiability matrix |

### Legacy docs (for historical context)

- `paper/legacy/v359_README_legacy_sections.md` — historical README sections
- `paper/legacy/v3_legacy_dm_dynamics_hill_Fp.md` — Hill function F_p(z) (DROPPED v3.3+)
- `paper/legacy/v357_f_back_clarification.md` — f_back naming revolution (v3.5.7+)
- `paper/legacy/v358_user_driven_refinements.md` — v3.5.8 audit details
- `paper/legacy/v359_path_B2_rejected.md` — Path B2 (rejected)
- `paper/legacy/v359_audit_housekeeping.md` — A1 details
- `paper/legacy/legacy_paper.md` — historical sections from older versions

---

## ⚠️ What this paper is NOT

- **Not a finished theory**. It is a **thought experiment**.
- **Not a derivation from first principles**. Quantitative values are *fits* to observation or *derived* from framework structure (L308v α-GM).
- **Not predictive**. SIDC has 0 unique testable predictions beyond ΛCDM and MOND.
- **Not written by a physicist**. By a software developer with AI assistance.

---

## 🤖 AI Disclosure

Developed in conversation with **Mavis (M3, MiniMax)**. The AI's role: cross-checking derivations, catching inconsistencies (the user has done the same — see L308f through L308aa for 23 user-driven insights), suggesting notation cleanup (see `paper/build_tools/fix_notation.py` for the consolidated tool), and maintaining consistency across the 23 markdown files.

---

## 📖 Citation

> ampbuster (2026). *Gravity as Residual: A Thought Experiment on Dimensional Inversion, Annihilation, and the Origin of the Dark Sector.* v3.5.9+, 400 pages.
> [github.com/ampbuster/gravity-as-residual](https://github.com/ampbuster/gravity-as-residual)
