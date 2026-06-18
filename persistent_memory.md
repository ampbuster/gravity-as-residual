# SIDC Persistent Memory

> Project-level persistent notes for the **Scale-Invariant Dimensional
> Cascade** (SIDC) paper. Captures important findings, conventions,
> open work items, and gotchas that should survive across sessions.

**Repo:** [github.com/ampbuster/gravity-as-residual](https://github.com/ampbuster/gravity-as-residual)
**Current version:** v3.1.1-final (paper) — 338 pages, 71 honest limitations
**Last updated:** June 18, 2026

---

## 1. The model in one paragraph (REVISED v3.1.1-final)

SIDC proposes that gravity, dark matter, and dark energy are all
consequences of a single dimensional-projection mechanism:

- A 4D event created our 3+1D universe (the Big Bang)
- The 4D event's gravity **inverts to antigravity** when projected into 3+1D
- This 4D antigravity **cancels** (1 - ε) of 3+1D's own gravity
  - ε = 10⁻³⁸ is the residual = gravity weakness (hierarchy, observed)
  - The un-cancelled fraction = DE = 10⁻¹²³ × M_Pl⁴ (cosmological CC, observed)
- The 4D event is "practically eternal" from 3+1D frame (γ ~ 10⁶², τ_4D ~ 10³⁴ yr)
- 3+1D leaks f_back = t_Pl/τ_4D ~ 10⁻⁸⁵ back to 4D during its lifetime
- DE = f_back × ε × M_Pl⁴ (closed loop, frame-consistent with γ ~ 10⁶²)
- In our universe, every energetic event (SNe, BH mergers, etc.) creates a 2D universe
- 2D universe lives for τ_2D = (E/E_Pl)^1.29 × t_Pl (M^1.29 scaling law, 14 events)
- 2D universe dies, **100% of energy returns to 3+1D as DM** (death return, not f_back)
- DM is cumulative 2D universe deaths (Σ M_2D × N)

**Two distinct cross-dimensional stories:**
- 4D ↔ 3+1D: CLOSED LOOP (f_back = 10⁻⁸⁵, governed by γ)
- 3+1D → 2D: CREATION + DEATH RETURN (M^1.29 lifetime, governed by α)

---

## 2. The proper closed loop (REVISED v3.1.1-final)

The closed loop is **specifically the 3+1D ↔ 4D cycle**:

$$f_{\rm back} = \frac{t_{\rm Pl,3}}{\tau_{\rm 4D}} = \frac{t_{\rm Pl,3}}{T_{\rm 4D,proper} \times \gamma}$$

For γ ~ 10⁶² (within cone picture's range 10⁶⁰-10¹⁰⁰):
- τ_4D = 4.35×10⁴¹ s = 1.4×10³⁴ yr (10²⁴ × universe age, "practically eternal")
- f_back = 5.4×10⁻⁴⁴ / 4.35×10⁴¹ = 1.2×10⁻⁸⁵
- DE = f_back × ε × M_Pl⁴ = 1.2×10⁻⁸⁵ × 10⁻³⁸ × 2.22×10⁷⁶ = 2.7×10⁻⁴⁷ GeV⁴
- Observed: 2.4×10⁻⁴⁷ GeV⁴ (within 14%)

**The closed loop is a CONSISTENCY CHECK** between γ, f_back, ε, and DE.

**What changed in v3.1.1-final:**
- v10 used f_back = (t_Pl/τ_4D) × (τ_SN/τ_universe) × (E_4D/E_SN)^(1/(2α))
  - This required τ_4D = 10²⁸ yr (γ ~ 10⁵⁶, OUTSIDE cone picture range)
  - The extra factors were artifact of v10's wrong 2D-to-3D interpretation
- v3.1.1-final: f_back = t_Pl/τ_4D (single factor)
  - τ_4D corresponds to γ ~ 10⁶² (within cone picture range)
  - Frame-consistent

**f_back = 10⁻⁸⁵ ONLY makes sense as 3D-to-4D leakage** (L141 RESOLVED):
- 2D universe lifetime (33s for SN) is too short for while-alive f_back to matter
- Per SN: f_back_2D = t_Pl/33 = 10⁻⁴⁵, leakage = 0.16 J (negligible)
- 2D-3D story is: 100% death return as DM, not a while-alive f_back

---

## 3. The 2D universe story (M^1.29 scaling law, INDEPENDENT of closed loop)

The M^1.29 scaling law is empirically validated across 14 event types:

$$\tau_{2D} = \left(\frac{E}{E_{\rm Pl}}\right)^{\alpha} \times t_{\rm Pl}, \quad \alpha = 1.289$$

- α = 1.289 = 1 + 1/√12 from N=12 SYK
- N=12 = 12 SM Weyl fermions (dim(SU(3)×SU(2)×U(1)) = 8+3+1 = 12)
- This is a 2D universe LIFETIME formula, independent of the closed loop
- The 2D-3D story is: 2D universe dies, 100% energy returns to 3+1D as DM
- NO while-alive f_back at 2D-3D level (lifetimes too short)

**α's role has NARROWED in v3.1.1-final:**
- BEFORE: α-symmetry unifies forward and backward (α × 1/(2α) = 1/2)
- AFTER: α governs 2D-3D lifetimes; γ (cone picture) governs 3D-4D closed loop
- The "α-symmetry" claim of v10 was artifact of wrong interpretation

**What α is used for NOW:**
- 2D universe lifetime scaling (M^1.29 law, 14 event types) ✓
- N=12 SM connection (structural) ✓
- Lagrangian skeleton decomposition (α = 1 + 1/√12) ✓

**What α is NOT used for NOW:**
- Closed loop formula (uses γ, not α) ✗
- α-symmetry (α × 1/(2α) = 1/2) ✗
- "Three derivations of 1/2" as closed loop evidence ✗

---

## 4. The Lagrangian skeleton (RESCOPED v3.1.1-final)

$$L_{\rm SIDC} = L_{c=1,\rm Liouville} + L_{N=12,\rm SYK} + L_{\rm Schwarzian}$$

**This is now scoped as a CANDIDATE for 2D universe physics, NOT evidence for the closed loop.**

- α = 1.289 = 1 + 1/√12 (N=12 SYK saddle)
- α = 1/2 (Schwarzian) + 1/2 (kinematic) + 1/√12 (N=12 SYK)
- 1/2 in 2D papers: Schwarzian (τ~√E), DOZZ (b²=1/2), Calabrese-Cardy
- 1/√12: 2D × √3 generations (or N=12 finite-N)
- N=12 = 12 SM Weyl fermions (Standard Model "backbone")

**Status (revised):**
- ✓ Structure identified (c=1 + N=12 + Schwarzian)
- ✓ α = 1.289 matches M^1.29 law across 14 events
- ✗ Full Lagrangian (couplings, cross-couplings, regularization, Z derivation)
- ✗ First-principles derivation of 1/√N (structural match only)
- ⚠️ NOT evidence for closed loop (closed loop uses γ, not α)

**Democratic cosmology (§3.17):** all 14 events = SAME operator at different γ.
1 species, 14 γ values.

---

## 5. The build infrastructure (v3.0.21 + v3.1.1)

**Self-contained in repo:**
- `paper/build_pdf.sh` — orchestrator (~1100 lines, documented)
- `paper/build_tools/` — 4 original + 5 new math cleanup scripts
- `paper/.build/` — intermediate files (gitignored)
- `paper/legacy/` — historical content (3289 lines moved)
- `paper/markdown/` — 16+ source files (alphabetical order matters for PDF)

**Build commands:**
```bash
bash paper/build_pdf.sh                    # full build (337-338 pages)
python3 paper/build_tools/cleanup_math.py  # run all math cleanup
python3 paper/build_tools/cleanup_math.py --build  # cleanup + build
```

**Last working build:** 338 pages (June 18, 2026, v3.1.1-final).

**Build state:**
- Paper PDF: `paper/paper.pdf` (1.2 MB, 338 pages)
- paper_combined.md next to paper.pdf
- All build infrastructure self-contained inside the repo

---

## 6. Open work items (v3.1.1-final)

| Limitation | Status | What needs to happen |
|------------|--------|----------------------|
| L41: Why μ is its value | OPEN | Derive 2D cosmological constant from first principles |
| L42: Why m_{3+1D} is its value | OPEN | Derive induced 3+1D Planck mass from bulk geometry |
| L43: Lagrangian skeleton → full L | OPEN, NARROWED | α for 2D-3D lifetimes only, not closed loop |
| L100: F_p(z) Hill function | OPEN | Derive primordial vs cumulative DM ratio |
| L138 (NEW) | f_back = 10⁻⁸⁵ is calibration, not derived | CONFIRMED honest |
| L139 (REVISED) | Closed loop: f_back is 3D-to-4D leakage | PARTIAL, frame-consistent |
| L140 (NEW) | ε = 10⁻³⁸ is observed, not derived | OPEN (hierarchy problem) |
| L141 (NEW) | f_back = 10⁻⁸⁵ ONLY as 3D-to-4D leakage | RESOLVED |
| L121-L127 (5D-9D) | SPECULATIVE, UNCERTAIN | α-power-law extrapolation may not hold |

**Closing L41-L43 requires:** 2D CFT theoretical physicist or brute-force path integral.

**L43 status (REVISED v3.1.1-final):**
- WAS: α derivation relevant to closed loop
- NOW: α derivation relevant only to M^1.29 law (2D universe physics)
- L43 stays OPEN, but scope is narrower

**v3.0.21 update**: §3.62.1 added — SIDC IS structurally Karch-Randall + JT gravity (Deng et al. arXiv:2211.13415). Z_SIDC = Z_JT × Z_Liouville × Z_SYK is in principle tractable.

**v3.0.21 update 2**: §3.62.2 + L93-L97 summarize 5 more attempts (v14-v19).
- v14/v14c/v14d/v14e: scaling law IS the time dilation. STILL VALID.
- v15: μ is NOT structural in c=1 Liouville
- v16: α = 1.289 = 1 (SR) + 1/√12 (N=12 finite-N)
- v17: pure SYK q=4 N=12 gives α ~ 1, not 1.289
- v18: f_back is NOT exp(-S_2D)
- v19: α is CROSS-SECTOR EMERGENT, not from Z

**HONEST VERDICT (v14-v19)**: L41, L42, L43 cannot be closed by more brute force.
They require STRUCTURAL INPUT: 5D matching (L41, L42) or cross-coupling terms
+ correct observable identification (L43). Pure 2D partition function doesn't
give α = 1.289 directly.

---

## 7. The 5D/6D/9D extension (UNCERTAIN v3.1.1-final)

The cascade extension to 5D-9D was based on a power-law extrapolation:
$$M_{\rm Pl,N} = M_{\rm Pl,4} / \alpha^{(N-4)}$$

This was SPECULATIVE (L121-L127) and is now UNCERTAIN in light of the closed loop revision:
- L122: M_Pl,9D = 249 GeV ≈ v_Higgs (within 1.3%) — suggestive but extrapolation
- L123: String scale = v_Higgs (M_string = 246 GeV) — testable but invisible
- L124: Higgs = bridge between SIDC and string theory — structural
- L125: LHC null via f_back² suppression — works
- L126: 12 SYK Majorana = 9 spatial + 3 generational — speculative
- L127: Hierarchy problem solved by cascade — structural, not derived

**v3.1.1-final status**: These SPECULATIVE claims rely on the α-power-law extrapolation.
Since the closed loop no longer uses α, the structural support for these is weaker.
They remain IN THE PAPER as speculative, but with the caveat that they require
further justification beyond "α governs everything."

---

## 8. Key conventions (DO NOT BREAK)

### Naming
- Use **SIDC** (not "the cascade", "DC", "Dimensional Cascade")
- **Majorana** fermions (not "Majorana fermions" with extra space)
- **N=12** with explicit equals sign in math, N = 12 in prose
- **f_back** (lowercase f, with underscore) — never "fback" or "f-back"

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

### f_back variable
- f_back = t_Pl/τ_4D (3D-to-4D leakage) — the only meaningful f_back
- f_back_2D = t_Pl/τ_2D — while-alive gravitational coupling, NEGLIGIBLE
- f_back_death = 1 — 100% energy return at universe death

### Closed loop
- Forward (4D → 3+1D): f_back = 10⁻⁸⁵ (projection efficiency)
- Backward (3+1D → 4D): f_back = 10⁻⁸⁵ (leakage rate)
- DE = f_back × ε × M_Pl⁴
- γ ~ 10⁶² (cone picture time dilation)
- NEVER use the v10 formula with 1/(2α) factor — it's wrong

---

## 9. Important files

**Paper structure:**
- `paper/markdown/00_title.md` — title, v3.0 highlight, honest boundary
- `paper/markdown/01_executive_summary.md` — summary, 17 tests score card
- `paper/markdown/02_glossary.md` — §0 parameter glossary
- `paper/markdown/03a_relations.md` — main physics, includes §3.60, §3.62
- `paper/markdown/03b_predictions.md` — RAR, AGC/KKR, end-of-universe
- `paper/markdown/03c_lagrangian.md` — Lagrangian, §3.60.3 (closed loop), §3.67, §3.68
- `paper/markdown/06_limitations.md` — 71 honest limitations
- `paper/markdown/07_conclusion.md` — 70+ external constraints
- `paper/markdown/10_end_universe.md` — §10 energy-scaling ladder
- `paper/markdown/15_falsifiability_matrix.md` — predictions vs observations

**Supporting:**
- `README.md` — public release (closed-loop intro REMOVED v3.1.1)
- `supporting/layman_summary.md` — 5-step layman version
- `changelog.md` — version history
- `ai_disclosure.md` — AI assistance disclosure
- `calculations/v27_*.py` — 30+ constraint calculations
- `calculations/lagrangian_v[1-9]*.py` — Lagrangian trial-and-error
- `calculations/v31_*.py` — v3.1.1 revisions (closed loop, f_back, F_p)

---

## 10. Recent session summary (June 18, 2026 — v3.1.1-final)

**This session's contributions (REVISIONS to v3.1.1):**

1. **Honest f_back/closed loop revision (L138, L139, L140, L141)**
   - v10's "closed loop" used τ_4D = 1e28 yr (γ ~ 10⁵⁶, OUTSIDE cone range)
   - User reframing: f_back = 10⁻⁸⁵ is 3D-to-4D leakage, NOT 2D-to-3D
   - Proper closed loop: f_back = t_Pl/τ_4D with γ ~ 10⁶² (within cone range)
   - DE matches observation to within 14% (vs v10's 12% via tuning)
   - 2D-3D story: 100% death return as DM, NOT a while-alive f_back
   - 2D lifetimes too short (33s for SN) for while-alive coupling to matter

2. **α's role narrowed (no longer in closed loop)**
   - α still works for 2D universe lifetimes (M^1.29 law, 14 events)
   - α still has N=12 SM connection (structural)
   - α does NOT appear in proper closed loop (uses γ, not α)
   - "α-symmetry" (α × 1/(2α) = 1/2) was artifact of v10's wrong interpretation
   - Lagrangian is structural proposal for 2D universe physics, not closed loop evidence

3. **README "two main points" removed (v3.1.1)**
   - "Closed loop" and "scaling law" as ground truth were overstated
   - Replaced with ⚠️ STATUS NOTE pointing to L138-L141
   - "The closed loop" → "The geometric picture" (with caveats)

4. **Files updated:**
   - paper/markdown/03c_lagrangian.md — §3.60.3 rewritten honestly
   - paper/markdown/06_limitations.md — L138, L139, L140, L141 added
   - README.md — status note + softening of "closed loop" claims
   - calculations/v31_F_p_consistency.py, v31_proper_closed_loop.py, v31_f_back_only_3d_to_4d.py
   - paper/paper.pdf — rebuilt 338 pages

5. **Key user insights this session:**
   - f_back only makes sense as 3D-to-4D (2D lifetimes too short)
   - 4D event is "practically eternal" not strictly eternal
   - ε = 10⁻³⁸ is observed (hierarchy problem), not derived
   - 10⁻⁸⁵ is the DE/Planck ratio divided by ε (calibration, not derivation)
   - The Lagrangian is a structural proposal, not closed loop evidence

6. **GitHub commits:**
   - 7020b75: L138/L139/L140 honest limitations
   - 9a44b34: Remove "two main points" from README
   - f2092b1: Proper closed loop (user reframing)
   - e202211: f_back only as 3D-to-4D leakage (L141)

---

## 11. Things to NOT re-do

- **Don't claim f_back = 10⁻⁸⁵ is a derived physical fraction.** It's a calibration (= ρ_DE / (ε × M_Pl⁴)). See L138.
- **Don't claim the closed loop closes numerically.** The v10 formula was tuned (τ_4D = 1e28 yr, outside cone range). The proper closed loop is a consistency check, not a derivation. See L139.
- **Don't claim ε is derived.** It's observed (hierarchy problem). SIDC provides a geometric story but not a derivation. See L140.
- **Don't claim f_back = 10⁻⁸⁵ is universal across levels.** It's only 3D-to-4D. The 2D-3D story uses 100% death return, not f_back. See L141.
- **Don't try to derive α=1.29 from a single calculation.** It's a saddle-point result; structural matches to 1+1/√12 are the right framing.
- **Don't add "free parameters" without justification.** Current count: μ, m_{3+1D} (the only 2 truly free). Everything else is derived or calibrated to a single observation.
- **Don't promise "first-principles derivation" if it's structural.** Be honest about which pieces are derived vs structural matches.
- **Don't break the c=1 Liouville convention.** It's set by the 2D universe having 1 scalar; b=i is forced.
- **Don't reorder the 14 event types by lifetime.** They're 1 species at 14 different γ values (democratic cosmology).
- **Don't reintroduce the 5D/6D/9D extrapolation as derived.** It's SPECULATIVE, even with the 9D = string theory match. The α-power-law is one of several possibilities.

---

## 12. Useful commands

```bash
# Build
bash paper/build_pdf.sh                    # full paper (30-60s)
bash paper/build_pdf.sh --dry-run          # README + layman (5-15s)

# Math cleanup
python3 paper/build_tools/cleanup_math.py file.md  # single file
python3 paper/build_tools/cleanup_math.py          # all files
python3 paper/build_tools/cleanup_math.py --build  # cleanup + build

# v3.1.1 calculations
python3 calculations/v31_F_p_consistency.py        # F_p = 0 check
python3 calculations/v31_proper_closed_loop.py     # proper closed loop
python3 calculations/v31_f_back_only_3d_to_4d.py   # 3D-4D leakage

# Git
git log --oneline | head -10
git log -- paper/paper.pdf                 # find last good build

# Search
grep -n "f_back\|fback" paper/markdown/02_glossary.md | head -5
grep -rn "closed loop" paper/markdown/03c_lagrangian.md | head -5
```

---

## 13. Memory cross-references

- Agent memory has full v3.0.21 build_tools details and Lagrangian v9-v10 findings
- Topic file `cascade-physics.md` has older v2.x-era physics and v2.7.x history
- This file is the **quick reference** for current state (v3.1.1-final)

For very old context (v1.x, v2.0-v2.5), see `changelog.md` and the topic file.

---

## 14. v3.1.1-final at a glance

**Key claims that are STILL VALID:**
- M^1.29 scaling law across 14 event types
- 4D antigravity cancellation mechanism (geometric picture)
- Lagrangian skeleton as structural proposal for 2D universe physics
- L41, L42 (μ, m_{3+1D} identification)
- N=12 SM connection
- 2D universe → DM death return (cumulative 2D deaths)

**Key claims that are REVISED:**
- f_back = 10⁻⁸⁵ ONLY makes sense as 3D-to-4D leakage
- Closed loop is a CONSISTENCY CHECK (γ ~ 10⁶²), not a derivation
- α's role narrowed: 2D-3D lifetime only, not closed loop
- "α-symmetry" was artifact of v10's wrong interpretation
- 5D/6D/9D extension is UNCERTAIN (relies on α power-law)

**Key claims that are REJECTED:**
- v10's closed loop formula (required unjustified τ_4D = 1e28 yr)
- f_back as 2D-to-3D back-projection (lifetimes too short)
- "α-symmetry bridges forward and backward" (no longer applicable)
- "Three derivations of 1/2 close the loop" (now just structural interpretations)

**Honest framing:**
- SIDC is a geometric framework with empirical constraints
- It provides a CONSISTENT PICTURE, not derivations
- The closed loop is a CONSISTENCY CHECK, not a derivation
- The Lagrangian is a STRUCTURAL PROPOSAL, not a complete theory
- ε, f_back, and DE values are OBSERVED, not derived
- The hierarchy and cosmological constant problems are NOT solved by SIDC
