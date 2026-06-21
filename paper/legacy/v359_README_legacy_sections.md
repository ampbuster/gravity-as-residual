# LEGACY README Sections (v3.5.9+ extraction)

> **Status**: ARCHIVED — This file preserves legacy sections of the README that used DROPPED frameworks (F_p(z) Hill function, primordial DM, v3.0.21 f_back naming).
> 
> **Date extracted**: 2026-06-21 (v3.5.9+ SESSION 5+ cleanup)
> 
> **Why extracted**: Per user request: "put those legacy else somewhere like a legacy readme. keep the paper and readme current."
> 
> **Current framework (v3.5.9+ A1)**: bilateral cascade + f_leak = H_0 + calibrated AGN rate. No F_p(z). No primordial DM. No f_back (renamed to f_DE / f_DM,leak / f_DM,death in v3.5.7+ naming revolution).

---

## Section 1: "Sun, tidal dwarfs, AGC/KKR" (HISTORICAL)

**Original README location**: Lines 258-293
**Original date**: v3.2, user-question
**Original content**:

> ⚠️ **HISTORICAL FRAMEWORK NOTE (v3.2, pre-v3.3)**: This section uses the **OLD Hill function F_p(z)** framework which was **DROPPED in v3.3+** (per L100, user-critique 6 times). The 5/5 dwarf cases, cosmic SFH calculation, and AGC/KKR analysis are STILL VALID (they use the smooth C(E) = E^(1+α) function which is RETAINED), but the F_p(z) framing for primordial vs cumulative DM is HISTORICAL. Current framework (v3.5.9+ A1) uses bilateral cascade with f_leak = H_0; 27% DM comes from calibrated AGN rate. See `paper/legacy/v3_legacy_dm_dynamics_hill_Fp.md`.

**User question**: "how about the sun? and tidal dwarfs? is the paper still consistent? agc/kkr?"

**Answer**: YES, the paper is still consistent. The 5/5 dwarf cases all pass under v3.2's smooth function.

**Per-event smooth function C(E) = E^(1+ α)** gives the DM contribution:

| Case | E (J) | C(E)/C(SN) | DM status | Consistent? |
|---|---|---|---|---|
| Solar flare (typical) | 10²² | 10⁻⁵¹ | Negligible | ✓ |
| Solar flare (max) | 10²⁵ | 10⁻⁴⁴ | Negligible | ✓ |
| Sun daily output | 10²⁸ | 10⁻³⁷ | Negligible | ✓ |
| **Sun total over 4.6 Gyr** | 5×10⁴³ | **0.20** | sub-SN | ✓ (Sun has no DM, ~1 SN over Hubble) |
| **Sun total over Hubble time** | 1.5×10⁴⁴ | **2.5** | comparable to 1 SN | ✓ |
| AGC 114905 SF (low) | 10³⁰ | 10⁻³³ | Negligible | ✓ (no DM) |
| Tidal dwarf cumulative (1 Gyr) | 10³⁶ | 10⁻¹⁹ | Negligible | ✓ (no DM) |
| KKR 25 (intermediate SF) | 10³⁸ | 10⁻¹⁴ | Negligible per event, DM via cumulative | ✓ (DM-rich via S_destruction) |
| DF2/DF4 (old pop) | — | — | No recent events | ✓ (no DM) |

**Why Sun has no DM**: a single Sun's TOTAL output over 13.8 Gyr is comparable to 1 SN, but spread over 10 Gyr. Galaxies have 10⁶-10¹² SNe, so the Sun's 1-SN worth is below detection threshold for a single star system.

**Why tidal dwarfs / AGC 114905 have no DM**: low-mass SF, no recent SN, smooth function C = 10⁻³³ to 10⁻¹⁹ × C(SN), negligible.

**Why KKR 25 has DM**: intermediate-age SF (1-4 Gyr ago). Current SF negligible, but cumulative return from past SN (S_destruction mechanism) contributes.

**v3.2 changes don't affect this analysis**:
- N_sub FREE (doesn't affect individual galaxy DM)
- M_Pl,2D = 2.95 TeV (natural E_crit, below all dwarf cases)
- M_Pl,4D = 3.93 × 10²³ GeV (v3.3+ α-weighted GM, was 887 GeV in v3.1.2 Scenario X)
- M^α scaling, closed loop (unchanged)

**5/5 dwarf cases still pass**: Sun, AGC 114905, KKR 25, DF2/DF4, FCC 224.

**CURRENT (v3.5.9+)**: The 5/5 dwarf test cases (Sun, AGC 114905, KKR 25, DF2/DF4, FCC 224) are RETAINED in current framework but the per-event smooth function table above uses pre-v3.3 framing. The CURRENT test is in paper §12 (36/36 galaxy-zoo tests).

---

## Section 2: "Cosmic SFH → Ω_DM Closed-Loop Calculation" (LEGACY HISTORICAL)

**Original README location**: Lines 294-345
**Original date**: v3.2, user-requested
**Original content**:

**User request**: "for closed loop -> Calculate the total returned energy from the cosmic star formation history and show it matches Ω_DM ≈ 0.27"

**HONEST RESULT**: Cosmic SFH integrated gives 7.6×10⁶× TOO LITTLE DM to match Ω_DM = 0.27 from SN-driven 2D universe deaths alone.

**Step-by-step calculation**:

1. **Cosmic SFH (Madau-Dickinson 2014)** integrated over z = 0 to 10:
   ρ_* = 8.05 × 10⁸ M_⊙/Mpc³

2. **Total SNe**: 1 SN per 100 M_⊙ (Salpeter IMF, M > 8):
   N_SN = 8.05 × 10⁶ SNe/Mpc³

3. **Per-SN 2D universe rest mass**:
   M_2D,actual = 5.59 × 10⁻⁴ M_⊙

4. **Total SN-driven DM**:
   ρ_DM(SN driven) = 4.5 × 10³ M_⊙/Mpc³

5. **Compare to observed Ω_DM**:
   ρ_DM(observed) = 3.4 × 10¹⁰ M_⊙/Mpc³

6. **Ratio**: 7.6 × 10⁶

**Interpretation**: SN-driven 2D universe deaths give 7.6 million × too little DM.

**How the framework addressed this (DROPPED framework)**: F_p(z) Hill function separates PRIMORDIAL vs CUMULATIVE:
- **99.93% of DM is PRIMORDIAL** (from 4D event's 2D universe deaths at z ~ 1)
- **0.07% of DM is CUMULATIVE** (from SN-driven 2D universe deaths)
- F_p(0) = 0.9993 (calibrated), F_p(1) = 1.0

**Primordial contribution**: 4D event mass = 6.0×10¹¹ M_⊙ (galaxy scale). To explain Ω_DM:
   N_p = ρ_DM(observed) / M_4D = 0.057 ≈ 6%

**Closed loop, honestly (v3.2 framing)**:
- ✓ DE matching: 0.13% match (simple f_DE formula)
- ✗ DM from SN: 7.6×10⁶× too small
- ✓ DM from 4D event (primordial): matches if N_p ~ 10¹²

**CURRENT (v3.5.9+ A1)**: 
- F_p(z) Hill function DROPPED in v3.3+ (user-catch SIX TIMES)
- 'Primordial DM' REVISED — concept was WRONG (1st catch), cumulative NOT just SNe (2nd catch), DM/baryon ratio (3rd catch), f_back can't balance DM (4th catch), DM→ν decay too short (5th catch), f_back formula is per-event (6th catch)
- Current framework uses bilateral cascade + f_leak = H_0 + calibrated AGN rate
- 27% DM = OBSERVATIONAL DATA (Planck 2018), not derived from F_p(z)
- See `paper/legacy/v3_legacy_dm_dynamics_hill_Fp.md` for the full framework transition

---

## Section 3: "F_p(z) is OLD and AGC/KKR problem" (LEGACY HISTORICAL)

**Original README location**: Lines 346-374
**Original date**: v3.2, user-caught
**Original content**:

**User question**: "isn't F_p(z) old? also, if DM is mostly primordial, how to explain agc/kkr"

**HONEST ANSWER**: Both concerns are valid.

**F_p(z) is OLD (v2.7.52, pre-Lagrangian)**:
- F_p(z) = 0.9993 + 0.0007 × z²/(z_half² + z²), z_half = 3
- Introduced in v2.7.52, BEFORE the v3 Lagrangian era
- Has NOT been updated for v3.x
- The Lagrangian gives per-event creation C(E) = E^(1+ α) and pulsed return at death
- But F_p(z) z-evolution is STILL phenomenological

**AGC/KKR inconsistency**:
- If 99.93% of DM is primordial (F_p(0) = 0.9993), then per-galaxy DM variation CANNOT be explained by cumulative 0.07% alone
- AGC 114905 (no DM) vs KKR 25 (DM-rich) variation is 100% (zero to significant)
- But cumulative is only 0.07% of total DM

**Status (v3.2)**:
- ✓ 5/5 cases are self-consistent for cumulative DM
- ✗ Total DM variation (primordial + cumulative) is NOT addressed
- ✗ F_p(z) functional form is a FIT, not derived

**CURRENT (v3.5.9+)**: This entire section is REPLACED. F_p(z) DROPPED. The 5/5 dwarf cases still pass but under different mechanism (cumulative SN-driven 2D deaths, not 99.93% primordial).

---

## Section 4: "Result 2: Closed-Loop Formula f_back" (v3.0.21 HISTORICAL)

**Original README location**: Lines 96-161
**Original date**: v3.0.21
**Original content**: See git history at commit pre-v3.5.7.

**CURRENT (v3.5.9+)**: 
- f_back was RENAMED in v3.5.7+ naming revolution
- f_back (2D→3D continuous) → f_DM,leak = 1.6×10⁻⁴⁵
- f_back (3D→4D continuous) → f_DE = 1.22×10⁻⁸⁵
- 100% pulsed return at death → f_DM,death = 1
- See `paper/legacy/v357_f_back_clarification.md` for the full naming revolution

---

## Section 5: "#1 (Consistency with ΛCDM)" (HISTORICAL framework notes)

**Original README location**: Lines 744-789
**Original date**: v2.7.4-v2.7.5
**Original content**: See git history at pre-v3.3.

**CURRENT (v3.5.9+)**: 
- The r(z) ≈ (1+z)³ match is REPRODUCED in current framework via different mechanism (bilateral cascade)
- F_p(z) DROPPED v3.3+; smooth E^(1+α) creation function RETAINED
- Thomson scattering contribution is NEGLIGIBLE under E^(1+α) weighting
- The 47 TUC TEST (§11) is the only TRULY differentiating prediction between SIDC and ΛCDM

---

## Summary

| Section | Original Lines | Status | Replaced by (v3.5.9+) |
|---------|----------------|--------|------------------------|
| Sun/tidal dwarfs/AGC/KKR | 258-293 | HISTORICAL | §12 galaxy-zoo tests (36/36) |
| Cosmic SFH → Ω_DM | 294-345 | LEGACY HISTORICAL | 27% DM from calibrated AGN rate |
| F_p(z) is OLD | 346-374 | LEGACY HISTORICAL | DROPPED entirely |
| Result 2: Closed-Loop | 96-161 | v3.0.21 HISTORICAL | f_DE / f_DM,leak / f_DM,death naming |
| #1 Consistency with ΛCDM | 744-789 | HISTORICAL framework | r(z) match via bilateral cascade |

**Total extracted**: ~80 lines of legacy content
**New README sections**: Replaced with short pointer banners

---

## Section 6: v2.7.3 STATE summary (HISTORICAL)

**Original README location**: Lines 822-836 (pre-extraction)
**Original date**: v2.7.3

**Original content**:
- v2.7.3 milestone: 45 external constraints catalogued; 4 → 2 free parameters via web-research convergence
- 50 honest limitations (v2.7.42+; 30 open, 10 partial, 3 closed, 2 falsified, 4 reverted, 1 discarded)
- 45 external constraints (4 parameter-reducing, 7 interpretive-cosmological, 4 interpretive-theoretical, 5 latest 2024-2025, 5 final 2024-2025, 5 late 2025-2026, 5 extended 2025-2026, 5 round 8, 1 new SIDC prediction)
- 🎯 47 TUC TEST (§11): PREDICTION (not yet a result). SIDC predicts $M_{dyn} \approx M_{stars}$ (no local DM); particle DM predicts $M_{dyn} > M_{stars}$. Awaiting DR1 (2027) or Y10 (2034).
- 🧪 36/36 GALAXY-ZOO TESTS PASS (§12)
- ✅ CMB RESOLVED (§4.48.1, v2.7.5+, HISTORICAL F_p(z) framework): smooth $F_p(z)$ (Hill n=2, $z_{half}$=3) gives r(z) ≈ (1+z)³ at high z. F_p(z) DROPPED v3.3+; r(z) ≈ (1+z)³ REPRODUCED in current framework via bilateral cascade.
- 📊 MCMC RAR FIT (§13.7): $a_0 = 2.34 \times 10^{-10}$ ± $1.54 \times 10^{-10}$ m/s²
- Killer match: TRGB $H_0 = 69.8 \pm 1.9$ is 0.2σ from SIDC $H_{0,4D} = 70.16$
- Theoretical foundation: c=1 string theory matrix model
- 2 remaining free parameters: μ + $m_{3+1D}$ (require 2D CFT expert)
- 0 strongly confirmed, 0 falsified, 16 pass, 1 confounded (out of 17 test categories)
- Smoking guns: 3 reproducible, but not unique to SIDC. 47 Tuc test is the only TRULY differentiating prediction.

---

## Section 7: v2.7.3+ §11 — 47 TUC TEST FOR RUBIN/LSST (HISTORICAL)

**Original README location**: Lines 837-840 (pre-extraction)
**Original date**: v2.7.3+

**Original content**:

A new section §11 anchors SIDC's DM mechanism to a near-term, low-cost, high-leverage falsification test: the 47 Tucanae (NGC $10^4$) globular cluster in the context of Rubin/LSST DP1 (released June 30, 2025).

- 47 Tuc is the cleanest test: no current SN, no massive star formation, $\sim 10^6$ old low-mass stars
- SIDC prediction: $M_{dyn} \approx M_{stars}$ (no local DM enhancement), 5 tidal tails fit Galactic potential
- Testable predictions: DP1 (2025), DR1 (2027), Y10 (~2034)
- Falsification: $M_{dyn} > 2 \times M_{stars}$ at 3σ → SIDC's DM mechanism falsified
- Generalization: SIDC's "no current activity → no local DM" rule applies to all quiescent systems

The 47 Tuc test does NOT depend on the speculative end-of-universe extension in §10. It tests the core of SIDC: the link between energetic activity and local DM enhancement.

---

## Section 8: Intermediate F(z) dwarf population — historical F(z) framework

**Original README location**: Lines 945-1010 (pre-extraction)
**Original date**: v2.7.32+

**Original content** (summary):

SIDC's HISTORICAL smooth F(z) function:
- F(z) = 1/(1 + (z/z_half)^{-n}), Hill n=2, z_half=3
- Predicts intermediate F(z) ~ 0.1-0.5 population (10-30% of field dwarfs)
- This is the "missing dwarf" population
- Testable with LSST Y1 (2027), Euclid Q1 (2026)

CURRENT (v3.5.9+ A1): The prediction is REPRODUCED via calibrated AGN rate giving 27% DM. The specific F(z) ~ 0.1-0.5 distribution is HISTORICAL. See `paper/legacy/v3_legacy_dm_dynamics_hill_Fp.md` for framework transition.

Key observational papers:
- Bidaran et al. 2025 (arXiv:2501.02910): quenched isolated dwarfs in voids, log(M*/M☉) = 8.9-9.5
- CVnC dwarf (Hagen+ 2026): $M_{dyn}$ ≫ $M_{b}$
- Pre-2025: bimodal (gas-rich vs. quenched); 2025-2026: intermediate population discovered

---

## Summary Table (Updated)

| Section | Original Lines | Status | Replaced by (v3.5.9+) |
|---------|----------------|--------|------------------------|
| Sun/tidal dwarfs/AGC/KKR | 258-293 | HISTORICAL | §12 galaxy-zoo tests (36/36) |
| Cosmic SFH → Ω_DM | 294-345 | LEGACY HISTORICAL | 27% DM from calibrated AGN rate |
| F_p(z) is OLD | 346-374 | LEGACY HISTORICAL | DROPPED entirely |
| Result 2: Closed-Loop | 96-161 | v3.0.21 HISTORICAL | f_DE / f_DM,leak / f_DM,death naming |
| #1 Consistency with ΛCDM | 744-789 | HISTORICAL framework | r(z) match via bilateral cascade |
| v2.7.3 STATE | 822-836 | HISTORICAL | Current state in README |
| v2.7.3+ §11 | 837-840 | HISTORICAL | 47 Tuc test description in README |
| Intermediate F(z) population | 945-1010 | HISTORICAL framework | intermediate past-SF dwarfs in README |

**Total extracted**: ~150 lines of legacy content (was ~80 before this pass)
**New README sections**: Replaced with short pointer banners
