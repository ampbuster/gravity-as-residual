# LEGACY — f_back Terminology Clarification (v3.5.7)

> **Status**: Active clarification. This file documents the overloaded use of
> "f_back" in the framework, which has caused confusion.
>
> **Issue raised**: User (June 19, 2026): "what does f_back mean? 2d death ->
> 3d DM? why 10^-85? isn't that number for 4d->3d DE?"

---

## The Problem

The symbol "f_back" has been overloaded with TWO different meanings. The user
suggested better naming (**f_DM_leak / f_DM_death / f_DE**), which we adopt:

| Usage | Direction | Value | What it produces |
|-------|-----------|-------|------------------|
| **f_DE** (was: f_DE) | 3+1D → 4D | 1.2×10⁻⁸⁵ (= t_Pl/τ_4D) | **DE** (dark energy) |
| **f_DM_leak** (was: f_DM_leak) | 2D → 3+1D (while alive) | 1.6×10⁻⁴⁵ (= t_Pl/τ_2D) | Negligible (0.16 J per SN) |
| **f_DM_death** (was: "100% pulsed return") | 2D → 3+1D (at death) | **1** (100%) | **DM** (27% cumulative) |

The user is CORRECT:
- **10⁻⁸⁵ is NOT for 2D → 3D DM**
- **10⁻⁸⁵ is for 3+1D → 4D DE**
- **2D → 3D DM is 100% pulsed return at death**, not a leakage fraction

---

## The Three Flows (CLEAR Distinction)

### Flow #1: 4D → 3+1D (DE direction, downward)
- **Continuous leakage** while 3+1D universe exists
- **f_DE = 10⁻⁸⁵** (3+1D-to-4D)
- This is what explains DE (68% of ρ_crit)
- **Closed loop** with 4D → 3+1D projection (γ_4D ~ 10⁶²)

### Flow #2: 3+1D → 2D (DM direction, downward)
- **Pulsed creation** when 3+1D events create 2D universes
- **100% pulsed return** when 2D dies
- M^α law: τ_2D = (E_3+1D/M_Pl,3D)^α × t_Pl,3D
- This is what produces **DM** (27% of ρ_crit)

### Flow #3: 2D → 3+1D (DM direction, upward)
- **Pulsed return at death = 100%**
- NOT continuous leakage (which is only 1.6×10⁻⁴⁵ per SN)
- Cumulative over cosmic history gives 27% DM

---

## What Goes Where (Clear Summary)

| Phenomenon | Mechanism | Value | Direction |
|------------|-----------|-------|-----------|
| **Dark energy (68%)** | 4D antigravity, time-dilated | f_DE = **10⁻⁸⁵** | 4D → 3+1D |
| **Dark matter (27%)** | Cumulative 2D universe deaths | **100% pulsed** | 2D → 3+1D at death |
| **Baryons (5%)** | Standard BBNS | N/A | Standard |
| **Gravity (ε = 10⁻³⁸)** | 4D antigravity cancels 3+1D gravity | residual | 4D bulk |

---

## The Confusing Line in §3c Lagrangian

> "4D event creates 3+1D (forward, f_DE = 10⁻⁸⁵)"
> "3+1D leaks back to 4D (backward, f_DE = 10⁻⁸⁵)"

This is the **closed loop for DE**, NOT for DM. It explicitly:
- Uses γ_4D ~ 10⁶² (time dilation)
- Gives DE = f_back × ε × M_Pl⁴
- Is for 4D ↔ 3+1D transition ONLY

DM is a DIFFERENT flow entirely.

---

## Proposed Renaming (Future Cleanup)

To avoid future confusion, the framework SHOULD rename:

| Old | New | Why |
|-----|-----|-----|
| f_back (3D→4D) = 10⁻⁸⁵ | **f_DE** or **f_4D-leak** | It's specifically for DE |
| f_back (2D→3D while alive) = 10⁻⁴⁵ | **f_leak** | It's continuous leakage |
| 2D universe death = 100% return | **pulsed return** | Already named correctly |
| 4D → 3+1D "projection" | **γ_4D projection** | Keep, it's specific |

---

## Current Paper Status

The paper EXPLICITLY distinguishes these in §3c Lagrangian:

> **"f_DE = 10⁻⁸⁵ ONLY makes sense as 3D-to-4D"**
> - 3+1D universe CURRENT AGE: 13.8 Gyr; LIFETIME: ~10³⁰ yr
> - **f_DE = t_Pl/τ_4D = 1.2×10⁻⁸⁵ ✓ → DE**
> - **f_DM_leak = t_Pl/τ_2D = 1.6×10⁻⁴⁵ (NOT 10⁻⁸⁵)**
> - DM = cumulative 2D universe deaths (Σ M_2D × N), 100% pulsed at death

But this distinction is buried in §3c, easy to miss.

---

## Recommendation

Add to §0 Glossary or §3c a **"f_back USAGE GUIDE"** clearly stating:

1. **f_DE = 10⁻⁸⁵** = 3+1D→4D leakage rate → explains DE
2. **f_DM_leak = 10⁻⁴⁵** = 2D→3+1D while-alive leakage → negligible
3. **DM from 2D death** = 100% pulsed return (NOT a continuous f_back)

This would prevent the user's confusion in future reads.

---

## User's Three Questions Answered

**Q1: What does f_back mean?**
A: Continuous back-leakage fraction. Different values for different transitions.

**Q2: 2D death → 3D DM?**
A: YES, but as **100% pulsed return at death**, NOT as f_back (which is continuous while-alive).

**Q3: Why 10⁻⁸⁵? Isn't that for 4D→3D DE?**
A: **YES, EXACTLY.** You're correct. 10⁻⁸⁵ is specifically the 3+1D→4D leakage rate that explains DE (68%). It's NOT for 2D→3D DM. The framework's language was confusing, but the math is right.

---

**File created**: June 19, 2026 (v3.5.7 audit)
**Last modified**: June 19, 2026
**Commit**: `cb24056` (this commit)
**Location**: `paper/legacy/v357_f_back_clarification.md`