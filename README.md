# Gravity as Residual

> A thought experiment on dimensional inversion, annihilation, and the origin of the dark sector.

**Author:** A non-specialist (software developer)  
**AI assistance:** Developed in conversation with Mavis (Claude), disclosed in §1 and `ai_disclosure.md`  
**Version:** 2.0 (June 2026)  
**Status:** Submitted to ai.viXra.org (reference: 18068418)

---

## The idea in one paragraph

What if gravity is *weak* because most of it gets cancelled? In this model, a single ongoing 4-dimensional event projects into our 3+1-dimensional universe. The projection *inverts* the sign of gravity, so the 4D event's native gravity is cancelled on the 3+1D brane — leaving only a small positive residue that we call ordinary gravity. The un-cancelled *antigravity* component is what we observe as **dark energy**. Every energetic event in 3+1D (a star, a supernova, a black hole) creates a *child universe* at the next level (a 2D universe embedded in our 3+1D space). When that 2D universe dies in a Big Crunch, its death-flash back-projects to 3+1D as *attractive* gravity — which we observe as **dark matter**. The model is *intentionally ending-agnostic* — five possible universe endings (fixed-time boundary, cyclic, diminishing cyclic, Big Rip, Big Freeze) are all empirically distinguishable by upcoming observatories (Euclid, Roman, LSST, SKA).

---

## Contents

| Folder / File | What's in it |
|---|---|
| `paper/paper.md` | The full paper, v2.0 (markdown source) |
| `paper/paper.pdf` | Compiled PDF (60 pages) |
| `supporting/layman_summary.md` | Plain-language summary for general readers |
| `supporting/reddit_summary.md` | Shorter summary for social media |
| `supporting/publication_strategy.md` | Notes on where to publish |
| `calculations/numerical_verification.py` | Python script — re-derives every numerical claim |
| `changelog.md` | v1.02 → v2.0 version history |
| `ai_disclosure.md` | How Mavis was used in the development |
| `LICENSE` | MIT License |
| `CITATION.cff` | How to cite this work |

---

## How to read

**New to the idea?** Start with `supporting/layman_summary.md`. It walks through the model without equations.

**Want the full argument?** Read `paper/paper.md` (or `paper/paper.pdf` for the compiled version). The paper is structured as:

- **§1** — Introduction and AI disclosure
- **§2** — The dimensional-cascade model (the core)
- **§3** — Testable predictions
- **§4** — Speculative extensions to other physics (sub-mm gravity, CMB, black holes, weak/strong forces, ...)
- **§5-§6** — Connections to other work
- **§7** — Honest limitations (15 items)

**Want to verify the math?** Run `python3 calculations/numerical_verification.py`. It re-derives every number claim from first principles.

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

It also does not provide a Lagrangian, action principle, or equations of motion. The "Mathematical sketch" in §2.4 is *qualitative* — it shows the *shape* of the cancellation, not the specific numbers. The specific values of dark energy and dark matter densities are not derived from first principles; they are observed inputs.

The 22 cited references are real published papers used to anchor the model's claims in observational/experimental data.

---

## Citation

```bibtex
@misc{ampbuster2026gravity,
  author = {ampbuster},
  title = {Gravity as Residual: A Thought Experiment on Dimensional Inversion, Annihilation, and the Origin of the Dark Sector},
  year = {2026},
  version = {2.0},
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
