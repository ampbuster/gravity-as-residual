#!/usr/bin/env python3
"""
v27_paper_inconsistency_audit.py
=================================
Audit of the cascade paper (paper/paper.md) for internal inconsistencies.

This audit was performed in the v27 session (2026-06-15) in response to
user request "find more inconsistencies in the paper."

INCONSISTENCIES FOUND:

1. CRITICAL: f_proj notation overload
   f_proj is used for two different concepts with very different values.

2. MEDIUM: 5/27 inner split dropped but "universal split" still claimed
   v2.7.1 dropped the 5:27 inner split (Limitation 17, FAILED earlier derivation)
   But §2.6 still claims "the SAME 5%/27%/68% energy budget split applies at
   each of the two cascade levels" (line 506) — this is the SAME dropped postulate
   in different language.

3. MEDIUM: F_p = 0.7 is "MARGINAL" in the table, but "GOOD" in the text
   §4.48 table (line 3211-3219): F_p = 0.7 → r(z=6) = 0.57 → MARGINAL
   §4.48 text (line 3221): "F_p > 0.3 (marginal) to F_p > 0.7 (good)"
   The text says F_p > 0.7 is "good" but the table shows F_p = 0.7 is MARGINAL.

4. MEDIUM: τ_2D = 33 s for SN vs α = 1.29
   Paper claims SN τ_2D = 33 s and α = 1.29. Formula gives 32 s, not 33 s.
   (Within rounding error, but if exact calibration: α should be 1.290, not 1.29)

5. CONCEPTUAL: τ_2D applied uniformly to all events
   Paper applies τ_2D formula to all events. But §4.48 has F_p = 0.7 PRIMORDIAL
   events (not SN), and the per-event energy for primordial is unspecified.
   The "33 s" calibration is for SN, not for primordial events.

6. CONCEPTUAL: §4.48 "primordial" event energy is unspecified
   §4.48 specifies R_p (primordial rate in events/s/m³) but not the per-event
   energy E_primordial. The growth factor G, lifetime τ_2D, and cumulative
   energy all depend on E_primordial, which is a free parameter.

7. CONCEPTUAL: f_back = 10^-85 vs 32/68 split
   f_back = 10^-85 (line 728) is for the cosmological constant, not the
   32/68 split (line 511, 529, 585). These are different concepts but
   are sometimes conflated in the paper's discussion.

8. PARAMETER: f_active = 0.05 (RAR fit) vs F_p = 0.7 (primordial)
   These are different concepts but the paper doesn't always distinguish:
   - f_active = fraction of cumulative 2D universe back-projection that is active
   - F_p = fraction of DM from primordial (vs stellar) Lagrangian
   The 0.05 vs 0.7 difference is 14x, but they measure different things.
"""

import math
import numpy as np


def main():
    print("="*80)
    print("PAPER INCONSISTENCY AUDIT")
    print("="*80)
    print()

    print("="*80)
    print("INCONSISTENCY 1 (CRITICAL): f_proj notation overload")
    print("="*80)
    print()
    print("The symbol 'f_proj' is used in the paper for TWO different concepts:")
    print()
    print("  USE 1: 32%/68% split (line 2484, 2486, 2539)")
    print("    'f_proj = 0.32 (the cascade's 32%/68% split between projected and antigravity)'")
    print("    'α ~ 0.03-0.3 gives f_proj ≈ 0.32'")
    print()
    print("  USE 2: Back-projection efficiency (line 5163)")
    print("    'The 2 free parameters (μ, m_3+1D) plus the calibrated f_proj'")
    print("    Here f_proj is implied to be a SMALL number (calibrated)")
    print()
    print("  These are very different numbers (0.32 vs ~10^-10)!")
    print()
    print("  Fix: use f_split for the 32/68 ratio, f_proj for the back-projection")
    print("  efficiency. Or rename one of them.")
    print()

    print("="*80)
    print("INCONSISTENCY 2 (MEDIUM): 5/27 inner split dropped, 'universal split' claimed")
    print("="*80)
    print()
    print("  v2.7.1 (line 3) explicitly DROPPED the 5/27 inner split:")
    print("    'The 5:27 inner split (5% active 2D universes vs 27% cumulative deaths)")
    print("     is dropped in v2.7.1 as a separate postulate that conflicts with")
    print("     the empirical 33 s lifetime'")
    print()
    print("  But §2.6 line 506 still claims the 5/27/68 split is 'universal':")
    print("    'the SAME 5%/27%/68% energy budget split applies at EACH of the two")
    print("     cascade levels (3+1D and 2D), by the scale-invariance principle'")
    print()
    print("  This is the SAME dropped postulate in different language!")
    print()
    print("  Fix: clarify that the 5/27/68 is OBSERVATIONAL 3+1D data (§2.6+)")
    print("  not a universal split. The 'universal' claim was tied to the dropped")
    print("  5/27 inner split.")
    print()

    print("="*80)
    print("INCONSISTENCY 3 (MEDIUM): F_p = 0.7 'MARGINAL' vs 'GOOD'")
    print("="*80)
    print()
    print("  §4.48 table (line 3211-3219):")
    print("    F_p = 0.70  r(z=6) = 0.57  MARGINAL")
    print("    F_p = 0.90  r(z=6) = 0.68  MARGINAL")
    print("    F_p = 1.00  r(z=6) = 0.73  MATCHES")
    print()
    print("  §4.48 text (line 3221):")
    print("    'F_p > 0.3 (marginal) to F_p > 0.7 (good) to satisfy both constraints'")
    print()
    print("  DISCREPANCY: text says F_p = 0.7 is 'good' but the table says MARGINAL.")
    print("  Only F_p = 1.0 is MATCHES. F_p = 0.7 is just barely better than MARGINAL.")
    print()
    print("  Fix: clarify that F_p = 0.7 is 'best compromise' not 'good'.")
    print()

    print("="*80)
    print("INCONSISTENCY 4 (MINOR): τ_2D = 33 s vs α = 1.29 (within rounding)")
    print("="*80)
    print()
    t_Pl = 5.39e-44
    E_SN = 1e44
    E_Pl = 1.96e9
    alpha_paper = 1.29
    tau = t_Pl * (E_SN / E_Pl) ** alpha_paper
    print(f"  Paper claim: SN τ_2D = 33 s, α = 1.29")
    print(f"  Formula gives τ_2D = {tau:.3f} s")
    print()
    print(f"  For exact 33 s: required α = {np.log(33/t_Pl) / np.log(E_SN/E_Pl):.6f}")
    print()
    print("  Within rounding, but the paper presents α = 1.29 as the calibration")
    print("  (the EXACT value giving 33 s would be 1.2903...)")
    print()

    print("="*80)
    print("INCONSISTENCY 5 (CONCEPTUAL): τ_2D applied uniformly to all events")
    print("="*80)
    print()
    print("  The paper applies the energy-scaling rule τ_2D = t_Pl * (E/E_Pl)^α")
    print("  to all events (LHC, SN, hypernova, AGN, etc.) uniformly.")
    print()
    print("  But §4.48 has F_p = 0.7 PRIMORDIAL events (not SN).")
    print("  For primordial events, the per-event energy is DIFFERENT from SN.")
    print("  The 33 s calibration is specifically for SN events.")
    print()
    print("  For primordial 2D universes, the per-event energy is unspecified")
    print("  (see Inconsistency 6). The lifetime of primordial 2D universes")
    print("  could be very different from SN's 33 s.")
    print()
    print("  Fix: clarify that the 33 s calibration is for SN only, and the")
    print("  primordial 2D universe lifetime is a free parameter (or derived")
    print("  from the 4D event's internal dynamics).")
    print()

    print("="*80)
    print("INCONSISTENCY 6 (CONCEPTUAL): §4.48 'primordial' event energy unspecified")
    print("="*80)
    print()
    print("  §4.48 specifies:")
    print("    R_p = primordial rate (events per second per m^3)")
    print("    F_p = primordial fraction (~0.7)")
    print()
    print("  But UNSPECIFIED:")
    print("    E_primordial = energy per primordial event (in joules)")
    print()
    print("  The growth factor G, lifetime τ_2D, and cumulative energy all depend")
    print("  on E_primordial, which is a FREE PARAMETER in §4.48.")
    print()
    print("  Fix: add E_primordial as a free parameter in §4.48. Or derive it")
    print("  from the 4D event's dynamics.")
    print()

    print("="*80)
    print("INCONSISTENCY 7 (MINOR): f_back = 10^-85 vs 32/68 split")
    print("="*80)
    print()
    print("  f_back = 10^-85 (line 728) is the 'staying fraction' for the")
    print("  COSMOLOGICAL CONSTANT (DE), bridging the 10^85 gap between the")
    print("  cascade's raw prediction and observation.")
    print()
    print("  32/68 split (lines 511, 529, 585) is the PROJECTION RATIO")
    print("  (32% of 4D event energy projects to 3+1D, 68% stays as 4D antigravity).")
    print()
    print("  These are different concepts:")
    print("    - f_back: small fraction of un-cancelled antigravity that becomes DE")
    print("    - 32/68: the projection ratio (how much 4D energy goes to 3+1D vs stays)")
    print()
    print("  The paper sometimes conflates them, but they're distinct concepts.")
    print()

    print("="*80)
    print("INCONSISTENCY 8 (PARAMETER): f_active vs F_p")
    print("="*80)
    print()
    print("  Two different 'fractions' in the cascade:")
    print()
    print("  f_active = 0.05 (MCMC fit, line 23):")
    print("    Fraction of cumulative 2D universe back-projection that is 'active'")
    print("    (currently alive). Empirical fit, not derived.")
    print()
    print("  F_p = 0.7 (§4.48, line 3185):")
    print("    Fraction of DM from primordial Lagrangian (vs stellar)")
    print("    Trial-and-error to match high-z UV LF.")
    print()
    print("  These are DIFFERENT quantities:")
    print("    f_active = (active 2D universe population) / (total cumulative)")
    print("    F_p = (primordial DM contribution) / (total DM)")
    print()
    print("  They could be related (active is mostly stellar-created 2D universes,")
    print("  and stellar F_s = 0.3 of total DM), but the paper doesn't make this")
    print("  connection explicit.")
    print()
    print("  Connection:")
    print("    f_active × F_s = 0.05 × 0.3 = 0.015 (active stellar 2D universes)")
    print("    f_active × F_p = 0.05 × 0.7 = 0.035 (active primordial 2D universes)")
    print("    These are not constrained by current data, so the relationship is unclear.")
    print()

    print("="*80)
    print("SUMMARY")
    print("="*80)
    print()
    print("CRITICAL:")
    print("  1. f_proj notation overload (0.32 vs ~10^-10)")
    print()
    print("MEDIUM:")
    print("  2. 5/27 inner split dropped but 'universal split' still claimed")
    print("  3. F_p = 0.7 'MARGINAL' in table but 'good' in text")
    print()
    print("MINOR:")
    print("  4. τ_2D = 33 s vs α = 1.29 (rounding error)")
    print("  7. f_back = 10^-85 vs 32/68 split (different concepts)")
    print()
    print("CONCEPTUAL:")
    print("  5. τ_2D applied uniformly to all events (primordial events are different)")
    print("  6. §4.48 'primordial' event energy unspecified (free parameter)")
    print("  8. f_active vs F_p (different fractions, not always distinguished)")
    print()
    print("ACTION ITEMS:")
    print("  1. Rename f_proj (USE 1) to f_split or f_attractive")
    print("  2. Soften 'universal split' claim in §2.6 to be consistent with v2.7.1")
    print("  3. Update §4.48 text to say F_p ~ 0.7 is 'best compromise' not 'good'")
    print("  4. Specify E_primordial in §4.48 (or note as free parameter)")
    print("  5. Clarify that τ_2D = 33 s is SN-specific, not universal")


if __name__ == "__main__":
    main()
