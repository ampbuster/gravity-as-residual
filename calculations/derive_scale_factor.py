#!/usr/bin/env python3
"""
Derive the mass-dependent scale factor (cascade M_halo / empirical M_halo).

Empirically (commits 117-118): scale = 0.1 for MW, scale = 0.7 for cluster.
This means the cascade's intrinsic M_halo is 10% of empirical for MW,
70% of empirical for cluster.

HYPOTHESIS: the empirical M_halo is INFLATED by baryonic effects:
- In galaxies: gas pressure, stellar feedback, non-circular motions,
  triaxiality all contribute to overestimating the true M_halo
- In clusters: baryons are a smaller fraction of total mass, less
  inflation, empirical M_halo closer to true

Let me test this hypothesis by computing the expected inflation factor.
"""

import math

print("=" * 80)
print("DERIVE MASS-DEPENDENT SCALE FACTOR")
print("=" * 80)
print()

# Empirical: scale = 0.1 for MW, 0.7 for cluster
# Inflation factor = 1/scale
# MW: 1/0.1 = 10x inflation
# Cluster: 1/0.7 = 1.4x inflation

# Baryonic fraction
# Galaxy: f_b = M_baryons / M_total ~ 0.05
# Cluster: f_b = M_baryons / M_total ~ 0.01-0.02

# Inflation mechanism:
# In a galaxy, the gas + stars contribute to the rotation curve
# If they're not in equilibrium (e.g., turbulent gas), they can
# artificially boost v_circ

# Simple model: v_circ_observed^2 = v_circ_DM^2 + v_circ_baryon^2 + v_circ_turbulent^2
# 
# If gas is turbulent, v_turb^2 ~ 3 * c_s^2 (sound speed squared)
# For molecular clouds: c_s ~ 1 km/s, so v_turb ~ 1.7 km/s
# For MW rotation: v_circ ~ 220 km/s
# v_turb^2 / v_circ^2 = (1.7/220)^2 ~ 6e-5 (negligible)
# 
# Hmm that's not enough to explain 10x inflation
# 
# Let me think differently
# 
# The empirical M_halo is what you get from rotation curve fitting
# It includes ALL the mass that contributes to v_circ
# 
# In a galaxy: M_halo = M_DM + M_baryons (stars + gas)
# In a cluster: M_halo = M_DM + M_baryons (galaxies + ICM gas)
# 
# The cascade predicts M_DM_cascade (cumulative 2D universe gravity)
# 
# The empirical M_halo includes:
# - M_DM_cascade (cumulative 2D universe gravity)
# - M_baryons (stars, gas, etc.)
# - M_other (anything else that contributes to v_circ)
# 
# In a galaxy, the "M_other" might include:
# - Modified gravity effects at low accelerations
# - Primordial black holes
# - Other DM components
# 
# In a cluster, "M_other" is less:
# - Less modified gravity (DE is more important)
# - Fewer PBHs (formed in early universe, distributed differently)
# - Other DM is just DM

# Actually, the simplest interpretation:
# The cascade's M_halo is the "true" DM mass
# The empirical M_halo = M_true + M_extras
# 
# M_extras is mass that's NOT part of the cascade's 2D universe gravity
# In galaxies, M_extras is large (10x M_true)
# In clusters, M_extras is small (1.4x M_true)
# 
# What could M_extras be?
# 1. Primordial black holes (more in galaxies than clusters)
# 2. Modified gravity contribution (more important at low g)
# 3. A second DM component (WIMPs, axions, etc.)
# 
# The cascade explicitly says "all DM is cumulative 2D universe gravity"
# If this is wrong (i.e., there's ALSO a particle DM component), then
# the empirical M_halo = M_2D_universe + M_particle
# 
# For MW: M_2D_universe / M_empirical = 0.1, so 90% is M_particle
# For cluster: M_2D_universe / M_empirical = 0.7, so 30% is M_particle
# 
# This is a specific prediction: the cascade's 2D universe gravity is
# a MINORITY component of DM in galaxies and a MAJORITY in clusters.
# 
# Testable? Maybe. If the cascade's 2D universe gravity has specific
# properties (e.g., follows the 1/r isothermal profile), then we can
# look for the additional particle DM component as a different
# spatial distribution.

# Let me compute the "missing DM" fraction
print("Missing DM fraction (1 - scale):")
print("  MW: 1 - 0.1 = 0.9 (90% missing)")
print("  Cluster: 1 - 0.7 = 0.3 (30% missing)")
print()

# This is significant! 90% of MW's DM is unaccounted for by the cascade
# 30% of cluster's DM is unaccounted for
# 
# Possible explanations:
# 1. Particle DM (WIMPs, axions, etc.) - the standard explanation
# 2. Modified gravity (MOND-like) - more important at galaxy scale
# 3. Primordial black holes - more in galaxies than clusters
# 4. Some combination

# Let me see if the ratio 90%/30% = 3x correlates with anything
# - kappa ratio: 100/17 = 5.9 (cluster/MW)
# - baryon fraction ratio: 0.05/0.015 = 3.3 (galaxy/cluster)
# - dynamical time ratio: 0.2 Gyr / 1 Gyr = 0.2

# Hmm
# 3x missing DM (galaxy/cluster)
# 5.9x kappa (cluster/galaxy)
# 3.3x baryon fraction (galaxy/cluster)

# Maybe: missing_DM ∝ 1/kappa
# 1/kappa(MW) = 1/17 = 0.059
# 1/kappa(cluster) = 1/100 = 0.01
# 0.059/0.01 = 5.9

# Scale ∝ 1/kappa^(-1) = kappa^(-1)?
# scale(MW) = 0.1 ≈ 1/kappa(MW) * 1.7 = 0.059 * 1.7
# scale(cluster) = 0.7 ≈ 1/kappa(cluster) * 70 = 0.01 * 70

# Hmm doesn't quite work

# Let me try: scale ∝ kappa^2
# scale(MW) = 0.1, kappa^2 = 289, 0.1/289 = 3.5e-4
# scale(cluster) = 0.7, kappa^2 = 10000, 0.7/10000 = 7e-5
# Different constants, not constant

# Or: scale ∝ log(kappa) or something
# log(kappa(MW)) = log(17) = 2.83
# log(kappa(cluster)) = log(100) = 4.61
# ratio: 1.63

# Hmm

# Let me just check if scale correlates with the central density
# For a halo: rho_c ∝ M_halo / R_halo^3
# MW: 1e12 / 30^3 = 3.7e7
# Cluster: 1e14 / 500^3 = 8e3
# ratio: 4.6e3 (galaxy/cluster)

# So central density ratio is HUGE
# Scale ratio is 0.1/0.7 = 0.14
# So scale ratio is 1/central_density_ratio^?

# Hmm
# log(0.14) = -1.97
# log(4.6e3) = 8.4
# Different scales

# Maybe scale ∝ 1/sqrt(rho_c) (?)
# 1/sqrt(3.7e7) = 1.6e-4
# 1/sqrt(8e3) = 1.1e-2
# ratio: 1.4e-2 / 1.6e-4 = 70
# So scale(cluster)/scale(MW) = 7 (from data)
# 70 != 7

# Let me try a different relationship
# scale ∝ M_halo^(some power)
# 0.1 / 1e12 = 1e-13
# 0.7 / 1e14 = 7e-15
# ratio: 7e-15/1e-13 = 0.07
# So scale/M_halo ratio is 0.07 for cluster, 1e-13 for MW
# Hmm

# Let me just tabulate some values and look for patterns
print("TABLE OF PARAMETERS:")
print()
print("  Object      M_halo    R_halo    kappa    scale    1/scale    baryon_frac    central_rho")
print("  " + "-" * 95)
objects = [
    ('MW', 1e12, 30, 17, 0.1, 10, 0.05, 3.7e7),
    ('Cluster', 1e14, 500, 100, 0.7, 1.4, 0.015, 8e3),
]
for name, M, R, kappa, scale, inv, bf, rho_c in objects:
    print(f"  {name:<10s}  {M:>10.1e}  {R:>6.0f}  {kappa:>5.1f}  {scale:>5.2f}  {inv:>5.2f}  {bf:>10.3f}  {rho_c:>10.2e}")

print()
print("LOOKING FOR PATTERNS:")
print()
# Ratio of (cluster/MW) for various quantities
# M_halo: 100
# R_halo: 16.7
# kappa: 5.9
# scale: 7
# 1/scale: 0.14
# baryon_frac: 0.3
# central_rho: 0.00022

# Pattern: scale(MW)/scale(cluster) = 0.14 ≈ 1/7
# kappa(cluster)/kappa(MW) = 5.9
# These are CLOSE but not identical

# Maybe: scale ∝ kappa^0.7 or similar
# log(7)/log(5.9) = 1.95/1.77 = 1.1
# So scale ∝ kappa^1.1
# Check: 17^1.1 = 24.3, 100^1.1 = 158
# scale(MW) = 0.1, scale(cluster) = 0.7
# 0.7/0.1 = 7
# 158/24.3 = 6.5
# Close! But not exact

# So scale ∝ kappa^1.1 is a reasonable approximation
# This is a specific prediction that could be tested

# Let me check more carefully
# scale(MW) = 0.1 = A * 17^1.1
# A = 0.1 / 24.3 = 0.00411
# scale(cluster) = 0.00411 * 100^1.1 = 0.00411 * 158 = 0.65
# 0.65 vs 0.7 - close!

# So scale ∝ kappa^1.1 is a good approximation
# This is a DERIVABLE relationship if kappa^1.1 comes from cascade physics

# Why kappa^1.1?
# Hmm not obvious
# Maybe it's a coincidence
# Or maybe there's a specific cascade reason

print("Possible relationship: scale ∝ kappa^1.1")
print(f"  For MW: scale = A * kappa^1.1 = 0.00411 * 17^1.1 = {0.00411 * 17**1.1:.3f} (data: 0.1)")
print(f"  For cluster: scale = A * kappa^1.1 = 0.00411 * 100^1.1 = {0.00411 * 100**1.1:.3f} (data: 0.7)")
print()
print("The relationship scale ∝ kappa^1.1 fits the data to ~10% precision")
print("This is a testable prediction of the cascade.")
print()
print("WHY kappa^1.1? Possible physical reasons:")
print("  - Cascade's M_halo ∝ kappa * (something with kappa^0.1)")
print("  - The 'something' might be a cascade-specific efficiency factor")
print("  - Or a coincidence with another physics parameter")
print()
print("This is a CANDIDATE relationship, not a derivation.")
print("A specific implementation would need to derive kappa^1.1 from cascade dynamics.")
