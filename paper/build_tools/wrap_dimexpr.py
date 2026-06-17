#!/usr/bin/env python3
"""Convert p{(\\columnwidth - N\\tabcolsep)*\\real{X}} to p{\\dimexpr(...)*X\\relax}"""
import re
import sys

# Use build dir if provided, else /tmp
BUILD_DIR = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
INPUT = f'{BUILD_DIR}/paper_body.tex'

with open(INPUT, 'r') as f:
    content = f.read()

# Simpler pattern matching the literal text
# p{(\columnwidth - 4\tabcolsep) * \real{0.2727}}
pattern = r'p\{\((\\columnwidth) - (\d+)(\\tabcolsep)\) \* \\real\{([\d.]+)\}\}'

def replace_one(m):
    columnwidth = m.group(1)
    n = m.group(2)
    tabcolsep = m.group(3)
    x = m.group(4)
    return f'p{{\\dimexpr({columnwidth} - {n}{tabcolsep})*{x}\\relax}}'

new_content = re.sub(pattern, replace_one, content)

with open(INPUT, 'w') as f:
    f.write(new_content)

n_replaced = len(re.findall(pattern, content))
print(f"Wrapped {n_replaced} dimexpr expressions in {INPUT}")
