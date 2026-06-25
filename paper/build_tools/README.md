# Build Tools for Math Cleanup Pipeline

This directory contains the **math notation cleanup pipeline** for the SIDC
paper. The pipeline runs in a fixed order (defined in `master_pipeline.py`)
to convert plain-text math notation into proper LaTeX `$...$` math mode,
fix broken patterns, and produce a clean build.

## Master Pipeline (current state)

The full pipeline is run via:
```bash
python3 paper/build_tools/master_pipeline.py
```

It runs **18 steps** in order:

```
# 1. STRUCTURAL FIXES (source bugs that block the build)
Step 1:  fix_broken_wraps           # revert bad wrap_math_vars.py outputs
Step 2:  fix_unbalanced_dollars     # revert accidental 7457 to $
Step 3:  fix_math_spacing           # initial spacing pass

# 2. UNICODE / WRAPPING
Step 4:  wrap_unicode_powers        # wrap 10⁻⁴⁵ etc. patterns
Step 5:  inline_to_unicode          # convert simple inline LaTeX to Unicode
Step 6:  wrap_math_vars             # wrap M_Pl, E_4D, v_Higgs, etc.

# 3. POST-WRAP CLEANUP
Step 7:  fix_broken_wraps           # again, to clean up after wrap_math_vars
Step 8:  fix_math_spacing           # again, for new spacing issues
Step 9:  fix_dollar_letter_no_space # insert space after $ when followed by letter

# 4. NOTATION-SPECIFIC FIXES (the recent aggressive fixes)
Step 10: fix_unicode_greek_subscripts  # wrap α_2D, ρ_DE, etc. in $...$
Step 11: fix_letter_caret              # wrap M^N, V^4 in $...$
Step 12: fix_physics_subscripts       # wrap H_0, M_b, sigma_int, etc.
Step 13: replace_unicode_fallback      # ℓ→\ell, ⋆→\star, emoji→[OK]/[FAIL]
Step 14: fix_greek_value_patterns      # wrap ε = 6.32×10⁻³⁴ in $...$
Step 15: fix_unicode_times_powers      # wrap N × 10ⁿ patterns
Step 16: fix_subscript_vars            # wrap r_12, l_12, D_A, M_Pl,3D etc.

# 5. BUILD
Step 17: build_pdf                  # runs paper/build_pdf.sh
Step 18: audit                       # post-build verification
```

## Why order matters

- **`fix_math_spacing`** is run TWICE — once before wrapping (Step 3) and
  once after (Step 8) — because new wrapping introduces new spacing issues.
- **`fix_broken_wraps`** is run TWICE — once at the start (Step 1) to
  clean up known-bad patterns, and once after `wrap_math_vars` (Step 7)
  to clean up new broken patterns that wrapper might create.
- **`fix_subscript_vars`** runs LAST among fixers (Step 16) so it only
  wraps true plain-text patterns, not patterns already wrapped by
  earlier steps.

## Build Tools Inventory (current)

### Master / orchestration

| Script | Purpose |
|--------|---------|
| `master_pipeline.py` | Runs all 18 steps in order with build + audit |
| `cleanup_math.py` | Legacy: runs a subset of cleanup scripts in sequence |
| `audit_v2.py` | Fast audit with pre-computed math-mode state |
| `audit_broken_math.py` | Audit for various broken math patterns |
| `audit_units.py` | Audit tables for bare numbers that should have units |

### Source bug fixes (run early)

| Script | Purpose | When added |
|--------|---------|-----------|
| `fix_broken_wraps.py` | Revert bad `wrap_math_vars.py` outputs (`$f_{\rmleak}$` etc.) | L308dk |
| `fix_unbalanced_dollars.py` | Fix source bugs that break `$` balance | L308dk |
| `fix_math_spacing.py` | Two-pass math spacing fix | L308dk |

### Wrapping / Unicode conversion

| Script | Purpose | When added |
|--------|---------|-----------|
| `wrap_unicode_powers.py` | Safe wrapper for unicode power-of-10 patterns | L308dk |
| `inline_to_unicode.py` | Convert simple inline LaTeX math to Unicode | L308dk |
| `wrap_math_vars.py` | Wrap physics variables in `$...$` math mode | L308dk |
| `wrap_powers_of_10.py` | Convert `10^N` to `$10^{N}$` in body text | L308dk |
| `e_to_math.py` | Convert e-notation (1.5e10) to math form | L308dk |
| `greek_to_latex.py` | Convert Unicode Greek (α, β) to LaTeX (`\alpha`, `\beta`) | L308dk |
| `replace_unicode_chars.py` | Replace Unicode chars that don't work with DejaVu Serif | L308dk |
| `wrap_dimexpr.py` | Wrap `\dimexpr` expressions | L308dk |
| `use_linewidth.py` | Convert `\dimexpr` column specs to `\linewidth` | L308dk |

### Notation-specific fixes (the recent aggressive fixes)

| Script | What it fixes | When added |
|--------|--------------|-----------|
| `fix_dollar_letter_no_space.py` | Add space after closing `$` when followed by letter | L308dk |
| `fix_unicode_greek_subscripts.py` | Wrap α_2D, ρ_DE, Ω_c in `$...$` (165 fixes) | L308dm |
| `fix_letter_caret.py` | Wrap plain-text `M^N`, `V^4` in `$...$` (91 fixes) | L308dn |
| `fix_physics_subscripts.py` | Wrap `H_0`, `M_*`, `sigma_int` etc. in `$...$` (452 fixes) | L308dn |
| `fix_greek_value_patterns.py` | Wrap standalone Greek=value with Unicode super (612 fixes) | L308dr |
| `fix_double_comma.py` | Fix redundant `\,` (thin space) commands causing double commas | L308dq |
| `replace_unicode_fallback.py` | ℓ→\ell, ⋆→\star, ≪→\ll, emoji→[OK]/[FAIL] (77 fixes) | L308do |
| `fix_unicode_times_powers.py` | Wrap `N × 10ⁿ [unit]` patterns (202 fixes) | L308dz |
| `fix_subscript_vars.py` | **Wrap `r_12`, `l_12`, `D_A`, `M_Pl,3D`, `τ_2D`, etc. in `$...$` (120 fixes)** | **L308er** |

### Legacy / unused (kept for reference)

These scripts are not called by `master_pipeline.py` (some have known bugs
that produce broken patterns):

| Script | Status |
|--------|--------|
| `fix_greek_subscripts.py` | UNUSED — `fix_unicode_greek_subscripts.py` supersedes it |
| `fix_broken_markdown.py` | UNUSED — patterns 1-23 superseded by newer fixers |
| `combine_adjacent_math.py` | UNUSED — `$X$ $Y$` → `$X Y$` not needed in current state |
| `fix_notation.py` | UNUSED — older comprehensive fixer, subsumed |
| `fix_pl_subscripts.py` | UNUSED — older fixer |
| `fix_sigma.py` | UNUSED — incomplete (just `import re`) |
| `fix_dashes.py` | UNUSED — incomplete (just `import re`) |

## Fix Categories Summary (L308dm–L308er)

The recent notation fixes (16 commits L308dm–L308er) caught:

| Category | Total fixes | Tool |
|----------|-------------|------|
| Unicode Greek+subscript (α_2D, ρ_DE, etc.) | 165 | fix_unicode_greek_subscripts |
| Letter+caret (M^N, V^4) | 91 | fix_letter_caret |
| Physics subscripts (H_0, M_b, sigma_int) | 452 | fix_physics_subscripts |
| Brace subscripts (M_{b}) | 31 | fix_physics_subscripts (extended) |
| Unicode missing chars (ℓ, ⋆, emoji) | 77 | replace_unicode_fallback |
| Greek=value with Unicode super | 612 | fix_greek_value_patterns |
| Broken math (α_3+1D, f_DE,closed) | 30+ | source bugs |
| ×10ⁿ plain text | 202 | fix_unicode_times_powers |
| GeV⁴ and m/s² Unicode | 46 | source bugs |
| 10ⁿ unit in tables | 251 | source regex |
| $X$=Y broken math | 22 | source bugs |
| $X$ = value TeV/GeV | 52 | source bugs |
| $X$ = value time_unit | 17 | source bugs |
| α_X = value | 6 | source bugs |
| More N×10ⁿ patterns | 11 | source bugs |
| Δχ² (CMB penalty) | 19 | source bugs |
| l_12, r_12, D_A patterns | 50+50 | source bugs + fix_subscript_vars |
| ^(D-2) → ^{D-2} | 44 | source bugs |
| Subscript vars (r_12_disk, M_Pl,3D) | 120 | fix_subscript_vars |
| **Total** | **~2,500** | (16 commits) |

## Usage

Run the full pipeline:
```bash
python3 paper/build_tools/master_pipeline.py
```

Run individual scripts:
```bash
python3 paper/build_tools/fix_subscript_vars.py              # All files
python3 paper/build_tools/fix_subscript_vars.py README.md    # Single file
python3 paper/build_tools/fix_subscript_vars.py --all        # All markdown files
```

Run audit (read-only):
```bash
python3 paper/build_tools/audit_units.py              # Find bare-number table cells
python3 paper/build_tools/audit_broken_math.py        # Find broken math patterns
```

## Adding a New Tool

When adding a new math-fix tool:

1. Write the script as `paper/build_tools/fix_<category>.py`
2. Add the script to the inventory above
3. Add a `step_fix_<category>()` function in `master_pipeline.py`
4. Add the step name to the `STEPS` list (in the right order)
5. Add the step function to the `step_fns` dict
6. Add a docstring describing what the step fixes and examples
7. Add the new tool to the "Fix Categories Summary" table above
8. Test with `python3 paper/build_tools/master_pipeline.py`

## Cache Warning

If you modify a script, clear Python's bytecode cache:
```bash
rm -rf paper/build_tools/__pycache__
```

Otherwise Python may load the OLD compiled version.

## Related Files

- `paper/build_pdf.sh` — Actual paper build script (xelatex + postprocessing)
- `paper/.build/paper_full.log` — Build log (check here for build errors)
- `paper/.build/xelatex2.log` — Xelatex log (find Missing $ inserted, etc.)