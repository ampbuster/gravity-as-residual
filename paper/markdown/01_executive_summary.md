<!-- 01_executive_summary.md - part of paper.md split (v3.0.13) -->

## Abstract

**EXECUTIVE SUMMARY (for hurried readers).** This paper proposes a geometric framework (the **Dimensional Cascade**, DC) in which gravity, dark matter, and dark energy are all consequences of a dimensional projection mechanism. We are a software developer, not a physicist; this is a thought experiment, not a finished theory. The cascade is a **cone-shaped 3-level structure** (4D parent → 3+1D us → 2D children, terminal at 2D), NOT a scale-invariant infinite cascade (1D and 0D universes are nonsensical, so the cascade terminates at 2D). The cascade IS scale-invariant in the *energy/size* sense within the 2D level (the Liouville 2D CFT is conformally invariant, and any energetic event creates a 2D universe of proportional size, weighted by a smooth E^(1+alpha) creation function — see §2.5.3; the v2.3.0 E_crit phase-transition threshold has been replaced by this single smooth function). The cascade postulates that all dark matter is 2D universe mass, time-compressed to 3+1D via the 5D AdS_5 bulk geometry. Honest status: **16/17 test categories** (16 pass, 1 confounded) and **7/7 specific cases** pass real-data tests, with **2 components falsified** (g_obs = g_bar + g_cum + g_active functional form, FALSIFIED in v2.2; Mechanism A Hubble, FALSIFIED in commit ~80) and **0 strongly confirmed**. The 2 falsifications were *specific functional forms* that the cascade has since replaced (cascade-MOND hybrid for RAR; Mechanism M for Hubble tension), not the cascade's framework. The cascade's STRENGTH is local physics (RAR matches SPARC to 10% median residual, AGN host DM strongly supported at p<10⁻⁵⁰ partial correlation, g_+ approximately constant at galaxy scale across 4.5 decades in M_b but the correlation is not statistically significant, r=+0.19, p=0.22). The cascade's WEAKNESS is CMB-era physics (Hubble tension ACCEPTED as real tension, H_0,4D = 70.16 is a geometric-mean property but specific H_0 values are not derived, 2D-to-3+1D time compression has 54-orders-of-magnitude uncertainty, full Lagrangian requires 2D expert). The cascade documents **37 honest limitations** (§7.0 Master Table, v2.7.23+): 17 OPEN, 10 PARTIAL, 3 CLOSED, 2 FALSIFIED, 4 REVERTED, 1 DISCARDED (§3.13 mechanism). 36 entries are in the master table; the 1 DISCARDED entry (L9_ext) was added in v2.7.20 when §3.13 was discarded. L9 (2D universe physics) explicitly remains open — the form of DM at 2D universe death is UNSPECIFIED. The cascade commits to a **geometric DM framework** (Option D in §3.14) by default; specific particle interpretations (WIMP, axion, sterile neutrino) are possible but stability requires discrete symmetries, not Pauli blocking. Bottom line: **consistent with current data, falsifiable, ready for theoretical physicist to complete, with self-critical methodology (§3.16)**.

**5/27/68 honest framing (v2.7.1).** The 5/27/68 split is **observational data** (Planck 2018), not a cascade prediction. The cascade's qualitative interpretation is: 5% = baryons (real 3+1D), 27% = DM from 2D universe back-projection, 68% = DE from 4D event antigravity. **The 5/27 inner split (5% "active" 2D universes vs 27% "cumulative deaths") is dropped in v2.7.1 as a separate postulate** that conflicted with the empirical 33 s lifetime (which gives f_active ~ 10^-17, not 0.05). The 5:27 inner split was a post-hoc fit, and the "three 5%" coincidence was a confusion. f_active is now a free parameter, not derived.

**Hubble tension position (v2.7, Mechanism M).** The cascade adopts Mechanism M: the Hubble tension is **ACCEPTED as a real observational tension**, not resolved. The cascade is qualitatively consistent with H_0 = 70 ± 3 across all measurements (SH0ES 73, TRGB 69.8 ± 1.9 [Freedman 2024, JWST], Planck 67.4, standard sirens 70 ± 12). The cascade's intrinsic H_0,4D = sqrt(H_CMB × H_local) = 70.16 is a non-trivial property of the data. The 5.6 km/s/Mpc gap between local and Planck-inferred H_0 is a ΛCDM-framework artifact, not a cascade problem. Earlier 4-zone H(z) attempts were removed in v2.7 (they were data fitting with 8 free parameters for ~5 data points, and the P(y) problem made them internally inconsistent).

---

We propose a unifying interpretation of three open problems in fundamental physics — the weakness of gravity (the hierarchy problem), the nature of dark matter, and the nature of dark energy — under a single geometric process. In this picture, our 3+1 dimensional universe is the *projection* of a single *ongoing* event in a higher-dimensional space: an energetic release of gravitational energy in the bulk, with the energy of that event manifesting in our brane as the Big Bang, and the dimensional projection mechanism producing the dark sector as a byproduct. The model is **a thought experiment, not a finished theory** — it provides a *geometric framing* that unifies three problems and yields specific testable predictions, but does not yet derive quantitative values from first principles. We are explicit about what is derived, what is fit, and what is postulated.

**What the model does well (data backing).** The cascade has been tested against multiple independent observations. **16/17 test categories** (RAR, cluster g_+, dwarf phase-transition, globular cluster DM, direct detection, isolated vs cluster dwarf, AGN host DM, halo M/M* vs z, missing satellites, too-big-to-fail, dSph M_dyn, MDAR, lensing flux ratio, cluster baryon fraction, BTFR, dSph σ(r) profile, BTFR SPARC, HI-DM correlation, Vflat-morphology; ~430 data points) are consistent with the cascade; **1/17 is confounded** (HI-DM correlation confounded by gas-radius correlation; the Vflat-morphology test, previously inconclusive, is now documented as inconclusive due to sample selection bias). Of the 16 passing tests, **6 are clean real-data passes (was 5; AGN host DM added in v2.3.1 with morphology matching, +6.4%, p=0.047), 4 are structural (cascade avoids ΛCDM problems by having no sub-halos), 5 are not discriminative vs ΛCDM, and 1 is qualitatively consistent (AGN host DM).** **7/7 specific cases** (SPARC, Tian+ 2024, Sun, DF2/DF4, FCC 224, AGC 114905, KKR 25) are also consistent.

- **Radial Acceleration Relation (SPARC, 175 galaxies):** the cascade-MOND hybrid matches the RAR to a 10% median residual, comparable to MOND itself. MCMC posterior: $f_{active} = 0.0513^{+0.0070}_{-0.0073}$ (1σ), the fraction of cumulative 2D universe back-projection that is "active" at any moment. **CAVEAT (v2.7.1):** f_active ~ 0.05 is a phenomenological RAR fit, NOT derived from cascade first principles. The cascade's "derivation" f_active = τ_2D/T_universe = 0.7/13.8 = 0.051 used τ_2D ~ 0.7 Gyr (gas consumption timescale) as a SEPARATE POSTULATE, identified by physical analogy. The empirical 33 s lifetime gives f_active ~ 10^-17, not 0.05. f_active is a FREE PARAMETER. See §4.35.
- **Cluster scale (Tian+ 2024, 50 BCGs):** the cluster g₊ enhancement to $\sim 1.3 \times 10^{-9}$ m/s² is naturally explained as the MOND external field effect ($V_{local}$ formula), matching Tian+ 2024's $1.7 \times 10^{-9}$ to within 30% (the cascade's MCMC 1σ range is 5.3e-10 to 2.7e-9, which does include 1.7e-9).
- **Phase-transition principle (5 dwarf-galaxy tests, REVISED v2.7.36+):** the critical-energy threshold $E_{crit} \sim 10^{30}$ J correctly predicts: Sun (no detectable DM, as expected), DF2/DF4 (DM-poor, no recent energetic events), FCC 224 (DM-poor), AGC 114905 (DM-poor, low-mass SF below threshold), and KKR 25 (consistent via the S_destruction cumulative-return pathway: intermediate-age SF at 1-4 Gyr produced 2D universes whose energy has been returned to 3+1D as DM per the action's S_destruction). 5/5 specific dwarf cases consistent (each tested independently, no bifurcation framing). The S_destruction energy-return mechanism is a model assumption, not a derivation; if the 2D universe's death energy instead escapes the 3+1D brane, KKR 25 would revert to a TENSION.
- **Hubble constant:** the cascade is **qualitatively consistent** with $H_0 = 70 \pm 3$ across all measurements (SH0ES $73.04 \pm 1.04$, TRGB $69.8 \pm 1.9$ [Freedman 2024, JWST], Planck CMB $67.4$, standard sirens $70 \pm 12$). The cascade does **not** derive a specific $H_0$ value — earlier multiplicative boost formula ($H_0 = 70.13$) was a postdiction, removed in v2.5. The 5.6 km/s/Mpc gap to Planck CMB-inferred $H_0 = 67.4$ is a **ΛCDM-framework artifact**, not a cascade prediction. See §2.6.1 (Honest H_0 framework) and Limitation 26.
- **Cosmic energy budget:** the cascade is consistent with the observed 5% ordinary / 27% dark matter / 68% dark energy split (Planck 2018). These values are **observational data**, not cascade predictions. The cascade provides a qualitative INTERPRETATION: 5% = baryons (real 3+1D energy), 27% = DM (cumulative 2D universe back-projection), 68% = DE (4D event antigravity). The 32%/68% outer split is "interpretable" from projection kinematics. **The 5:27 inner split (5% "active" vs 27% "cumulative") is dropped in v2.7.1 as a separate postulate that conflicts with the empirical 33 s lifetime** (which gives f_active ~ 10^-17, not 0.05).
- **Concrete action functional (§2.5.1):** the geometric picture is now backed by a Lagrangian-level skeleton: $S = S_{grav} + S_{matter} + S_{brane 2D} + S_{creation} + S_{destruction}$, with $\alpha$ coupling, $\delta$-function 2D brane localization, and Stoke's-theorem energy conservation. Reduces to standard RS-II brane-world as $\alpha \to 0$.
- **First-principles g₊ derivation (§4.17):** g₊ = $k \cdot \int (event rate) \cdot E_{event} \cdot \tau_{2D} / L_{2D}\ dt$, the cascade's formula for the universal acceleration scale, equivalent to empirical $g_+ \propto \int \rho_{events} / M_{b}\ dt$ scaling.

**What the model is honest about (limitations).** The cascade is a *geometric framing*, not a derived Lagrangian. Quantitative values are *fits* to observation (5/27/68, $f_{active} \sim 0.05$, $g_+ \sim 1.2 \times 10^{-10}$, $\epsilon \sim 10^{-38}$, $f_{back} \sim 10^{-85}$), not first-principles predictions. The 5/27/68 formula's "self+neighbor edges in a graph" interpretation fails to survive the cone-shape refinement — it was a post-hoc fit to a pre-v2.1 4-level model that no longer exists. The cascade's *specific* 5/27/68 derivation is left to future work (Limitation 26, §7.1 *Appeals to Formalism*). The model documents **37 honest limitations** across all major claims (see §7.0 Master Table, v2.7.30+): 17 OPEN (including 1 architectural), 10 PARTIAL, 3 CLOSED, 2 FALSIFIED, 4 REVERTED (including 1 PARTIAL→REVERTED), 1 DISCARDED (§3.13 mechanism in v2.7.20). L14 was resolved by the v2.1 mathematical sketch; L32 was removed in v2.7; L34 added v2.7.4 for E_primordial; L35 added v2.7.4 for z_half; L36 added v2.7.4 for E_crit REVERTED; **L37 added v2.7.30 for α=1.29 CGHS derivation** (§3.24 self-critique: in RANGE but NOT derived); **L9_ext DISCARDED v2.7.20 for Pauli-blocked sterile ν** (Batell-Yin 2024 bound).

**Architectural choice: cone-shape is the default, NOT scale-invariance.** The cascade is **cone-shaped, not scale-invariant** in the dimensional sense. The 4D parent → 3+1D us → 2D children structure is the architecture; 2D is the hard floor (1D and 0D universes are nonsensical, so the cascade terminates at 2D). The earlier framing of "scale-invariance / infinite cascade" with a $\rho_{crit}$ regulator has been removed — the 2D floor is a structural limit, not a choice. The cascade IS still scale-invariant in the *energy/size* sense within the 2D level: the Liouville 2D CFT is conformally invariant, and any energetic event creates a 2D universe of proportional size (weighted by the smooth E^(1+alpha) creation function in §2.5.3 — the v2.3.0 E_crit step threshold has been removed). This is a different kind of scale invariance — not dimensional, but energy-scale — and it does not require a cascade to lower dimensions.

**Democratic cosmology (v2.7.24-v2.7.25+, §3.17-§3.18).** A user-supplied insight (June 2026) revealed a deep pattern: all 2D universes have the same proper lifetime in 2D frame (= t_Pl,3), and all 3+1D universes have the same proper lifetime in 3+1D frame (= t_Pl,4). The energy-scaling rule $\tau_{2D_{3+1D}} = (E/E_{Pl,3})^{1.29} \times t_{Pl,3}$ is now a **DERIVATION from time dilation**, not a separate empirical fit. The same α = 1.29 applies at every level. This is a "democratic" cosmology: every universe at the same level is equal in its own frame, but the parent dimension sees vastly different lifetimes (10⁻⁶³ s to 10⁸ yr for 2D; 10⁻¹⁹ s to 10⁴⁰ yr for 3+1D). **α is no longer a free parameter** — it is a property of the projection geometry, derivable in principle from CGHS-with-back-reaction (§3.19, §3.22). The cascade's net free parameter count: 1 (z_half only).

**Self-critical methodology (v2.7.22+, §3.16).** The cascade's iterative process is formalized: build → user pushback → self-critique → discard or revise → document. The §3.13 → §3.14 → §3.15 sequence (sterile neutrino DM with Pauli-blocked decay) is a worked example: built in v2.7.18, self-critiqued in v2.7.19, discarded in v2.7.20 after literature search (Batell-Yin 2024 m<10meV bound, sub-eV DM is HDM not CDM, 3.5 keV X-ray line weakened). The cascade documents the discard explicitly rather than papering over broken hypotheses.

**11 framework connections (v2.7.6-v2.7.29, §3.8, §3.22).** The cascade's framework is supported by 11 established frameworks: 1 STRONGEST MATCH (CGHS, α=1.29 in [1,3] back-reaction range), 6 STRUCTURAL (Padmanabhan, Horava-Witten, KK, Geodetic brane, DGP, Verlinde), 2 TENSION (Jacobson, RT — predict linear scaling, not power law), 2 SPECULATIVE (Massive gravity, Conformal gravity). No framework uniquely derives α = 1.29 from first principles; a specific CGHS-with-back-reaction calculation would close L9.

**Testable predictions (§3):** (1) BCG g₊ correlates with cluster ICM activity, not BCG stellar mass alone. (2) Dwarf g₊ correlates with recent star formation rate, not total $M_*$. (3) Dark matter fraction in quiescent galaxies should be *lower* than in identical-mass active galaxies (phase-transition test). (4) The cascade predicts AGC 114905 has *no* high-energy events above $10^{30}$ J in its recent history — testable with deep X-ray/radio observations.

**Why the Dimensional Cascade vs its competitors — quick comparison.** Whether the cascade is "superior" depends on the metric. On *mathematical and operational completion*, standard $\Lambda$CDM remains the reigning framework. On *parsimony and empirical coverage* — explaining the maximum number of distinct cosmic anomalies with the fewest arbitrary assumptions — the cascade presents an architecturally superior alternative. The table below summarizes the tradeoffs:

| Competitor | Main weakness | Dimensional Cascade advantage |
|------------|---------------|-----------------|
| **ΛCDM** | 4 unresolved small-scale crises (cusp-core, missing sats, TBTF, MFRP); requires WIMP + $\Lambda$ + 20+ feedback params | DM is geometric → no sub-halos → all 4 crises collapse by construction |
| **MOND** | Fails in cluster cores (g₊ ~17× too low) | Phase-transition scales g₊ naturally to cluster regime |
| **ADD/RS brane-worlds** | Static bulk; no native dark-sector explanation | Dynamic cascade: dims are spawned, dark sector falls out as transactional debt |
| **Verlinde (entropic)** | No historical clock → can't explain different-DM identical-baryon galaxies | Stellar Age Lifecycle ledger explains AGC 114905 vs KKR 25 timing |

The full architectural comparison is given in §9 (Cascade vs its Competitors: A Detailed Comparison).

# Main Points (TL;DR)

If you read nothing else, read this section.

## What is the cascade?

The **Dimensional Cascade** (now formally named **SIDC — Scale-Invariant Dimensional Cascade**, v3.0.2) is a thought-experiment framework that proposes:

- **Dark energy** = a "back-projection" of the 4D event that created our 3+1D universe
- **Dark matter** = the cumulative gravity of countless 2D universes created by every energetic event in our universe
- **Gravity's weakness** = the residual of a near-cancellation between 4D and 2D gravitational effects

## What does v3.0 actually derive?

v3.0 made a **major breakthrough**: a single number — **N = 12** — derives multiple cascade parameters from a specific physical model (q = 4 SYK — Sachdev-Ye-Kitaev, a model of quantum chaos — with N = 12 Majorana fermions):

| Parameter | Value | Derivation |
|-----------|-------|------------|
| α (lifetime scaling) | 1.289 | α = 1 + 1/√N (saddle-point fluctuation) |
| c (central charge) | 1/2 | c = N/24 (Ising CFT) |
| 1/(2α) (back-action) | 0.388 | c/α (composite) |
| f_back (universal) | 8.6×10⁻⁸⁵ | (1/(2α))-powered formula |

N = 12 is **uniquely determined** by α = 1.29 (off by 0.001; for N = 10, 11, 13, 14 the match is much worse).

## What does the cascade predict (and what doesn't)?

**Strong predictions** (testable, falsifiable):

1. **47 Tucanae**: M_dyn ≈ M_stars (no local DM) — differentiator from particle DM
2. **Intermediate F(z) dwarfs**: 10-30% of dwarfs are DM-poor (consistent with Bidaran+ 2025 etc.)
3. **Massive quiescent galaxies at z > 4**: very high M_dyn (consistent with RUBIES, EXCELS etc.)
4. **Tidal dwarf galaxies**: shifting toward DM-poor (consistent with Zaragoza-Cardiel+ 2024 etc.)
5. **14 event-type lifetimes**: all follow τ_2D ~ M^1.29 (SN, GRB, BNS, AGN, etc.)

**Indistinguishable from ΛCDM or below detection** (currently):

- DESI w(z): w = -1, same as ΛCDM
- 2D universe death GW: 80-100 orders below LISA/PTA detection
- PPN γ: 1 to 10⁻⁷³, same as GR

**Doesn't derive (honest)**:

- Specific CKM/PMNS values
- SM mass hierarchy
- Why N = 12 specifically (vs N = 11 or 13)
- Specific dS_2 topology details

## What is the cascade's "secret symmetry"?

The cascade is **structurally scale-invariant** (works at any dimensional level — a "Russian nesting doll"):

- 5D event → 4D universe → ... → DM
- **4D event → 3+1D universe (us) → ... → DM**
- 3D event → 2D universe → ... → DM

The pattern is the same at every level. The specific values (α, c, N, f_back) are **dimension-dependent** but the structure is universal. This is the cascade's "dimensional self-similarity" — the SIDC in the name.

## The cascade's honest stance

- **37 honest limitations** documented in §7.0
- 5 closed, 62 open, 11 partial, 2 falsified, 4 reverted, 1 discarded
- **0 free parameters** at the level of the composite model (N = 12, α = 1.289, c = 1/2, f_back = 8.6e-86 are all derived)
- 1 free parameter at the data-fitting level (z_half = 3)

The cascade is a **geometric framing with a strongly specified backbone**, not a fully derived Lagrangian. It's a thought experiment, not a complete theory.

---



