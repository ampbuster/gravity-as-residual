#!/bin/bash
# build_pdf.sh - Build the paper PDF from paper.md (or paper/markdown/*.md)
#
# Usage: ./build_pdf.sh
#
# Requires: pandoc, xelatex (TeX Live with fontspec)
#
# Output: paper.pdf (in same directory)
#
# Note: The paper uses Unicode superscripts (10^-50, 10^-85, etc.) which
# require xelatex with Unicode font support, NOT pdflatex.
#
# v3.0.13+: paper.md is now split into paper/markdown/*.md files.
# If paper/markdown/ exists, files are concatenated in order.
# If paper/markdown/ doesn't exist, falls back to paper.md.

set -e

# Resolve script's own directory
PAPER_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PAPER_DIR"

# Step 0: If paper/markdown/ exists, combine into a single file
if [ -d "markdown" ]; then
    echo "Combining markdown/*.md into combined source..."
    # Concatenate all .md files in alphabetical order (00_, 01_, ...).
    # The <!-- comments at the top of each file are HTML comments and
    # are stripped by pandoc automatically.
    cat markdown/*.md > /tmp/paper_combined.md
    PAPER_SOURCE=/tmp/paper_combined.md
else
    PAPER_SOURCE=paper.md
fi

# Step 1: Convert paper.md to body.tex via pandoc (markdown_strict to avoid YAML parse issues)
pandoc "$PAPER_SOURCE" -o /tmp/paper_body.tex -f markdown_strict

# Step 2: Strip the first \section{...} (we have \title{} in the header)
python3 << 'PYEOF'
import re
with open('/tmp/paper_body.tex', 'r') as f:
    body = f.read()

# Remove first \section{...} block (the H1 title)
m = re.search(r'\\section\{[^}]+\}\s*\n\n', body)
if m:
    body = body[m.end():]

with open('/tmp/paper_body_clean.tex', 'w') as f:
    f.write(body)
print(f"Body length after stripping: {len(body)} chars")
PYEOF

# Step 3: Create header.tex with Unicode support
cat > /tmp/paper_header.tex << 'HEADEREOF'
\documentclass[10pt]{article}
\usepackage{amsmath, amssymb}
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
\date{v2.7.4 (June 2026) \\ \small \url{https://github.com/ampbuster/gravity-as-residual}}
\begin{document}
\maketitle
\tableofcontents
\newpage
HEADEREOF

# Step 4: Combine and compile
cat /tmp/paper_header.tex /tmp/paper_body_clean.tex > /tmp/paper_full.tex
echo '\end{document}' >> /tmp/paper_full.tex

# Compile with xelatex (Unicode support for superscripts)
cd /tmp
xelatex -interaction=nonstopmode -halt-on-error paper_full.tex > /tmp/xelatex1.log 2>&1 || {
    echo "First xelatex run failed. Tail of log:"
    tail -30 /tmp/xelatex1.log
    exit 1
}

# Second run for table of contents
xelatex -interaction=nonstopmode -halt-on-error paper_full.tex > /tmp/xelatex2.log 2>&1 || {
    echo "Second xelatex run failed. Tail of log:"
    tail -30 /tmp/xelatex2.log
    exit 1
}

# Copy result back
cp /tmp/paper_full.pdf "${PAPER_DIR}/paper.pdf"
echo ""
echo "✓ Paper PDF built: ${PAPER_DIR}/paper.pdf"
ls -la "${PAPER_DIR}/paper.pdf"
