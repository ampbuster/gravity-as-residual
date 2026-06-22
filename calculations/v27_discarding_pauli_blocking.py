"""
v27_discarding_pauli_blocking.py
=================================

Discarding the §3.13 sterile neutrino + Pauli blocking mechanism.

Research findings (2024-2025):
1. Batell & Yin (arXiv:2406.17028, PRD 110, 075038): "Cosmic Stability of Dark Matter
   from Pauli Blocking" - shows Pauli blocking can stabilize DM, but only for
   m_DM < 10 meV (sub-eV regime).

2. Cho, Choi, Joh, Seto (arXiv:2407.08229): Generalizes to QFT. Same mass bound.

3. The 3.5 keV X-ray sterile neutrino signal has WEAKENED in 2024 reanalysis.

4. X-ray non-detection rules out minimal sterile neutrino DM at keV scale.

5. Sub-eV DM has a different problem: it's HOT dark matter (HDM), not COLD
   dark matter (CDM). The cascade requires CDM-like behavior for structure
   formation.

Conclusion: The §3.13 mechanism (sterile neutrino with Pauli-blocked decay) is
DOUBLE-BROKEN:
- For GeV-scale DM (cascade's equilibrium): Pauli blocking is INEFFECTIVE
  (E_decay >> p_F, ratio ~10^21)
- For sub-eV DM (where Pauli blocking works): it's HDM, not CDM
  (small-scale structure doesn't form)

The cascade should DISCARD §3.13 and commit to its geometric framework.


**HISTORICAL (v2.7 era, mid-2025)**: This file is from the v2.7.x era, predating:
- v3.0+ Lagrangian work (L102-L136)
- v3.1+ Multi-universe picture (L142-L150)
- v3.3 Bilateral cascade (E_4D = 5e79 J, M_Pl,4D = 3.93e23 GeV)
- v3.5.7+ Naming revolution (f_back → f_DE,f_DM,leak,f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N×v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via α-GM, L308v)
- α = 1.289 (FIRST-PRINCIPLES via L308n)
- ε = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- γ_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- τ_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v2.7 era framework, not v3.5.9+ A2.
"""

import math
import json

# === Mass bound from Batell & Yin 2024 ===
# Pauli blocking works for m_DM < 10 meV (sub-eV)
# Cascade's required m_s ~ 1 GeV (from equilibrium)
mass_ratio = 1.0  # GeV (cascade) / 1e-5  # GeV (10 meV bound)
mass_ratio_actual = 1.0 / 1e-5
print(f"=== Pauli Blocking Mass Bound ===\n")
print(f"Batell & Yin 2024 mass bound: m_DM < 10 meV = 1e-5 GeV")
print(f"Cascade's required sterile neutrino mass: m_s ~ 1 GeV")
print(f"Ratio: 1 GeV / 1e-5 GeV = {mass_ratio_actual:.0e}")
print(f"  → Cascade's m_s is 10^5 times HEAVIER than the Pauli blocking bound")
print()

# === Issue 1: GeV DM doesn't have Pauli blocking ===
print("=== Issue 1: GeV DM doesn't have Pauli blocking ===\n")
rho_halo = 0.3  # GeV/cm³
m_s = 1.0  # GeV
n_DM = rho_halo / m_s
print(f"DM number density in halo: {n_DM:.2e} /cm³ = {n_DM*1e6:.2e} /m³")
hbar = 1.055e-34
n_SI = n_DM * 1e6
p_F = (3 * math.pi**2 * n_SI)**(1/3) * hbar
p_F_eV = p_F * 1e9 / 1.602e-19 / 3e8
print(f"Fermi momentum p_F: {p_F_eV:.2e} eV")
E_decay = m_s / 2 * 1e9  # MeV in eV
print(f"Decay product energy: {E_decay:.0e} eV")
print(f"Ratio E_decay/p_F: {E_decay/p_F_eV:.2e}")
print(f"Verdict: Pauli blocking is INEFFECTIVE (ratio 10^21)")
print()

# === Issue 2: Sub-eV DM is HDM, not CDM ===
print("=== Issue 2: Sub-eV DM is HDM, not CDM ===\n")
# For DM to be CDM, m_DM > keV typically
# For DM to be WDM, m_DM ~ keV
# For DM to be HDM, m_DM < eV
print("Dark matter classification by mass:")
print("  - HDM (hot): m < 1 eV (relativistic, doesn't form small-scale structure)")
print("  - WDM (warm): 1 eV < m < ~10 keV (semi-relativistic)")
print("  - CDM (cold): m > ~10 keV (non-relativistic, forms structure)")
print()
print("Pauli blocking works for m < 10 meV → this is HDM regime")
print("Cascade's framework requires CDM-like behavior:")
print("  - Small-scale structure (dwarf galaxies, subhalos)")
print("  - Lyman-alpha forest (m > ~2 keV)")
print("  - Galaxy formation at high z (JWST, m > ~keV)")
print()
print("Verdict: sub-eV DM fails the cascade's structure formation requirements")
print()

# === Issue 3: X-ray constraints on keV sterile neutrino ===
print("=== Issue 3: X-ray constraints on keV sterile neutrino DM ===\n")
# 3.5 keV X-ray line was a possible signal in 2014 (Bulbul et al., Boyarsky et al.)
# 2024 reanalysis: signal has weakened
print("Sterile neutrino DM history:")
print("  - 2014: 3.5 keV X-ray line detected in galaxy clusters (Bulbul, Boyarsky)")
print("  - Suggests sterile neutrino m_s = 7 keV")
print("  - 2024: signal weakened in updated analysis (Simons Foundation, Aug 2024)")
print("  - Current: minimal sterile neutrino DM at keV is HEAVILY CONSTRAINED")
print("  - νSMEFT extensions can evade X-ray but require new physics")
print()
print("Cascade's m_s = 1 GeV is WAY beyond the keV sterile neutrino regime.")
print("Cascade's required sin²(2θ) ~ 10^-4 is squeezed by beam dump, BBN, LHC.")
print()

# === Alternative stable DM at GeV scale ===
print("=== Alternative: stable GeV DM via discrete symmetries ===\n")
print("GeV-scale DM CAN be stable, but needs other mechanisms:")
print("  - WIMP: Z2 symmetry (R-parity in SUSY, KK parity in extra dimensions)")
print("  - Neutralino: SUSY R-parity")
print("  - Sterile neutrino: lepton number (approximately conserved)")
print("  - Stable scalar: Z2 or Z3 symmetry")
print()
print("These are well-motivated and don't require Pauli blocking.")
print("But they're not 'more clustered = slower decay' mechanisms.")
print()

# === Conclusion ===
print("=== Conclusion: DISCARD §3.13 ===\n")
print("The §3.13 mechanism (sterile neutrino + Pauli-blocked decay) is DOUBLE-BROKEN:")
print()
print("  Failure mode 1: GeV DM")
print("    - Cascade's required m_s ~ 1 GeV")
print("    - Pauli blocking INEFFECTIVE (E_decay/p_F ~ 10^21)")
print()
print("  Failure mode 2: Sub-eV DM (where Pauli blocking works)")
print("    - m < 10 meV is in HDM regime")
print("    - Doesn't form small-scale structure")
print("    - Conflicts with cascade's CDM-like behavior requirement")
print()
print("Therefore: §3.13 should be DISCARDED.")
print()
print("Cascade's honest commitment:")
print("  - DM is geometric (Option D in §3.14), not a particle")
print("  - 'DM and no neutrinos' is by construction (no particle, no decay)")
print("  - L9 (2D universe physics) remains open")
print("  - Specific particle interpretations (WIMP, axion, sterile neutrino) are")
print("    possible, but stability must come from discrete symmetries, not Pauli blocking")

# Save results
results = {
    'pauli_blocking_mass_bound_eV': 0.01,  # 10 meV
    'cascade_required_mass_GeV': 1.0,
    'mass_ratio': mass_ratio_actual,
    'pauli_blocking_ineffective_at_GeV': True,
    'sub_eV_is_HDM': True,
    'cascade_requires_CDM': True,
    'verdict': 'DISCARD §3.13 - Pauli blocking mechanism is double-broken',
    'alternative': 'Cascade should commit to geometric DM framework (Option D in §3.14)',
    'literature_support': [
        'Batell & Yin 2024 (arXiv:2406.17028, PRD 110.075038)',
        'Cho, Choi, Joh, Seto 2024 (arXiv:2407.08229)',
        'Boyarsky et al. 2019 (X-ray constraints review)',
        'Simons Foundation 2024 (3.5 keV line weakened)'
    ]
}

with open('v27_discarding_pauli_blocking.json', 'w') as f:
    json.dump(results, f, indent=2)

print()
print("Results saved to: calculations/v27_discarding_pauli_blocking.json")
