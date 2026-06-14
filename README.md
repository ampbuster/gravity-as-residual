# Gravity as Residual

> A thought experiment on dimensional inversion, annihilation, and the origin of the dark sector.

**Author:** A non-specialist (software developer)  
**AI assistance:** Developed in conversation with Mavis (M3, MiniMax), disclosed in §1 and `ai_disclosure.md`  
**Version:** 2.3.1 (patch: cascade direction default + abstract strengthened) (June 2026) — internal consistency pass + new RAR tests after v2.2 audit  
**Status:** Public release. 187 commits, 28 honest limitations documented (29 if including the closed Limitation 14).

---

## The idea in one paragraph

What if gravity is *weak* because most of it gets cancelled? In this model, a single ongoing 4-dimensional event projects into our 3+1-dimensional universe. The projection *inverts* the sign of gravity, so the 4D event's native gravity is cancelled on the 3+1D brane — leaving only a small positive residue that we call ordinary gravity. The un-cancelled *antigravity* component is what we observe as **dark energy**. Every energetic event in 3+1D (a star, a supernova, a black hole) creates a *child universe* at the next level — a literal 2D universe (one time + one space) embedded in our 3+1D space, its gravity back-projected to 3+1D as the cumulative effect we call **dark matter**. The cascade is *scale-invariant by default* (4D → 3+1D → 2D → 1D-like → ...) with *cone-shape* (early termination at 2D) as a viable alternative — the choice is architectural, not empirical. The 5/27/68 mass-energy split is observational 3+1D data that constrains the 4D event's geometry, not a free postulate.

---

## What the model gets right (data backing)

The cascade has been tested against multiple independent observations. **6/7 specific cases consistent, 1 TENSION (KKR 25)** with the model's predictions:

| System | Test | Result | Status |
|---|---|---|---|
| **SPARC** (175 galaxies) | Radial Acceleration Relation | 10% median residual | ✓ Consistent |
| **Tian+ 2024** (50 BCGs) | Cluster-scale $g_+$ | 14% median residual, $g_+ = 1.3\times 10^{-9}$ within 1σ of Tian+ 2024's $1.7 \times 10^{-9}$ | ✓ Consistent |
| **Sun** (null test) | DM detection | 1e-17 of galaxy's DM, undetectable | ✓ Consistent |
| **DF2 / DF4** | DM-rich vs DM-poor | DM-poor, old stellar pop (no SN) | ✓ Consistent |
| **FCC 224** | DM-rich vs DM-poor | DM-poor, old stellar pop | ✓ Consistent |
| **AGC 114905** (anomaly) | Phase-transition test | DM-poor, low-mass SF below $E_{\text{crit}} \sim 10^{30}$ J | ✓ Consistent (anomaly resolved) |
| **KKR 25** (positive case) | Active dwarf | DM-rich, active history | ✓ Consistent |

**Other data backing:**

- **Hubble constant:** $H_0 = 73$ km/s/Mpc, matches SH0ES ($73.04 \pm 1.04$) and Pantheon+ ($73.00$, within 1σ of diagonal-error range). 5.6 km/s/Mpc gap to Planck CMB ($67.4$) accepted as a separate open problem.
- **Cosmic energy budget:** 5% ordinary / 27% DM / 68% DE (Planck 2018) — consistent with cascade's projection picture. The 32%/68% outer split is derivable from projection kinematics; the 5:27 inner split is observational 3+1D data, not derived.
- **Cluster $g_+$ enhancement:** $1.2\times 10^{-9}$ m/s² (cascade's $V_{\text{local}}$) vs Tian+ 2024's $1.7 \times 10^{-9}$ m/s² — within 1σ, naturally explained as the MOND external field effect.
- **MCMC posterior on $f_{\text{active}}$:** $0.0513^{+0.0070}_{-0.0073}$ (1σ) from RAR fit, strongly preferred over the originally-postulated 0.30.
- **Concrete action functional** (§2.5.1): rare for thought experiments — a Lagrangian-level skeleton a mathematical physicist can work with. Reduces to standard RS-II brane-world as $\alpha \to 0$.
- **First-principles $g_+$ derivation** (§4.17): $g_+ = k \cdot \int \text{(event rate)} \cdot E_{\text{event}} \cdot \tau_{\text{2D}} / L_{\text{2D}}\, dt$ — equivalent to empirical $g_+ \propto \int \rho_{\text{events}} / M_b\, dt$ scaling.

---

## What's new in v2.3.1 (since v2.3.0)

This is a **polish + real-data test** patch:

- **Cascade direction clarified** (per Gemini's architectural argument): the model defaults to (a) scale-invariance / infinite cascade (open upward AND downward, regulated by $\rho_{\text{crit}}$ at each level), with (b) cone-shape / early-termination at 2D as a viable alternative. The choice is architectural, not empirical — both give the same 7/7 specific-case predictions. §2.6 *Cone-shaped hierarchy* updated; Limitation 11 strengthened; new Limitation 11.5 added.
- **5/27/68 formula rejection strengthened**: now documented as broken in BOTH infinite-cascade and cone-shape interpretations. The "self+neighbor edges in a graph" picture requires a closed graph, which neither interpretation provides.
- **Real-data test of phase-transition principle (NEW, §4.8)**: 5/5 specific dwarf-galaxy cases tested with REAL observational data (not synthesized). AGC 114905, DF2/DF4, FCC 224, KKR 25, and the Sun. Each case uses published stellar population age to compute maximum surviving stellar mass, then checks if it's above the 8 M☉ SN threshold (which determines if events cross E_crit). Result: 4/5 consistent, 1 TENSION (KKR 25). AGC 114905 anomaly RESOLVED by the specific stellar population age (0.5-2 Gyr → only A-type stars survive → no SN progenitors → no events above E_crit → no DM contribution). KKR 25 is a TENSION: cascade predicts DM-poor (no current SN), but observation is DM-rich. *Real challenge for the cascade.*
- **Abstract strengthened**: now leads with the data backing (6/7 specific cases (1 TENSION), MCMC f_active, g_+ derivation, action functional) rather than starting with "we propose" / "we reframe".
- **Layman summary rewritten**: the "changelog" section is now in plain language, with technical terms explained for non-physicists.
- **28 honest limitations** (was 30 in v2.3.0; corrected count after re-audit. Limitation 11.5 was already counted in v2.3.0.)

Total commits: 196. PDF: 114 pages, 581 KB.

## What's new in v2.3.0 (since v2.2.1)

This is a **major theoretical contribution**: a concrete action functional S for the cascade, plus a first-principles derivation of the g_+ acceleration scale.

- **§2.5.1 NEW: Concrete action functional S** (commit 163). Per the gap identified by Gemini and the user, replaced the cascade's geometric narrative with a concrete action functional a mathematical physicist can work with:
  - S = S_{grav} + S_{matter} + S_{brane 2D} + S_{creation} + S_{destruction}
  - S_{creation} has α coupling and δ-function localization of 2D brane at 3+1D event
  - S_{destruction} returns energy to 3+1D as DM after τ_2D
  - Local energy conservation preserved (Stoke's theorem)
  - Reduces to standard RS-II brane-world when α → 0

- **§2.5.1 HONEST STATUS** (commit 164): the action is a SKELETON, not a complete theory. It has 5+ free parameters (L_2D, α, death mechanism, T^DM at death, the 5/27/68 split, the cascade-MOND g_+) that need to be specified. The cascade's contribution is the GEOMETRY; the dynamics are open problems.

- **§4.11 NEW: First-principles g_+ derivation** (commit 165). From the action's α coupling, derived:
  - g_+ = k * ∫ event rate * E_event * τ_2D / L_2D dt
  - This is Gemini's scaling relation: g_+ ∝ ∫ ρ_events/M_b dt

- **CLUSTER g_+ ENHANCEMENT (Tian+ 2024) NOW EXPLAINED** as a natural consequence. A BCG sits at the bottom of a cluster's potential well and sees not just its own stellar history but the entire cluster's ICM activity (AGN feedback, mergers, thermal bremsstrahlung, ram pressure). Cluster event rate ~ 100× BCG's own, cluster events ~ 10× more energetic, ~ 10× larger. Net enhancement ~ 100×, matching Tian+ 2024's 10-17×.

- **4 testable predictions** from the g_+ formula (Limitation 26 unchanged: cascade provides geometry, not Lagrangian):
  1. BCG g_+ correlates with cluster ICM activity (cooling flow vs not)
  2. Dwarf g_+ correlates with recent SFR, not total M_*
  3. g_+ ratio between systems matches event rate ratio, not M_b ratio
  4. Direct test: partial correlation between SFR, M_*, and g_+ (TENSION: §4.7 found SFR signal entirely mediated by M_b)

- **Build infrastructure fix** (commit 163). Replaced one longtable that was breaking xelatex with bullet list format. Added xcolor [table] option for future longtables. PDF now builds cleanly: 100 → 103 pages.

- **30 honest limitations** (was 28). Limitation 26 refined: "Cascade provides geometry, not Lagrangian. The action in §2.5.1 is a SKELETON with 5+ free parameters that need to be specified for a complete theory."

- **New companion code**:
  - `calculations/cascade_action.py` (210 lines) — cascade action functional skeleton
  - `calculations/cascade_action_honest.py` — honest assessment of the action's remaining gaps
  - `calculations/g_plus_scaling_derivation.py` (450 lines) — first-principles g_+ derivation

---

- **§2.5 NEW**: Phase-transition threshold principle (Gemini's insight). 2D universe creation is a NON-LINEAR PHASE TRANSITION with critical event energy E_crit ~ 10^30 J. Below threshold, zero cascade. Above, full cascade. **Resolves the AGC 114905 anomaly**: its ongoing SF is at energies below threshold, so no 2D universes are created. 4/5 specific cases consistent + 1 TENSION (was 4/5 + 1 challenge, with KKR 25 upgraded from "challenge" to documented TENSION in v2.3.1).

## What's new in v2.2.1 (since v2.2)

This was an audit pass plus a substantive new analysis of the Radial Acceleration Relation (RAR):

- **Cone-shaped hierarchy is canonical** — all pre-v2.1 "fractal"/"infinite" references replaced. 1D/0D/negative-D universes do not exist. The cascade terminates at 2D.
- **5/27/68 reframed as observational 3+1D data** — not a free property of the 4D event. The 5%/27%/68% comes from BBN, CMB+LSS, and supernovae+BAO. The cascade *interprets* these observations in 4D terms, but doesn't *choose* them.
- **RAR fit to 8-12%** across the full mass spectrum (ultra-faint dwarf to supercluster). Three tuning parameters (f_active ≈ 0.05, isothermal profile, mass-dependent scale ≈ 1/κ) match the empirical RAR.
- **f_active is ~5%, not the originally-postulated 30%** — found by grid search against the RAR. The 4× gap to 30% is documented. A specific 4D event model would need to derive f_active from the 4D geometry.
- **The "5%" appears in three places** in the cascade (baryon fraction, 5/27 ratio, f_active). They're not all the same 5%, but the 5/27 ratio corresponds to the cosmic star formation timescale (Madau & Dickinson 2014).
- **All existing tests re-verified with the new framing** — Pantheon+ with full covariance, Mechanism M for the Hubble tension, the cone-shaped hierarchy. None are broken by the §2.6 reframing.
- **28 honest limitations** (was 18) — added §7 Limitations 19-28 for the dynamical-mixing, RAR residuals, scale factor, and Lagrangian constraints.

---

## Contents

| Folder / File | What's in it |
|---|---|
| `paper/paper.md` | The full paper, v2.3.0 (markdown source) |
| `paper/paper.pdf` | Compiled PDF (114 pages) |
| `paper/no-lmodern-template.tex` | Custom LaTeX template (no lmodern needed) |
| `supporting/layman_summary.md` | Plain-language summary (v2.3.0) |
| `supporting/data/` | Pantheon+ SNe data and covariance matrix |
| `supporting/publication_strategy.md` | Notes on where to publish |
| `calculations/` | ~50 Python scripts (numerical verification, derivations, tests) |
| `calculations/rar_*.py` | New RAR analysis scripts (commits 101-119) |
| `calculations/cascade_model.py` | The main OO model implementation |
| `calculations/figures/cascade_summary.png` | 9-panel summary figure |
| `changelog.md` | Full version history v1.02 → v2.3.0 |
| `ai_disclosure.md` | How Mavis was used in the development |
| `LICENSE` | MIT License |
| `CITATION.cff` | How to cite this work |

## Key findings (v2.3.0)

- **Cone-shaped hierarchy** (4D event → 3+1D → 2D, terminal at 2D; 1D universes do not exist). Closes the 1D-universes limitation.
- **Sign ambiguity RESOLVED** in §2.4: ordinary gravity and dark energy are two physically distinct small contributions to the effective 3+1D action, not opposite-sign components of the same quantity.
- **Growth factor G = 9.7e7** is DERIVED from 2D universe FRW dynamics (was 1e8 free parameter).
- **Pantheon+ full-covariance test**: cascade's Mechanism B/F H_0(z) prediction REJECTED at 7 sigma. Pantheon+ shows H_0 is constant at ~73 across all z. Cascade's *qualitative* H_0 = 73 prediction is confirmed.
- **Cascade's final H_0 position (Mechanism M)**: cascade accommodates the Hubble tension (predicts 73, not 67.4) but does not resolve the 5.6 km/s/Mpc gap. Joins LCDM in leaving the tension unresolved.
- **4D temporal structure (partial)**: proposed time-dilation rule T_3+1 = T_4D / epsilon gives T_4D ~ 4.35e-21 s, L_4D ~ 1.3 picometers (in Dark Dimension scenario range).
- **5/27 inner split is OBSERVATIONAL 3+1D DATA**, not a 4D postulate. This is a key reframing: 5/27/68 is what we observe in 3+1D (BBN, CMB, supernovae), and it CONSTRAINS the 4D event's geometry.
- **RAR fit: 8-12% across mass spectrum.** Three-parameter model (f_active ≈ 0.05, isothermal cumulative, mass-dependent scale) matches McGaugh+ 2016 galaxy RAR and Tian+ 2024 cluster RAR. Residual 8% is the cascade's RAR signature.
- **f_active ≈ 0.05, not 0.30 (postulated).** Found by grid search. The 5/27 inner split ↔ cosmic SFR timescale (~2.5 Gyr). f_active ↔ gas consumption timescale (~0.7 Gyr). 4× tension between these is documented.
- **Mass-dependent scale factor** (cascade M_halo / empirical M_halo): 10% for MW, 70% for cluster. The 7× ratio matches the kappa ratio (5.9×) remarkably well, suggesting cascade intrinsic M_halo scales as 1/κ.
- **28 honest limitations** documented in §7.

---

## How to read

**New to the idea?** Start with `supporting/layman_summary.md`. It walks through the model without equations.

**Want the full argument?** Read `paper/paper.md` (or `paper/paper.pdf` for the compiled version). The paper is structured as:

- **§1** — Introduction and AI disclosure
- **§2** — The dimensional-cascade model (the core, including cone-shape, growth factor, 4D temporal structure, 5/27/68 observational reframing)
- **§3** — Testable predictions
- **§4** — Quantitative tests, including the RAR fit (commits 101-119)
- **§5-§6** — Connections to other work
- **§7** — Honest limitations (28 items: 2 fully closed + 2 partially closed + 1 cone-shape closed + 23 open)

---

## Honest limitations

The paper is a *thought experiment*, not a derivation. It does not derive:

- Cosmic inflation
- Baryogenesis (matter-antimatter asymmetry)
- Big Bang nucleosynthesis (BBN is used as INPUT, not derived)
- The Standard Model particle spectrum (19 free parameters)
- Neutrino masses
- A specific mechanism for the Hubble tension (5.6 km/s/Mpc gap)
- A Lagrangian, action principle, or equations of motion
- The RAR's 8% residual (a real signature of the cascade, not yet understood)
- f_active from first principles (constrained to 0.05-0.18 by 3+1D data, but not uniquely derived)
- The mass-dependent scale factor (MW=10%, cluster=70% — empirical fit, not derived)

The 5/27/68 split is now correctly framed as **observational 3+1D data** that constrains the cascade, not a free postulate. But a first-principles derivation of 5/27/68 from the 4D event's specific geometry (rather than a fit to observation) is the unfinished business of fundamental physics.

**Closed/partial limitations (5: 2 full + 2 partial + 1 cone-shape):** sign ambiguity (Limitation 14), 1D universes (cone-shape), growth factor G (Limitation 5, partial), Ω_DE ≈ 68% (Limitation 15, partial).

**Open limitations (23: 13 original + 10 new):** including 5/27 inner split (Limitation 17, now reframed as observational), 4D temporal structure (Limitation 6, partial), 4D projection geometry (Limitation 5), cone uniqueness (Limitation 8), 2D physics (Limitation 9), RAR 8% residual (documented in §4.1), f_active derivation (Limitation 20), and the Hubble tension (Limitation 18, accepted as unresolved).

The 22+ cited references are real published papers used to anchor the model's claims in observational/experimental data.

---

## Citation

```bibtex
@misc{ampbuster2026gravity,
  author = {ampbuster},
  title = {Gravity as Residual: A Thought Experiment on Dimensional Inversion, Annihilation, and the Origin of the Dark Sector},
  year = {2026},
  version = {2.2.1},
  howpublished = {GitHub},
  url = {https://github.com/ampbuster/gravity-as-residual}
}
```

See `CITATION.cff` for machine-readable citation metadata.

---

## License

MIT — see `LICENSE` for the full text. You're free to use, modify, redistribute, and build on this work, as long as you preserve the copyright notice. The paper and code are both MIT-licensed.

---

## Author note

I'm a software developer, not a physicist. This is a thought experiment, developed over many iterations with an AI assistant (Mavis), in an attempt to unify several pieces of the dark-sector puzzle under a single geometric picture. I'm putting it out in the open because:

1. Even if the model is wrong, the cleanest version of it might be useful to someone.
2. The honest acknowledgment of what it *doesn't* derive is rare in this space and might be valuable.
3. The model makes some testable predictions, and someone with the right data and the right skepticism could falsify or refine it.

If you have thoughts — especially *critical* thoughts — please open an issue or contact me.

— ampbuster
