#!/usr/bin/env python3
"""
RAR across mass scales (v2)

Updated with 2024-2025 observations:
- EDGE 2025 (Júlio+): Low-mass dwarf galaxies (M_bar ~ 10^4-10^7.5 M_sun) lie
  SYSTEMATICALLY ABOVE the low-mass extrapolation of the McGaugh+2016 RAR.
  Conclusion: "the RAR does not apply to low-mass dwarf galaxies"
- Tian+ 2024: BCG-cluster RAR has a 17x LARGER acceleration scale than the galaxy RAR.
  Conclusion: BCGs and clusters follow a DISTINCT RAR.
- DESI 2024-2025: Hints of time-varying dark energy (w != -1)

The cascade's prediction for g_+ across mass scales:
  g_+_cascade = (3/4) * G * f_cumulative * M_DM / (pi * R_halo^2)
  
  This depends on M_DM/R^2, which is SMALLER for both dwarfs and clusters
  (since M_DM is much smaller/larger, but R^2 doesn't scale the same way).
  
  The cascade predicts:
  - Galaxies (M_DM ~ 1e12, R ~ 30 kpc): g_+ ~ 2.6e-11 m/s^2 (~0.22x empirical)
  - Dwarfs (M_DM ~ 1e9, R ~ 5 kpc): g_+ ~ 9e-13 m/s^2 (much smaller)
  - Clusters (M_DM ~ 1e14, R ~ 500 kpc): g_+ ~ 9e-12 m/s^2 (smaller, not 17x larger!)
  
The empirical data:
  - Galaxies: g_+ ~ 1.2e-10 m/s^2 (McGaugh+ 2016)
  - Dwarfs: ABOVE the RAR extrapolation (EDGE 2025)
  - Clusters: g_+ ~ 17x larger (Tian+ 2024)

Conclusion:
  - The cascade's g_+ is in the right ballpark for galaxies (~0.22x off)
  - For dwarfs: cascade predicts very small g_+, but EDGE shows dwarfs have MORE DM
    than the standard RAR predicts. The cascade UNDER-predicts the dwarf DM.
  - For clusters: cascade predicts SMALLER g_+ than galaxies, but Tian+ shows
    clusters have 17x LARGER g_+. The cascade UNDER-predicts the cluster g_+.
  - The cascade's g_+ scaling is wrong at both extremes of mass.

Implication:
  - The cascade is consistent with the galaxy-scale RAR (within a factor of 5)
  - The cascade's g_+ scaling (g_+ ~ M_DM/R^2) needs modification to match
    the empirical scaling across mass scales.
  - A specific implementation of the cascade would need to add additional
    physics at dwarf and cluster scales (e.g., baryonic feedback, ICM physics)
    to match the full range of observations.
"""

import math

G = 6.674e-11  # m^3/kg/s^2
M_sun = 1.989e30  # kg
kpc_to_m = 3.086e19  # m/kpc

# Cascade prediction
f_cum = 0.7

def g_plus_cascade(M_DM_Msun, R_halo_kpc):
    """Cascade prediction for g_+"""
    M = M_DM_Msun * M_sun
    R = R_halo_kpc * kpc_to_m
    return (3/4) * G * f_cum * M / (math.pi * R**2)

# Empirical values
g_plus_McGaugh = 1.2e-10  # galaxies (McGaugh+ 2016)
g_plus_Tian_cluster = 17 * g_plus_McGaugh  # clusters (Tian+ 2024, 17x larger)
# For dwarfs, EDGE 2025 says they lie ABOVE the RAR extrapolation
# The "effective g_+" for dwarfs is higher than the galaxy g_+
# Quantitatively, dwarfs at fixed g_bar have HIGHER g_obs
# This implies the dwarfs are on a RAR with a HIGHER g_+

print("=" * 80)
print("RAR g_+ ACROSS MASS SCALES: CASCADE vs OBSERVATIONS")
print("=" * 80)
print()
print("Cascade prediction: g_+ = (3/4) * G * f_cumulative * M_DM / (pi * R_halo^2)")
print()
print(f"  {'Object':<20s} {'M_DM (M_sun)':>15s} {'R (kpc)':>10s} {'g_+ cascade':>15s} {'g_+ obs':>15s} {'ratio':>8s}")
print("  " + "-"*95)

# Galaxy scales
for name, M, R in [
    ('Dwarf (EDGE 2025)', 1e9, 5),
    ('Small spiral', 1e10, 10),
    ('Milky Way', 1e12, 30),
    ('Large spiral', 5e12, 50),
    ('Cluster (Tian 2024)', 1e14, 500),
    ('Supercluster', 1e15, 3000),
]:
    g_cas = g_plus_cascade(M, R)
    
    # Empirical
    if 'Dwarf' in name:
        g_obs = g_plus_McGaugh  # EDGE: dwarfs above RAR -> higher effective g_+
        obs_note = "> galaxy g_+"
    elif 'Cluster' in name or 'Supercluster' in name:
        g_obs = g_plus_Tian_cluster
        obs_note = "17x galaxy"
    else:
        g_obs = g_plus_McGaugh
        obs_note = "1.2e-10"
    
    ratio = g_cas / g_obs
    print(f"  {name:<20s} {M:>15.2e} {R:>10.0f} {g_cas:>15.3e} {g_obs:>15.3e} {ratio:>8.2f}")

print()
print("=" * 80)
print("INTERPRETATION")
print("=" * 80)
print()
print("1. Galaxy scale (Milky Way-like):")
print("   Cascade g_+ = 2.6e-11, empirical = 1.2e-10. Ratio: 0.22x")
print("   CASCADE IS IN THE RIGHT BALLPARK (within a factor of 5)")
print()
print("2. Dwarf scale (M_DM ~ 1e9 M_sun, EDGE 2025):")
print("   Cascade g_+ = 9.3e-13, empirical g_+ (effective) > 1.2e-10")
print("   CASCADE UNDER-PREDICTS DWARF g_+ by ~100x")
print("   The cascade says dwarfs have very small g_+, but EDGE shows")
print("   dwarfs have MORE DM than the standard RAR predicts.")
print()
print("3. Cluster scale (M_DM ~ 1e14 M_sun, Tian+ 2024):")
print("   Cascade g_+ = 9.3e-12, empirical g_+ = 2.0e-9 (17x galaxy g_+)")
print("   CASCADE UNDER-PREDICTS CLUSTER g_+ by ~200x AND IN THE WRONG DIRECTION")
print("   The cascade predicts g_+ decreases with mass, but empirically it INCREASES")
print()
print("4. The cascade's g_+ scaling (g_+ ~ M_DM/R^2) is wrong at both ends of the mass spectrum.")
print("   This is a meaningful test of the cascade that should be documented.")
print()
print("=" * 80)
print("CAVEATS AND HONEST ACKNOWLEDGMENTS")
print("=" * 80)
print()
print("1. The cascade's g_+ is a first-order calculation. A more sophisticated")
print("   implementation might include baryonic feedback, ICM physics, or other")
print("   effects that modify g_+ at extreme mass scales.")
print()
print("2. The empirical cluster g_+ (Tian+ 2024) is from gravitational LENSING,")
print("   not kinematics. The kinematic vs lensing RAR may differ.")
print()
print("3. The EDGE 2025 dwarfs are LOW-MASS (M_bar ~ 1e4-1e7 M_sun), much smaller")
print("   than the SPARC range (M_bar ~ 1e8-1e11 M_sun). The cascade's simple")
print("   picture may need modification for these ultra-low-mass systems.")
print()
print("4. The 5/27/68 split is 4D-event-specific, not derived from first principles.")
print("   The cascade's 30/70 active/cumulative split is a postulate.")
print()
print("5. The 70% cumulative-return assumption might be wrong for clusters and dwarfs.")
print("   If clusters have a HIGHER active fraction (because they have more activity),")
print("   the g_+ would be different. This is a parameter the cascade can adjust.")

