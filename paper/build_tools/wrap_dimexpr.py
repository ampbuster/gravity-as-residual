#!/usr/bin/env python3
"""Convert p{(\\columnwidth - N\\tabcolsep)*\\real{X}} to p{\\dimexpr(...)*X\\relax}"""
import re
import sys

# Use build dir if provided, else /tmp
BUILD_DIR = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
INPUT = f'{BUILD_DIR}/paper_body.tex'

with open(INPUT, 'r') as f:
    content = f.read()

# Pattern matches: p{(\columnwidth - N\tabcolsep) * \real{X}}
# Optionally preceded by >{...} column prefix.
# The opening `p{` may follow `>{...}` (a column specifier).
pattern = r'(>?\{[^}]*\})?p\{\((\\columnwidth) - (\d+)(\\tabcolsep)\) \* \\real\{([\d.]+)\}\}'

def replace_one(m):
    prefix = m.group(1) or ''
    columnwidth = m.group(2)
    n = m.group(3)
    tabcolsep = m.group(4)
    x = m.group(5)
    return f'{prefix}p{{\\dimexpr({columnwidth} - {n}{tabcolsep})*{x}\\relax}}'

new_content = re.sub(pattern, replace_one, content)

with open(INPUT, 'w') as f:
    f.write(new_content)

# Count actual replacements in the *original* content (before mutation)
n_replaced = len(re.findall(pattern, content))
print(f"Wrapped {n_replaced} dimexpr expressions in {INPUT}")
