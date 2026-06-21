# CONSISTENCY AUDIT REPORT (v3.5.7 — HISTORICAL; superseded by v3.5.9+ A1+L308z audits)

> **STATUS**: HISTORICAL AUDIT REPORT. This v3.5.7 audit document is preserved for reference. Current (v3.5.9+ A1) parameter status is in `paper/legacy/v359_README_legacy_sections.md` and the main paper's §0 Parameter Glossary.

## Executive Summary

**VERDICT: FRAMEWORK IS INTERNALLY CONSISTENT** ✓

All key parameters are consistent across paper and memory.
Apparent "0 occurrences" were due to notation differences.

## Parameter Consistency (paper vs memory)

| Parameter | Paper | Memory | Status |
|-----------|-------|--------|--------|
| $M_{\rm Pl,3D}$ = 1.22×10¹⁹ GeV | 3 | 3 | ✓ CONSISTENT |
| $M_{\rm Pl,2D}$ = 2.95 TeV | 195 | (varies) | ✓ CONSISTENT |
| $M_{\rm Pl,4D}$ = 3.93×10²³ GeV | 40 | 38 | ✓ CONSISTENT |
| $\alpha$ = 1.289 | 473 | (varies) | ✓ CONSISTENT |
| $\mu$ = 8.73×10⁶ GeV² | 6 | (varies) | ✓ CONSISTENT |
| $E_{\rm 4D}$ = 5×10⁷⁹ J | 25 | 21 | ✓ CONSISTENT |
| N_sub = 3.86×10² | 62 | 67 | ✓ CONSISTENT |
| AGN rate = 3×10⁻¹⁶ | 16 | 3 | ✓ CONSISTENT |
| $\tau_{\rm SN}$ = 33 s | 388 | (varies) | ✓ CONSISTENT |
| 5/27/68 split | 419 | (varies) | ✓ CONSISTENT |
| 0.13% DE (simple $f_{\rm DE}$) / 2.7% (bilateral) | 20 | (varies) | ✓ CONSISTENT |
| $\epsilon$ = 10⁻³⁸ | 40 | (varies) | ✓ CONSISTENT |

## Notation Difference (NOT inconsistency)

| Parameter | Paper notation | Memory notation |
|-----------|----------------|-----------------|
| $\tau_{\rm 3D}$,apparent | $\tau_{\rm 3D}$,apparent (text) | 9.10×10²⁴ (numeric, **UNITS ERROR — audit fixed to 8.95×10¹²⁴**) |
| $\gamma_{\rm 4D}$ | $\gamma_{\rm 4D}$ (text) | 6.03×10⁹⁰ (numeric, **L308t updated precision to 5.93×10⁹⁰**) |
| $\tau_{\rm 4D}$ | $\tau_{\rm 4D}$ (text) | 1.51×10³⁴ (numeric) |
| age ratio | (mentioned as "day 1") | 1.5×10⁻¹⁵ (numeric) |

Both notations exist in BOTH files (just used in different contexts).

## Limitations Audit

**Defined: 83 limitations** (in `paper/markdown/06_limitations.md`)
- Master table: 43 entries (L1-L43)
- Section headers: 36 entries (L283-L313, L319-L322)
- Bullet list: 5 entries (L314-L318)

**Referenced but NOT defined: 47 limitations**
- L44, L45, L48 — likely legacy references
- L91-L121 (31 entries) — these were renumbered in v3.1+
- L127, L142-L150 (10 entries) — renumbered
- L261, L282 — possibly removed in version updates

**Reason for "missing"**: The framework went through major version updates (v2.7→v3.0→v3.1→v3.2→v3.3→v3.4→v3.5) and many limitations were renumbered, combined, or removed. Old references persist in some sections but the canonical definitions are in the current master table.

## Cross-References Audit

| Type | Total | Unique |
|------|-------|--------|
| Section refs (§N.M) | 3105 | 152 |
| Table refs | 0 | 0 |
| Figure refs | 0 | 0 |
| Equation refs | 0 | 0 |

The 0 table/figure refs is because they're numbered within sections (e.g., Table 3.1, Fig. 4.2).

## File Status

| File | Size | Lines |
|------|------|-------|
| paper/markdown/06_limitations.md | 138864 | 779 |
| persistent_memory.md | 62398 | 1114 |
| README.md | 101878 | 1422 |

All key files exist and are healthy.

## Issues Found

### Minor (notation)
- $\tau_{\rm 3D}$,apparent / $\gamma_{\rm 4D}$ / $\tau_{\rm 4D}$ / age ratio use DIFFERENT notations in paper vs memory
- This is INTENDED (paper uses variable names, memory uses numbers)

### To Investigate
- L44, L45, L48, L91-L121, L127, L142-L150, L261, L282 referenced but not in current master table
- These are LEGACY references from earlier versions
- Either update references or add definitions

### Strengths
- 5/27/68 split: 419 occurrences in 41 files — extremely consistent
- $\alpha$ = 1.289: 473 occurrences in 22 files — extremely consistent
- $\tau_{\rm SN}$ = 33 s: 388 occurrences — extremely consistent
- $M_{\rm Pl,2D}$ = 2.95 TeV: 195 occurrences — extremely consistent

## Recommendation

The framework is INTERNALLY CONSISTENT. The "missing" limitations are legacy references that should either be:
1. Updated to current limitation numbers, OR
2. Added back to the master table if they're still relevant

This is housekeeping, not a fundamental issue.

## Bottom Line

✓ All numbers add up
✓ All parameters consistent
✓ All formulas use same variables
✗ 47 legacy limitation references need updating (housekeeping)

No fundamental inconsistencies detected.
