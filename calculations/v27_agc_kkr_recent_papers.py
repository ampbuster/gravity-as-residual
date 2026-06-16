"""
v27_agc_kkr_recent_papers.py
==============================

Research update on AGC 114905 and KKR 25 (June 2026).

KEY FINDINGS:

1. AGC 114905 ("no DM" claim) is CONTESTED in 2022-2025 literature:
   - Mancera Piña+ 2022 (MNRAS 512, 3230): "No trace of DM" — original claim
   - Sellwood 2022 (MNRAS, stac1604): "AGC 114905 NEEDS DM" — argues original
     analysis underestimates the halo; disc is too stable without DM
   - Mancera Piña+ 2024 (A&A, arXiv:2404.06537): ultra-deep imaging,
     inclination 31±2°, MOND does not fit, CDM needs unusual halo,
     SIDM/FDM remain feasible
   - Afruni+ 2025 (MNRAS 538, 60, arXiv:2502.08717): AGC 114905 can
     evolve in low-density halos that challenge ΛCDM

2. KKR 25: NO new observations found in 2024-2026 literature
   - The 2012 Makarov paper remains the only detailed study
   - Still no published velocity dispersion

3. The cascade's AGC 114905 entry (M_dyn/M_b ~ 1.36) may be:
   - Right (per Mancera Piña 2022)
   - Too low (per Sellwood 2022)
   - Even more uncertain (per Mancera Piña 2024 inclination analysis)

4. The cascade's bifurcation with KKR 25 is now MUCH less certain:
   - Both galaxies have uncertain M_dyn/M_b
   - AGC 114905 may have more DM than the cascade assumed
   - KKR 25's M_dyn is estimated, not measured
   - The "0.7-3×" bifurcation may be even smaller

This is a positive development for the cascade in some ways:
- The cascade's geometric DM is similar to SIDM/FDM (which 2024-2025
  papers find more viable than CDM for AGC 114905)
- The cascade doesn't require "usual" CDM halos
- The cascade can accommodate the unusual halo properties

But the bifurcation story is now even weaker:
- AGC 114905 has uncertain DM content
- KKR 25 has no measured σ
- The "820×" was a numerical error
- The "0.7-3×" is an estimate
- The actual bifurcation may be even smaller (1-2×)
"""

import json

# Summary of recent papers
print("=== §3.29: Recent papers on AGC 114905 and KKR 25 (v2.7.35+) ===\n")

print("AGC 114905 literature (2012-2025):\n")
papers_agc = [
    {
        'year': 2022,
        'authors': 'Mancera Piña et al.',
        'journal': 'MNRAS 512, 3230',
        'arxiv': '2110.00014',
        'finding': 'No trace of dark matter in AGC 114905',
        'cascade_impact': 'Original "no DM" claim, M_dyn/M_b ~ 1.36'
    },
    {
        'year': 2022,
        'authors': 'Sellwood',
        'journal': 'MNRAS (stac1604)',
        'arxiv': '2206.04609',
        'finding': 'AGC 114905 NEEDS dark matter',
        'cascade_impact': 'Counter-paper: disc is too stable without DM, original analysis underestimates halo'
    },
    {
        'year': 2024,
        'authors': 'Mancera Piña, Golini, Trujillo, Montes',
        'journal': 'A&A',
        'arxiv': '2404.06537',
        'finding': 'Ultra-deep imaging, inclination 31±2°; MOND does not fit; CDM needs unusual halo; SIDM/FDM remain feasible',
        'cascade_impact': 'Confirms unusual halo, M_dyn/M_b uncertain'
    },
    {
        'year': 2025,
        'authors': 'Afruni, Marinacci, Mancera Piña, Fraternali',
        'journal': 'MNRAS 538, 60',
        'arxiv': '2502.08717',
        'finding': 'AGC 114905 can evolve in low-density halos that challenge ΛCDM',
        'cascade_impact': 'Supports unusual halo, consistent with cascade geometric DM'
    },
]

for p in papers_agc:
    print(f"  {p['year']} {p['authors']} ({p['journal']}):")
    print(f"    Finding: {p['finding']}")
    print(f"    Cascade impact: {p['cascade_impact']}")
    print()

print("KKR 25 literature (2012-2025):\n")
print("  2012 Makarov et al. (MNRAS 425, 709): 'A unique isolated dSph at D=1.9 Mpc'")
print("    Finding: original photometric and spectroscopic study")
print("    Cascade impact: source of all KKR 25 data used by cascade")
print()
print("  2024-2025: NO new observations found in literature search")
print("    Cascade impact: KKR 25's M_dyn is still estimated, not measured")
print()

print("=== What this means for the cascade ===\n")
print("1. AGC 114905 DM content is CONTESTED")
print("   - Mancera Piña 2022: no DM, M_dyn/M_b ~ 1.36")
print("   - Sellwood 2022: needs DM, M_dyn/M_b > 1.36")
print("   - Mancera Piña 2024: uncertain, unusual halo")
print("   - Afruni 2025: unusual low-density halo, OK for non-CDM")
print()

print("2. KKR 25 DM content is ESTIMATED, not measured")
print("   - No velocity dispersion published")
print("   - M_dyn/M_b ~ 1-4 is a range based on assumed σ")
print()

print("3. The cascade's bifurcation is now WEAKER than v2.7.33+ claimed")
print("   - Old claim: 820× → 219× (numerical error, fixed)")
print("   - v2.7.33+ claim: 0.7-3× (estimate)")
print("   - v2.7.35+ reality: maybe 1-2× (AGC 114905 may have more DM than assumed)")
print()

print("4. POSITIVE for the cascade:")
print("   - AGC 114905's unusual halo is HARD for standard CDM")
print("   - SIDM/FDM (similar to cascade's geometric DM) remain feasible")
print("   - The cascade doesn't need 'usual' halos")
print("   - AGC 114905 is no longer a 'DM-free' anomaly for the cascade")
print()

print("5. L40 added: AGC 114905 DM content is contested in 2022-2025 literature")
print("   L41 added: KKR 25 has no new observations in 2024-2026")
print("   L42 added: Cascade's bifurcation is now even more uncertain")
print()

print("=== Recommendations ===\n")
print("- Cascade's §4.45 / §4.46 should reference the contested status of AGC 114905")
print("- Cascade's bifurcation should be re-cast as 'qualitative direction' only")
print("- L40-42 added to the limitations table")
print("- Future work: get KKR 25 σ, get AGC 114905 inclination re-measured")

results = {
    'agc_114905_status': 'DM content CONTESTED in 2022-2025 literature',
    'kkr_25_status': 'No new observations since 2012',
    'cascade_bifurcation_status': 'Even more uncertain (0.7-3× → 1-2×)',
    'positive_for_cascade': 'AGC 114905 unusual halo is hard for CDM, easy for cascade',
    'papers': papers_agc,
}

with open('v27_agc_kkr_recent_papers.json', 'w') as f:
    json.dump(results, f, indent=2)

print()
print("Results saved to: calculations/v27_agc_kkr_recent_papers.json")
