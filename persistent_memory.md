# SIDC Persistent Memory

> Project-level persistent notes for the **Scale-Invariant Dimensional
> Cascade** (SIDC) paper. Captures important findings, conventions,
> open work items, and gotchas that should survive across sessions.

**Repo:** [github.com/ampbuster/gravity-as-residual](https://github.com/ampbuster/gravity-as-residual)
**Current version:** v3.0.2 (paper content) / v3.0.21 (build) — 330 pages
**Last updated:** June 17, 2026

---

## 1. The model in one paragraph

SIDC proposes that gravity, dark matter, and dark energy are all
consequences of a single dimensional-projection mechanism:

- A 4D event created our 3+1D universe (the Big Bang)
- That 4D event's gravity, projected into 3+1D, has a *repulsive* component → **dark energy**
- In our universe, every energetic event (supernovae, BH mergers, GRBs, AGN flares, even LHC collisions) creates a tiny **2D universe**
- The 2D universe sits deep in an AdS_5 bulk at depth y_2D set by the creating event's energy
- The cumulative *gravitational back-projection* of all those 2D universes is what we measure as **dark matter**
- The same bulk-brane cancellation that gives gravity its weakness (10⁻³⁸ hierarchy) also gives the un-cancelled antigravity (DE) and the small back-projection fraction (DM)

**The closed loop:** one geometric process (dimensional projection through bulk-brane cancellation) explains three effects (gravity weakness, DE, DM).

---

## 2. The 3 ε's (related through bulk-brane cancellation)

| Symbol | Value | Meaning |
|--------|-------|---------|
| ε_1 | ~10⁻³⁸ | Bulk-brane coupling (gravity hierarchy) |
| ε_2 | ~1.78×10⁻¹⁵¹ | Un-cancelled vacuum (ρ_DE / M_Pl,4⁴) |
| ε_3 | ~10⁻⁸⁵ | Per-2D-universe back-projection fraction (f_back) |

**Same mechanism, different L's** — different physical situations give different ε's because each entity sits at a different bulk depth:
- L_5 (extra-dim size): fixed by 4D-5D Planck matching
- L_2D (2D universe depth): event-dependent, set by E_event

The closed loop is structural, not numerical.

---

## 3. f_back and γ share the SAME α = 1.289

This was the key insight confirmed in **Lagrangian v10** (June 17, 2026):

```
Forward (time dilation):  γ = (E/E_Pl)^α       with α = 1.289
Backward (back-action):   f_back = (E_4D/E)^(1/(2α)) × prefactors
α × 1/(2α) = 1/2                              (round-trip loss)
```

**The composite exponent 1/(2α) = c/α where c = 1/2 = N/24 = 12/24** (Ising central charge).

For SN: γ = 5.49×10⁴⁴, τ_obs = γ × t_Pl = 33 s ✓
For SN: f_back = 8.76×10⁻⁸⁶ ≈ 10⁻⁸⁵ ✓ (off by 0.06 orders)

**§3.60 has the formula.** L52 (closed in v2.7.66): "f_back ≈ 8.6×10⁻⁸⁶ UNIVERSAL, scaling law."

After scaling by (E/E_SN)^(α - 1/(2α)), f_back is **universal** across all 14 event types.

---

## 4. The Lagrangian skeleton (paper §3.62)

```
L_SIDC = L_c=1,Liouville + L_N=12,SYK + L_Schwarzian
```

- **α = 1.289 = 1 + 1/√12** (N=12 SYK saddle, uniquely determined, off by 0.001 from α=1.29)
- α = 1/2 + 1/2 + 1/√12 (Schwarzian + kinematic + SYK correction)
- 1/2 in 2D papers: Schwarzian (τ~√E), DOZZ (b²=1/2), Calabrese-Cardy, etc.
- 1/√12 = 1/(2√3): the 2 is 2D itself, √3 is 3 SM generations
- N=12 = 4 Weyl × 3 generations (Standard Model "backbone")

**Democratic cosmology (§3.17):** all 14 events = SAME operator at different γ. 1 species, 14 γ values.

**Status:**
- ✓ Structure identified
- ✓ Saddle-point derivation of α
- ✗ Full Lagrangian (couplings, cross-couplings, regularization, Z derivation)
- ✗ First-principles derivation of 1/√N (structural match only)

---

## 5. The build infrastructure (v3.0.21)

**Self-contained in repo:**
- `paper/build_pdf.sh` — orchestrator (~1100 lines, documented)
- `paper/build_tools/` — 4 post-processors (wrap_dimexpr, use_linewidth, fix_dashes, fix_sigma)
- `paper/.build/` — intermediate files (gitignored)
- `paper/markdown/` — 16 source files

**Build commands:**
```bash
bash paper/build_pdf.sh                    # full build
bash paper/build_pdf.sh --dry-run          # fast check (README + layman)
bash paper/build_pdf.sh --dry-run FILE.md  # check specific files
```

**Last working build:** 330 pages (June 17, 2026).

**Pre-build state (v3.0.21 commits):**
- c7f6976: post-processors moved into paper/build_tools/
- cc94e52: math fixes from post-3dbd6a7 rebuild
- ee197ab: README "Building the paper" section
- b41ea66: --dry-run mode

---

## 6. Open work items (L41, L42, L43 still OPEN)

| Limitation | Status | What needs to happen |
|------------|--------|----------------------|
| L41: Why μ is its value | OPEN | Derive 2D cosmological constant from first principles |
| L42: Why m_{3+1D} is its value | OPEN | Derive induced 3+1D Planck mass from bulk geometry |
| L43: Lagrangian skeleton → full L | OPEN | Path integral Z, regularization, cross-couplings |
| L48 (REVISED): f_back derived from α | CLOSED for form | Numerical value still calibrated |

**Closing L41-L43 requires:** 2D CFT theoretical physicist or brute-force path integral computation. No plausible path within reach of current SIDC resources.

**v3.0.21 update**: §3.62.1 added — SIDC IS structurally Karch-Randall + JT gravity (Deng et al. arXiv:2211.13415). Z_SIDC = Z_JT × Z_Liouville × Z_SYK is in principle tractable. Lagrangian v13 attempted combined Z computation; α = 1.289 NOT cleanly recovered from Z alone in tested β ranges. L91 (holographic reduction framing) and L92 (3D→2D gravity inversion prior art) added to limitations.

---

## 7. Key conventions (DO NOT BREAK)

### Naming
- Use **SIDC** (not "the cascade", "DC", "Dimensional Cascade")
- **Majorana** fermions (not "Majorana fermions" with extra space)
- **N=12** with explicit equals sign in math, N = 12 in prose

### Notation
- NO Unicode subscripts/superscripts (use LaTeX: `M_{Pl}`, `E_{4D}`)
- NO e-notation in body text (use `$10^{N}$`)
- NO plain text `X_Y` patterns (use `$X_Y$`)
- Use `\sim` or `\approx`, not `~` in math
- Use `×` not `x` for multiplication in math
- Use Unicode minus (`−`) for `w = -1`, etc.
- Use `\frac{a}{b}` not `a/b` in display math

### Math structure
- Display math: `$$...$$`
- Inline math: `$...$`
- α = 1.289 (NOT 1.29 when precise)
- N = 12 (when in math), N=12 (in prose)

### Tables (Pandoc gotchas)
- Blank line BEFORE table
- Blank line BEFORE heading
- NO `---` immediately after table
- Use `\mathrm{}` for non-italic multi-letter subscripts (`\mathrm{AdS}` not `\AdS`)

---

## 8. Important files

**Paper structure:**
- `paper/markdown/00_title.md` — title, v3.0 highlight, honest boundary
- `paper/markdown/01_executive_summary.md` — summary, 17 tests score card
- `paper/markdown/02_glossary.md` — §0 parameter glossary
- `paper/markdown/03_relations.md` — main physics, includes §3.60, §3.62
- `paper/markdown/04_predictions.md` — RAR, AGC/KKR, end-of-universe
- `paper/markdown/06_limitations.md` — 45 honest limitations
- `paper/markdown/07_conclusion.md` — 45 external constraints
- `paper/markdown/10_end_universe.md` — §10 energy-scaling ladder
- `paper/markdown/15_falsifiability_matrix.md` — predictions vs observations

**Supporting:**
- `README.md` — public release with closed-loop intro
- `supporting/layman_summary.md` — 5-step layman version
- `changelog.md` — version history
- `ai_disclosure.md` — AI assistance disclosure
- `calculations/v27_*.py` — 30+ constraint calculations
- `calculations/lagrangian_v[1-9]*.py` — Lagrangian trial-and-error

---

## 9. Recent session summary (June 17, 2026)

**This session's contributions:**

1. **Build infrastructure refactor (v3.0.21)**
   - Moved 4 post-processors from /tmp/ to paper/build_tools/
   - Moved intermediate files to paper/.build/ (gitignored)
   - Added --dry-run mode for fast LaTeX checking
   - Fixed ~30 LaTeX errors from post-3dbd6a7 commits
   - Build: 330 pages

2. **Lagrangian v7-v10 (4 calculations)**
   - v7: Hagedorn, density of states, N=12 spectrum
   - v8: Hagedorn T for N=12 SYK (no finite T_H in Schwarzian regime)
   - v9: f_back from closed loop (3 ε's are RELATED but not equal)
   - **v10: f_back from SAME α as time dilation** — KEY FINDING (re-confirmed §3.60)

3. **5 GitHub commits pushed**
   - c7f6976, cc94e52, ee197ab (build)
   - b41ea66 (--dry-run)
   - f353942, 2cd554c, 39ff56c, 706e219 (Lagrangian v7-v10)

**Key insight:** the closed loop closes for f_back specifically — both γ and f_back use the same α = 1.289 from N=12 SYK. The composite exponent 1/(2α) = c/α = (1/2)/1.289 = 0.388 ties them together.

---

## 10. Things to NOT re-do

- **Don't try to derive α=1.29 from a single calculation.** It's a saddle-point result; structural matches to 1+1/√12 are the right framing.
- **Don't add "free parameters" without justification.** Current count: μ, m_{3+1D} (the only 2 truly free). Everything else is derived or calibrated to a single observation.
- **Don't promise "first-principles derivation" if it's structural.** Be honest about which pieces are derived vs structural matches.
- **Don't break the c=1 Liouville convention.** It's set by the 2D universe having 1 scalar; b=i is forced.
- **Don't reorder the 14 event types by lifetime.** They're 1 species at 14 different γ values (democratic cosmology).

---

## 11. Useful commands

```bash
# Build
bash paper/build_pdf.sh                    # full paper (30-60s)
bash paper/build_pdf.sh --dry-run          # README + layman (5-15s)

# Git
git log --oneline | head -10               # recent commits
git log -- paper/paper.pdf                 # PDF-only commits (finds last good build)
git log --oneline <sha>..HEAD --stat       # changes since commit

# Search
grep -n "f_back\|fback" paper/markdown/02_glossary.md | head -5
grep -rn "α\|\\\\alpha" paper/markdown/03_relations.md | head -5

# Memory
memory_append(scope="agent", content="...")  # NOT memory_append alone
```

---

## 12. Memory cross-references

- Agent memory has the full v3.0.21 build_tools details and Lagrangian v9-v10 findings
- Topic file `cascade-physics.md` has the older v2.x-era physics and v2.7.x history
- This file is the **quick reference** for current state (v3.0.2)

For very old context (v1.x, v2.0-v2.5), see `changelog.md` and the topic file.