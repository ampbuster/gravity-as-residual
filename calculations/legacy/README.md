# Legacy Calculations (Superseded by v3.1.2-final)

This directory contains calculation scripts that were **superseded** by v3.1.2-final work. They are preserved for historical reference and to show the development path of the framework.

## v3.1.2 superseded files

| File | Status | Reason for move to legacy |
|---|---|---|
| `v31_scenario_B.py` | REJECTED (kept for historical reference) | Scenario B adopted M_Pl,4 = 1.22×10¹⁹ GeV (standard 4D Planck). User pushed back: "3D != 4D". Replaced by Scenario X (M_Pl,4D = 887 GeV, 4D BULK Planck, brane-world). |
| `v31_f_back_only_3d_to_4d.py` | SUPERSEDED (v3.1.1) | v3.1.1 claimed f_DE = 10⁻⁸⁵ ONLY makes sense as 3D-to-4D leakage. v3.1.2 unifies: f_back = (M_Pl,N/E_event)^α is universal at EVERY dimensional transition (different M_Pl,N at each level). |
| `v31_proper_closed_loop.py` | SUPERSEDED (v3.1.1-final) | v3.1.1-final framed closed loop as 3D-to-4D leakage (frame-consistent). v3.1.2 §3.71 generalizes: closed loop applies at BOTH 2D→3D AND 3D→4D. |
| `v31_F_p_consistency.py` | SUPERSEDED (v3.1.1) | L100 F_p(z) Hill function check from v3.1.1. F_p is still a phenomenological fit (L100 OPEN), not a derivation. This calculation verified consistency, not derivation. |
| `v31_fp_z_derivation.py` | REVERTED (v3.1.2) | Attempted to derive F_p(z) from cone depth framing. REVERTED in v3.1.2 (v10 was wrong, but the result was suggestive; left as is to keep L100 OPEN). |

## v3.1.2 CURRENT files (in `calculations/`)

- `v31_closed_loop_fback.py` — Closed-loop formula derivation (universal at every transition)
- `v31_scenario_X.py` — Scenario X verification (current adopted)
- `v31_multi_universe_alpha.py` — Multi-universe picture (4D-galaxy collision picture, v3.1.2)

## Why keep legacy files?

The v3.1.2-final framework is the result of multiple iterations. Some calculations were:
1. **REJECTED** because empirical evidence contradicted them (e.g., α = 1.258 fails 13/14 events)
2. **SUPERSEDED** because the framework evolved (e.g., "f_back only 3D→4D" → "f_back universal")
3. **REVERTED** because the assumption was wrong but informative (e.g., F_p cone depth attempt)

Keeping these files shows the development path and prevents repeating past mistakes.

## v3.1.2-final key corrections (the reason for moving these to legacy)

1. **AGE vs LIFETIME distinct**: 13.8 Gyr is universe AGE, predicted total LIFETIME ~10³⁰ yr
2. **FRAME OF REFERENCE distinct**: M^α law gives apparent durations in lower-D frame, 4D event proper duration ~10⁻²⁰ s
3. **SCENARIO X ADOPTED**: M_Pl,4D = 887 GeV (4D BULK Planck, brane-world), 3D≠4D
4. **α = 1.258 REJECTED**: 14-event M^1.29 fit requires α = 1.289 (α_true = 1.258 fails 13/14 events)
5. **Sub-universe = 4D-galaxy collision**: N_sub = 300 (not 3×10¹² from multi-universe = galaxy count)
