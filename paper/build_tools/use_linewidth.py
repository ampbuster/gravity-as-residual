#!/usr/bin/env python3
"""Convert \\dimexpr(...) column specs to \\linewidth (simpler, no \\real needed)"""
import re
import sys

BUILD_DIR = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
INPUT = f'{BUILD_DIR}/paper_body.tex'

with open(INPUT, 'r') as f:
    c = f.read()

# Replace \dimexpr(...) with linewidth
# Pattern in the file: p{\dimexpr(\columnwidth - 4\tabcolsep)*0.4375\relax}
# Want to extract: 0.4375 and replace with: 0.4375\linewidth
pattern = r"\\dimexpr\([^)]+\)\*([0-9.]+)\\relax"
replacement = r"\1\\linewidth"
c_new = re.sub(pattern, replacement, c)

n_changed = c.count("\\dimexpr") - c_new.count("\\dimexpr")
print(f"Converted {n_changed} \\dimexpr column specs to \\linewidth")

with open(INPUT, 'w') as f:
    f.write(c_new)
