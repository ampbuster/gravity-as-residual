# Gravity as Residual

> A thought experiment on dimensional inversion, annihilation, and the origin of the dark sector.

**Author:** A non-specialist (software developer)  
**AI assistance:** Developed in conversation with Mavis (M3, MiniMax), disclosed in §1 and `ai_disclosure.md`  
**Version:** 2.2 (June 2026)  
**Status:** Public release. 90 commits, 18 honest limitations documented.

---

## The idea in one paragraph

What if gravity is *weak* because most of it gets cancelled? In this model, a single ongoing 4-dimensional event projects into our 3+1-dimensional universe. The projection *inverts* the sign of gravity, so the 4D event's native gravity is cancelled on the 3+1D brane — leaving only a small positive residue that we call ordinary gravity. The un-cancelled *antigravity* component is what we observe as **dark energy**. Every energetic event in 3+1D (a star, a supernova, a black hole) creates a *child universe* at the next level (a 2D universe embedded in our 3+1D space). As each child universe ends, its energy returns to 3+1D — through a *Big Crunch* (brief, intense death-flash) for large child universes where gravity wins, or *heat death* (slow, diffuse return) for small ones where dark energy wins. This *cumulative energy return* is what we observe as **dark matter**. The model is *intentionally ending-agnostic* — five possible universe endings (fixed-time boundary, cyclic, diminishing cyclic, Big Rip, Big Freeze) are all empirically distinguishable by upcoming observatories (Euclid, Roman, LSST, SKA).

---

## Contents

| Folder / File | What's in it |
|---|---|
| `paper/paper.md` | The full paper, v2.2 (markdown source) |
| `paper/paper.pdf` | Compiled PDF (81 pages) |
| `paper/no-lmodern-template.tex` | Custom LaTeX template (no lmodern needed) |
| `supporting/layman_summary.md` | Plain-language summary for general readers |
| `supporting/data/` | Pantheon+ SNe data and covariance matrix |
| `supporting/publication_strategy.md` | Notes on where to publish |
| `calculations/` | 42 Python scripts (numerical verification, derivations, tests) |
| `calculations/cascade_model.py` | The main OO model implementation |
| `calculations/figures/cascade_summary.png` | 9-panel summary figure |
| `changelog.md` | Full version history v1.02 → v2.2 |
| `ai_disclosure.md` | How Mavis was used in the development |
| `LICENSE` | MIT License |
| `CITATION.cff` | How to cite this work |

## Key findings (v2.2)

- **Cone-shaped hierarchy** (4D event → 3+1D → 2D, terminal at 2D; 1D universes do not exist). Closes the 1D-universes limitation.
- **Sign ambiguity RESOLVED** in §2.4: ordinary gravity and dark energy are now two physically distinct small contributions to the effective 3+1D action, not opposite-sign components of the same quantity.
- **Growth factor G = 9.7e7** is DERIVED from 2D universe FRW dynamics (was 1e8 free parameter).
- **Pantheon+ full-covariance test**: cascade's Mechanism B/F H_0(z) prediction REJECTED at 7 sigma. Pantheon+ shows H_0 is constant at ~73 across all z. Cascade's *qualitative* H_0 = 73 prediction is confirmed.
- **Cascade's final H_0 position (Mechanism M)**: cascade accommodates the Hubble tension (predicts 73, not 67.4) but does not resolve the 5.6 km/s/Mpc gap. Joins LCDM in leaving the tension unresolved.
- **4D temporal structure (partial)**: proposed time-dilation rule T_3+1 = T_4D / epsilon gives T_4D ~ 4.35e-21 s, L_4D ~ 1.3 picometers (in Dark Dimension scenario range).
- **5/27 ratio NOT derivable**: confirmed (Limitation 7, 10+ attempts). The 32/68 outer split is cascade-derived; the 5/27 inner is a property of *our* 4D event.
- **18 honest limitations** documented in §7, with status (2 fully closed, 2 partially closed, 14 open. Plus 1 separate limitation (1D universes) closed by cone-shape).

---

## How to read

**New to the idea?** Start with `supporting/layman_summary.md`. It walks through the model without equations.

**Want the full argument?** Read `paper/paper.md` (or `paper/paper.pdf` for the compiled version). The paper is structured as:

- **§1** — Introduction and AI disclosure
- **§2** — The dimensional-cascade model (the core, including cone-shape, growth factor, 4D temporal structure)
- **§3** — Testable predictions
- **§4** — Speculative extensions to other physics (sub-mm gravity, CMB, black holes, weak/strong forces, ...)
- **§5-§6** — Connections to other work
- **§7** — Honest limitations (18 items, 2 fully closed, 2 partially closed, 14 open. Plus 1 separate limitation (1D universes) closed by cone-shape)

**Want to verify the math?** Run `python3 calculations/cascade_model.py` or any of the 42 scripts in `calculations/`. They re-derive every number claim from first principles.

---

## Testable predictions (short list)

1. **Dark matter should track energetic activity** on galaxy scales (more dark matter in galaxies with more star formation, more supernovae, more AGN). The model predicts a *correlation* with star formation rate and supernova rate, not just a fixed profile.
2. **Five possible universe endings** (fixed-time boundary, cyclic, diminishing cyclic, Big Rip, Big Freeze) are all empirically distinguishable by measuring $w$ (dark energy equation of state) with Euclid, Roman, LSST, SKA.
3. **Sub-millimeter gravity tests** (Eot-Wash, Hu et al.) should see *no deviation* from $1/r^2$ down to ~10 μm — the model predicts no new short-range force.
4. **The Radial Acceleration Relation (RAR)** is naturally reproduced by the cumulative back-projection of 2D universes, with a slight activity-dependence that MOND does not predict.

---

## Honest limitations

The paper is a *thought experiment*, not a derivation. It does not derive:

- Cosmic inflation
- Baryogenesis (matter-antimatter asymmetry)
- Big Bang nucleosynthesis
- The Standard Model particle spectrum (19 free parameters)
- Neutrino masses
- The 5/27 ratio (matter/DM inner split)
- The 4D→3+1D projection geometry
- A specific mechanism for the Hubble tension (5.6 km/s/Mpc gap)

It also does not provide a Lagrangian, action principle, or equations of motion. The "Mathematical sketch" in §2.4 is *qualitative* — it shows the *shape* of the cancellation, not the specific numbers. The specific values of dark energy and dark matter densities are not derived from first principles; they are observed inputs.

**Closed/partial limitations (5: 2 full + 2 partial + 1 cone-shape):** sign ambiguity (Limitation 14), 1D universes (cone-shape), growth factor G (Limitation 5, partial), Ω_DE ≈ 68% (Limitation 15, partial).

**Open limitations (14: 11 original + 3 new):** including 5/27 (Limitation 7), 4D temporal structure (Limitation 6, partial), 4D projection geometry (Limitation 5), cone uniqueness (Limitation 8), 2D physics (Limitation 9), and the Hubble tension (Limitation 18, accepted as unresolved).

The 22 cited references are real published papers used to anchor the model's claims in observational/experimental data.

---

## Citation

```bibtex
@misc{ampbuster2026gravity,
  author = {ampbuster},
  title = {Gravity as Residual: A Thought Experiment on Dimensional Inversion, Annihilation, and the Origin of the Dark Sector},
  year = {2026},
  version = {2.2},
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
