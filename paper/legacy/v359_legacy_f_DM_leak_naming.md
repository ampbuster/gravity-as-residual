# LEGACY — f_DM,leak Naming Convention (v3.5.7+ — v3.5.9+ A1, REPLACED v3.5.9+ A2)

> **Status**: Superseded. The frame-dependent naming `f_DM,leak` was
> replaced with the frame-neutral, transition-explicit naming
> `f_leak,2D→3D` in v3.5.9+ A2 (L308ax, 2026-06-22).

---

## The Issue (caught by user, 2026-06-22)

User insight: "f_leak from 2d->3d seen from 2d = f_DM,leak from 2d->3d
seen from 3d" — the previous naming was frame-dependent.

| Same physical process | 2D's frame | 3+1D's frame |
|---|---|---|
| Leakage at 2D→3D | "I'm leaking to 3D" = `f_leak` | "I'm gaining DM from 2D" = `f_DM,leak` |
| Leakage at 3+1D→4D | "I'm leaking to 4D" = `f_leak` | "I'm gaining DM from 3D" = `f_DM,leak` |

The "DM" prefix made sense only from the 3+1D observer's view.

## The Refactor (v3.5.9+ A2, L308ax)

| Old name (frame-dependent) | New name (frame-neutral) |
|---|---|
| `f_DM,leak` | `f_leak,2D→3D` |
| `f_leak` (= H_0) | `f_leak,3D→4D` |

The new names are transition-explicit (which cascade transition) and
frame-neutral (any observer can read them the same way).

## Key Simplification

The "natural" cascade leak formula `(M_Pl,parent/E)^α` gives TINY values
at BOTH transitions:
- `f_leak,2D→3D` (natural) = 1.6×10⁻⁴⁵ (88 orders below death pulse)
- `f_leak,3D→4D` (natural) = ~10⁻⁸⁶ (67 orders below H_0)

The 27-order gap at the 3+1D→4D transition tells us `f_leak = H_0` is a
**calibrated stability principle**, not a natural cascade phenomenon.

Both natural leaks are dropped as negligible. The only significant
leakage is `f_leak,3D→4D = H_0` (calibrated, prevents DM over-accumulation).

## Files Changed (v3.5.9+ A2)

- `paper/markdown/02_glossary.md`: §0.5 updated to 4-flow table + L308av note
- `paper/markdown/03c_lagrangian.md`: 5 f_DM,leak → f_leak,2D→3D
- `paper/markdown/06_limitations.md`: 1 replacement + new §7.4.42b (L308ax)
- `paper/paper.md`: 9 replacements (auto-rebuild)

## Reference

- Section 7.4.42b (L308ax): Frame-Neutral Naming of Leakage Channels
- Section 0.5 in 02_glossary.md: Four flows, four names (frame-neutral)
