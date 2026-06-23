# Release Notes — v3.5.9-A2

**Tag**: `v3.5.9-A2`
**Commit**: `e25fbdc`
**Date**: 2026-06-23

## Highlights

**L308ce**: Audited and fixed 5 consistency issues in Qwen's LaTeX arxiv paper. The 6-page arxiv paper (`paper/arxiv/paper_arxiv.tex`) is now fully consistent with the SIDC framework.

### Fixes applied
- `γ_4D` correctly named "cascade amplification factor" (not "time dilation")
- Fraction of 4D time observed corrected from 10⁻²⁶ to ~9×10⁻²⁵
- z transitions clearly distinguished (matter-DE equality z ≈ 0.30 vs decel-accel z ≈ 0.63)
- "EXACT match" language softened to "accommodated... rather than first-principles derived"
- C(6) connection described as "isomorphic to" SM algebra, with "additional physical postulate required" caveat

### What's in this release

- **`paper/paper.pdf`** — Main paper, 597 pages, 1.94 MB
- **`paper/arxiv/paper_arxiv.pdf`** — Condensed arxiv paper, 6 pages, 82 KB
- **`paper/arxiv/paper_arxiv.tex`** — LaTeX source for the arxiv paper
- **`paper/arxiv/paper.md`** — Markdown source (reference only)
- **`paper/arxiv/build_arxiv.sh`** — Self-contained build script
- **`README.md`** — Top-level summary
- **`STATE_OF_THE_MODEL.md`** — Current model state
- **`CITATION.cff`** — Citation metadata

### Full changelog from v3.5.7+ to v3.5.9+ A2

The L308 chain (L308ab-L308ce) covers:
- **L308ab** — kL=76.4 re-calibration, M_Pl,4D via α-GM
- **L308ac** — f_DE re-derivation in A2
- **L308ad-af** — A1→A2 transition
- **L308ag-ah** — Frame-neutral naming
- **L308ai-aj** — Mirror geometry fix for ghost problem
- **L308ak** — Calibrated parameter accounting
- **L308al-an** — MCMC observational tests
- **L308ao-ap** — Parameter hierarchy
- **L308aq-ar** — Test matrix
- **L308as** — Galaxy Zoo analysis
- **L308at-au** — C(6) SM algebra (Stoica 2018)
- **L308av** — Option B Strengthened
- **L308aw** — Halving rule = Bott periodicity
- **L308ax** — Cascade dimension invariance
- **L308ay** — MCMC audit v2
- **L308az** — Mirror geometry ghost fix
- **L308ba** — Halving rule (N_D = 12/2^(D-2))
- **L308bb** — 93% Lagrangian audit
- **L308bc** — DOF conservation
- **L308bd-be** — First-principles re-framing
- **L308bf** — Status note
- **L308bg** — Web research audit
- **L308bh** — C(6) IS the SM Algebra (Stoica 2018)
- **L308bi** — Option B Strengthened
- **L308bj** — Halving Rule First-Principles
- **L308bk** — Cascade Dimension Invariance
- **L308bl** — REJECTED (Hubble tension via f_leak)
- **L308bm** — Framework Audit
- **L308bn** — M_Pl,4D Re-Derivation in A2
- **L308bo** — DE/DM Ratio Evolution
- **L308bp** — DM-DE Unification
- **L308bq** — Decel-Accel Transition (z_t = 0.63)
- **L308br** — DM/DE Cleaner Narrative (DE = const, DM = depleted)
- **L308bs** — TIGHT vs LOOSE Correlation
- **L308bt** — TIGHT Overshoots Hubble Tension
- **L308bu** — Logical Audit Pass (15 params verified)
- **L308bv** — Observational Predictions (Euclid/Roman/SKA)
- **L308bw** — 4D Burst Thought Experiment
- **L308bx** — Paper Consistency Audit (3 MAJOR inconsistencies fixed)
- **L308by** — §3.72 Lagrangian Summary
- **L308bz** — §3.68 Lagrangian Re-Audit v2 (96%)
- **L308ca** — Condensed Paper for arXiv
- **L308cb** — Build Tools Fix (lmodern, \tightlist, \real, \pandocbounded)
- **L308cc** — Qwen Critique Addressed
- **L308cd** — Qwen LaTeX Template Adopted
- **L308ce** — Audit Qwen LaTeX for Consistency (THIS RELEASE)

### Key claims (with caveats)

**Testable predictions:**
1. **w = -1 EXACTLY** (no evolution, tighter than ΛCDM) — testable by Euclid (2024+), Roman (2027+)
2. **DE/DM ratio follows (1+z)⁻³ EXACTLY** — testable by BAO + growth rate f(z)σ_8
3. **M_Pl,2D = 2.95 TeV** — testable at HL-LHC as anomalous missing-energy threshold

**Numerical values (A2):**
- ε = 6.32×10⁻³⁴
- f_DE,closed = 1.79×10⁻⁹⁰
- γ_4D = 1.10×10¹¹¹
- τ_3D,apparent = 1.66×10¹⁴⁵ yr
- ρ_DE = 2.5×10⁻⁴⁷ GeV⁴ (matches observed)
- f×ε invariant = 1.13×10⁻¹²³ (preserved across A1 and A2)
- H_0 = 67.4 km/s/Mpc (Planck, inherited from ΛCDM)
- r_s = 141.85 Mpc (1.88% off Planck 144.57)

**15 parameters:**
- 1 MEASURED (M_Pl,3D)
- 3 FIRST-PRINCIPLES (α, M_Pl,2D, μ)
- 2 DERIVED (M_Pl,4D via α-GM, E_4D via N_sub × E_sub)
- 4 CALIBRATED (ε, τ_4D, AGN rate, f_leak,3D→4D = H_0)
- 4 STRUCTURAL (E_sub, τ_3D,apparent, γ_4D, N=12)
- 1 FREE (N_sub = 386)

### Citation

```bibtex
@software{ampbuster2026gravity,
  author = {ampbuster},
  title = {Gravity as Residual: A Thought Experiment on Dimensional Inversion, Annihilation, and the Origin of the Dark Sector},
  version = {v3.5.9-A2},
  year = {2026},
  url = {https://github.com/ampbuster/gravity-as-residual},
  doi = {10.5281/zenodo.XXXXXXX}  % to be filled in
}
```

---

**Full development log**: see the 597-page paper and `paper/markdown/` directory.
