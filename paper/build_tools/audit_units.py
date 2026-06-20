#!/usr/bin/env python3
"""
audit_units.py - Audit tables for bare numbers that should have units
====================================================================

USAGE:
  python3 audit_units.py           # audit all files
  python3 audit_units.py <file>    # audit specific file

GOAL:
  Find table columns where:
  1. The header has a physical unit (yr, s, km/s, kpc, etc.)
  2. BUT the values are bare numbers (lost unit context)

  This catches cases like:
  | Header: "r (kpc)" | Value: "8" |   <- unit missing in value
  | Header: "σ (km/s)" | Value: "2.7" | <- unit missing in value

WHAT IT SKIPS:
  - Dimensionless counts (row #s, N_sub, N_orbits, f_mix)
  - Ratios and fractions (M_dyn/M_b, S_8, r(z))
  - Logs (log M*, log M_b)
  - Cells where unit IS in the value (e.g., "33 s", "$10^{44}$ J")
  - Cells with "varies", "—", "n/a" etc.

OUTPUT:
  Prints lines like:
    paper/markdown/03b_predictions.md:L431 col4: header='σ (km/s)', 6 bare values: ['2.7', '5.0', ...]
"""

import os
import re
import sys

# Recognized physical units (case-sensitive, must be SHORT - no prose)
UNITS = [
    # Time
    r's', r'sec', r'min', r'hr', r'hour', r'day', r'week', r'month',
    r'yr', r'year', r'Gyr', r'Myr', r'kyr', r'ms', r'μs', r'ns', r'ps',
    # Length
    r'm', r'cm', r'mm', r'km', r'μm', r'nm', r'pm', r'fm',
    r'Mpc', r'kpc', r'pc', r'ly', r'AU', r'au',
    # Energy/Mass
    r'GeV', r'MeV', r'keV', r'eV', r'TeV', r'J', r'erg', r'cal', r'kW', r'W',
    # Mass
    r'kg', r'g', r'mg', r't',
    # Frequency
    r'Hz', r'kHz', r'MHz', r'GHz', r'THz',
    # Temperature
    r'K', r'°C', r'°F',
    # Percent
    r'%', r'percent',
    # Solar mass
    r'M_\odot', r'M_sun',
]


def is_real_unit(s):
    """Check if s is a SHORT physical unit (not prose like 'Value', 'Brane')."""
    s = s.strip()
    if not s or len(s) > 15:
        return False
    # Known simple units (exact match)
    simple = ['s', 'sec', 'min', 'hr', 'hour', 'day', 'week', 'month',
              'yr', 'year', 'Gyr', 'Myr', 'kyr', 'ms', 'μs', 'ns', 'ps',
              'm', 'cm', 'mm', 'km', 'μm', 'nm', 'pm', 'fm',
              'Mpc', 'kpc', 'pc', 'ly', 'AU', 'au',
              'GeV', 'MeV', 'keV', 'eV', 'TeV', 'J', 'erg', 'cal', 'kW', 'W',
              'kg', 'g', 'mg', 't',
              'Hz', 'kHz', 'MHz', 'GHz', 'THz',
              'K', '%', 'percent', '°C', '°F']
    if s in simple:
        return True
    # Solar mass (must be exactly right)
    if s in ['M_\\odot', 'M_sun']:
        return True
    # Compound with /: km/s, km/s/Mpc
    if re.match(r'^[a-zA-Z]+(\^[a-zA-Z0-9{}+\-]+)?(/[a-zA-Z]+(\^[a-zA-Z0-9{}+\-]+)?)+$', s):
        return True
    # Math style with ^ or {}: cm^{-3}, GeV/c^2
    if '^' in s or '{' in s:
        if re.match(r'^[a-zA-Z]+(\^[\{]?[+\-]?\d+[\}]?)?(/\w+(\^[\{]?[+\-]?\d+[\}]?)?)?$', s):
            return True
    return False


def has_unit(s):
    """Check if string contains a physical unit."""
    # Check parens for explicit unit
    m = re.search(r'\(([^)]+)\)', s)
    if m and is_real_unit(m.group(1).strip()):
        return True
    # Check words
    words = re.findall(r'\b[\w/°^]+\b', s)
    for w in words:
        if is_real_unit(w):
            return True
    # Math style: \text{s}, \text{min}, etc.
    if re.search(r'\\text\{[^}]*(s|min|hr|yr|J|GeV)', s):
        return True
    return False


def is_bare_number(cell):
    """Check if cell is a bare number (no unit)."""
    cell = cell.strip()
    if not cell or cell in ['—', '–', '-', 'N/A', 'n/a']:
        return False
    if not re.search(r'\d', cell):
        return False
    if has_unit(cell):
        return False
    return True


def find_tables(lines):
    """Find all table regions (consecutive lines with |)."""
    tables = []
    in_table = False
    start = 0
    for i, line in enumerate(lines):
        if '|' in line and line.count('|') >= 2:
            if not in_table:
                start = i
                in_table = True
        else:
            if in_table:
                if i - start >= 3:
                    tables.append((start, i))
                in_table = False
    if in_table:
        tables.append((start, len(lines)))
    return tables


def audit_file(filepath):
    """Audit one file, return list of issues."""
    with open(filepath, 'r') as f:
        content = f.read()
    lines = content.split('\n')
    tables = find_tables(lines)
    
    issues = []
    for start, end in tables:
        sep_row = None
        for r in range(start, end):
            if '---' in lines[r] or '===' in lines[r]:
                sep_row = r
                break
        if sep_row is None:
            continue
        header_cells = [c.strip() for c in lines[start].split('|')]
        
        for j, hcell in enumerate(header_cells):
            if not has_unit(hcell):
                continue  # Header has no unit - skip
            
            bare_count = 0
            total_with_number = 0
            sample_bare = []
            for r in range(sep_row+1, end):
                cells = [c.strip() for c in lines[r].split('|')]
                if len(cells) > j:
                    v = cells[j]
                    if re.search(r'\d', v):
                        total_with_number += 1
                        if is_bare_number(v):
                            bare_count += 1
                            if len(sample_bare) < 5:
                                sample_bare.append(v)
            
            # Flag if header has unit AND ALL values are bare
            if bare_count >= 2 and bare_count == total_with_number:
                issues.append((start+1, j+1, hcell, sample_bare, bare_count))
    
    return issues


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        # Default: all paper markdown files
        files = []
        for root, dirs, fs in os.walk('paper/markdown'):
            for f in fs:
                if f.endswith('.md'):
                    files.append(os.path.join(root, f))
        files += ['README.md', 'changelog.md', 'persistent_memory.md', 'STATE_OF_THE_MODEL.md']
    
    all_issues = {}
    for fp in files:
        if not os.path.exists(fp):
            print(f"SKIP: {fp} (not found)")
            continue
        issues = audit_file(fp)
        if issues:
            all_issues[fp] = issues
    
    total = sum(len(v) for v in all_issues.values())
    print(f"=== UNIT AUDIT: {total} issues across {len(all_issues)} files ===\n")
    
    for fp, issues in all_issues.items():
        print(f"\n{fp}: {len(issues)} issues")
        for line, col, header, sample, count in issues:
            print(f"  L{line} col{col}: header={header!r}")
            print(f"    {count} bare values: {sample}")
    
    if total == 0:
        print("✓ All tables have consistent units (header matches cells)")


if __name__ == '__main__':
    main()
