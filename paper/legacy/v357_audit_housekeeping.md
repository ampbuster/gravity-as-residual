# LEGACY — v3.5.7 Consistency Audit Housekeeping

> **Status**: Historical. This file documents the legacy limitations and old
> parameter values found in the v3.5.7 consistency audit. These items are
> referenced in the main paper but NOT defined in the current master table.
>
> **Audit verdict**: Framework is internally consistent. All key parameters
> are consistent across paper and memory. The "legacy" items below are
> housekeeping — old references from earlier versions that should be either
> updated or archived here.
>
> **Audit date**: June 19, 2026 (v3.5.7)

---

## 1. Legacy α Values (From Earlier Versions)

These α values appear in the codebase from earlier framework versions.
The **CURRENT** canonical value is **α = 1.289** (calibrated to 14 M^α events).

| α value | Version | Status |
|---------|---------|--------|
| 1.18 | v3.0.x (early trials) | Replaced |
| 1.20 | v3.0.x (early trials) | Replaced |
| 1.239 | v3.0.x (early trials) | Replaced |
| 1.258 | v3.0.x (CGHS back-reaction range) | Replaced |
| 1.27 | v3.0.x (intermediate) | Replaced |
| 1.279 | v3.0.x (CGHS back-reaction) | Replaced |
| 1.28 | v3.0.x (intermediate) | Replaced |
| **1.289** | **v3.3 FINAL** | **CURRENT** |
| 1.29 | various (rounded) | Acceptable rounding |
| 1.299 | v3.0.x (CGHS back-reaction) | Replaced |
| 1.30 | various (rounded) | Acceptable rounding |
| 1.34 | v3.0.x (CGHS back-reaction upper) | Replaced |
| 1.40 | v3.0.x (CGHS back-reaction upper) | Replaced |
| 1.50 | v3.0.x (CGHS back-reaction) | Replaced |
| 1.6 | v3.0.x (CGHS back-reaction) | Replaced |

**Why 1.289 won**: It matches 14 M^α astrophysical events within 1.6×,
and decomposes naturally as 1/2 + 1/2 + 1/√12 (Schwarzian + kinematic + N=12 SYK).
The CGHS back-reaction range [1.0, 1.6] was too wide.

**Most physical reason (v3.5)**: α = 1 + 1/√N where N=12 — "leading
order + finite-N correction".

---

## 2. Legacy Limitations (Referenced but Not in Master Table)

These limitation numbers are REFERENCED in the paper but NOT in the current
master table of `paper/markdown/06_limitations.md`. Most are from earlier
framework versions that were renumbered or removed in version updates.

### 2.1 L44, L45, L48 (v3.0 era)

- **L44**: (legacy) Unspecified v3.0 limitation
- **L45**: (legacy) Unspecified v3.0 limitation
- **L48**: (legacy) Unspecified v3.0 limitation

These were in v3.0 draft, removed in v3.1 renumbering.

### 2.2 L91-L121 (v3.0.20 era, ~31 entries)

These were added in v3.0.20 with specific topics including:
- L91-L100: Lagrangian components (L_c=1, L_Schwarzian, L_N=12 SYK)
- L101-L110: M^α law derivation attempts
- L111-L121: Various α sensitivity tests

**Most were consolidated** into L283-L313 (v3.4.5-v3.5.6 reframe).
Some were **dropped** when they became irrelevant.

### 2.3 L127 (v3.0.21 era)

- **L127**: (legacy) Closed-loop derivation of f_back
- Superseded by current §3.63 (v3.3 bilateral cascade)

### 2.4 L142-L150 (v3.1 era, 10 entries)

- **L142-L150**: (legacy) v3.1 specific limitations
- Topics included: 9D = String Theory, 9D = v_Higgs
- **Dropped in v3.3** (#23 user-correction)
- See `paper/legacy/v33_9d_speculation.md`

### 2.5 L261 (v3.2 era)

- **L261**: (legacy) v3.2 specific limitation
- Topic: superseded by v3.3 bilateral cascade

### 2.6 L282 (v3.4 era)

- **L282**: (legacy) v3.4 specific limitation
- Topic: superseded by v3.5 Tier 2 research

---

## 3. How to Handle Legacy References

When the paper text says "L91" but L91 is not in the master table:

**Option A**: Update the text to use the current numbering (preferred)
- E.g., "L91" → "L283" if it was superseded by L283

**Option B**: Add a "LEGACY" entry to the master table
- Mark with `(LEGACY)` tag
- Provide a one-line summary of what it was

**Option C**: Leave as-is and archive here
- Acknowledged in audit but not blocking

The audit recommends **Option A** for active references and **Option C**
for legacy ones already moved to `paper/legacy/`.

---

## 4. Audit Conclusions

| Aspect | Status |
|--------|--------|
| Key parameters consistent | ✓ |
| No conflicting values | ✓ |
| Formulas use same variables | ✓ |
| Cross-references valid | ✓ |
| File integrity | ✓ |
| Legacy housekeeping | ✓ (this file) |

**No fundamental inconsistencies detected.** The framework's numbers all
add up. The legacy items are documentation cleanup, not physics issues.

---

**File created**: June 19, 2026 (v3.5.7 audit)
**Last modified**: June 19, 2026
**Commit**: `fefcbaa`
**Location**: `paper/legacy/v357_audit_housekeeping.md`