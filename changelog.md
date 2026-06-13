# Changelog

All notable changes to this paper are documented here.

## v2.0 (June 2026) — Current

**First public release.** Numerical errors fixed, internal consistency cleaned up (alternating cascade → universal bulk-brane cancellation, two-types-of-endings → ending-agnostic, **strict inversion principle → downward perceptual inversion principle** (4D gravity stays attractive in 4D; inversion is brane perception of projected contribution, *grounded in the standard GR $\rho + 3P < 0$ mechanism* for negative effective gravitating density — the same mechanism that drives cosmic inflation and dark energy in our universe), **dark matter = death-flash → dark matter = cumulative energy return** — Big Crunch gives brief death-flash, heat death gives slow diffuse return, mix depends on event size), speculative sections removed, honest acknowledgments added throughout.

**Energy budget clarifications** (added June 2026): (1) the 4D event's energy delivery to 3+1D may be <100% efficient, parameterized by $f_{\text{deliver}} \leq 1$ (default: full delivery, the most parsimonious assumption); (2) the 2D universe is *one channel* of an event's total energy budget (alongside heat, light, neutrinos, gravitational waves, etc.), not a separate effect requiring additional energy.

**Universal-split self-consistency** (added June 2026): added §2.6 subsection showing that the cascade is self-consistent under the assumption that the same 5%/27%/68% energy budget split applies at *every* level of the cascade (by the strongest form of the scale-invariance principle). Under this assumption, the 2D universe's mass-energy is dominated by its own dark energy (68%) and its own dark matter (27%, from cumulative 1D universe back-projection in 2D), with the original event energy being only 5% of the 2D universe's total mass-energy budget. The 32% attractive fraction (5% + 27%) projects up to 3+1D as part of our DM. This naturally explains why the 2D universe's total mass-energy can be much larger than the original event energy — the 2D universe is dark-energy dominated and has its own expansion that grows its mass budget, just as in our universe. The model is self-consistent under this universal-split assumption, but the assumption is a *postulate* (not derived from first principles). A specific implementation would need to derive the 5%/27%/68% split from a particular bulk-brane geometry and 2D universe dynamics, which is left to future work.

**Neutrino discussion expanded** (added June 2026): §2.3 now has explicit subsections on (1) the energy-deposition threshold principle (neutrinos in flight don't count, only interactions), (2) the Sun-vs-galaxy distinction (Sun has neutrinos but no DM, galaxy has both), (3) the Standard Model origin of neutrinos (β decay, β+ decay, electron capture, muon/tau decays all emit neutrinos), and (4) the question of neutrino-DE interaction (no novel cascade coupling, neutrinos feel the 4D event's antigravity via standard GR). The Sun's 10³⁸/s neutrino rate is *not* a coincidence with the cascade's ε ~ 10⁻³⁸ — they are physically unrelated — but the rate creates a *problem* the energy-deposition threshold resolves (otherwise the Sun would dominate DM via neutrino emission).

**Hierarchy-DE unification insight** (added June 2026): added §2.6 subsection noting that the cascade's bulk-brane coupling ε ~ 10⁻³⁸ and the hierarchy 10³⁸ are *the same physical quantity* (bulk-brane coupling) in different forms. The hierarchy = 1/ε, and the dark energy ∝ ε · f_back. The "coincidence" 10³⁸ = 1/10⁻³⁸ is the *signature* of this unification, not a coincidence in the cascade's framing. The two numbers are structurally related: gravity is weak in 3+1D by 10³⁸ *because* the bulk-brane cancellation removes most of the 4D event's projected gravity; the dark energy is a small un-cancelled fraction of the same projected antigravity, modulated by f_back. In RS brane-world physics, the analogous parameter is the warp factor e^(-kr_c) — the cascade's ε is the analogous parameter.

**Section 5 reduced to a brief pointer** (June 2026): the original §5 was a full restatement of §2.3's content (since §2.3 has grown to cover all the material). §5 is now a brief pointer that explains its role as a narrative marker and points readers to §2.3 for the substantive content. This keeps the table of contents and cross-references stable without duplicating content.

**Self-corrections and "Numerical correction" notes removed from body** (June 2026): seven "Numerical correction" or self-correction notes were removed from the body (lines that said "an earlier version said X, corrected to Y" or "this is not because X — that phrasing is misleading"). The corrections are documented in this changelog, not in the body. The body now reads as a finished work, with all numerical claims stated correctly and no meta-commentary about earlier wrong versions.

**Parameter list consistency fix** (June 2026): the §2.6 "Honest quantitative assessment" subsection previously listed "three free parameters (ε, f_inv, cascade partition)" but f_inv was an orphan variable (used nowhere else), f_deliver (added later) was missing, and f_back (used throughout) was missing. Replaced with the actual four parameters used in the paper: ε_{3+1D} ~ 10⁻³⁸, f_back ~ 10⁻⁸⁵, f_deliver ≤ 1, and cumulative 2D back-projection efficiency. The other parameter list at line 269 (R, τ_2D, E_2D, projection fraction) is properly contextualized as the *DM-specific* parameters, not the *global* parameters.

**Version header trimmed** (June 2026): the v2.0 version header at the top of paper.md was 1126 chars (describing all v1.x → v2.0 changes inline). Trimmed to 369 chars (one-line summary pointing to changelog for details).

### Numerical fixes

| Section | Old (wrong) | New (correct) |
|---|---|---|
| §2.3 SN τ_2D | 10⁻¹⁰ s | 33 s |
| §2.3 LHC τ_2D | 10⁻²⁵ s | 3×10⁻²⁴ s |
| §4.7 SN visible light | 10⁴⁹ ergs | 1.6×10⁴⁸ ergs (10⁶⁰ eV conversion) |
| §4.7 Sun total output | 7.5×10⁵² ergs | 1.2×10⁵¹ ergs |
| §4.10 Sgr A* Schwarzschild | 10¹⁰ m | 1.2×10¹⁰ m |
| §4.10 Sgr A* 2D lifetime | 30 s | ~40 s |
| §4.10 "1% of Sun's total" | 1% | 0.1% |

### Removed sections

- **§4.6** (neutrino mass) — *removed*. Neutrino mass is a Standard Model physics question, not addressed by this model.
- **§4.12** (neutrino interpretation) — *removed*. The neutrino interpretation was speculative and introduced internal inconsistencies. Neutrino properties are taken as given in the Standard Model; the dimensional-cascade framework does not currently address them.

### Internal consistency cleanup

- **"Alternating cascade" framing** (odd levels attractive, even levels repulsive) was *replaced* with the **"universal bulk-brane cancellation" framing** (every level similar to 3+1D, just at smaller scales). The model is now a *fractal hierarchy of similar universes*, not a parity-based alternating structure.
- **"Two types of endings"** (odd=heat death, even=Big Crunch) was *replaced* with **"ending-agnostic" framing** (every level has similar dynamics; the same 5 possible endings apply at every level).
- **L310 contradiction** (model does not predict heat death, then Big Freeze added) was *refined* to acknowledge the Big Freeze as a possible ending while clarifying the paper's *default* is the fixed-time boundary.

### New content

- **§2.5 "Universal bulk-brane cancellation"** — every level has the same basic structure as 3+1D
- **§2.5 "Summary of the cascade framework"** — 10 core claims listed explicitly
- **§2.5 "Lensing and the inversion principle"** — strict cascade inversion
- **§2.5 "Dark matter = cumulative energy return from 2D universe endings"** — Big Crunch gives brief death-flash, heat death gives slow diffuse return, mix depends on event size (consistent with smooth observed dark matter + activity-dependence)
- **§2.6 "Energy budget breakdown"** — 5%/27%/68% made explicit
- **§2.6 "Symmetries and conservation laws"** — explicit list of model assumptions
- **§2.6 "Honest acknowledgment"** — what the model does and does not address
- **§2.1 "All universes are 3+1D" terminology note** — D-labels are placeholders
- **§2.8 "Five possible universe endings"** — fixed-time boundary, cyclic, diminishing cyclic, Big Rip, Big Freeze (all empirically distinguishable)
- **§2.8 "Cascade is infinite in principle, finite in practice"** — depth clarification
- **§2.8 "The model is intentionally ending-agnostic"** — explicit framing
- **§2.8 "Inception analogy"** — for time-dilation across levels
- **§2.8 "Quantum mechanics as 2D-level Standard Model projection"** — reframing
- **§4.5 "Inflation, matter-antimatter asymmetry, and other open issues"** — honest acknowledgment

### Cascade depth clarification

The cascade is *infinite in principle* (no a priori depth limit) but *practically finite* (energy decreases at each level, eventually too small to create a new universe). Labels can extend to "-1D", "-2D", etc., but the *quantitative* cascade truncates at some Planck-scale or energy-threshold depth.

### Energy budget explicit

~5% ordinary, ~27% DM, ~68% DE. The "ordinary/dark sector" split is ~5%/~95%, with the dark sector being ~27% (DM) + ~68% (DE) = ~95%.

---

## v1.0 (June 2026) — Initial Public Release (Superseded)

Initial draft. 36 pages, 171 KB. Internal iteration only; not publicly released.

---

## Earlier versions (v0.x)

Internal iteration history, not publicly released. Key milestones:
- v1.00 - Initial model with 4D event and 3+1D universe
- v1.30 - First framing of the "two dark-sector products"
- v1.35 - Scale-invariance introduced
- v1.47 - Scale invariance update
- v1.50 - "Two types of energy" era (later replaced)
- v1.57 - Major simplification pass
- v1.58 - Numerical errors caught and fixed
- v2.0 - This release
