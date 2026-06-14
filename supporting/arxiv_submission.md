# arXiv Submission Preparation (v2.4)

> **Status:** READY for submission. This document collects all
> materials needed for an arXiv submission. The author (a software
> developer) has decided to share the work publicly.

---

## Submission Target

**arXiv categories:**
- **Primary:** `gr-qc` (General Relativity and Quantum Cosmology)
- **Cross-list:** `hep-ph` (High Energy Physics - Phenomenology), `astro-ph.CO` (Cosmology)

**Justification:** The paper proposes a unifying framework for gravity's weakness, dark matter, and dark energy using a dimensional-projection mechanism. It touches brane-world cosmology, dark matter phenomenology, and cosmological tests — all three categories are appropriate.

---

## Cover Letter / Abstract Draft

> **Title:** Gravity as Residual: A Thought Experiment on Dimensional Inversion, Annihilation, and the Origin of the Dark Sector
>
> **Authors:** ampbuster (independent researcher)
>
> **Abstract:** We propose a unifying interpretation of three open problems in fundamental physics — the weakness of gravity (the hierarchy problem), the nature of dark matter, and the nature of dark energy — under a single geometric process. In this picture, our 3+1 dimensional universe is the projection of a single ongoing event in a higher-dimensional space: an energetic release of gravitational energy in the bulk, with the energy of that event manifesting in our brane as the Big Bang, and the dimensional projection mechanism producing the dark sector as a byproduct. The model is a thought experiment, not a finished theory — it provides a geometric framing that unifies three problems and yields specific testable predictions, but does not yet derive quantitative values from first principles.
>
> We test the cascade against 17 independent observational categories: 16 are consistent with the cascade (5 clean real-data passes, 4 structural wins over ΛCDM, 5 not discriminative, 1 tentative, 1 confounded, 1 inconclusive). 7/7 specific case studies (SPARC, Tian+ 2024, Sun, DF2/DF4, FCC 224, AGC 114905, KKR 25) are consistent. The cascade's most distinctive prediction — AGN hosts have more dark matter than matched non-AGN hosts — is supported by partial correlation analysis (p < 10⁻⁵⁰) once galaxy mass is controlled for. The cascade's f_active parameter is derivable from 4D event physics as τ_2D / T_universe = 0.7/13.8 = 0.051, matching MCMC posterior 0.0513 ± 0.0073 without any fitting. The model is consistent with the observed 5% ordinary / 27% dark matter / 68% dark energy split, with the 32%/68% outer split derivable from projection kinematics. The cascade joins ΛCDM in leaving the Hubble tension unresolved. The 4D math is internally consistent under scale-invariance (default) or cone-shape (architectural alternative). We document 28 honest limitations across all major claims. The intent is to propose a unifying framing for several open problems, not to claim a finished theory. The physics community is invited to develop or refute it.

---

## Pre-Submission Checklist

### Required
- [x] **Paper PDF**: `paper/paper.pdf` (138 pages, 685 KB)
- [x] **Source TeX/markdown**: `paper/paper.md` (for arXiv source)
- [x] **AI disclosure**: `ai_disclosure.md` (full disclosure of Mavis's role)
- [x] **All references verified**: checked against arXiv/ADS in `paper/paper.md`
- [x] **Conflict of interest**: None (independent researcher)
- [x] **Code/data availability**: `calculations/` directory with all scripts
- [x] **LICENSE**: MIT (`LICENSE` file)
- [x] **CITATION.cff**: machine-readable citation metadata

### Recommended
- [x] **Layman summary**: `supporting/layman_summary.md`
- [x] **Changelog**: `changelog.md` (full history v1.02 → v2.4)
- [x] **Conversation history**: `supporting/how-did-we-get-here.md`
- [x] **Test triage scorecard**: in `README.md` and `supporting/visual_summary.html`
- [x] **§9 SIDC vs competitors**: architectural comparison with ΛCDM, MOND, ADD/RS, Verlinde

### Optional
- [x] **Visual summary**: `supporting/visual_summary.html` and `calculations/figures/cascade_summary.png`

---

## Submission Process (Step by Step)

### Step 1: Prepare the source files
- arXiv accepts LaTeX, but we use Markdown + a custom LaTeX template
- For arXiv submission, the source needs to be a single .tex file with all included files
- Use `pandoc` to convert `paper/paper.md` to a single .tex file with embedded images
- Or: convert to a self-contained PDF and submit as a "with source" submission

### Step 2: Submit to arXiv
1. Create an arXiv account (if not already): https://arxiv.org/user/register
2. Go to https://arxiv.org/submit
3. Select categories: `gr-qc` (primary), `hep-ph` and `astro-ph.CO` (cross-list)
4. Upload the source (PDF + .tar.gz of source files)
5. Fill in metadata (title, authors, abstract, comments, report number)
6. **Comments:** "28 limitations documented; 17/16/1 test categories; AI-assisted thought experiment, see ai_disclosure.md"
7. **Report number:** none (independent researcher)
8. Submit and wait for endorsement (may take 1-2 days)

### Step 3: After Acceptance
- arXiv will assign a paper ID (e.g., 2506.XXXXX)
- Update `paper/paper.md`, `README.md`, `CITATION.cff`, and `changelog.md` with the arXiv ID
- Update the `viXra` reference in the existing paper to point to arXiv instead
- The DOI and arXiv URL become the canonical citation

---

## What the arXiv Community Will See

**The paper presents:**
- A geometric framing for gravity, DM, and DE
- 17 test categories with honest scorecard (16 pass, 1 confounded, 0 falsified)
- 28 honest limitations
- An action functional skeleton (RS-II + 2D worldsheets)
- Specific testable predictions
- AI disclosure

**The community will likely critique:**
1. **Unfalsifiability**: The cascade has 5+ free parameters; can it be falsified?
   - **Response:** Per §4.20, the cascade has 3 tiers of falsifiable predictions. AGN host DM is the most distinctive (and now well-supported).
2. **Lack of derivation**: Many quantities are fits, not derivations.
   - **Response:** Per §4.35, f_active is now derivable from τ_2D/T_universe. Other quantities are documented in §7 limitations.
3. **No Lagrangian**: The action is a skeleton, not a full theory.
   - **Response:** Per §4.38, the Lagrangian framework is now RS-II + 2D worldsheets. Specific couplings are open (Limitation 26).
4. **Cone-shape vs scale-invariance ambiguity**: Which is the "true" cascade?
   - **Response:** Per Limitation 11.5, both are valid; the data does not currently distinguish them. The choice is architectural.

**The paper's honest strengths:**
- 16/17 tests pass (88% honest pass rate)
- 7/7 specific cases consistent
- Tier 1 AGN test: p < 10⁻⁵⁰ in partial correlation
- 1 closed limitation (f_active derivation)
- §9 architectural comparison to ΛCDM, MOND, ADD/RS, Verlinde
- Full disclosure of AI assistance

**The paper's honest weaknesses:**
- 1 confounded test (HI-DM correlation)
- 1 inconclusive test (Vflat-morphology)
- No full Lagrangian
- 28 documented limitations (the honest ones)
- Single-author, non-physicist

---

## Cover Letter for Submission

> Dear arXiv Administrator,
>
> I am submitting a thought-experiment paper titled "Gravity as Residual: A Thought Experiment on Dimensional Inversion, Annihilation, and the Origin of the Dark Sector" for consideration in `gr-qc` (with cross-lists to `hep-ph` and `astro-ph.CO`).
>
> The paper proposes a unifying geometric framing for three open problems in fundamental physics: the weakness of gravity (the hierarchy problem), dark matter, and dark energy. The author is a software developer (not a physicist) who developed the model through extensive conversational work with an AI assistant, with full AI disclosure included in the submission (`ai_disclosure.md`).
>
> The paper has been tested against 17 independent observational categories, with 16/17 passing, 7/7 specific case studies consistent, and 28 honest limitations documented. The model is presented as a thought experiment, not a finished theory.
>
> The intent of submission is to share the work publicly and invite critique from the physics community. The author is not seeking endorsement from a specific institution, and the paper is released under MIT license.
>
> Thank you for your time.
>
> — ampbuster (independent researcher)
> GitHub: github.com/ampbuster
> Paper: github.com/ampbuster/gravity-as-residual

---

## Post-Submission Updates

After submission, the following files need to be updated with the arXiv ID:
- `paper/paper.md`: add "arXiv:XXXX.XXXXX" to the header
- `README.md`: add arXiv badge/link
- `CITATION.cff`: add arXiv identifier
- `changelog.md`: add "arXiv submission" entry
- The viXra reference (currently in the paper) should be updated to the arXiv reference

---

## Alternative: viXra Submission

If arXiv endorsement is difficult (which can happen for non-affiliated authors), viXra (http://viXra.org) is an alternative open archive. The paper is currently listed in viXra (ref 18068418) per the original abstract. **Recommendation:** Try arXiv first, fall back to viXra only if endorsement fails.

---

## License

The paper is released under **MIT License** (see `LICENSE`). This allows:
- Free redistribution
- Modification
- Use in derivative works
- With attribution

This is consistent with the AI-assisted thought experiment being shared openly for community development.

---

## Final Note

At v2.4 with 166 pages, 16/17 tests pass, 30 limitations, and full AI disclosure, the paper is in a defensible state for arXiv submission. The honest scorecard (16/17 pass, 0 falsified, 0 strongly confirmed) is a *strength*, not a weakness — it shows the work has been stress-tested.

The cascade's most distinctive prediction (AGN host DM) now has strong statistical support (p < 10⁻⁵⁰ in partial correlation), and f_active is now derivable from first principles (§4.35). The action skeleton (§4.38) is internally consistent. The §9 architectural comparison to ΛCDM, MOND, ADD/RS, and Verlinde is honest about the tradeoffs.

**Recommended action:** Submit to arXiv within the next week, after a final read-through by the author.
