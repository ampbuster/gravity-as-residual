# LEGACY: v2.x-v3.2 Hill Function F_p Framework (DROPPED in v3.3+)

**Status**: This file documents the OLD Hill function framework for DM dynamics that was **DROPPED in v3.3** (per user critique, 6 times, commit 910a167, L100). The current framework uses **bilateral cascade** with **f_leak = H_0** as new principle (Approach A1, §7.4.20).

## What Was Dropped

### The Hill Function F_p(z)

The OLD framework had a smooth Hill function describing the fraction of DM that is primordial (from 4D event) vs cumulative (from 3+1D events over cosmic history):

$$F_p(z) = 0.9993 + 0.0007 \cdot \frac{z^2}{z_{half}^2 + z^2}$$

With:
- $z_{half} = 3$ (transition redshift)
- $F_p(z=0) = 0.9993$ → 99.93% primordial at z=0
- $F_p(z=3) = 0.85$ → 50% transition
- $F_p(z=\infty) = 1.0$ → 100% primordial at high z

This was a **Hill function n=2** with calibrated $z_{half}$.

### Why It Was Dropped

User catch (L100, v3.2):
> "F_p(z) framework is broken"

**Reasons**:
1. Required $F_p(0) = 0.9993$ which is OUTDATED — current model uses 70% primordial at z=0
2. Inconsistent with v3.3 bilateral cascade (no continuous DM leak)
3. Conflicted with AGC 114905 and KKR 25 observations
4. Multiple arbitrary parameters ($z_{half}$, Hill coefficients)
5. No clean derivation

### Current Framework (v3.5.9+ A1)

The framework now uses:
- **Bilateral cascade**: 100% DM pulsed at 2D universe death, no continuous leak
- **f_leak = H_0** as new framework principle (post-Friedmann)
- **DM steady state**: M_DM = R_add / f_leak = 27% × ρ_crit
- **τ_DM = 14.5 Gyr** (just over universe age)
- **Universe at 95.1% of DM lifetime**

NO Hill function, NO primordial/cumulative split.

## Legacy Formulas (DO NOT USE)

These formulas are in the current paper's body but are LEGACY/OUTDATED. They were kept for historical context but should NOT be used in current calculations:

- $F_p(0) = 0.9993$ (was 99.93% primordial)
- $F_p(z) = 0.9993 + 0.0007 \cdot z^2/(z_{half}^2 + z^2)$ (Hill n=2, $z_{half}=3$)
- $F_{cum}(z) = 1 - F_p(z)$ (cumulative fraction)
- 99.93% primordial at z=0 (OUTDATED, current is 70%)
- 0.07% cumulative DM (OUTDATED)

These appear in:
- `paper/markdown/01_executive_summary.md` (line ~24, ~32, ~63)
- `paper/markdown/02_glossary.md` (line ~10 matches)
- `paper/markdown/03a_relations.md` (line ~18 matches)
- `paper/markdown/03b_predictions.md` (line ~13 matches)
- `paper/markdown/03c_lagrangian.md` (line ~1 match)
- `paper/markdown/04_predictions.md` (line ~5+ matches)
- `paper/markdown/04_tests.md` (line ~5 matches)
- `paper/markdown/06_limitations.md` (line ~4 matches)
- `paper/markdown/07_conclusion.md` (line ~3+ matches)
- `paper/markdown/11_testable.md` (line ~5 matches)
- `paper/markdown/12_galaxy_zoo.md` (line ~5 matches)
- `paper/markdown/13_cmb_gap.md` (line ~1 match)
- `paper/markdown/14_appendix.md` (line ~1 match)

## Other Legacy Content (Moved Here)

### §3.67 Scaled-Leak Formula (REPLACED in v3.5.9+ A1)

OLD formula: $f_{\rm leak} = \alpha \times f_{\rm back,3+1D} \times \gamma_{\rm 4D}^{1/\alpha^2}$

With v3.3 era $\gamma_{\rm 4D} = 1.29 \times 10^{64}$, this gave $f_{\rm leak} = 2.40 \times 10^{-18}$ /s ≈ H_0 (1.4% match).

**Status**: REPLACED by f_leak = H_0 as new principle in Approach A1 (v3.5.9+).

The 1.4% match becomes a "striking coincidence" rather than a derivation.

### τ_3D,apparent History

- v3.3 era: $\tau_{\rm 3D,apparent} = 9.10 \times 10^{124}$ yr (with γ_4D = 5.93×10⁹⁰)
- Path B2 (rejected): $\tau_{\rm 3D,apparent} = 1.69 \times 10^{98}$ yr (with γ_4D = 1.12×10⁶⁴)
- **Current (A1)**: $\tau_{\rm 3D,apparent} = 8.95 \times 10^{124}$ yr (γ_4D = 5.93×10⁹⁰ REINSTATED)

### 9D = v_Higgs Hypothesis (DROPPED)

OLD: 9D = $v_{\rm Higgs}$ = 246 GeV (hypothesized as intermediate dimension)

**Status**: DROPPED in v3.5.8+ (user correction, doesn't add to framework).

### 12 Weyl Fermions = 12 SYK Majoranas (BREAKTHROUGH L308u)

Connection: SM 3 generations × 4 Weyl = 12 Weyl = 12 SYK Majoranas (if N=12)

This is CURRENT (v3.5.9+ L308u), NOT legacy. It's the breakthrough that unifies "12" across the cascade.

