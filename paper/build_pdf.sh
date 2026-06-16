#!/bin/bash
# build_pdf.sh - Build the paper PDF from paper/markdown/*.md files
# =====================================================================
#
# FINDINGS & HISTORY (v3.0.x build pipeline, June 2026)
# ======================================================
#
# This build script was iteratively developed over many sessions. The
# markdown → LaTeX → PDF pipeline has many subtle gotchas. Below is
# the full documentation of what was tried, what failed, and why.
#
# ---------------------------------------------------------------------
# 0. CRITICAL GOTCHAS (read these first!)
# ---------------------------------------------------------------------
#
# This section is a TL;DR of the most damaging silent failures in this
# build pipeline. Each one produces a broken PDF with NO LaTeX error
# and NO warning. If you see weird PDF output, check this section first.
#
# GOTCHA #1: $...$ math with parens inside a table cell (section 4.4)
#   SYMPTOM: column widths printed as text in the table
#   EXAMPLE: | GeV DM (cascade's mass) | $E_{decay}/p_F \sim 10^{21}$ | FAILS |
#   FIX: drop parens, use \[...\] or \(...\), or remove math from cell
#   SECTION: 3 (full analysis) and 4.4 (workarounds)
#
# GOTCHA #2: `---` (horizontal rule) immediately after a table (section 4.2)
#   SYMPTOM: all content after the `---` is wrapped in a 1-column narrow
#            table (0.0556 of page width, ~0.4 inches), text wraps one
#            character per line
#   EXAMPLE:
#     | col1 | col2 |        <- table ends here
#     |------|------|
#     | data | data |
#     ---                    <- DON'T! Pandoc reads this as table continuation
#     # Next Section         <- this gets wrapped in 1-column table
#   FIX: remove the `---`, use blank line + blank line instead
#   SECTION: 4.2 (full analysis)
#
# GOTCHA #3: raw LaTeX in markdown needs raw_tex option (section 1)
#   SYMPTOM: \begin{align}... shows as literal text, not compiled
#   FIX: raw_tex is already enabled in our pandoc options, just use it
#
# GOTCHA #4: First line "---" gets parsed as YAML (section 1)
#   SYMPTOM: parse error on the first line
#   FIX: -yaml_metadata_block is already in our options
#
# GOTCHA #5: Missing blank line between heading and table (section 4.1)
#   SYMPTOM: table is rendered as inline text with literal |---| separators
#   EXAMPLE:
#     **Comparison**:
#     | col1 | col2 |        <- NO BLANK LINE ABOVE!
#     |------|------|
#     | data | data |
#   FIX: add a blank line between the **Heading**: and the |
#   SECTION: 4.1 (table syntax)
#
# GOTCHA #6: Pipe table with unbalanced column lengths (section 4.1)
#   SYMPTOM: short content in wide columns, long content overflowing narrow
#            columns, awkward text wrapping at column boundaries
#   EXAMPLE: Parameter | Value | Purpose | Calibrated to
#            The 'Purpose' column has long math content but Pandoc
#            allocates width based on header text length, not content
#   FIX: convert to GRID TABLE with explicit column widths
#        (use longer |---| for wider columns)
#   SECTION: 4.1 (table syntax, "PIPE TABLES: WHEN TO ESCAPE TO GRID TABLES")
#
# ---------------------------------------------------------------------
# 1. THE PANDOC OPTIONS
# ---------------------------------------------------------------------
#
# We use: markdown+grid_tables+pipe_tables+raw_tex-yaml_metadata_block
#
# - markdown:        base markdown parser
# - grid_tables:     enables |---|---| grid tables (Pandoc grid syntax)
# - pipe_tables:     enables |---|---| pipe tables (GitHub-style syntax)
# - raw_tex:         preserves raw LaTeX (e.g. \begin{equation})
# - -yaml_metadata_block:  DISABLES Pandoc's YAML metadata parsing
#                         (avoids parse errors on the first line "---")
#
# Earlier we used `markdown_strict` which produced a working PDF but
# had TABLES AS RAW TEXT in the PDF. Switching to grid_tables+pipe_tables
# is what enables proper table rendering.
#
# Required LaTeX packages in the header:
#   - amsmath, amssymb     : standard math
#   - mathrsfs             : \mathscr{R} (script R) for the cascade action
#   - longtable, booktabs  : long tables and \toprule/\midrule/\bottomrule
#   - enumitem             : tighter list spacing
#   - parskip              : paragraph spacing
#   - geometry             : page margins
#   - array, multirow      : table cell formatting
#
# ---------------------------------------------------------------------
# 2. THE POST-PROCESSOR PIPELINE
# ---------------------------------------------------------------------
#
# Pandoc generates LaTeX that needs cleanup before xelatex can compile.
# The pipeline runs four post-processors in order:
#
#   1. wrap_dimexpr.py     : wraps `\real{N}` in \dimexpr
#   2. use_linewidth.py    : converts \dimexpr(...) to \linewidth
#   3. fix_dashes.py       : fixes en-dash "1--2" → hyphen "1-2" in math
#   4. fix_sigma.py        : fixes \sigma\^{}{N} → \sigma^{N} patterns
#
# Why all four? Pandoc's LaTeX output has bugs that don't surface in
# standard markdown → HTML conversion. Each script addresses one
# specific issue. See the script files for details.
#
# ---------------------------------------------------------------------
# 3. THE \dimexpr BUG (THE BIG ONE, FOUND IN v3.0.21)
# ---------------------------------------------------------------------
#
# The most subtle and damaging bug: Pandoc generates longtable column
# specifications like this:
#
#   p{(\columnwidth - 4\tabcolsep) * \real{0.4375}}
#
# We wrap this in \dimexpr to make it a real LaTeX dimension:
#
#   p{\dimexpr(\columnwidth - 4\tabcolsep)*0.4375\relax}
#
# This LOOKS correct but has a SILENT LaTeX bug: when the table contains
# cells with parens (like "(cascade's required mass)") or math mode
# (like "$E_{decay}/p_F \sim 10^{21}$"), the \dimexpr expansion fails
# and LaTeX PRINTS the column WIDTHS as text:
#
#   Failure     .4375     .2812     .2812     Problem    Verdict
#   mode              MECHANISM    Pauli
#   GeV        FAILS    block-
#   DM                ing
#   (cas-            IN-
#   ... etc, completely broken layout
#
# No LaTeX error, no warning. The PDF is silently broken.
#
# THE FIX: use \linewidth syntax instead, which is more robust:
#
#   p{0.4375\linewidth}
#
# This is what use_linewidth.py does. The page count dropped from
# 408 to 353 when this was applied because the broken tables were
# taking up many extra pages with their invisible/overlapping text.
#
# ---------------------------------------------------------------------
# 4. HOW TO PROPERLY WRITE MARKDOWN FOR THIS BUILD
# ---------------------------------------------------------------------
#
# This section is a style guide. Follow these rules to avoid LaTeX
# issues in the PDF.
#
# ---- 4.1 TABLES ----
#
# Two table formats work in this build: PIPE TABLES and GRID TABLES.
# Each has tradeoffs. Choose based on what you need.
#
# === PIPE TABLES (default, GitHub-style) ===
#
# Format:
#   | Column 1 | Column 2 | Column 3 |
#   |----------|----------|----------|
#   | data 1   | data 2   | data 3   |
#   | data 4   | data 5   | data 6   |
#
# PROS:
#   - Easy to type and maintain
#   - Renders well on GitHub.com
#   - Pandoc's default markdown table format
#
# CONS:
#   - Column widths are AUTO-ALLOCATED by Pandoc based on HEADER text
#     length, NOT content length
#   - This often produces bad proportions:
#     * Short headers get narrow columns with overflowing content
#     * Long headers get wide columns with short content
#   - You have NO direct control over column widths
#
# USE PIPE TABLES when:
#   - All columns have similar content lengths
#   - You don't care about exact column proportions
#   - Content is short (e.g., values, numbers, short labels)
#
# EXAMPLE (good fit for pipe tables):
#   | Galaxy | M_b (M_o) | σ (km/s) | Type  |
#   |--------|-----------|----------|-------|
#   | M31    | 1.5e11    | 160      | Sb    |
#   | MW     | 6e10      | 120      | Sbc   |
#
# === GRID TABLES (explicit column widths) ===
#
# Format:
#   +---------+---------+----------------+----------------+
#   | Column 1| Column 2| Column 3       | Column 4       |
#   +=========+=========+================+================+
#   | data 1  | data 2  | long content   | more content   |
#   +---------+---------+----------------+----------------+
#   | data 3  | data 4  | more long      | more content   |
#   +---------+---------+----------------+----------------+
#
# PROS:
#   - EXPLICIT control over column widths
#   - Use longer |---| for wider columns
#   - Use shorter |---| for narrower columns
#   - The = signs in the header separator mark it as a grid table
#
# CONS:
#   - More verbose to type and maintain
#   - Doesn't render as nicely on GitHub.com (shows as literal text)
#   - Harder to add/remove columns (need to update all separators)
#
# USE GRID TABLES when:
#   - You have very different content lengths across columns
#   - Long content (math, prose) is in one column, short in another
#   - You want specific column proportions
#   - The pipe table version looks bad
#
# WIDTH CALCULATION: Pandoc uses the |---| separator lengths to
# determine column width ratios. The actual lengths don't matter
# (e.g., 8 chars vs 24 chars), only the RATIO between them.
#
# EXAMPLE (good fit for grid tables):
#   +----------+-------+----------------------------------------------+-----------------------+
#   | Parameter | Value | Purpose                                      | Calibrated to         |
#   +==========+=======+==============================================+=======================+
#   | α        | 1.29  | Energy-scaling rule exponent τ_2D = ...     | 1 data point: SN 33s  |
#   +----------+-------+----------------------------------------------+-----------------------+
#   | z_half   | ≈ 3   | Smooth F_p(z) Hill-function transition       | 2 anchors: z=0 and z=1100 |
#   +----------+-------+----------------------------------------------+-----------------------+
#
# === PIPE TABLES: WHEN TO ESCAPE TO GRID TABLES ===
#
# Convert pipe tables to grid tables when you see:
#   - Long content overflowing narrow columns
#   - Short content in overly wide columns
#   - Text wrapping awkwardly at column boundaries
#   - A specific column needs to be wider for readability
#
# EXAMPLE of problematic pipe table:
#   | Parameter | Value | Purpose | Calibrated to |
#   |-----------|-------|---------|---------------|
#   | α         | 1.29  | Energy-scaling rule exponent τ_2D = (E/E_Pl)^α · t_Pl | 1 data point: SN 33s lifetime |
# The 'Purpose' column is too narrow for the math, and 'Calibrated to'
# is too wide for the short text.
#
# SOLUTION: grid table with explicit proportions
#   (the |---| lengths directly control the column widths)
#
# === SYNTAX GOTCHAS ===
#
# Pipes in cell content: ESCAPE them with backslash:
#   | text \| more text |
#
# Empty cells: just leave the area between pipes empty:
#   | cell1 |  | cell3 |
#   | cell4 |  | cell6 |
#
# Line breaks within cells: use <br> in pipe tables:
#   | line 1<br>line 2 |
#
# In GRID tables, you can use literal newlines in cells:
#   +-------+----+
#   | A     | B  |
#   +=======+====+
#   | line1 | x  |
#   | line2 |    |
#   +-------+----+
#
# BUT: in pipe tables, multi-line cells are tricky. Use <br>.
#
# === BLANK LINE BEFORE TABLE (REQUIRED) ===
#
# ALWAYS put a blank line between a heading and a table. Without it,
# Pandoc may not recognize the table.
#
# BREAKS:
#   **Comparison**:
#   | col1 | col2 |
#   |------|------|
#   | data | data |
#
# WORKS:
#   **Comparison**:
#
#   | col1 | col2 |
#   |------|------|
#   | data | data |
#
# (See section 4.2 for the related `---` gotcha.)
#
# ---- 4.2 HORIZONTAL RULES AND TABLE SEPARATORS ----
#
# AVOID: `---` (horizontal rule) immediately after a table.
#
# Pandoc can misinterpret `---` as a table row separator, causing
# the following content to be wrapped in a single narrow column
# (e.g., 0.0556\linewidth) with text wrapped one character per line.
#
# Example of what breaks:
#   | col1 | col2 |
#   |------|------|
#   | data | data |
#
#   ---     <-- DON'T DO THIS
#
#   # Next Section
#   This content will be wrapped in a 1-column narrow table.
#
# WORKAROUND: use blank line + blank line, or no separator at all.
#   | col1 | col2 |
#   |------|------|
#   | data | data |
#
#   (blank line)
#
#   # Next Section
#   This content renders normally.
#
# This is a Pandoc ambiguity: `---` can be a horizontal rule, a
# Setext header underline, or (in some contexts) a table separator.
# In the context of a markdown file with `pipe_tables` enabled,
# Pandoc tends to interpret it as table continuation, which is
# almost never what you want.

# ---- 4.3 MATH IN TEXT ----
#
# INLINE MATH in a sentence, use $...$:
#   The mass is $m = 10^{21}$ kg.
#
# DISPLAY MATH (centered, on its own line), use $$...$$:
#   $$
#   E = mc^2
#   $$
#
# OR for an unnumbered display equation, use \[...\]:
#   \[
#   E = mc^2
#   \]
#
# For complex multi-line equations, use the align environment directly
# (raw_tex is enabled so Pandoc passes it through):
#   \begin{align}
#   E &= mc^2 \\
#     &= h\nu
#   \end{align}
#
# ---- 4.4 TABLE CELLS WITH MATH ----
#
# AVOID: $...$ math mode with PARENS inside a TABLE CELL.
# Example that breaks the table:
#   | GeV DM (cascade's mass) | $E_{decay}/p_F \sim 10^{21}$ | FAILS |
#                                                                 ^^^
#   This breaks the \dimexpr in the column width and prints the
#   widths as text. Use ONE of these fixes:
#
#   (a) Drop the parens from the cell text:
#       | GeV DM cascade mass | $E_{decay}/p_F \sim 10^{21}$ | FAILS |
#
#   (b) Put the math in display mode \[...\]:
#       | GeV DM (cascade's mass) | \[E_{decay}/p_F \sim 10^{21}\] | FAILS |
#
#   (c) Use \(...\) instead of $...$ (slightly more reliable):
#       | GeV DM (cascade's mass) | \(E_{decay}/p_F \sim 10^{21}\) | FAILS |
#
# IN PRACTICE: option (a) is simplest. Drop parens where you can.
# For long equations, consider rewriting them as display math OUTSIDE
# the table rather than inside it.
#
# ---- 4.5 SPECIAL CHARACTERS ----
#
# In LaTeX text mode, several characters need escaping:
#
#   $ → \$       (dollar sign, math mode shift)
#   % → \%       (comment character)
#   & → \&       (alignment character, crucial in tables)
#   # → \#       (parameter character)
#   _ → \_       (subscript, math mode shift)
#   { } → \{ \}  (grouping characters, but usually fine in pairs)
#   ~ → \textasciitilde{} or $\sim$
#   ^ → \textasciicircum{} or $\hat{}$
#   \ → \textbackslash{}
#
# In TABLES: ALWAYS escape & to \&. Other characters usually work but
# may produce warnings.
#
# In MARKDOWN paragraphs: Pandoc handles most escaping automatically.
# Use $...$ for math, not escaped dollar signs.
#
# ---- 4.6 GREEK LETTERS AND SYMBOLS ----
#
# GREEK: use LaTeX commands: \alpha, \beta, \gamma, \delta, etc.
# (NOT Unicode α unless you want to test font support)
#
# Common cascade symbols:
#   \alpha = 1.29     energy-scaling exponent
#   \tau_{2D}         2D universe lifetime
#   \Omega_{DM}       dark matter density
#   \mu, b            Liouville CFT parameters
#   \epsilon          back-action factor
#   \gamma            Lorentz factor
#
# Always wrap math in $...$ even in tables.
#
# ---- 4.7 SECTION HEADERS ----
#
# Pandoc's ATX-style headers work (preferred):
#   # Top-level
#   ## Subsection
#   ### Subsubsection
#
# Setext-style (===, ---) headers also work but are less common in
# this paper.
#
# The first \section{...} is STRIPPED in Step 2 because the title is
# already in the LaTeX header (from paper_header.tex). So don't put
# important content in the first section header.
#
# ---- 4.8 CODE, FILENAMES, URLs ----
#
# Inline code: `code` → \texttt{code} in PDF
#
# Code blocks:
#   ```python
#   def f(x):
#       return x
#   ```
#
# Filenames: `calculations/v27_foo.py` (use backticks)
#
# URLs: <https://example.com> or just bare https://example.com
# Both work; Pandoc makes them clickable in PDF.
#
# ---- 4.9 CROSS-REFERENCES ----
#
# Section refs: §3.15, §2.5.3, etc. (just type the § character)
#
# Reference to specific section: \S 3.15 in LaTeX, or just §3.15 in
# markdown. (Don't use $...$ around § or you'll get errors.)
#
# ---- 4.10 LISTS ----
#
# Use `-` or `*` for unordered lists, `1.` for ordered.
# Indent nested lists with 2 or 4 spaces.
#
# ---- 4.11 EMPHASIS ----
#
# *italic*   → \emph{italic} in PDF
# **bold**   → \textbf{bold} in PDF
# ***bold italic*** → \textbf{\emph{...}} in PDF
#
# ---- 4.12 STRIKETHROUGH ----
#
# Pandoc's ~~strikethrough~~ doesn't work with markdown_strict but
# does work with our pandoc options. However, it sometimes produces
# strange output. Prefer (\emph{rejected text}) for emphasis instead.
#
# ---- 4.13 AVOID THESE ----
#
# ❌ DON'T use raw HTML in markdown (won't render in PDF)
# ❌ DON'T use <br> for line breaks (use double-space at end of line)
# ❌ DON'T use $...$ with parens inside table cells (see 4.3)
# ❌ DON'T use \S in math mode ($§3$ breaks; use §3 in text mode)
# ❌ DON'T use \textasciitilde or \textasciicircum in math (use \sim, \hat)
# ❌ DON'T use Unicode subscripts/superscripts like ₁₀ (font issues)
#    Use $x_{10}$ instead.
# ❌ DON'T use Unicode special characters like —, –, …, × without
#    testing (use ---, --, \ldots, \times in LaTeX)
# ❌ DON'T use $...$ for full sentences (only short math expressions)
#
# ---- 4.14 COMMON PATTERNS THAT WORK ----
#
# Inline math:  $E = mc^2$           ✅
# Display math: \[E = mc^2\]         ✅
# Display math: $$E = mc^2$$         ✅
# Align env:    \begin{align}...     ✅ (raw_tex passes through)
# Cite:         [Einstein 1905]      ✅ (with bibliography)
# Footnote:     [^1] then [^1]: ...  ✅
# Image:        ![alt](path.png)     ✅
# Table:        |---|---|            ✅
# Greek:        \alpha, \beta        ✅ (in $...$)
# Section:      ## My Section        ✅
# Code inline:  `code`               ✅
# Code block:   ```python ... ```    ✅
# Bold:         **text**             ✅
# Italic:       *text*               ✅
# Strikethrough: ~~text~~            ✅ (use sparingly)
# Cross-ref:    §3.15                ✅ (just the § character)
#
# ---------------------------------------------------------------------
# 5. TROUBLESHOOTING
# ---------------------------------------------------------------------
#
# IF THE BUILD FAILS with a cryptic LaTeX error:
#   1. Look at /tmp/xelatex1.log for the actual error
#   2. Find the LINE NUMBER in the error
#   3. Look at /tmp/paper_full.tex at that line
#   4. Most errors are: $ in text mode, _ in text mode, mismatched braces
#
# IF TABLES ARE BROKEN (column widths printed as text):
#   1. Check if any cells have parens or $...$ math
#   2. Use option (a), (b), or (c) from section 4.4 above
#   3. Or simply remove the math from the cell and use prose
#   (See section 3 above for the full \dimexpr bug analysis)
#
# IF CONTENT IS WRAPPED IN A 1-COLUMN NARROW TABLE (text one char/line):
#   1. Check if there's a `---` (horizontal rule) immediately after a table
#   2. The `---` is being interpreted by Pandoc as a table row separator
#   3. ALL content after the `---` is being wrapped in a longtable with
#      a single column of width 0.0556 of the page (~0.4 inches)
#   4. FIX: Remove the `---` separator. Use a blank line instead.
#   (See section 4.2 above for the full analysis)
#   Diagnostic command:
#     grep -n "^---$" paper/markdown/*.md
#   Then look at what's directly above each `---`:
#     sed -n 'N-3,N+3p' paper/markdown/FILENAME.md
#   If line N-1 starts with `|`, that's the problem.
#
# IF THE BUILD IS SLOW (multi-minute xelatex):
#   1. Check for runaway regex in post-processors
#   2. Look at /tmp/paper_full.tex size (should be < 2MB)
#
# IF TABLES ARE TOO WIDE (text wraps in tiny columns):
#   1. The page is letter size, 6.5" wide content area
#   2. Tables with 4+ columns will be cramped
#   3. Consider splitting into multiple tables or using abbreviations
#
# ---------------------------------------------------------------------
# 6. PERFORMANCE NOTES
# ---------------------------------------------------------------------
#
# Build time: ~30-60 seconds for ~350 page PDF
# - pandoc conversion: ~1-2 seconds
# - 4 post-processors: <1 second total
# - xelatex run 1: ~10-20 seconds (generates aux files)
# - xelatex run 2: ~10-20 seconds (resolves cross-references)
#
# ---------------------------------------------------------------------
# 7. THE PIPELINE STEPS
# ---------------------------------------------------------------------

set -e

PAPER_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PAPER_DIR"

# Step 0: Combine markdown files
if [ -d "markdown" ]; then
    cat markdown/*.md > /tmp/paper_combined.md
    SOURCE=/tmp/paper_combined.md
else
    SOURCE=paper.md
fi

# Step 1: Convert with markdown+grid_tables+pipe_tables+raw_tex-yaml_metadata_block
# See section 1 above for why these specific options.
pandoc "$SOURCE" -o /tmp/paper_body.tex -f markdown+grid_tables+pipe_tables+raw_tex-yaml_metadata_block

# Post-processor 1: wrap \real{N} in \dimexpr
# Pandoc generates: p{(\columnwidth - 4\tabcolsep) * \real{0.4375}}
# We want:         p{\dimexpr(\columnwidth - 4\tabcolsep)*0.4375\relax}
# See /tmp/wrap_dimexpr.py for details.
python3 /tmp/wrap_dimexpr.py

# Post-processor 2: convert \dimexpr(...) to \linewidth
# This is the v3.0.21 fix for the silent table-breaking bug.
# See section 3 above for the full explanation.
# See /workspace/github-repo/paper/use_linewidth.py for details.
python3 /workspace/github-repo/paper/use_linewidth.py

# Post-processor 3: fix en-dash in math mode
# Pandoc converts "1-2" in math cells to "1--2" (en-dash).
# This breaks math mode. Fix: "1--2" → "1-2" in math cells.
# See /tmp/fix_dashes.py for details.
python3 /tmp/fix_dashes.py

# Post-processor 4: fix \sigma\^{}{N} patterns
# Pandoc generates \sigma\^{}{N} (empty arg hat) which is invalid.
# Fix: \sigma\^{}{N} → \sigma^{N}
# See /tmp/fix_sigma.py for details.
python3 /tmp/fix_sigma.py

# Step 2: Strip the first \section{...}
# The title is already in the LaTeX header, so we don't want it twice.
python3 -c "
import re
with open('/tmp/paper_body.tex', 'r') as f:
    body = f.read()
m = re.search(r'\\\\section\\{[^}]+\\}\\s*\\n\\n', body)
if m:
    body = body[m.end():]
with open('/tmp/paper_body_clean.tex', 'w') as f:
    f.write(body)
"

# Step 3: Create header
# The LaTeX preamble. The packages here are required - see section 1 above.
cat > /tmp/paper_header.tex << 'HEADEREOF'
\documentclass[10pt]{article}
\usepackage{amsmath, amssymb}
\usepackage{mathrsfs}
\usepackage{fontspec}
\usepackage{hyperref}
\usepackage{geometry}
\usepackage{enumitem}
\usepackage{parskip}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{array}
\usepackage{multirow}
\geometry{margin=1in}
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
\providecommand{\tightlist}{}
\title{Gravity as Residual: A Thought Experiment on Dimensional Inversion, Annihilation, and the Origin of the Dark Sector}
\author{ampbuster (software developer, not a physicist) \\ \small AI assistance: Mavis (M3, MiniMax)}
\date{v3.0.21 (June 2026) \\ \small \url{https://github.com/ampbuster/gravity-as-residual}}
\begin{document}
\maketitle
\tableofcontents
\newpage
HEADEREOF

# Step 4: Combine and compile
cat /tmp/paper_header.tex /tmp/paper_body_clean.tex > /tmp/paper_full.tex
echo '\end{document}' >> /tmp/paper_full.tex

cd /tmp
# Run xelatex TWICE: first to generate aux files, second to resolve cross-refs
xelatex -interaction=nonstopmode -halt-on-error paper_full.tex > /tmp/xelatex1.log 2>&1 || {
    echo "First xelatex run failed. Tail of log:"
    tail -30 /tmp/xelatex1.log
    exit 1
}
xelatex -interaction=nonstopmode -halt-on-error paper_full.tex > /tmp/xelatex2.log 2>&1 || {
    echo "Second xelatex run failed. Tail of log:"
    tail -30 /tmp/xelatex2.log
    exit 1
}

cp /tmp/paper_full.pdf "${PAPER_DIR}/paper.pdf"
echo "Paper PDF built: ${PAPER_DIR}/paper.pdf"
ls -la "${PAPER_DIR}/paper.pdf"
