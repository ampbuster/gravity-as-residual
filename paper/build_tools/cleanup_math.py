#!/usr/bin/env python3
"""
cleanup_math.py - Run all math cleanup scripts in sequence
==================================================================

Master script that runs the math cleanup tools in the correct order:
1. wrap_math_vars.py       - Wrap H_0, M_Pl, f_back, etc. in $...$
2. wrap_powers_of_10.py    - Convert 10^N to $10^{N}$
3. e_to_math.py            - Convert 1.5e10 to $1.5 \times 10^{10}$
4. greek_to_latex.py       - Convert α, β, γ to $\alpha$, $\beta$, $\gamma$
5. fix_greek_subscripts.py - Fix $\tau$_obs → $\tau_{\rm obs}$ patterns

Then builds the PDF and verifies.

Usage:
  python3 cleanup_math.py            # Run on paper/markdown/*.md
  python3 cleanup_math.py file.md    # Run on specific file
  python3 cleanup_math.py --build    # Run + build PDF
"""
import os
import sys
import subprocess

SCRIPTS = [
    ('wrap_math_vars.py', 'Wrap physics variables in math mode'),
    ('wrap_powers_of_10.py', 'Convert 10^N to $10^{N}$'),
    ('e_to_math.py', 'Convert e-notation to math form'),
    ('greek_to_latex.py', 'Convert Unicode Greek to LaTeX'),
    ('fix_greek_subscripts.py', 'Fix \\tau\_obs broken patterns'),
    ('fix_broken_markdown.py', 'Fix ** $math and ( $math patterns'),
]


def run_script(script_name, target=None):
    """Run a single script."""
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    if not os.path.exists(script_path):
        print(f"  WARNING: {script_name} not found")
        return 0

    cmd = ['python3', script_path]
    if target:
        cmd.append(target)

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERROR in {script_name}:")
        print(f"  stdout: {result.stdout}")
        print(f"  stderr: {result.stderr}")
        return 0
    # Get the "Total:" line from output
    output = result.stdout.strip()
    # Extract last number from "Total: N substitutions"
    if 'Total:' in output:
        try:
            return int(output.split('Total:')[1].split()[0])
        except (ValueError, IndexError):
            pass
    return 0


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else None
    build_pdf = '--build' in sys.argv

    print("="*72)
    print("MATH CLEANUP - running all scripts")
    print("="*72)
    print()

    total = 0
    for script, desc in SCRIPTS:
        print(f"[{script}] {desc}")
        n = run_script(script, target)
        print(f"  {n} substitutions")
        total += n
        print()

    print(f"="*72)
    print(f"TOTAL: {total} substitutions")
    print(f"="*72)

    if build_pdf:
        print("\nBuilding PDF...")
        result = subprocess.run(['bash', 'paper/build_pdf.sh'],
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("PDF build: SUCCESS")
        else:
            print("PDF build: FAILED")
            print(result.stderr[-500:] if len(result.stderr) > 500 else result.stderr)


if __name__ == '__main__':
    main()
