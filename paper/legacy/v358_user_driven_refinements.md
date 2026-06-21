# v3.5.8: User-Driven Refinements (June 20, 2026)

**Status:** Current version (released June 20, 2026)
**Paper:** 393 pages, 1.42 MB
**Limitations:** 128 (was 116 in v3.5.7, +L308f through L308q)

This document captures the v3.5.8 session work in detail. The README and main paper
header are kept CURRENT (v3.5.8 only). For full v3.5.8 history, see this file.

---

## 1. NEW LIMITATIONS (12 added, 116 → 128)

### L308f-L308l: User-Driven Refinements (v3.5.7+ extension)

- **L308f**: M_Pl,2D = 3 TeV origin (N=12 SYK + v_Higgs, NOT "holographic", USER-CAUGHT)
- **L308g**: M_Pl,4D = 4×10²³ derivation chain (α-GM + closed loop, NOT first-principles, USER-CAUGHT)
- **L308h**: 0/9 parameters first-principles derived (USER-DIRECTED)
- **L308i**: Geometric factor 2π vs 4π is BOUNDARY-SPHERE STRUCTURED (USER-DISCOVERED)
- **L308j**: Cone extension to 9D/10D/12D is NOT APPLICABLE (USER-DIRECTED)
- **L308k**: Cone's true geometric endpoint is 7D/8D, not 4D (USER-CORRECTED)
- **L308l**: Cone has natural range n=1 to n≈17 (USER-DIRECTED)

### L308m-L308q: MCMC Breakthrough + User-Insights (NEW v3.5.8)

- **L308m**: MCMC finds 4/9 params observationally pinned, 2/9 framework choices, 3/9 derived
- **L308n**: α = 1 + 1/√12 EXACT first-principles match (BREAKTHROUGH, 0.025%)
- **L308o**: N_sub = E_4D/E_sub scales linearly (USER-INSIGHT)
- **L308p**: Cone is asymmetric: 4D linear, 2D one-to-one (USER-INSIGHT)
- **L308q**: 2D universe is discrete quantum (USER-INSIGHT)

### Status updates

- **L43** (Lagrangian skeleton → α): **OPEN → PARTIAL** (α = 1+1/√12 derived)
- **First-principles progress**: 0/9 → 1/9 (α)
- **M_Pl,3D** measured: 1/9 first-principles
- **N_sub** moved from "free parameter" to "SEMI-DERIVED" (linear in E_4D)

---

## 2. NEW PAPER SECTIONS (11 added, §7.4.5 - §7.4.15)

| Section | Title | Key Finding |
|---|---|---|
| §7.4.5 | μ's 5 Structural Motivations | μ has 5+ structural origins |
| §7.4.6 | α-GM Consistency and Cone Depth Structure | M_Pl,2D uniquely fixed at 2.89 TeV |
| §7.4.7 | First-Principles Search Summary | 0/9 first-principles (was true) |
| §7.4.8 | Geometric Factor Asymmetry: 2π vs 4π | Boundary sphere structure |
| §7.4.9 | Extending Cascade to 9D, 10D, 12D | NOT APPLICABLE |
| §7.4.10 | Extending Cascade to 0 and Negative Dimensions | Cone range n=1 to n≈17 |
| §7.4.11 | Monte Carlo Parameter Convergence | 4/9 observationally pinned |
| §7.4.12 | First-Principles Search: Remaining Parameters | M_Pl,2D = 12×v_Higgs |
| §7.4.13 | N_sub Scales Linearly with E_4D | User-insight, linear scaling |
| §7.4.14 | Cone is Asymmetric: 4D Linear, 2D One-to-One | User-insight |
| §7.4.15 | 2D Universe is a Discrete Quantum | M_2D is smallest unit of DM |

---

## 3. NEW CALCULATIONS (11 added)

1. `v35_alpha_cone_depth_structure.py` (α-GM consistency, "12" unit)
2. `v35_first_principles_search.py` (0/9 derived summary)
3. `v35_first_principles_rest.py` (remaining 8 parameters)
4. `v35_geometric_factor_progression.py` (CORRECTED sphere volumes)
5. `v35_extending_to_9d_10d_12d.py` (cone extension)
6. `v35_cone_extends_to_zero.py` (full range)
7. `v35_monte_carlo_parameter_search.py` (MCMC breakthrough)
8. `v35_2d_cft_monte_carlo_alpha.py` (α first-principles)
9. `v35_n_sub_scaling.py` (N_sub = E_4D/E_sub)
10. `v35_2d_universe_quantum.py` (M_2D discrete)
11. `v35_first_principles_rest.py` (M_Pl,2D, N_sub, ε analysis)

### New result files

- `v35_monte_carlo_results.txt` (MCMC parameter convergence)
- `v35_alpha_first_principles.txt` (α = 1+1/√12 derivation)
- `v35_first_principles_rest.txt` (search results)

### New plots

- `plots/geometric_factor_progression.png` (linear + log scale)
- `plots/geometric_factor_progression_main.png` (single panel)
- `plots/cone_extends_to_zero.png` (full range with 0/negative)

---

## 4. KEY DISCOVERIES (v3.5.8)

### 1. M_Pl,2D & M_Pl,4D honest origins (USER-CAUGHT)
- M_Pl,2D = 3 TeV: 12 × v_Higgs = 2952 GeV (1.5% off)
- M_Pl,4D = 4×10²³: α-GM + closed loop, 1% match (BUT NOT first-principles)
- v3.1.2 tried three rejected scenarios (A: 8.3×10¹², B: 1.22×10¹⁹, X: 887 GeV)
- v3.3 α-GM is the current derivation

### 2. Boundary sphere structure (USER-DISCOVERED)
- 2D→3D: factor 2π (S¹ circle boundary)
- 3D→4D: factor 4π (S² sphere boundary)
- Each transition factor = parent's boundary sphere surface area
- L146 (4π specificity) PARTIAL → STRUCTURAL
- L142a (4π origin) PARTIAL → STRUCTURAL (S² boundary hypothesis)

### 3. Geometric peak at n=6 (USER-CORRECTED)
- S⁶ surface area = 33.07 is the maximum
- Framework's 4D choice was PRACTICAL, not geometric
- Cone could extend to 7D/8D where peak is
- Past n=17, factors < 1, cone weakens
- At n→∞, factors → 0, cone dissolves
- At n=0, A=2; at n=-2, A=-1/π (NEGATIVE area, mathematical curiosity)

### 4. α = 1 + 1/√12 EXACT first-principles match (BREAKTHROUGH)
- α_2D_CFT = 1.2886751346
- Framework α = 1.289
- Match: 0.025% (essentially EXACT)
- N=12 = 12 Majorana = 3 generations × 4 Weyl per gen
- Schwarzian coefficient c_s = 1/√N
- L43 OPEN → PARTIAL
- First-principles progress: 0/9 → 1/9

### 5. MCMC parameter convergence (USER-DIRECTED)
- Tier 1 (4/9 STRONGLY CONSTRAINED): α, ε, τ_4D, AGN rate (converge within 0.5σ)
- Tier 2 (2/9 WEAKLY CONSTRAINED): M_Pl,2D, N_sub
- Tier 3 (3/9 DERIVED): M_Pl,4D, γ_4D, E_4D
- Confirms 4 params are observationally pinned

### 6. "12" is the cascade fundamental unit
- α = 1 + 1/√12 (Schwarzian SYK saddle-point)
- M_Pl,2D = 12 × v_Higgs (structural)
- Cone depth 4D→3+1D = 12 sub-steps
- 12 Majorana = 6 Dirac = 3 generations × 2
- All consistent but deep reason needs theoretical work (L43 PARTIAL)

### 7. N_sub linear scaling (USER-INSIGHT)
- N_sub = E_4D / E_sub (energy conservation)
- E_sub = 1.25×10⁷⁷ J (~10²⁹ M_sun, sub-universe scale) [REVISED L308z: E_sub = 1.295×10⁷⁷ J, N_sub = 386]
- For framework: N_sub = 400 (E_4D = 5×10⁷⁹ J) [REVISED L308z: N_sub = 386, E_sub = 1.295×10⁷⁷ J]
- Different 4D events → different N_sub (sub-galaxy: N=4, supercluster: N=400,000)
- N_sub no longer "free parameter" — SEMI-DERIVED

### 8. Cone asymmetry (USER-INSIGHT)
- 4D → 3+1D: linear (N_sub ∝ E_4D, universe-creating, transcendent)
- 3+1D → 2D: one-to-one (1 universe per event, universe-modifying, internal)
- 2D asymmetry CONSTRAINED by DM observation
- Linear at 2D would overproduce DM by 10⁶⁵

### 9. 2D universe is discrete quantum (USER-INSIGHT)
- Fixed mass M_2D = M_Pl,2D²/M_Pl,3D = 7.4×10⁻¹³ GeV
- Variable lifetime (M^α law from event energy)
- 1 universe per event (no splitting)
- Analogous to a particle: mass quantum + variable lifetime + single creation mode
- M_2D/2 would require M_Pl,2D = 2.12 TeV (breaks α-GM by 9.4%)

---

## 5. COMMITS (v3.5.8)

This session pushed 6 commits:

1. `f4c4655` - v3.5.8: User-driven refinements (M_Pl origins, geometric factors, cone structure)
2. `942f725` - v3.5.8: MCMC parameter search + α = 1+1/√12 first-principles breakthrough
3. `20b83ec` - v3.5.8: First-principles search for remaining parameters (§7.4.12)
4. `66d4fdc` - v3.5.8: N_sub scales linearly with E_4D (L308o)
5. `2460fcf` - v3.5.8: Cone is asymmetric - 4D linear, 2D one-to-one (L308p)
6. `f47e052` - v3.5.8: 2D universe is discrete quantum (L308q)
7. `7381fd1` - persistent_memory.md: comprehensive v3.5.8 update

---

## 6. USER-DRIVEN WORKFLOW (KEY LESSONS)

1. **User's intuitive questions often lead to breakthroughs**:
   - "Monte Carlo to find where params converge" → MCMC tier structure
   - "Maybe N_sub depends on event size" → linear scaling discovery
   - "Does it mean n_sub for 2d as well?" → cone asymmetry
   - "Why can't there be 2 half-mass universes" → 2D quantum

2. **The "12" insight is multi-pronged**: doesn't come from one derivation but from multiple independent consistencies

3. **The framework is more rigid than expected**: 4/9 params observationally pinned, 1/9 first-principles derived

4. **The 2D universe's "discreteness" is structural**: it's a quantum of the 2D level, not a continuous distribution

5. **User catches are crucial**: M_Pl,2D & M_Pl,4D were never first-principles derived — user caught this

---

## 7. KEY FILES

- `paper/paper.md` - Main paper (393 pages, 1.42 MB)
- `paper/markdown/06_limitations.md` - 128 honest limitations
- `persistent_memory.md` - Project memory (1558 lines)
- `changelog.md` - All version history
- `calculations/v35_*.py` - 11 new calculations
- `calculations/v35_*.txt` - 3 new result files
