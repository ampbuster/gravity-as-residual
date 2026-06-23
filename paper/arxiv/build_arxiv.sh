#!/bin/bash
# build_arxiv.sh - Build the arxiv condensed paper PDF
# =====================================================================

set -e

ARXIV_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ARXIV_DIR"

echo "==========================================="
echo "Building arXiv condensed paper PDF"
echo "==========================================="
echo ""

# Check for required tools
command -v pandoc >/dev/null 2>&1 || { echo "ERROR: pandoc not installed"; exit 1; }
command -v xelatex >/dev/null 2>&1 || { echo "ERROR: xelatex not installed"; exit 1; }

# Build dir
BUILD_DIR="$ARXIV_DIR/.build"
mkdir -p "$BUILD_DIR"

# Check for lmodern package - if missing, use a different font setup
LMODERN_PATH=$(kpsewhich lmodern.sty 2>/dev/null || echo "")
HAVE_LMODERN=""
if [ -n "$LMODERN_PATH" ]; then
    HAVE_LMODERN="yes"
    echo "[1/5] lmodern.sty found: $LMODERN_PATH"
else
    echo "[1/5] lmodern.sty NOT found - will use DejaVu fonts (no lmodern dependency)"
fi

# Step 1: Generate header.tex with our font setup (no lmodern dependency)
echo "[2/5] Generating header.tex..."
cat > "$BUILD_DIR/header.tex" <<'EOF'
\documentclass[11pt,a4paper]{article}

\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{calc}

% Font setup (no lmodern dependency)
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}

% Make tables look nice
\renewcommand{\arraystretch}{1.2}

% Pandoc compatibility - pandoc emits \tightlist but no preamble
\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}

% Pandoc emits \pandocbounded but no preamble
\providecommand{\pandocbounded}[1]{#1}

% Title
\title{\textbf{Gravity as Residual: A Thought Experiment on Dimensional Inversion, Annihilation, and the Origin of the Dark Sector}}
\author{ampbuster \\ \small Independent Researcher}
\date{June 23, 2026}

\begin{document}
\maketitle
EOF
echo ""

# Step 2: Convert paper.md to LaTeX body
echo "[3/5] Converting paper.md to LaTeX..."
pandoc paper.md \
    -f markdown+grid_tables+pipe_tables+raw_tex-yaml_metadata_block \
    -t latex \
    --no-highlight \
    -o "$BUILD_DIR/body.tex" || { echo "    pandoc FAILED"; exit 1; }

# Check for math balance
echo "    Checking math balance..."
SINGLE_DOLLARS=$(grep -o '\$[^$]*\$' "$BUILD_DIR/body.tex" | wc -l)
echo "    Math expressions: $SINGLE_DOLLARS"

# Step 3: Combine header + body + trailer
echo "[4/5] Combining document..."
cat > "$BUILD_DIR/footer.tex" <<'EOF'

\end{document}
EOF

cat "$BUILD_DIR/header.tex" "$BUILD_DIR/body.tex" "$BUILD_DIR/footer.tex" > "$BUILD_DIR/full.tex"

# Step 4: Compile with xelatex
echo "[5/5] Compiling with xelatex..."
cd "$BUILD_DIR"
xelatex -interaction=nonstopmode -halt-on-error full.tex > xelatex.log 2>&1 || {
    echo "    xelatex FAILED"
    echo "    Errors:"
    grep -E "^!|^l\." xelatex.log | head -20
    echo ""
    echo "    Full log: $BUILD_DIR/xelatex.log"
    exit 1
}

# Run xelatex twice for cross-references
xelatex -interaction=nonstopmode full.tex > xelatex_run2.log 2>&1 || {
    echo "    xelatex run 2 FAILED (warnings only)"
}

# Check output
if [ -f "full.pdf" ]; then
    PAGES=$(pdfinfo full.pdf 2>/dev/null | grep "Pages:" | awk '{print $2}')
    SIZE=$(ls -la full.pdf | awk '{print $5}')
    SIZE_KB=$((SIZE / 1024))
    echo ""
    echo "==========================================="
    echo "BUILD SUCCESS!"
    echo "Pages: $PAGES"
    echo "Size:  ${SIZE_KB} KB"
    echo "File:  $BUILD_DIR/full.pdf"
    echo "==========================================="
    
    # Copy to arxiv directory for easy access
    cp full.pdf "$ARXIV_DIR/paper_arxiv.pdf"
    echo "Copied to: $ARXIV_DIR/paper_arxiv.pdf"
else
    echo "BUILD FAILED: full.pdf not created"
    exit 1
fi