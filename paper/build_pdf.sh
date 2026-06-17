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

# ---- 4.3.1 HOW TO WRITE MATH FOR ALL TARGETS (PDF, github.com, Markor) ----
#
# THE PAPER.MD FILES use the LaTeX build pipeline (xelatex) which handles
# LaTeX correctly. But the README.md and layman_summary.md are public-facing
# and render on github.com (mobile + desktop) and in Markor. These have
# DIFFERENT requirements for math.
#
# GITHUB.COM MOBILE HAS STRICT REQUIREMENTS:
#
#   1. WHITESPACE around $...$ is REQUIRED:
#      WRONG:  M_dyn > 2$\times$ M_stars   (no spaces)
#      RIGHT:  M_dyn > 2 $\times$ M_stars   (with spaces)
#      The $...$ must have whitespace (or other non-letter characters) on
#      both sides. Without spaces, github mobile shows literal "$...$" text.
#
#   2. USE PROPER LATEX, NOT UNICODE SUBSCRIPTS/SUPERSCRIPTS:
#      WRONG:  10¹²  (Unicode superscript, may not render)
#      WRONG:  H₀       (Unicode subscript, may not render)
#      RIGHT:  $10^{12}$    (LaTeX math mode)
#      RIGHT:  $H_0$        (LaTeX math mode)
#
#   3. KEEP MATH EXPRESSIONS WHOLE IN $...$:
#      WRONG:  $\sim$10^55   (\sim in math, 10^55 outside)
#      WRONG:  $\sim$10³$\times$ (three separate math segments)
#      RIGHT:  $\sim 10^{55}$  (whole expression in math)
#      RIGHT:  $\sim 10^{3} \times$  (whole expression in math)
#
#   4. AVOID SPACES INSIDE $...$ DELIMITERS:
#      WRONG:  $\epsilon $     (space inside closing $)
#      WRONG:  $ \epsilon$     (space inside opening $)
#      WRONG:  $ \epsilon $    (space inside both)
#      RIGHT:  $\epsilon$      (no spaces inside $...$)
#
#   5. AVOID DUPLICATE $ DELIMITERS:
#      WRONG:  $\sim$$10^{55}$  (two $ adjacent)
#      RIGHT:  $\sim 10^{55}$   (single $ wrapping the whole)
#
# COMMON PATTERNS AND THEIR FIXES:
#
#   Pattern                    | Fix
#   ---------------------------|----------------------------------------
#   10^19 (plain text)         | $10^{19}$
#   10^-43 (negative)          | $10^{-43}$
#   10⁴ (⁴ = superscript 4)| $10^{4}$
#   H_0 (plain text)           | $H_0$
#   M_Pl^4 (mixed)             | $M_{Pl}^4$
#   E_{4D} (curly braces)      | $E_{4D}$
#   \times                    | $\times$
#   \sim                      | $\sim$
#   \to                       | $\to$
#   \pm                       | $\pm$
#   \approx                   | $\approx$
#   \geq / \leq              | $\geq$ / $\leq$
#   \propto                   | $\propto$
#
# LATEX COMMANDS (Greek letters, operators, etc.):
#
#   \alpha -> α     \beta -> β     \gamma -> γ
#   \delta -> δ     \epsilon -> ε   \zeta -> ζ
#   \eta -> η       \theta -> θ     \iota -> ι
#   \kappa -> κ     \lambda -> λ   \mu -> μ
#   \nu -> ν         \xi -> ξ       \pi -> π
#   \rho -> ρ        \sigma -> σ     \tau -> τ
#   \phi -> φ        \chi -> χ      \psi -> ψ
#   \omega -> ω      \Gamma -> Γ     \Delta -> Δ
#   \Theta -> Θ      \Lambda -> Λ   \Xi -> Ξ
#   \Pi -> Π         \Sigma -> Σ    \Phi -> Φ
#   \Psi -> Ψ        \Omega -> Ω
#
# WHY THREE TARGETS HAVE DIFFERENT RULES:
#
#   - PAPER.MD -> PDF: xelatex handles all LaTeX correctly. $...$ and
#     $$...$$ work. \alpha, \beta etc. all render. Whitespace inside
#     $...$ is fine.
#
#   - README.MD/LAYMAN -> github.com desktop: MathJax renders $...$
#     math. Requires whitespace around $...$ for proper recognition.
#     Most LaTeX commands work.
#
#   - README.MD/LAYMAN -> github.com MOBILE: Same MathJax, but the
#     MOBILE renderer is more strict. WITHOUT WHITESPACE, $...$ shows
#     as literal text. Some complex LaTeX commands may not render.
#
#   - README.MD/LAYMAN -> Markor: Renders LaTeX natively. $...$ works.
#     Slightly more permissive than github.com mobile.
#
# RULE OF THUMB: If your math renders correctly in github.com MOBILE,
# it will render correctly everywhere else.

# ---- 4.3.2 NOTATION RULES (numbers, quantities, ratios) ----
#
# BEYOND the 5 categories of broken LaTeX above, there are NOTATION
# RULES that apply to ALL targets (PDF, github.com, Markor). These
# rules make the paper and docs consistent.
#
# ============================================================
# RULE 1: ALL POWERS OF 10 -> LaTeX math form
# ============================================================
#
#   WRONG:  10^44 J            (plain text "10^44" with caret)
#   WRONG:  10⁵                (Unicode superscript, doesn't render reliably)
#   WRONG:  2.4e-15            (e-notation in body text, informal)
#   WRONG:  $10^44             (no braces, may not render correctly)
#   RIGHT:  $10^{44}$ J        (LaTeX math mode with braces)
#   RIGHT:  $2.4 \times 10^{-15}$ (e-notation converted to math)
#
# ALWAYS use $10^{N}$ (with braces!) for any power of 10 in body text.
# The braces are REQUIRED for multi-digit exponents ($10^{44}$ not $10^44$).
#
# EXCEPTIONS:
#   - CODE BLOCKS: e-notation is natural in code (e.g. `2.4e-15`)
#   - TABLE CELLS (when there's no math context): e-notation is OK
#     (e.g. `9.74e-11`), but prefer $9.74 \times 10^{-11}$ for
#     consistency.
#
# ============================================================
# RULE 2: PHYSICAL QUANTITIES -> math mode with proper subscripts
# ============================================================
#
# ANY quantity with a subscript or superscript MUST be in $...$ math.
# Plain text with underscores or Unicode subscripts is INCONSISTENT.
#
#   WRONG:  H_0 = 73.04         (H_0 in plain text)
#   WRONG:  M_dyn ≈ M_b        (underscores in plain text)
#   WRONG:  f_back = ε × ...   (f_back in plain text)
#   WRONG:  Hₐ = 73.04          (Unicode subscript)
#   RIGHT:  $H_0$ = 73.04
#   RIGHT:  $M_{dyn} \approx M_b$
#   RIGHT:  $f_{\rm back} = \epsilon \times ...$
#
# Common physics quantities to ALWAYS put in math:
#
#   Cosmology:
#     H_0, H_{0,4D}, H_0_CMB, H_0_local
#     Ω_m, Ω_DM, Ω_GW
#     σ_8, S_8, w_0, w_a, a_0
#     z_half
#
#   Mass and energy:
#     M_b, M_halo, M_Pl, M_stars, M_sun (use $M_\odot$ for solar mass),
#     M_dyn, M_baryon, M_stellar, M_BH, M_o, M_2D, M_star
#     E_Pl, E_4D, E_crit, E_primordial
#     t_Pl
#     l_Pl (or $\ell_{\rm Pl}$)
#
#   Acceleration and force:
#     g_+, g_bar, g_obs, g_cum, g_active
#     F_p, F_s
#
#   Fractions and ratios:
#     f_back, f_active
#     ε, ε_GW
#
#   Spacetime topology:
#     AdS_2, AdS_5, dS_2 (use $\AdS_2$ etc.)
#     τ_2D, γ_2D, T_2D
#
#   GW and strain:
#     h_c, Ω_GW
#
#   Velocity and length:
#     V_local, r_h, p_F
#     m_s
#
#   Cross sections / couplings:
#     G_5, G_D, L_V
#
# SUBSCRIPT NAMING CONVENTION:
#   - Single letter/number subscripts: $H_0$, $M_b$, $E_4D$
#   - Multi-letter subscripts: use {\rm ...} for roman text:
#     $f_{\rm back}$, $f_{\rm active}$, $M_{\rm Pl}$, $E_{\rm crit}$
#   - Numbers stay as plain subscripts: $H_0$, $E_4D$
#
# ============================================================
# RULE 3: RATIOS -> math mode with fraction or division
# ============================================================
#
# RATIOS of two quantities should be in math with proper subscripts.
#
#   WRONG:  M_dyn/M_b ~ 14-30  (plain text with / and underscores)
#   WRONG:  τ_2D/E^1.29       (mixed)
#   RIGHT:  $M_{dyn}/M_b \sim 14$--$30$  (math with en-dash for range)
#   RIGHT:  $E^{1+\alpha}$    (creation function, in math)
#
# The slash `/` is fine in math: $M_{dyn}/M_b$ renders as expected.
# For en-dash ranges in math: use `--` (e.g. $1$--$1700$).
#
# ============================================================
# RULE 4: $E^{N}$ vs $E^N$ -- ALWAYS use braces
# ============================================================
#
# LaTeX power notation: ALWAYS use `^{N}` with braces, not `^N` without.
#
#   WRONG:  $E^1.29$           (no braces, LaTeX may misinterpret)
#   WRONG:  $E^(1+alpha)$       (parentheses, not braces)
#   WRONG:  $E^{1+alpha}        (missing closing brace if typed manually)
#   RIGHT:  $E^{1.29}$          (braces, single exponent)
#   RIGHT:  $E^{1+\alpha}$      (braces, expression in exponent)
#   RIGHT:  $E^{2.29}$          (braces, multi-character exponent)
#
# For the lifetime scaling law:
#   - Lifetime:  $\tau_{2D} \sim E^{1.29}$ (uses E for energy, not M)
#   - Creation:  $C(E) = E^{1+\alpha} = E^{2.29}$ (general form, evaluated)
#   - Mass:      $M_{2D,2D} \propto E^{0.71}$ (derived)
#
# ============================================================
# RULE 5: M^1.29 vs E^1.29 -- name vs physics
# ============================================================
#
# `M^1.29` is the CANONICAL NAME for the scaling law (in headers, titles,
# emphasis). It refers to "the 1.29-th power of the event's mass-equivalent".
#
# `E^1.29` is the PROPER PHYSICS NOTATION (lifetime vs event energy).
# Since E=Mc², M^1.29 ∝ E^1.29, dimensionally equivalent.
#
# USE:
#   - `M^1.29` in section titles and emphasis ("the M^1.29 scaling law")
#   - `E^1.29` in physics formulas and equations
#   - Both are acceptable in body text where context makes the meaning clear
#
# ============================================================
# RULE 6: e-notation handling
# ============================================================
#
# e-notation (1.5e10, 2.4e-15) is a CALCULATOR format, not typesetting.
# In body text, ALWAYS convert to math form:
#
#   WRONG:  h_c = 2.4e-15 at f_yr
#   WRONG:  a_0 = 1.20e-10 m/s²
#   RIGHT:  $h_c = 2.4 \times 10^{-15}$ at $f_{yr}$
#   RIGHT:  $a_0 = 1.20 \times 10^{-10}$ m/s²
#
# EXCEPTIONS (e-notation OK):
#   - CODE BLOCKS: code is code, keep e-notation
#   - TABLE CELLS: e-notation is compact and readable
#     (but prefer $N \times 10^{M}$ for cross-document consistency)
#
# ============================================================
# RULE 7: Symbol conventions
# ============================================================
#
# SOLAR MASS: use $\odot$ (LaTeX), not Unicode ☉ or M_sun plain text
#   WRONG:  M_sun, M_☉, M☉
#   RIGHT:  $M_\odot$
#
# EM-DASH / EN-DASH:
#   - EM-DASH (—): for breaks in text, plain Unicode OK
#   - EN-DASH (–): for RANGES in text or math
#     WRONG:  10^5-10^7
#     WRONG:  $10^5$-$10^7$
#     WRONG:  $10^{5}$--$10^{7}$  (split math, breaks on github mobile)
#     WRONG:  $10^{5}$\text{--}$10^{7}$  (text{--} is plain '--' on mobile)
#     WRONG:  $10^{5}\text{--}10^{7}$  (\text{--} shows as '--' on github mobile)
#     RIGHT:  $10^{5}$–$10^{7}$  (Unicode en-dash between two math blocks)
#     RIGHT:  $10^{5}–10^{7}$  (Unicode en-dash inside single math block)
#     RIGHT:  10^5 to 10^7        (in text)
#
# The Unicode en-dash character (–) is the most reliable for github mobile.
# It renders correctly in: PDF (as en-dash), github desktop, github mobile, Markor.
#
# GITHUB MOBILE GOTCHA: split math ranges like $X$--$Y$ (separate
# math blocks joined by '--') get rendered as plain text on github
# mobile. The en-dash becomes ' - -' and the entire expression
# displays as broken. Use $X\text{--}Y$ (single math block) instead.
# This pattern was found in lines like:
#   ($10^{5}$--$10^{7}\,M_\odot$): → ($10^{5}\text{--}10^{7}\,M_\odot$)
#   $M_{dyn}/M_b \sim 1$--$1700$ → $M_{dyn}/M_b \sim 1\text{--}1700$
#
# GITHUB MOBILE GOTCHA #2: $X$ immediately after '(' is sometimes EATEN.
# Even with parens inside math like $(X\text{--}Y)$, github mobile
# can fail to render correctly. The first '$' gets eaten and the
# whole block falls back to plain text. SAFER alternatives:
#   - Remove the parens entirely and use a colon:
#     **Name:** $X\text{--}Y$\text{ }unit
#   - Use a different separator (em-dash, hyphen, etc.)
#   - Put the parens deep inside the math: \text{(}X\text{)}
# This pattern was found in README galaxy bullets (lines 283-289).
#
# GITHUB MOBILE/DESKTOP GOTCHA #3: '-' (hyphen-minus) inside math is
# rendered as en-dash ('–') by GitHub's KaTeX rendering. This is
# DOCUMENTED behavior per:
#   https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions
# The official docs even show the example "x − y" (which is
# literally '- 1' rendered as en-dash).
# 
# For SIDC's purposes, we want MINUS, not en-dash, in some contexts:
#   $b^2 = -1$       → renders as "b² = – 1" (en-dash, wrong for us)
#   $\sim -12$     → renders as "~ – 12" (en-dash, wrong for us)
#   $w_0 = -0.84$   → renders as "w₀ = – 0.84" (also en-dash per docs)
# 
# The user's working example "w_0 = -0.84" is actually PLAIN TEXT (not
# in $...$), so it renders as a normal minus. To make SIDC's math
# render correctly:
# 
# FIX #1 (PREFERRED for in-line expressions): Use plain text
# with hyphen-minus (or with .0 for integers to match decimal style).
#   b² = -1.0      (renders as proper minus, matches -0.84 style)
#   log g_bar ~ -12.0   (renders as proper minus, matches -0.84 style)
#   w₀ = -0.84      (plain text, no $ delimiters)
# 
# The reason: GitHub's KaTeX rendering intentionally shows math minus
# as en-dash (per official docs). Plain text bypasses this and renders
# as a normal minus sign.
# 
# Use this for INLINE expressions (within a larger sentence/text).
# When the expression is part of other prose, use plain text. Examples:
#   "b = i is natural ... — b² = -1.0, $Q = 0$, $c = 1 ✓"
#   "RAR extends to log $g_\\rm bar$ ~ -12.0 (MIGHTEE-HI 2025)"
# The expressions are INLINE with other text, not standalone.
# 
# FIX #2: Use Unicode minus (U+2212 '−') inside $...$ math:
#   $b^2 = −1$     (renders as proper minus)
#   $\sim −12$   (renders as proper minus)
# 
# Use this for LONGER expressions that need to be in math mode for
# other reasons (subscripts, superscripts, fractions, etc.)
# Example: "$g_\\rm bar = 10^{-12}$ m/s²" (MUST be in math)
# 
# Both fixes produce proper minus on github mobile AND desktop.
# This was found in README line 102, 105, 109, 925.
#
# GITHUB MOBILE/DESKTOP GOTCHA #4: $\\sim$ and $\\to$ inside math are
# sometimes rendered as literal '\sim' and '\to' text on github
# desktop (and possibly mobile). The fix is to AVOID using these
# specific LaTeX commands inline in math mode. Use Unicode or split:
#   $A_{event} \\sim 67$        → $A_{event}$ ~ 67  (plain tilde)
#   $\\sim 10^{6}$ old stars    → ~ $10^{6}$ old stars
#   $\\to$ next                → → (Unicode arrow) OR ~> (plain text)
#   $m_{3+1D} \\to$ m          → $m_{3+1D}$ → m
# Why: the GitHub KaTeX renderer seems to have inconsistent handling
# of these two specific commands. Splitting into multiple math blocks
# or using Unicode is more reliable.
# Found in README line 24, 65, 101, 593, 828, 836, etc.
#
# GITHUB MOBILE/DESKTOP GOTCHA #5: math inside italic (*...*) AND
# italic markers (*) adjacent to math ($...$) may render as literal
# text on github desktop. There are TWO sub-issues:
#
# (a) Math INSIDE *...* italic:
#     *incl. $A_{event}$ ~ 67*  → shows "$A_{event}$" as literal
#     Reason: github's markdown parser processes inline markdown
#     (italic, bold) BEFORE math. $ inside *...* is not recognized
#     as math boundaries.
#
# (b) Italic markers * adjacent to math:
#     *incl.* $A_{event}$ *~ 67*  → shows "*" as literal
#     Reason: even after splitting, the * right next to $...$ is
#     sometimes rendered as literal *.
#
# CLEANEST FIX: remove italic entirely from any line that has math.
# The italic styling is not worth the rendering bugs. For L24 of
# README, we removed the italic wrapper from the Version line.
#
# ALTERNATIVE: use HTML <em>text</em> instead of *text* for italic.
# HTML tags are processed AFTER math, so they don't interfere.
#
# Found in README line 24 (Version line). This is a generic gotcha
# for any math inside or adjacent to italic text.
#
# APPROXIMATELY EQUAL:
#   WRONG:  ≈ (Unicode)
#   WRONG:  ~ (tilde, not typeset)
#   RIGHT:  $\approx$
#   RIGHT:  $\sim$ (for "of order" / "approximately", different from $\approx$)
#
# MULTIPLICATION:
#   WRONG:  × (Unicode)
#   WRONG:  * (asterisk)
#   WRONG:  2.2 x 10^{-6}
#   RIGHT:  $\times$
#   RIGHT:  \cdot (for "dot product" / "concatenation")
#
# PLUS/MINUS:
#   WRONG:  ± (Unicode)
#   RIGHT:  $\pm$
#
# ============================================================
# RULE 8: Greek letters -- ALWAYS use \alpha not α
# ============================================================
#
#   WRONG:  α, β, γ (Unicode)
#   WRONG:  alpha, beta (plain English)
#   RIGHT:  $\alpha$, $\beta$, $\gamma$ (LaTeX)
#
# Common Greek letters in this paper:
#   α, β, γ, δ, ε, ζ, η, θ, ι, κ, λ, μ, ν, ξ, π, ρ, σ, τ, φ, χ, ψ, ω
#   Γ, Δ, Θ, Λ, Ξ, Π, Σ, Φ, Ψ, Ω
#
# ============================================================
# SUMMARY: the 8 rules
# ============================================================
#
#   RULE 1: ALL powers of 10 -> $10^{N}$ (no Unicode, no e-notation in body)
#   RULE 2: Physical quantities -> $X_{...}$ in math (no plain H_0)
#   RULE 3: Ratios -> $X/Y$ in math
#   RULE 4: $E^{N}$ always with braces
#   RULE 5: M^1.29 (name) vs E^1.29 (physics) -- both OK in context
#     - 'M^1.29' as plain text is the CANONICAL NAME of the scaling law
#       (e.g., headings: '## ⚖️ THE SCALING LAW: M^1.29 ACROSS ...')
#     - 'M^{1.29}' in math is the PHYSICS expression (e.g., equations)
#     - 'E^{1.29}' is the energy form (dimensionally equivalent via E=Mc²)
#     - WRONG: 'τ_{2D} ~ M^1.29' in math → renders as M^{1}.29
#       (only '1' is superscript, '.29' is plain text)
#     - RIGHT: 'τ_{2D} ∼ M^{1.29}' in math
#     Found in paper/01_executive_summary.md L81, paper/03_relations.md L3058/3066/3221/3229/3419
#   RULE 6: e-notation -> $\times 10^{...}$ in body text
#   RULE 7: ☉ for solar mass, -- for ranges, \approx for ≈
#   RULE 8: Greek letters always as \alpha not α
#
# CHECK BEFORE COMMITTING:
#   - Run: grep -nE '(^|[^$])[A-Za-z]+_[A-Za-z]+' paper/markdown/*.md
#     (find plain-text X_Y that should be in math)
#   - Run: grep -nE '(^|[^$])10\^[0-9]' paper/markdown/*.md
#     (find plain-text 10^N that should be in math)
#   - Run: grep -nE '[0-9]e[-+][0-9]' paper/markdown/*.md
#     (find e-notation in body text)
#
#
# ============================================================
# HISTORICAL CONTEXT: math notation cleanup (June 2026)
# ============================================================
#
# This section documents the JOURNEY of fixing math notation for
# github mobile rendering. The issue: math that worked in PDF and
# github desktop was BROKEN on github mobile. We went through 5
# iterations before finding the right answer.
#
# ATTEMPT 1: $X$--$Y$ (split math blocks joined by en-dash)
#   Issue: github mobile ate the first '$' after a '('
#   Result: $10^{5}$ rendered as plain "10^5" text
#   Lines affected: 283-289 in README (galaxy bullets)
#
# ATTEMPT 2: $(X$--$Y$) (parens inside math)
#   Issue: still had the paren-eating bug
#   Result: parens inside math didn't help
#
# ATTEMPT 3: $(X\text{--}Y)$ (use \text{--} in math)
#   Issue: github mobile rendered \text{--} as literal '--' (double dash!)
#   Result: still showed "--" instead of en-dash
#   Verified broken: this is what was visible in the screenshot
#
# ATTEMPT 4: **Name:** $X$--$Y$ (remove parens, use colon)
#   Issue: split math with '--' still showed double dash
#   Result: first '$' was OK but '--' rendered as "--"
#
# ATTEMPT 5: $X$–$Y$ (Unicode en-dash between math blocks) ✓ WORKS!
#   The Unicode en-dash character (U+2013) renders correctly EVERYWHERE:
#   - PDF (as en-dash in math mode)
#   - github desktop (as en-dash in math)
#   - github mobile (as en-dash, the only reliable approach!)
#   - Markor (as en-dash in math)
#   Lines fixed: README 283-289, 709-710, paper 04:19
#
# FINAL RULES:
#   - For RANGES in math: USE Unicode en-dash (–), NOT '--' or '\text{--}'
#   - For RANGES in text: just write "10^5 to 10^7"
#   - For RANGES in split math ($X$Y$): use en-dash BETWEEN blocks
#   - For parens around math: put them INSIDE math: $(X)$
#     OR avoid them entirely: use a colon separator instead
#
# LESSON: when in doubt, test on github MOBILE (the most restrictive
# renderer). If it works there, it works everywhere.
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
#   1. Look at paper/.build/xelatex1.log for the actual error
#   2. Find the LINE NUMBER in the error
#   3. Look at paper/.build/paper_full.tex at that line
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
#   2. Look at paper/.build/paper_full.tex size (should be < 2MB)
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

# =============================================================================
# CLI options
# =============================================================================
DRY_RUN=false
DRY_FILES=""

usage() {
    cat << 'USAGE_EOF'
Usage: bash paper/build_pdf.sh [OPTIONS]

Options:
  --dry-run [FILE...]   Run pandoc + post-processors + xelatex on FILE...
                        (default: README.md supporting/layman_summary.md)
                        Skips the full paper build. Use this to find LaTeX
                        issues in non-paper markdown files (README, layman
                        summary, etc.) without doing a full 30-60s build.
  --help, -h            Show this help.

Examples:
  bash paper/build_pdf.sh                       # full paper build
  bash paper/build_pdf.sh --dry-run             # check README + layman
  bash paper/build_pdf.sh --dry-run README.md   # check just README
  bash paper/build_pdf.sh --dry-run \
      README.md changelog.md                    # check multiple

USAGE_EOF
}

# Parse args
while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run)
            DRY_RUN=true
            shift
            # Collect any file args after --dry-run
            while [[ $# -gt 0 && "$1" != --* && "$1" != -* ]]; do
                DRY_FILES="$DRY_FILES $1"
                shift
            done
            # Default dry-run files
            if [ -z "$DRY_FILES" ]; then
                DRY_FILES="README.md supporting/layman_summary.md"
            fi
            ;;
        --help|-h)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

PAPER_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PAPER_DIR"

# Build scratch dir: keep all intermediate files inside the paper/ folder
# so they survive across sessions (unlike /tmp which is wiped).
# Gitignored via .gitignore.
BUILD_DIR="${PAPER_DIR}/.build"
TOOLS_DIR="${PAPER_DIR}/build_tools"
mkdir -p "$BUILD_DIR"

# =============================================================================
# DRY-RUN MODE
# =============================================================================
# Run pandoc + 4 post-processors + xelatex on a small set of files to find
# LaTeX issues without doing the full paper build. Useful for README/layman.
if [ "$DRY_RUN" = true ]; then
    # In dry-run, change to the repo root (one above paper/) so we can find
    # README.md, layman_summary.md, etc. that live at the top of the repo.
    REPO_ROOT="$(cd "${PAPER_DIR}/.." && pwd)"
    cd "$REPO_ROOT"

    echo "[DRY-RUN mode]"
    echo "[Files:$DRY_FILES]"
    echo "[Repo root: $REPO_ROOT]"
    echo "[Build dir: $BUILD_DIR]"
    echo ""

    # Concatenate the requested files
    cat $DRY_FILES > "${BUILD_DIR}/dry_combined.md"
    SOURCE="${BUILD_DIR}/dry_combined.md"

    # Step 1: pandoc
    # Use --no-highlight to skip code-block syntax highlighting (which would
    # need minted/highlighting-kate/Highlight.js setup). Code blocks render
    # as plain monospace, which is what we want for a dry-run check.
    echo "[1/6] pandoc..."
    pandoc "$SOURCE" -o "${BUILD_DIR}/paper_body.tex" \
        -f markdown+grid_tables+pipe_tables+raw_tex-yaml_metadata_block \
        --no-highlight || {
        echo "    pandoc FAILED"
        exit 1
    }

    # Steps 2-5: the 4 post-processors
    echo "[2/6] wrap_dimexpr..."
    python3 "${TOOLS_DIR}/wrap_dimexpr.py" "$BUILD_DIR" || true

    echo "[3/6] use_linewidth..."
    python3 "${TOOLS_DIR}/use_linewidth.py" "$BUILD_DIR" || true

    echo "[4/6] fix_dashes..."
    python3 "${TOOLS_DIR}/fix_dashes.py" "$BUILD_DIR" || true

    echo "[5/6] fix_sigma..."
    python3 "${TOOLS_DIR}/fix_sigma.py" "$BUILD_DIR" || true

    # Step 6: xelatex (single run, halts on error so we see them)
    echo "[6/6] xelatex..."
    cat > "${BUILD_DIR}/paper_header.tex" << 'HDR_EOF'
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
\usepackage{framed}   % for Shaded code-block env (from README/layman)
\geometry{margin=1in}
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
\providecommand{\tightlist}{}
\title{[DRY-RUN: pre-build check]}
\begin{document}
\maketitle
HDR_EOF

    cat "${BUILD_DIR}/paper_header.tex" "${BUILD_DIR}/paper_body.tex" > "${BUILD_DIR}/dry_full.tex"
    echo '\end{document}' >> "${BUILD_DIR}/dry_full.tex"

    cd "$BUILD_DIR"
    xelatex -interaction=nonstopmode -halt-on-error dry_full.tex > "${BUILD_DIR}/dry_xelatex.log" 2>&1 || {
        echo ""
        echo "=========================================="
        echo "  XELATEX FAILED — here's the error:"
        echo "=========================================="
        grep -E "^!|^l\." "${BUILD_DIR}/dry_xelatex.log" | head -20
        echo ""
        echo "Full log: ${BUILD_DIR}/dry_xelatex.log"
        echo "TeX file: ${BUILD_DIR}/dry_full.tex (find the line above)"
        exit 1
    }

    echo ""
    echo "=========================================="
    echo "  DRY-RUN SUCCESS"
    echo "=========================================="
    echo "Output: ${BUILD_DIR}/dry_full.pdf"
    echo "TeX:    ${BUILD_DIR}/dry_full.tex"
    echo "Log:    ${BUILD_DIR}/dry_xelatex.log"
    pdfinfo "${BUILD_DIR}/dry_full.pdf" | grep -E "Pages|Size" 2>/dev/null || true
    exit 0
fi


# Step 0: Combine markdown files
if [ -d "markdown" ]; then
    cat markdown/*.md > "${BUILD_DIR}/paper_combined.md"
    SOURCE="${BUILD_DIR}/paper_combined.md"
else
    SOURCE=paper.md
fi

# Step 1: Convert with markdown+grid_tables+pipe_tables+raw_tex-yaml_metadata_block
# See section 1 above for why these specific options.
pandoc "$SOURCE" -o "${BUILD_DIR}/paper_body.tex" -f markdown+grid_tables+pipe_tables+raw_tex-yaml_metadata_block

# Post-processor 1: wrap \real{N} in \dimexpr
# Pandoc generates: p{(\columnwidth - 4\tabcolsep) * \real{0.4375}}
# We want:         p{\dimexpr(\columnwidth - 4\tabcolsep)*0.4375\relax}
# See build_tools/wrap_dimexpr.py for details.
python3 "${TOOLS_DIR}/wrap_dimexpr.py" "$BUILD_DIR"

# Post-processor 2: convert \dimexpr(...) to \linewidth
# This is the v3.0.21 fix for the silent table-breaking bug.
# See section 3 above for the full explanation.
# See build_tools/use_linewidth.py for details.
python3 "${TOOLS_DIR}/use_linewidth.py" "$BUILD_DIR"

# Post-processor 3: fix en-dash in math mode
# Pandoc converts "1-2" in math cells to "1--2" (en-dash).
# This breaks math mode. Fix: "1--2" → "1-2" in math cells.
# See build_tools/fix_dashes.py for details.
python3 "${TOOLS_DIR}/fix_dashes.py" "$BUILD_DIR"

# Post-processor 4: fix \sigma\^{}{N} patterns
# Pandoc generates \sigma\^{}{N} (empty arg hat) which is invalid.
# Fix: \sigma\^{}{N} → \sigma^{N}
# See build_tools/fix_sigma.py for details.
python3 "${TOOLS_DIR}/fix_sigma.py" "$BUILD_DIR"

# Step 2: Strip the first \section{...}
# The title is already in the LaTeX header, so we don't want it twice.
python3 -c "
import re, sys
build_dir = sys.argv[1]
with open(f'{build_dir}/paper_body.tex', 'r') as f:
    body = f.read()
m = re.search(r'\\\\section\\{[^}]+\\}\\s*\\n\\n', body)
if m:
    body = body[m.end():]
with open(f'{build_dir}/paper_body_clean.tex', 'w') as f:
    f.write(body)
" "$BUILD_DIR"

# Step 3: Create header
# The LaTeX preamble. The packages here are required - see section 1 above.
cat > "${BUILD_DIR}/paper_header.tex" << 'HEADEREOF'
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
cat "${BUILD_DIR}/paper_header.tex" "${BUILD_DIR}/paper_body_clean.tex" > "${BUILD_DIR}/paper_full.tex"
echo '\end{document}' >> "${BUILD_DIR}/paper_full.tex"

cd "$BUILD_DIR"
# Run xelatex TWICE: first to generate aux files, second to resolve cross-refs
xelatex -interaction=nonstopmode -halt-on-error paper_full.tex > "${BUILD_DIR}/xelatex1.log" 2>&1 || {
    echo "First xelatex run failed. Tail of log:"
    tail -30 "${BUILD_DIR}/xelatex1.log"
    exit 1
}
xelatex -interaction=nonstopmode -halt-on-error paper_full.tex > "${BUILD_DIR}/xelatex2.log" 2>&1 || {
    echo "Second xelatex run failed. Tail of log:"
    tail -30 "${BUILD_DIR}/xelatex2.log"
    exit 1
}

cp "${BUILD_DIR}/paper_full.pdf" "${PAPER_DIR}/paper.pdf"
echo "Paper PDF built: ${PAPER_DIR}/paper.pdf"
ls -la "${PAPER_DIR}/paper.pdf"
