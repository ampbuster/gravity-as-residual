# Build Tools: Math Notation Cleanup Pipeline

This directory contains the post-processor tools that fix broken math
notation in markdown files (paper, README, etc.).

## Quick Start

For a single file:
```bash
# Run the full cleanup pipeline on a file
python3 paper/build_tools/cleanup_math.py path/to/file.md
```

For all markdown files in the repo:
```bash
# Run from the repo root
python3 paper/build_tools/cleanup_math.py
```

## Order of Operations (CRITICAL)

The tools **MUST** be run in the order below. The first set does
"structural" fixes (wrapping, replacing); the last step does "cleanup"
(spacing, combining) which depends on the structural fixes being done first.

```
Step 1: wrap_math_vars.py        # Wrap M_Pl, E_4D, v_Higgs, etc. in $...$
Step 2: wrap_powers_of_10.py     # Convert 10^N to $10^{N}$
Step 3: e_to_math.py             # Convert 1.5e10 to $1.5 \times 10^{10}$
Step 4: greek_to_latex.py        # Convert α, β, γ to $\alpha$, $\beta$, $\gamma$

--- (run all cleanup tools in this order) ---

Step 5: combine_adjacent_math.py # Combine "$X$ $Y$" into "$X Y$"
Step 6: fix_math_spacing.py      # RUN THIS LAST to fix spacing inside math
```

**Why this order matters:**
- `fix_math_spacing.py` and `combine_adjacent_math.py` are sensitive to
  the placement of `$` delimiters. Running them BEFORE the structural
  fixes can result in over-aggressive combining of broken math.
- `fix_math_spacing.py` should ALWAYS be the LAST step because earlier
  fixes can introduce new spacing issues inside newly-wrapped math.

## Individual Tools

### Structural Fixes (run first)

| Tool | Purpose |
|---|---|
| `wrap_math_vars.py` | Wrap physics variables (`M_Pl`, `E_4D`, `v_Higgs`, etc.) in `$...$` |
| `wrap_powers_of_10.py` | Convert `10^N` text to `$10^{N}$` math |
| `e_to_math.py` | Convert scientific notation (`1.5e10`) to math form |
| `greek_to_latex.py` | Convert Unicode Greek letters (α, β, etc.) to LaTeX |

### Cleanup Fixes (run after)

| Tool | Purpose |
|---|---|
| `combine_adjacent_math.py` | Combine adjacent math blocks: `$X$ $Y$` → `$X Y$` |
| `fix_math_spacing.py` | **ALWAYS RUN LAST** - fix spacing inside math blocks |

### Master Scripts

| Tool | Purpose |
|---|---|
| `cleanup_math.py` | Master script that runs steps 1-4 (structural) in sequence |
| `build_pdf.sh` | Full build pipeline including post-processors 5-6 (cleanup) |

## Common Issues and Fixes

### Issue: "M_Pl" appears as raw text (not math)

**Before:** `M_Pl,2D = 3 TeV`
**After:** `$M_{\rm Pl,2D} = 3$ TeV`

**Fix:** Run `wrap_math_vars.py`

### Issue: Greek letters appear as Unicode (α, β, etc.) outside math

**Before:** `α = 1.289`
**After:** `$\alpha = 1.289$`

**Fix:** Run `greek_to_latex.py`

### Issue: Adjacent math blocks not combined

**Before:** `$N_{\rm sub}$ = $E_{\rm 4D}/E_{\rm sub}$`
**After:** `$N_{\rm sub} = E_{\rm 4D}/E_{\rm sub}$`

**Fix:** Run `combine_adjacent_math.py`

### Issue: Spaces inside math (e.g., `$\alpha$ = 1.289`)

**Before:** `$\alpha$ = 1.289`
**After:** `$\alpha = 1.289$`

**Fix:** Run `fix_math_spacing.py` (LAST!)

## Why this matters

The math notation fixes are needed because:
- **GitHub** renders `$X$` as LaTeX math
- **The paper** uses pandoc → xelatex, which needs proper `$X$` math
- **Searchability** is better with consistent notation
- **PDF generation** is more reliable when math is properly delimited

## Running the Full Pipeline

The build script `paper/build_pdf.sh` runs the FULL pipeline including
the post-processors. To rebuild the paper after fixing math:

```bash
bash paper/build_pdf.sh
```

This runs:
1. The structural fixers (via `cleanup_math.py`)
2. pandoc to convert markdown to LaTeX
3. The cleanup fixers (`fix_dashes.py`, `fix_sigma.py`)
4. xelatex to compile the PDF

## Verification

After running the pipeline, verify with:

```bash
# Math balance check (0 lines with odd $ count = good)
python3 -c "
with open('README.md') as f:
    content = f.read()
bad = 0
for line in content.split('\n'):
    if line.strip().startswith('\`\`\`'): continue
    n = line.count('\$')
    if n % 2 == 1:
        print(f'Line broken: {line[:60]}')
        bad += 1
print(f'Lines with odd \$ count: {bad}')
"
```

## Last Updated

v3.5.8 (June 20, 2026) - Initial README created
