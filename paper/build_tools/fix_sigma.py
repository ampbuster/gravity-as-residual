#!/usr/bin/env python3
"""Fix pandoc's \\sigma\\^{}{N} and \\sigma\\^{}N patterns"""
import re
import sys

BUILD_DIR = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
INPUT = f'{BUILD_DIR}/paper_body.tex'

with open(INPUT, 'r') as f:
    content = f.read()

# \sigma\^{}{N} -> \sigma^{N}
# \sigma\^{}N -> \sigma^{N}
new_content = re.sub(r'\\sigma\\\^\{\}(\d+)', r'\\sigma^{\1}', content)
new_content = re.sub(r'\\sigma\\\^\{\}\{\}', r'\\sigma', new_content)

with open(INPUT, 'w') as f:
    f.write(new_content)

print(f"Fixed sigma patterns in {INPUT}")
