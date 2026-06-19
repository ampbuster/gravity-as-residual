# LEGACY — Old Parameter Values (Historical)

> **Status**: Historical. This file documents old parameter values used in
> earlier versions of SIDC, found in the v3.5.7 consistency audit.
> All "legacy" values are SUPERSEDED by the current canonical parameters.
>
> **Current canonical values** (v3.5.7):
> - α = 1.289
> - M_Pl,3D = 1.22×10¹⁹ GeV
> - M_Pl,2D = 3 TeV
> - M_Pl,4D = 4×10²³ GeV (derived)
> - μ = 9×10⁶ GeV²
> - E_4D = 5×10⁷⁹ J
> - τ_4D = 1.51×10³⁴ yr
> - γ_4D = 6.03×10⁹⁰
> - τ_3D,apparent = 9.10×10²⁴ yr
> - N_sub = 4×10²
> - ε = 10⁻³⁸

---

## 1. α Parameter Evolution

### v2.7 era (early framework)
- α = 1.5 (early estimate, "simple Schwarzian")
- α = 1.6 (CGHS back-reaction upper bound)

### v3.0.x era (trial-and-error)
- α = 1.18 (rejected, too low for SN match)
- α = 1.20 (rejected, marginal SN match)
- α = 1.239 (rejected, before M^α law)
- α = 1.258 (CGHS back-reaction lower bound)
- α = 1.27 (intermediate, decent match)
- α = 1.279 (CGHS back-reaction, close to optimal)
- α = 1.28 (intermediate, near-final)

### v3.0.20 era (Lagrangian trial-error)
- α = 1/2 + 1/2 + 1/√12 = 0.5 + 0.5 + 0.2887 = **1.2887** (near-final)
- α = 1 + 1/√12 = 1.2887 (simplified decomposition)
- α = 1.34 (CGHS upper, rejected)

### v3.1 era (reframe)
- α = 1.289 (current, calibrated to 14 events)
- α = 1.29 (rounded, used in some sections)
- α = 1.30 (rounded, used in some sections)

### v3.5 era (web research)
- α = 1 + 1/√N where N=12 — "leading + finite-N" (cleanest reason)
- α = 1 + ln(q²/N) for q=4 — curve-fit (no physical reason)

**CURRENT**: α = 1.289 (universal, calibrated, structurally motivated)

---

## 2. M_Pl,4D Evolution

### v3.0.x era
- M_Pl,4D = 887 GeV (initial, before 9D scaling)
- M_Pl,4D = 9×10¹⁸ GeV (9D = v_Higgs era)

### v3.1 era
- M_Pl,4D = 4.34×10¹⁹ GeV (M_Pl,3D × α^5, dropped in v3.3)
- Direction was WRONG (lower than M_Pl,3D)

### v3.3 era (FINAL)
- **M_Pl,4D = 4×10²³ GeV** (DERIVED via α-weighted GM)
- Formula: M_Pl,4D = M_Pl,3D^α × M_Pl,2D^(1-α) = 4×10²³ GeV
- Direction CORRECT (higher than M_Pl,3D)
- Uses BOTH Plancks structurally via framework's α

**CURRENT**: M_Pl,4D = 4×10²³ GeV (derived, not free)

---

## 3. τ_3D Evolution

### v2.x era
- τ_3D = 1.83×10⁹⁸ yr (incorrect gamma_4D = 1.29×10⁶⁴)

### v3.3 era (FINAL)
- **τ_3D,apparent = 9.10×10²⁴ yr** (5×10²⁷× longer)
- γ_4D = 6.03×10⁹⁰ (was 1.29×10⁶⁴)
- This means universe at 1.5×10⁻¹⁵ of lifetime (was 7.5×10⁻⁸⁹)

**CURRENT**: τ_3D,apparent = 9.10×10²⁴ yr

---

## 4. γ_4D Evolution

### v2.x era
- γ_4D = 1.29×10⁶⁴ (incorrect)

### v3.3 era (FINAL)
- **γ_4D = 6.03×10⁹⁰** (correct, after M_Pl,4D derivation)
- The factor of 5×10²⁷ increase comes from M_Pl,4D = 4×10²³ vs 9×10¹⁸

**CURRENT**: γ_4D = 6.03×10⁹⁰

---

## 5. E_4D Evolution

### v3.0 era
- E_4D = 10⁶⁹ J (M_Pl,3D scale, no 4D event)

### v3.3 era (FINAL)
- **E_4D = 5×10⁷⁹ J** (universe-scale, M^α law with M_Pl,4D and τ_4D)
- 10⁸× observable universe, 10⁷× full universe (structural requirement)
- Universe is ~10⁻⁸ of 4D event

**CURRENT**: E_4D = 5×10⁷⁹ J (universe-scale)

---

## 6. M_Pl,2D Evolution

### v2.x era
- M_Pl,2D = 1 TeV (initial guess)
- M_Pl,2D = 10 TeV (calibrated to different SN lifetime)

### v3.0 era (FINAL)
- **M_Pl,2D = 3 TeV** (calibrated to τ_SN = 33 s)
- μ = M_Pl,2D² = 9×10⁶ GeV²

**CURRENT**: M_Pl,2D = 3 TeV (calibrated)

---

## 7. Version Timeline Summary

| Version | Key changes |
|---------|-------------|
| v2.7 | α = 1.29 from CGHS, 37 limitations |
| v3.0 | Lagrangian trial-error, α decomposition |
| v3.1 | α = 1.289 final, 92 limitations |
| v3.2 | de Sitter cosmology, falsification tests |
| v3.3 | BILATERAL CASCADE, M_Pl,4D derived, 30 corrections |
| v3.4 | F-theory 12D + "12 propagates" honest reframe |
| v3.4.5 | 8 inconsistencies in "12" hypothesis |
| v3.4.6 | "12 is correlation not derivation" |
| v3.4.7 | Why "12" is common in physics |
| v3.4.8 | Universe age = 1.5×10⁻¹⁵ of lifetime |
| v3.5 | TIER 2 research (CY3 Z_12, α, μ) |
| v3.5.1-v3.5.5 | μ first-principles (11 angles, 45 formulas, etc.) |
| v3.5.6 | **WEB SEARCH BREAKTHROUGH** — μ has 5+ structural origins |
| v3.5.7 | **AUDIT** + consistency check |

---

## 8. What Goes in Legacy

When parameter values change across versions, OLD values go here.

**Pattern**:
- Old value documented with version
- Reason for change
- Pointer to current canonical value
- New value

This way:
- Future readers can see the evolution
- Code can reference legacy values without breaking
- Audit can identify orphan references

---

**File created**: June 19, 2026 (v3.5.7 audit)
**Last modified**: June 19, 2026
**Commit**: `fefcbaa`
**Location**: `paper/legacy/v357_legacy_parameters.md`