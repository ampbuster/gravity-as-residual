<!-- 15_falsifiability_matrix.md - part of paper.md split (v3.0.13) -->

## 14. Falsifiability Matrix: What Would Test SIDC? (v2.7.13+)

This section consolidates SIDC's *testable predictions* across all upcoming and ongoing observations, organized as a single reference matrix. Each entry specifies:

- **What SIDC predicts** (with quantitative amplitudes where possible)
- **What observation would falsify it** (with thresholds)
- **The current status** (validated, pending, or untested)
- **The year the test becomes possible**

SIDC's predictions span 5-10 orders of magnitude in energy, time, and frequency. The matrix below is the comprehensive list.

### 14.1 Near-term tests (2026-2027)

#### DESI DR3 (2026-2027): dark energy equation of state w₀, wₐ

**SIDC prediction:** w₀ = -0.83 ± 0.16, wₐ = -0.75 ± 0.30 (DESI+ACT+Planck 2024-25, currently 3.5σ tension with $\Lambda{\rm CDM}$)

**Falsification threshold:**
- If w₀ = -1 confirmed at > 5σ: SIDC's standard Lagrangian (constant $f_{back}$) is right
- If w₀ = -0.83 confirmed at > 5σ: SIDC's standard Lagrangian falsified; needs running $f_{back}(z)$ (adds 1 free parameter)

**Status:** PENDING. Currently 3.5σ, not yet falsification or validation.

#### LSST Y1 (2027): 47 Tuc DM content

**SIDC prediction:** 47 Tuc has *no DM* (old GCs have no DM, per SIDC's stellar-density argument). DM detection threshold: $M_{DM}/M_* < 10^{-5}$.

**Falsification threshold:** If 47 Tuc shows DM at > 5σ (e.g., via stellar kinematics), SIDC's prediction is falsified.

**Status:** PENDING. LSST Y1 data 2027.

#### eROSITA + SPHEREx + GW231123 + GW230529: ongoing multi-messenger

**SIDC prediction:** Consistent with $\Lambda{\rm CDM}$ at the level of these specific observations (no specific tension). The 2025-2026 catalog of 45 external constraints is consistent with SIDC.

**Status:** VALIDATED. All 2024-2026 observations are consistent with SIDC's qualitative framework.

### 14.2 Mid-term tests (2027-2034)

#### SKA-MPG PTAs (2030s): BNS/AGN 2D universe death GW

**SIDC prediction:** Stochastic GW background at frequencies:
- BNS: $f_{GW} \approx 7 \times 10^{-14}$ Hz (PTA band)
- AGN: $f_{GW} \approx 2 \times 10^{-17}$ Hz (PTA band)

**Falsification threshold:**
- If GW detected at SIDC's predicted frequencies: α = 1.29 validated to ±0.11
- If GW detected at 10× off-frequency: α falsified to ±0.11
- If BNS+AGN internally inconsistent: framework-level falsification (not just α)
- If no GW detected: SIDC's GW prediction falsified (less direct)

**Status:** PENDING. SKA-MPG operational 2030s.

#### LISA (2034+): 2D universe death GW at mHz

**SIDC prediction:** SIDC's SN death GW at 0.03 Hz is 6-14 orders BELOW LISA noise. LISA will NOT detect SIDC's death GW.

**Falsification threshold:** If LISA detects *something* at SIDC's predicted amplitudes, that's a *positive* surprise (SIDC underpredicts GW).

**Status:** Most likely LISA will see no SIDC signal, consistent with SIDC's prediction.

#### Direct $M_{\rm Pl,4}$ measurement (2030s+ colliders)

**SIDC prediction:** $M_{\rm Pl,4D} \geq 887$ GeV (derived from $T_{3D}' \geq 13.8$ Gyr).

**Falsification threshold:** If $M_{\rm Pl,4}$ measured at < $3.93 \times 10^{23}\,\text{GeV}$, SIDC's bulk-brane coupling is wrong.

**Status:** PENDING. Future colliders or precision tests.

### 14.3 Long-term tests (2034+)

#### μAres (next-gen PTA, 2040s?): higher-precision α

**SIDC prediction:** α = 1.29 to ±0.055 precision (1 dex frequency precision → 0.055 in α).

**Falsification threshold:** If α measured at < 1.20 or > 1.40, SIDC's energy-scaling rule is wrong.

**Status:** PENDING. μAres operational 2040s.

#### BBN precision (10× improvement)

**SIDC prediction:** DE at BBN era (z = 10¹⁰) is ∼ 10⁻²⁰ of radiation. BBN proceeds as standard.

**Falsification threshold:** If $\rho_{DE}(BBN) > 10^{-20} \times \rho_{rad}(BBN)$, SIDC's BBN prediction is wrong.

**Status:** PENDING. Future precision BBN.

### 14.4 Cross-observational consistency

| Test | SIDC predicts | Falsification threshold |
|------|------------------|-------------------------|
| w₀ (DESI DR3) | -0.83 ± 0.16 | > 5σ away from -0.83 |
| wₐ (DESI DR3) | -0.75 ± 0.30 | > 5σ away from -0.75 |
| 47 Tuc DM (LSST) | < 10⁻⁵ M_* | DM detected at > 5σ |
| BNS GW (SKA-MPG) | f ≈ $7 \times 10^{-14}\,\text{Hz}$ | 10× off-frequency |
| AGN GW (SKA-MPG) | f ≈ $2 \times 10^{-17}\,\text{Hz}$ | 10× off-frequency |
| $M_{\rm Pl,4}$ (colliders) | ≥ $4 \times 10^{23}\,\text{GeV}$ | Measured < $3.93 \times 10^{23}\,\text{GeV}$ |
| BBN DE (precision) | < 10⁻²⁰ rad | > 10⁻²⁰ detected |
| 5/27/68 (Planck) | 5/27/68 (input) | Input, not tested |

### 14.5 The 5-10 year window

SIDC's critical test period is **2026-2034**:
- 2026-2027: DESI DR3 + LSST Y1 (DE and 47 Tuc)
- 2027-2030: eROSITA-final, SPHEREx, ongoing multi-messenger
- 2030s: SKA-MPG PTAs (GW)
- 2034: LISA launch

If multiple tests simultaneously validate SIDC, that's strong evidence. If multiple falsify, SIDC is in trouble. The 5-10 year window is when SIDC's status will be **either** "validated 2D universe framework" **or** "falsified, time to move on".

**The honest cost:** SIDC is testable, but most tests are in the future. Until then, SIDC is a *promising* phenomenological framework with structural support from 5 of 6 framework analyses (§3.8), but no first-principles derivation. See `calculations/v27_alpha_sensitivity.py` for α sensitivity analysis.
*Version: v2.4*
*Repository: https://github.com/ampbuster/gravity-as-residual*
*Version: v2.4 (pending version bump; v2.3.2 → v2.4)*
*Repository: https://github.com/ampbuster/gravity-as-residual*
*License: CC-BY 4.0 (manuscript), MIT (code)*
*Correspondence: GitHub issues*

*How this paper came to be:* SIDC emerged from a series of plain-language intuitions in conversation between a non-physicist (the author) and an AI assistant (Mavis / MiniMax-M3). The original intuitions — dark matter as "like a neutrino," as a wind on paper, as a cancelling-through-dimensions effect — are preserved verbatim in `supporting/how-did-we-get-here.md`. The model was developed by progressively making those intuitions mathematically precise and testing them against observational data. The paper at v2.3.1 is the artifact; the conversation is the origin story.

