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
