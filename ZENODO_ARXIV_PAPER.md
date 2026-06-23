# Optional: Manual Zenodo Upload for the arxiv Paper

If you want a **separate DOI** specifically for the condensed arxiv paper (rather than the whole repo), use this approach. This is Option A from the discussion.

## When to use this

- You want the arxiv paper to have its own DOI distinct from the repo
- You want a clean citable record that links to the full work on GitHub
- You want a "publication-ready" record without exposing the full development log

## Steps

1. Go to **https://zenodo.org** and log in
2. Click **Upload** (top navigation)
3. Click **New upload** → **Start a new record**
4. Fill in the metadata (see below)
5. Upload the files
6. Click **Publish**
7. Get your DOI

## Metadata to use

### Basic info

- **Title**: `Gravity as Residual: A Geometric Framework for the Dark Sector via Scale-Invariant Dimensional Cascades`
- **Publication date**: 2026-06-23
- **Resource type**: Preprint (or "Other" if you want to be flexible)

### Authors

- **Name**: Lee, Jia Ray
- **Affiliation**: Independent Researcher
- **ORCID**: (skip if you don't have one)

### Description

```markdown
This is the condensed arxiv-ready version of "Gravity as Residual", a thought
experiment proposing that gravity, dark matter, and dark energy emerge from
a unified dimensional projection mechanism (Scale-Invariant Dimensional
Cascade, SIDC).

The full 597-page development paper and all supporting materials are available
at the GitHub repository: https://github.com/ampbuster/gravity-as-residual

## Abstract

We propose a phenomenological geometric framework—the Scale-Invariant
Dimensional Cascade (SIDC)—in which gravity, dark matter, and dark energy
emerge from a unified dimensional projection mechanism. The framework
postulates a three-level hierarchical cascade (4D bulk event → 3+1D brane →
2D terminal quantum gravity floor) governed by a Z_2 mirror symmetry at the
3+1D boundary. Downward dimensional projection induces an effective sign-flip
in the gravitational coupling (yielding dark energy), while upward projection
preserves standard attractive gravity (yielding dark matter). The cascade's
structural parameters (N_2D = 12, N_3+1D = 6, N_4D = 3) are motivated by
Clifford algebra representations and Bott periodicity. We construct an
effective action that matches the observed dark energy density
(ρ_DE = 2.5×10⁻⁴⁷ GeV⁴) via cascade structure, and yields three sharp,
falsifiable predictions: (i) w = -1 exactly, with no high-redshift evolution;
(ii) DE/DM density ratio scaling precisely as (1+z)⁻³; and (iii) a structural
2D Planck scale at M_Pl,2D = 2.95 TeV.

## Key results

- 16/17 observational test categories pass (1 confounded)
- 7/7 specific cases pass (SPARC, Tian+ clusters, DF2/DF4, AGC 114905, KKR 25)
- ρ_DE matches observation within 0.13%
- 15 parameters total (1 measured, 3 first-principles, 2 derived, 4 calibrated,
  4 structural, 1 free)
- Three testable predictions for Euclid (2024+), Roman (2027+), SKA (2030+)

## License

CC-BY-4.0

## Related identifiers

- GitHub: https://github.com/ampbuster/gravity-as-residual
- Full paper: see GitHub repo for the 597-page version
```

### Keywords

- dark matter
- dark energy
- modified gravity
- extra dimensions
- dimensional cascade
- Clifford algebra
- Bott periodicity
- cosmological constant problem
- coincidence problem

### License

- **License**: Creative Commons Attribution 4.0 International (CC-BY-4.0)

### Funding

- Skip (no funding)

### Related works

- **Is referenced by**: (skip)
- **Is referenced by**: (skip)
- **Is supplement to**: `https://github.com/ampbuster/gravity-as-residual`

## Files to upload

1. `paper_arxiv.pdf` (the 6-page PDF, 82 KB)
2. `paper_arxiv.tex` (the LaTeX source, 16 KB)

## What you get

- A DOI like `10.5281/zenodo.XXXXXXX`
- A landing page with metadata, abstract, and download links
- A BibTeX export for easy citation

## Citation

Once uploaded, the paper can be cited as:

> Lee, Jia Ray. (2026). Gravity as Residual: A Geometric Framework for the Dark Sector via Scale-Invariant Dimensional Cascades. Zenodo. https://doi.org/10.5281/zenodo.20810441

## Notes

- **Don't upload the full 597-page paper to this record** — keep it on GitHub. The arxiv paper is the focused "publication" version.
- **The GitHub integration (Option B) is the simpler approach** if you don't need a separate DOI. See `ZENODO_SETUP.md` for that.
- **You can do both** — the GitHub integration archives the full repo with one DOI, and this manual upload gives the arxiv paper its own DOI.
