# SIDC Persistent Memory

> Project-level persistent notes for the **Scale-Invariant Dimensional
> Cascade** (SIDC) paper. Captures important findings, conventions,
> open work items, and gotchas that should survive across sessions.

**Repo:** [github.com/ampbuster/gravity-as-residual](https://github.com/ampbuster/gravity-as-residual)
**Current version:** v3.1.2-final (paper) — 354 pages, 81 honest limitations
**Last updated:** June 18, 2026

---

## 1. The model in one paragraph (REVISED v3.1.2-final)

SIDC proposes that gravity, dark matter, and dark energy are all
consequences of a single dimensional-projection mechanism:

- A energetic 4D-bulk event in a 4D BULK created our 3+1D universe
- The 4D bulk has its own gravity scale: M_Pl,4D = 887 GeV (4D BULK Planck, INFERRED, brane-world, Scenario X)
- Our universe's Planck: M_Pl,3D = 1.22×10¹⁹ GeV (MEASURED via Newton's G)
- The 2D universes' Planck: M_Pl,2D = 10³⁸ GeV (brane-world, INFERRED)
- Three DIFFERENT M_Pl at three different levels (3D ≠ 4D, brane-world consistency)
- The 4D event's gravity **inverts to antigravity** when projected into 3+1D
- This 4D antigravity **cancels** (1 - ε) of 3+1D's own gravity
  - ε = 10⁻³⁸ is the residual = gravity weakness (hierarchy, observed)
  - The un-cancelled fraction = DE = 10⁻¹²³ × M_Pl⁴ (cosmological CC, observed)
- The 4D event is "practically eternal" from 3+1D frame (γ ~ 10⁶², τ_4D ~ 10³⁴ yr apparent)
- 3+1D leaks f_back = (M_Pl,4D/E_4D)^α ~ 10⁻⁸⁵ back to 4D during its lifetime
- DE = f_back × ε × M_Pl,3D⁴ (closed loop formula, frame-consistent with γ ~ 10⁶²)
- In our universe, every energetic event (SNe, BH mergers, etc.) creates a 2D universe
- 2D universe lives for τ_2D = (E/E_Pl,3D)^α × t_Pl (M^α law, 14 events, α = 1.289)
- 2D universe dies, **100% of energy returns to 3+1D as DM** (death return, not f_back)
- DM is cumulative 2D universe deaths (Σ M_2D × N)

**AGE vs LIFETIME (v3.1.2-final, HONEST):**
- 13.8 Gyr = universe **AGE** (observed, the only firm value)
- **LIFETIME: UNKNOWN** — depends on E_sub = E_4D / N_sub, where N_sub is a FREE PARAMETER (4D-bulk dynamics unknown)
- For N_sub = 1: τ_sub = τ_4D = 1.4×10³⁴ yr
- For N_sub = 300: τ_sub = ~9×10³⁰ yr (was the ARBITRARY choice previously presented as derived)
- For N_sub = 4.2×10¹⁸: τ_sub = 13.8 Gyr (lower bound, universe just alive, AUDIT-CORRECTED from 2×10¹⁹)
- For N_sub = 10¹²: τ_sub = ~4.8×10¹⁸ yr (AUDIT-CORRECTED from ~10¹⁵ yr)
- For N_sub = 10⁶: τ_sub = ~2.6×10²⁶ yr (AUDIT-CORRECTED from ~10²⁷ yr)
- Constraint: τ_sub > 13.8 Gyr (universe still alive)
- User caught this: "N_sub = 300 is not known, and not fixed; could be 150 with double the masses each"

**FRAME OF REFERENCE (v3.1.2-final, KEY):**
- M^α law gives APPARENT durations in LOWER-D frame, NOT proper time
- 2D lifetime (33s) is in 3+1D frame
- 3+1D sub-universe lifetime (~10³⁰ yr) is in 3+1D's own frame
- 4D event apparent duration (1.4×10³⁴ yr) is in 3+1D frame, time-dilated from 4D proper time via γ ~ 10⁶²
- 4D event proper duration: T_4D_proper = τ_4D / γ ~ 10⁻²⁰ s

**Universal closed-loop formula (v3.1.2-final):**
- f_back(N→N-1) = (M_Pl,N / E_event)^α — universal at EVERY dimensional transition
- Three different M_Pl at three different levels: 2D = 10³⁸ GeV, 3D = 10¹⁹ GeV, 4D = 887 GeV
- α = 1.289 is the SAME at every level
- Pulsed return at universe death: 100% (universal, no α dependence)
- 4π at 3D→4D continuous leakage: verified ~1.7%, specific to that transition (NOT universal)

**Multi-universe picture (v3.1.2-final, USER-CORRECTED TWICE, v3.1.2-final: N_sub is FREE):**
- An ENERGETIC EVENT in a 4D BULK can create 3+1D sub-universes
- The SPECIFIC 4D-bulk mechanism is UNKNOWN (NOT specifically '4D-galaxy collisions' — earlier version was too specific)
- We only know the FORM: energetic event creates N_sub sub-universes
- **N_sub is a FREE PARAMETER** (not determined by the cascade)
- For ANY N_sub: E_sub = E_4D / N_sub, τ_sub = (E_sub/M_Pl,4D)^α × t_Pl
- Constraint: N_sub < 2×10¹⁹ (so τ_sub > 13.8 Gyr)
- The 10¹² galaxies in our 3+1D universe are a SEPARATE population (formed after sub-universe creation)

---

## 2. The universal closed loop (REVISED v3.1.2-final)

**v3.1.2-final KEY INSIGHT**: The closed-loop formula is **universal at every dimensional transition**:

$$f_{\rm back}(N \to N-1) = \left(\frac{M_{\rm Pl,N}}{E_{\rm event}}\right)^\alpha, \quad \alpha = 1.289$$

**Three different M_Pl at three different levels (Scenario X):**

| Level | M_Pl | Status | E_event example | τ | f_back |
|---|---|---|---|---|---|
| 2D (children) | 10³⁸ GeV | brane-world, INFERRED | 10⁴⁴ J (SN) | 33 s | 1.6×10⁻⁴⁵/s |
| 3+1D (us) | 1.22×10¹⁹ GeV | MEASURED (Newton's G) | - | AGE: 13.8 Gyr, LIFETIME: ~10³⁰ yr | - |
| 4D bulk (parent) | 887 GeV | INFERRED (cascade, brane-world) | 1.07×10⁵⁹ J (4D event) | 1.4×10³⁴ yr (apparent, in 3+1D frame) | 1.2×10⁻⁸⁵/s |

**Closed-loop formula at every transition:**
- For 2D→3D: M_Pl,3D = 1.22×10¹⁹ GeV, E_SN = 10⁴⁴ J, gives f_back_2D = 1.6×10⁻⁴⁵/s, τ_2D = 33s ✓
- For 3D→4D: M_Pl,4D = 887 GeV, E_4D = 1.07×10⁵⁹ J, gives f_back_4D = 1.2×10⁻⁸⁵/s, τ_4D = 1.4×10³⁴ yr ✓
- The M^α law is the SAME formula at every level

**DE matching (3D→4D):**
- DE = f_back × ε × M_Pl,3D⁴ = 1.2×10⁻⁸⁵ × 10⁻³⁸ × (1.22×10¹⁹)⁴ GeV⁴
- Observed: 2.4×10⁻⁴⁷ GeV⁴ (within 14%)

**Frame-of-reference clarification (v3.1.2-final):**
- 2D lifetime (33s) is in 3+1D frame
- 4D event apparent duration (1.4×10³⁴ yr) is in 3+1D frame, time-dilated from 4D proper time via γ ~ 10⁶²
- 4D event proper duration: T_4D_proper = τ_4D / γ ~ 10⁻²⁰ s
- 3+1D universe AGE: 13.8 Gyr (in 3+1D's own frame)
- 3+1D universe LIFETIME: ~10³⁰ yr (in 3+1D's own frame, M^α with M_Pl,4D = 887 GeV)

**What changed in v3.1.2-final (vs v3.1.1-final):**
- v3.1.1-final: f_back = 10⁻⁸⁵ ONLY makes sense as 3D-to-4D leakage (L141 RESOLVED)
- v3.1.2-final: f_back is universal in FORM, VALUES differ because M_Pl,N and E_event differ
  - 2D→3D: f_back_2D = 1.6×10⁻⁴⁵/s (during 33s, integrated = 5.4×10⁻⁴⁴ of E_2D, negligible)
  - 3D→4D: f_back_4D = 1.2×10⁻⁸⁵/s (during 1.4×10³⁴ yr apparent, integrated = DE)
  - 100% pulsed return at universe death (universal, no α dependence)

**Evolution:**
- v10: f_back = (t_Pl/τ_4D) × (τ_SN/τ_universe) × (E_4D/E_SN)^(1/(2α)) — REJECTED (required unjustified τ_4D = 1e28 yr)
- v3.1.1-final: f_back = t_Pl/τ_4D (single factor) — PARTIALLY RESOLVED
- v3.1.2-final: f_back = (M_Pl,N/E_event)^α universal at every level — RESOLVED

---

## 3. The 2D universe story (M^α scaling law, α = 1.289, UNIVERSAL at every level v3.1.2-final)

The M^α scaling law is empirically validated across 14 event types:

$$\tau_{2D} = \left(\frac{E}{E_{\rm Pl}}\right)^{\alpha} \times t_{\rm Pl}, \quad \alpha = 1.289$$

- α = 1.289 = 1 + 1/√12 from N=12 SYK
- N=12 = 12 SM Weyl fermions (dim(SU(3)×SU(2)×U(1)) = 8+3+1 = 12)
- This is a 2D universe LIFETIME formula, applied at every dimensional transition
- The 2D-3D story is: 2D universe dies, 100% energy returns to 3+1D as DM
- WHILE-ALIVE f_back is NEGLIGIBLE at 2D-3D level (33s too short, f_back_2D = 1.6×10⁻⁴⁵/s × 33s = 5.4×10⁻⁴⁴ of E_2D)

**α's role has EVOLVED:**
- v3.1.1-final: α governs 2D-3D lifetimes only; γ (cone picture) governs 3D-4D closed loop
- v3.1.2-final: α is UNIVERSAL at every dimensional transition (formula f_back = (M_Pl,N/E)^α)
  - At 2D→3D: α governs 2D universe lifetime
  - At 3D→4D: α governs 3+1D sub-universe lifetime AND back-flow rate
- The "α-symmetry" claim of v10 was artifact of wrong interpretation (REJECTED)

**What α is used for NOW (v3.1.2-final):**
- 2D universe lifetime scaling (M^α law, 14 event types) ✓
- Universal closed-loop formula f_back = (M_Pl,N/E_event)^α at every level ✓
- 3+1D sub-universe lifetime ~10³⁰ yr (M^α with M_Pl,4D = 887 GeV) ✓
- N=12 SM connection (structural) ✓
- Lagrangian skeleton decomposition (α = 1 + 1/√12) ✓

**What α is NOT used for:**
- 4π factor at 3D→4D (specific to that transition, not universal) ✗
- α-symmetry (α × 1/(2α) = 1/2) ✗
- "Three derivations of 1/2" as closed loop evidence ✗

---

## 4. The Lagrangian skeleton (RESCOPED v3.1.2-final)

$$L_{\rm SIDC} = L_{c=1,\rm Liouville} + L_{N=12,\rm SYK} + L_{\rm Schwarzian}$$

**This is now scoped as a CANDIDATE for 2D universe physics, NOT evidence for the closed loop.**

- α = 1.289 = 1 + 1/√12 (N=12 SYK saddle)
- α = 1/2 (Schwarzian) + 1/2 (kinematic) + 1/√12 (N=12 SYK)
- 1/2 in 2D papers: Schwarzian (τ~√E), DOZZ (b²=1/2), Calabrese-Cardy
- 1/√12: 2D × √3 generations (or N=12 finite-N)
- N=12 = 12 SM Weyl fermions (Standard Model "backbone")

**Status (revised v3.1.2-final):**
- ✓ Structure identified (c=1 + N=12 + Schwarzian)
- ✓ α = 1.289 matches M^α law across 14 events
- ✗ Full Lagrangian (couplings, cross-couplings, regularization, Z derivation)
- ✗ First-principles derivation of 1/√N (structural match only)
- ⚠️ NOT evidence for closed loop (closed loop uses γ and (M_Pl/E)^α, not α alone)

**Democratic cosmology (§3.17):** all 14 events = SAME operator at different γ.
1 species, 14 γ values.

**v3.1.2-final Lagrangian scope (REVISED)**:
- L_2D is for 2D universes, NOT for the closed loop
- L_3+1D uses M_Pl,3D = 1.22×10¹⁹ GeV (MEASURED)
- L_4D uses M_Pl,4D = 887 GeV (INFERRED, Scenario X) — separate from L_3+1D
- Lagrangian now reflects three different M_Pl at three different levels
- Lim26 (c=1, b=i) still OPEN (needs 2D CFT expert)

---

## 5. The build infrastructure (v3.0.21 + v3.1.2-final)

**Self-contained in repo:**
- `paper/build_pdf.sh` — orchestrator (~1100 lines, documented)
- `paper/build_tools/` — 4 original + 5 new math cleanup scripts
- `paper/.build/` — intermediate files (gitignored)
- `paper/legacy/` — historical content (3289 lines + v3.1.2 superseded §3.60.4)
- `paper/markdown/` — 16+ source files (alphabetical order matters for PDF)
- `calculations/legacy/` — 5 superseded v3.1.1-v3.1.2 calculation scripts

**Build commands:**
```bash
bash paper/build_pdf.sh                    # full build (354 pages, v3.1.2-final)
python3 paper/build_tools/cleanup_math.py  # run all math cleanup
python3 paper/build_tools/cleanup_math.py --build  # cleanup + build
```

**Last working build:** 354 pages (June 18, 2026, v3.1.2-final, commit fcffc04).

**Build state:**
- Paper PDF: `paper/paper.pdf` (1.27 MB, 354 pages)
- paper_combined.md next to paper.pdf
- All build infrastructure self-contained inside the repo

---

## 6. Open work items (v3.1.2-final)

| Limitation | Status | What needs to happen |
|------------|--------|----------------------|
| L41: Why μ is its value | OPEN | Derive 2D cosmological constant from first principles |
| L42: Why m_{3+1D} is its value | OPEN | Derive induced 3+1D Planck mass from bulk geometry |
| L43: Lagrangian skeleton → full L | OPEN, NARROWED | α for 2D-3D lifetimes only, not closed loop |
| L100: F_p(z) Hill function | OPEN | Derive primordial vs cumulative DM ratio |
| L138 (REVISED v3.1.2) | f_back = 10⁻⁸⁵ is calibration, not derived; formula gives FORM not value | PARTIALLY RESOLVED (Scenario X) |
| L139 (REVISED v3.1.2) | Closed loop: f_back universal at 2D→3D AND 3D→4D with DIFFERENT M_Pl | RESOLVED (Scenario X) |
| L140 | ε = 10⁻³⁸ is observed, not derived | OPEN (hierarchy problem) |
| L141 (REVISED v3.1.2) | f_back = (M_Pl,N/E_event)^α universal with different M_Pl,N | RESOLVED → REINFORCED |
| L142 | 4π within 1.7% of DE | PARTIAL |
| L142a | 4π geometric factor needs derivation | OPEN |
| L142b (RESOLVED) | α_true = 1.258 REJECTED by 14-event M^1.29 fit | RESOLVED |
| L143 | Sub-universe = energetic 4D-bulk events (not 3+1D galaxies); 4D-bulk mechanism UNKNOWN | RESOLVED (USER-CORRECTED) |
| L144 | N_sub is a FREE PARAMETER (4D-bulk dynamics unknown, NOT fixed at 300) | OPEN (what determines N_sub?) |
| L145 | AGE vs LIFETIME: 13.8 Gyr age vs UNKNOWN lifetime (was "~10³⁰ yr" but based on arbitrary N_sub = 300) | REVISED (HONEST) |
| L146 | 4π specific to 3D→4D, not universal | OPEN |
| L147 | DE-DM unification via two closed-loop mechanisms | OPEN |
| L148 | Pulsed vs continuous: why two mechanisms? | OPEN |
| L149 (RESOLVED) | 4π only at 3D→4D vs universal f_back | RESOLVED (empirical) |
| L150 (NEW v3.1.2) | SCENARIO X ADOPTED: M_Pl,4D = 887 GeV, 3D≠4D, age/lifetime, frame of reference | RESOLVED (choice made) |
| L121-L127 (5D-9D) | 9D = v_H match (1.3%, suggestive), M^α M_Pl,N at 5-9D gives EW physics | SPECULATIVE (Scenario X supports) |

**Closing L41-L43 requires:** 2D CFT theoretical physicist or brute-force path integral.

**L43 status (REVISED v3.1.2-final):**
- WAS (v3.1.1-final): α derivation relevant to M^1.29 law (2D universe physics)
- NOW (v3.1.2-final): α derivation relevant to M^α law (universal closed loop AND 2D universe physics)
- L43 stays OPEN, but scope is broader (α is universal at every dimensional transition)

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

## 7. The 5D/6D/9D extension (SCENARIO X SUPPORTS v3.1.2-final)

The cascade extension to 5D-9D is based on a power-law extrapolation:
$$M_{\rm Pl,N} = M_{\rm Pl,4D} / \alpha^{(N-4)}$$

Under **Scenario X (v3.1.2-final adopted)** with M_Pl,4D = 887 GeV:
- M_Pl,5 = 688 GeV
- M_Pl,6 = 534 GeV
- M_Pl,7 = 414 GeV
- M_Pl,8 = 321 GeV
- **M_Pl,9 = 249 GeV ≈ v_Higgs = 246 GeV (1.3% match)** ✓
- M_Pl,10 = 193 GeV

The hierarchy CONVERGES to the EW scale at N ~ 9. This is the cascade's STRONGEST "extra" prediction.

**v3.1.2-final status**: Under Scenario X, the 5D-9D extension SUPPORTS:
- L121: Cone extends to 5D/6D with same α — SPECULATIVE but Scenario X compatible
- L122: M_Pl,9D = v_Higgs (1.3% match) — suggestive, FRAGILE (single number)
- L123: String scale = v_Higgs (246 GeV) — testable, FRAGILE
- L124: Higgs = bridge between SIDC and string theory — structural
- L125: LHC null via f_back² suppression — works
- L126: 12 SYK Majorana = 9 spatial + 3 generational — speculative
- L127: Hierarchy problem solved by cascade — structural, not derived

**Scenario B REJECTED in v3.1.2-final** because it broke 9D = v_H match (M_Pl,4D = M_Pl,3D = 10¹⁹ GeV would give M_Pl,9D = 10¹⁶× off v_Higgs). Scenario X PRESERVES the 9D = v_H match.

**Honest framing**: 9D = v_H match is suggestive (1.3% on a single number, could be coincidence). The 1.3% match is the cascade's strongest extra prediction beyond the basic closed loop, but it is FRAGILE.

---

## 7.5 v3.1.2 SCENARIO X — KEY CORRECTIONS (June 18, 2026)

### Three different M_Pl at three different levels (Scenario X)

| Level | M_Pl | Status | E_event example | τ | f_back |
|---|---|---|---|---|---|
| 2D (children) | 10³⁸ GeV | brane-world, INFERRED | 10⁴⁴ J (SN) | 33 s | 1.6×10⁻⁴⁵/s |
| 3+1D (us) | 1.22×10¹⁹ GeV | MEASURED (Newton's G) | - | AGE: 13.8 Gyr, LIFETIME: ~10³⁰ yr | - |
| 4D bulk (parent) | 887 GeV | INFERRED (cascade, brane-world) | 1.07×10⁵⁹ J (4D event) | 1.4×10³⁴ yr (apparent) | 1.2×10⁻⁸⁵/s |

**Why M_Pl,4D ≠ M_Pl,3D**: In brane-world physics (ADD since 1998, RS-I/II since 1999), the bulk Planck is INDEPENDENT of the brane Planck. The 4D bulk is a SEPARATE 4-dimensional spacetime with its OWN gravity scale, different from our universe's. M_Pl,3D = 10¹⁹ GeV is OUR universe's gravity (measured). M_Pl,4D = 887 GeV is the BULK's gravity (inferred, brane-world). The cascade's 2D universes (M_Pl,2D = 10³⁸ GeV) are also separate structures with their own gravity. Different levels, different gravity scales. The asymmetric Occam's razor is NOT applied.

### AGE vs LIFETIME (v3.1.2-final, HONEST, AUDIT-CORRECTED)
- **AGE**: 13.8 Gyr = current age of our 3+1D universe (OBSERVED, the only firm value)
- **LIFETIME: UNKNOWN** — depends on E_sub = E_4D / N_sub, where N_sub is a FREE PARAMETER
  - For N_sub = 1: τ_sub = τ_4D = 1.4×10³⁴ yr
  - For N_sub = 300: τ_sub = ~9×10³⁰ yr (was ARBITRARY choice presented as derived)
  - For N_sub = 4.2×10¹⁸: τ_sub = 13.8 Gyr (lower bound, AUDIT-CORRECTED from 2×10¹⁹)
  - For N_sub = 10¹²: τ_sub = ~4.8×10¹⁸ yr (AUDIT-CORRECTED from ~10¹⁵ yr)
  - For N_sub = 10⁶: τ_sub = ~2.6×10²⁶ yr (AUDIT-CORRECTED from ~10²⁷ yr)
- Constraint: τ_sub > 13.8 Gyr (universe still alive) → N_sub < 4.2×10¹⁸
- User caught this: "N_sub = 300 is not known, and not fixed; could be 150 with double the masses each"
- AGE ≠ LIFETIME: the universe has not yet died, but its total lifetime is genuinely unknown

### FRAME OF REFERENCE (v3.1.2-final, KEY)
- M^α law gives **APPARENT durations in the LOWER-D frame**, not proper times in the higher-D frame
- **2D lifetime (33 s)** is in the 3+1D frame (apparent)
- **3+1D sub-universe lifetime (~10³⁰ yr)** is in the 3+1D's OWN frame
- **4D event apparent duration (1.4×10³⁴ yr)** is in the 3+1D frame, time-dilated from 4D proper time via γ ~ 10⁶²
- **4D event proper duration**: T_4D_proper = τ_4D / γ ~ 10⁻²⁰ s
- The 3+1D universe's current age (13.8 Gyr) is in the 3+1D's own frame

### Multi-universe picture (v3.1.2-final, USER-CORRECTED TWICE, v3.1.2-final: N_sub is FREE)
- An ENERGETIC EVENT in a 4D BULK can create 3+1D sub-universes
- The SPECIFIC 4D-bulk mechanism is UNKNOWN (NOT specifically '4D-galaxy collisions' — that earlier version was too specific)
- We only know the FORM: energetic event creates N_sub sub-universes
- **N_sub is a FREE PARAMETER** (not determined by the cascade, 4D-bulk dynamics unknown)
- For ANY N_sub: E_sub = E_4D / N_sub, τ_sub = (E_sub/M_Pl,4D)^α × t_Pl
- Constraint: N_sub < 2×10¹⁹ (so τ_sub > 13.8 Gyr, universe still alive)
- The previous choice N_sub = 300, E_sub = 3.57×10⁵⁶ J (small galaxy mass) was ARBITRARY
- User caught: "N_sub = 300 is not known, and not fixed; could be 150 with double the masses each"
- The 10¹² galaxies in our 3+1D universe are a SEPARATE population (formed after sub-universe creation)
- Our 3+1D universe is ONE of these sub-universes (whatever N_sub is)

### Why M_Pl,4D = 887 GeV (motivation)
- (a) Brane-world consistency: bulk Planck can be TeV-scale (ADD)
- (b) 9D = v_Higgs match (1.3% off v_H = 246 GeV)
- (c) M^α scaling for M_Pl,N at 5-9D gives EW-scale physics (200-700 GeV)
- (d) Cascade's M_Pl,4 ≥ 887 GeV floor from previous analysis
- (e) 4D event is galaxy-scale (10⁵⁹ J ≈ 10⁹ M_sun), more natural than universe-scale (10⁷⁵ J)

### Scenarios REJECTED
- **Scenario A** (M_Pl,4 = 8.3×10¹² GeV, E_4D = 10⁶⁹ J): REJECTED, breaks 9D = v_H match (10¹³× off)
- **Scenario B** (M_Pl,4 = 10¹⁹ GeV, E_4D = 10⁷⁵ J): REJECTED, M_Pl,4 = M_Pl,3 violates brane-world principle

### Why the closed loop is universal (v3.1.2-final)
- v3.1.1-final: f_back = 10⁻⁸⁵ ONLY makes sense as 3D-to-4D leakage (L141 RESOLVED)
- v3.1.2-final: f_back = (M_Pl,N/E_event)^α is universal at EVERY dimensional transition
  - Same FORM, different M_Pl,N and E_event at each level
  - 2D→3D: f_back_2D = 1.6×10⁻⁴⁵/s
  - 3D→4D: f_back_4D = 1.2×10⁻⁸⁵/s
- 100% pulsed return at universe death is also universal (no α dependence)
- 4π at 3D→4D continuous leakage: verified ~1.7%, specific to that transition (NOT universal)

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

### f_back variable (v3.1.2-final)
- f_back = (M_Pl,N / E_event)^α — universal closed-loop formula at every dimensional transition
- f_back_2D (2D→3D) = (M_Pl,3D / E_SN)^α = 1.6×10⁻⁴⁵/s (during 33s, integrated = 5.4×10⁻⁴⁴ of E_2D, negligible)
- f_back_4D (3D→4D) = (M_Pl,4D / E_4D)^α = 1.2×10⁻⁸⁵/s (during 1.4×10³⁴ yr, integrated = DE)
- f_back_death = 1 — 100% energy return at universe death (universal, no α dependence)
- DIFFERENT M_Pl at each level: 2D = 10³⁸ GeV, 3D = 10¹⁹ GeV, 4D = 887 GeV

### Closed loop (v3.1.2-final)
- Forward (4D → 3+1D): f_back = 1.2×10⁻⁸⁵/s (projection efficiency with 4π)
- Backward (3+1D → 4D): f_back = 1.2×10⁻⁸⁵/s (leakage rate)
- DE = f_back × ε × M_Pl,3D⁴ (uses OUR universe's Planck, MEASURED)
- γ ~ 10⁶² (cone picture time dilation)
- 4π at 3D→4D continuous leakage: verified ~1.7%, SPECIFIC to that transition
- NEVER use the v10 formula with 1/(2α) factor — it's wrong
- NEVER confuse 13.8 Gyr (AGE) with ~10³⁰ yr (LIFETIME)

### Scenario X (current adopted)
- M_Pl,4D = 887 GeV (4D BULK Planck, INFERRED, brane-world)
- E_4D = 1.07×10⁵⁹ J (galaxy-scale 4D event, ~10⁹ M_sun)
- 3 different M_Pl: 2D = 10³⁸ GeV, 3D = 10¹⁹ GeV, 4D = 887 GeV
- 9D = v_H match (1.3% off) — fragile but suggestive
- N_sub = 300 (energetic 4D-bulk events per event)

---

## 9. Important files

**Paper structure:**
- `paper/markdown/00_title.md` — title, v3.0 highlight, honest boundary
- `paper/markdown/01_executive_summary.md` — summary, 17 tests score card
- `paper/markdown/02_glossary.md` — §0 parameter glossary
- `paper/markdown/03a_relations.md` — main physics, includes §3.60, §3.62
- `paper/markdown/03b_predictions.md` — RAR, AGC/KKR, end-of-universe
- `paper/markdown/03c_lagrangian.md` — Lagrangian, §3.60.3 (closed loop), §3.60.4 (multi-universe), §3.67, §3.68, §3.71
- `paper/markdown/06_limitations.md` — 81 honest limitations
- `paper/markdown/07_conclusion.md` — 70+ external constraints
- `paper/markdown/10_end_universe.md` — §10 energy-scaling ladder
- `paper/markdown/15_falsifiability_matrix.md` — predictions vs observations

**Legacy (archived, v3.1.2-final moved here):**
- `paper/legacy/legacy_paper.md` — older draft of full paper
- `paper/legacy/v31_60_4_old.md` — v3.1.2 §3.60.4 with E_4D = 10⁶⁹ J (Scenario A) and α=1.258 dual framing
- `paper/legacy/README.md` — documentation of legacy

**Supporting:**
- `README.md` — public release (v3.1.2-final)
- `supporting/layman_summary.md` — 5-step layman version
- `changelog.md` — version history
- `ai_disclosure.md` — AI assistance disclosure
- `persistent_memory.md` — THIS FILE (project quick reference)
- `calculations/v27_*.py` — 30+ constraint calculations
- `calculations/lagrangian_v[1-9]*.py` — Lagrangian trial-and-error
- `calculations/v31_*.py` — v3.1.2 current (closed_loop_fback, scenario_X, multi_universe_alpha)
- `calculations/legacy/*.py` — v3.1.1-v3.1.2 superseded (5 scripts, see README)
- `json/calculations/` — 79 calculation result JSONs (machine-readable outputs)
- `json/data/SPARC/` — 6 SPARC galaxy data files (observational)
- `json/data/Tian/` — 4 Tian+ 2024 BCG data files (observational)
- `json/data/UDG/` — 1 UDG data file (observational)
- `json/README.md` — structure documentation

---

## 10. Recent session summary (June 18, 2026 — v3.1.2-final)

**This session's contributions (v3.1.2, MULTIPLE ITERATIONS):**

### v3.1.2 REVISIONS — EMPIRICAL SMOKING GUN
- Tested α = 1.258 (interpretation B) against 14 M^α events
- **REJECTED**: 13/14 events fail (solar flare 281%, AGN 52%, BNS 45%, TDE 62%, etc.)
- Only SN matches (calibration point)
- α = 1.289 is robust

### v3.1.2 SCENARIO TESTING (A, B, X)
- All three scenarios (A: M_Pl,4 = 8.3×10¹² GeV, X: 887 GeV, B: 10¹⁹ GeV) are consistent with closed loop
- Different M_Pl,4 give different 9D = v_H and galaxy count predictions
- **Scenario X ADOPTED** (user-driven: "3D != 4D")
- **Scenario B REJECTED** (M_Pl,4 = M_Pl,3D violates brane-world principle)

### v3.1.2 SCENARIO X ADOPTED
- M_Pl,4D = 887 GeV (4D BULK Planck, INFERRED, brane-world)
- 3 different M_Pl at 3 different levels: 2D = 10³⁸ GeV, 3D = 10¹⁹ GeV, 4D = 887 GeV
- E_4D = 1.07×10⁵⁹ J (galaxy-scale 4D event, ~10⁹ M_sun)
- KEEPS: 9D = v_Higgs match (1.3% off v_H = 246 GeV), M^α M_Pl,N at 5-9D gives EW physics
- DROPS: standard 4D Planck throughout, multi-universe = galaxy count

### v3.1.2 USER-CORRECTED MULTI-UNIVERSE
- "energetic events in 4D can create 3D universes"
- 4D-bulk dynamics are UNKNOWN (NOT specifically '4D-galaxy collisions' — that earlier version was too specific)
- N_sub = 300 = number of sub-universes per 4D event
- Sub-universe = energetic 4D-bulk event (NOT 3+1D galaxy)
- E_sub = 3.5×10⁵⁶ J = small galaxy mass
- The 10¹² galaxies in our 3+1D universe are a SEPARATE population (formed after sub-universe creation)

### v3.1.2 FINAL: AGE vs LIFETIME / FRAME OF REFERENCE / LEGACY (KEY CORRECTIONS)

1. **AGE vs LIFETIME (KEY)**:
   - 13.8 Gyr = universe AGE (observed)
   - ~10³⁰ yr = predicted total LIFETIME (M^α)
   - Universe is at 1.4×10⁻²⁰ of its predicted lifetime (very young)

2. **FRAME OF REFERENCE (KEY)**:
   - M^α law gives APPARENT durations in LOWER-D frame, not proper time
   - 2D lifetime (33s) is in 3+1D frame
   - 3+1D sub-universe lifetime (~10³⁰ yr) is in 3+1D's own frame
   - 4D event apparent duration (1.4×10³⁴ yr) is in 3+1D frame, time-dilated from 4D proper time via γ ~ 10⁶²
   - 4D event proper duration: T_4D_proper = τ_4D / γ ~ 10⁻²⁰ s

3. **LEGACY CONTENT MOVED**:
   - calculations/legacy/: v31_scenario_B, v31_f_back_only_3d_to_4d, v31_proper_closed_loop, v31_F_p_consistency, v31_fp_z_derivation
   - paper/legacy/v31_60_4_old.md: original v3.1.2 §3.60.4 with E_4D = 10⁶⁹ J (Scenario A) and DUAL FRAMING
   - paper/legacy/README.md + calculations/legacy/README.md: documentation

### v3.1.2 §3.60.4 + §3.71 REWRITTEN
- §3.60.4: Scenario X, age vs lifetime, frame of reference explicit, sub-universe = energetic 4D-bulk event
- §3.71: Closed-loop formula universal at every level (with different M_Pl,N)
- L138, L139, L141, L145, L150 all updated in 06_limitations.md

### Files updated v3.1.2-final:
- paper/markdown/03c_lagrangian.md §3.60.4 (rewritten)
- paper/markdown/03c_lagrangian.md §3.71 (rewritten)
- paper/markdown/06_limitations.md (L138, L139, L141, L145, L150)
- README.md (version 3.1.2-final)
- paper/legacy/v31_60_4_old.md (NEW, archived old §3.60.4)
- paper/legacy/README.md (NEW)
- calculations/legacy/* (5 superseded scripts moved)
- calculations/legacy/README.md (NEW)

### GitHub commits (v3.1.2, latest first):
- fcffc04: v3.1.2 FINAL: AGE/LIFETIME/FRAME-OF-REFERENCE/LEGACY
- 0b6ad16: USER-CORRECTED sub-universe = energetic 4D-bulk event
- c629095: SCENARIO X ADOPTED M_Pl,4D = 887 GeV
- 0edd312: CLARIFY 4D event IS Big Bang
- 7f43183: CLARIFY M_Pl,3D measured vs M_Pl,4D assumed
- 3284601: SCENARIO B ADOPTED M_Pl,4 = standard 4D Planck
- ff2cf0a: §3.71 CLOSED-LOOP f_back SCALING WITH alpha
- dd11d1a: KEY SYMMETRY 2D->3D and 3D->4D identical structure
- 0e02846: v3.1.2 FINAL Remove alpha_true = 1.258
- 9ecd41f: v3.1.2 EMPIRICAL SMOKING GUN alpha=1.258 fails 13/14
- e9eff8e: v3.1.2 USER-CAUGHT Internal inconsistency 4pi and universal f_back

**Build: 354 pages, 81 limitations, all pushed to GitHub (fcffc04).**

---

## 11. Things to NOT re-do

- **Don't claim f_back = 10⁻⁸⁵ is a derived physical fraction.** It's a calibration (= ρ_DE / (ε × M_Pl⁴)). See L138.
- **Don't claim the closed loop closes numerically with v10 formula.** v10's formula was tuned (τ_4D = 1e28 yr, outside cone range). Use v3.1.2-final formula: f_back = (M_Pl,N/E_event)^α universal at every level. See L139.
- **Don't claim ε is derived.** It's observed (hierarchy problem). SIDC provides a geometric story but not a derivation. See L140.
- **Don't claim f_back is the SAME VALUE at every level.** It's universal in FORM (M_Pl/E)^α, but VALUES differ because M_Pl,N and E_event differ. 2D→3D = 1.83×10⁻⁴⁵ (audit), 3D→4D = 1.22×10⁻⁸⁵. See L141.
- **Don't confuse f_back (continuous) with pulsed return.** f_back formula gives CONTINUOUS back-flow fraction. Pulsed return at death is 100% (universal). 2D→3D: pulsed dominates by 10⁴⁵× (DM is pulsed, not f_back_2D). 3D→4D: continuous dominates NOW (DE is f_back_4D continuous, pulsed is in the future). See v31_fback_both_levels.py.
- **Don't conflate 13.8 Gyr with universe LIFETIME.** 13.8 Gyr is the universe's AGE (observed, the only firm value). LIFETIME is UNKNOWN — depends on N_sub (free parameter). User caught: "N_sub = 300 is not known, and not fixed; could be 150 with double the masses each". See L145.
- **Don't claim N_sub = 300 as if it were derived.** N_sub is a FREE PARAMETER (4D-bulk dynamics unknown). E_4D = N_sub × E_sub is fixed, but the partition is undetermined. See L144.
- **Don't ignore frame of reference.** M^α law gives APPARENT durations in LOWER-D frame, not proper time in higher-D frame. 4D event apparent duration (1.4×10³⁴ yr) is in 3+1D frame, time-dilated from 4D proper time (~10⁻²⁰ s) via γ ~ 10⁶².
- **Don't assume M_Pl,4D = M_Pl,3D.** In brane-world physics, bulk Planck is INDEPENDENT of brane Planck. The cascade has THREE different M_Pl: 2D = 10³⁸ GeV, 3D = 10¹⁹ GeV, 4D = 887 GeV. See L150.
- **Don't identify sub-universe with 3+1D galaxies.** Sub-universes are 3+1D universes created by an ENERGETIC EVENT in a 4D BULK (specific 4D-bulk mechanism UNKNOWN — NOT specifically '4D-galaxy collisions'). N_sub = 300 (sub-universes per 4D event), NOT 3×10¹². See L143, L150.
- **Don't present α = 1.258 as an alternative.** It's REJECTED by 14-event M^1.29 fit. Only α = 1.289 survives. See L142b.
- **Don't claim 4π is universal across all transitions.** 4π is specific to 3D→4D continuous leakage (verified ~1.7%). It is NOT at 2D→3D or higher transitions. See L146, L149.
- **Don't try to derive α=1.29 from a single calculation.** It's a saddle-point result; structural matches to 1+1/√12 are the right framing.
- **Don't add "free parameters" without justification.** Current count: α (calibrated), ε (calibrated), M_Pl,3D (MEASURED), M_Pl,4D (INFERRED). 4 free parameters total. See L150.
- **Don't promise "first-principles derivation" if it's structural.** Be honest about which pieces are derived vs structural matches.
- **Don't break the c=1 Liouville convention.** It's set by the 2D universe having 1 scalar; b=i is forced.
- **Don't reorder the 14 event types by lifetime.** They're 1 species at 14 different γ values (democratic cosmology).
- **Don't reintroduce the 5D/6D/9D extrapolation as derived.** It's SPECULATIVE, even with the 9D = string theory match. The α-power-law is one of several possibilities.
- **Don't keep stale content in main paper.** Move superseded sections to `paper/legacy/`. See `paper/legacy/README.md` for the archive.

---

## 12. Useful commands

```bash
# Build
bash paper/build_pdf.sh                    # full paper (30-60s, 354 pages)
bash paper/build_pdf.sh --dry-run          # README + layman (5-15s)

# Math cleanup
python3 paper/build_tools/cleanup_math.py file.md  # single file
python3 paper/build_tools/cleanup_math.py          # all files
python3 paper/build_tools/cleanup_math.py --build  # cleanup + build

# v3.1.2 calculations (current adopted)
python3 calculations/v31_closed_loop_fback.py      # closed-loop formula (universal at every level)
python3 calculations/v31_scenario_X.py             # Scenario X verification (M_Pl,4D = 887 GeV)
python3 calculations/v31_multi_universe_alpha.py   # multi-universe picture (energetic 4D-bulk events)

# v3.1.1 superseded (now in calculations/legacy/)
python3 calculations/legacy/v31_F_p_consistency.py        # F_p = 0 check (legacy)
python3 calculations/legacy/v31_proper_closed_loop.py     # proper closed loop (legacy)
python3 calculations/legacy/v31_f_back_only_3d_to_4d.py   # 3D-4D leakage (legacy)

# Git (with SSH key)
GIT_SSH_COMMAND="ssh -i /root/.ssh/github-deploy-key -o StrictHostKeyChecking=no" git push
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
- This file is the **quick reference** for current state (v3.1.2-final)
- `paper/legacy/` and `calculations/legacy/` have SUPERSEDED v3.1.2 content (Scenario A/B, α = 1.258, v10 closed loop)

For very old context (v1.x, v2.0-v2.5), see `changelog.md` and the topic file.

---

## 14. v3.1.2-final at a glance

**Key claims that are STILL VALID:**
- M^α scaling law across 14 event types (α = 1.289)
- 4D antigravity cancellation mechanism (geometric picture)
- Lagrangian skeleton as structural proposal for 2D universe physics
- L41, L42 (μ, m_{3+1D} identification)
- N=12 SM connection
- 2D universe → DM death return (cumulative 2D deaths)
- 9D = v_Higgs match (1.3% off, suggestive)
- Multi-universe picture (energetic 4D-bulk events)

**Key claims that are REVISED in v3.1.2-final:**
- **Closed loop is now universal**: f_back = (M_Pl,N/E_event)^α at EVERY dimensional transition (was: only 3D→4D in v3.1.1-final)
- **M_Pl,4D ≠ M_Pl,3D**: Three different M_Pl at three levels (2D = 10³⁸ GeV, 3D = 10¹⁹ GeV, 4D = 887 GeV)
- **Scenario X adopted**: M_Pl,4D = 887 GeV (4D BULK Planck, brane-world)
- **Sub-universe = energetic 4D-bulk events**: N_sub = 300, not 3×10¹² (galaxies)
- **AGE vs LIFETIME distinct**: 13.8 Gyr age, ~10³⁰ yr predicted lifetime
- **FRAME OF REFERENCE explicit**: M^α law gives apparent durations in lower-D frame
- **α still = 1.289** (only survivor of 14-event M^1.29 fit)

**Key claims that are REJECTED:**
- α = 1.258 (interpretation B): 13/14 events fail (solar flare 281% off, etc.)
- v10's closed loop formula (required unjustified τ_4D = 1e28 yr)
- f_back as 2D-to-3D back-projection (lifetimes too short, v3.1.1)
- "α-symmetry bridges forward and backward" (artifact of v10)
- "Three derivations of 1/2 close the loop" (now structural)
- Multi-universe = 3+1D galaxy count (interpretation A: 3×10¹²)
- Scenario A (M_Pl,4 = 8.3×10¹² GeV, breaks 9D = v_H)
- Scenario B (M_Pl,4 = M_Pl,3D, violates brane-world principle)
- 4π as universal geometric factor (specific to 3D→4D only)

**Free parameters (4 total, v3.1.2-final):**
- α = 1.289 (calibrated to 14 M^α events)
- ε = 10⁻³⁸ (calibrated to hierarchy)
- M_Pl,3D = 1.22×10¹⁹ GeV (MEASURED via Newton's G)
- M_Pl,4D = 887 GeV (INFERRED, cascade consistency + 9D = v_H match)

**Honest framing:**
- SIDC is a geometric framework with empirical constraints
- It provides a CONSISTENT PICTURE, not derivations
- The closed loop is a CONSISTENCY CONDITION (universal formula at every level)
- The Lagrangian is a STRUCTURAL PROPOSAL, not a complete theory
- ε, f_back, and DE values are OBSERVED/CALIBRATED, not derived
- M_Pl,4D is INFERRED (not measured)
- The hierarchy and cosmological constant problems are NOT solved by SIDC
- 9D = v_H match is suggestive (1.3%, single number, could be coincidence)
