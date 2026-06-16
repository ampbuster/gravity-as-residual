#!/bin/bash
# build_pdf.sh - Build the paper PDF from paper/markdown/*.md files

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

# Step 1: Convert with markdown+grid_tables+pipe_tables+raw_tex-yaml_metadata_block (original setting)
pandoc "$SOURCE" -o /tmp/paper_body.tex -f markdown+grid_tables+pipe_tables+raw_tex-yaml_metadata_block

# Post-process: wrap p{(\\columnwidth - X\\tabcolsep) * N} in \\dimexpr
python3 /tmp/wrap_dimexpr.py

# Post-process: fix \\$N--N\\$ → \\$N-N\\$
python3 /tmp/fix_dashes.py

# Post-process: fix \\^{}{N} and \\sigma\\^{}{N} patterns
python3 /tmp/fix_sigma.py

# Post-process: wrap p{(\columnwidth - X\tabcolsep) * N} in \dimexpr


# Step 2: Strip the first \section{...}
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
\date{v3.0.15 (June 2026) \\ \small \url{https://github.com/ampbuster/gravity-as-residual}}
\begin{document}
\maketitle
\tableofcontents
\newpage
HEADEREOF

# Step 4: Combine and compile
cat /tmp/paper_header.tex /tmp/paper_body_clean.tex > /tmp/paper_full.tex
echo '\end{document}' >> /tmp/paper_full.tex

cd /tmp
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
