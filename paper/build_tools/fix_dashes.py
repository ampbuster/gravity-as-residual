#!/usr/bin/env python3
"""Fix pandoc's en-dash 1--2 -> 1-2 in math cells"""
import re
import sys

BUILD_DIR = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
INPUT = f'{BUILD_DIR}/paper_body.tex'

with open(INPUT, 'r') as f:
    content = f.read()

# Replace en-dashes (--) with single hyphens in math environments
# Be careful: -- in LaTeX text is en-dash, but we want plain range separator
new_content = re.sub(r'(\d)--(\d)', r'\1-\2', content)

with open(INPUT, 'w') as f:
    f.write(new_content)

print(f"Fixed en-dash ranges in {INPUT}")
