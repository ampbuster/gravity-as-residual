# Build Tools for Math Cleanup Pipeline

This directory contains scripts that clean up broken math notation patterns
introduced by hand-editing or auto-conversion. Run them in order, with
`fix_math_spacing.py` LAST (it's sensitive to $ placement).

## Pipeline Order (CRITICAL)

```
# STRUCTURAL FIXES (run first - modify LaTeX structure)
Step 1: wrap_math_vars.py         (wrap M_Pl, E_4D, v_Higgs, etc. in $...$)
Step 2: wrap_powers_of_10.py      (convert 10^N to $10^{N}$)
Step 3: e_to_math.py              (convert 1.5e10 to $1.5 \times 10^{10}$)
Step 4: greek_to_latex.py         (convert α, β, γ to $\alpha$, $\beta$, $\gamma$)
Step 5: fix_greek_subscripts.py   (fix $\tau$_obs → $\tau_{\rm obs}$ broken patterns)
Step 6: fix_broken_markdown.py    (fix ** $math, ( $math, $M_{dyn}/$M_b, etc.)

# ADJACENT MATH CLEANUP (run after structural fixes)
Step 7: combine_adjacent_math.py  (combine "$X$ $Y$" into "$X Y$")

# SPACING FIX (ALWAYS RUN LAST)
Step 8: fix_math_spacing.py       (fix spacing inside math, sensitive to $ placement)
```

## Why order matters

- `fix_math_spacing.py` is **sensitive to $ placement**. Run it LAST so
  earlier fixes don't add new spacing issues inside newly-wrapped math.
- `combine_adjacent_math.py` should run AFTER `fix_broken_markdown.py`
  because the latter may merge adjacent math blocks differently.
- `fix_greek_subscripts.py` runs AFTER `greek_to_latex.py` because the
  latter wraps Greek in math but leaves subscript outside (creates
  `$\tau$_obs` from `τ_obs`). This is a "broken-from-prior-fix" pattern.

## fix_broken_markdown.py patterns (1-23)

1. `** $math` → `**$math` (bold + space + math)
2. `( $math` → `($math` (open paren + space + math)
3. `[ $math` → `[$math` (open bracket, less common)
4. `- $math` at start of line (preserve, clean space)
5. `$X\times$ 10^{N}` → `$X\times 10^{N}$` (split math block)
6. `**NUMBER × 10^N**` → `**$NUMBER \times 10^{-N}$**` (bold Unicode)
7. `**10⁻N suffix**` → `**$10^{-N}$ suffix**` (bold Unicode 10^N + text)
8. `$\Omega$DM` → `$\Omega_{\rm DM}$` (DM as subscript)
9. `$$$...$` → `$$...$$` (triple dollar → display math)
10. `$\Lambda$CDM` → `$\Lambda{\rm CDM}$` (CDM in roman)
11. `$X/$Y` → `$X/Y$` (slash between adjacent math, with chain handling)
12. `$X^{$Y^Z}$` → `$X^{Y^Z}$` (nested math in superscript)
13. `X^$Y$` → `$X^{Y}$` (sup symbol before math)
14. `\times $X$` → `\times X$` (remove inner math delimiters)
15. `\sim $X$` → `\sim X$` (remove inner math delimiters)
16. `1/(2$\alpha$)` → `$1/(2\alpha)$` (wrap whole in math)
17. `c/\alpha$` → `$c/\alpha$` (wrap whole in math, lookbehind for $)
18. `(1/2$\alpha$)` → `$(1/(2\alpha))$` (table cells, wrap whole in math)
19b. `)^$\alpha$` → `)$^{\alpha}$` (caret outside math, preserve $ count)
20b. `)^($X$)` → `)$^{X}$` (nested parens around math, preserve $ count)
21. `E_Pl,N` → `$E_{\rm Pl,N}$` (wrap in math, lookbehind for $)
22. `digit$\math$` → `$digit\math$` (e.g., `4$\pi$` → `$4\pi$`, `1$\sigma$` → `$1\sigma$`)
23. e-notation (4e9, 1.5e-43) → `$4 \times 10^{9}$` etc. (works in tables too)

## Common Issues Table

| Before | After |
|--------|-------|
| `** $\alpha$ = 1.258` | `**$\alpha$ = 1.258` |
| `( $M_{\rm 2D}$ is...` | `($M_{\rm 2D}$ is...` |
| `ratio ( $\tau$_pred...)` | `ratio ($\tau_{\rm pred}$...)` |
| `$1.6\times$ 10⁻⁴⁵` | `$1.6\times 10^{-45}$` |
| `$\Omega$DM ≈ 0.27` | `$\Omega_{\rm DM} \approx 0.27$` |
| `$$$N_p = ...$` | `$$N_p = ...$$` |
| `$\Lambda$CDM` | `$\Lambda{\rm CDM}$` |
| `$M_{dyn}/$M_b` | `$M_{dyn}/M_b$` |
| `$10^{$10^{1} }$` | `$10^{10^{1}}$` |

## Usage

Run the full pipeline:
```bash
python3 paper/build_tools/cleanup_math.py
```

Run individual scripts:
```bash
python3 paper/build_tools/fix_broken_markdown.py              # All files
python3 paper/build_tools/fix_broken_markdown.py README.md    # Single file
```

## Audit Scripts (read-only, no modifications)

Two audit scripts find issues without modifying files. Run them to check
for issues introduced by edits or auto-conversion:

```bash
python3 paper/build_tools/audit_units.py              # Find tables with bare-number cells
python3 paper/build_tools/audit_broken_math.py        # Find broken math patterns
```

**`audit_units.py`** (173 lines): Finds table cells where the header has
a unit but the cell value is bare number (e.g., `33` instead of `33 s`).
Skips dimensionless ratios (M_dyn/M_b), counts (N_sub), versions.

**`audit_broken_math.py`** (128 lines): Finds:
- Pattern 22 collateral damage (`X.$\math$` orphan `$`)
- Unbalanced `{` in math blocks
- Triple `$$$` instead of `$$`
- Other structural issues

**False positives**: Both scripts use heuristic filters and may report
some legitimate patterns. Always verify the line context before fixing.

## Cache Warning

If you modify a script, clear Python's bytecode cache:
```bash
rm -rf paper/build_tools/__pycache__
```

Otherwise Python may load the OLD compiled version.
